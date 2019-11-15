from __future__ import annotations

from abc import abstractmethod
from typing import Set, Any
from functools import total_ordering

from mypy_boto3_builder.import_helpers.import_record import ImportRecord


@total_ordering
class FakeAnnotation:
    def __hash__(self) -> int:
        return hash(self.render())

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, FakeAnnotation):
            raise ValueError(f"Cannot compare FakeAnnotation with {other}")

        return str(self) == str(other)

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, FakeAnnotation):
            raise ValueError(f"Cannot compare FakeAnnotation with {other}")

        return not self == other

    def __gt__(self, other: FakeAnnotation) -> bool:
        return str(self) > str(other)

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

    def is_dict(self) -> bool:  # pylint: disable=no-self-use
        return False

    def is_list(self) -> bool:  # pylint: disable=no-self-use
        return False

    @abstractmethod
    def copy(self) -> FakeAnnotation:
        pass
