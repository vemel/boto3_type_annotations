# Attribute

> Auto-generated documentation for [builder.mypy_boto3_builder.structures.attribute](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/attribute.py) module.

Class or module attribute.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Attribute
    - [Attribute](#attribute)
        - [Attribute().get_types](#attributeget_types)

## Attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/attribute.py#L11)

```python
dataclass
class Attribute():
```

Class or module attribute.

#### Attributes

- `name` - Attribute name.
- `type` - Attribute type annotation.
- `value` - Attribute value.

### Attribute().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/attribute.py#L26)

```python
def get_types() -> Set[FakeAnnotation]:
```

Return all type annotations used.

#### Returns

A set of type annotations.
