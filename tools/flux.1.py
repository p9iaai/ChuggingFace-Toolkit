import os
import time
import random
from dotenv import load_dotenv
from PIL import Image
import requests
from io import BytesIO

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face token from the environment variable
HF_TOKEN = os.getenv('HF_TOKEN')

def generate_image_with_timeout(model, prompt, guidance_scale, num_inference_steps, width, height, seed, timeout):
    """
    Generate an image using the Hugging Face Inference API with a timeout.
    """
    API_URL = f"https://api-inference.huggingface.co/models/black-forest-labs/{model}"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json",
        "x-wait-for-model": "true"  # Always wait for the model to load or you won't get very far
    }

    data = {
        "inputs": prompt,
        "parameters": {
            "guidance_scale": guidance_scale,
            "num_inference_steps": num_inference_steps,
            "width": width,
            "height": height,
            "seed": seed,
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=timeout)
        response.raise_for_status()  # Raise an error for bad status codes
        return Image.open(BytesIO(response.content))  # Convert response content to an image
    except requests.exceptions.RequestException as e:
        print(f"\n💩   Request failed. {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"\n    👿   Response content: {e.response.content}")
            print(f"\n    😈   Response headers: {e.response.headers}")
        raise e

def generate_image(prompt, model="FLUX.1-schnell", guidance_scale=7.5, num_inference_steps=6, width=1024, height=1024, max_retries=9):
# def generate_image(prompt, model="FLUX.1-dev", guidance_scale=5, num_inference_steps=24, width=1024, height=1024, max_retries=9):
    """
    Generates an image based on a given text prompt using the specified model.
    
    Parameters:
    - prompt (str): The text prompt to generate the image.
    - model (str): The model to use: FLUX.1-schnell or FLUX.1-dev.
    - guidance_scale (float): A higher guidance scale value encourages the model to generate images closely linked to the text prompt.
    - num_inference_steps (int): The number of denoising steps. More steps usually lead to a higher quality image.
    - width (int): The width of the output image in pixels.
    - height (int): The height of the output image in pixels.
    - max_retries (int): The maximum number of retries for the request in case of a server error or timeout.
    """
    # Generate a random seed for the image generation
    seed = random.randint(1, 18446744073709552000) # This number is 2^64 - 1 if you care about that sort of thing
    # seed = # Add your seed here if you want to use a specific seed (remember to comment out the random seed line above)
    
    # Retry mechanism with exponential backoff
    for attempt in range(max_retries):
        try:
            # Generate the image using the specified parameters with a timeout of 60 seconds
            print(f"\n🚀   Processing. Please wait...")
            image = generate_image_with_timeout(
                model,
                prompt,
                guidance_scale,
                num_inference_steps,
                width,
                height,
                seed,
                timeout=60  # Timeout 60 seconds
            )
            break  # Exit the loop if the request is successful
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 503:
                print(f"\n🙄   Model is not ready (503). Retrying {attempt + 1}/{max_retries}...")
            elif e.response.status_code == 500:
                print(f"\n🙄   Server error (500). Retrying {attempt + 1}/{max_retries}...")
            elif e.response.status_code == 429:
                print(f"\n🙄   Too Many Requests (429). Retrying {attempt + 1}/{max_retries}...")
            else:
                print(f"\n🙄   HTTP error occurred: {e}. Retrying {attempt + 1}/{max_retries}...")
            time.sleep((2 ** attempt) + random.uniform(0, 1))  # Exponential backoff with jitter (lovely)
        except requests.exceptions.Timeout:
            print(f"\n🙄   Request timed out. Retrying {attempt + 1}/{max_retries}...")
            time.sleep((2 ** attempt) + random.uniform(0, 1))  # Exponential backoff with jitter (delightful)
        except Exception as e:
            print(f"\n🤬   An unexpected error occurred: {e}.\n\n🙄   WTF? Fuuuuuuuu... Retrying {attempt + 1}/{max_retries}...")
            time.sleep((2 ** attempt) + random.uniform(0, 1))  # Exponential backoff with jitter (splendid)
    else:
        print("\n😭   Max retries reached. Failed to generate image.")
        return
    
    # Save the image
    output_dir = f"output/flux.1/{model}"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = int(time.time())
    output_path = os.path.join(output_dir, f"{timestamp}_{width}x{height}.png")
    image.save(output_path)
    
    # Print and log the results
    print(f"\n     💾   PNG SAVED TO     >   {output_path}")
    print(f"     🤖   MODEL            >   {model}")
    print(f"     🎲   SEED             >   {seed}")
    print(f"     🟢   PROMPT           >   {prompt}")
    print("                          ✔️    SUCCESS")

    with open(f".logs/FLUX.1.txt", "a") as log_file:
        log_file.write(f"PNG SAVED TO   {output_path}\nMODEL          {model}\nSEED           {seed}\nGUIDANCE       {guidance_scale}\nSTEPS          {num_inference_steps}\nRESOLUTION     {width}x{height}\nPROMPT         {prompt}\n\n")

# Example usage (FLUX models do not use negative prompts)

generate_image("a frog walking in a comic book art style")
generate_image("a frog walking in a realistic art style")
generate_image("a frog walking in a neon art style")
generate_image("a frog walking in a fantasy art style")
generate_image("a frog walking in a science fiction art style")
generate_image("a frog walking in a b-movie art style")
generate_image("a frog walking in a jacobian art style")
generate_image("a frog walking in a comedic art style")
