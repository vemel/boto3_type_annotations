# Parsers

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Parsers
    - [get_resource_public_actions](#get_resource_public_actions)
    - [manually_set_method](#manually_set_method)
    - [parse_arguments](#parse_arguments)
    - [parse_attributes](#parse_attributes)
    - [parse_client](#parse_client)
    - [parse_collections](#parse_collections)
    - [parse_identifiers](#parse_identifiers)
    - [parse_methods](#parse_methods)
    - [parse_paginators](#parse_paginators)
    - [parse_resource](#parse_resource)
    - [parse_return_type](#parse_return_type)
    - [parse_service_paginator](#parse_service_paginator)
    - [parse_service_resource](#parse_service_resource)
    - [parse_service_waiter](#parse_service_waiter)
    - [parse_type_from_str](#parse_type_from_str)
    - [parse_waiters](#parse_waiters)
    - [retrieve_sub_resources](#retrieve_sub_resources)

## get_resource_public_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L43)

```python
def get_resource_public_actions(resource_class: Resource) -> Dict[str, Any]:
```

## manually_set_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L54)

```python
def manually_set_method(name: str) -> Method:
```

## parse_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L71)

```python
def parse_arguments(parsed_doc: Docstring) -> Generator[Argument, None, None]:
```

## parse_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L84)

```python
def parse_attributes(
    resource: Boto3ServiceResource,
) -> Generator[Attribute, None, None]:
```

## parse_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L95)

```python
def parse_client(session: Session, service_name: ServiceName) -> Client:
```

## parse_collections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L104)

```python
def parse_collections(
    resource: Boto3ServiceResource,
) -> Generator[Collection, None, None]:
```

## parse_identifiers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L123)

```python
def parse_identifiers(
    resource: Boto3ServiceResource,
) -> Generator[Attribute, None, None]:
```

## parse_methods

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L131)

```python
def parse_methods(public_methods: Dict) -> Generator[Method, None, None]:
```

## parse_paginators

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L252)

```python
def parse_paginators(
    client: BaseClient,
    service_paginator_model: PaginatorModel,
) -> Generator[Paginator, None, None]:
```

## parse_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L147)

```python
def parse_resource(resource: Boto3ServiceResource) -> Resource:
```

## parse_return_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L169)

```python
def parse_return_type(meta: List[DocstringMeta]) -> TypeAnnotation:
```

## parse_service_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L236)

```python
def parse_service_paginator(
    session: Session,
    service_name: ServiceName,
) -> Optional[ServicePaginator]:
```

## parse_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L177)

```python
def parse_service_resource(
    session: Session,
    service_name: ServiceName,
) -> Optional[ServiceResource]:
```

## parse_service_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L216)

```python
def parse_service_waiter(
    session: Session,
    service_name: ServiceName,
) -> Optional[ServiceWaiter]:
```

## parse_type_from_str

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L209)

```python
def parse_type_from_str(type_str: str) -> TypeAnnotation:
```

## parse_waiters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L226)

```python
def parse_waiters(client: BaseClient) -> Generator[Waiter, None, None]:
```

## retrieve_sub_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L268)

```python
def retrieve_sub_resources(
    session: Session,
    resource: Boto3ResourceMeta,
) -> Generator[Boto3ServiceResource, None, None]:
```
