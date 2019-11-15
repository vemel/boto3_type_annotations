# TypeAnnotation

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_annotation](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeAnnotation
    - [TypeAnnotation](#typeannotation)
        - [TypeAnnotation().copy](#typeannotationcopy)
        - [TypeAnnotation().get_import_record](#typeannotationget_import_record)
        - [TypeAnnotation().is_dict](#typeannotationis_dict)
        - [TypeAnnotation().is_list](#typeannotationis_list)
        - [TypeAnnotation().render](#typeannotationrender)

## TypeAnnotation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L10)

```python
class TypeAnnotation(FakeAnnotation):
    def __init__(wrapped_type: Any) -> None:
```

### TypeAnnotation().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L51)

```python
def copy() -> TypeAnnotation:
```

### TypeAnnotation().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L40)

```python
def get_import_record() -> ImportRecord:
```

### TypeAnnotation().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L45)

```python
def is_dict() -> bool:
```

### TypeAnnotation().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L48)

```python
def is_list() -> bool:
```

### TypeAnnotation().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L17)

```python
def render() -> str:
```
