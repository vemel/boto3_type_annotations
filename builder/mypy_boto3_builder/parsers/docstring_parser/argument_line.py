from __future__ import annotations

from typing import Iterable, List, Any


class ArgumentLine:
    def __init__(
        self,
        name: str = "",
        type_name: str = "",
        line: Iterable[str] = tuple(),
        description: str = "",
        indented: Iterable[Any] = tuple(),
    ) -> None:
        self.line = "".join(line)
        self.name = name
        self.type_name = type_name
        self.description = description
        self._indented = indented

    @property
    def indented(self) -> List[ArgumentLine]:
        result: List[ArgumentLine] = []
        for line in self._indented:
            result.append(ArgumentLine(**line))
        return result

    @property
    def required(self) -> bool:
        return "REQUIRED" in self.description or "**must**" in self.description

    def render(self) -> str:
        result: List[str] = []
        indent = "  " if self.line else ""
        if self.line:
            result.append(self.line)
            result.append("")
        for indented_line in self.indented:
            result.append(f"{indent}{indented_line.render()}")
        return "\n".join(result)
