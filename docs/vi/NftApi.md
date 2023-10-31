# nemo_api.NftApi

Phương thức | Yêu cầu HTTP | Mô tả
------------- | ------------- | -------------
[**mint**](NftApi.md#mint) | **POST** /nft/mint | Gửi một giao dịch để tạo một NFT và chuyển nó cho một tài khoản, được thực thi bởi Minter. Nhận UUID của NFT nếu thành công
[**request_mint**](NftApi.md#request_mint) | **POST** /nft/request_mint | Gửi một giao dịch để tạo một NFT và chuyển nó cho một tài khoản, được thực thi bởi người dùng. Nhận UUID của NFT nếu thành công

# **mint**
> str mint(recipient, metadata, callback)

Đúc một NFT.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
RECIPIENT = "<account>"
METADATA = "<metadata>"
CALLBACK = "<callback>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.NftApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.mint(RECIPIENT, METADATA, CALLBACK)
    print(api_response)
except Exception as e:
    print("Exception when calling NftApi->mint: %s\n" % e)
```

### Tham số

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
------------- | ------------- | ------------- | -------------
 **recipient** | **str**| Tài khoản | 
 **metadata** | **dict**| Metadata của NFT | 
 **callback** | **str**| Đường dẫn callback | 

### Kiểu trả về

**str**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **request_mint**
> str request_mint(recipient, metadata, callback)

Yêu cầu tạo một NFT.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
RECIPIENT = "<account>"
METADATA = "<metadata>"
CALLBACK = "<callback>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.NftApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.request_mint(RECIPIENT, METADATA, CALLBACK)
    print(api_response)
except Exception as e:
    print("Exception when calling NftApi->request_mint: %s\n" % e)
```

### Tham số

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
------------- | ------------- | ------------- | -------------
 **recipient** | **str**| Tài khoản | 
 **metadata** | **dict**| Metadata của NFT | 
 **callback** | **str**| Đường dẫn callback | 

### Kiểu trả về

**str** 

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **mints**
> list[object] mints(nfts)

Đúc hàng loạt NFT.

### Example

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
NFTs = "<NFTs>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.NftApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.mints(NFTs)
    print(api_response)
except Exception as e:
    print("Exception when calling NftApi->mints: %s\n" % e)
```

### Tham số

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
------------- | ------------- | ------------- | -------------
 **payload** | **list[dict]**| Danh sách các tham số của mint | 

### Kiểu trả về

**list[object]**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)