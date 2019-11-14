from pathlib import Path
from typing import Optional, List

import black

from mypy_boto3_builder.constants import LINE_LENGTH


def clean_doc(doc: Optional[str]) -> str:
    if doc is None:
        return ""

    lines = doc.split("\n")
    result: List[str] = []
    for line in lines:
        line = line.rstrip()
        line = line.replace('"""', "'\"'")
        line = line.replace("\\:", ":")
        if not line and result and not result[-1]:
            continue

        if len(line) <= LINE_LENGTH:
            result.append(line)
            continue

        while len(line) > LINE_LENGTH:
            indent = " " * (len(line) - len(line.lstrip()))
            line = line.strip()
            space_index = line.rfind(" ", 0, LINE_LENGTH - len(indent))
            if space_index != -1:
                result.append(f"{indent}{line[:space_index].rstrip()}")
                line = f"{indent}{line[space_index + 1 :]}"
                continue

            equals_index = line.rfind("=", 0, LINE_LENGTH - len(indent))
            if equals_index != -1:
                result.append(f"{indent}{line[:equals_index+1].rstrip()}")
                line = f"{indent}    {line[equals_index + 1 :]}"
                continue

            vertical_bar_index = line.rfind("|", 0, LINE_LENGTH - len(indent))
            if vertical_bar_index != -1:
                result.append(f"{indent}{line[:vertical_bar_index].rstrip()}")
                line = f"{indent}{line[vertical_bar_index :]}"
                continue

            space_index = line.find(" ", LINE_LENGTH - len(indent))
            if space_index != -1:
                result.append(f"{indent}{line[:space_index].rstrip()}")
                line = f"{indent}{line[space_index + 1 :]}"
                continue

            result.append(f"{indent}{line}")
            break
        result.append(line)

    return "\n".join(result)


def black_reformat(source_path: Path) -> bool:
    return black.format_file_in_place(
        source_path, fast=False, mode=black.FileMode(), write_back=black.WriteBack.YES,
    )


def get_class_prefix(func_name: str) -> str:
    return "".join([i.capitalize() for i in func_name.split("_")])
