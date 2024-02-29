# product-configurator.ConfigurationApi

All URIs are relative to *https://product-configurator.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_configurator_get_available_configuration**](ConfigurationApi.md#product_configurator_get_available_configuration) | **GET** /v1/{tenantId}/product/{productId}/configuration | Get Available Configuration
[**product_configurator_get_available_configuration2**](ConfigurationApi.md#product_configurator_get_available_configuration2) | **POST** /v1/{tenantId}/product/{productId}/configuration | Get Available Configuration
[**product_configurator_get_configuration_from_selections**](ConfigurationApi.md#product_configurator_get_configuration_from_selections) | **POST** /v1/{tenantId}/product/{productId}/configuration-from-selections | Get Configuration from Selections


# **product_configurator_get_available_configuration**
> ConfigurationGetAvailableConfigurationResponse product_configurator_get_available_configuration(tenant_id, product_id, configurator_id=configurator_id)

Get Available Configuration

Retrieve available configurations for a specific product and tenant. Use a GET request for read-only access or submit additional criteria in the body of a POST request for tailored configuration results. Streamline the retrieval of configurations effortlessly.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.configuration_get_available_configuration_response import ConfigurationGetAvailableConfigurationResponse
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
    api_instance = product-configurator.ConfigurationApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    product_id = 'product_id_example' # str | 
    configurator_id = 'configurator_id_example' # str | If not set, the service returns the active configurator (optional)

    try:
        # Get Available Configuration
        api_response = api_instance.product_configurator_get_available_configuration(tenant_id, product_id, configurator_id=configurator_id)
        print("The response of ConfigurationApi->product_configurator_get_available_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->product_configurator_get_available_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **product_id** | **str**|  | 
 **configurator_id** | **str**| If not set, the service returns the active configurator | [optional] 

### Return type

[**ConfigurationGetAvailableConfigurationResponse**](ConfigurationGetAvailableConfigurationResponse.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [APIAuthorization](../README.md#APIAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **product_configurator_get_available_configuration2**
> ConfigurationGetAvailableConfigurationResponse product_configurator_get_available_configuration2(tenant_id, product_id, body)

Get Available Configuration

Retrieve available configurations for a specific product and tenant. Use a GET request for read-only access or submit additional criteria in the body of a POST request for tailored configuration results. Streamline the retrieval of configurations effortlessly.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.configuration_get_available_configuration_response import ConfigurationGetAvailableConfigurationResponse
from product-configurator.models.product_configurator_get_available_configuration2_request import ProductConfiguratorGetAvailableConfiguration2Request
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
    api_instance = product-configurator.ConfigurationApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    product_id = 'product_id_example' # str | 
    body = product-configurator.ProductConfiguratorGetAvailableConfiguration2Request() # ProductConfiguratorGetAvailableConfiguration2Request | 

    try:
        # Get Available Configuration
        api_response = api_instance.product_configurator_get_available_configuration2(tenant_id, product_id, body)
        print("The response of ConfigurationApi->product_configurator_get_available_configuration2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->product_configurator_get_available_configuration2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **product_id** | **str**|  | 
 **body** | [**ProductConfiguratorGetAvailableConfiguration2Request**](ProductConfiguratorGetAvailableConfiguration2Request.md)|  | 

### Return type

[**ConfigurationGetAvailableConfigurationResponse**](ConfigurationGetAvailableConfigurationResponse.md)

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

# **product_configurator_get_configuration_from_selections**
> ConfigurationGetConfigurationFromSelectionsResponse product_configurator_get_configuration_from_selections(tenant_id, product_id, body)

Get Configuration from Selections

Retrieve a configuration based on user selections for a specific product and tenant. Submit a POST request with user selections in the body to receive a tailored configuration. Enhance the user experience by dynamically generating configurations based on user input.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.configuration_get_configuration_from_selections_response import ConfigurationGetConfigurationFromSelectionsResponse
from product-configurator.models.product_configurator_get_configuration_from_selections_request import ProductConfiguratorGetConfigurationFromSelectionsRequest
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
    api_instance = product-configurator.ConfigurationApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    product_id = 'product_id_example' # str | 
    body = product-configurator.ProductConfiguratorGetConfigurationFromSelectionsRequest() # ProductConfiguratorGetConfigurationFromSelectionsRequest | 

    try:
        # Get Configuration from Selections
        api_response = api_instance.product_configurator_get_configuration_from_selections(tenant_id, product_id, body)
        print("The response of ConfigurationApi->product_configurator_get_configuration_from_selections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->product_configurator_get_configuration_from_selections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **product_id** | **str**|  | 
 **body** | [**ProductConfiguratorGetConfigurationFromSelectionsRequest**](ProductConfiguratorGetConfigurationFromSelectionsRequest.md)|  | 

### Return type

[**ConfigurationGetConfigurationFromSelectionsResponse**](ConfigurationGetConfigurationFromSelectionsResponse.md)

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

