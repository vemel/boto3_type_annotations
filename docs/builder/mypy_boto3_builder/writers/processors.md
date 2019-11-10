# Processors

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.processors](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/processors.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Processors
    - [process_service_client](#process_service_client)
    - [process_service_paginator](#process_service_paginator)
    - [process_service_resource](#process_service_resource)
    - [process_service_waiter](#process_service_waiter)

## process_service_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/processors.py#L36)

```python
def process_service_client(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Client:
```

## process_service_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/processors.py#L109)

```python
def process_service_paginator(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Optional[ServicePaginator]:
```

## process_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/processors.py#L57)

```python
def process_service_resource(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Optional[ServiceResource]:
```

## process_service_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/processors.py#L83)

```python
def process_service_waiter(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Optional[ServiceWaiter]:
```
