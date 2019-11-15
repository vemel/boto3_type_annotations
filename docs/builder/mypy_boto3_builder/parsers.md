# Parsers

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py) module.

Parsers for boto3 clients and resources.

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
    - [parse_sub_resources](#parse_sub_resources)

## get_boto3_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L39)

```python
def get_boto3_client(
    session: Session,
    service_name: ServiceName,
) -> BaseClient:
```

Get boto3 client from `session`.

#### Arguments

- `session` - boto3 session.
- `service_name` - ServiceName instance.

#### Returns

Boto3 client.

## get_boto3_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L53)

```python
def get_boto3_resource(
    session: Session,
    service_name: ServiceName,
) -> Boto3ServiceResource:
```

Get boto3 resource from `session`.

#### Arguments

- `session` - boto3 session.
- `service_name` - ServiceName instance.

#### Returns

Boto3 resource.

#### Raises

- `ResourceNotExistsError` - If service does not have ServiceResource.

## get_resource_public_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L72)

```python
def get_resource_public_actions(resource_class: Resource) -> Dict[str, Any]:
```

## parse_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L87)

```python
def parse_attributes(resource: Boto3ServiceResource) -> List[Attribute]:
```

## parse_boto3_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L347)

```python
def parse_boto3_module(
    session: Session,
    service_names: Iterable[ServiceName],
) -> Boto3Module:
```

## parse_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L101)

```python
def parse_client(session: Session, service_name: ServiceName) -> Client:
```

## parse_collections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L111)

```python
def parse_collections(resource: Boto3ServiceResource) -> List[Collection]:
```

## parse_fake_service_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L309)

```python
def parse_fake_service_module(
    session: Session,
    service_name: ServiceName,
) -> ServiceModule:
```

## parse_identifiers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L134)

```python
def parse_identifiers(resource: Boto3ServiceResource) -> List[Attribute]:
```

## parse_master_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L336)

```python
def parse_master_module(
    session: Session,
    service_names: Iterable[ServiceName],
) -> MasterModule:
```

## parse_methods

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L142)

```python
def parse_methods(
    class_name: str,
    public_methods: Dict[str, Any],
) -> List[Method]:
```

## parse_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L167)

```python
def parse_resource(resource: Boto3ServiceResource) -> Resource:
```

## parse_service_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L259)

```python
def parse_service_module(
    session: Session,
    service_name: ServiceName,
) -> ServiceModule:
```

## parse_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L187)

```python
def parse_service_resource(
    session: Session,
    service_name: ServiceName,
) -> Optional[ServiceResource]:
```

## parse_sub_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L220)

```python
def parse_sub_resources(
    session: Session,
    service_name: ServiceName,
    resource: Boto3ResourceMeta,
) -> List[Boto3ServiceResource]:
```
