from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.typed_dicts import ec2_tag_type


__all__ = ("DOCLESS_METHOD_ARGUMENT_MAP",)


DOCLESS_METHOD_ARGUMENT_MAP = {
    "ServiceResource.create_tags": [
        Argument("self", None),
        Argument("Resources", TypeSubscript(Type.List, [Type.Any]),),
        Argument("Tags", TypeSubscript(Type.List, [ec2_tag_type]),),
        Argument("DryRun", Type.bool, TypeConstant(False)),
    ]
}
