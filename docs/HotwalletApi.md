# nemo_api.HotwalletApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance**](HotwalletApi.md#balance) | **POST** /hotwallet/balance | Account's hotwallet information
[**charge**](HotwalletApi.md#charge) | **POST** /hotwallet/charge | Deduct balance from the user's account
[**award**](HotwalletApi.md#award) | **POST** /hotwallet/award | Award token to user
[**get_allowance**](HotwalletApi.md#get_allowance) | **POST** /hotwallet/get_allowance | Get user's approval for the service

# **balance**
> AccountBalance balance(account)

Account's hotwallet information.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **Union[str, AccountBalance]**| Account | 

### Return type

[**AccountBalance**](AccountBalance.md)

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge**
> tuple(InternalTransaction, AccountBalance) charge(account, amount)

Deduct balance from the user's account

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **Union[str, AccountBalance]**| Currency | 
 **amount** | **str**| Amount | 

### Return type

tuple([**InternalTransaction**](InternalTransaction.md), [**AccountBalance**](AccountBalance.md))

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **award**
> tuple(InternalTransaction, AccountBalance) award(account, amount)

Award token to user

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **Union[str, AccountBalance]**| Currency | 
 **amount** | **str**| Amount | 

### Return type

tuple([**InternalTransaction**](InternalTransaction.md), [**AccountBalance**](AccountBalance.md))

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allowance**
> HotwalletAllowance get_allowance(account)

Get user's approval for the service.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **Union[str, AccountBalance]**| Account | 

### Return type

[**HotwalletAllowance**](HotwalletAllowance.md)

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)