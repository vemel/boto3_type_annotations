# TypeLiteral

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_literal](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py) module.

Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeLiteral
    - [TypeLiteral](#typeliteral)
        - [TypeLiteral().add_child](#typeliteraladd_child)
        - [TypeLiteral().add_literal_child](#typeliteraladd_literal_child)
        - [TypeLiteral().copy](#typeliteralcopy)
        - [TypeLiteral.get_import_record](#typeliteralget_import_record)
        - [TypeLiteral().is_literal](#typeliteralis_literal)
        - [TypeLiteral().render](#typeliteralrender)

## TypeLiteral

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L11)

```python
class TypeLiteral(FakeAnnotation):
    def __init__(*children: Any) -> None:
```

Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`

#### Arguments

- `children` - Literal values.

### TypeLiteral().add_child

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L58)

```python
def add_child(child: FakeAnnotation) -> None:
```

### TypeLiteral().add_literal_child

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L61)

```python
def add_literal_child(child: Any) -> None:
```

Add new child to [TypeLiteral](#typeliteral) annotation.

### TypeLiteral().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L46)

```python
def copy() -> 'TypeLiteral':
```

Create a copy of type annotation wrapper.

### TypeLiteral.get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L34)

```python
@staticmethod
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

### TypeLiteral().is_literal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L52)

```python
def is_literal() -> bool:
```

Whether type annotation is `Literal`.

### TypeLiteral().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L22)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.
