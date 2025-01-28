import os
import time
import json
import threading
import queue
import yaml
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

print("")

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face API token from the environment
HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize the InferenceClient
client = InferenceClient(api_key=HF_TOKEN)



# Choose one of the available models
MODEL = "Qwen/Qwen2.5-Coder-32B-Instruct"
# MODEL = "meta-llama/Llama-3.1-70B-Instruct"
# MODEL = "meta-llama/Llama-3.3-70B-Instruct"
# MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"



# Folder containing input YAML files
INPUT_FOLDER = "input/docmaker"

# Output folder for generated Markdown files
OUTPUT_FOLDER = "output/docmaker"

# Folder to store chat history files
HISTORY_FOLDER = ".logs/docmaker"

# Timeout for API requests (in seconds)
TIMEOUT = 30

def create_output_structure(input_filename, categories):
    """Create folder structure for output files."""
    base_path = os.path.join(OUTPUT_FOLDER, os.path.splitext(input_filename)[0])
    os.makedirs(base_path, exist_ok=True)
    
    for category in categories:
        category_path = os.path.join(base_path, category)
        os.makedirs(category_path, exist_ok=True)
    
    return base_path

def save_markdown_files(history, base_path):
    """Save assistant responses as Markdown files."""
    for i in range(1, len(history), 2):  # Process only even-numbered entries (assistant responses)
        entry = history[i]
        if entry["role"] != "assistant":
            continue
            
        # Create file path
        category_path = os.path.join(base_path, entry["category"])
        filename = f"{entry['topic'].replace('/', '-')}.md"
        filepath = os.path.join(category_path, filename)
        
        # Write Markdown content
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(entry["content"])

def get_history_file_path(input_filename):
    """Get the path for the history file based on input filename."""
    history_filename = f"{os.path.splitext(input_filename)[0]}.json"
    return os.path.join(HISTORY_FOLDER, history_filename)

def load_chat_history(input_filename):
    """Load chat history from the history file for specific input file."""
    history_file = get_history_file_path(input_filename)
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            return json.load(f)
    return []

def save_chat_history(history, input_filename):
    """Save chat history to the history file for specific input file."""
    history_file = get_history_file_path(input_filename)
    os.makedirs(os.path.dirname(history_file), exist_ok=True)
    with open(history_file, "w") as f:
        json.dump(history, f, indent=2)

# Thread pool for managing API calls
thread_pool = []

def chat_completion(prompt):
    """Send a chat completion request to the model with a timeout."""
    def _call_api(result_queue):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],  # Only send the current prompt
                max_tokens=27000
            )
            result_queue.put(response.choices[0].message.content)
        except Exception as e:
            result_queue.put(e)

    result_queue = queue.Queue()
    thread = threading.Thread(target=_call_api, args=(result_queue,))
    thread_pool.append(thread)
    thread.start()

    # Wait for the thread to complete or timeout
    thread.join(timeout=TIMEOUT)

    if thread.is_alive():
        print("     💩   Timeout reached...")
        return None
    else:
        result = result_queue.get()
        if isinstance(result, Exception):
            print(f"\n     💩  Error: {result}.")
            return None
        return result

def cleanup_threads():
    """Clean up any remaining threads before program exit."""
    for thread in thread_pool:
        if thread.is_alive():
            thread.join(timeout=1)

def process_yaml_files():
    """Read YAML files from the input folder and process them."""
    print("Processing YAML files from the input folder...")

    # Create input/output folders if they don't exist
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Get all YAML files in the input folder
    input_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".yaml") or f.endswith(".yml")]
    if not input_files:
        print(f"No YAML files found in the '{INPUT_FOLDER}' folder.")
        return

    for input_file in input_files:
        file_path = os.path.join(INPUT_FOLDER, input_file)
        with open(file_path, "r") as f:
            yaml_data = yaml.safe_load(f)

        print(f"\n🟣  Processing file: {input_file}")

        # Initialize history for this file
        history = load_chat_history(input_file)
        
        # Create output folder structure
        categories = list(yaml_data.keys())
        base_path = create_output_structure(input_file, categories)

        for category, topics in yaml_data.items():
            print(f"\n  🟠  Category: {category}")
            for topic in topics:
                # Ensure the topic is a string (in case the YAML structure is nested)
                if isinstance(topic, dict):
                    topic = list(topic.values())[0]  # Extract the first value if it's a dict
                elif not isinstance(topic, str):
                    continue  # Skip if the topic is not a string

                print(f"    ◻️  Topic: {topic}")

                # Construct the prompt
                prompt = f"Please create a long-context full-featured Markdown cheat sheet style learning document for the following category and topic. Do not include any introductory phrases like 'Certainly' or 'Here is a'. The title should be the topic name. Start directly with the content and also avoid sign-off messages, external links and citations:\n\nCategory:  {category}\n\nTopic:  {topic}"

                while True:
                    response = chat_completion(prompt)
                    if response is not None:
                        break
                    print("    🙄    Retrying...")

                # Save the prompt and response to history with metadata
                history.append({
                    "input_filename": input_file,
                    "category": category,
                    "topic": topic,
                    "role": "user",
                    "content": prompt
                })
                history.append({
                    "input_filename": input_file,
                    "category": category,
                    "topic": topic,
                    "role": "assistant",
                    "content": response
                })
                save_chat_history(history, input_file)

                print(f"      ◽️  Response saved.")

        # Save Markdown files after processing each YAML file
        save_markdown_files(history, base_path)

    print("\n✔️   All YAML files processed.")
    return

if __name__ == "__main__":
    try:
        process_yaml_files()
    finally:
        cleanup_threads()
