# TypeAnnotation

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_annotation](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeAnnotation
    - [TypeAnnotation](#typeannotation)
        - [TypeAnnotation().get_import_record](#typeannotationget_import_record)
        - [TypeAnnotation().render](#typeannotationrender)

## TypeAnnotation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L8)

```python
class TypeAnnotation(FakeAnnotation):
    def __init__(wrapped_type: Any) -> None:
```

### TypeAnnotation().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L38)

```python
def get_import_record() -> ImportRecord:
```

### TypeAnnotation().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_annotation.py#L15)

```python
def render() -> str:
```
