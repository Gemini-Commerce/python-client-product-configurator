# coding: utf-8

"""
    Product Configurator Service

    ## Introduction  This comprehensive guide will equip you with the knowledge to integrate and leverage our Product Configurator Service in your applications.  ## Quick Start  Get up and running in no time! Follow these steps to kickstart your integration:  1. **Authentication:** Obtain your integration JWT to authenticate your requests. 2. **Client Libraries:** Explore our GitHub repositories to grab client libraries in your preferred programming language. 3. **API Overview:** Familiarize yourself with our RESTful API using the OpenAPI specification.  ## Integration  ### API Overview  Our RESTful API is the gateway to unlocking the full potential of Product Configurator. Check out the detailed [API Reference](/docs/category/configurator) for a granular understanding of each endpoint and request/response format.  ### Client Libraries  To expedite your integration process, we provide client libraries for various programming languages. Find the one that suits your stack in our [GitHub repositories](https://github.com/Gemini-Commerce).  ### Authentication  Security is paramount. Learn how to authenticate your requests using JWT. This ensures a secure and reliable connection between your application and Product Configurator.  ## Configuration Management  ### Configurator Lifecycle  Understand the lifecycle of configurators, from draft to active and deleted. This flexibility allows you to manage configurations at your own pace.  ### Steps and Options  Configure product steps with ease and define options effortlessly. Explore the power of dependencies to create dynamic and intuitive configurations.  ### Matrices  Delve into matrices—your secret weapon. Explore price and weight matrices, and learn how configured steps influence properties and pricing.  ### Price Management  Unleash dynamic pricing with our versatile price matrices. From fixed prices to incremental structures, adapt to diverse pricing models effortlessly.  ## Security  Your data is in safe hands. Discover how Product Configurator ensures security through JWT authentication, safeguarding your sensitive information.  ## Backward Compatibility  Stay ahead of the curve. Learn about our versioning strategy, providing backward compatibility while allowing our service to evolve seamlessly.  ## Developer Support  Have questions? Need assistance? Write to us at [info@gemini-commerce.com](mailto:info@gemini-commerce.com) and we will get back to you.

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from product-configurator.models.localisation_localized_text import LocalisationLocalizedText
from product-configurator.models.productconfiguratoroption_entity import ProductconfiguratoroptionEntity
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProductconfiguratorstepEntity(BaseModel):
    """
    ProductconfiguratorstepEntity
    """ # noqa: E501
    id: Optional[StrictStr] = None
    grn: Optional[StrictStr] = None
    label: Optional[LocalisationLocalizedText] = None
    description: Optional[LocalisationLocalizedText] = None
    subject_to_step_id: Optional[StrictStr] = Field(default=None, alias="subjectToStepId")
    position: Optional[StrictStr] = None
    is_required: Optional[StrictBool] = Field(default=None, alias="isRequired")
    options: Optional[List[ProductconfiguratoroptionEntity]] = None
    has_multiple_selection: Optional[StrictBool] = Field(default=None, alias="hasMultipleSelection")
    options_have_quantity: Optional[StrictBool] = Field(default=None, alias="optionsHaveQuantity")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "grn", "label", "description", "subjectToStepId", "position", "isRequired", "options", "hasMultipleSelection", "optionsHaveQuantity", "createdAt", "updatedAt"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProductconfiguratorstepEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of label
        if self.label:
            _dict['label'] = self.label.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item in self.options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['options'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProductconfiguratorstepEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "grn": obj.get("grn"),
            "label": LocalisationLocalizedText.from_dict(obj.get("label")) if obj.get("label") is not None else None,
            "description": LocalisationLocalizedText.from_dict(obj.get("description")) if obj.get("description") is not None else None,
            "subjectToStepId": obj.get("subjectToStepId"),
            "position": obj.get("position"),
            "isRequired": obj.get("isRequired"),
            "options": [ProductconfiguratoroptionEntity.from_dict(_item) for _item in obj.get("options")] if obj.get("options") is not None else None,
            "hasMultipleSelection": obj.get("hasMultipleSelection"),
            "optionsHaveQuantity": obj.get("optionsHaveQuantity"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


