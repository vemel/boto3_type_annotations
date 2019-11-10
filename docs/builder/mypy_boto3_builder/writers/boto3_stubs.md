# Boto3 Stubs

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.boto3_stubs](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/boto3_stubs.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Boto3 Stubs
    - [get_render_items](#get_render_items)
    - [write_boto3_stubs_files](#write_boto3_stubs_files)
    - [write_boto3_stubs_module](#write_boto3_stubs_module)

## get_render_items

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/boto3_stubs.py#L57)

```python
def get_render_items(
    root_output_path: Path,
    service_names: Iterable[ServiceName],
) -> List[Tuple[ServiceSubmodule, ServiceName]]:
```

## write_boto3_stubs_files

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/boto3_stubs.py#L35)

```python
def write_boto3_stubs_files(
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> None:
```

## write_boto3_stubs_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/boto3_stubs.py#L15)

```python
def write_boto3_stubs_module(output_path: Path) -> None:
```
