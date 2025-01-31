import requests
import re
import os
import time
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')

print("")

API_URL = "https://api-inference.huggingface.co/models/suno/bark"

headers = {"Authorization": f"Bearer {HF_TOKEN}", "x-wait-for-model": "true"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Prompt user for input text
input_text = input("💬   Enter the text to convert to speech: ")

# Sanitize the input text to create a valid filename
safe_filename = re.sub(r'[^\w\s-]', '', input_text).replace(' ', '_')[:50]  # Remove special characters and limit length

# Ensure it has a .wav extension
timestamp = int(time.time())
output_dir = "output/text-to-speech"
os.makedirs(output_dir, exist_ok=True)
output_file = f"{output_dir}/{timestamp}-{safe_filename}.wav"

# Get the audio bytes
audio_bytes = query({"inputs": input_text})

# Save the audio to a file
if audio_bytes:
    with open(output_file, "wb") as f:
        f.write(audio_bytes)
    print(f" 🔊  Audio saved as {output_file}\n")
else:
    print(" 🔇  Failed to generate audio.")
