# API documentation

- `p9iaai/edit-image`
  - A duplicated space from `black-forest-labs/FLUX.1-canny-dev`

## API endpoint

Choose a language to see the code snippets for interacting with the API.

1. Install the python client (docs) if you don't already have it installed.

```terminal
pip install gradio_client
```

2. Find the API endpoint below corresponding to your desired function in the app. Copy the code snippet, replacing the placeholder values with your own input data.

### `api_name: /infer`

```python
from gradio_client import Client, handle_file

client = Client("p9iaai/edit-image")
result = client.predict(
        control_image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
        prompt="Hello!!",
        seed=0,
        randomize_seed=True,
        width=1024,
        height=1024,
        guidance_scale=30,
        num_inference_steps=28,
        api_name="/infer"
)
print(result)
```

Accepts 8 parameters:

- control_image `Dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: Dict())` **Required**

The input value that is provided in the "Upload the image for control" Image component. For input, either path or url must be provided. For output, path is always provided.

- prompt `str` **Required**

The input value that is provided in the "Prompt" Textbox component.

- seed `float` **Default: 0**

The input value that is provided in the "Seed" Slider component.

- randomize_seed `bool` **Default: True**

The input value that is provided in the "Randomize seed" Checkbox component.

- width `float` **Default: 1024**

The input value that is provided in the "Width" Slider component.

- height `float` **Default: 1024**

The input value that is provided in the "Height" Slider component.

- guidance_scale `float` **Default: 30**

The input value that is provided in the "Guidance Scale" Slider component.

- num_inference_steps `float` **Default: 28**

The input value that is provided in the "Number of inference steps" Slider component.

Returns tuple of 2 elements:

- [0] `Dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: Dict())`

The output value that appears in the "Result" Image component.

- [1] `float`

The output value that appears in the "Seed" Slider component.
