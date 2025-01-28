# API documentation

- `p9iaai/background-removal`
  - A duplicated space from `not-lain/background-removal`

## 3 API endpoints

1. Install the python client if you don't already have it installed.

```bash
pip install gradio_client
```

2. Find the API endpoint below corresponding to your desired function in the app. Copy the code snippet, replacing the placeholder values with your own input data. If this is a private Space, you may need to pass your Hugging Face token as well.

### `api_name: /image`

```python
from gradio_client import Client, handle_file

client = Client("p9iaai/background-removal")
result = client.predict(
		image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
		api_name="/image"
)
print(result)
```

Accepts 1 parameter:

- image `filepath` **Required**

The input value that is provided in the "Upload an image" Image component.

Returns 1 element:

- `Tuple[filepath | None, filepath | None] | None`

The output value that appears in the "Processed Image" Imageslider component.

### `api_name: /text`

```python
from gradio_client import Client

client = Client("p9iaai/background-removal")
result = client.predict(
		image="Hello!!",
		api_name="/text"
)
print(result)
```

Accepts 1 parameter:

- image `str` **Required**

The input value that is provided in the "Paste an image URL" Textbox component.

Returns 1 element:

- `Tuple[filepath | None, filepath | None] | None`

The output value that appears in the "Processed Image from URL" Imageslider component.

### `api_name: /png`

```python
from gradio_client import Client, handle_file

client = Client("p9iaai/background-removal")
result = client.predict(
		f=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
		api_name="/png"
)
print(result)
```

Accepts 1 parameter:

- f `filepath` **Required**

The input value that is provided in the "Upload an image" Image component.

Returns 1 element:

- `filepath`

The output value that appears in the "Output PNG File" File component.
