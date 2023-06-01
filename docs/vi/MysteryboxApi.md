# nemo_api.MysteryboxApi

| Phương thức   | Yêu cầu HTTP     | Mô tả |
| -------------- | ---------------- | ---------------------------------------------------------- |
| **mint**       | **POST** /mysterybox/mint    | Gửi một giao dịch tạo một NFT BOX và chuyển nó đến một tài khoản, được thực thi bởi Minter. Trả về UUID của NFT nếu thành công. |
| **mints**      | **POST** /mysterybox/mints   | Gửi các giao dịch tạo nhiều NFT BOX, được thực hiện bởi Minter. | 

# **mint**
> str mint(box_id, recipient, metadata, callback)

Đúc một NFT BOX.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
BOX_ID = "<box_id>"
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
api_instance = nemo_api.MysteryboxApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.mint(BOX_ID, RECIPIENT, METADATA, CALLBACK)
    print(api_response)
except Exception as e:
    print("Exception when calling MysteryboxApi->mint: %s\n" % e)
```

### Tham số

| Tên | Kiểu dữ liệu | Mô tả | Ghi chú |
| -------------- | ---------------- | ---------------------------------------------------------- | -------------
| **box_id**       | **str**        | ID của hộp | 
| **recipient**   | **str**        | Tài khoản nhận | 
| **metadata**    | **dict**           | Metadata của NFT | 
| **callback**    | **str**        | Địa chỉ URI của callback | 

### Kiểu kết quả trả về

**str**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **mints**
> list[object] mints(boxs)

Đúc hàng loạt NFT Box.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
BOXS = "<boxs>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.MysteryboxApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.mints(BOXS)
    print(api_response)
except Exception as e:
    print("Exception when calling MysteryboxApi->mints: %s\n" % e)
```

### Tham số

Tên | Kiểu dữ liệu | Mô tả  | Ghi chú
------------- | ------------- | ------------- | -------------
 **boxes** | **list[dict]**| Danh sách các tham số của mint | 

### Kiểu kết quả trả về

**list[object]**

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)