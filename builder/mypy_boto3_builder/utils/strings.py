"""
Multiple string utils collection.
"""
import re
from typing import Optional, List

from mypy_boto3_builder.constants import LINE_LENGTH

# Regexp to replace single backslashes
RE_BACKSLASH = re.compile(r"\\{1,2}")


def clean_doc(doc: Optional[str]) -> str:
    """
    Clean docstring to be safely rendered.

    - If `doc` is not set, returns an empty docstring.
    - Returns extra empty lines.
    - Escapes backslashes.
    - Replace trible doublequotes with triple single quotes.
    - Tries to fit docstring to `LINE_LENGTH`

    Arguments:
        doc -- Instance docstring.

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

        if len(line) <= LINE_LENGTH:
            result.append(line)
            continue

        while True:
            if len(line) <= LINE_LENGTH:
                result.append(line)
                break

            indent_length = len(line) - len(line.lstrip())
            indent = " " * indent_length
            line = line.strip()
            max_line_length = LINE_LENGTH - indent_length

            space_index = line.rfind(" ", 0, max_line_length + 1)
            if space_index > 0:
                result.append(f"{indent}{line[:space_index].rstrip()}")
                line = f"{indent}{line[space_index + 1 :]}"
                continue

            equals_index = line.rfind("=", 0, max_line_length)
            if equals_index > 0:
                result.append(f"{indent}{line[:equals_index + 1].rstrip()}")
                line = f"{indent}    {line[equals_index + 1 :]}"
                continue

            vertical_bar_index = line.rfind("|", 0, max_line_length + 1)
            if vertical_bar_index > 0:
                result.append(f"{indent}{line[:vertical_bar_index].rstrip()}")
                line = f"{indent}{line[vertical_bar_index :]}"
                continue

            space_index = line.find(" ", max_line_length)
            if space_index != -1:
                result.append(f"{indent}{line[:space_index].rstrip()}")
                line = f"{indent}{line[space_index + 1 :]}"
                continue

            result.append(f"{indent}{line}")
            break

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
