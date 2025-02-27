<div align="center">

# <img src="chuggingface_toolkit.png" width="40" alt="ChuggingFace"> **ChuggingFace Toolkit** <img src="chuggingface_toolkit.png" width="40" alt="ChuggingFace"> 

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/p9iaai)

This project is primarily designed for prototyping and leverages both 🤗HuggingFace Spaces and Serverless Inference API.

All scripts can be used with ***`ZERO`*** API costs and was developed in `Python v3.11.9`

---

## 🛠 **Available Tools**

See individual tool docs in `.docs` folder for more information.

Tools marked with 🔄 indicate that the Space is running on CPU.

Usage of these `🔄tools` will not count against your `🤗Serverless API` or `🤗Spaces API` GPU time.

| Tool | Description | API |
| :-: | :-: | :-: |
| `background-removal.py` | Removes backgrounds from images | Spaces API 🤗 |
| `canny-edge-detect.py` | Generates Canny edge maps from images | Spaces API 🤗 🔄 |
| `depth-anything.py` | Generates depth maps using DepthAnythingv2 | Spaces API 🤗 |
| `docmaker.py` | Converts YAML files into Markdown docs | 🤗 Serverless API |
| `edit-image.py` | Transform images using AI with a prompt | Spaces API 🤗 |
| `face-swap.py` | Swap faces between a source and target image | Spaces API 🤗 |
| `flux.1,py` | FLUX.1 AI image generation | 🤗 Serverless API |
| `image-captioning.py` | Creates text captions for images | 🤗 Serverless API |
| `image-upscaler.py` | Upscales images and enhances facial details | Spaces API 🤗 |
| `stable-diffusion.py` | Stable Diffusion AI image generation | 🤗 Serverless API |
| `text-to-speech.py` | Converts text into a WAV audio file | 🤗 Serverless API |

---

## <img src="chuggingface_toolkit.png" width="40" alt="ChuggingFace"> ChuggingFace UI! <img src="chuggingface_toolkit.png" width="40" alt="ChuggingFace">

### You can now use the first 4 tools in the new UI!
### Run `chuggingface-ui.py`! A Gradio app will spin up on `port 7860`.
### It is essentially `monkey-patching` the tool scripts which remain unchanged so you can still use them individually.
### Full UI will be completed when I get around to it as I am currently working on another large personal project.

---

## 📦 Requirements

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)

`🤗HuggingFace` Account & `Read` API Token (*`FREE`* or <img src=".docs/.assets/hf_pro.png" width="34">)

---

### 🔗 API Usage & Limits

**UPDATED: 4th Feb. 2025**

The `🤗HuggingFace` Inference API now operates on a credit-based system:

| Account Type | Monthly `🤗Serverless API` Credits |
| :-: | :-: |
| *`FREE`* | Less than $0.10 |
| <img src=".docs/.assets/hf_pro.png" width="34"> | $2.00 |

The `🤗HuggingFace` <img src=".docs/.assets/hf_zerogpu.png" width="48"> time remains the same (for `Spaces API🤗` scripts):

| Account Type | Daily `Spaces API🤗` Credits |
| :-: | :-: |
| *`FREE`* | 5 Minutes <img src=".docs/.assets/hf_zerogpu.png" width="48">|
| <img src=".docs/.assets/hf_pro.png" width="34"> | 25 Minutes <img src=".docs/.assets/hf_zerogpu.png" width="48">|

---

### 💵 Pricing

Charges based on compute time × hardware price

Example: 10-second `🤗Serverless API` request on GPU ($0.00012/sec) = $0.0012

**Important Notes:**

**When credits are depleted:**

**Free users:** API access stops  
**PRO/Enterprise users:** Additional usage billed beyond subscription

Not intended for heavy production use  
Authentication required (`token or browser`)  
Monitor usage on billing page (`PRO`/`Enterprise`)  

**For production-scale applications, consider:**

Inference Endpoints (`dedicated resources`)  
Inference Providers (`serverless usage`)

---

## 📑 Key Notes

**Synchronous Execution:** Scripts are designed to process API calls sequentially to be mindful of free-tier server limitations. While asynchronous execution is possible, it may lead to inefficient API usage for free-tier users.

**Gated Models:** Some models require access approval. Visit the respective `🤗HuggingFace` model pages to request access. Details and links are available in `.gated-models.md` in the `.docs` folder.

**Portability:** Each script is confined to a single file for easy integration into function calling or agentic tools.

**Important Notice Regarding Spaces API:** See `.IMPORTANT.md` in `.docs/.api/` folder.

<div align="left">

---

## 🚀 Quick Setup

### Using Setup Script

**Windows** `.\setup.bat`

**Linux/MacOS** `chmod +x setup.sh` then `./setup.sh`

- **Note for MacOS:** Requires Python 3. Install via `brew install python` if needed.

### Add HuggingFace Token
Add your token to `.env`:
```text
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 😎 Manual Installation

1. Create and activate virtual environment:
```terminal
# Create
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Linux/MacOS)
source .venv/bin/activate
```

2. Install dependencies:
```terminal
pip install -r requirements.txt
```

3. Create required directories and .env:
```terminal
mkdir .logs input output
echo. > .env  # Windows
touch .env    # Linux/MacOS
```

4. Add your HuggingFace token to `.env`:
```text
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

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
