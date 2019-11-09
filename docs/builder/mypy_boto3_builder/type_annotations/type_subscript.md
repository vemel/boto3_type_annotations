# Type Subscript

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_subscript](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / Type Subscript
    - [TypeSubstript](#typesubstript)
        - [TypeSubstript().get_import_record](#typesubstriptget_import_record)
        - [TypeSubstript().get_types](#typesubstriptget_types)
        - [TypeSubstript().render](#typesubstriptrender)

## TypeSubstript

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L7)

```python
class TypeSubstript(FakeAnnotation):
    def __init__(
        parent: FakeAnnotation,
        children: Iterable[FakeAnnotation] = (),
    ) -> None:
```

### TypeSubstript().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L24)

```python
def get_import_record() -> ImportRecord:
```

### TypeSubstript().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L27)

```python
def get_types() -> Set[FakeAnnotation]:
```

### TypeSubstript().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L17)

```python
def render() -> str:
```
