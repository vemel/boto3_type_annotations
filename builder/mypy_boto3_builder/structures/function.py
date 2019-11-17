"""
Module-level function.
"""
from dataclasses import dataclass, field
from typing import Set, List

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.structures.argument import Argument


@dataclass
class Function:
    """
    Module-level function.
    """

    name: str
    arguments: List[Argument]
    docstring: str
    return_type: FakeAnnotation
    decorators: List[FakeAnnotation] = field(default_factory=lambda: [])
    body: str = "pass"

    def get_types(self) -> Set[FakeAnnotation]:
        types = self.return_type.get_types()
        for argument in self.arguments:
            types.update(argument.get_types())
        for decorator in self.decorators:
            types.update(decorator.get_types())

        return types
