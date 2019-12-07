"""
String to type annotation map that find type annotation by method and argument name.
"""
from typing import Dict, Optional

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_maps.typed_dicts import s3_copy_source_type, ec2_tag_type


OPERATION_TYPE_MAP: Dict[str, Dict[str, FakeAnnotation]] = {
    "UploadPartCopyRequest": {
        "CopySource": TypeSubscript(Type.Union, [Type.str, s3_copy_source_type])
    },
    "CopyObjectRequest": {
        "CopySource": TypeSubscript(Type.Union, [Type.str, s3_copy_source_type])
    },
    "CreateTagsRequest": {"Tags": TypeSubscript(Type.List, [ec2_tag_type])},
    "DeleteTagsRequest": {"Tags": TypeSubscript(Type.List, [ec2_tag_type])},
}


def get_argument_type_stub(
    operation_name: str, argument_name: str
) -> Optional[FakeAnnotation]:
    return OPERATION_TYPE_MAP.get(operation_name, {}).get(argument_name)
