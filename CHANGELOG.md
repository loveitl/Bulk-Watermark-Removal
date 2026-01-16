# Bulk Watermark Removal

## 🚀 Version 2.5.1 – UI Stability & Workflow Update

This release focuses on **UI stability**, **professional layout behavior**, and **workflow completeness**. It resolves long‑standing preview/layout issues and finalizes the end‑to‑end watermark‑removal experience.

---

## ✨ Key Highlights

### 🪟 Window & Popup Behavior

* Main application **always opens centered on screen**
* All popups (Freehand Editor, Progress, Summary) **open centered relative to the main window**
* No random placement or flickering

---

### 🖼 Image Table Improvements

* Vertical **and horizontal scrollbars** for large file lists
* Handles long filenames gracefully
* **Auto‑selects first image** when images are added
* Preview is shown **automatically** on first load
* **Clear Table** button resets:

  * File list
  * Preview
  * Freehand masks

---

### 👁 Preview Panel (Major UX Fix)

* Preview area now has a **fixed height**
* Large images no longer push UI controls off‑screen
* **START button is always visible**
* Live overlay preview includes:

  * Preset watermark region (red transparent box)
  * Freehand markup overlay
* Preview updates instantly when:

  * Preset position changes
  * Freehand mask is added or cleared

---

### ✍ Freehand Markup Editor

* Adjustable **brush size slider** (small → large)
* Live drawing with visual feedback
* **Clear Drawing** button inside editor
* Empty masks are ignored automatically
* Editor opens centered over the main UI

---

### 📍 Preset Watermark Positions

All preset positions are fully functional:

* Top Left
* Top Right
* Bottom Left
* Bottom Right

**Logic improvement:**

* Presets apply automatically when no effective freehand mask exists
* Freehand masks override presets only when they contain actual data

---

### ⏳ Processing Experience

* Non‑blocking background processing
* **Progress popup** with:

  * Progress bar
  * Live ETA calculation
* **Summary popup** after completion showing:

  * Total images
  * Successfully processed images

---

## 🛠 Technical Improvements

* Stable Tkinter layout (no widget overlap)
* Fixed geometry propagation issues
* Safer mask handling (ignores empty masks)
* Explicit watermark position mapping
* Cleaner separation of preview, controls, and actions

---

## ✅ Who Should Update

* Anyone experiencing hidden buttons or broken layout
* Users working with large images or long file lists
* Users relying on preset watermark positions
* Anyone wanting a polished, professional UI experience

---

## 📌 Notes

* This version is intended as a **stable base release**
* Future updates can safely build on this without re‑introducing layout bugs

---

## 🔮 Planned Enhancements (Next Versions)

* Cancel button during processing
* Per‑image presets and masks
* Undo support for freehand strokes
* Zoomable preview / editor
* Save & load watermark projects
* Standalone EXE packaging

---

**Thank you for using Bulk Watermark Removal!**
If you encounter issues or have feature requests, please open an issue or discussion on GitHub.
