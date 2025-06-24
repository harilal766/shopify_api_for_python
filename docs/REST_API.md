

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



