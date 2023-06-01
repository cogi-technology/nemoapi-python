# nemo_api.NemoIdApi

Phương thức | Yêu cầu HTTP | Mô tả
------------- | ------------- | -------------
[**login**](NemoIdApi.md#login) | **POST** /nemoid/login | Đăng nhập và lấy thông tin Tài khoản NemoId
[**user_info**](NemoIdApi.md#user_info) | **POST** /nemoid/user_info | Lấy thông tin Tài khoản NemoId
[**relogin**](NemoIdApi.md#relogin) | **POST** /nemoid/relogin | Đăng nhập lại và lấy thông tin Tài khoản NemoId

# **login**
> NemoIdAccount login(code, code_verifier, redirect_uri)

Đăng nhập.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
CODE = "<code>"
CODE_VERIFIER = "<code_verifier>"
REDIRECT_URI = "<redirect_uri>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.NemoIdApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.login(CODE, CODE_VERIFIER, REDIRECT_URI)
    print(api_response)
except Exception as e:
    print("Exception when calling NemoIdApi->login: %s\n" % e)
```

### Tham số

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
------------- | ------------- | ------------- | -------------
 **code** | **str**| Mã xác thực | 
 **code_verifier** | **str**| Mã xác thực | 
 **redirect_uri** | **str**| Địa chỉ URL chuyển hướng | 

### Kiểu kết quả trả về

[**NemoIdAccount**](NemoIdAccount.md)

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **user_info**
> NemoIdAccount user_info(access_token)

Lấy thông tin Tài khoản NemoId bằng accessToken.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
ACCESS_TOKEN = "<access_token>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.NemoIdApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.user_info(ACCESS_TOKEN)
    print(api_response)
except Exception as e:
    print("Exception when calling NemoIdApi->user_info: %s\n" % e)
```

### Tham số

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access token | 

### Kiểu kết quả trả về

[**NemoIdAccount**](NemoIdAccount.md)

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **relogin**
> NemoIdAccount relogin(refresh_token, code_verifier)

Đăng nhập lại.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
REFRESH_TOKEN = "<refresh_token>"
CODE_VERIFIER = "<code_verifier>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.NemoIdApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.relogin(REFRESH_TOKEN, CODE_VERIFIER)
    print(api_response)
except Exception as e:
    print("Exception when calling NemoIdApi->relogin: %s\n" % e)
```

### Tham số

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**| Refresh token | 
 **code_verifier** | **str**| Mã xác thực | 

### Kiểu kết quả trả về

[**NemoIdAccount**](NemoIdAccount.md)

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

