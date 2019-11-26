# Processors

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.processors](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/processors.py) module.

Processors for parsing and writing modules.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Processors
    - [process_boto3_stubs](#process_boto3_stubs)
    - [process_master](#process_master)
    - [process_service](#process_service)

## process_boto3_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/processors.py#L28)

```python
def process_boto3_stubs(
    session: Session,
    service_names: Iterable[ServiceName],
    output_path: Path,
) -> Boto3StubsPackage:
```

## process_master

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/processors.py#L42)

```python
def process_master(
    session: Session,
    service_names: Iterable[ServiceName],
    output_path: Path,
) -> MasterPackage:
```

## process_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/processors.py#L56)

```python
def process_service(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
) -> ServicePackage:
```
