# Depth-Anything Image Processing Script

This script processes images using the `p9iaai/Depth-Anything-V2` API, generating both colour and black and white depth maps and saving the results to an output folder. It includes features like retries with exponential backoff, progress updates, and logging.

## Features

- **Batch Processing**: Cycles through all images in the `input/depth-anything` folder.
- **Output Naming**: Saves output files with descriptive names, including the original filename, depth map type, and a Unix timestamp.
- **Retry Mechanism**: Retries failed API requests with exponential backoff.
- **Progress Updates**: Displays clean, client-friendly progress updates in the terminal with emojis.
- **Logging**: Saves detailed logs with timestamps to `.logs/depth-anything.txt`.
- **Error Handling**: Logs errors and continues processing the remaining images.

## Folder Structure

Before running the script, ensure your project folder has the following structure:

```text
Chuggingface-Toolkit/
.
├── input/
│ └── depth-anything/               Place your input images here
├── output/
│ └── depth-anything/               Processed images will be saved here
├── .logs/                          Logs will be saved here
└── tools/
  └── depth_anything.py             The script
```

## Usage

1. **Place Images**:
   - Add your images to the `input/depth-anything` folder. Supported formats: `.png`, `.jpg`, `.jpeg`.

2. **Run the Script**:
   - Activate your virtual environment and run the script:

     ```terminal
     python depth_anything.py
     ```

3. **Check Outputs**:
   - Processed images will be saved in the `output/depth-anything` folder with the following naming convention:
     - `{original_filename}_depth_rgb_{unix-timestamp}.png`
     - `{original_filename}_depth_bw_{unix-timestamp}.png`

4. **Review Logs**:
   - Logs are saved to `.logs/depth-anything.txt` and include timestamps for each event.

## Script Configuration

You can modify the following variables in the script to suit your needs:

- `INPUT_DIR`: Path to the input folder (default: `input/depth-anything`).
- `OUTPUT_DIR`: Path to the output folder (default: `output/depth-anything`).
- `LOG_DIR`: Path to the logs folder (default: `.logs`).
- `RETRIES`: Number of retries for failed API requests (default: `3`).
- `INITIAL_BACKOFF`: Initial backoff time in seconds for retries (default: `3`).

## Example Terminal Output

```terminal
Loaded as API: https://p9iaai-depth-anything-v2.hf.space ✔

  🔍    Processing image 1/2: the-frog-example-1.png...
     ✅ Saved depth maps for the-frog-example-1.png!

  🔍    Processing image 2/2: the-frog-example-2.png...
     ✅ Saved depth maps for the-frog-example-2.png!
```

## Logs Example

```text
2023-10-15 12:34:56 - INFO - Found 5 images to process.
2023-10-15 12:35:01 - INFO - Outputs saved for bus.
2023-10-15 12:35:10 - INFO - Outputs saved for car.
2023-10-15 12:35:15 - WARNING - Attempt 1 failed for tree.jpg. Retrying in 1 seconds...
2023-10-15 12:35:20 - ERROR - Failed to process tree.jpg: API request timed out.
2023-10-15 12:35:25 - INFO - Outputs saved for house.
2023-10-15 12:35:30 - INFO - Outputs saved for dog.
```

## Notes

- Ensure the `HF_TOKEN` environment variable is set correctly to authenticate with the API.
- If the script encounters an error, it will log the issue and continue processing the remaining images.
- The script creates the `output/depth-anything` and `.logs` folders if they don't already exist.

## Example Images

| Input PNG | Colour Depth Map | Greyscale Depth Map |
| :-: | :-: | :-: |
| <img src=".assets/the-frog-example-1.png" width="256"> | <img src=".assets/the-frog-example-1_depth_rgb_1738074635.png" width="256"> | <img src=".assets/the-frog-example-1_depth_bw_1738074635.png" width="256"> |
| <img src=".assets/the-frog-example-2.png" width="256"> | <img src=".assets/the-frog-example-2_depth_rgb_1738074645.png" width="256"> | <img src=".assets/the-frog-example-2_depth_bw_1738074645.png" width="256"> |

---
