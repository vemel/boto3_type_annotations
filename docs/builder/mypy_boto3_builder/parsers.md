# Parsers

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Parsers
    - [get_boto3_client](#get_boto3_client)
    - [get_boto3_resource](#get_boto3_resource)
    - [get_resource_public_actions](#get_resource_public_actions)
    - [parse_attributes](#parse_attributes)
    - [parse_boto3_module](#parse_boto3_module)
    - [parse_client](#parse_client)
    - [parse_collections](#parse_collections)
    - [parse_fake_service_module](#parse_fake_service_module)
    - [parse_identifiers](#parse_identifiers)
    - [parse_master_module](#parse_master_module)
    - [parse_methods](#parse_methods)
    - [parse_resource](#parse_resource)
    - [parse_service_module](#parse_service_module)
    - [parse_service_resource](#parse_service_resource)
    - [retrieve_sub_resources](#retrieve_sub_resources)

## get_boto3_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L40)

```python
def get_boto3_client(
    session: Session,
    service_name: ServiceName,
) -> BaseClient:
```

## get_boto3_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L44)

```python
def get_boto3_resource(
    session: Session,
    service_name: ServiceName,
) -> Boto3ServiceResource:
```

## get_resource_public_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L50)

```python
def get_resource_public_actions(resource_class: Resource) -> Dict[str, Any]:
```

## parse_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L61)

```python
def parse_attributes(
    resource: Boto3ServiceResource,
) -> Generator[Attribute, None, None]:
```

## parse_boto3_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L307)

```python
def parse_boto3_module(
    session: Session,
    service_names: Iterable[ServiceName],
) -> Boto3Module:
```

## parse_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L72)

```python
def parse_client(session: Session, service_name: ServiceName) -> Client:
```

## parse_collections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L82)

```python
def parse_collections(
    resource: Boto3ServiceResource,
) -> Generator[Collection, None, None]:
```

## parse_fake_service_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L269)

```python
def parse_fake_service_module(
    session: Session,
    service_name: ServiceName,
) -> ServiceModule:
```

## parse_identifiers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L104)

```python
def parse_identifiers(
    resource: Boto3ServiceResource,
) -> Generator[Attribute, None, None]:
```

## parse_master_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L296)

```python
def parse_master_module(
    session: Session,
    service_names: Iterable[ServiceName],
) -> MasterModule:
```

## parse_methods

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L112)

```python
def parse_methods(
    public_methods: Dict[str, Any],
) -> Generator[Method, None, None]:
```

## parse_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L133)

```python
def parse_resource(resource: Boto3ServiceResource) -> Resource:
```

## parse_service_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L222)

```python
def parse_service_module(
    session: Session,
    service_name: ServiceName,
) -> ServiceModule:
```

## parse_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L155)

```python
def parse_service_resource(
    session: Session,
    service_name: ServiceName,
) -> Optional[ServiceResource]:
```

## retrieve_sub_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L188)

```python
def retrieve_sub_resources(
    session: Session,
    service_name: ServiceName,
    resource: Boto3ResourceMeta,
) -> Generator[Boto3ServiceResource, None, None]:
```
