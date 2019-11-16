# Parsers

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py) module.

Parsers for boto3 clients and resources.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Parsers
    - [get_boto3_client](#get_boto3_client)
    - [get_boto3_resource](#get_boto3_resource)
    - [get_public_methods](#get_public_methods)
    - [get_resource_public_methods](#get_resource_public_methods)
    - [get_sub_resources](#get_sub_resources)
    - [parse_attributes](#parse_attributes)
    - [parse_boto3_module](#parse_boto3_module)
    - [parse_client](#parse_client)
    - [parse_collections](#parse_collections)
    - [parse_fake_service_module](#parse_fake_service_module)
    - [parse_identifiers](#parse_identifiers)
    - [parse_master_module](#parse_master_module)
    - [parse_method](#parse_method)
    - [parse_resource](#parse_resource)
    - [parse_service_module](#parse_service_module)
    - [parse_service_resource](#parse_service_resource)

## get_boto3_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L42)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L56)

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

## get_public_methods

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L104)

```python
def get_public_methods(inspect_class: Any) -> Dict[str, FunctionType]:
```

Extract public methods from any class.

#### Arguments

- `inspect_class` - Inspect class.

#### Returns

A dictionary of method name and method.

## get_resource_public_methods

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L75)

```python
def get_resource_public_methods(
    resource_class: Boto3ResourceMeta,
) -> Dict[str, FunctionType]:
```

Extract public methods from boto3 sub resource.

#### Arguments

- `resource_class` - boto3 resource meta.

#### Returns

A dictionary of method name and method.

## get_sub_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L358)

```python
def get_sub_resources(
    session: Session,
    service_name: ServiceName,
    resource: Boto3ResourceMeta,
) -> List[Boto3ServiceResource]:
```

Initialize ServiceResource sub-resources with fake data.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.
- `resource` - Parent ServiceResource.

#### Returns

A list of initialized `Boto3ServiceResource`.

## parse_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L128)

```python
def parse_attributes(resource: Boto3ServiceResource) -> List[Attribute]:
```

Extract attributes from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Attribute structures.

## parse_boto3_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L564)

```python
def parse_boto3_module(
    session: Session,
    service_names: Iterable[ServiceName],
) -> Boto3Module:
```

Parse data for boto3-stubs module.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

MasterModule structure.

## parse_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L151)

```python
def parse_client(session: Session, service_name: ServiceName) -> Client:
```

Parse boto3 client to a structure.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

Client structure.

## parse_collections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L183)

```python
def parse_collections(
    parent_name: str,
    resource: Boto3ServiceResource,
) -> List[Collection]:
```

Extract collections from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Collection structures.

## parse_fake_service_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L504)

```python
def parse_fake_service_module(
    session: Session,
    service_name: ServiceName,
) -> ServiceModule:
```

Create fake boto3 service module structure.

Used by stubs and master package.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

ServiceModule structure.

## parse_identifiers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L219)

```python
def parse_identifiers(resource: Boto3ServiceResource) -> List[Attribute]:
```

Extract collections from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Attribute structures.

## parse_master_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L543)

```python
def parse_master_module(
    session: Session,
    service_names: Iterable[ServiceName],
) -> MasterModule:
```

Parse data for master module.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

MasterModule structure.

## parse_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L236)

```python
def parse_method(parent_name: str, name: str, method: FunctionType) -> Method:
```

Parse method to a structure.

#### Arguments

- `parent_name` - Parent class name.
- `method` - Inspect method.

#### Returns

Method structure.

## parse_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L266)

```python
def parse_resource(
    resource: Boto3ServiceResource,
    service_name: ServiceName,
) -> Resource:
```

Parse boto3 sub Resource data.

#### Arguments

- `resource` - Original boto3 resource.

#### Returns

Resource structure.

## parse_service_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L406)

```python
def parse_service_module(
    session: Session,
    service_name: ServiceName,
) -> ServiceModule:
```

Extract all data from boto3 service meodule.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

ServiceModule structure.

## parse_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers.py#L307)

```python
def parse_service_resource(
    session: Session,
    service_name: ServiceName,
) -> Optional[ServiceResource]:
```

Parse boto3 ServiceResource data.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

ServiceResource structure or None if service does not have a resource.
