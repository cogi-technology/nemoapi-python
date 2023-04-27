# nemo_api.NemoIdApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](NemoIdApi.md#login) | **POST** /nemoid/login | Login and get NemoIdAccount's information
[**user_info**](NemoIdApi.md#user_info) | **POST** /nemoid/user_info | Get NemoIdAccount's information
[**relogin**](NemoIdApi.md#relogin) | **POST** /nemoid/relogin | Relogin and get NemoIdAccount's information

# **login**
> NemoIdAccount login(code, code_verifier, redirect_uri)

Login.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Authorization code | 
 **code_verifier** | **str**| Code verifier | 
 **redirect_uri** | **str**| Redirect URI | 

### Return type

[**NemoIdAccount**](NemoIdAccount.md)

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_info**
> NemoIdAccount user_info(access_token)

Get NemoIdAccount's information by access_token.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access token | 

### Return type

[**NemoIdAccount**](NemoIdAccount.md)

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relogin**
> NemoIdAccount relogin(refresh_token, code_verifier)

Relogin.

### Example

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**| Refresh token | 
 **code_verifier** | **str**| Code verifier | 

### Return type

[**NemoIdAccount**](NemoIdAccount.md)

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

