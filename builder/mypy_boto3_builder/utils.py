import re
from typing import Union, Optional, List

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
    parameters: List[str] = []
    preamble = []
    indices_to_remove = []
    parameter_regex = re.compile("^:(.*[a-zA-Z]):")
    lines = doc.split("\n")
    for i, line in enumerate(lines):
        if parameter_regex.search(line.strip()):
            parameters.append(line.replace("'", "\\'").replace('"', '\\"').rstrip())
            indices_to_remove.append(i)
            n = i + 1
            while (
                n < len(lines)
                and not parameter_regex.search(lines[n].strip())
                and line.strip() != ":returns:"
            ):
                if lines[n].strip():
                    parameters.append(
                        lines[n].replace("'", "\\'").replace('"', '\\"').rstrip()
                    )
                    indices_to_remove.append(n)
                n += 1
    for i in reversed(indices_to_remove):
        del lines[i]
    for i, line in enumerate(lines):
        line = line.strip()
        if line == "::" or (line.startswith("**") and line.endswith("**")):
            lines[i] = line
    for line in lines:
        if line.strip():
            if line.strip().startswith("**") and line.strip().endswith("**"):
                preamble.append("")
            preamble.append(line)
    return "\n".join(preamble + parameters)
