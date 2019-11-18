# Collections

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.collections](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/collections.py) module.

Boto3 ServiceResource collections parser, produces `structures.Collection`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Collections
    - [parse_collections](#parse_collections)

## parse_collections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/collections.py#L16)

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
