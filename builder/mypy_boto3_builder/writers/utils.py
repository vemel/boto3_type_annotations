from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

from mypy_boto3_builder.nice_path import NicePath
from mypy_boto3_builder.utils import black_reformat
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.constants import TEMPLATES_PATH, ASSETS_PATH


logger = get_logger()


def write_asset(output_path: Path, template_path: Path, **kwargs: str) -> None:
    template_path = ASSETS_PATH / template_path
    logger.debug(f"Rendering {NicePath(template_path)} to {NicePath(output_path)}")
    output_path.write_text(template_path.read_text().format(**kwargs))


def format_path(path: Path) -> None:
    logger.debug(f"Applying black formatting to {NicePath(path)}")
    for source_path in path.glob("**/*.py"):
        logger.debug(f"Reformatting {NicePath(source_path)}")
        result = black_reformat(source_path)
        if result:
            logger.debug(f"Reformatted {NicePath(source_path)}")


def render_jinja2_template(
    output_path: Path, template_path: Path, **kwargs: Any
) -> None:
    env = Environment(loader=FileSystemLoader(TEMPLATES_PATH.as_posix()))
    template = env.get_template(template_path.as_posix())
    logger.debug(
        f"Rendering {NicePath(TEMPLATES_PATH / template_path)} to {NicePath(output_path)}"
    )
    output_path.write_text(template.render(**kwargs))
