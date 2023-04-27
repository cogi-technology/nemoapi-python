# nemo_api.SubgraphApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**call**](SubgraphApi.md#call) | **POST** /subgraph/call | Execute a GraphQL query on subgraph
[**getTotalVolume**](SubgraphApi.md#getTotalVolume) | **POST** /subgraph/getTotalVolume | Calculate the total volume of the marketplace on the subgraph

# **call**
> object call(params)

Execute a GraphQL query.

### Example

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
VARIABLES = "<variables>"
QUERY = "<query>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.SubgraphApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.call({
        "variables": VARIABLES,
        "query": QUERY
    })
    print(api_response)
except Exception as e:
    print("Exception when calling SubgraphApi->call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | **dict**| The body parameters to make a POST request to GraphQL | 

### Return type

**object**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getTotalVolume**
> object getTotalVolume(params)

Get the total volume of the marketplace on the subgraph.

### Example

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
VARIABLES = "<variables>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.SubgraphApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.getTotalVolume(VARIABLES)
    print(api_response)
except Exception as e:
    print("Exception when calling SubgraphApi->getTotalVolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | **dict**| Variables allow you to parameterize your queries and mutations | 

### Return type

**object**

### Authorization

[apiv2](../README.md#apiv2)

### HTTP request headers

### HTTP response details

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)