# Master

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.master](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/master.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Master
    - [write_master_module](#write_master_module)
    - [write_master_module_service_stub](#write_master_module_service_stub)

## write_master_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/master.py#L15)

```python
def write_master_module(
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> None:
```

## write_master_module_service_stub

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/master.py#L60)

```python
def write_master_module_service_stub(
    output_path: Path,
    service_name: ServiceName,
    service_output_path: Path,
) -> None:
```
