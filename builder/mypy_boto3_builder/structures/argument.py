"""
Method or function argument.
"""
from dataclasses import dataclass
from typing import Set, Optional

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


@dataclass
class Argument:
    """
    Method or function argument.

    Attributes:
        name -- Argument name.
        type -- Argument type annotation.
        value -- Default argument value.
        prefix -- Used for starargs.
    """

    name: str
    type: Optional[FakeAnnotation] = None
    default: Optional[FakeAnnotation] = None
    prefix: str = ""

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        if self.type is not None:
            types.update(self.type.get_types())
        if self.default is not None:
            types.update(self.default.get_types())

        return types