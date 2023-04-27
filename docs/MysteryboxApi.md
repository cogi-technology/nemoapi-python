# nemo_api.MysteryboxApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**mint**](MysteryboxApi.md#mint) | **POST** /mysterybox/mint | Send a transaction to mint an NFT BOX and transfer it to an account, executed by the minter. Get UUID of NFT if successful
[**mints**](MysteryboxApi.md#mints) | **POST** /mysterybox/mints | Send batch transaction to mint multiple NFT BOX, executed by the minter

# **mint**
> str mint(box_id, recipient, metadata, callback)

Mint an NFT BOX.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **str**| Box ID | 
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

# **mints**
> list[object] mints(boxs)

Mint batch NFT Box.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boxs** | **list[dict]**| List of mint parameters | 

### Return type

**list[object]**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)