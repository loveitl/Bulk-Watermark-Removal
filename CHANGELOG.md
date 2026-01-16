# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog**
and this project follows **Semantic Versioning**.

---

## [2.5.1] - 2026-01-16
### Fixed
- Fixed UI layout issue where large preview images could hide the START button
- Prevented preview widget from expanding beyond its allocated area
- Ensured action buttons remain visible regardless of image size

### Improved
- Stabilized right-side panel layout using a fixed-height preview container
- Improved preview behavior for large and high-resolution images
- Improved window and popup centering behavior

---

## [2.5.0] - 2026-01-15
### Added
- Progress popup with progress bar during processing
- Live ETA display while processing images
- Summary popup after processing completion
- Horizontal scrollbar for image table
- Automatic centering of main window and all popups

### Improved
- Live overlay preview for preset watermark regions
- Freehand mask overlay shown in preview before processing
- Auto-select and auto-preview first image when images are added
- Clear Table button to reset images, preview, and masks

---

## [2.3.0] - 2026-01-14
### Added
- Freehand watermark markup editor
- Adjustable brush size slider
- Clear freehand drawing option
- Live overlay preview for freehand masks

### Fixed
- Preset watermark removal not triggering when empty freehand masks existed

---

## [2.2.0] - 2026-01-13
### Fixed
- Incorrect watermark preset positioning logic
- Top/Bottom and Left/Right presets not applying correctly

### Improved
- Explicit coordinate mapping for all preset watermark positions

---

## [2.0.0] - 2026-01-10
### Added
- Bulk watermark removal using OpenCV inpainting
- Drag-and-drop image support
- Preset watermark region removal
- Image preview panel

---

## [1.0.0] - 2026-01-01
### Added
- Initial release
