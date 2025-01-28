# API documentation

- `p9iaai/Depth-Anything-V2`
  - A duplicated space from `depth-anything/Depth-Anything-V2`

## API endpoint

Choose a language to see the code snippets for interacting with the API.

1. Install the python client (docs) if you don't already have it installed.

```terminal
pip install gradio_client
```

2. Find the API endpoint below corresponding to your desired function in the app. Copy the code snippet, replacing the placeholder values with your own input data.

### `api_name: /on_submit`

```python
from gradio_client import Client, handle_file

client = Client("p9iaai/Depth-Anything-V2")
result = client.predict(
	image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
	api_name="/on_submit"
)
print(result)
```

Accepts 1 parameter:

- image `filepath` **Required**

The input value that is provided in the "Input Image" Image component.

Returns tuple of 3 elements:

- [0] `Tuple[filepath | None, filepath | None] | None`

The output value that appears in the "Depth Map with Slider View" Imageslider component.

- [1] `filepath`

The output value that appears in the "Grayscale depth map" File component.

- [2] `filepath`

The output value that appears in the "16-bit raw output (can be considered as disparity)" File component.
