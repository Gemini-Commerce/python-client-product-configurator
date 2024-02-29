# product-configurator.PropertyApi

All URIs are relative to *https://product-configurator.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_configurator_bulk_create_properties**](PropertyApi.md#product_configurator_bulk_create_properties) | **POST** /v1/{tenantId}/property/create/bulk | Bulk Create Properties
[**product_configurator_bulk_update_properties**](PropertyApi.md#product_configurator_bulk_update_properties) | **PUT** /v1/{tenantId}/properties/bulk | Bulk Update Properties
[**product_configurator_create_property**](PropertyApi.md#product_configurator_create_property) | **POST** /v1/{tenantId}/property/create | Create Property
[**product_configurator_list_properties**](PropertyApi.md#product_configurator_list_properties) | **POST** /v1/{tenantId}/matrix/{matrixId}/page-size/{pageSize}/properties | List Properties
[**product_configurator_update_property**](PropertyApi.md#product_configurator_update_property) | **PUT** /v1/{tenantId}/property/{propertyId} | Update Property


# **product_configurator_bulk_create_properties**
> ProductconfiguratorpropertyBulkCreateResponse product_configurator_bulk_create_properties(tenant_id, body)

Bulk Create Properties

Efficiently add multiple properties to configurations with a bulk create operation. Specify the tenant ID and submit a POST request with the necessary property details in the body for streamlined property management.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_bulk_create_properties_request import ProductConfiguratorBulkCreatePropertiesRequest
from product-configurator.models.productconfiguratorproperty_bulk_create_response import ProductconfiguratorpropertyBulkCreateResponse
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
    api_instance = product-configurator.PropertyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = product-configurator.ProductConfiguratorBulkCreatePropertiesRequest() # ProductConfiguratorBulkCreatePropertiesRequest | 

    try:
        # Bulk Create Properties
        api_response = api_instance.product_configurator_bulk_create_properties(tenant_id, body)
        print("The response of PropertyApi->product_configurator_bulk_create_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->product_configurator_bulk_create_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**ProductConfiguratorBulkCreatePropertiesRequest**](ProductConfiguratorBulkCreatePropertiesRequest.md)|  | 

### Return type

[**ProductconfiguratorpropertyBulkCreateResponse**](ProductconfiguratorpropertyBulkCreateResponse.md)

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

# **product_configurator_bulk_update_properties**
> ProductconfiguratorpropertyBulkUpdateResponse product_configurator_bulk_update_properties(tenant_id, body)

Bulk Update Properties

Effortlessly update multiple properties. Specify the tenant ID and submit a PUT request with the updated property details in the body. Streamline the customization of a multitude of properties in one go.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_bulk_update_properties_request import ProductConfiguratorBulkUpdatePropertiesRequest
from product-configurator.models.productconfiguratorproperty_bulk_update_response import ProductconfiguratorpropertyBulkUpdateResponse
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
    api_instance = product-configurator.PropertyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = product-configurator.ProductConfiguratorBulkUpdatePropertiesRequest() # ProductConfiguratorBulkUpdatePropertiesRequest | 

    try:
        # Bulk Update Properties
        api_response = api_instance.product_configurator_bulk_update_properties(tenant_id, body)
        print("The response of PropertyApi->product_configurator_bulk_update_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->product_configurator_bulk_update_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**ProductConfiguratorBulkUpdatePropertiesRequest**](ProductConfiguratorBulkUpdatePropertiesRequest.md)|  | 

### Return type

[**ProductconfiguratorpropertyBulkUpdateResponse**](ProductconfiguratorpropertyBulkUpdateResponse.md)

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

# **product_configurator_create_property**
> ProductconfiguratorpropertyEntity product_configurator_create_property(tenant_id, body)

Create Property

Integrate a new property into configurations by specifying the tenant ID. Use a POST request with the required property details in the body for seamless customization and expansion of product configurations.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_create_property_request import ProductConfiguratorCreatePropertyRequest
from product-configurator.models.productconfiguratorproperty_entity import ProductconfiguratorpropertyEntity
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
    api_instance = product-configurator.PropertyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = product-configurator.ProductConfiguratorCreatePropertyRequest() # ProductConfiguratorCreatePropertyRequest | 

    try:
        # Create Property
        api_response = api_instance.product_configurator_create_property(tenant_id, body)
        print("The response of PropertyApi->product_configurator_create_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->product_configurator_create_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**ProductConfiguratorCreatePropertyRequest**](ProductConfiguratorCreatePropertyRequest.md)|  | 

### Return type

[**ProductconfiguratorpropertyEntity**](ProductconfiguratorpropertyEntity.md)

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

# **product_configurator_list_properties**
> PropertyListPropertiesResponse product_configurator_list_properties(tenant_id, matrix_id, page_size, body)

List Properties

Retrieve a list of properties for a specific matrix based on tenant and matrix IDs. Customize results by specifying page size for efficient pagination. Submit an empty body to get all properties associated with the matrix.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_list_properties_request import ProductConfiguratorListPropertiesRequest
from product-configurator.models.property_list_properties_response import PropertyListPropertiesResponse
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
    api_instance = product-configurator.PropertyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    matrix_id = 'matrix_id_example' # str | 
    page_size = 'page_size_example' # str | 
    body = product-configurator.ProductConfiguratorListPropertiesRequest() # ProductConfiguratorListPropertiesRequest | 

    try:
        # List Properties
        api_response = api_instance.product_configurator_list_properties(tenant_id, matrix_id, page_size, body)
        print("The response of PropertyApi->product_configurator_list_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->product_configurator_list_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **matrix_id** | **str**|  | 
 **page_size** | **str**|  | 
 **body** | [**ProductConfiguratorListPropertiesRequest**](ProductConfiguratorListPropertiesRequest.md)|  | 

### Return type

[**PropertyListPropertiesResponse**](PropertyListPropertiesResponse.md)

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

# **product_configurator_update_property**
> ProductconfiguratorpropertyEntity product_configurator_update_property(tenant_id, property_id, body)

Update Property

Modify an existing property by specifying the tenant and property IDs. Utilize a PUT request with updated property details in the body for seamless customization and fine-tuning of your product configurations.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_update_property_request import ProductConfiguratorUpdatePropertyRequest
from product-configurator.models.productconfiguratorproperty_entity import ProductconfiguratorpropertyEntity
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
    api_instance = product-configurator.PropertyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    property_id = 'property_id_example' # str | 
    body = product-configurator.ProductConfiguratorUpdatePropertyRequest() # ProductConfiguratorUpdatePropertyRequest | 

    try:
        # Update Property
        api_response = api_instance.product_configurator_update_property(tenant_id, property_id, body)
        print("The response of PropertyApi->product_configurator_update_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->product_configurator_update_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **property_id** | **str**|  | 
 **body** | [**ProductConfiguratorUpdatePropertyRequest**](ProductConfiguratorUpdatePropertyRequest.md)|  | 

### Return type

[**ProductconfiguratorpropertyEntity**](ProductconfiguratorpropertyEntity.md)

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

