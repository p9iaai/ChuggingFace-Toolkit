# Suno Bark Text-to-Speech Script

This Python script uses the Suno Bark model from 🤗HuggingFace to convert text input into audio files.

## Features

- Converts text to speech using the Suno Bark model
- Automatically sanitizes input text to create valid filenames
- Saves output as .wav files in the `output/text-to-speech/` directory

## Usage

1. Run the script from the root:

```bash
python tools/text-to-speech.py
```

2. Enter the text you want to convert when prompted

3. The audio file will be saved in the `output/text-to-speech/` directory

## File Structure

```text
.
├── tools/
│   └── suno-bark-tts.py    # Main script
└── output/
    └── suno-bark/          # Directory for audio output
```

## API Details

- Model: [suno/bark](https://huggingface.co/suno/bark)
- Endpoint: `https://api-inference.huggingface.co/models/suno/bark`
- Authorization: Bearer token required (`HF_TOKEN` in `.env`)

## Example

```bash
python tools/text-to-speech.py
```

## Terminal

#### Example Terminal output:

<img src = ".assets/text_to_speech_terminal.PNG" />

## Notes

- Output files are saved as .wav format
- Filenames are automatically generated from input text:
  - Special characters are removed
  - Spaces are replaced with underscores
  - Length is limited to 50 characters
- Ensure the `output/text-to-speech/` directory exists before running the script
- The model is uncensored.

---

<div align="center">

**ChuggingFace is very pleased...**

<img src=".assets/chuggingface_toolkit.png" width="512" alt="ChuggingFace">

---

**p9iaai** <img src=".assets/p9iaai.png" width="32" align="middle"> **2025**

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/p9iaai)

---

</div>
