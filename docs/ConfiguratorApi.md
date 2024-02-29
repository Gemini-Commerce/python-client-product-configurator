# product-configurator.ConfiguratorApi

All URIs are relative to *https://product-configurator.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_configurator_copy_configurator**](ConfiguratorApi.md#product_configurator_copy_configurator) | **POST** /v1/{tenantId}/product/{sourceConfiguratorId}/copy | Copy Configurator
[**product_configurator_create_configurator**](ConfiguratorApi.md#product_configurator_create_configurator) | **POST** /v1/{tenantId}/product/{productId}/create | Create Configurator
[**product_configurator_delete_configurator**](ConfiguratorApi.md#product_configurator_delete_configurator) | **DELETE** /v1/{tenantId}/configurator/{configuratorId} | Delete Configurator
[**product_configurator_get_configurator_by_product_id**](ConfiguratorApi.md#product_configurator_get_configurator_by_product_id) | **GET** /v1/{tenantId}/product/{productId} | Get Configurator by Product ID
[**product_configurator_get_configurator_by_product_id2**](ConfiguratorApi.md#product_configurator_get_configurator_by_product_id2) | **GET** /v1/{tenantId}/product/{productId}/status/{status} | Get Configurator by Product ID
[**product_configurator_list_configurators**](ConfiguratorApi.md#product_configurator_list_configurators) | **POST** /v1/{tenantId}/product/{productId}/page-size/{pageSize}/configurators | List Product Configurators
[**product_configurator_update_configurator**](ConfiguratorApi.md#product_configurator_update_configurator) | **PUT** /v1/{tenantId}/configurator/{configuratorId} | Update Configurator


# **product_configurator_copy_configurator**
> ProductconfiguratorconfiguratorEntity product_configurator_copy_configurator(tenant_id, source_configurator_id, body)

Copy Configurator

Duplicate an existing product configurator from the source to the specified tenant and product. Submit an empty body to initiate the copy process, creating a new configuration based on the source.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_copy_configurator_request import ProductConfiguratorCopyConfiguratorRequest
from product-configurator.models.productconfiguratorconfigurator_entity import ProductconfiguratorconfiguratorEntity
from product-configurator.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product-configurator.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product-configurator.Configuration(
    host = "https://product-configurator.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIAuthorization
configuration.api_key['APIAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
with product-configurator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product-configurator.ConfiguratorApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    source_configurator_id = 'source_configurator_id_example' # str | 
    body = product-configurator.ProductConfiguratorCopyConfiguratorRequest() # ProductConfiguratorCopyConfiguratorRequest | 

    try:
        # Copy Configurator
        api_response = api_instance.product_configurator_copy_configurator(tenant_id, source_configurator_id, body)
        print("The response of ConfiguratorApi->product_configurator_copy_configurator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfiguratorApi->product_configurator_copy_configurator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **source_configurator_id** | **str**|  | 
 **body** | [**ProductConfiguratorCopyConfiguratorRequest**](ProductConfiguratorCopyConfiguratorRequest.md)|  | 

### Return type

[**ProductconfiguratorconfiguratorEntity**](ProductconfiguratorconfiguratorEntity.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [APIAuthorization](../README.md#APIAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request or Limit Exceeded |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_configurator_create_configurator**
> ProductconfiguratorconfiguratorEntity product_configurator_create_configurator(tenant_id, product_id, body)

Create Configurator

Create a new product configurator for a specified tenant and product. Submit the desired configuration details in the request body to initiate the creation process.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_create_configurator_request import ProductConfiguratorCreateConfiguratorRequest
from product-configurator.models.productconfiguratorconfigurator_entity import ProductconfiguratorconfiguratorEntity
from product-configurator.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product-configurator.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product-configurator.Configuration(
    host = "https://product-configurator.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIAuthorization
configuration.api_key['APIAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
with product-configurator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product-configurator.ConfiguratorApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    product_id = 'product_id_example' # str | 
    body = product-configurator.ProductConfiguratorCreateConfiguratorRequest() # ProductConfiguratorCreateConfiguratorRequest | 

    try:
        # Create Configurator
        api_response = api_instance.product_configurator_create_configurator(tenant_id, product_id, body)
        print("The response of ConfiguratorApi->product_configurator_create_configurator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfiguratorApi->product_configurator_create_configurator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **product_id** | **str**|  | 
 **body** | [**ProductConfiguratorCreateConfiguratorRequest**](ProductConfiguratorCreateConfiguratorRequest.md)|  | 

### Return type

[**ProductconfiguratorconfiguratorEntity**](ProductconfiguratorconfiguratorEntity.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [APIAuthorization](../README.md#APIAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_configurator_delete_configurator**
> object product_configurator_delete_configurator(tenant_id, configurator_id)

Delete Configurator

Delete a product configurator by specifying the tenant and configurator IDs. Ensure precise removal of unwanted configurations with a straightforward DELETE request.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product-configurator.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product-configurator.Configuration(
    host = "https://product-configurator.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIAuthorization
configuration.api_key['APIAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
with product-configurator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product-configurator.ConfiguratorApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    configurator_id = 'configurator_id_example' # str | 

    try:
        # Delete Configurator
        api_response = api_instance.product_configurator_delete_configurator(tenant_id, configurator_id)
        print("The response of ConfiguratorApi->product_configurator_delete_configurator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfiguratorApi->product_configurator_delete_configurator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **configurator_id** | **str**|  | 

### Return type

**object**

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [APIAuthorization](../README.md#APIAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_configurator_get_configurator_by_product_id**
> ProductconfiguratorconfiguratorEntity product_configurator_get_configurator_by_product_id(tenant_id, product_id, status=status)

Get Configurator by Product ID

Retrieve product configurations with status details, filtered by product and tenant IDs. Flexible options for specifying additional status parameters.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.productconfiguratorconfigurator_entity import ProductconfiguratorconfiguratorEntity
from product-configurator.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product-configurator.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product-configurator.Configuration(
    host = "https://product-configurator.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIAuthorization
configuration.api_key['APIAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
with product-configurator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product-configurator.ConfiguratorApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    product_id = 'product_id_example' # str | 
    status = 'UNKNOWN' # str |  (optional) (default to 'UNKNOWN')

    try:
        # Get Configurator by Product ID
        api_response = api_instance.product_configurator_get_configurator_by_product_id(tenant_id, product_id, status=status)
        print("The response of ConfiguratorApi->product_configurator_get_configurator_by_product_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfiguratorApi->product_configurator_get_configurator_by_product_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **product_id** | **str**|  | 
 **status** | **str**|  | [optional] [default to &#39;UNKNOWN&#39;]

### Return type

[**ProductconfiguratorconfiguratorEntity**](ProductconfiguratorconfiguratorEntity.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [APIAuthorization](../README.md#APIAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_configurator_get_configurator_by_product_id2**
> ProductconfiguratorconfiguratorEntity product_configurator_get_configurator_by_product_id2(tenant_id, product_id, status)

Get Configurator by Product ID

Retrieve product configurations with status details, filtered by product and tenant IDs. Flexible options for specifying additional status parameters.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.productconfiguratorconfigurator_entity import ProductconfiguratorconfiguratorEntity
from product-configurator.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product-configurator.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product-configurator.Configuration(
    host = "https://product-configurator.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIAuthorization
configuration.api_key['APIAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
with product-configurator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product-configurator.ConfiguratorApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    product_id = 'product_id_example' # str | 
    status = 'status_example' # str | 

    try:
        # Get Configurator by Product ID
        api_response = api_instance.product_configurator_get_configurator_by_product_id2(tenant_id, product_id, status)
        print("The response of ConfiguratorApi->product_configurator_get_configurator_by_product_id2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfiguratorApi->product_configurator_get_configurator_by_product_id2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **product_id** | **str**|  | 
 **status** | **str**|  | 

### Return type

[**ProductconfiguratorconfiguratorEntity**](ProductconfiguratorconfiguratorEntity.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [APIAuthorization](../README.md#APIAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_configurator_list_configurators**
> ConfiguratorListResponse product_configurator_list_configurators(tenant_id, product_id, page_size, body)

List Product Configurators

List all product configurators.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.configurator_list_response import ConfiguratorListResponse
from product-configurator.models.product_configurator_list_properties_request import ProductConfiguratorListPropertiesRequest
from product-configurator.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product-configurator.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product-configurator.Configuration(
    host = "https://product-configurator.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIAuthorization
configuration.api_key['APIAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
with product-configurator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product-configurator.ConfiguratorApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    product_id = 'product_id_example' # str | 
    page_size = 56 # int | 
    body = product-configurator.ProductConfiguratorListPropertiesRequest() # ProductConfiguratorListPropertiesRequest | 

    try:
        # List Product Configurators
        api_response = api_instance.product_configurator_list_configurators(tenant_id, product_id, page_size, body)
        print("The response of ConfiguratorApi->product_configurator_list_configurators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfiguratorApi->product_configurator_list_configurators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **product_id** | **str**|  | 
 **page_size** | **int**|  | 
 **body** | [**ProductConfiguratorListPropertiesRequest**](ProductConfiguratorListPropertiesRequest.md)|  | 

### Return type

[**ConfiguratorListResponse**](ConfiguratorListResponse.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [APIAuthorization](../README.md#APIAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request or Limit Exceeded |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_configurator_update_configurator**
> ProductconfiguratorconfiguratorEntity product_configurator_update_configurator(tenant_id, configurator_id, body)

Update Configurator

Modify an existing product configurator by specifying the tenant and configurator IDs. Use a PUT request with the updated configuration details in the body to seamlessly update and manage product configurations

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_update_configurator_request import ProductConfiguratorUpdateConfiguratorRequest
from product-configurator.models.productconfiguratorconfigurator_entity import ProductconfiguratorconfiguratorEntity
from product-configurator.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product-configurator.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product-configurator.Configuration(
    host = "https://product-configurator.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIAuthorization
configuration.api_key['APIAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
with product-configurator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product-configurator.ConfiguratorApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    configurator_id = 'configurator_id_example' # str | 
    body = product-configurator.ProductConfiguratorUpdateConfiguratorRequest() # ProductConfiguratorUpdateConfiguratorRequest | 

    try:
        # Update Configurator
        api_response = api_instance.product_configurator_update_configurator(tenant_id, configurator_id, body)
        print("The response of ConfiguratorApi->product_configurator_update_configurator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfiguratorApi->product_configurator_update_configurator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **configurator_id** | **str**|  | 
 **body** | [**ProductConfiguratorUpdateConfiguratorRequest**](ProductConfiguratorUpdateConfiguratorRequest.md)|  | 

### Return type

[**ProductconfiguratorconfiguratorEntity**](ProductconfiguratorconfiguratorEntity.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [APIAuthorization](../README.md#APIAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request or Limit Exceeded |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

