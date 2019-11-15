# TypeSubscript

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_subscript](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeSubscript
    - [TypeSubscript](#typesubscript)
        - [TypeSubscript().add_child](#typesubscriptadd_child)
        - [TypeSubscript().copy](#typesubscriptcopy)
        - [TypeSubscript().get_import_record](#typesubscriptget_import_record)
        - [TypeSubscript().get_types](#typesubscriptget_types)
        - [TypeSubscript().is_dict](#typesubscriptis_dict)
        - [TypeSubscript().is_list](#typesubscriptis_list)
        - [TypeSubscript().remove_children](#typesubscriptremove_children)
        - [TypeSubscript().render](#typesubscriptrender)

## TypeSubscript

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L9)

```python
class TypeSubscript(FakeAnnotation):
    def __init__(
        parent: FakeAnnotation,
        children: Iterable[FakeAnnotation] = (),
    ) -> None:
```

### TypeSubscript().add_child

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L38)

```python
def add_child(child: FakeAnnotation) -> None:
```

### TypeSubscript().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L47)

```python
def copy() -> TypeSubscript:
```

### TypeSubscript().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L26)

```python
def get_import_record() -> ImportRecord:
```

### TypeSubscript().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L29)

```python
def get_types() -> Set[FakeAnnotation]:
```

### TypeSubscript().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L41)

```python
def is_dict() -> bool:
```

### TypeSubscript().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L44)

```python
def is_list() -> bool:
```

### TypeSubscript().remove_children

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L35)

```python
def remove_children() -> None:
```

### TypeSubscript().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L19)

```python
def render() -> str:
```
