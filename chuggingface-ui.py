import gradio as gr
import os
from pathlib import Path
import shutil
import time
import io
import contextlib
from gradio_client import Client, handle_file
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv('HF_TOKEN')

print("\n        Welcome to the ChuggingFace ToolKit!\n")

# Ensure input/output directories exist
def ensure_directories():
    for tool in ["background-removal", "canny-edge-detect", "depth-anything", "docmaker", "edit-image", "face-swap", "flux.1", "image-captioning", "image-upscaler", "stable-diffusion", "text-to-speech"]:
        Path(f"input/{tool}").mkdir(parents=True, exist_ok=True)
        Path(f"output/{tool}").mkdir(parents=True, exist_ok=True)
    Path(".logs").mkdir(exist_ok=True)

def background_removal(images):
    if not HF_TOKEN:
        return "Error: HF_TOKEN not found in .env file", None
    try:
        client = Client("p9iaai/background-removal", hf_token=HF_TOKEN)
        output_text = ""
        output_files = []
        total = len(images)
        output_text += f"🔍   Found {total} images to process!\n"
        yield output_text, output_files
        for idx, img in enumerate(images, 1):
            try:
                filename = Path(img).name
                input_path = Path("input/background-removal") / filename
                shutil.copy(img, input_path)
                output_text += f"🔄   Processing {idx}/{total}: {filename}\n"
                yield output_text, output_files
                output_path = Path("output/background-removal") / f"{Path(filename).stem}_nobg.png"
                result = client.predict(handle_file(str(input_path)), api_name="/png")
                if result and os.path.exists(result):
                    shutil.move(result, output_path)
                    output_files.extend([str(input_path), str(output_path)])
                    output_text += f"✔️    Successfully processed!\n"
                    yield output_text, output_files
                else:
                    output_text += f"❌   Failed to process: {filename} - No output file   ❌   💩💩💩\n"
                    yield output_text, output_files
            except Exception as e:
                output_text += f"🚫   Error processing {filename}: {str(e)}   🚫   😡🤬🥵\n"
                yield output_text, output_files
        successful = len(output_files) // 2
        output_text += f"🥰   Completed: {successful}/{total} images processed successfully!"
        yield output_text, output_files
    except Exception as e:
        yield f"Error: Failed to initialize client: {str(e)}", None

def canny_edge_detect(images):
    if not HF_TOKEN:
        return "Error: HF_TOKEN not found in .env file", None
    try:
        client = Client("p9iaai/canny-edge-detect", hf_token=HF_TOKEN)
        output_text = ""
        output_files = []
        total = len(images)
        output_text += f"🔍   Found {total} images to process!\n"
        yield output_text, output_files
        for idx, img in enumerate(images, 1):
            try:
                filename = Path(img).name
                input_path = Path("input/canny-edge-detect") / filename
                shutil.copy(img, input_path)
                output_text += f"🔄   Processing {idx}/{total}: {filename}\n"
                yield output_text, output_files
                output_path = Path("output/canny-edge-detect") / f"{Path(filename).stem}_edge.png"
                result = client.predict(handle_file(str(input_path)), api_name="/predict")
                if isinstance(result, list) and len(result) > 0:
                    result = result[0]
                result_path = result['path'] if isinstance(result, dict) else result
                if result_path and os.path.exists(result_path):
                    shutil.move(result_path, output_path)
                    output_files.extend([str(input_path), str(output_path)])
                    output_text += f"✔️    Successfully processed!\n"
                    yield output_text, output_files
                else:
                    output_text += f"❌   Failed to process: {filename} - No output file   ❌   💩💩💩\n"
                    yield output_text, output_files
            except Exception as e:
                output_text += f"🚫   Error processing {filename}: {str(e)}   🚫   😡🤬🥵\n"
                yield output_text, output_files
        successful = len(output_files) // 2
        output_text += f"🥰   Completed: {successful}/{total} images processed successfully!"
        yield output_text, output_files
    except Exception as e:
        yield f"Error: Failed to initialize client: {str(e)}", None

def depth_anything(images):
    if not HF_TOKEN:
        return "Error: HF_TOKEN not found in .env file", None
    try:
        client = Client("p9iaai/Depth-Anything-V2", hf_token=HF_TOKEN)
        output_text = ""
        output_files = []
        total = len(images)
        output_text += f"🔍   Found {total} images to process!\n"
        yield output_text, output_files
        for idx, img in enumerate(images, 1):
            try:
                filename = Path(img).name
                input_path = Path("input/depth-anything") / filename
                shutil.copy(img, input_path)
                output_text += f"🔄   Processing {idx}/{total}: {filename}\n"
                yield output_text, output_files
                for attempt in range(3):
                    try:
                        result = client.predict(image=handle_file(str(input_path)), api_name="/on_submit")
                        break
                    except Exception as e:
                        if attempt == 2:
                            raise
                        delay = 3 * (2 ** attempt)
                        output_text += f"⏳   Retry {attempt + 1} in {delay}s...\n"
                        yield output_text, output_files
                        time.sleep(delay)
                timestamp = int(time.time())
                rgb_output = result[0][1]
                bw_output = result[1]
                if rgb_output and bw_output:
                    rgb_output_path = Path("output/depth-anything") / f"{Path(filename).stem}_depth_rgb_{timestamp}.png"
                    bw_output_path = Path("output/depth-anything") / f"{Path(filename).stem}_depth_bw_{timestamp}.png"
                    shutil.move(rgb_output, rgb_output_path)
                    shutil.move(bw_output, bw_output_path)
                    output_files.extend([str(input_path), str(rgb_output_path), str(bw_output_path)])
                    output_text += f"✔️    Successfully processed!\n"
                    yield output_text, output_files
                else:
                    output_text += f"❌   Failed to process: {filename} - No output files   ❌   💩💩💩\n"
                    yield output_text, output_files
            except Exception as e:
                output_text += f"🚫   Error processing {filename}: {str(e)}   🚫   😡🤬🥵\n"
                yield output_text, output_files
        successful = len(output_files) // 3
        output_text += f"🥰   Completed: {successful}/{total} images processed successfully!"
        yield output_text, output_files
    except Exception as e:
        yield f"Error: Failed to initialize client: {str(e)}", None

def docmaker(yaml_file):
    if not HF_TOKEN:
        return "Error: HF_TOKEN not found in .env file"
    try:
        if yaml_file is None:
            return "Error: No YAML file uploaded"
        filename = Path(yaml_file).name
        if not (filename.endswith('.yaml') or filename.endswith('.yml')):
            return "Error: File must be a YAML file (.yaml or .yml)"
        input_dir = Path("input/docmaker")
        input_dir.mkdir(parents=True, exist_ok=True)
        input_path = input_dir / filename
        shutil.copy(yaml_file, input_path)
        import tools.docmaker
        output_text = f"📝 Processing YAML file: {filename}\n"
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            tools.docmaker.process_yaml_files()
        printed_output = f.getvalue()
        output_text += printed_output
        output_dir = Path("output/docmaker") / Path(filename).stem
        output_text += f"\n✨ Processing complete!\n"
        output_text += f"\n📂 Generated documentation can be found in:\n{output_dir}\n"
        yield output_text
    except Exception as e:
        yield f"Error processing YAML file: {str(e)}"

def docmaker_with_prompt(yaml_file, prompt_input, model_choice):
    if not yaml_file:
        return "Error: No YAML file uploaded"
    if not prompt_input.strip():
        output_lines = []
        for line in docmaker(yaml_file):
            if isinstance(line, str):
                output_lines.append(line)
        base_output = "\n".join(output_lines)
    else:
        base_output = ""
    try:
        import tools.docmaker as docmaker_module
        # Override model if a choice is provided.
        if model_choice:
            docmaker_module.MODEL = model_choice
        # Override chat_completion if custom prompt is provided.
        if prompt_input.strip():
            original_chat = docmaker_module.chat_completion
            def custom_chat(prompt):
                return original_chat(prompt_input)
            docmaker_module.chat_completion = custom_chat
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            docmaker_module.process_yaml_files()
        printed_output = f.getvalue()
        # Restore chat_completion if overridden.
        if prompt_input.strip():
            docmaker_module.chat_completion = original_chat
        filename = Path(yaml_file).name
        output_dir = Path("output/docmaker") / Path(filename).stem
        final_output = base_output + printed_output + f"\n✨ Processing complete!\n\n📂 Generated documentation can be found in:\n{output_dir}\n"
        return final_output
    except Exception as e:
        return f"Error processing YAML file: {str(e)}"

def edit_image():
    pass

def face_swap():
    pass

def flux():
    pass

def image_captioning():
    pass

def image_upscaler():
    pass

def stable_diffusion():
    pass

def text_to_speech():
    pass

with gr.Blocks(theme='gradio/default') as chugger:
    title = (
        """
<center> 
<h1> ChuggingFace Toolkit! </h1>
<h3> ‼️ Requires a 🤗HuggingFace API token in .env file ‼️ </h3>
</center>
        """
    )
    with gr.Row():
        gr.HTML(title)
    with gr.Tabs():
        with gr.Tab("Background Removal"):
            gr.Markdown("Remove background from images using AI.")
            with gr.Row():
                with gr.Column():
                    input_images = gr.File(label="Upload Images", file_count="multiple", type="filepath")
                    process_btn = gr.Button("Remove Backgrounds", variant="primary")
                with gr.Column():
                    output_text = gr.Textbox(label="Processing Status", placeholder="Processing output will appear here...", lines=4)
            output_gallery = gr.Gallery(label="Processed Images (Input | Output)", show_label=True, elem_id="gallery", columns=[2], rows=[1], preview=True)
            process_btn.click(fn=background_removal, inputs=[input_images], outputs=[output_text, output_gallery], show_progress=True)
        with gr.Tab("Canny Edge Detection"):
            gr.Markdown("Generate Canny edge-maps from images. This is not an AI solution. AI edge detection is COMING SOON!")
            with gr.Row():
                with gr.Column():
                    canny_input_images = gr.File(label="Upload Images", file_count="multiple", type="filepath")
                    canny_process_btn = gr.Button("Generate Edge Maps", variant="primary")
                with gr.Column():
                    canny_output_text = gr.Textbox(label="Processing Status", placeholder="Processing output will appear here...", lines=4)
            canny_output_gallery = gr.Gallery(label="Processed Images (Input | Output)", show_label=True, elem_id="canny_gallery", columns=[2], rows=[1], preview=True)
            canny_process_btn.click(fn=canny_edge_detect, inputs=[canny_input_images], outputs=[canny_output_text, canny_output_gallery], show_progress=True)
        with gr.Tab("Image Depth Maps"):
            gr.Markdown("Generate depth maps using DepthAnythingv2.")
            with gr.Row():
                with gr.Column():
                    depth_input_images = gr.File(label="Upload Images", file_count="multiple", type="filepath")
                    depth_process_btn = gr.Button("Generate Depth Maps", variant="primary")
                with gr.Column():
                    depth_output_text = gr.Textbox(label="Processing Status", placeholder="Processing output will appear here...", lines=4)
            depth_output_gallery = gr.Gallery(label="Processed Images (Input | RGB Depth | B&W Depth)", show_label=True, elem_id="depth_gallery", columns=[3], rows=[1], preview=True)
            depth_process_btn.click(fn=depth_anything, inputs=[depth_input_images], outputs=[depth_output_text, depth_output_gallery], show_progress=True)
        with gr.Tab("DocMaker"):
            gr.Markdown("Convert YAML files into Markdown documentation. This script is NOT quick! Check the terminal for updates.")
            with gr.Row():
                with gr.Column():
                    yaml_file = gr.File(label="Upload YAML File", file_count="single", type="filepath")
                    custom_prompt = gr.Textbox(label="Custom Prompt", placeholder="Enter custom prompt to override the default prompt (optional)", lines=2)
                    model_choice = gr.Dropdown(label="Select Model", choices=["Qwen/Qwen2.5-Coder-32B-Instruct", "meta-llama/Llama-3.1-70B-Instruct", "meta-llama/Llama-3.3-70B-Instruct", "mistralai/Mixtral-8x7B-Instruct-v0.1"], value="Qwen/Qwen2.5-Coder-32B-Instruct")
                    docmaker_btn = gr.Button("Generate Documentation", variant="primary")
                with gr.Column():
                    docmaker_output = gr.Textbox(label="Processing Status", placeholder="Processing output will appear here...", lines=16)
            docmaker_btn.click(fn=docmaker_with_prompt, inputs=[yaml_file, custom_prompt, model_choice], outputs=[docmaker_output], show_progress=True)
        with gr.Tab("AI Image Editor"):
            gr.Markdown("Transform images using AI with a prompt. COMING SOON!")
        with gr.Tab("Face Swap"):
            gr.Markdown("Swap faces between source and target images. COMING SOON!")
        with gr.Tab("FLUX.1 AI Images"):
            gr.Markdown("Generate images using FLUX.1 Dev or Schnell models. COMING SOON!")
        with gr.Tab("Image Captioning"):
            gr.Markdown("Create text captions for images. COMING SOON!")
        with gr.Tab("Image Upscaler"):
            gr.Markdown("Upscale images and enhance facial details. COMING SOON!")
        with gr.Tab("Stable Diffusion AI Images"):
            gr.Markdown("Generate images using Stability AI models. COMING SOON!")
        with gr.Tab("Text to Speech"):
            gr.Markdown("Convert text into WAV audio files. COMING SOON!")
if __name__ == "__main__":
    ensure_directories()
    chugger.launch(pwa=False)