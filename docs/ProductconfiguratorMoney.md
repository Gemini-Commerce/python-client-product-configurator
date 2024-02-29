# # ProductconfiguratorMoney
Represents an amount of money.

## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units**| **str** | The whole units of the amount. For example if &#x60;currencyCode&#x60; is &#x60;\&quot;USD\&quot;&#x60;, then 1 unit is one US dollar.  | [optional]
**micros**| **int** | Number of micro (10^-6) units of the amount. The value must be between -999,999 and +999,999 inclusive. If &#x60;units&#x60; is positive, &#x60;micros&#x60; must be positive or zero. If &#x60;units&#x60; is zero, &#x60;micros&#x60; can be positive, zero, or negative. If &#x60;units&#x60; is negative, &#x60;micros&#x60; must be negative or zero. For example $-1.75 is represented as &#x60;units&#x60;&#x3D;-1 and &#x60;micros&#x60;&#x3D;-750,000.  | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

