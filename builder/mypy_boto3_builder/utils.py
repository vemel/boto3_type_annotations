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

        while len(line) > LINE_LENGTH:
            indent = " " * (len(line) - len(line.lstrip()))
            line = line.strip()
            space_index = line.rfind(" ", 0, LINE_LENGTH - len(indent))
            if space_index == -1:
                result.append(f"{indent}{line}")
                break
            result.append(f"{indent}{line[:space_index].rstrip()}")
            line = f"{indent}{line[space_index + 1 :]}"

    return "\n".join(result)


def black_reformat(source_path: Path) -> bool:
    return black.format_file_in_place(
        source_path, fast=False, mode=black.FileMode(), write_back=black.WriteBack.YES,
    )
