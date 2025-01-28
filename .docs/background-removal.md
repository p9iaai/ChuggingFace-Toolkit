# Background Removal Tool

Batch processes images to remove backgrounds using 🤗HuggingFace Spaces API.

## Usage

1. Place images in the `input\background-removal` folder.
2. Run script:

    ```python
    python background-removal.py
    ```

3. Find processed images in the `output\background-removal` folder.

## Example Output

```bash
🔍   Found 3 images to process!

🙄   Processing 1/3: image1.png

✔️   Successfully processed!   ✔️   💪😎🤙

🙄   Processing 2/3: image2.png

✔️   Successfully processed!   ✔️   💪😎🤙

🙄   Processing 3/3: image3.png

✔️   Successfully processed!   ✔️   💪😎🤙

🥰   Completed: 3/3 images processed successfully!
```

## Supported Formats

- PNG
- JPG / JPEG

## Troubleshooting

- Invalid API response: Verify your HF_TOKEN is correct
- No output file: Ensure input images are valid format
- Permission errors: Check folder permissions

---
