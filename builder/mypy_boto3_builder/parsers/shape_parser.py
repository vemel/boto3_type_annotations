from typing import Dict, List, Any, Optional

from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.utils.strings import get_class_prefix
from mypy_boto3_builder.logger import get_logger


Shape = Dict[str, Any]


class ShapeParser:
    def __init__(self, service_shape: Shape):
        self._service_shape = service_shape
        self.logger = get_logger()

    @property
    def _shapes(self) -> Shape:
        return self._service_shape.get("shapes", {})

    @property
    def _operations(self) -> Shape:
        return self._service_shape.get("operations", {})

    def _get_shape(self, name: str) -> Shape:
        return self._shapes.get(name, {})

    def _get_operation(self, name: str) -> Optional[Shape]:
        return self._operations.get(name)

    def _parse_arguments(self, shape_name: str) -> List[Argument]:
        shape = self._get_shape(shape_name)
        result = [
            Argument("self", None),
        ]
        required = shape.get("required", [])
        for argument_name, argument_shape in shape["members"].items():
            argument = Argument(
                argument_name, self._parse_shape(argument_shape["shape"])
            )
            if argument_name not in required:
                argument.default = Type.none
            result.append(argument)

        result.sort(key=lambda x: not x.required)
        return result

    def _parse_return_type(self, shape_name: str) -> FakeAnnotation:
        return self._parse_shape(shape_name)

    def get_method(self, method_name: str) -> Optional[Method]:
        operation_name = get_class_prefix(method_name)
        operation_shape = self._get_operation(operation_name)
        if operation_shape is None:
            return None

        return_type: FakeAnnotation = Type.none
        arguments: List[Argument] = []

        if "input" in operation_shape:
            arguments = self._parse_arguments(operation_shape["input"]["shape"])

        if "output" in operation_shape:
            return_type = self._parse_return_type(operation_shape["output"]["shape"])
        return Method(name=method_name, arguments=arguments, return_type=return_type)

    def _parse_shape(self, name: str) -> FakeAnnotation:
        shape = self._get_shape(name)
        shape_type = shape["type"]
        if shape_type in ("integer", "long"):
            return Type.int
        if shape_type == "boolean":
            return Type.bool
        if shape_type in ("double", "float"):
            return Type.float
        if shape_type == "timestamp":
            return ExternalImport(ImportString("datetime"), "datetime")
        if shape_type == "blob":
            return Type.str
        if shape_type == "string":
            if "enum" not in shape:
                return Type.str

            type_literal = TypeLiteral()
            for option in shape["enum"]:
                type_literal.add_literal_child(option)

            return type_literal
        if shape_type == "map":
            type_subscript = TypeSubscript(Type.Dict)
            if "key" in shape:
                type_subscript.add_child(self._parse_shape(shape["key"]["shape"]))
            else:
                type_subscript.add_child(Type.str)
            if "value" in shape:
                type_subscript.add_child(self._parse_shape(shape["value"]["shape"]))
            else:
                type_subscript.add_child(Type.Any)
            return type_subscript
        if shape_type == "structure":
            required = shape.get("required", [])
            typed_dict = TypeTypedDict(f"{name}TypeDef")
            for attr_name, attr_shape in shape["members"].items():
                typed_dict.add_attribute(
                    attr_name,
                    self._parse_shape(attr_shape["shape"]),
                    attr_name in required,
                )
            return typed_dict
        if shape_type == "list":
            type_subscript = TypeSubscript(Type.List)
            if "member" in shape:
                type_subscript.add_child(self._parse_shape(shape["member"]["shape"]))
            else:
                type_subscript.add_child(Type.Any)
            return type_subscript
        self.logger.warning(f"Unknown shape: {shape}")
        return Type.Any
