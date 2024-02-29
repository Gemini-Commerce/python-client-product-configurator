# product-configurator.ProductConfiguratorApi

All URIs are relative to *https://product-configurator.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_configurator_get_property**](ProductConfiguratorApi.md#product_configurator_get_property) | **GET** /v1/{tenantId}/property/{propertyId} | 
[**product_configurator_list_properties_by_configuration**](ProductConfiguratorApi.md#product_configurator_list_properties_by_configuration) | **POST** /v1/{tenantId}/configurator/{configuratorId}/page-size/{pageSize}/properties | 


# **product_configurator_get_property**
> ProductconfiguratorpropertyEntity product_configurator_get_property(tenant_id, property_id)



### Example


```python
import time
import os
import product-configurator
from product-configurator.models.productconfiguratorproperty_entity import ProductconfiguratorpropertyEntity
from product-configurator.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product-configurator.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product-configurator.Configuration(
    host = "https://product-configurator.api.gogemini.io"
)


# Enter a context with an instance of the API client
with product-configurator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product-configurator.ProductConfiguratorApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    property_id = 'property_id_example' # str | 

    try:
        api_response = api_instance.product_configurator_get_property(tenant_id, property_id)
        print("The response of ProductConfiguratorApi->product_configurator_get_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductConfiguratorApi->product_configurator_get_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **property_id** | **str**|  | 

### Return type

[**ProductconfiguratorpropertyEntity**](ProductconfiguratorpropertyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_configurator_list_properties_by_configuration**
> PropertyListPropertiesByConfigurationResponse product_configurator_list_properties_by_configuration(tenant_id, configurator_id, page_size, body)



### Example


```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_list_properties_by_configuration_request import ProductConfiguratorListPropertiesByConfigurationRequest
from product-configurator.models.property_list_properties_by_configuration_response import PropertyListPropertiesByConfigurationResponse
from product-configurator.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product-configurator.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product-configurator.Configuration(
    host = "https://product-configurator.api.gogemini.io"
)


# Enter a context with an instance of the API client
with product-configurator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product-configurator.ProductConfiguratorApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    configurator_id = 'configurator_id_example' # str | 
    page_size = 'page_size_example' # str | 
    body = product-configurator.ProductConfiguratorListPropertiesByConfigurationRequest() # ProductConfiguratorListPropertiesByConfigurationRequest | 

    try:
        api_response = api_instance.product_configurator_list_properties_by_configuration(tenant_id, configurator_id, page_size, body)
        print("The response of ProductConfiguratorApi->product_configurator_list_properties_by_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductConfiguratorApi->product_configurator_list_properties_by_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **configurator_id** | **str**|  | 
 **page_size** | **str**|  | 
 **body** | [**ProductConfiguratorListPropertiesByConfigurationRequest**](ProductConfiguratorListPropertiesByConfigurationRequest.md)|  | 

### Return type

[**PropertyListPropertiesByConfigurationResponse**](PropertyListPropertiesByConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

