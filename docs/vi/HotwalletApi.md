# nemo_api.HotwalletApi

Phương thức | Yêu cầu HTTP | Mô tả
------------- | ------------- | -------------
[**balance**](HotwalletApi.md#balance) | **POST** /hotwallet/balance | Thông tin ví nóng của tài khoản
[**charge**](HotwalletApi.md#charge) | **POST** /hotwallet/charge | Trừ tiền từ tài khoản người dùng
[**award**](HotwalletApi.md#award) | **POST** /hotwallet/award | Trao token cho người dùng
[**get_allowance**](HotwalletApi.md#get_allowance) | **POST** /hotwallet/get_allowance | Lấy thông tin lượng token của người dùng đã cấp phép cho dịch vụ

# **balance**
> AccountBalance balance(account)

Thông tin ví nóng của tài khoản.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
ACCOUNT = "<account>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.HotwalletApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.balance(ACCOUNT)
    print(api_response)
except Exception as e:
    print("Exception when calling HotwalletApi->balance: %s\n" % e)
```

### Tham số

Tên | Kiểu dữ liệu | Mô tả  | Ghi chú
------------- | ------------- | ------------- | -------------
 **account** | **Union[str, AccountBalance]**| Tài khoản | 


### Kiểu kết quả trả về

[**AccountBalance**](AccountBalance.md)

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **charge**
> tuple(InternalTransaction, AccountBalance) charge(account, amount)

Trừ tiền từ tài khoản của người dùng.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
ACCOUNT = "<account>"
AMOUNT = "<amount>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.HotwalletApi(api_client)

try:
    # Get currency detail for lending
    api_response = api_instance.charge(ACCOUNT, AMOUNT)
    print(api_response)
except Exception as e:
    print("Exception when calling HotwalletApi->get_uni_currency: %s\n" % e)
```

### Tham số

Tên | Kiểu dữ liệu | Mô tả  | Ghi chú
------------- | ------------- | ------------- | -------------
 **account** | **Union[str, AccountBalance]**| Tài khoản | 
 **amount** | **str**| Số tiền | 

### Kiểu kết quả trả về

tuple([**InternalTransaction**](InternalTransaction.md), [**AccountBalance**](AccountBalance.md))

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **award**

> tuple(InternalTransaction, AccountBalance) award(account, amount)

Trao token cho người dùng.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
ACCOUNT = "<account>"
AMOUNT = "<amount>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.HotwalletApi(api_client)

try:
    # Get currency detail for lending
    api_response = api_instance.award(ACCOUNT, AMOUNT)
    print(api_response)
except Exception as e:
    print("Exception when calling HotwalletApi->get_uni_currency: %s\n" % e)
```

### Tham số

Tên | Kiểu dữ liệu | Mô tả  | Ghi chú
------------- | ------------- | ------------- | -------------
 **account** | **Union[str, AccountBalance]**| Tài khoản | 
 **amount** | **str**| Số tiền | 

### Kiểu kết quả trả về

tuple([**InternalTransaction**](InternalTransaction.md), [**AccountBalance**](AccountBalance.md))

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)

# **get_allowance**
> HotwalletAllowance get_allowance(account)

Lấy thông tin lượng token của người dùng đã cấp phép cho dịch vụ.

### Ví dụ

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
ACCOUNT = "<account>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.HotwalletApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.get_allowance(ACCOUNT)
    print(api_response)
except Exception as e:
    print("Exception when calling HotwalletApi->balance: %s\n" % e)
```

### Tham số

Tên | Kiểu dữ liệu | Mô tả  | Ghi chú
------------- | ------------- | ------------- | -------------
 **account** | **Union[str, AccountBalance]**| Tài khoản | 

### Kiểu kết quả trả về

[**HotwalletAllowance**](HotwalletAllowance.md)

### Xác thực

[apiv2](./README.md#apiv2)

### HTTP request headers

### Chi tiết phản hồi của yêu cầu HTTP

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)