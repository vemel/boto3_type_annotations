from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_def import TypeDef


__all__ = ("DOCLESS_METHOD_ARGUMENT_MAP",)


DOCLESS_METHOD_ARGUMENT_MAP = {
    "ServiceResource.create_tags": [
        Argument("self", None),
        Argument("Resources", TypeSubscript(Type.List, [Type.Any]),),
        Argument("Tags", TypeSubscript(Type.List, [TypeDef("EC2Tag")]),),
        Argument("DryRun", Type.bool, TypeConstant(False)),
    ]
}
