"""
Multiple string utils collection.
"""
import re
import textwrap
from typing import Optional, List, Iterator

# Regexp to replace single backslashes
RE_BACKSLASH = re.compile(r"\\{1,2}")


def wrap_line(line: str, max_length: int) -> Iterator[str]:
    """
    Wrap text line to fit `max_length`.

    Arguments:
        line -- Text to wrap.
        max_length -- Result line max length.

    Yields:
        A string of wrapped text.
    """
    indent_length = len(line) - len(line.lstrip())
    indent = " " * indent_length
    max_line_length = max_length - indent_length
    for sub_line in textwrap.wrap(
        line.strip(), max_line_length, break_long_words=False, break_on_hyphens=False
    ):
        indented_sub_line = f"{indent}{sub_line}"
        if len(indented_sub_line) > max_line_length:
            yield from wrap_code_line(indented_sub_line, max_line_length)
            continue
        yield indented_sub_line


def wrap_code_line(line: str, max_length: int) -> Iterator[str]:
    """
    Wrap source code line to fit `max_length`.

    Arguments:
        line -- Source code text to wrap.
        max_length -- Result line max length.

    Yields:
        A string of wrapped text.
    """
    while len(line) > max_length:
        indent_length = len(line) - len(line.lstrip())
        indent = " " * indent_length

        equals_index = line.rfind("=", 0, max_length)
        if equals_index > 0:
            yield line[: equals_index + 1].rstrip()
            line = f"{indent}    {line[equals_index + 1 :]}"
            continue

        vertical_bar_index = line.rfind("|", indent_length + 1, max_length + 1)
        if vertical_bar_index > 0:
            yield line[:vertical_bar_index].rstrip()
            line = f"{indent}{line[vertical_bar_index :]}"
            continue

        vertical_bar_index = line.rfind("|", indent_length + 1)
        if vertical_bar_index > 0:
            yield line[:vertical_bar_index].rstrip()
            line = f"{indent}{line[vertical_bar_index :]}"
            continue

        yield line
        return

    yield line


def clean_doc(doc: Optional[str], max_length: int) -> str:
    """
    Clean docstring to be safely rendered.

    - If `doc` is not set, returns an empty docstring.
    - Returns extra empty lines.
    - Escapes backslashes.
    - Replace trible doublequotes with triple single quotes.
    - Tries to fit docstring to `max_length`

    Arguments:
        doc -- Instance docstring.
        max_length -- Result line max length.

    Returns:
        Cleaned docstring.
    """
    if doc is None:
        return ""

    lines = doc.split("\n")
    result: List[str] = []
    for line in lines:
        line = line.rstrip()
        line = RE_BACKSLASH.sub(r"\\\\", line)
        line = line.replace('"""', "'''")
        if not line and result and not result[-1]:
            continue

        if len(line) <= max_length:
            result.append(line)
            continue

        if " " in line.strip():
            for sub_line in wrap_line(line, max_length):
                result.append(sub_line)
            continue

        for sub_line in wrap_code_line(line, max_length):
            result.append(sub_line)

    return "\n".join(result)


def get_class_prefix(func_name: str) -> str:
    """
    Get a valid Python class prefix from `func_name`.

    Arguments:
        func_name -- Any string.

    Returns:
        String with a class prefix.
    """
    parts = [f"{i[:1].upper()}{i[1:]}" for i in func_name.split("_") if i]
    return "".join(parts)
