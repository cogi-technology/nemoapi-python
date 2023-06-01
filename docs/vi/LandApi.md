# nemo_api.LandApi

Phương thức | Yêu cầu HTTP | Mô tả
------------- | ------------- | -------------
[**mint**](LandApi.md#mint) | **POST** /land/mint | Đúc NFT Land và chuyển nó cho một tài khoản, được thực hiện bởi Minter. Nhận UUID của NFT Land nếu thành công.
[**request_mint**](LandApi.md#request_mint) | **POST** /land/request_mint | Đúc NFT Land và chuyển nó cho một tài khoản, được thực hiện bởi người dùng. Nhận UUID của NFT Land nếu thành công.
[**mints**](LandApi.md#mints) | **POST** /land/mints | Gửi giao dịch để tạo ra nhiều NFT Land, được thực hiện bởi Minter.
[**request_mints**](LandApi.md#request_mints) | **POST** /land/request_mints | Gửi giao dịch để tạo ra nhiều NFT Land, được thực hiện bởi người dùng.
[**request_cancelbuys**](LandApi.md#request_cancelbuys) | **POST** /land/request_cancelbuys | Gửi yêu cầu hủy giao dịch mua hàng.

# **mint**
> str mint(recipient, land_id, level, land_x, land_y, metadata, callback)

Tạo một NFT Land.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
RECIPIENT = "<recipient>"
LAND_ID = "<land_id>"
LEVEL = "<level>"
LAND_X = "<land_x>"
LAND_Y = "<land_y>"
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
api_instance = nemo_api.LandApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.mint(RECIPIENT, LAND_ID, LEVEL, LAND_X, LAND_Y, METADATA, CALLBACK)
    print(api_response)
except Exception as e:
    print("Exception when calling LandApi->mint: %s\n" % e)
```

### Tham số

Tên | Kiểu dữ liệu | Sự mô tả | Ghi chú
------------- | ------------- | ------------- | -------------
 **recipient** | **str**| Tài khoản | 
 **land_id** | **str**| Id Land | 
 **level** | **str**| Cấp độ Land | 
 **land_x** | **str**| Vị trí X | 
 **land_y** | **str**| Vị trí Y | 
 **metadata** | **dict**| Dữ liệu phân loại Land (Metadata) | 
 **callback** | **str**| URI Callback| 

### Kiểu kết quả trả về

**str**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **request_mint**
> str request_mint(recipient, land_id, level, land_x, land_y, metadata, callback)

Yêu cầu đúc một NFT.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
RECIPIENT = "<recipient>"
LAND_ID = "<land_id>"
LEVEL = "<level>"
LAND_X = "<land_x>"
LAND_Y = "<land_y>"
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
api_instance = nemo_api.LandApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.request_mint(RECIPIENT, LAND_ID, LEVEL, LAND_X, LAND_Y, METADATA, CALLBACK)
    print(api_response)
except Exception as e:
    print("Exception when calling LandApi->request_mint: %s\n" % e)
```

### Tham số

Tên | Kiểu dữ liệu | Mô tả  | Ghi chú
------------- | ------------- | ------------- | -------------
 **recipient** | **str**| Tài khoản | 
 **land_id** | **str**| id Land | 
 **level** | **str**| Cấp độ Land | 
 **land_x** | **str**| Vị trí X | 
 **land_y** | **str**| Vị trí Y | 
 **metadata** | **dict**| Metadata của Land | 
 **callback** | **str**| URI gọi lại |

### Kiểu kết quả trả về

**str**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **mints**
> list[object] mints(lands)

Đúc NFT hàng loạt.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
LANDS = "<lands>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.LandApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.mints(LANDS)
    print(api_response)
except Exception as e:
    print("Exception when calling LandApi->mints: %s\n" % e)
```

### Tham số

Tên | Kiểu dữ liệu | Mô tả | Ghi chú
------------- | ------------- | ------------- | -------------
 **lands** | **list[dict]**| Danh sách các tham số để khởi tạo | 

### Kiểu kết quả trả về

**list[object]**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **request_mints**
> list[object] request_mints(lands)

Mint NFT hàng loạt.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
LANDS = "<lands>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.LandApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.request_mints(LANDS)
    print(api_response)
except Exception as e:
    print("Exception when calling LandApi->request_mints: %s\n" % e)
```

### Tham số

Tên | Kiểu dữ liệu | Mô tả | Ghi chú
------------- | ------------- | ------------- | -------------
 **lands** | **list[dict]**| Danh sách các tham số để khởi tạo | 

### Kiểu kết quả trả về

**list[object]**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **request_cancelbuys**
> list[object] request_cancelbuys(lands)

Yêu cầu hủy lệnh mua NFT.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
LANDS = "<lands>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.LandApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.request_cancelbuys(LANDS)
    print(api_response)
except Exception as e:
    print("Exception when calling LandApi->request_cancelbuys: %s\n" % e)
```

### Tham số

Tên | Kiểu dữ liệu | Mô tả | Ghi chú
------------- | ------------- | ------------- | -------------
 **lands** | **list[dict]**| Danh sách của các đối tượng gồm account và cid | 

### Kiểu kết quả trả về

**list[object]**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)