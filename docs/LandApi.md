# nemo_api.LandApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**mint**](LandApi.md#mint) | **POST** /land/mint | Send a transaction to mint an NFT Land and transfer it to an account, executed by the minter. Get UUID of NFT Land if successful
[**request_mint**](LandApi.md#request_mint) | **POST** /land/request_mint | Send a transaction to mint an NFT Land and transfer it to an account, executed by the user. Get UUID of NFT Land if successful
[**mints**](LandApi.md#mints) | **POST** /land/mints | Send batch transaction to mint multiple NFT Land, executed by the minter
[**request_mints**](LandApi.md#request_mints) | **POST** /land/request_mints | Send batch transaction to mint multiple NFT Land, executed by the user
[**request_cancelbuys**](LandApi.md#request_cancelbuys) | **POST** /land/request_cancelbuys | Send batch request cancel buy

# **mint**
> str mint(recipient, land_id, level, land_x, land_y, metadata, callback)

Mint an NFT.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient** | **str**| Account | 
 **land_id** | **str**| Land id | 
 **level** | **str**| Land level | 
 **land_x** | **str**| Position X | 
 **land_y** | **str**| Position Y | 
 **metadata** | **dict**| Land Metadata | 
 **callback** | **str**| Callback uri | 

### Return type

**str**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_mint**
> str request_mint(recipient, land_id, level, land_x, land_y, metadata, callback)

Request mint an NFT.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient** | **str**| Account | 
 **land_id** | **str**| Land id | 
 **level** | **str**| Land level | 
 **land_x** | **str**| Position X | 
 **land_y** | **str**| Position Y | 
 **metadata** | **dict**| Land Metadata | 
 **callback** | **str**| Callback uri | 

### Return type

**str**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mints**
> list[object] mints(lands)

Mint batch NFT.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lands** | **list[dict]**| List of mint parameters | 

### Return type

**list[object]**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_mints**
> list[object] request_mints(lands)

Mint batch NFT.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lands** | **list[dict]**| List of mint parameters | 

### Return type

**list[object]**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_cancelbuys**
> list[object] request_cancelbuys(lands)

Request batch cancel buy.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lands** | **list[dict]**| The list of objects includes attributes for both account and cid | 

### Return type

**list[object]**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)