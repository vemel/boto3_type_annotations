# Resource

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.resource](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/resource.py) module.

Parser for Boto3 ServiceResource sub-resource, produces `structures.Resource`

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Resource
    - [get_resource_public_methods](#get_resource_public_methods)
    - [parse_resource](#parse_resource)

## get_resource_public_methods

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/resource.py#L62)

```python
def get_resource_public_methods(
    resource_class: Type[Boto3ServiceResource],
) -> Dict[str, FunctionType]:
```

Extract public methods from boto3 sub resource.

#### Arguments

- `resource_class` - boto3 resource meta.

#### Returns

A dictionary of method name and method.

## parse_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/resource.py#L21)

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
