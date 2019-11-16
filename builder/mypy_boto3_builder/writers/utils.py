from pathlib import Path
from typing import Any

from boto3 import __version__ as boto3_version
import jinja2
import black

from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.constants import (
    TEMPLATES_PATH,
    MODULE_NAME,
    PYPI_NAME,
    BOTO3_STUBS_NAME,
)
from mypy_boto3_builder.version import __version__ as version


logger = get_logger()
jinja2_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH.as_posix()),
    undefined=jinja2.StrictUndefined,
)


def format_path(path: Path) -> None:
    logger.debug(f"Applying black formatting to {NicePath(path)}")
    for source_path in path.glob("**/*.py"):
        logger.debug(f"Reformatting {NicePath(source_path)}")
        result = black.format_file_in_place(
            source_path,
            fast=False,
            mode=black.FileMode(),
            write_back=black.WriteBack.YES,
        )
        if result:
            logger.debug(f"Reformatted {NicePath(source_path)}")


def render_jinja2_template(
    output_path: Path, template_path: Path, **kwargs: Any
) -> bool:
    """
    Render Jinja2 template to a file.

    If file content is the same - file is not overwritten.

    Returns:
        True if file was updated.
    """
    template_full_path = TEMPLATES_PATH / template_path
    logger.debug(f"Rendering {template_path} to {NicePath(output_path)}")
    if not template_full_path.exists():
        raise ValueError(f"Template {template_path} not found")

    output_path.parent.parent.mkdir(exist_ok=True)
    output_path.parent.mkdir(exist_ok=True)
    template = jinja2_env.get_template(template_path.as_posix())
    new_content = template.render(
        version=version,
        master_pypi_name=PYPI_NAME,
        master_module_name=MODULE_NAME,
        boto3_stubs_name=BOTO3_STUBS_NAME,
        boto3_version=boto3_version,
        **kwargs,
    )
    if output_path.exists():
        old_content = output_path.read_text()
        print(output_path, old_content == new_content)
        if old_content == new_content:
            return False

    output_path.write_text(new_content)
    return True
