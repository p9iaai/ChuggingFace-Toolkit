import os
import argparse
import logging
from datetime import datetime
from dotenv import load_dotenv
from gradio_client import Client, handle_file
from PIL import Image
import time
import requests
import shutil

print("")

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv('HF_TOKEN')

# Setup directories
INPUT_DIR = "input/edit-image"
OUTPUT_DIR = "output/edit-image"
LOGS_DIR = ".logs"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=os.path.join(LOGS_DIR, 'edit-image.txt'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_input_image():
    """Get an input image from the input directory or download default"""
    # Check for existing PNG files in input directory
    png_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.png')]
    
    if png_files:
        # Use the first PNG file found
        return os.path.join(INPUT_DIR, png_files[0])
    
    # If no PNG files exist, download default
    default_image_url = 'https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'
    default_image_path = os.path.join(INPUT_DIR, 'default.png')
    
    print("📥 Downloading default control image...")
    try:
        response = requests.get(default_image_url, stream=True)
        response.raise_for_status()
        with open(default_image_path, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        print("✅ Default image downloaded successfully")
        logging.info("Downloaded default control image")
        return default_image_path
    except Exception as e:
        print(f"💩 Error downloading default image: {str(e)}")
        logging.error(f"Error downloading default image: {str(e)}")
        raise

def setup_argparse():
    """Setup command line argument parsing"""
    parser = argparse.ArgumentParser(description='Edit image using AI')
    parser.add_argument('prompt', type=str, help='Prompt for image editing')
    parser.add_argument('--image', type=str, help='Path to input image (optional, uses first PNG in input directory if not provided)')
    parser.add_argument('--width', type=int, default=1024, help='Image width')
    parser.add_argument('--height', type=int, default=1024, help='Image height')
    parser.add_argument('--seed', type=int, default=0, help='Seed for generation')
    parser.add_argument('--steps', type=int, default=28, help='Number of inference steps')
    parser.add_argument('--guidance', type=float, default=30, help='Guidance scale')
    return parser.parse_args()

# Make sure to handle transparent formats. Can always run output through `background-removal.py`
def prepare_image(image_path):
    """Prepare image for API submission"""
    try:
        # Open and verify the image
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            # Create a temporary file with proper format
            temp_path = os.path.join(INPUT_DIR, 'temp_input.png')
            img.save(temp_path, 'PNG')
            return temp_path
    except Exception as e:
        logging.error(f"Error preparing image: {str(e)}")
        raise

def main():
    """Main function to handle image editing process"""
    try:
        print("🚀 Initializing AI Image Editor...")
        args = setup_argparse()
        logging.info(f"Starting image edit with prompt: {args.prompt}")

        # Get input image path
        input_image_path = args.image if args.image else get_input_image()
        if not os.path.exists(input_image_path):
            raise FileNotFoundError(f"Input image not found: {input_image_path}")

        # Get input filename without extension
        input_filename = os.path.splitext(os.path.basename(input_image_path))[0]

        prepared_image_path = prepare_image(input_image_path)
        
        # Gradio client
        print("📞 Connecting to API...")
        client = Client("p9iaai/edit-image", hf_token=HF_TOKEN)
        
        # Generate timestamp (avoid overwriting files if same seed is used)
        timestamp = int(time.time())
        
        print("\n🎨 Generating image...")
        print(f"😎 Using control image: {input_image_path}\n")
        
        result = client.predict(
            handle_file(prepared_image_path),
            args.prompt,
            args.seed,
            True,  # randomize_seed
            args.width,
            args.height,
            args.guidance,
            args.steps,
            api_name="/infer"
        )
        
        # The result is a tuple where the first element is the output image path
        result_image_path = result[0]
        used_seed = result[1]
        
        print("💾 Saving image...")
        output_filename = f"{timestamp}_{input_filename}_{used_seed}_edited.png"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        
        img = Image.open(result_image_path)
        img.save(output_path, 'PNG')
        
        if os.path.exists(prepared_image_path) and prepared_image_path != input_image_path:
            os.remove(prepared_image_path)
        
        print(f"😇 Done! Image saved as: {output_path}")
        print(f"🎲 Seed used: {used_seed}\n")
        logging.info(f"Successfully generated image: {output_path}")
        
    except Exception as e:
        print(f"💩❌ Error: {str(e)}")
        logging.error(f"Error during image generation: {str(e)}")
        raise

if __name__ == "__main__":
    main()

# That was annoying
