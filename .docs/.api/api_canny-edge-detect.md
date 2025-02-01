# API documentation

- `p9iaai/canny-edge-detect`
  - A duplicated space from `ameerazam08/find-canny`

## API endpoint

Choose a language to see the code snippets for interacting with the API.

1. Install the python client (docs) if you don't already have it installed.

```terminal
pip install gradio_client
```

2. Find the API endpoint below corresponding to your desired function in the app. Copy the code snippet, replacing the placeholder values with your own input data.

### `api_name: /predict`

```python
from gradio_client import Client, handle_file

client = Client("p9iaai/canny-edge-detect")
result = client.predict(
        img=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
        api_name="/predict"
)
print(result)
```

Accepts 1 parameter:

- img `dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict())` **Required**

The input value that is provided in the "img" Image component. For input, either path or url must be provided. For output, path is always provided.

Returns 1 element:

- `dict(path: str | None (Path to a local file), url: str | None (Publicly available url or base64 encoded image), size: int | None (Size of image in bytes), orig_name: str | None (Original filename), mime_type: str | None (mime type of image), is_stream: bool (Can always be set to False), meta: dict())`

The output value that appears in the "output" Image component.
