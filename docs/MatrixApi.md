# product-configurator.MatrixApi

All URIs are relative to *https://product-configurator.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_configurator_create_matrix**](MatrixApi.md#product_configurator_create_matrix) | **POST** /v1/{tenantId}/matrix/create | Create Matrix
[**product_configurator_delete_matrix**](MatrixApi.md#product_configurator_delete_matrix) | **DELETE** /v1/{tenantId}/matrix/{matrixId} | Delete Matrix
[**product_configurator_get_matrix**](MatrixApi.md#product_configurator_get_matrix) | **GET** /v1/{tenantId}/matrix/{matrixId} | Get Matrix
[**product_configurator_list_matrices**](MatrixApi.md#product_configurator_list_matrices) | **POST** /v1/{tenantId}/configurator/{configuratorId}/page-size/{pageSize}/matrices | List Matrices
[**product_configurator_remove_pricelist_from_matrix**](MatrixApi.md#product_configurator_remove_pricelist_from_matrix) | **DELETE** /v1/{tenantId}/matrix/{matrixId}/pricelist/{pricelistGrn} | Remove Pricelist from Matrix
[**product_configurator_update_matrix**](MatrixApi.md#product_configurator_update_matrix) | **PUT** /v1/{tenantId}/matrix/{matrixId} | Update Matrix


# **product_configurator_create_matrix**
> ProductconfiguratormatrixEntity product_configurator_create_matrix(tenant_id, body)

Create Matrix

Establish a new matrix by specifying the tenant ID. Utilize a POST request with the required matrix details in the body for seamless customization and expansion of matrix configurations.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_create_matrix_request import ProductConfiguratorCreateMatrixRequest
from product-configurator.models.productconfiguratormatrix_entity import ProductconfiguratormatrixEntity
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
    api_instance = product-configurator.MatrixApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = product-configurator.ProductConfiguratorCreateMatrixRequest() # ProductConfiguratorCreateMatrixRequest | 

    try:
        # Create Matrix
        api_response = api_instance.product_configurator_create_matrix(tenant_id, body)
        print("The response of MatrixApi->product_configurator_create_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatrixApi->product_configurator_create_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**ProductConfiguratorCreateMatrixRequest**](ProductConfiguratorCreateMatrixRequest.md)|  | 

### Return type

[**ProductconfiguratormatrixEntity**](ProductconfiguratormatrixEntity.md)

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

# **product_configurator_delete_matrix**
> object product_configurator_delete_matrix(tenant_id, matrix_id)

Delete Matrix

Remove a specific matrix by specifying the tenant and matrix IDs. Ensure precision in matrix management with a straightforward DELETE request, simplifying the elimination of unwanted matrix configurations.

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
    api_instance = product-configurator.MatrixApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    matrix_id = 'matrix_id_example' # str | 

    try:
        # Delete Matrix
        api_response = api_instance.product_configurator_delete_matrix(tenant_id, matrix_id)
        print("The response of MatrixApi->product_configurator_delete_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatrixApi->product_configurator_delete_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **matrix_id** | **str**|  | 

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

# **product_configurator_get_matrix**
> ProductconfiguratormatrixEntity product_configurator_get_matrix(tenant_id, matrix_id)

Get Matrix

Retrieve matrix details by specifying the tenant and matrix IDs. Utilize a GET request for a comprehensive view of matrix configurations within your product configurator service.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.productconfiguratormatrix_entity import ProductconfiguratormatrixEntity
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
    api_instance = product-configurator.MatrixApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    matrix_id = 'matrix_id_example' # str | 

    try:
        # Get Matrix
        api_response = api_instance.product_configurator_get_matrix(tenant_id, matrix_id)
        print("The response of MatrixApi->product_configurator_get_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatrixApi->product_configurator_get_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **matrix_id** | **str**|  | 

### Return type

[**ProductconfiguratormatrixEntity**](ProductconfiguratormatrixEntity.md)

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

# **product_configurator_list_matrices**
> MatrixListMatricesResponse product_configurator_list_matrices(tenant_id, configurator_id, page_size, body)

List Matrices

Retrieve a list of matrices for a specific configurator based on tenant and configurator IDs. Customize results by specifying page size for efficient pagination. Submit an empty body to get all matrices associated with the configurator. Streamline matrix management effortlessly.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.matrix_list_matrices_response import MatrixListMatricesResponse
from product-configurator.models.product_configurator_list_matrices_request import ProductConfiguratorListMatricesRequest
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
    api_instance = product-configurator.MatrixApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    configurator_id = 'configurator_id_example' # str | 
    page_size = 'page_size_example' # str | 
    body = product-configurator.ProductConfiguratorListMatricesRequest() # ProductConfiguratorListMatricesRequest | 

    try:
        # List Matrices
        api_response = api_instance.product_configurator_list_matrices(tenant_id, configurator_id, page_size, body)
        print("The response of MatrixApi->product_configurator_list_matrices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatrixApi->product_configurator_list_matrices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **configurator_id** | **str**|  | 
 **page_size** | **str**|  | 
 **body** | [**ProductConfiguratorListMatricesRequest**](ProductConfiguratorListMatricesRequest.md)|  | 

### Return type

[**MatrixListMatricesResponse**](MatrixListMatricesResponse.md)

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

# **product_configurator_remove_pricelist_from_matrix**
> ProductconfiguratormatrixEntity product_configurator_remove_pricelist_from_matrix(tenant_id, matrix_id, pricelist_grn)

Remove Pricelist from Matrix

Remove a specific pricelist from a matrix by specifying the tenant, matrix, and pricelist IDs. Use a DELETE request for precise management of pricelist configurations within your product configurator service.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.productconfiguratormatrix_entity import ProductconfiguratormatrixEntity
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
    api_instance = product-configurator.MatrixApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    matrix_id = 'matrix_id_example' # str | 
    pricelist_grn = 'pricelist_grn_example' # str | 

    try:
        # Remove Pricelist from Matrix
        api_response = api_instance.product_configurator_remove_pricelist_from_matrix(tenant_id, matrix_id, pricelist_grn)
        print("The response of MatrixApi->product_configurator_remove_pricelist_from_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatrixApi->product_configurator_remove_pricelist_from_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **matrix_id** | **str**|  | 
 **pricelist_grn** | **str**|  | 

### Return type

[**ProductconfiguratormatrixEntity**](ProductconfiguratormatrixEntity.md)

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

# **product_configurator_update_matrix**
> ProductconfiguratormatrixEntity product_configurator_update_matrix(tenant_id, matrix_id, body)

Update Matrix

Modify an existing matrix by specifying the tenant and matrix IDs. Utilize a PUT request with updated matrix details in the body for seamless customization and fine-tuning of your product configurations. Keep your matrices in sync effortlessly.

### Example

* OAuth Authentication (standardAuthorization):
* Api Key Authentication (APIAuthorization):

```python
import time
import os
import product-configurator
from product-configurator.models.product_configurator_update_matrix_request import ProductConfiguratorUpdateMatrixRequest
from product-configurator.models.productconfiguratormatrix_entity import ProductconfiguratormatrixEntity
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
    api_instance = product-configurator.MatrixApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    matrix_id = 'matrix_id_example' # str | 
    body = product-configurator.ProductConfiguratorUpdateMatrixRequest() # ProductConfiguratorUpdateMatrixRequest | 

    try:
        # Update Matrix
        api_response = api_instance.product_configurator_update_matrix(tenant_id, matrix_id, body)
        print("The response of MatrixApi->product_configurator_update_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatrixApi->product_configurator_update_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **matrix_id** | **str**|  | 
 **body** | [**ProductConfiguratorUpdateMatrixRequest**](ProductConfiguratorUpdateMatrixRequest.md)|  | 

### Return type

[**ProductconfiguratormatrixEntity**](ProductconfiguratormatrixEntity.md)

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

