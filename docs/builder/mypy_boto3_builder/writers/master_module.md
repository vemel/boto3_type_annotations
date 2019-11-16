# Master Module

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.master_module](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/master_module.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Master Module
    - [get_service_module_file_paths](#get_service_module_file_paths)
    - [write_master_module](#write_master_module)

## get_service_module_file_paths

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/master_module.py#L81)

```python
def get_service_module_file_paths(
    service_module: ServiceModule,
    package_path: Path,
    templates_path: Path,
) -> List[Tuple[Path, Path]]:
```

## write_master_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/master_module.py#L12)

```python
def write_master_module(
    master_module: MasterModule,
    output_path: Path,
    reformat: bool,
) -> List[Path]:
```
