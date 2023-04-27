# nemo_api.NftApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**mint**](NftApi.md#mint) | **POST** /nft/mint | Send a transaction to mint an NFT and transfer it to an account, executed by the minter. Get UUID of NFT if successful
[**request_mint**](NftApi.md#request_mint) | **POST** /nft/request_mint | Send a transaction to mint an NFT and transfer it to an account, executed by the user. Get UUID of NFT if successful

# **mint**
> str mint(recipient, metadata, callback)

Mint an NFT.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient** | **str**| Account | 
 **metadata** | **dict**| Metadata object | 
 **callback** | **str**| Callback uri | 

### Return type

**str**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_mint**
> str request_mint(recipient, metadata, callback)

Request mint an NFT.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient** | **str**| Account | 
 **metadata** | **dict**| Metadata object | 
 **callback** | **str**| Callback uri | 

### Return type

**str**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)