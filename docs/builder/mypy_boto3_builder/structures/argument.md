# Argument

> Auto-generated documentation for [builder.mypy_boto3_builder.structures.argument](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/argument.py) module.

Method or function argument.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Argument
    - [Argument](#argument)
        - [Argument().get_types](#argumentget_types)
        - [Argument().required](#argumentrequired)

## Argument

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/argument.py#L11)

```python
dataclass
class Argument():
```

Method or function argument.

#### Attributes

- `name` - Argument name.
- `type` - Argument type annotation.
- `value` - Default argument value.
- `prefix` - Used for starargs.

### Argument().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/argument.py#L28)

```python
def get_types() -> Set[FakeAnnotation]:
```

### Argument().required

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/argument.py#L37)

```python
@property
def required() -> bool:
```
