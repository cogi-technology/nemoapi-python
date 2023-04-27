# nemo_api.NemoAccountApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_link**](NemoAccountApi.md#get_link) | **POST** /account/get_link | Get a list of Metamask addresses linked to Nemo Wallet
[**get_nemo_wallet**](NemoAccountApi.md#get_nemo_wallet) | **POST** /account/get_nemo_wallet | Get the Nemo Wallet address that is linked from the Metamask address

# **get_link**
> list[str] get_link(main_account)

Get a list of Metamask addresses linked to Nemo Wallet.

### Example

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

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main_account** | **str**| NEMO Wallet address | 

### Return type

**list[str]**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nemo_wallet**
> object get_nemo_wallet(sub_account)

Get the Nemo Wallet address that is linked from the Metamask address.

### Example

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

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account** | **str**| Metamask Wallet address | 

### Return type

**object**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)