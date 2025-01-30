# Face Swap CLI Tool

🌟 A command-line interface for face swapping using 🤗HuggingFace's Gradio API.

## 🚀 Usage

### Basic Usage

1. Place your source and named target images in `input/face-swap`:
   - `source.png` - The face to be swapped
   - `target.png` - The target image
2. Run the script from the root:

   ```terminal
   python tools/face-swap.py
   ```

3. Follow the prompts to enable/disable face enhancement
4. Find your result in `output/face-swap`

### 📂 File Structure

```text
.
├── input/
│   └── face-swap/
│       ├── source.png
│       └── target.png
├── output/
│   └── face-swap/
│       └── face-swap_YYYYMMDD_HHMMSS.png
├── .logs/
│   └── face-swap.txt
└── tools/
    └── face-swap.py
```

### ⚙️ Configuration

- **Face Enhancement**: Enable/disable during runtime
- **Output Format**: PNG format with timestamp
- **Logging**: Detailed logs in `.logs/face-swap.txt`

## 🐛 Troubleshooting

- Check `.logs/face-swap.txt` for detailed error information
- Ensure input images named `source.png` and `target.png` are in the correct directory (`input/face-swap`)
- Verify internet connection for API access

---

<div align="center">

**ChuggingFace is very pleased...**

<img src=".assets/chuggingface_toolkit.png" width="512" alt="ChuggingFace">

---

**p9iaai** <img src=".assets/p9iaai.png" width="32" align="middle"> **2025**

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/p9iaai)

---

</div>
