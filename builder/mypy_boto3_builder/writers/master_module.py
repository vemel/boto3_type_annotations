from pathlib import Path
import shutil
import filecmp
from typing import List, Tuple

from mypy_boto3_builder.structures import MasterModule
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.writers.utils import render_jinja2_template
from mypy_boto3_builder.constants import MYPY_BOTO3_STATIC_PATH


def write_master_module(master_module: MasterModule, output_path: Path) -> List[Path]:
    modified_paths: List[Path] = []
    module_path = output_path / master_module.package_name
    templates_path = Path("master")
    file_paths = [
        (output_path / "setup.py", templates_path / "setup.py.jinja2"),
        (output_path / "README.md", templates_path / "README.md.jinja2"),
        (
            module_path / "__init__.py",
            templates_path / "master" / "__init__.py.jinja2",
        ),
        (
            module_path / "__main__.py",
            templates_path / "master" / "__main__.py.jinja2",
        ),
        (module_path / "py.typed", templates_path / "master" / "py.typed.jinja2",),
        (module_path / "version.py", templates_path / "master" / "version.py.jinja2",),
    ]

    for file_path, template_path in file_paths:
        modified = render_jinja2_template(
            file_path, template_path, module=master_module
        )
        if modified:
            modified_paths.append(file_path)

    for service_module in master_module.service_modules:
        service_module_path = module_path / service_module.service_name.import_name
        service_templates_path = templates_path / "master" / "service_module"
        service_file_paths: List[Tuple[Path, Path]] = [
            (
                service_module_path / "__init__.py",
                service_templates_path / "__init__.py.jinja2",
            ),
            (
                service_module_path / "client.py",
                service_templates_path / "client.py.jinja2",
            ),
        ]
        if service_module.service_resource:
            service_file_paths.append(
                (
                    service_module_path / "service_resource.py",
                    service_templates_path / "service_resource.py.jinja2",
                )
            )
        if service_module.waiters:
            service_file_paths.append(
                (
                    service_module_path / "waiter.py",
                    service_templates_path / "waiter.py.jinja2",
                )
            )
        if service_module.paginators:
            service_file_paths.append(
                (
                    service_module_path / "paginator.py",
                    service_templates_path / "paginator.py.jinja2",
                )
            )
        if service_module.typed_dicts:
            service_file_paths.append(
                (
                    service_module_path / "type_defs.py",
                    service_templates_path / "type_defs.py.jinja2",
                )
            )

        for file_path, template_path in service_file_paths:
            modified = render_jinja2_template(
                file_path, template_path, service_name=service_module.service_name
            )
            if modified:
                modified_paths.append(file_path)

    for static_path in MYPY_BOTO3_STATIC_PATH.glob("**/*.pyi"):
        relative_output_path = static_path.relative_to(MYPY_BOTO3_STATIC_PATH)
        file_path = (
            module_path
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
