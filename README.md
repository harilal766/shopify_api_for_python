# shopify_api_for_python
Python library to access shopify admin api.

# Installation and running.

- Install the library via pip (not operational right now).
```bash
pip install shopify_api_for_python
``` 
- Or clone the project.
```bash
git clone "https://github.com/harilal766/shopify_api_for_python"
```
- Create a virtual environment
```bash
python -m venv env
```
- Activate the environment
```bash
env/scripts/activate
```

# Overview - REST API

### Supported Endpoints
- orders

### Basic url 
```https://{shop}.myshopify.com/admin/api/{version}/{endpoint}.json```

### Explanation
- `{shop}` : storename given on the hopmepage url of the shopify admin page after logged in.
    Eg : `https://admin.shopify.com/store/237h8-6`, here `237h8-6` is the storename.
- `{version}` : 2025-04 is the current latest version
- `{endpint}` : This will change based on the API model you want to access, right now `orders` is the only supported endpoint.
