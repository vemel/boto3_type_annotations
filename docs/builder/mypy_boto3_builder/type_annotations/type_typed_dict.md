# TypeTypedDict

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_typed_dict](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeTypedDict
    - [TypeTypedDict](#typetypeddict)
        - [TypeTypedDict().add_attribute](#typetypeddictadd_attribute)
        - [TypeTypedDict().copy](#typetypeddictcopy)
        - [TypeTypedDict().get_children_types](#typetypeddictget_children_types)
        - [TypeTypedDict().get_import_record](#typetypeddictget_import_record)
        - [TypeTypedDict().get_optional](#typetypeddictget_optional)
        - [TypeTypedDict().get_required](#typetypeddictget_required)
        - [TypeTypedDict().get_types](#typetypeddictget_types)
        - [TypeTypedDict().has_both](#typetypeddicthas_both)
        - [TypeTypedDict().has_optional](#typetypeddicthas_optional)
        - [TypeTypedDict().has_required](#typetypeddicthas_required)
        - [TypeTypedDict().is_dict](#typetypeddictis_dict)
        - [TypeTypedDict().is_same](#typetypeddictis_same)
        - [TypeTypedDict().render](#typetypeddictrender)
        - [TypeTypedDict().render_class](#typetypeddictrender_class)
    - [TypedDictAttribute](#typeddictattribute)
        - [TypedDictAttribute().render](#typeddictattributerender)

## TypeTypedDict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L23)

```python
class TypeTypedDict(FakeAnnotation):
    def __init__(
        name: str,
        children: Iterable[TypedDictAttribute] = (),
        docstring: str = '',
    ) -> None:
```

### TypeTypedDict().add_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L43)

```python
def add_attribute(
    name: str,
    type_annotation: FakeAnnotation,
    required: bool,
) -> None:
```

### TypeTypedDict().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L84)

```python
def copy() -> TypeTypedDict:
```

### TypeTypedDict().get_children_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L92)

```python
def get_children_types() -> Set[FakeAnnotation]:
```

### TypeTypedDict().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L37)

```python
def get_import_record() -> ImportRecord:
```

### TypeTypedDict().get_optional

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L77)

```python
def get_optional() -> List[TypedDictAttribute]:
```

### TypeTypedDict().get_required

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L70)

```python
def get_required() -> List[TypedDictAttribute]:
```

### TypeTypedDict().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L40)

```python
def get_types() -> Set[FakeAnnotation]:
```

### TypeTypedDict().has_both

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L67)

```python
def has_both() -> bool:
```

### TypeTypedDict().has_optional

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L55)

```python
def has_optional() -> bool:
```

### TypeTypedDict().has_required

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L61)

```python
def has_required() -> bool:
```

### TypeTypedDict().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L48)

```python
def is_dict() -> bool:
```

### TypeTypedDict().is_same

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L87)

```python
def is_same(other: TypeTypedDict) -> bool:
```

### TypeTypedDict().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L34)

```python
def render() -> str:
```

### TypeTypedDict().render_class

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L51)

```python
def render_class() -> str:
```

## TypedDictAttribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L13)

```python
class TypedDictAttribute():
    def __init__(name: str, type_annotation: FakeAnnotation, required: bool):
```

### TypedDictAttribute().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L19)

```python
def render() -> str:
```
