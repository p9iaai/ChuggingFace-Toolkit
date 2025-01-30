import os
import sys
import time
import httpx
from gradio_client import Client, handle_file
from pathlib import Path
from typing import Literal
import logging
from dotenv import load_dotenv

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 3  # seconds

print("")

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv('HF_TOKEN')

# Create logs directory if it doesn't exist
Path(".logs").mkdir(parents=True, exist_ok=True)

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create formatters
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter(f'%(asctime)s - %(levelname)s - %(message)s')

# Create file handler
file_handler = logging.FileHandler('.logs/image-upscaler.txt', encoding='utf-8')
file_handler.setFormatter(file_formatter)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(console_formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def upscale_images(
    input_dir: str,
    output_dir: str,
    scale: float = 2.0,
    enhance_mode: Literal['Only Face Enhance', 'Only Image Enhance', 'Face Enhance + Image Enhance'] = "Face Enhance + Image Enhance"
):
    """
    Upscale images from input directory and save to output directory.
    
    Args:
        input_dir: Path to directory containing input images
        output_dir: Path to directory to save upscaled images
        scale: Upscaling factor (default: 2.0)
        enhance_mode: Enhancement mode (default: "Face Enhance + Image Enhance")
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Initialize Gradio client
    try:
        client = Client("p9iaai/upscaler", hf_token=HF_TOKEN) # Dupe of 'smartfeed/image_hd'
    except httpx.ReadTimeout:
        logger.error(f"Read timed out. Try again in a few minutes.\n                                  It usually means HuggingFace is having issues.\n")
        sys.exit(1)
    
    # Get list of image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp']
    image_files = [
        f for f in os.listdir(input_dir)
        if os.path.splitext(f)[1].lower() in image_extensions
    ]
    
    if not image_files:
        logger.warning(f"No images found in {input_dir}")
        return
        
    # Process each image
    for image_file in image_files:
        retry_count = 0
        while retry_count <= MAX_RETRIES:
            try:
                logger.info(f"Processing {image_file}...")
                
                # Construct full input path
                input_path = os.path.join(input_dir, image_file)
                
                # Call API
                result = client.predict(
                    input_image=handle_file(input_path),
                    scale=scale,
                    enhance_mode=enhance_mode,
                    api_name="/enhance_image"
                )
                
                # Save result
                output_path = os.path.join(output_dir, f"Upscaled_{scale}x_'{enhance_mode}'-{image_file}")
                os.rename(result[1], output_path)
                
                logger.info(f"Successfully saved upscaled image to {output_path}\n")
                break
                
            except Exception as e:
                retry_count += 1
                if retry_count <= MAX_RETRIES:
                    logger.warning(f"Attempt {retry_count}/{MAX_RETRIES} failed for {image_file}: {str(e)}")
                    logger.info(f"Retrying in {RETRY_DELAY} seconds...")
                    time.sleep(RETRY_DELAY)
                else:
                    logger.error(f"Failed to process {image_file} after {MAX_RETRIES} attempts: {str(e)}")
                    break

if __name__ == "__main__":

# Example usage
    upscale_images(input_dir=r"input/image-upscaler", output_dir=r"output/image-upscaler", scale=2, enhance_mode='Face Enhance + Image Enhance')
