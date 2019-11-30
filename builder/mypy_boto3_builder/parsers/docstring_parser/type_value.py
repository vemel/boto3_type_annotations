"""
Structure for parsed as dict request or response syntax values.
"""
from __future__ import annotations

from typing import Dict, Any, List, Union, Optional, IO
from datetime import datetime

from mypy_boto3_builder.type_maps.syntax_type_map import SYNTAX_TYPE_MAP
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_class import TypeClass


class TypeValue:
    """
    Structure for parsed as dict request or response syntax values.
    """

    def __init__(self, prefix: str, value: Dict[str, Any]) -> None:
        self.prefix = prefix
        self.raw = value
        self.dict_items = value.get("dict_items")
        self.set_items: Optional[List[Any]] = value.get("set_items")
        self.list_items: Optional[List[Any]] = value.get("list_items")
        self.func_call: Optional[Dict[str, Any]] = value.get("func_call")
        self.union_items: List[Any] = []
        if value.get("union_first_item"):
            self.union_items.append(value["union_first_item"])
            self.union_items.extend(value["union_rest_items"])
        self.literal_items: List[Any] = []
        if value.get("literal_first_item"):
            self.literal_items.append(value["literal_first_item"])
            self.literal_items.extend(value["literal_rest_items"])

        self.value: Optional[str] = value.get("value")

    def is_dict(self) -> bool:
        return self.dict_items is not None

    def is_list(self) -> bool:
        return self.list_items is not None

    def is_literal(self) -> bool:
        return bool(self.literal_items)

    def is_set(self) -> bool:
        return bool(self.set_items)

    def is_union(self) -> bool:
        return bool(self.union_items)

    def is_func_call(self) -> bool:
        return bool(self.func_call)

    def is_plain(self) -> bool:
        return self.value is not None

    def _get_type_dict(self) -> FakeAnnotation:
        if not self.dict_items:
            return TypeSubscript(Dict, [TypeClass(str), TypeAnnotation.Any()])

        first_key = self.dict_items[0]["key"]
        if first_key in SYNTAX_TYPE_MAP:
            result = TypeSubscript(Dict)
            result.add_child(SYNTAX_TYPE_MAP[first_key])
            result.add_child(
                TypeValue(self.prefix, self.dict_items[0]["value"]).get_type()
            )
            return result

        typed_dict = TypeTypedDict(f"{self.prefix}TypeDef")
        for item in self.dict_items:
            key_name = self._parse_constant(item["key"])
            prefix = f"{self.prefix}{key_name}"
            typed_dict.add_attribute(
                key_name, TypeValue(prefix, item["value"]).get_type(), required=False,
            )
        return typed_dict

    def _get_type_list(self) -> TypeSubscript:
        if not self.list_items:
            return TypeSubscript(List, [TypeAnnotation.Any()])

        result = TypeSubscript(List)
        for item_index, item in enumerate(self.list_items):
            prefix = f"{self.prefix}{item_index if item_index else ''}"
            result.add_child(TypeValue(prefix, item).get_type())
        return result

    def _get_type_union(self) -> TypeSubscript:
        result = TypeSubscript(Union)
        for item_index, item in enumerate(self.union_items):
            prefix = f"{self.prefix}{item_index if item_index else ''}"
            result.add_child(TypeValue(prefix, item).get_type())
        return result

    def _get_type_set(self) -> TypeAnnotation:
        if not self.set_items:
            return TypeAnnotation.Any()

        plain_values = [i["value"] for i in self.set_items]
        if plain_values == ["'... recursive ...'"]:
            return TypeAnnotation.Any()

        raise ValueError(f"Unknown set: {self.raw}")

    def _get_type_func_call(self) -> TypeClass:
        if not self.func_call:
            raise ValueError(f"Value is not a func call: {self.raw}")

        if self.func_call["name"] == "datetime":
            return TypeClass(datetime)

        raise ValueError(f"Unknown function {self.func_call}")

    def _get_type_plain(self) -> FakeAnnotation:
        if not self.value:
            raise ValueError(f"Value is not plain: {self.raw}")

        if self.value in SYNTAX_TYPE_MAP:
            return SYNTAX_TYPE_MAP[self.value]

        return TypeClass(str)

    def _get_type_literal(self) -> FakeAnnotation:
        if not self.literal_items:
            raise ValueError(f"Value is not literal: {self.raw}")

        plain_values = [i["value"] for i in self.literal_items]
        if plain_values == ["True", "False"]:
            return TypeClass(bool)
        if plain_values == ["b'bytes'", "file"]:
            return TypeSubscript(Union, [TypeClass(bytes), TypeAnnotation(IO)])

        result = TypeLiteral()
        for item in self.literal_items:
            result.add_literal_child(self._parse_constant(item["value"]))

        return result

    @staticmethod
    def _parse_constant(value: str) -> Any:
        if value.startswith("'"):
            return value.replace("'", "")

        if value.isdigit():
            return int(value)

        raise ValueError(f"Invalid constant: {value}")

    def get_type(self) -> FakeAnnotation:
        if self.is_list():
            return self._get_type_list()
        if self.is_dict():
            return self._get_type_dict()
        if self.is_set():
            return self._get_type_set()
        if self.is_func_call():
            return self._get_type_func_call()
        if self.is_union():
            return self._get_type_union()
        if self.is_literal():
            return self._get_type_literal()
        if self.is_plain():
            return self._get_type_plain()

        raise ValueError(f"Unknown value: {self.raw}")
