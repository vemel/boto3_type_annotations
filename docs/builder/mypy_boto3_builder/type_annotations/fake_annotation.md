# FakeAnnotation

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.fake_annotation](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / FakeAnnotation
    - [FakeAnnotation](#fakeannotation)
        - [FakeAnnotation().add_child](#fakeannotationadd_child)
        - [FakeAnnotation().copy](#fakeannotationcopy)
        - [FakeAnnotation().get_import_record](#fakeannotationget_import_record)
        - [FakeAnnotation().get_types](#fakeannotationget_types)
        - [FakeAnnotation().is_dict](#fakeannotationis_dict)
        - [FakeAnnotation().is_list](#fakeannotationis_list)
        - [FakeAnnotation().remove_children](#fakeannotationremove_children)
        - [FakeAnnotation().render](#fakeannotationrender)

## FakeAnnotation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L10)

```python
total_ordering
class FakeAnnotation():
```

### FakeAnnotation().add_child

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L47)

```python
def add_child(child: FakeAnnotation) -> None:
```

### FakeAnnotation().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L56)

```python
@abstractmethod
def copy() -> FakeAnnotation:
```

### FakeAnnotation().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L37)

```python
@abstractmethod
def get_import_record() -> ImportRecord:
```

### FakeAnnotation().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L41)

```python
def get_types() -> Set[FakeAnnotation]:
```

### FakeAnnotation().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L50)

```python
def is_dict() -> bool:
```

### FakeAnnotation().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L53)

```python
def is_list() -> bool:
```

### FakeAnnotation().remove_children

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L44)

```python
def remove_children() -> None:
```

### FakeAnnotation().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L33)

```python
@abstractmethod
def render() -> str:
```
