# API documentation

- `p9iaai/upscaler`
  - A duplicated space from `smartfeed/image_hd`

## API Endpoint

1. Install the python client (docs) if you don't already have it installed.

```bash
$ pip install gradio_client
```

2. Find the API endpoint below corresponding to your desired function in the app. Copy the code snippet, replacing the placeholder values with your own input data.

### `api_name: /enhance_image`

```python
from gradio_client import Client, handle_file

client = Client("p9iaai/upscaler")
result = client.predict(
		input_image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
		scale=2,
		enhance_mode="Face Enhance + Image Enhance",
		api_name="/enhance_image"
)
print(result)
```

Accepts 3 parameters:

- input_image `Dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: Dict())` **Required**

The input value that is provided in the "Input Image" Image component. For input, either path or url must be provided. For output, path is always provided.

- scale `float` **Default: 2**

The input value that is provided in the "Scale" Slider component.

- enhance_mode `Literal['Only Face Enhance', 'Only Image Enhance', 'Face Enhance + Image Enhance']` **Default: "Face Enhance + Image Enhance"**

The input value that is provided in the "Enhance Mode" Dropdown component.

Returns tuple of 2 elements:

[0] `Dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: Dict())`

The output value that appears in the "Enhanced Image" Image component.

[1] `filepath`

The output value that appears in the "Download the Enhanced Image" File component.
