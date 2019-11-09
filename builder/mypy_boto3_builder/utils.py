from pathlib import Path
from typing import Optional, List

import black


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
        result.append(line)
    return "\n".join(result)


def black_reformat(source_path: Path) -> bool:
    return black.format_file_in_place(
        source_path, fast=False, mode=black.FileMode(), write_back=black.WriteBack.YES,
    )
