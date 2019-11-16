from pathlib import Path
from typing import List

from mypy_boto3_builder.structures import ServiceModule
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.writers.utils import (
    render_jinja2_template,
    blackify_str,
)


def write_service_module(
    service_module: ServiceModule, output_path: Path, reformat: bool
) -> List[Path]:
    modified_paths: List[Path] = []
    package_path = output_path / service_module.service_name.module_name

    output_path.mkdir(exist_ok=True)
    package_path.mkdir(exist_ok=True)

    templates_path = Path("service")
    module_templates_path = templates_path / "service"
    file_paths = [
        (output_path / "setup.py", templates_path / "setup.py.jinja2"),
        (output_path / "README.md", templates_path / "README.md.jinja2"),
        (package_path / "version.py", module_templates_path / "version.py.jinja2"),
        (package_path / "__init__.py", module_templates_path / "__init__.py.jinja2"),
        (package_path / "__main__.py", module_templates_path / "__main__.py.jinja2"),
        (package_path / "py.typed", module_templates_path / "py.typed.jinja2"),
        (package_path / "client.py", module_templates_path / "client.py.jinja2"),
    ]
    if service_module.service_resource:
        file_paths.append(
            (
                package_path / "service_resource.py",
                module_templates_path / "service_resource.py.jinja2",
            )
        )
    if service_module.paginators:
        file_paths.append(
            (
                package_path / "paginator.py",
                module_templates_path / "paginator.py.jinja2",
            )
        )
    if service_module.waiters:
        file_paths.append(
            (package_path / "waiter.py", module_templates_path / "waiter.py.jinja2",)
        )
    if service_module.typed_dicts:
        file_paths.append(
            (
                package_path / "type_defs.py",
                module_templates_path / "type_defs.py.jinja2",
            )
        )

    for file_path, template_path in file_paths:
        content = render_jinja2_template(
            template_path,
            module=service_module,
            service_name=service_module.service_name,
        )
        if reformat and file_path.suffix == ".py":
            content = blackify_str(content)

        if not file_path.exists() or file_path.read_text() != content:
            modified_paths.append(file_path)
            file_path.write_text(content)

    return modified_paths
