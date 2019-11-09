from pathlib import Path
from typing import Iterable, Dict, List


from mypy_boto3_builder.writers.utils import write_asset
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.constants import WITH_DOCS_PYPI_POSTFIX, MODULE_NAME, PYPI_NAME


logger = get_logger()


def write_master_module(
    output_path: Path, service_names: Iterable[ServiceName]
) -> None:
    logger.info(f"Writing master module")
    logger.debug(f"Writing assets")

    write_asset(output_path / "py.typed", "py.typed.template")
    write_asset(output_path / "__main__.py", "__main__.py.template")
    write_asset(output_path / "__init__.py", "__init__.py.template")
    write_asset(output_path / "version.py", "version.py.template", version=version)
    write_asset(output_path.parent / "README.md", "master_readme_md.template")

    extras_require: Dict[str, List[str]] = {
        "all": [],
        f"all{WITH_DOCS_PYPI_POSTFIX}": [],
        "essential": [],
        f"essential{WITH_DOCS_PYPI_POSTFIX}": [],
    }
    for service_name in service_names:
        service_install_string = f"{service_name.pypi_name}=={version}"
        extras_require[service_name.extras_name] = [service_install_string]
        if service_name.is_with_docs():
            extras_require[f"all{WITH_DOCS_PYPI_POSTFIX}"].append(
                service_install_string
            )
        else:
            extras_require[f"all"].append(service_install_string)

        if service_name.is_essential():
            if service_name.is_with_docs():
                extras_require[f"essential{WITH_DOCS_PYPI_POSTFIX}"].append(
                    service_install_string
                )
            else:
                extras_require[f"essential"].append(service_install_string)

    write_asset(
        output_path.parent / "setup.py",
        "setup.py.template",
        module_name=MODULE_NAME,
        name=PYPI_NAME,
        extras_require=str(extras_require),
    )


def write_master_module_service_stub(
    output_path: Path, service_name: ServiceName, service_output_path: Path
) -> None:
    master_service_path = output_path / service_name.import_name
    master_service_path.mkdir(exist_ok=True)

    write_asset(
        master_service_path / "__init__.py",
        "master_service_init.template",
        service_module_name=service_name.module_name,
        fallback_service_module_name=service_name.fallback.module_name,
        module_name=MODULE_NAME,
        import_name=service_name.import_name,
        extras_name=service_name.fallback.extras_name,
    )

    submodule_names = ["client", "paginator", "service_resource", "waiter"]
    for submodule_name in submodule_names:
        submodule_path = service_output_path / f"{submodule_name}.py"
        if not submodule_path.exists():
            continue

        write_asset(
            master_service_path / f"{submodule_name}.py",
            "master_service_submodule.template",
            submodule_name=submodule_name,
            service_module_name=service_name.module_name,
            fallback_service_module_name=service_name.fallback.module_name,
            module_name=MODULE_NAME,
            import_name=service_name.import_name,
            extras_name=service_name.fallback.extras_name,
        )
