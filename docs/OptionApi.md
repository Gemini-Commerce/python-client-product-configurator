# product-configurator.OptionApi

All URIs are relative to *https://product-configurator.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_configurator_bulk_create_options**](OptionApi.md#product_configurator_bulk_create_options) | **POST** /v1/{tenantId}/step/{stepId}/option/create/bulk | Bulk Create Options
[**product_configurator_bulk_delete_options**](OptionApi.md#product_configurator_bulk_delete_options) | **POST** /v1/{tenantId}/option/delete/bulk | Bulk Delete Options
[**product_configurator_bulk_update_options**](OptionApi.md#product_configurator_bulk_update_options) | **PUT** /v1/{tenantId}/option/bulk | Bulk Update Options
[**product_configurator_copy_option**](OptionApi.md#product_configurator_copy_option) | **POST** /v1/{tenantId}/option/{sourceOptionId}/copy | Copy Option
[**product_configurator_create_option**](OptionApi.md#product_configurator_create_option) | **POST** /v1/{tenantId}/step/{stepId}/option/create | Create Option
[**product_configurator_delete_option**](OptionApi.md#product_configurator_delete_option) | **DELETE** /v1/{tenantId}/option/{optionId} | Delete Option
[**product_configurator_list_options**](OptionApi.md#product_configurator_list_options) | **POST** /v1/{tenantId}/step/{stepId}/page-size/{pageSize}/options | List Options
[**product_configurator_update_option**](OptionApi.md#product_configurator_update_option) | **PUT** /v1/{tenantId}/option/{optionId} | Update Option


# **product_configurator_bulk_create_options**
> ProductconfiguratoroptionBulkCreateResponse product_configurator_bulk_create_options(tenant_id, step_id, body)

Bulk Create Options

Add multiple options to an existing step simultaneously. Submit a POST request with the necessary option details in the body to efficiently expand the configuration possibilities in bulk. Streamline large-scale option management effortlessly.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_bulk_create_options_request import ProductConfiguratorBulkCreateOptionsRequest
from product-configurator.models.productconfiguratoroption_bulk_create_response import ProductconfiguratoroptionBulkCreateResponse
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
    api_instance = product-configurator.OptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    step_id = 'step_id_example' # str | 
    body = product-configurator.ProductConfiguratorBulkCreateOptionsRequest() # ProductConfiguratorBulkCreateOptionsRequest | 

    try:
        # Bulk Create Options
        api_response = api_instance.product_configurator_bulk_create_options(tenant_id, step_id, body)
        print("The response of OptionApi->product_configurator_bulk_create_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionApi->product_configurator_bulk_create_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **step_id** | **str**|  | 
 **body** | [**ProductConfiguratorBulkCreateOptionsRequest**](ProductConfiguratorBulkCreateOptionsRequest.md)|  | 

### Return type

[**ProductconfiguratoroptionBulkCreateResponse**](ProductconfiguratoroptionBulkCreateResponse.md)

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

# **product_configurator_bulk_delete_options**
> object product_configurator_bulk_delete_options(tenant_id, body)

Bulk Delete Options

Efficiently remove multiple options from configurations using a bulk delete operation. Specify the tenant ID and submit a POST request with the list of option IDs in the body for streamlined option management.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_bulk_delete_options_request import ProductConfiguratorBulkDeleteOptionsRequest
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
    api_instance = product-configurator.OptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = product-configurator.ProductConfiguratorBulkDeleteOptionsRequest() # ProductConfiguratorBulkDeleteOptionsRequest | 

    try:
        # Bulk Delete Options
        api_response = api_instance.product_configurator_bulk_delete_options(tenant_id, body)
        print("The response of OptionApi->product_configurator_bulk_delete_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionApi->product_configurator_bulk_delete_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**ProductConfiguratorBulkDeleteOptionsRequest**](ProductConfiguratorBulkDeleteOptionsRequest.md)|  | 

### Return type

**object**

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

# **product_configurator_bulk_update_options**
> ProductconfiguratoroptionBulkUpdateResponse product_configurator_bulk_update_options(tenant_id, body)

Bulk Update Options

Effortlessly update multiple options. Specify the tenant ID and submit a PUT request with the updated option details in the body. Streamline the customization of a multitude of options in one go.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_bulk_update_options_request import ProductConfiguratorBulkUpdateOptionsRequest
from product-configurator.models.productconfiguratoroption_bulk_update_response import ProductconfiguratoroptionBulkUpdateResponse
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
    api_instance = product-configurator.OptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = product-configurator.ProductConfiguratorBulkUpdateOptionsRequest() # ProductConfiguratorBulkUpdateOptionsRequest | 

    try:
        # Bulk Update Options
        api_response = api_instance.product_configurator_bulk_update_options(tenant_id, body)
        print("The response of OptionApi->product_configurator_bulk_update_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionApi->product_configurator_bulk_update_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**ProductConfiguratorBulkUpdateOptionsRequest**](ProductConfiguratorBulkUpdateOptionsRequest.md)|  | 

### Return type

[**ProductconfiguratoroptionBulkUpdateResponse**](ProductconfiguratoroptionBulkUpdateResponse.md)

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

# **product_configurator_copy_option**
> ProductconfiguratoroptionEntity product_configurator_copy_option(tenant_id, source_option_id, body)

Copy Option

Duplicate an existing option from the source to a specified tenant. Utilize a POST request with an empty body to initiate the copy process, creating a new option based on the source configuration. Streamline option replication effortlessly.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_copy_option_request import ProductConfiguratorCopyOptionRequest
from product-configurator.models.productconfiguratoroption_entity import ProductconfiguratoroptionEntity
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
    api_instance = product-configurator.OptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    source_option_id = 'source_option_id_example' # str | 
    body = product-configurator.ProductConfiguratorCopyOptionRequest() # ProductConfiguratorCopyOptionRequest | 

    try:
        # Copy Option
        api_response = api_instance.product_configurator_copy_option(tenant_id, source_option_id, body)
        print("The response of OptionApi->product_configurator_copy_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionApi->product_configurator_copy_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **source_option_id** | **str**|  | 
 **body** | [**ProductConfiguratorCopyOptionRequest**](ProductConfiguratorCopyOptionRequest.md)|  | 

### Return type

[**ProductconfiguratoroptionEntity**](ProductconfiguratoroptionEntity.md)

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

# **product_configurator_create_option**
> ProductconfiguratoroptionEntity product_configurator_create_option(tenant_id, step_id, body)

Create Option

Integrate a new option into an existing step by specifying the tenant and step IDs. Use a POST request with the required option details in the body for seamless customization and expansion of product configurations.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_create_option_request import ProductConfiguratorCreateOptionRequest
from product-configurator.models.productconfiguratoroption_entity import ProductconfiguratoroptionEntity
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
    api_instance = product-configurator.OptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    step_id = 'step_id_example' # str | 
    body = product-configurator.ProductConfiguratorCreateOptionRequest() # ProductConfiguratorCreateOptionRequest | 

    try:
        # Create Option
        api_response = api_instance.product_configurator_create_option(tenant_id, step_id, body)
        print("The response of OptionApi->product_configurator_create_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionApi->product_configurator_create_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **step_id** | **str**|  | 
 **body** | [**ProductConfiguratorCreateOptionRequest**](ProductConfiguratorCreateOptionRequest.md)|  | 

### Return type

[**ProductconfiguratoroptionEntity**](ProductconfiguratoroptionEntity.md)

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

# **product_configurator_delete_option**
> object product_configurator_delete_option(tenant_id, option_id)

Delete Option

Remove a specific option by specifying the tenant and option IDs. Ensure precision in option management with a straightforward DELETE request, simplifying the elimination of unwanted configuration choices.

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
    api_instance = product-configurator.OptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    option_id = 'option_id_example' # str | 

    try:
        # Delete Option
        api_response = api_instance.product_configurator_delete_option(tenant_id, option_id)
        print("The response of OptionApi->product_configurator_delete_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionApi->product_configurator_delete_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **option_id** | **str**|  | 

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

# **product_configurator_list_options**
> OptionListOptionsResponse product_configurator_list_options(tenant_id, step_id, page_size, body)

List Options

Retrieve a list of options for a specific step based on tenant and step IDs. Customize results by specifying page size for efficient pagination. Submit an empty body to get all options associated with the step.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.option_list_options_response import OptionListOptionsResponse
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
    api_instance = product-configurator.OptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    step_id = 'step_id_example' # str | 
    page_size = 56 # int | 
    body = product-configurator.ProductConfiguratorListPropertiesRequest() # ProductConfiguratorListPropertiesRequest | 

    try:
        # List Options
        api_response = api_instance.product_configurator_list_options(tenant_id, step_id, page_size, body)
        print("The response of OptionApi->product_configurator_list_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionApi->product_configurator_list_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **step_id** | **str**|  | 
 **page_size** | **int**|  | 
 **body** | [**ProductConfiguratorListPropertiesRequest**](ProductConfiguratorListPropertiesRequest.md)|  | 

### Return type

[**OptionListOptionsResponse**](OptionListOptionsResponse.md)

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

# **product_configurator_update_option**
> ProductconfiguratoroptionEntity product_configurator_update_option(tenant_id, option_id, body)

Update Option

Modify an existing option by specifying the tenant and option IDs. Utilize a PUT request with updated option details in the body for seamless customization and fine-tuning of your product configurations.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_update_option_request import ProductConfiguratorUpdateOptionRequest
from product-configurator.models.productconfiguratoroption_entity import ProductconfiguratoroptionEntity
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
    api_instance = product-configurator.OptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    option_id = 'option_id_example' # str | 
    body = product-configurator.ProductConfiguratorUpdateOptionRequest() # ProductConfiguratorUpdateOptionRequest | 

    try:
        # Update Option
        api_response = api_instance.product_configurator_update_option(tenant_id, option_id, body)
        print("The response of OptionApi->product_configurator_update_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionApi->product_configurator_update_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **option_id** | **str**|  | 
 **body** | [**ProductConfiguratorUpdateOptionRequest**](ProductConfiguratorUpdateOptionRequest.md)|  | 

### Return type

[**ProductconfiguratoroptionEntity**](ProductconfiguratoroptionEntity.md)

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

