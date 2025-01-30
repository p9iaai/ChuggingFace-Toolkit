# Background Removal Tool Documentation

## Overview

This tool provides automated background removal for images using 🤗HuggingFace Spaces API. It processes images in batch mode, making it ideal for bulk image processing tasks.

## Usage Instructions

### Input Preparation

1. Place images in the `input/background-removal` folder
2. Ensure images are in supported formats: PNG, JPG/JPEG
3. Verify folder permissions allow read/write access

### Execution

Run the script from the project root directory:

```bash
python tools/background-removal.py
```

### Output

Processed images will be saved in:

```text
output/background-removal
```

### Example Terminal output:

<img src=".assets/background_removal_terminal.PNG" alt="Terminal Example Screen" />

## Performance Expectations

- Average processing time: 2-3 seconds per image
- Maximum image size: 5MB
- Recommended batch size: Up to 100 images per run

## Troubleshooting Guide

### Common Issues

- **Invalid API response**
  - Verify HF_TOKEN is correctly set
  - Check token permissions
  - Ensure API quota is available

- **No output file generated**
  - Verify input image format
  - Check file permissions
  - Ensure image size is within limits

- **Permission errors**
  - Verify folder permissions
  - Check user account privileges
  - Ensure sufficient disk space

---

<div align="center">

**ChuggingFace is very pleased...**

<img src=".assets/chuggingface_toolkit.png" width="512" alt="ChuggingFace">

---

**p9iaai** <img src=".assets/p9iaai.png" width="32" align="middle"> **2025**

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/p9iaai)

---

</div>
