from pathlib import Path
import shutil

from boto3 import __version__ as boto3_version

from mypy_boto3_builder.structures import MasterModule
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.writers.utils import render_jinja2_template
from mypy_boto3_builder.constants import TEMPLATES_PATH, MYPY_BOTO3_STATIC_PATH


def write_master_module(master_module: MasterModule, output_path: Path) -> None:
    module_path = output_path / master_module.package_name
    render_jinja2_template(
        output_path / "setup.py",
        Path("master") / "setup.py.jinja2",
        module=master_module,
        boto3_version=boto3_version,
    )
    shutil.copy(
        TEMPLATES_PATH / "master" / "README.md.jinja2", output_path / "README.md"
    )
    for file_name in [
        "__init__.py",
        "__main__.py",
        "py.typed",
        "version.py",
    ]:
        render_jinja2_template(
            module_path / file_name,
            Path("master") / "master" / f"{file_name}.jinja2",
            module=master_module,
        )
    for service_module in master_module.service_modules:
        service_module_path = module_path / service_module.service_name.import_name
        render_jinja2_template(
            service_module_path / "__init__.py",
            Path("master") / "master" / "service_module" / f"__init__.py.jinja2",
            service_name=service_module.service_name,
        )
        render_jinja2_template(
            service_module_path / "client.py",
            Path("master") / "master" / "service_module" / f"client.py.jinja2",
            service_name=service_module.service_name,
        )
        render_jinja2_template(
            service_module_path / "type_defs.py",
            Path("master") / "master" / "service_module" / f"type_defs.py.jinja2",
            service_name=service_module.service_name,
        )
        if service_module.service_resource:
            render_jinja2_template(
                service_module_path / "service_resource.py",
                Path("master")
                / "master"
                / "service_module"
                / f"service_resource.py.jinja2",
                service_name=service_module.service_name,
            )
        if service_module.waiters:
            render_jinja2_template(
                service_module_path / "waiter.py",
                Path("master") / "master" / "service_module" / f"waiter.py.jinja2",
                service_name=service_module.service_name,
            )
        if service_module.paginators:
            render_jinja2_template(
                service_module_path / "paginator.py",
                Path("master") / "master" / "service_module" / f"paginator.py.jinja2",
                service_name=service_module.service_name,
            )

    for static_path in MYPY_BOTO3_STATIC_PATH.glob("**/*.pyi"):
        relative_output_path = static_path.relative_to(MYPY_BOTO3_STATIC_PATH)
        output_path = (
            module_path
            / relative_output_path.parent
            / f"{relative_output_path.stem}.py"
        )
        output_path.parent.mkdir(exist_ok=True)
        shutil.copy(static_path, output_path)
