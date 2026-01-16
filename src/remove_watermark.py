import os, cv2, threading, time
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
from tkinterdnd2 import TkinterDnD, DND_FILES

# ================= APP INFO =================
APP_NAME = "Bulk Watermark Removal"
APP_VERSION = "2.5.0"

WM_W, WM_H = 0.26, 0.18

POSITION_MAP = {
    "top_left":     lambda w, h, ww, hh: (0, 0),
    "top_right":    lambda w, h, ww, hh: (w - ww, 0),
    "bottom_left":  lambda w, h, ww, hh: (0, h - hh),
    "bottom_right": lambda w, h, ww, hh: (w - ww, h - hh),
}

# ================= WINDOW CENTER HELPER =================
def center_window(win, parent=None, width=None, height=None):
    win.update_idletasks()
    w = width or win.winfo_width()
    h = height or win.winfo_height()

    if parent:
        x = parent.winfo_rootx() + (parent.winfo_width() // 2) - (w // 2)
        y = parent.winfo_rooty() + (parent.winfo_height() // 2) - (h // 2)
    else:
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)

    win.geometry(f"{w}x{h}+{x}+{y}")

# ================= APP =================
class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.files = []
        self.masks = []

        self.pos_var = tk.StringVar(value="top_right")
        self.preview_img = None

        # progress
        self.pwin = None
        self.pbar = None
        self.plabel = None
        self.start_time = None

        self.title(f"{APP_NAME} v{APP_VERSION}")
        self.minsize(1100, 680)

        self.build_ui()
        center_window(self)

    # ================= UI =================
    def build_ui(self):
        main = ttk.Frame(self)
        main.pack(fill="both", expand=True, padx=10, pady=10)

        # LEFT PANEL
        left = ttk.LabelFrame(main, text="Images")
        left.pack(side="left", fill="both", expand=True)

        table_frame = ttk.Frame(left)
        table_frame.pack(fill="both", expand=True)

        self.table = ttk.Treeview(
            table_frame, columns=("No", "File"), show="headings"
        )
        self.table.heading("No", text="No")
        self.table.heading("File", text="File")
        self.table.column("No", width=50, anchor="center")
        self.table.column("File", width=600, anchor="w")

        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=self.table.xview)
        self.table.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.table.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        self.table.bind("<<TreeviewSelect>>", self.on_select)
        self.table.drop_target_register(DND_FILES)
        self.table.dnd_bind("<<Drop>>", self.on_drop)

        ttk.Button(left, text="Clear Table", command=self.clear_all)\
            .pack(fill="x", pady=4)

        # RIGHT PANEL
        right = ttk.LabelFrame(main, text="Preview & Controls")
        right.pack(side="right", fill="y", padx=8)

        self.preview = ttk.Label(right)
        self.preview.pack(fill="both", expand=True, pady=6)

        ttk.Label(right, text="Watermark Position").pack(pady=(6, 2))
        for p in POSITION_MAP:
            ttk.Radiobutton(
                right, text=p.replace("_", " ").title(),
                variable=self.pos_var, value=p,
                command=self.update_preview_overlay
            ).pack(anchor="w")

        ttk.Button(right, text="Add Freehand Markup",
                   command=self.add_freehand_mask).pack(fill="x", pady=6)

        ttk.Button(right, text="Clear Freehand Markup",
                   command=self.clear_masks).pack(fill="x", pady=2)

        ttk.Button(right, text="START",
                   command=self.start_processing).pack(fill="x", pady=12)

    # ================= PREVIEW =================
    def on_select(self, _):
        sel = self.table.selection()
        if sel:
            self.show_preview(self.files[self.table.index(sel[0])])

    def show_preview(self, path):
        img = Image.open(path).convert("RGBA")
        w, h = img.size

        overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        # preset overlay
        ww, hh = int(WM_W * w), int(WM_H * h)
        x, y = POSITION_MAP[self.pos_var.get()](w, h, ww, hh)
        draw.rectangle([x, y, x + ww, y + hh], fill=(255, 0, 0, 80))

        # freehand overlay
        for m in self.masks:
            ov = m.convert("RGBA")
            ov.putalpha(120)
            overlay = Image.alpha_composite(overlay, ov)

        img = Image.alpha_composite(img, overlay)
        img.thumbnail((420, 420))

        self.preview_img = ImageTk.PhotoImage(img)
        self.preview.config(image=self.preview_img)

    def update_preview_overlay(self):
        if self.files:
            self.show_preview(self.files[0])

    # ================= FREEHAND =================
    def add_freehand_mask(self):
        img = Image.open(self.files[0]).convert("RGB")
        w, h = img.size

        win = tk.Toplevel(self)
        win.title("Freehand Markup")
        center_window(win, self)

        canvas = tk.Canvas(win, width=w, height=h)
        canvas.pack()

        win.tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=win.tk_img)

        mask = Image.new("L", (w, h), 0)
        draw = ImageDraw.Draw(mask)

        brush = tk.IntVar(value=20)
        last = None

        def paint(e):
            nonlocal last
            if last:
                draw.line((last[0], last[1], e.x, e.y),
                          fill=255, width=brush.get())
                canvas.create_line(
                    last[0], last[1], e.x, e.y,
                    fill="red", width=brush.get()
                )
            last = (e.x, e.y)

        def reset(_):
            nonlocal last
            last = None

        def clear_canvas():
            canvas.delete("all")
            canvas.create_image(0, 0, anchor="nw", image=win.tk_img)
            draw.rectangle((0, 0, w, h), fill=0)

        def save():
            if np.array(mask).max() > 0:
                self.masks.append(mask.copy())
            win.destroy()
            self.update_preview_overlay()

        ttk.Label(win, text="Brush Size").pack()
        ttk.Scale(win, from_=5, to=60,
                  orient="horizontal", variable=brush).pack(fill="x", padx=10)

        ttk.Button(win, text="Clear Drawing",
                   command=clear_canvas).pack(fill="x", pady=4)
        ttk.Button(win, text="Done",
                   command=save).pack(fill="x", pady=6)

        canvas.bind("<B1-Motion>", paint)
        canvas.bind("<ButtonRelease-1>", reset)

    def clear_masks(self):
        self.masks.clear()
        self.update_preview_overlay()

    # ================= PROCESS =================
    def start_processing(self):
        if not self.files:
            messagebox.showerror("Error", "No images added")
            return

        self.show_progress(len(self.files))
        threading.Thread(target=self.process_images, daemon=True).start()

    def show_progress(self, total):
        self.pwin = tk.Toplevel(self)
        self.pwin.title("Processing")
        center_window(self.pwin, self, 360, 140)

        ttk.Label(self.pwin, text="Processing Images...").pack(pady=(10, 4))
        self.pbar = ttk.Progressbar(self.pwin, length=300)
        self.pbar.pack(padx=20, pady=6)
        self.plabel = ttk.Label(self.pwin, text="Starting...")
        self.plabel.pack(pady=(0, 10))

        self.start_time = time.time()
        self.total_images = total

    def update_progress(self, done):
        elapsed = time.time() - self.start_time
        eta = int((elapsed / max(done, 1)) * (self.total_images - done))
        self.pbar["value"] = (done / self.total_images) * 100
        self.plabel.config(
            text=f"{done}/{self.total_images} | ETA: {eta}s"
        )

    def process_images(self):
        processed = 0
        for path in self.files:
            img = cv2.imread(path)
            h, w = img.shape[:2]

            final_mask = np.zeros((h, w), np.uint8)

            for m in self.masks:
                final_mask |= np.array(m.resize((w, h), Image.NEAREST))

            if final_mask.max() == 0:
                ww, hh = int(WM_W * w), int(WM_H * h)
                x, y = POSITION_MAP[self.pos_var.get()](w, h, ww, hh)
                final_mask[y:y + hh, x:x + ww] = 255

            final_mask = cv2.GaussianBlur(final_mask, (21, 21), 0)
            result = cv2.inpaint(img, final_mask, 3, cv2.INPAINT_TELEA)
            cv2.imwrite(path, result)

            processed += 1
            self.after(0, lambda d=processed: self.update_progress(d))

        self.after(0, lambda: self.finish_processing(processed))

    def finish_processing(self, processed):
        if self.pwin:
            self.pwin.destroy()

        summary = tk.Toplevel(self)
        summary.title("Summary")
        center_window(summary, self, 320, 180)

        ttk.Label(summary, text="Processing Complete",
                  font=("Segoe UI", 12, "bold")).pack(pady=(12, 6))
        ttk.Label(summary, text=f"Total Images : {self.total_images}").pack()
        ttk.Label(summary, text=f"Processed    : {processed}").pack()

        ttk.Button(summary, text="Close",
                   command=summary.destroy).pack(pady=12)

    # ================= INPUT =================
    def on_drop(self, event):
        for p in self.tk.splitlist(event.data):
            if p.lower().endswith((".jpg", ".jpeg", ".png")):
                self.files.append(p)
                self.table.insert(
                    "", "end",
                    values=(len(self.files), os.path.basename(p))
                )

        if self.files:
            self.table.selection_set(self.table.get_children()[0])
            self.show_preview(self.files[0])

    def clear_all(self):
        self.files.clear()
        self.masks.clear()
        self.table.delete(*self.table.get_children())
        self.preview.config(image="")

# ================= RUN =================
if __name__ == "__main__":
    App().mainloop()
