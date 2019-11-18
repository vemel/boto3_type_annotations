"""
Jinja2 renderer and black formatter.
"""
from pathlib import Path
from typing import Any

from boto3 import __version__ as boto3_version
import jinja2
import black

from mypy_boto3_builder.constants import (
    TEMPLATES_PATH,
    MODULE_NAME,
    PYPI_NAME,
    BOTO3_STUBS_NAME,
)
from mypy_boto3_builder.version import __version__ as version


jinja2_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH.as_posix()),
    undefined=jinja2.StrictUndefined,
)


def blackify(content: str, file_path: Path, fast: bool = True) -> str:
    """
    Format `content` with `black` if `file_path` is `*.py` or `*.pyi`.

    On error writes invalid `content` to `file_path` to check for errors.

    Arguments:
        content -- Python code to format.
        file_path -- Target file path.
        fast -- Whether to skip AST post-check.

    Returns:
        Formatted python code.

    Raises:
        ValueError -- If `content` is not a valid Python code.
    """
    if file_path.suffix not in (".py", ".pyi"):
        return content

    file_mode = black.FileMode(is_pyi=file_path.suffix == ".pyi")
    try:
        content = black.format_file_contents(content, fast=fast, mode=file_mode)
    except black.NothingChanged:
        pass
    except black.InvalidInput as e:
        file_path.write_text(content)
        raise ValueError(f"Cannot parse {file_path}: {e}")

    return content


def render_jinja2_template(template_path: Path, **kwargs: Any) -> str:
    """
    Render Jinja2 template to a string.

    Arguments:
        template_path -- Relative path to template in `TEMPLATES_PATH`
        kwargs -- Format arguments.

    Returns:
        A rendered template.
    """
    template_full_path = TEMPLATES_PATH / template_path
    if not template_full_path.exists():
        raise ValueError(f"Template {template_path} not found")

    template = jinja2_env.get_template(template_path.as_posix())
    return template.render(
        version=version,
        master_pypi_name=PYPI_NAME,
        master_module_name=MODULE_NAME,
        boto3_stubs_name=BOTO3_STUBS_NAME,
        boto3_version=boto3_version,
        **kwargs,
    )
