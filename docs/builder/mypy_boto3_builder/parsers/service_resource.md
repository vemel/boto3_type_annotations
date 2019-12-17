# Service Resource

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.service_resource](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/service_resource.py) module.

Parser for Boto3 ServiceResource, produces `structires.ServiceResource`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Service Resource
    - [get_sub_resources](#get_sub_resources)
    - [parse_service_resource](#parse_service_resource)

## get_sub_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/service_resource.py#L97)

```python
def get_sub_resources(
    session: Session,
    service_name: ServiceName,
    resource: Boto3ServiceResource,
) -> List[Boto3ServiceResource]:
```

Initialize ServiceResource sub-resources with fake data.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.
- `resource` - Parent ServiceResource.

#### Returns

A list of initialized `Boto3ServiceResource`.

## parse_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/service_resource.py#L29)

```python
def parse_service_resource(
    session: Session,
    service_name: ServiceName,
    shape_parser: ShapeParser,
) -> Optional[ServiceResource]:
```

Parse boto3 ServiceResource data.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

ServiceResource structure or None if service does not have a resource.
