# TypeConstant

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_constant](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_constant.py) module.

Wrapper for constant like `False` or `"test"`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeConstant
    - [TypeConstant](#typeconstant)
        - [TypeConstant().copy](#typeconstantcopy)
        - [TypeConstant().get_import_record](#typeconstantget_import_record)
        - [TypeConstant().render](#typeconstantrender)

## TypeConstant

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_constant.py#L12)

```python
class TypeConstant(FakeAnnotation):
    def __init__(value: Any) -> None:
```

Wrapper for constant like `False` or `"test"`.

#### Arguments

- `value` - Constant value.

### TypeConstant().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_constant.py#L35)

```python
def copy() -> TypeConstant:
```

Create a copy of type annotation wrapper.

### TypeConstant().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_constant.py#L32)

```python
def get_import_record() -> ImportRecord:
```

### TypeConstant().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_constant.py#L23)

```python
def render() -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.
