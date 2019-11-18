# Helpers

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.helpers](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/helpers.py) module.

Helpers for parsing methods and attributes.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Helpers
    - [get_public_methods](#get_public_methods)
    - [parse_attributes](#parse_attributes)
    - [parse_method](#parse_method)

## get_public_methods

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/helpers.py#L18)

```python
def get_public_methods(inspect_class: Any) -> Dict[str, FunctionType]:
```

Extract public methods from any class.

#### Arguments

- `inspect_class` - Inspect class.

#### Returns

A dictionary of method name and method.

## parse_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/helpers.py#L42)

```python
def parse_attributes(resource: Boto3ServiceResource) -> List[Attribute]:
```

Extract attributes from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Attribute structures.

## parse_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/helpers.py#L65)

```python
def parse_method(parent_name: str, name: str, method: FunctionType) -> Method:
```

Parse method to a structure.

#### Arguments

- `parent_name` - Parent class name.
- `method` - Inspect method.

#### Returns

Method structure.
