# nemo_api.SubgraphApi

Phương thức | Yêu cầu HTTP | Mô tả
------------- | ------------- | -------------
[**call**](SubgraphApi.md#call) | **POST** /subgraph/call | Thực thi một truy vấn GraphQL trên subgraph
[**getTotalVolume**](SubgraphApi.md#gettotalvolume) | **POST** /subgraph/getTotalVolume | Tính tổng khối lượng của thị trường trên subgraph

# **call**
> object call(params)

Thực thi một truy vấn GraphQL.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
VARIABLES = "<variables>"
QUERY = "<query>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.SubgraphApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.call({
        "variables": VARIABLES,
        "query": QUERY
    })
    print(api_response)
except Exception as e:
    print("Exception when calling SubgraphApi->call: %s\n" % e)
```

### Tham số

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
------------- | ------------- | ------------- | -------------
 **params** | **dict**| Các tham số để yêu cầu POST đến GraphQL | 

### Kiểu trả về

**object**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **getTotalVolume**
> object getTotalVolume(params)

Lấy tổng khối lượng của thị trường trên subgraph.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
VARIABLES = "<variables>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.SubgraphApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.getTotalVolume(VARIABLES)
    print(api_response)
except Exception as e:
    print("Exception when calling SubgraphApi->getTotalVolume: %s\n" % e)
```

### Tham số

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
------------- | ------------- | ------------- | -------------
 **params** | **dict**| Các biến cho phép bạn tham số hóa các truy vấn và sửa đổi | 

### Kiểu trả về

**object**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)