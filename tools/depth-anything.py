import os
import time
from datetime import datetime
from gradio_client import Client, handle_file
import logging
from PIL import Image

INPUT_DIR = "input/depth-anything"
OUTPUT_DIR = "output/depth-anything"
LOG_DIR = ".logs"
LOG_FILE = os.path.join(LOG_DIR, "depth-anything.txt")
HF_TOKEN = os.getenv("HF_TOKEN")
RETRIES = 3
INITIAL_BACKOFF = 3  # Initial exp. backoff time in seconds

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

client = Client("p9iaai/Depth-Anything-V2", hf_token=HF_TOKEN)

print("")

def process_image(image_path, retries=RETRIES, backoff=INITIAL_BACKOFF):
    """Process an image with retries and exponential backoff."""
    for attempt in range(retries):
        try:
            result = client.predict(
                image=handle_file(image_path),
                api_name="/on_submit"
            )
            return result
        except Exception as e:
            if attempt == retries - 1:
                raise
            logging.warning(f"Retry {attempt + 1} for {image_path} in {backoff}s...")
            time.sleep(backoff)
            backoff *= 2

def save_outputs(result, original_filename):
    """Save both outputs with proper naming and 16-bit handling."""
    timestamp = int(time.time())
    outputs = [
        (result[0][1], f"{original_filename}_depth_rgb_{timestamp}.png"),  # RGB depth map
        (result[1], f"{original_filename}_depth_bw_{timestamp}.png"),      # Grayscale depth map
    ]

    for src, dest in outputs:
        if src:
            dest_path = os.path.join(OUTPUT_DIR, dest)
            if "raw16" in dest:
                # Handle 16-bit image with Pillow
                with Image.open(src) as img:
                    img.save(dest_path, format="PNG")
            else:
                os.rename(src, dest_path)
    logging.info(f"Saved outputs for {original_filename}")

def main():
    images = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    total = len(images)
    logging.info(f"Processing {total} images")

    for idx, img_name in enumerate(images, 1):
        img_path = os.path.join(INPUT_DIR, img_name)
        base_name = os.path.splitext(img_name)[0]
        
        print(f"  🔍    Processing image {idx}/{total}: {img_name}...")
        try:
            result = process_image(img_path)
            save_outputs(result, base_name)
            print(f"     ✅ Saved depth maps for {img_name}!\n")
        except Exception as e:
            logging.error(f"Failed {img_name}: {str(e)}")
            print(f"     ❌ Failed {img_name}. Check logs.\n")

if __name__ == "__main__":
    main()
