# TypeClass

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_class](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_class.py) module.

Wrapper for classes like `Paginator`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeClass
    - [TypeClass](#typeclass)
        - [TypeClass().copy](#typeclasscopy)
        - [TypeClass().get_import_name](#typeclassget_import_name)
        - [TypeClass().get_import_record](#typeclassget_import_record)
        - [TypeClass().render](#typeclassrender)

## TypeClass

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_class.py#L13)

```python
class TypeClass(FakeAnnotation):
    def __init__(value: type, alias: str = '') -> None:
```

Wrapper for classes like `Paginator`.

#### Arguments

- `value` - Any Class.
- `alias` - Local name.

### TypeClass().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_class.py#L53)

```python
def copy() -> TypeClass:
```

Create a copy of type annotation wrapper.

### TypeClass().get_import_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_class.py#L38)

```python
def get_import_name() -> str:
```

### TypeClass().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_class.py#L41)

```python
def get_import_record() -> ImportRecord:
```

### TypeClass().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_class.py#L26)

```python
def render() -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.
