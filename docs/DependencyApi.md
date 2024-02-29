# product-configurator.DependencyApi

All URIs are relative to *https://product-configurator.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_configurator_create_dependency**](DependencyApi.md#product_configurator_create_dependency) | **POST** /v1/{tenantId}/step/{stepId}/dependency/create | Create Dependency
[**product_configurator_delete_dependency**](DependencyApi.md#product_configurator_delete_dependency) | **DELETE** /v1/{tenantId}/dependency/{dependencyId} | Delete Dependency
[**product_configurator_list_dependencies**](DependencyApi.md#product_configurator_list_dependencies) | **POST** /v1/{tenantId}/page-size/{pageSize}/dependencies | List Dependencies
[**product_configurator_update_dependency**](DependencyApi.md#product_configurator_update_dependency) | **PUT** /v1/{tenantId}/dependency/{dependencyId} | Update Dependency


# **product_configurator_create_dependency**
> ProductconfiguratordependencyEntity product_configurator_create_dependency(tenant_id, step_id, body)

Create Dependency

Establish a new dependency for an existing step by specifying the tenant and step IDs. Utilize a POST request with the required dependency details in the body to seamlessly enhance the configuration logic of your product.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_create_dependency_request import ProductConfiguratorCreateDependencyRequest
from product-configurator.models.productconfiguratordependency_entity import ProductconfiguratordependencyEntity
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
    api_instance = product-configurator.DependencyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    step_id = 'step_id_example' # str | 
    body = product-configurator.ProductConfiguratorCreateDependencyRequest() # ProductConfiguratorCreateDependencyRequest | 

    try:
        # Create Dependency
        api_response = api_instance.product_configurator_create_dependency(tenant_id, step_id, body)
        print("The response of DependencyApi->product_configurator_create_dependency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependencyApi->product_configurator_create_dependency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **step_id** | **str**|  | 
 **body** | [**ProductConfiguratorCreateDependencyRequest**](ProductConfiguratorCreateDependencyRequest.md)|  | 

### Return type

[**ProductconfiguratordependencyEntity**](ProductconfiguratordependencyEntity.md)

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

# **product_configurator_delete_dependency**
> object product_configurator_delete_dependency(tenant_id, dependency_id)

Delete Dependency

Remove a specific dependency by specifying the tenant and dependency IDs. Ensure precision in dependency management with a straightforward DELETE request, simplifying the elimination of unwanted configuration logic.

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
    api_instance = product-configurator.DependencyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    dependency_id = 'dependency_id_example' # str | 

    try:
        # Delete Dependency
        api_response = api_instance.product_configurator_delete_dependency(tenant_id, dependency_id)
        print("The response of DependencyApi->product_configurator_delete_dependency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependencyApi->product_configurator_delete_dependency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **dependency_id** | **str**|  | 

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
**400** | Bad Request or Limit Exceeded |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_configurator_list_dependencies**
> DependencyListDependenciesResponse product_configurator_list_dependencies(tenant_id, page_size, body)

List Dependencies

Retrieve a list of dependencies based on the specified tenant ID. Customize results by specifying page size for efficient pagination. Submit an empty body to get all dependencies associated with the configurations.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.dependency_list_dependencies_response import DependencyListDependenciesResponse
from product-configurator.models.product_configurator_list_dependencies_request import ProductConfiguratorListDependenciesRequest
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
    api_instance = product-configurator.DependencyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    page_size = 56 # int | 
    body = product-configurator.ProductConfiguratorListDependenciesRequest() # ProductConfiguratorListDependenciesRequest | 

    try:
        # List Dependencies
        api_response = api_instance.product_configurator_list_dependencies(tenant_id, page_size, body)
        print("The response of DependencyApi->product_configurator_list_dependencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependencyApi->product_configurator_list_dependencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **page_size** | **int**|  | 
 **body** | [**ProductConfiguratorListDependenciesRequest**](ProductConfiguratorListDependenciesRequest.md)|  | 

### Return type

[**DependencyListDependenciesResponse**](DependencyListDependenciesResponse.md)

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

# **product_configurator_update_dependency**
> ProductconfiguratordependencyEntity product_configurator_update_dependency(tenant_id, dependency_id, body)

Update Dependency

Modify an existing dependency by specifying the tenant and dependency IDs. Utilize a PUT request with updated dependency details in the body for seamless customization and fine-tuning of your product configurations.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_update_dependency_request import ProductConfiguratorUpdateDependencyRequest
from product-configurator.models.productconfiguratordependency_entity import ProductconfiguratordependencyEntity
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
    api_instance = product-configurator.DependencyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    dependency_id = 'dependency_id_example' # str | 
    body = product-configurator.ProductConfiguratorUpdateDependencyRequest() # ProductConfiguratorUpdateDependencyRequest | 

    try:
        # Update Dependency
        api_response = api_instance.product_configurator_update_dependency(tenant_id, dependency_id, body)
        print("The response of DependencyApi->product_configurator_update_dependency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependencyApi->product_configurator_update_dependency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **dependency_id** | **str**|  | 
 **body** | [**ProductConfiguratorUpdateDependencyRequest**](ProductConfiguratorUpdateDependencyRequest.md)|  | 

### Return type

[**ProductconfiguratordependencyEntity**](ProductconfiguratordependencyEntity.md)

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

