# Line Generators

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.line_generators](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/line_generators.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Line Generators
    - [write_client](#write_client)
    - [write_collection](#write_collection)
    - [write_resource](#write_resource)
    - [write_service_paginator](#write_service_paginator)
    - [write_service_resource](#write_service_resource)
    - [write_service_waiter](#write_service_waiter)

## write_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/line_generators.py#L166)

```python
def write_client(
    client: Client,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool,
) -> None:
```

## write_collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/line_generators.py#L60)

```python
def write_collection(
    collection: Collection,
    file_object: IO,
    include_doc: bool = False,
) -> None:
```

## write_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/line_generators.py#L78)

```python
def write_resource(
    resource: Union[Resource, ServiceResource],
    name: str,
    file_object: IO,
    include_doc: bool = False,
) -> None:
```

## write_service_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/line_generators.py#L137)

```python
def write_service_paginator(
    service_paginator: ServicePaginator,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool,
) -> None:
```

## write_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/line_generators.py#L23)

```python
def write_service_resource(
    service_resource: ServiceResource,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool,
) -> None:
```

## write_service_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/line_generators.py#L109)

```python
def write_service_waiter(
    service_waiter: ServiceWaiter,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool = False,
) -> None:
```
