import os
import logging
from gradio_client import Client, handle_file
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv('HF_TOKEN')

# Configure logging
os.makedirs('.logs', exist_ok=True)
logging.basicConfig(
    filename='.logs/face-swap.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def face_swap(source_path, target_path, enhance=False):
    """Perform face swap using the Hugging Face API"""
    try:
        # Initialize client
        client = Client("p9iaai/face-swap", hf_token=HF_TOKEN) # Dupe of 'tuan2308/face-swap'
        
        # Log start
        logging.info(f"🚀 Starting face swap with source: {source_path}, target: {target_path}, enhance: {enhance}")
        print("🔄 Processing face swap...")
        
        # Make prediction
        result = client.predict(
            source_file=handle_file(source_path),
            target_file=handle_file(target_path),
            doFaceEnhancer=enhance,
            api_name="/predict"
        )
        
        # Save output
        output_dir = 'output/face-swap'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"face-swap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        os.rename(result, output_path)
        
        # Log success
        logging.info(f"✅ Face swap successful! Output saved to: {output_path}")
        print(f"🎉 Success! Output saved to: {output_path}")
        
        return output_path
        
    except Exception as e:
        # Log error
        logging.error(f"❌ Error during face swap: {str(e)}")
        print(f"😢 Oops! Something went wrong: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    source = "input/face-swap/source.png"
    target = "input/face-swap/target.png"
    
    print("🌟 Welcome to Face Swap CLI!")
    print("📂 Looking for input files...")
    
    if not os.path.exists(source) or not os.path.exists(target):
        print("😕 Missing input files! Please ensure source.png and target.png exist in input/face-swap/")
    else:
        enhance = input("✨ Do you want to enable face enhancement? (y/n): ").lower() == 'y'
        result = face_swap(source, target, enhance)
        
        if result:
            print("🌈 All done! Check your output folder for the result.")
        else:
            print("💔 Operation failed. Check the logs for more details.")