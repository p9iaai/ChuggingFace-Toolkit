import os
import logging
import time
from pathlib import Path
from gradio_client import Client, handle_file

print("")

# Configuration
INPUT_DIR = Path("./input/canny-edge-detect")
OUTPUT_DIR = Path("./output/canny-edge-detect")
LOG_FILE = Path("./.logs/canny-edge-detect.txt")
RETRY_COUNT = 3  # Configurable retry count
RETRY_DELAY = 5  # Seconds between retry attempts
SUPPORTED_EXTENSIONS = (".png", ".jpg", ".jpeg", ".bmp", ".webp")
HF_TOKEN = os.getenv("HF_TOKEN")

# Setup logging
os.makedirs(LOG_FILE.parent, exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_image(client, image_path, retries=RETRY_COUNT):
    """Process a single image with retry logic"""
    for attempt in range(retries):
        if attempt > 0:
            delay = RETRY_DELAY * attempt  # Progressive backoff
            print(f"⏳ Waiting {delay} seconds before retry...")
            time.sleep(delay)
            
        try:
            print(f"🔄 Processing {image_path.name} (attempt {attempt + 1}/{retries})")
            result = client.predict(
                img=handle_file(str(image_path)),
                api_name="/predict"
            )
            
            # The API returns a list where the first element is the image data
            if isinstance(result, list) and len(result) > 0:
                result = result[0]
            
            # Handle both dictionary and direct path string responses
            result_path = result['path'] if isinstance(result, dict) else result
            
            # Save output
            output_path = OUTPUT_DIR / f"{image_path.stem}_edge.png"
            os.rename(result_path, output_path)
            print(f"✅ Successfully processed {image_path.name}\n")
            logging.info(f"Successfully processed {image_path.name}")
            return True
            
        except Exception as e:
            logging.error(f"Failed to process {image_path.name}: {str(e)}")
            if attempt == retries - 1:
                print(f"❌ Failed to process {image_path.name} after {retries} attempts")
                return False

def main():
    print("🌟 Starting Canny Edge Detection Processing")
    logging.info("Starting processing")
    
    # Initialize API client once
    try:
        client = Client("p9iaai/canny-edge-detect", hf_token=HF_TOKEN)
        print(f"\n🔗 Connected to API: {client.src}")
    except Exception as e:
        logging.error(f"Failed to initialize API client: {str(e)}")
        print("❌ Failed to connect to API")
        return
    
    # Get all supported images
    images = [f for f in INPUT_DIR.iterdir() if f.suffix.lower() in SUPPORTED_EXTENSIONS]
    
    if not images:
        print("⚠️ No images found in input directory")
        return
    
    print(f"\n📂 Found {len(images)} images to process\n")
    
    # Process images sequentially
    for image_path in images:
        process_image(client, image_path)
    
    print("🎉 Processing complete!\n")
    logging.info("Processing complete")

if __name__ == "__main__":
    main()