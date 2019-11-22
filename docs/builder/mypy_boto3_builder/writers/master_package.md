# Master Package

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.master_package](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/master_package.py) module.

Master package writer.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Master Package
    - [get_service_module_file_paths](#get_service_module_file_paths)
    - [write_master_package](#write_master_package)

## get_service_module_file_paths

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/master_package.py#L81)

```python
def get_service_module_file_paths(
    package: ServicePackage,
    package_path: Path,
    templates_path: Path,
) -> List[Tuple[Path, Path]]:
```

## write_master_package

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/master_package.py#L16)

```python
def write_master_package(
    package: MasterPackage,
    output_path: Path,
) -> List[Path]:
```
