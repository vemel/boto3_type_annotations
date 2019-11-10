# Submodule

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.submodule](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/submodule.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Submodule
    - [write_init_file](#write_init_file)
    - [write_submodule](#write_submodule)
    - [write_submodule_assets](#write_submodule_assets)

## write_init_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/submodule.py#L86)

```python
def write_init_file(
    file_path: Path,
    import_records: Set[ImportRecord],
    service_name: ServiceName,
) -> None:
```

## write_submodule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/submodule.py#L26)

```python
def write_submodule(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
) -> None:
```

## write_submodule_assets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/submodule.py#L59)

```python
def write_submodule_assets(
    service_output_path: Path,
    service_name: ServiceName,
) -> None:
```
