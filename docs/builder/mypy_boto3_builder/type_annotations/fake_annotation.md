# FakeAnnotation

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.fake_annotation](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py) module.

Parent class for all type annotation wrappers.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / FakeAnnotation
    - [FakeAnnotation](#fakeannotation)
        - [FakeAnnotation().add_child](#fakeannotationadd_child)
        - [FakeAnnotation().add_literal_child](#fakeannotationadd_literal_child)
        - [FakeAnnotation().copy](#fakeannotationcopy)
        - [FakeAnnotation().get_import_record](#fakeannotationget_import_record)
        - [FakeAnnotation().get_types](#fakeannotationget_types)
        - [FakeAnnotation().is_dict](#fakeannotationis_dict)
        - [FakeAnnotation().is_list](#fakeannotationis_list)
        - [FakeAnnotation().is_literal](#fakeannotationis_literal)
        - [FakeAnnotation().is_potential_literal](#fakeannotationis_potential_literal)
        - [FakeAnnotation().remove_children](#fakeannotationremove_children)
        - [FakeAnnotation().render](#fakeannotationrender)

## FakeAnnotation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L13)

```python
total_ordering
class FakeAnnotation():
```

Parent class for all type annotation wrappers.

### FakeAnnotation().add_child

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L63)

```python
def add_child(child: FakeAnnotation) -> None:
```

Add new child to `TypeSubscript` or `TypeTypedDict` annotation.

### FakeAnnotation().add_literal_child

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L68)

```python
def add_literal_child(child: Any) -> None:
```

Add new child to `TypeLiteral` annotation.

### FakeAnnotation().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L97)

```python
@abstractmethod
def copy() -> FakeAnnotation:
```

Create a copy of type annotation wrapper.

### FakeAnnotation().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L46)

```python
@abstractmethod
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

### FakeAnnotation().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L52)

```python
def get_types() -> Set[FakeAnnotation]:
```

Get all used type annotations recursively including self.

### FakeAnnotation().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L73)

```python
def is_dict() -> bool:
```

Whether type annotation is `Dict` or `TypedDict`.

### FakeAnnotation().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L79)

```python
def is_list() -> bool:
```

Whether type annotation is `List`.

### FakeAnnotation().is_literal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L85)

```python
def is_literal() -> bool:
```

Whether type annotation is `Literal`.

### FakeAnnotation().is_potential_literal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L91)

```python
def is_potential_literal() -> bool:
```

Whether type annotation can be a `Literal`.

### FakeAnnotation().remove_children

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L58)

```python
def remove_children() -> None:
```

Remove all children from `TypeSubscript` or `TypeTypedDict` annotation.

### FakeAnnotation().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/fake_annotation.py#L40)

```python
@abstractmethod
def render() -> str:
```

Render type annotation to a valid Python code for local usage.
