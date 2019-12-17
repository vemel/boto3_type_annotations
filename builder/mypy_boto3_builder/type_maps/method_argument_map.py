"""
String to type annotation map that find type annotation by method and argument name.
"""
from typing import Dict, Optional, List

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_maps.typed_dicts import ec2_tag_type


__all__ = ("get_method_arguments_stub",)


MethodTypeMap = Dict[str, List[Argument]]
ClassTypeMap = Dict[str, MethodTypeMap]
ServiceTypeMap = Dict[str, ClassTypeMap]


METHOD_MAP: ServiceTypeMap = {
    ServiceNameCatalog.ec2.boto3_name: {
        "Instance": {
            "delete_tags": [
                Argument("Resources", TypeSubscript(Type.List, [Type.Any])),
                Argument("Tags", TypeSubscript(Type.List, [ec2_tag_type]), Type.none),
                Argument("DryRun", Type.bool, Type.none),
            ]
        },
    },
}


def get_method_arguments_stub(
    service_name: ServiceName, class_name: str, method_name: str
) -> Optional[List[Argument]]:
    return (
        METHOD_MAP.get(service_name.boto3_name, {}).get(class_name, {}).get(method_name)
    )