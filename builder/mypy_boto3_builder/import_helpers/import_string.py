"""
Wrapper for Python import strings.
"""
from __future__ import annotations

from typing import Any


class ImportString:
    """
    Wrapper for Python import strings.

    Arguments:
        import_string -- Wrapped import string.

    Examples::

        import_string = ImportString('my.name')

        str(import_string)
        'my.name'

        import_string.render()
        'my.name'

        import_string.parts.append('test')
        import_string.render()
        'my.name.test'
    """

    def __init__(self, import_string: str) -> None:
        self.parts = import_string.split(".")

    def __bool__(self) -> bool:
        return bool(self.parts)

    def __str__(self) -> str:
        return self.render()

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Any) -> bool:
        return str(self) == str(other)

    def __gt__(self, other: Any) -> bool:
        return str(self) > str(other)

    def startswith(self, other: ImportString) -> bool:
        """
        Check if import string starts with `other`.

        Examples::

            ImportString('my.name').startswith(ImportString('my'))
            True

            ImportString('my_module.name').startswith(ImportString('my'))
            False

            ImportString('my.name').startswith(ImportString('my.name'))
            True

            ImportString('my.name').startswith(ImportString(''))
            True

        Arguments:
            other -- Other import string.
        """
        for part_index, part in enumerate(other.parts):
            try:
                self_part = self.parts[part_index]
            except IndexError:
                return False

            if self_part != part:
                return False

        return True

    def render(self) -> str:
        """
        Render to string.

        Returns:
            Ready to use import string.
        """
        return ".".join(self.parts)

    @property
    def master_name(self) -> str:
        """
        Get first import string part or `builtins`.
        """
        if not self.parts:
            return "builtins"

        return self.parts[0]
