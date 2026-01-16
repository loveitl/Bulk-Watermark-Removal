# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog** and this project follows **Semantic Versioning**.

---

## [2.5.1] - 2026-01-16

### Fixed

* Fixed UI layout issue where the preview image could hide or overlap the START button
* Prevented preview widget from expanding beyond its allocated area
* Ensured action buttons are always visible regardless of image size

### Improved

* Stabilized right-side panel layout with a fixed-height preview container
* Improved overall UI consistency when loading large images

---

## [2.5.0] - 2026-01-15

### Added

* Progress popup with progress bar during watermark removal
* Live ETA display while processing images
* Summary popup after processing completion
* Horizontal scrollbar for image table to support long filenames
* Automatic centering of main window and all popups

### Improved

* Preview panel now shows live overlay for preset watermark regions
* Preview panel displays freehand mask overlay before processing
* Automatically selects and previews the first image when images are added
* Added Clear Table button to reset image list, preview, and masks

---

## [2.3.0] - 2026-01-14

### Added

* Freehand watermark markup editor
* Adjustable brush size slider for freehand drawing
* Clear freehand markup option inside editor
* Live visual overlay of freehand mask on preview

### Fixed

* Preset watermark removal not triggering when empty freehand masks existed
* Improved handling of empty or unused freehand masks

---

## [2.2.0] - 2026-01-13

### Fixed

* Incorrect preset watermark positioning logic
* Top/Bottom and Left/Right presets not applying correctly in some cases

### Improved

* Introduced explicit coordinate mapping for all preset watermark positions
* Improved reliability of preset fallback behavior

---

## [2.0.0] - 2026-01-10

### Added

* Bulk watermark removal using OpenCV inpainting
* Drag-and-drop support for adding images
* Preset watermark region removal
* Image preview panel

---

## [1.0.0] - 2026-01-01

### Added

* Initial release with basic watermark removal functionality
