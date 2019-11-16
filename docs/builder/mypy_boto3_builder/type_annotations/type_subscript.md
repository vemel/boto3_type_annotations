# TypeSubscript

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_subscript](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py) module.

Wrapper for subscript type annotations, like `List[str]`.

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L12)

```python
class TypeSubscript(FakeAnnotation):
    def __init__(
        parent: FakeAnnotation,
        children: Iterable[FakeAnnotation] = (),
    ) -> None:
```

Wrapper for subscript type annotations, like `List[str]`.

#### Arguments

- `parent` - Parent type annotation.
- `children` - Children type annotations.

### TypeSubscript().add_child

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L55)

```python
def add_child(child: FakeAnnotation) -> None:
```

### TypeSubscript().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L64)

```python
def copy() -> TypeSubscript:
```

### TypeSubscript().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L43)

```python
def get_import_record() -> ImportRecord:
```

### TypeSubscript().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L46)

```python
def get_types() -> Set[FakeAnnotation]:
```

### TypeSubscript().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L58)

```python
def is_dict() -> bool:
```

### TypeSubscript().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L61)

```python
def is_list() -> bool:
```

### TypeSubscript().remove_children

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L52)

```python
def remove_children() -> None:
```

### TypeSubscript().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_subscript.py#L30)

```python
def render() -> str:
```

Render to string.

#### Returns

A string with a valid type annotation.
