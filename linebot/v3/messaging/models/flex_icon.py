# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from linebot.v3.messaging.models.flex_component import FlexComponent

class FlexIcon(FlexComponent):
    """
    FlexIcon
    https://developers.line.biz/en/reference/messaging-api/#icon
    """
    url: Optional[StrictStr] = None
    size: Optional[StrictStr] = None
    aspect_ratio: Optional[StrictStr] = Field(None, alias="aspectRatio")
    margin: Optional[StrictStr] = None
    position: Optional[StrictStr] = None
    offset_top: Optional[StrictStr] = Field(None, alias="offsetTop")
    offset_bottom: Optional[StrictStr] = Field(None, alias="offsetBottom")
    offset_start: Optional[StrictStr] = Field(None, alias="offsetStart")
    offset_end: Optional[StrictStr] = Field(None, alias="offsetEnd")
    type: str = "icon"

    __properties = ["type", "url", "size", "aspectRatio", "margin", "position", "offsetTop", "offsetBottom", "offsetStart", "offsetEnd"]

    @validator('position')
    def position_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('relative', 'absolute'):
            raise ValueError("must be one of enum values ('relative', 'absolute')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FlexIcon:
        """Create an instance of FlexIcon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FlexIcon:
        """Create an instance of FlexIcon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FlexIcon.parse_obj(obj)

        _obj = FlexIcon.parse_obj({
            "type": obj.get("type"),
            "url": obj.get("url"),
            "size": obj.get("size"),
            "aspect_ratio": obj.get("aspectRatio"),
            "margin": obj.get("margin"),
            "position": obj.get("position"),
            "offset_top": obj.get("offsetTop"),
            "offset_bottom": obj.get("offsetBottom"),
            "offset_start": obj.get("offsetStart"),
            "offset_end": obj.get("offsetEnd")
        })
        return _obj
