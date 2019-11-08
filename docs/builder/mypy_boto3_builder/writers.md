# Writers

> Auto-generated documentation for [builder.mypy_boto3_builder.writers](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Writers
    - [create_module_directory](#create_module_directory)
    - [format_arguments](#format_arguments)
    - [generate_attributes](#generate_attributes)
    - [generate_method](#generate_method)
    - [generate_methods](#generate_methods)
    - [write_client](#write_client)
    - [write_collection](#write_collection)
    - [write_init_file](#write_init_file)
    - [write_resource](#write_resource)
    - [write_service_paginator](#write_service_paginator)
    - [write_service_resource](#write_service_resource)
    - [write_service_waiter](#write_service_waiter)
    - [write_services](#write_services)

## create_module_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L36)

```python
def create_module_directory(module_path: Path) -> None:
```

## format_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L43)

```python
def format_arguments(method: Method) -> Generator[str, None, None]:
```

## generate_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L56)

```python
def generate_attributes(
    attributes: List[Attribute],
) -> Generator[str, None, None]:
```

## generate_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L79)

```python
def generate_method(
    method: Method,
    method_body: str = 'pass',
    first_arg: str = 'self',
    decorator: str = None,
    include_doc: bool = False,
) -> Generator[str, None, None]:
```

## generate_methods

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L61)

```python
def generate_methods(
    methods: List[Method],
    method_body: str = 'pass',
    first_arg: str = 'self',
    decorator: str = None,
    include_doc: bool = False,
) -> Generator[str, None, None]:
```

## write_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L239)

```python
def write_client(
    client: Client,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    with_docs: bool,
) -> None:
```

## write_collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L156)

```python
def write_collection(
    collection: Collection,
    file_object: IO,
    with_docs: bool = False,
) -> None:
```

## write_init_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L356)

```python
def write_init_file(
    file_path: Path,
    import_records: Set[ImportRecord],
    service_name: ServiceName,
) -> None:
```

## write_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L170)

```python
def write_resource(
    resource: Union[Resource, ServiceResource],
    name: str,
    file_object: IO,
    with_docs: bool = False,
) -> None:
```

## write_service_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L215)

```python
def write_service_paginator(
    service_paginator: ServicePaginator,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    with_docs: bool,
) -> None:
```

## write_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L114)

```python
def write_service_resource(
    service_resource: ServiceResource,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    with_docs: bool,
) -> None:
```

## write_service_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L193)

```python
def write_service_waiter(
    service_waiter: ServiceWaiter,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    with_docs: bool = False,
) -> None:
```

## write_services

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L259)

```python
def write_services(
    session: Session,
    service_names: Iterable[ServiceName],
    output_path: Path,
    module_name: str,
    with_docs: bool,
) -> None:
```
