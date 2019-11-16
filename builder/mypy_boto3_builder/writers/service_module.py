from pathlib import Path
from typing import List

from boto3 import __version__ as boto3_version

from mypy_boto3_builder.structures import ServiceModule
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.writers.utils import render_jinja2_template


def write_service_module(
    service_module: ServiceModule, output_path: Path
) -> List[Path]:
    modified_paths: List[Path] = []
    module_path = output_path / service_module.service_name.module_name
    templates_path = Path("service")
    module_templates_path = templates_path / "service"
    file_paths = [
        (output_path / "setup.py", templates_path / "setup.py.jinja2"),
        (module_path / "__init__.py", module_templates_path / "__init__.py.jinja2"),
        (module_path / "__main__.py", module_templates_path / "__main__.py.jinja2"),
        (module_path / "py.typed", module_templates_path / "py.typed.jinja2"),
        (module_path / "client.py", module_templates_path / "client.py.jinja2"),
    ]
    if service_module.service_resource:
        file_paths.append(
            (
                module_path / "service_resource.py",
                module_templates_path / "service_resource.py.jinja2",
            )
        )
    if service_module.paginators:
        file_paths.append(
            (
                module_path / "paginator.py",
                module_templates_path / "paginator.py.jinja2",
            )
        )
    if service_module.waiters:
        file_paths.append(
            (module_path / "waiter.py", module_templates_path / "waiter.py.jinja2",)
        )
    if service_module.typed_dicts:
        file_paths.append(
            (
                module_path / "type_defs.py",
                module_templates_path / "type_defs.py.jinja2",
            )
        )

    for file_path, template_path in file_paths:
        modified = render_jinja2_template(
            file_path,
            template_path,
            module=service_module,
            service_name=service_module.service_name,
        )
        if modified:
            modified_paths.append(file_path)

    return modified_paths
