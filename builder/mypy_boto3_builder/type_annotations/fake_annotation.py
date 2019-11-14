from __future__ import annotations

from abc import abstractmethod
from typing import Set

from mypy_boto3_builder.import_helpers.import_record import ImportRecord


class FakeAnnotation:
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

    def remove_children(self) -> None:
        pass

    def add_child(self, child: FakeAnnotation) -> None:
        pass

    def is_dict(self) -> bool:
        return False

    def is_list(self) -> bool:
        return False

    @abstractmethod
    def copy(self) -> FakeAnnotation:
        pass
