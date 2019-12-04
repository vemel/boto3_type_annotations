"""
Helpers for parsing methods and attributes.
"""
import inspect
import textwrap
from typing import List, Dict, Any
from types import FunctionType

from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.type_maps.docless_method_argument_map import (
    DOCLESS_METHOD_ARGUMENT_MAP,
)
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.utils.strings import get_class_prefix
from mypy_boto3_builder.parsers.docstring_parser.argspec_parser import ArgSpecParser
from mypy_boto3_builder.parsers.docstring_parser.docstring_parser import DocstringParser
from mypy_boto3_builder.logger import get_logger


def get_public_methods(inspect_class: Any) -> Dict[str, FunctionType]:
    """
    Extract public methods from any class.

    Arguments:
        inspect_class -- Inspect class.

    Returns:
        A dictionary of method name and method.
    """
    class_members = inspect.getmembers(inspect_class)
    methods: Dict[str, FunctionType] = {}
    for name, member in class_members:
        if not inspect.ismethod(member):
            continue

        if name.startswith("_"):
            continue

        methods[name] = member

    return methods


def parse_attributes(resource: Boto3ServiceResource) -> List[Attribute]:
    """
    Extract attributes from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Attribute structures.
    """
    result: List[Attribute] = []
    if not resource.meta.client:
        return result
    if not resource.meta.resource_model:
        return result

    service_model = resource.meta.client.meta.service_model
    if resource.meta.resource_model.shape:
        shape = service_model.shape_for(resource.meta.resource_model.shape)
        attributes = resource.meta.resource_model.get_attributes(shape)
        for name, attribute in attributes.items():
            result.append(
                Attribute(
                    name, DocstringParser.parse_type(attribute[1].type_name, name)
                )
            )

    return result


def parse_method(parent_name: str, name: str, method: FunctionType) -> Method:
    """
    Parse method to a structure.

    Arguments:
        parent_name -- Parent class name.
        method -- Inspect method.

    Returns:
        Method structure.
    """
    logger = get_logger()
    logger.debug(f"Parsing {parent_name}.{name} method")
    docstring = textwrap.dedent(inspect.getdoc(method) or "")
    return_type: FakeAnnotation = Type.none
    if not docstring:
        logger.debug(f"Fixing {parent_name}.{name} method with no docstring")
        return Method(
            name=name,
            arguments=DOCLESS_METHOD_ARGUMENT_MAP[f"{parent_name}.{name}"],
            return_type=return_type,
        )

    prefix = f"{get_class_prefix(parent_name)}{get_class_prefix(name)}"
    arg_spec_parser = ArgSpecParser(prefix)
    arguments = arg_spec_parser.get_function_arguments(method)
    docstring_parser = DocstringParser(prefix, arguments)
    arguments = docstring_parser.get_arguments(docstring)
    return_type = docstring_parser.get_return_type(docstring)

    return Method(name=name, arguments=arguments, return_type=return_type)
