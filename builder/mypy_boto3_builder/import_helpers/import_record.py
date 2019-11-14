from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from functools import total_ordering

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.constants import MODULE_NAME, TYPE_DEFS_NAME


@dataclass
@total_ordering
class ImportRecord:
    type_defs_import_string = ImportString(TYPE_DEFS_NAME)
    builtins_import_string = ImportString("builtins")
    third_party_import_strings = (
        ImportString("boto3"),
        ImportString("botocore"),
    )

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

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, ImportRecord):
            raise ValueError(f"Cannot compare ImportString with {other}")

        return not self == other

    @property
    def package_name(self) -> str:
        if not self.source:
            return "builtins"

        return self.source.parts[0]

    def __gt__(self, other: ImportRecord) -> bool:
        if self.source == other.source:
            return self.name > other.name

        if self.is_local() and not other.is_local():
            return True

        if other.is_local() and not self.is_local():
            return False

        if self.is_third_party() and not other.is_third_party():
            return True

        if other.is_third_party() and not self.is_third_party():
            return False

        return self.source > other.source

    def render(self) -> str:
        return str(self)

    def get_local_name(self) -> str:
        return self.alias or self.name or self.source.render()

    def is_builtins(self) -> bool:
        return self.source.startswith(self.builtins_import_string)

    def is_type_defs(self) -> bool:
        return self.source.startswith(self.type_defs_import_string)

    def is_third_party(self) -> bool:
        for third_party_import_string in self.third_party_import_strings:
            if self.source.startswith(third_party_import_string):
                return True

        return False

    def is_local(self) -> bool:
        if not self.source:
            return False

        if self.package_name.startswith(MODULE_NAME):
            return True

        if self.is_type_defs():
            return True

        return False
