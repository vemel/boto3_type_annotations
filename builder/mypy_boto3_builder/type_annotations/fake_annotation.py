from __future__ import annotations

from abc import abstractmethod
from typing import Set

from mypy_boto3_builder.import_helpers.import_record import ImportRecord


class FakeAnnotation:
    is_internal = False

    def __hash__(self) -> int:
        return hash(self.render())

    def __str__(self) -> str:
        return self.render()

    @abstractmethod
    def render(self) -> str:
        pass

    @abstractmethod
    def get_import_record(self) -> ImportRecord:
        pass

    def get_types(self) -> Set[FakeAnnotation]:
        return {self}
