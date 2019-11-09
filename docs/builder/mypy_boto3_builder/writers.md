# Writers

> Auto-generated documentation for [builder.mypy_boto3_builder.writers](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Writers
    - [format_arguments](#format_arguments)
    - [format_path](#format_path)
    - [generate_attributes](#generate_attributes)
    - [generate_method](#generate_method)
    - [generate_methods](#generate_methods)
    - [process_service_client](#process_service_client)
    - [process_service_paginator](#process_service_paginator)
    - [process_service_resource](#process_service_resource)
    - [process_service_waiter](#process_service_waiter)
    - [write_asset](#write_asset)
    - [write_client](#write_client)
    - [write_collection](#write_collection)
    - [write_init_file](#write_init_file)
    - [write_master_module](#write_master_module)
    - [write_master_module_service_stub](#write_master_module_service_stub)
    - [write_resource](#write_resource)
    - [write_service_paginator](#write_service_paginator)
    - [write_service_resource](#write_service_resource)
    - [write_service_waiter](#write_service_waiter)
    - [write_submodule](#write_submodule)
    - [write_submodule_assets](#write_submodule_assets)

## format_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L41)

```python
def format_arguments(method: Method) -> Generator[str, None, None]:
```

## format_path

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L413)

```python
def format_path(path: Path) -> None:
```

## generate_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L54)

```python
def generate_attributes(
    attributes: List[Attribute],
) -> Generator[str, None, None]:
```

## generate_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L77)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L59)

```python
def generate_methods(
    methods: List[Method],
    method_body: str = 'pass',
    first_arg: str = 'self',
    decorator: str = None,
    include_doc: bool = False,
) -> Generator[str, None, None]:
```

## process_service_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L280)

```python
def process_service_client(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Client:
```

## process_service_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L353)

```python
def process_service_paginator(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Optional[ServicePaginator]:
```

## process_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L301)

```python
def process_service_resource(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Optional[ServiceResource]:
```

## process_service_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L327)

```python
def process_service_waiter(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Optional[ServiceWaiter]:
```

## write_asset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L528)

```python
def write_asset(file_path: Path, template_name: str, **kwargs: str) -> None:
```

## write_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L255)

```python
def write_client(
    client: Client,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool,
) -> None:
```

## write_collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L149)

```python
def write_collection(
    collection: Collection,
    file_object: IO,
    include_doc: bool = False,
) -> None:
```

## write_init_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L535)

```python
def write_init_file(
    file_path: Path,
    import_records: Set[ImportRecord],
    service_name: ServiceName,
) -> None:
```

## write_master_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L422)

```python
def write_master_module(
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> None:
```

## write_master_module_service_stub

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L467)

```python
def write_master_module_service_stub(
    output_path: Path,
    service_name: ServiceName,
    service_output_path: Path,
) -> None:
```

## write_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L169)

```python
def write_resource(
    resource: Union[Resource, ServiceResource],
    name: str,
    file_object: IO,
    include_doc: bool = False,
) -> None:
```

## write_service_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L227)

```python
def write_service_paginator(
    service_paginator: ServicePaginator,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool,
) -> None:
```

## write_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L112)

```python
def write_service_resource(
    service_resource: ServiceResource,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool,
) -> None:
```

## write_service_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L199)

```python
def write_service_waiter(
    service_waiter: ServiceWaiter,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool = False,
) -> None:
```

## write_submodule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L380)

```python
def write_submodule(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
) -> None:
```

## write_submodule_assets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers.py#L501)

```python
def write_submodule_assets(
    service_output_path: Path,
    service_name: ServiceName,
) -> None:
```
