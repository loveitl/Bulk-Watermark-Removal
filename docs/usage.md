# Usage Guide – Bulk Watermark Removal

This guide explains how to use **Bulk Watermark Removal** to remove watermarks from images using preset regions or freehand masking.

---

## 📦 Requirements

Before running the application, ensure the following are installed:

* Python 3.9 or newer
* Required libraries (install once):

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

From the project root directory:

```bash
python src/remove_watermark.py
```

The application window will open centered on your screen.

---

## 🖼 Adding Images

You can add images in two ways:

### 1️⃣ Drag & Drop

* Drag one or more `.jpg`, `.jpeg`, or `.png` files
* Drop them directly into the **Images table**

### 2️⃣ Folder Selection (if enabled in your build)

* Select a folder containing images
* All supported images will be added automatically

➡️ The **first image is auto-selected**, and a preview is shown immediately.

---

## 👁 Understanding the Preview Panel

The preview panel shows:

* The selected image (scaled to fit the preview area)
* A **red transparent overlay** indicating the watermark region

### Overlay Types

* **Preset Overlay** – shows the selected watermark position
* **Freehand Overlay** – shows custom-drawn watermark areas

The preview updates instantly when:

* You change the preset position
* You add or clear freehand markup

---

## 📍 Using Preset Watermark Positions

Preset positions are useful when the watermark location is consistent across images.

Available presets:

* Top Left
* Top Right
* Bottom Left
* Bottom Right

### How presets work

* Presets are applied automatically if **no freehand mask exists**
* If a freehand mask is present, it takes priority over presets

---

## ✍ Freehand Watermark Markup

Use freehand markup when the watermark is irregular or not in a fixed position.

### Steps

1. Click **Add Freehand Markup**
2. A popup editor opens centered on the main window
3. Draw directly over the watermark area using the mouse
4. Adjust **Brush Size** using the slider
5. Click **Clear Drawing** to redraw if needed
6. Click **Done** to save the mask

> Empty drawings are ignored automatically.

---

## 🧹 Clearing Freehand Markup

* Click **Clear Freehand Markup** in the main window
* All saved freehand masks will be removed
* The preview updates immediately

---

## ⏳ Processing Images

### Start Processing

* Click the **START** button
* Processing runs in the background (UI remains responsive)

### Progress Popup

During processing, a popup displays:

* Progress bar
* Number of images processed
* Estimated time remaining (ETA)

---

## 📊 Completion Summary

After processing finishes:

* A summary popup appears
* Shows total images and processed count

Click **Close** to return to the main application.

---

## 🔄 Clearing the Session

Click **Clear Table** to:

* Remove all images from the table
* Clear the preview panel
* Remove all freehand masks

This resets the application to a fresh state.

---

## ⚠️ Notes & Best Practices

* Always review the overlay in the preview before processing
* Use presets for consistent watermark locations
* Use freehand markup for complex or irregular watermarks
* Test on a small batch before processing many images

---

## 🆘 Troubleshooting

**START button not visible?**

* Update to version 2.5.1 or newer

**Watermark not fully removed?**

* Increase freehand coverage
* Combine preset positioning with freehand masks

---

## 📌 Support

If you encounter issues or have feature requests:

* Open an issue on GitHub
* Include screenshots if possible

---

Thank you for using **Bulk Watermark Removal** 🙌
