# product-configurator.StepApi

All URIs are relative to *https://product-configurator.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_configurator_bulk_create_steps**](StepApi.md#product_configurator_bulk_create_steps) | **POST** /v1/{tenantId}/configurator/{configuratorId}/step/create/bulk | Bulk Create Steps
[**product_configurator_bulk_delete_steps**](StepApi.md#product_configurator_bulk_delete_steps) | **POST** /v1/{tenantId}/step/delete/bulk | Bulk Delete Steps
[**product_configurator_copy_step**](StepApi.md#product_configurator_copy_step) | **POST** /v1/{tenantId}/step/{sourceStepId}/copy | Copy Step
[**product_configurator_create_step**](StepApi.md#product_configurator_create_step) | **POST** /v1/{tenantId}/configurator/{configuratorId}/step/create | Create Step
[**product_configurator_delete_step**](StepApi.md#product_configurator_delete_step) | **DELETE** /v1/{tenantId}/step/{stepId} | Delete Step
[**product_configurator_update_step**](StepApi.md#product_configurator_update_step) | **PUT** /v1/{tenantId}/step/{stepId} | Update Step


# **product_configurator_bulk_create_steps**
> ProductconfiguratorstepBulkCreateResponse product_configurator_bulk_create_steps(tenant_id, configurator_id, body)

Bulk Create Steps

Add multiple steps to an existing product configurator simultaneously. Submit a POST request with the necessary step details in the body to efficiently extend the configuration process in bulk. Simplify large-scale configuration management effortlessly.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_bulk_create_steps_request import ProductConfiguratorBulkCreateStepsRequest
from product-configurator.models.productconfiguratorstep_bulk_create_response import ProductconfiguratorstepBulkCreateResponse
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
    api_instance = product-configurator.StepApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    configurator_id = 'configurator_id_example' # str | 
    body = product-configurator.ProductConfiguratorBulkCreateStepsRequest() # ProductConfiguratorBulkCreateStepsRequest | 

    try:
        # Bulk Create Steps
        api_response = api_instance.product_configurator_bulk_create_steps(tenant_id, configurator_id, body)
        print("The response of StepApi->product_configurator_bulk_create_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StepApi->product_configurator_bulk_create_steps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **configurator_id** | **str**|  | 
 **body** | [**ProductConfiguratorBulkCreateStepsRequest**](ProductConfiguratorBulkCreateStepsRequest.md)|  | 

### Return type

[**ProductconfiguratorstepBulkCreateResponse**](ProductconfiguratorstepBulkCreateResponse.md)

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

# **product_configurator_bulk_delete_steps**
> object product_configurator_bulk_delete_steps(tenant_id, body)

Bulk Delete Steps

Efficiently remove multiple steps from a product configurator using a bulk delete operation. Specify the tenant ID and submit a POST request with the list of step IDs in the body for streamlined configuration management.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_bulk_delete_steps_request import ProductConfiguratorBulkDeleteStepsRequest
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
    api_instance = product-configurator.StepApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = product-configurator.ProductConfiguratorBulkDeleteStepsRequest() # ProductConfiguratorBulkDeleteStepsRequest | 

    try:
        # Bulk Delete Steps
        api_response = api_instance.product_configurator_bulk_delete_steps(tenant_id, body)
        print("The response of StepApi->product_configurator_bulk_delete_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StepApi->product_configurator_bulk_delete_steps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**ProductConfiguratorBulkDeleteStepsRequest**](ProductConfiguratorBulkDeleteStepsRequest.md)|  | 

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

# **product_configurator_copy_step**
> ProductconfiguratorstepEntity product_configurator_copy_step(tenant_id, source_step_id, body)

Copy Step

Duplicate an existing step from the source to a specified tenant. Utilize a POST request with an empty body to initiate the copy process, creating a new step based on the source configuration. Streamline step replication effortlessly.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_copy_step_request import ProductConfiguratorCopyStepRequest
from product-configurator.models.productconfiguratorstep_entity import ProductconfiguratorstepEntity
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
    api_instance = product-configurator.StepApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    source_step_id = 'source_step_id_example' # str | 
    body = product-configurator.ProductConfiguratorCopyStepRequest() # ProductConfiguratorCopyStepRequest | 

    try:
        # Copy Step
        api_response = api_instance.product_configurator_copy_step(tenant_id, source_step_id, body)
        print("The response of StepApi->product_configurator_copy_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StepApi->product_configurator_copy_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **source_step_id** | **str**|  | 
 **body** | [**ProductConfiguratorCopyStepRequest**](ProductConfiguratorCopyStepRequest.md)|  | 

### Return type

[**ProductconfiguratorstepEntity**](ProductconfiguratorstepEntity.md)

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

# **product_configurator_create_step**
> ProductconfiguratorstepEntity product_configurator_create_step(tenant_id, configurator_id, body)

Create Step

Add a new step to an existing product configurator by specifying the tenant and configurator IDs. Utilize a POST request with the required step details in the body to seamlessly extend the configuration process.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_create_step_request import ProductConfiguratorCreateStepRequest
from product-configurator.models.productconfiguratorstep_entity import ProductconfiguratorstepEntity
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
    api_instance = product-configurator.StepApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    configurator_id = 'configurator_id_example' # str | 
    body = product-configurator.ProductConfiguratorCreateStepRequest() # ProductConfiguratorCreateStepRequest | 

    try:
        # Create Step
        api_response = api_instance.product_configurator_create_step(tenant_id, configurator_id, body)
        print("The response of StepApi->product_configurator_create_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StepApi->product_configurator_create_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **configurator_id** | **str**|  | 
 **body** | [**ProductConfiguratorCreateStepRequest**](ProductConfiguratorCreateStepRequest.md)|  | 

### Return type

[**ProductconfiguratorstepEntity**](ProductconfiguratorstepEntity.md)

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

# **product_configurator_delete_step**
> GooglerpcStatus product_configurator_delete_step(tenant_id, step_id)

Delete Step

Remove a step from a product configurator by specifying the tenant and step IDs. Ensure precision in configuration management with a straightforward DELETE request, simplifying the elimination of unwanted steps.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.googlerpc_status import GooglerpcStatus
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
    api_instance = product-configurator.StepApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    step_id = 'step_id_example' # str | 

    try:
        # Delete Step
        api_response = api_instance.product_configurator_delete_step(tenant_id, step_id)
        print("The response of StepApi->product_configurator_delete_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StepApi->product_configurator_delete_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **step_id** | **str**|  | 

### Return type

[**GooglerpcStatus**](GooglerpcStatus.md)

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

# **product_configurator_update_step**
> ProductconfiguratorstepEntity product_configurator_update_step(tenant_id, step_id, body)

Update Step

Modify an existing step within a product configurator by specifying the tenant and step IDs. Utilize a PUT request with updated step details in the body for seamless customization and fine-tuning of your product configurations.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_update_step_request import ProductConfiguratorUpdateStepRequest
from product-configurator.models.productconfiguratorstep_entity import ProductconfiguratorstepEntity
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
    api_instance = product-configurator.StepApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    step_id = 'step_id_example' # str | 
    body = product-configurator.ProductConfiguratorUpdateStepRequest() # ProductConfiguratorUpdateStepRequest | 

    try:
        # Update Step
        api_response = api_instance.product_configurator_update_step(tenant_id, step_id, body)
        print("The response of StepApi->product_configurator_update_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StepApi->product_configurator_update_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **step_id** | **str**|  | 
 **body** | [**ProductConfiguratorUpdateStepRequest**](ProductConfiguratorUpdateStepRequest.md)|  | 

### Return type

[**ProductconfiguratorstepEntity**](ProductconfiguratorstepEntity.md)

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

