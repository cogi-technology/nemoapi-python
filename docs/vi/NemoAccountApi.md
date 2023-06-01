# nemo_api.NemoAccountApi

| Phương thức   | Yêu cầu HTTP     | Mô tả |
------------- | ------------- | -------------
[**get_link**](NemoAccountApi.md#get_link) | **POST** /account/get_link | Lấy danh sách địa chỉ ví Metamask đã liên kết với Nemo wallet
[**get_nemo_wallet**](NemoAccountApi.md#get_nemo_wallet) | **POST** /account/get_nemo_wallet | Lấy địa chỉ ví Nemo bằng địa chỉ ví Metamask đã liên kết

# **get_link**
> list[str] get_link(main_account)

Lấy danh sách địa chỉ ví Metamask đã liên kết với Nemo wallet.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
NEMO_ACCOUNT = "<nemo_account>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.NemoAccountApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.get_link(NEMO_ACCOUNT)
    print(api_response)
except Exception as e:
    print("Exception when calling NemoAccountApi->get_link: %s\n" % e)
```

### Parameters

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
------------- | ------------- | ------------- | -------------
 **main_account** | **str**| Địa chỉ ví NEMO | 

### Kiểu kết quả trả về

**list[str]**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **get_nemo_wallet**
> object get_nemo_wallet(sub_account)

Lấy địa chỉ ví Nemo bằng địa chỉ ví Metamask đã liên kết.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
SUB_ACCOUNT = "<sub_account>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.NemoAccountApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.get_nemo_wallet(SUB_ACCOUNT)
    print(api_response)
except Exception as e:
    print("Exception when calling NemoAccountApi->get_nemo_wallet: %s\n" % e)
```

### Parameters

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
------------- | ------------- | ------------- | -------------
 **sub_account** | **str**| Địa chỉ ví Metamasks | 

### Kiểu kết quả trả về

**object**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)