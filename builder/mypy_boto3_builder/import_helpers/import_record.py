"""
Helper for Python import strings.
"""
from __future__ import annotations

from typing import Any
from functools import total_ordering

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.constants import MODULE_NAME, TYPE_DEFS_NAME


@total_ordering
class ImportRecord:
    """
    Helper for Python import strings.

    Arguments:
        source -- Source of import.
        name -- Import name.
        alias -- Import local name.
    """

    _is_internal = False
    type_defs_import_string = ImportString(TYPE_DEFS_NAME)
    builtins_import_string = ImportString("builtins")
    third_party_import_strings = (
        ImportString("boto3"),
        ImportString("botocore"),
    )

    def __init__(
        self, source: ImportString, name: str = "", alias: str = "", safe: bool = False
    ) -> None:
        self.source = source
        self.name = name
        self.alias = alias
        self.safe = safe

    def __bool__(self) -> bool:
        return bool(self.source)

    @classmethod
    def empty(cls) -> ImportRecord:
        return cls(ImportString.empty())

    def render(self) -> str:
        if self.name and self.alias:
            return f"from {self.source} import {self.name} as {self.alias}"
        if self.name:
            return f"from {self.source} import {self.name}"
        if self.alias:
            return f"import {self.source} as {self.alias}"
        return f"import {self.source}"

    def __str__(self) -> str:
        return self.render()

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

    def __gt__(self, other: ImportRecord) -> bool:
        if self.source == other.source:
            return self.name > other.name

        if self.safe and not other.safe:
            return True

        if other.safe and not self.safe:
            return False

        if self.is_local() and not other.is_local():
            return True

        if other.is_local() and not self.is_local():
            return False

        if self.is_third_party() and not other.is_third_party():
            return True

        if other.is_third_party() and not self.is_third_party():
            return False

        return self.source > other.source

    def get_local_name(self) -> str:
        """
        Get local import name.
        """
        return self.alias or self.name or self.source.render()

    def is_builtins(self) -> bool:
        """
        Whether import is from Python `builtins` module.
        """
        return self.source.startswith(self.builtins_import_string)

    def is_type_defs(self) -> bool:
        """
        Whether import is from `type_defs` module.
        """
        return self.source.startswith(self.type_defs_import_string)

    def is_third_party(self) -> bool:
        """
        Whether import is from 3rd party module.
        """
        for third_party_import_string in self.third_party_import_strings:
            if self.source.startswith(third_party_import_string):
                return True

        return False

    def is_local(self) -> bool:
        """
        Whether import is from local module.
        """
        if not self.source:
            return False

        if self.source.master_name.startswith(MODULE_NAME):
            return True

        if self.is_type_defs():
            return True

        return False

    def is_internal(self) -> bool:
        """
        Whether import is internal and requires `get_external` call before rendering.
        """
        return self._is_internal

    def get_external(self, _module_name: str) -> ImportRecord:
        """
        Get itself.

        Overriden by `InternalImportRecord`.
        """
        return self
