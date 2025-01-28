# <img src="chuggingface_toolkit.png" width="32" alt="ChuggingFace"> ChuggingFace Toolkit <img src="chuggingface_toolkit.png" width="32" alt="ChuggingFace">

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow)](https://huggingface.co/)

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

## 🛠 Available Tools

See individual tool docs in `.docs` folder for more information.

| Tool | Description | /API |
| --: | :-: | :-- |
| `background-removal.py` | Removes backgrounds from images in a specified folder. | Spaces API 🤗 |
| `depth-anything.py` | Generates state-of-the-art depth maps using DepthAnythingv2. | Spaces API 🤗 |
| `docmaker.py` | Converts YAML files into Markdown documentation. | 🤗 Serverless API |
| `face-swap.py` | Swaps faces between a source and target image. | Spaces API 🤗 |
| `flux.1,py` | Generate images using FLUX.1 Dev or Schnell models. | 🤗 Serverless API |
| `image-captioning.py` | Creates text captions for images in a folder. | 🤗 Serverless API |
| `image-upscaler.py` | Upscales images (2x, 3x, 4x) and optionally enhances facial details. | Spaces API 🤗 |
| `stable-diffusion.py` | Generates images using Stability AI diffusion models. | 🤗 Serverless API |
| `text-to-speech.py` | Converts text into a WAV audio file. | 🤗 Serverless API |

## 📦 Requirements

- Python 3.7+

- 🤗HuggingFace Account & API Token (*`FREE`* or <img src=".assets/hf_pro.png" width="34">)

  - *`FREE`* accounts include:
    
    - 5 minutes of <img src=".assets/hf_zerogpu.png" width="56"> GPU time.
    - 1000 Inference API requests per day.

  - *<img src=".assets/hf_pro.png" width="34">* accounts include:
    
    - 25 minutes of <img src=".assets/hf_zerogpu.png" width="56"> GPU time.
    - 20,000 Inference API requests per day.

- API Usage:

  - `🤗Spaces API` scripts consume <img src=".assets/hf_zerogpu.png" width="56"> GPU time.
  - `🤗Serverless API` scripts consume API requests.

---

## 🤗 Built with HuggingFace 🤗

<div align="left">

This project is designed for prototyping and leverages both HuggingFace Spaces and the Serverless Inference API. All scripts can be used at ***`ZERO`*** cost.

### Key Notes:

- **Synchronous Execution:** Scripts are designed to process API calls sequentially to be mindful of free-tier server limitations. While asynchronous execution is possible, it may lead to inefficient API usage for free-tier users.
- **Gated Models:** Some models require access approval. Visit the respective HuggingFace model pages to request access. Details and links are available in `.gated-models.md` in the `.docs` folder.
- **Portability:** Each script is confined to a single file for easy integration into function calling or agentic tools.

<div align="center">

**ChuggingFace is very pleased...**

<img src="chuggingface_toolkit.png" width="512" alt="ChuggingFace">

**p9iaai** <img src="p9iaai.png" width="32" align="middle"> **2025**

</div>
