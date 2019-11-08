from pathlib import Path
from typing import Union, Optional, List

import black

from mypy_boto3_builder.structures import TypeAnnotation


def render_type_annotation(
    type_annotation: TypeAnnotation, render_args: bool = False
) -> str:
    name = str(type_annotation)
    if hasattr(type_annotation, "_name"):
        name = getattr(type_annotation, "_name") or "Union"
    if getattr(type_annotation, "__name__", None):
        name = getattr(type_annotation, "__name__")
    if type_annotation == Union:
        name = "Union"
    if type_annotation == Optional:
        name = "Optional"
    if type_annotation == Ellipsis:
        name = "..."
    if name == "NoneType":
        name = "None"

    if str(type_annotation).startswith("~"):
        name = "Any"

    args_rendered = []
    if render_args and hasattr(type_annotation, "__args__"):
        for arg in getattr(type_annotation, "__args__"):
            args_rendered.append(render_type_annotation(arg, render_args=True))
        return f'{name}[{", ".join(args_rendered)}]'

    return name


def clean_doc(doc: str) -> str:
    lines = doc.split("\n")
    result: List[str] = []
    for line in lines:
        line = line.rstrip()
        line = line.replace('"""', "'\"'")
        if not line and result and not result[-1]:
            continue
        result.append(line)
    return "\n".join(result)


def render_template(template_name: str, **kwargs: str) -> str:
    template_path = Path(__file__).parent / "assets" / template_name
    return template_path.read_text().format(**kwargs)


def black_reformat(source_path: Path) -> bool:
    return black.format_file_in_place(
        source_path, fast=False, mode=black.FileMode(), write_back=black.WriteBack.YES,
    )
