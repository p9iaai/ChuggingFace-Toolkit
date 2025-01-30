import os
from pathlib import Path
from dotenv import load_dotenv
from gradio_client import Client, handle_file
import glob
import shutil

"""
This script processes images through the Hugging Face background removal API.
It reads images from the `input/background-removal` directory and processes them using the Hugging Face API.
The processed images are saved in the `output/background-removal` directory.
"""

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv('HF_TOKEN')

# Set up directories
INPUT_DIR = Path('input/background-removal')
OUTPUT_DIR = Path('output/background-removal')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def process_image(client, image_path):
    """Process a single image through background removal API"""
    output_path = OUTPUT_DIR / f"{Path(image_path).stem}_nobg.png"
    
    try:
        # Use the /png endpoint which returns a direct file
        result = client.predict(
            handle_file(image_path),
            api_name="/png"
        )
        
        if result and os.path.exists(result):
            shutil.move(result, output_path)
            print(f"✔️    Successfully processed!   ✔️   💪😎🤙")
            return True
        else:
            print(f"❌   Failed to process: {Path(image_path).name} - No output file   ❌   👀😭💩")
            return False
            
    except Exception as e:
        print(f"🚫   Error processing {Path(image_path).name}: {str(e)}   🚫   😡🤬🥵")
        return False

def main():
    client = Client(
        "p9iaai/background-removal", hf_token=HF_TOKEN # Dupe of 'not-lain/background-removal'
    )
    
    image_files = []
    for ext in ['*.png', '*.jpg', '*.jpeg']:
        image_files.extend(glob.glob(str(INPUT_DIR / ext)))
    
    total = len(image_files)
    print(f"\n🔍   Found {total} images to process!")
    
    successful = 0
    for idx, image_path in enumerate(image_files, 1):
        print(f"\n🙄   Processing {idx}/{total}: {Path(image_path).name}")
        if process_image(client, image_path):
            successful += 1
    
    print(f"\n🥰   Completed: {successful}/{total} images processed successfully!\n")

if __name__ == "__main__":
    main()