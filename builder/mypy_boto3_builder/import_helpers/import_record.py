from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from mypy_boto3_builder.import_helpers.import_string import ImportString


@dataclass
class ImportRecord:
    def __init__(self, source: str, name: str = "", alias: str = "") -> None:
        self.source = ImportString(source)
        self.name = name
        self.alias = alias

    def __str__(self) -> str:
        if self.name and self.alias:
            return f"from {self.source} import {self.name} as {self.alias}"
        if self.name:
            return f"from {self.source} import {self.name}"
        if self.alias:
            return f"import {self.source} as {self.alias}"
        return f"import {self.source}"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ImportRecord):
            raise ValueError(f"Cannot compare ImportString with {other}")

        return str(self) == str(other)

    def __gt__(self, other: ImportRecord) -> bool:
        if self.source == other.source:
            return self.name > other.name

        return self.source > other.source

    def render(self) -> str:
        return str(self)

    def get_local_name(self) -> str:
        return self.alias or self.name or self.source.render()
