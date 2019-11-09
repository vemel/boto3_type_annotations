from pathlib import Path
from typing import Iterable, List, Tuple

from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.constants import MODULE_NAME, PYPI_NAME
from mypy_boto3_builder.writers.utils import write_asset, render_jinja2_template
from mypy_boto3_builder.writers.enums import ServiceSubmodule


logger = get_logger()


def write_boto3_stubs_module(output_path: Path) -> None:
    logger.info(f"Writing boto3-stubs module")
    logger.debug(f"Writing assets")

    write_asset(output_path / "py.typed", "partial.py.typed.template")
    write_asset(output_path / "__init__.py", "__init__.py.template")
    write_asset(output_path / "__main__.py", "__main__.py.template")
    write_asset(output_path / "version.py", "version.py.template", version=version)
    write_asset(output_path.parent / "README.md", "master_readme_md.template")

    write_asset(
        output_path.parent / "setup.py",
        "boto3_stubs_setup.py.template",
        master_pypi_name=PYPI_NAME,
        name="boto3-stubs",
        package_name="boto3_stubs",
        version=version,
    )


def write_boto3_stubs_files(
    output_path: Path, service_names: Iterable[ServiceName]
) -> None:
    render_items = get_render_items(output_path.parent.parent, service_names)
    render_jinja2_template(
        output_path / "__init__.pyi",
        Path("boto3_stubs") / "__init__.pyi.jinja2",
        items=render_items,
        module_name=MODULE_NAME,
        service_submodules=ServiceSubmodule.get_imported(),
        service_names=service_names,
    )
    render_jinja2_template(
        output_path / "session.pyi",
        Path("boto3_stubs") / "session.pyi.jinja2",
        items=render_items,
        module_name=MODULE_NAME,
        service_submodules=ServiceSubmodule.get_imported(),
        service_names=service_names,
    )


def get_render_items(
    root_output_path: Path, service_names: Iterable[ServiceName]
) -> List[Tuple[ServiceSubmodule, ServiceName]]:
    items: List[Tuple[ServiceSubmodule, ServiceName]] = []

    for service_submodule in ServiceSubmodule.get_imported():
        for service_name in service_names:
            if service_name.is_with_docs():
                continue

            service_output_path = (
                root_output_path
                / f"{service_name.module_name}_package"
                / service_name.module_name
            )

            if not (service_output_path / service_submodule.file_name).exists():
                continue

            items.append((service_submodule, service_name))
    return items
