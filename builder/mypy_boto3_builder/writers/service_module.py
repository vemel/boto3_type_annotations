from pathlib import Path

from mypy_boto3_builder.structures import ServiceModule
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.writers.utils import render_jinja2_template


def write_service_module(service_module: ServiceModule, output_path: Path) -> None:
    module_path = output_path / service_module.service_name.module_name
    render_jinja2_template(
        output_path / "setup.py",
        Path("service") / "setup.py.jinja2",
        service_name=service_module.service_name,
    )
    render_jinja2_template(
        module_path / "__init__.py",
        Path("service") / "service" / f"__init__.py.jinja2",
        module=service_module,
    )
    render_jinja2_template(
        module_path / "__main__.py",
        Path("service") / "service" / f"__main__.py.jinja2",
        module=service_module,
    )
    render_jinja2_template(
        module_path / "py.typed",
        Path("service") / "service" / f"py.typed.jinja2",
        module=service_module,
    )
    render_jinja2_template(
        module_path / "client.py",
        Path("service") / "service" / f"client.py.jinja2",
        module=service_module,
    )
    if service_module.service_resource:
        render_jinja2_template(
            module_path / "service_resource.py",
            Path("service") / "service" / f"service_resource.py.jinja2",
            module=service_module,
        )
    if service_module.paginators:
        render_jinja2_template(
            module_path / "paginator.py",
            Path("service") / "service" / f"paginator.py.jinja2",
            module=service_module,
        )
    if service_module.waiters:
        render_jinja2_template(
            module_path / "waiter.py",
            Path("service") / "service" / f"waiter.py.jinja2",
            module=service_module,
        )
    if service_module.typed_dicts:
        render_jinja2_template(
            module_path / "type_defs.py",
            Path("service") / "service" / f"type_defs.py.jinja2",
            module=service_module,
        )
