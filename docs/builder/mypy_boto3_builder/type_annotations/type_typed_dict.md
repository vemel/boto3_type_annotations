# TypeTypedDict

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_typed_dict](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py) module.

Wrapper for `typing/typing_extensions.TypedDict` type annotations.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeTypedDict
    - [TypeTypedDict](#typetypeddict)
        - [TypeTypedDict().add_attribute](#typetypeddictadd_attribute)
        - [TypeTypedDict().copy](#typetypeddictcopy)
        - [TypeTypedDict().get_attribute](#typetypeddictget_attribute)
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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L41)

```python
class TypeTypedDict(FakeAnnotation):
    def __init__(
        name: str,
        children: Iterable[TypedDictAttribute] = (),
        docstring: str = '',
    ) -> None:
```

Wrapper for `typing/typing_extensions.TypedDict` type annotations.

#### Arguments

- `name` - Type name.
- `children` - Typed dict attributes.
- `docstring` - Docstring for render.

### TypeTypedDict().add_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L97)

```python
def add_attribute(
    name: str,
    type_annotation: FakeAnnotation,
    required: bool,
) -> None:
```

Add new attribute to a dictionary.

#### Arguments

- `name` - Argument name.
- `type_annotation` - Argument type annotation.
- `required` - Whether argument has to be set.

### TypeTypedDict().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L161)

```python
def copy() -> TypeTypedDict:
```

Create a copy of type annotation wrapper.

### TypeTypedDict().get_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L61)

```python
def get_attribute(name: str) -> TypedDictAttribute:
```

#### See also

- [TypedDictAttribute](#typeddictattribute)

### TypeTypedDict().get_children_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L172)

```python
def get_children_types() -> Set[FakeAnnotation]:
```

### TypeTypedDict().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L80)

```python
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

### TypeTypedDict().get_optional

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L154)

```python
def get_optional() -> List[TypedDictAttribute]:
```

### TypeTypedDict().get_required

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L147)

```python
def get_required() -> List[TypedDictAttribute]:
```

### TypeTypedDict().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L86)

```python
def get_types() -> Set[FakeAnnotation]:
```

Get set with itself.

To get child types, [TypeTypedDict().get_children_types](#typetypeddictget_children_types) has to be used.

#### Returns

A set of type annotations.

### TypeTypedDict().has_both

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L141)

```python
def has_both() -> bool:
```

Whether TypedDict has both optional and required keys.

### TypeTypedDict().has_optional

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L123)

```python
def has_optional() -> bool:
```

Whether TypedDict has optional keys.

### TypeTypedDict().has_required

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L132)

```python
def has_required() -> bool:
```

Whether TypedDict has required keys.

### TypeTypedDict().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L110)

```python
def is_dict() -> bool:
```

Always True as it is a TypedDict.

### TypeTypedDict().is_same

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L167)

```python
def is_same(other: TypeTypedDict) -> bool:
```

### TypeTypedDict().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L68)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

### TypeTypedDict().render_class

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L116)

```python
def render_class() -> str:
```

Render class-based definition for debugging.

## TypedDictAttribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L16)

```python
class TypedDictAttribute():
    def __init__(name: str, type_annotation: FakeAnnotation, required: bool):
```

TypedDict attribute wrapper.

#### Arguments

- `name` - Attribute name.
- `type_annotation` - Attribute type annotation.
- `required` - Whether the attribute has to be set.

### TypedDictAttribute().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_typed_dict.py#L31)

```python
def render() -> str:
```

Render attribute to use in class-based TypedDict definition.

#### Returns

A string with argument definition.
