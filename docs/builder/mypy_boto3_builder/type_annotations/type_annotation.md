# TypeAnnotation

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_annotation](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py) module.

Wrapper for simple type annotation like `str` or `Dict`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeAnnotation
    - [TypeAnnotation](#typeannotation)
        - [TypeAnnotation.Any](#typeannotationany)
        - [TypeAnnotation().copy](#typeannotationcopy)
        - [TypeAnnotation().get_import_name](#typeannotationget_import_name)
        - [TypeAnnotation().get_import_record](#typeannotationget_import_record)
        - [TypeAnnotation().is_dict](#typeannotationis_dict)
        - [TypeAnnotation().is_list](#typeannotationis_list)
        - [TypeAnnotation().render](#typeannotationrender)

## TypeAnnotation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L14)

```python
class TypeAnnotation(FakeAnnotation):
    def __init__(wrapped_type: Any) -> None:
```

Wrapper for simple type annotation like `str` or `Dict`.

#### Arguments

- `wrapped_type` - Original type annotation.

### TypeAnnotation.Any

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L42)

```python
@classmethod
def Any() -> TypeAnnotation:
```

### TypeAnnotation().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L78)

```python
def copy() -> TypeAnnotation:
```

Create a copy of type annotation wrapper.

### TypeAnnotation().get_import_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L57)

```python
def get_import_name() -> str:
```

### TypeAnnotation().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L66)

```python
def get_import_record() -> ImportRecord:
```

### TypeAnnotation().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L72)

```python
def is_dict() -> bool:
```

### TypeAnnotation().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L75)

```python
def is_list() -> bool:
```

### TypeAnnotation().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L48)

```python
def render() -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.
