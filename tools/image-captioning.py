import os
import time
import requests
from dotenv import load_dotenv


print("")

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face token from the environment variable
HF_TOKEN = os.getenv('HF_TOKEN')

model = "blip-image-captioning-large"






API_URL = f"https://api-inference.huggingface.co/models/Salesforce/{model}"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(filename):
    max_retries = 5
    base_delay = 1  # Start with 1 second delay
    
    for attempt in range(max_retries):
        try:
            with open(filename, "rb") as f:
                data = f.read()
            response = requests.post(API_URL, headers=headers, data=data)
            
            # If we get a 503, wait and retry
            if response.status_code == 503:
                if attempt < max_retries - 1:
                    delay = base_delay * (2 ** attempt)  # Exponential backoff
                    print(f"      Model not ready, retrying in {delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(delay)
                    continue
                else:
                    raise Exception("      Model is still not ready after maximum retries")
            
            # For other HTTP errors, raise immediately
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise Exception(f"      Failed after {max_retries} attempts: {str(e)}")
            delay = base_delay * (2 ** attempt)
            print(f"      Error occurred, retrying in {delay} seconds... (Attempt {attempt + 1}/{max_retries})")
            time.sleep(delay)

def process_images(input_folder):
    # Create the output directory if it doesn't exist
    output_dir = f"output/image-captioning/{model}"
    os.makedirs(output_dir, exist_ok=True)
    
    for image_filename in os.listdir(input_folder):
        if image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(input_folder, image_filename)
            print(f"🔄    Processing {image_path}...")
            
            # Generate the description
            output = query(image_path)
            if isinstance(output, list) and len(output) > 0:
                description = output[0].get("generated_text", "No description generated")
            else:
                description = "      No description generated"
            
            # Save the description with a Unix timestamped filename
            timestamp = int(time.time())
            output_filename = f"{os.path.splitext(image_filename)[0]}.txt"
            output_path = os.path.join(output_dir, output_filename)
            
            with open(output_path, "w") as f:
                f.write(description)
            
            print(f"  ✅  Description saved to {output_path}\n")

            # Append to a log file
            with open(".logs/image-captioning.txt", "a") as log_file:
                log_file.write(f"IMAGE:         {image_path}\nDESCRIPTION:   {description}\nFILENAME:      {output_filename}\nMODEL:         {model}\n\n")

# Example usage
process_images("input/image-captioning")
