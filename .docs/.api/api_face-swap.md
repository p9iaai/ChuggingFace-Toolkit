# API documentation

- `p9iaai/face-swap`
  - A duplicated space from `tuan2308/face-swap`

## API Endpoint

1. Install the python client (docs) if you don't already have it installed.

```terminal
pip install gradio_client
```

2. Find the API endpoint below corresponding to your desired function in the app. Copy the code snippet, replacing the placeholder values with your own input data.

### `api_name: /predict`

```python
from gradio_client import Client, handle_file

client = Client("p9iaai/face-swap")
result = client.predict(
	source_file=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
	target_file=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
	doFaceEnhancer=False,
	api_name="/predict"
)
print(result)
```

Accepts 3 parameters:

- source_file `filepath` **Required**

The input value that is provided in the "parameter_0" Image component.

- target_file `filepath` **Required**

The input value that is provided in the "parameter_1" Image component.

- doFaceEnhancer `bool` **Default: False**

The input value that is provided in the "Face Enhancer?" Checkbox component.

Returns 1 element:

`filepath`

The output value that appears in the "output" Image component.
