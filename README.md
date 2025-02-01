<div align="center">

---

# <img src="chuggingface_toolkit.png" width="40" alt="ChuggingFace"> ChuggingFace Toolkit <img src="chuggingface_toolkit.png" width="40" alt="ChuggingFace"> 

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/p9iaai)

<div align="left">

This project is designed for prototyping and leverages both 🤗HuggingFace Spaces and the Serverless Inference API. All scripts can be used at ***`ZERO`*** cost.

Developed in `Python v3.11.9`

## 📑 Key Notes

- **Synchronous Execution:** Scripts are designed to process API calls sequentially to be mindful of free-tier server limitations. While asynchronous execution is possible, it may lead to inefficient API usage for free-tier users.
- **Gated Models:** Some models require access approval. Visit the respective 🤗HuggingFace model pages to request access. Details and links are available in `.gated-models.md` in the `.docs` folder.
- **Portability:** Each script is confined to a single file for easy integration into function calling or agentic tools.
- **Important Notice Regarding Spaces API:** See `.IMPORTANT.md` in `.docs/.api/` folder.

## 🚀 Quick Setup

- **Windows**
  - Run the setup script:
    - `.\setup.bat`

- **Linux**
  - Make the setup script executable by running:
    - `chmod +x setup.sh`
  - Run the script:
    - `./setup.sh`

- **MacOS**
  - **Python 3:** macOS comes with Python 2 pre-installed, but Python 3 is required for this script. Ensure Python 3 is installed. You can install it via Homebrew (recommended):
    - `brew install python`
  - After installation, verify that `python3` is available:
    - `python3 --version`
  - Make the setup script executable by running:
    - `chmod +x setup.sh`
  - Run the script:
    - `./setup.sh`

- Add your 🤗HuggingFace token to the .env file:

```text
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## 😎 Manual Installation

For users who want to understand or customize the setup process, here are the manual steps equivalent to running `setup.bat`:

1. **Create Virtual Environment**

   ```terminal
   python -m venv .venv
   ```

2. **Activate Virtual Environment**

   ```terminal
   # Windows
   .venv\Scripts\activate
   
   # Linux/MacOS
   source .venv/bin/activate
   ```

3. **Upgrade pip**

   ```terminal
   python -m pip install --upgrade pip
   ```

4. **Install Requirements**

   ```terminal
   pip install -r requirements.txt
   ```

5. **Create Folder Structure**

   ```terminal
   mkdir .logs
   mkdir input
   mkdir output
   ```

6. **Create .env File**

   ```terminal
   if not exist .env echo. > .env
   ```

7. **Add HuggingFace Token**

Edit the `.env` file and add your 🤗HuggingFace token:

```text
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 📦 Requirements

- Python 3.7+

- 🤗HuggingFace Account & API Token (*`FREE`* or <img src=".docs/.assets/hf_pro.png" width="34">)

  - *`FREE`* accounts include:

    - 5 minutes of <img src=".docs/.assets/hf_zerogpu.png" width="56"> GPU time per day.
    - 1000 Inference API requests per day.

  - *<img src=".docs/.assets/hf_pro.png" width="34">* accounts include:

    - 25 minutes of <img src=".docs/.assets/hf_zerogpu.png" width="56"> GPU time per day.
    - 20,000 Inference API requests per day.

- API Usage:

  - `🤗Spaces API` scripts consume <img src=".docs/.assets/hf_zerogpu.png" width="56"> GPU time.
  - `🤗Serverless API` scripts consume API requests.

## 🛠 Available Tools

See individual tool docs in `.docs` folder for more information.

Tools marked with 🔄 indicate that the Space is running on CPU.

- Usage of these tools will not count against your `🤗Serverless API` or `🤗Spaces API` <img src=".docs/.assets/hf_zerogpu.png" width="56"> GPU time.

---

| Tool | Description | API |
| --: | :-: | :-- |
| `background-removal.py` | Removes backgrounds from images in a specified folder. | Spaces API 🤗 |
| `canny-edge-detect.py` | Generates Canny edge-maps from images in input folder. | Spaces API 🤗 🔄 |
| `depth-anything.py` | Generates state-of-the-art depth maps using DepthAnythingv2. | Spaces API 🤗 |
| `docmaker.py` | Converts YAML files into Markdown documentation. | 🤗 Serverless API |
| `edit-image.py` | Transform images using AI with a prompt. | Spaces API 🤗 |
| `face-swap.py` | Swaps faces between a source and target image. | Spaces API 🤗 |
| `flux.1,py` | Generate images using FLUX.1 Dev or Schnell models. | 🤗 Serverless API |
| `image-captioning.py` | Creates text captions for images in a folder. | 🤗 Serverless API |
| `image-upscaler.py` | Upscales images (2x, 3x, 4x) and optionally enhances facial details. | Spaces API 🤗 |
| `stable-diffusion.py` | Generates images using Stability AI diffusion models. | 🤗 Serverless API |
| `text-to-speech.py` | Converts text into a WAV audio file. | 🤗 Serverless API |

## 🧠 Contributing Guidelines

We welcome contributions to enhance this toolkit! Please follow these guidelines when adding new tools:

### Adding New Tools

- Place your tool in the `tools/` folder as a single file
- For tools using the Spaces API:
  - Add API documentation in `.docs/.api/api_{scriptname}.md`
  - Include script documentation in `.docs/{scriptname}.md`
- For tools using the Serverless API:
  - Add script documentation in `.docs/{scriptname}.md`

### Input/Output Management

- If your script requires input:
  - Use the `input/{scriptname}/` folder
- If your script produces output:
  - Use the `output/{scriptname}/` folder

### Logging & Console Output

- Store all logs in the `.logs/` folder
- Keep console output clean and user-friendly:
  - Focus on script progress updates
  - Use emojis sparingly for visual cues
  - Refer to examples in `.docs/` for guidance

### Running Tools

- Configure tools to run from the root directory:

```bash
C:/ChuggingFace-Toolkit> python tools/{scriptname}.py
```
  
- A planned future update requires this. Stay tuned!

### Documentation Assets

Store images and other documentation assets in `.docs/.assets/`

### README Updates

All updates to this main `README.md` will be handled by the maintainers.

We appreciate your contributions and look forward to seeing your tools in action!

---

## 📄 License
- [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

See the [LICENSE](LICENSE) file for the full text of the license.

---

<div align="center">

**ChuggingFace is very pleased...**

<img src="chuggingface_toolkit.png" width="512" alt="ChuggingFace">

---

**p9iaai** <img src="p9iaai.png" width="32" align="middle"> **2025**

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/p9iaai)

---

</div>
