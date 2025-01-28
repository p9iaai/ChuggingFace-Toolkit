# FLUX.1 Image Generation Script

This script generates images based on text prompts using the 🤗HuggingFace Serverless Inference API. It supports 2 models (`FLUX.1-schnell` and `FLUX.1-dev`) and includes robust error handling, retry mechanisms, and logging.

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Usage](#usage)
4. [Parameters](#parameters)
5. [Output](#output)
6. [Logs](#logs)
7. [Terminal](#terminal)
8. [Example Prompts](#example-prompts)
9. [Troubleshooting](#troubleshooting)

---

## Features

- **Text-to-Image Generation**: Generate images from text prompts using 🤗HuggingFace Serverless Inference API models.
- **Model Switcher**: Easily switch between supported models (`FLUX.1-schnell` and `FLUX.1-dev`).
- **Robust Error Handling**: Retry mechanism with exponential backoff for handling API errors and timeouts.
- **Logging**: Save prompts, seeds, and output paths to a log file for easy tracking.
- **Customizable Parameters**: Adjust image dimensions, guidance scale, number of inference steps, and more.

---

## Usage

### Basic Usage

To generate an image using the default model `FLUX.1-schnell` (default 6 denoising steps):

```python
generate_image("a futuristic cityscape at sunset")
```

### Switching Models

To generate an image using `FLUX.1-dev` (increase denoise steps for this model):

```python
generate_image("a futuristic cityscape at sunset", model="FLUX.1-dev", num_inference_steps=24)
```

### Full Example

Here’s an example of generating multiple images with different models:

```python
generate_image("a sentient toaster wearing a top hat and monocle")
generate_image("a group of squirrels playing poker in a tree", model="FLUX.1-dev", num_inference_steps=24)
```

## Parameters

### `generate_image` Function
- **NOTE: There is no negative prompting in FLUX.1 models.**

| Parameter         | Type  | Default Value    | Description |
|------------------|------|----------------|-------------|
| `prompt`        | `str`  | **Required**    | The text prompt to generate the image. |
| `model`         | `str`  | `"FLUX.1-schnell"` | The model to use (`"FLUX.1-schnell"` or `"FLUX.1-dev"`). |
| `guidance_scale` | `float` | `7.5` | Controls how closely the image follows the prompt. Higher values = stricter. |
| `num_inference_steps` | `int` | `6` | The number of denoising steps. More steps = higher quality (but slower). |
| `width`         | `int`  | `1024` | The width of the output image in pixels. |
| `height`        | `int`  | `576`  | The height of the output image in pixels. |
| `max_retries`   | `int`  | `9`    | The maximum number of retries for failed requests. |

- The default `num_inference_steps` is set to 6 for `FLUX.1-schnell`. You should make this 20~24 for `FLUX.1-dev`.

---

## Output

### Image Files

- Images are saved in the `output/flux.1/{model}` directory.
- Filename format: `{timestamp}_{width}x{height}.png`

#### Example:

```text
output/flux.1/FLUX.1-schnell/1737304723_1024x576.png
```

## Logs

### Log Files

- Text log is saved in the `.logs` directory.
- Filename: `flux.1.txt`

#### Example log entry:

```text
PNG SAVED TO   output/flux.1/FLUX.1-schnell\1737865936_1024x1024.png
MODEL          FLUX.1-schnell
SEED           4968401431917961061
GUIDANCE       7.5
STEPS          6
RESOLUTION     1024x1024
PROMPT         a cartoon styled image of a pirate ship

PNG SAVED TO   output/flux.1/FLUX.1-schnell\1737866049_1024x1024.png
MODEL          FLUX.1-schnell
SEED           2023399241889761214
GUIDANCE       7.5
STEPS          6
RESOLUTION     1024x1024
PROMPT         a comic book styled image of a pirate ship
```

## Terminal

#### Example Terminal output:

<img src=".assets/flux_terminal.PNG" alt="Terminal Example Screen" />

## Example Prompts

### Here are some fun and creative prompts you can use:

```python
generate_image("a sentient toaster wearing a top hat and monocle, hosting a tea party for other kitchen appliances")
generate_image("a group of squirrels playing poker in a tree, with one squirrel dramatically revealing a royal flush")
generate_image("a giant rubber duck floating in a bathtub ocean, with tiny sailboats sailing around it")
generate_image("a cat dressed as a medieval knight, riding a Roomba into battle against a horde of vacuum cleaners")
generate_image("a penguin in a Hawaiian shirt, surfing on a wave made of ice cubes in the middle of a desert")
generate_image("a raccoon wearing a lab coat, conducting experiments on a pile of glitter and marshmallows")
generate_image("a banana wearing sunglasses, skateboarding down a rainbow while being chased by a gang of jealous oranges")
generate_image("a dragon wearing a chef's hat, grilling marshmallows with its fire breath while unicorns watch in awe")
generate_image("a group of robots having a dance-off in a futuristic nightclub, with lasers and disco balls everywhere")
generate_image("a sloth dressed as a superhero, flying through the sky at the speed of 'meh' while eating a taco")
```

## Troubleshooting

### Common Issues

1. **API Timeouts:**

    - Increase the timeout parameter in the `generate_image_with_timeout` function.
    - Ensure your internet connection is stable.

2. **Model Not Ready:**

    - The script automatically retries with the `x-wait-for-model` header. If the model is still not ready, check the 🤗HuggingFace API status.

3. **Invalid Model Name:**

    - Ensure the model name is correct - `FLUX.1-dev` or `FLUX.1-schnell`.

4. **Missing .env File:**

    - Ensure the `.env` file exists and contains your 🤗HuggingFace API token.

5. **Speed:**

    - Don't expect this script to be particularly quick.  It will process all of your prompts (unless it skips after max retries) but we are dealing with a free API that is sufficiently busy most of the time.  Best advice is go grab a drink and let it run if you're processing a lot of prompts.  I've successully tested with over 100 prompts with no issue, other than the wait of course.

---
