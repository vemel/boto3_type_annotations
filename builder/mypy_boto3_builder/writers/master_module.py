"""
Master module writer.
"""
from pathlib import Path
import shutil
import filecmp
from typing import List, Tuple

from mypy_boto3_builder.structures.master_module import MasterModule
from mypy_boto3_builder.structures.service_module import ServiceModule
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.writers.utils import render_jinja2_template, blackify
from mypy_boto3_builder.constants import MYPY_BOTO3_STATIC_PATH


def write_master_module(master_module: MasterModule, output_path: Path) -> List[Path]:
    modified_paths: List[Path] = []
    package_path = output_path / master_module.package_name

    output_path.mkdir(exist_ok=True)
    package_path.mkdir(exist_ok=True)

    templates_path = Path("master")
    file_paths = [
        (output_path / "setup.py", templates_path / "setup.py.jinja2"),
        (output_path / "README.md", templates_path / "README.md.jinja2"),
        (
            package_path / "__init__.py",
            templates_path / "master" / "__init__.py.jinja2",
        ),
        (
            package_path / "__main__.py",
            templates_path / "master" / "__main__.py.jinja2",
        ),
        (package_path / "py.typed", templates_path / "master" / "py.typed.jinja2",),
        (package_path / "version.py", templates_path / "master" / "version.py.jinja2",),
    ]

    for file_path, template_path in file_paths:
        content = render_jinja2_template(template_path, module=master_module)
        content = blackify(content, file_path)

        if not file_path.exists() or file_path.read_text() != content:
            modified_paths.append(file_path)
            file_path.write_text(content)

    for service_module in master_module.service_modules:
        service_module_file_paths = get_service_module_file_paths(
            service_module, package_path, templates_path
        )

        for file_path, template_path in service_module_file_paths:
            content = render_jinja2_template(
                template_path, service_name=service_module.service_name
            )
            content = blackify(content, file_path)

            if not file_path.exists() or file_path.read_text() != content:
                modified_paths.append(file_path)
                file_path.write_text(content)

    for static_path in MYPY_BOTO3_STATIC_PATH.glob("**/*.py"):
        relative_output_path = static_path.relative_to(MYPY_BOTO3_STATIC_PATH)
        file_path = (
            package_path
            / relative_output_path.parent
            / f"{relative_output_path.stem}.py"
        )
        file_path.parent.mkdir(exist_ok=True)
        if file_path.exists() and filecmp.cmp(
            static_path.as_posix(), file_path.as_posix()
        ):
            continue

        shutil.copy(static_path, file_path)
        modified_paths.append(file_path)

    return modified_paths


def get_service_module_file_paths(
    service_module: ServiceModule, package_path: Path, templates_path: Path,
) -> List[Tuple[Path, Path]]:
    service_module_path = package_path / service_module.service_name.import_name
    service_module_path.mkdir(exist_ok=True)
    service_templates_path = templates_path / "master" / "service_module"

    file_paths: List[Tuple[Path, Path]] = [
        (
            service_module_path / "__init__.py",
            service_templates_path / "__init__.py.jinja2",
        ),
        (
            service_module_path / "client.py",
            service_templates_path / "client.py.jinja2",
        ),
        (
            service_module_path / "helpers.py",
            service_templates_path / "helpers.py.jinja2",
        ),
    ]
    if service_module.service_resource:
        file_paths.append(
            (
                service_module_path / "service_resource.py",
                service_templates_path / "service_resource.py.jinja2",
            )
        )
    if service_module.waiters:
        file_paths.append(
            (
                service_module_path / "waiter.py",
                service_templates_path / "waiter.py.jinja2",
            )
        )
    if service_module.paginators:
        file_paths.append(
            (
                service_module_path / "paginator.py",
                service_templates_path / "paginator.py.jinja2",
            )
        )
    if service_module.typed_dicts:
        file_paths.append(
            (
                service_module_path / "type_defs.py",
                service_templates_path / "type_defs.py.jinja2",
            )
        )
    return file_paths
