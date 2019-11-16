from pathlib import Path
import shutil
from typing import List
import filecmp

from boto3 import __version__ as boto3_version

from mypy_boto3_builder.structures import Boto3Module
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.writers.utils import render_jinja2_template
from mypy_boto3_builder.constants import BOTO3_STUBS_STATIC_PATH


def write_boto3_stubs_module(
    boto3_module: Boto3Module, output_path: Path
) -> List[Path]:
    package_path = output_path / boto3_module.package_name
    templates_path = Path("boto3-stubs")
    module_templates_path = templates_path / "boto3-stubs"
    modified_paths: List[Path] = []
    file_paths = [
        (output_path / "setup.py", templates_path / "setup.py.jinja2"),
        (output_path / "README.md", templates_path / "README.md.jinja2"),
        (package_path / "py.typed", module_templates_path / "py.typed.jinja2"),
        (package_path / "__init__.pyi", module_templates_path / "__init__.pyi.jinja2"),
        (package_path / "session.pyi", module_templates_path / "session.pyi.jinja2"),
        (package_path / "__init__.py", module_templates_path / "__init__.py.jinja2"),
        (package_path / "version.py", module_templates_path / "version.py.jinja2"),
    ]
    for file_path, template_path in file_paths:
        modified = render_jinja2_template(file_path, template_path, module=boto3_module)
        if modified:
            modified_paths.append(file_path)

    for static_path in BOTO3_STUBS_STATIC_PATH.glob("**/*.pyi"):
        relative_output_path = static_path.relative_to(BOTO3_STUBS_STATIC_PATH)
        file_path = package_path / relative_output_path
        file_path.parent.mkdir(exist_ok=True)
        if file_path.exists() and filecmp.cmp(
            static_path.as_posix(), file_path.as_posix()
        ):
            continue

        shutil.copy(static_path, file_path)
        modified_paths.append(file_path)

    return modified_paths
