from __future__ import annotations

import enum
from typing import List


class ImportRecordType(enum.Enum):
    builtins = "builtins"
    magic = "magic"
    python = "python"
    boto = "boto"
    local = "local"

    @classmethod
    def items(cls) -> List[ImportRecordType]:
        return [
            cls.magic,
            cls.python,
            cls.boto,
            cls.local,
        ]

    def get_comment(self) -> str:
        if self == self.local:
            return "pylint: disable=import-self"

        return ""
