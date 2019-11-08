from __future__ import annotations

from typing import Any


class ImportString:
    def __init__(self, import_string: str) -> None:
        self.parts = import_string.split(".")

    def __str__(self) -> str:
        return ".".join(self.parts)

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Any) -> bool:
        return str(self) == str(other)

    def __gt__(self, other: Any) -> bool:
        return str(self) > str(other)

    def startswith(self, other: ImportString) -> bool:
        for part_index, part in enumerate(other.parts):
            try:
                self_part = self.parts[part_index]
            except IndexError:
                return False

            if self_part != part:
                return False

        return True
