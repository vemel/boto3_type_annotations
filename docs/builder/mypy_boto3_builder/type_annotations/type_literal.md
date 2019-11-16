# TypeLiteral

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_literal](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py) module.

Wrapper for `Literal` type annotations like `Literal['a', 'b']`

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeLiteral
    - [TypeLiteral](#typeliteral)
        - [TypeLiteral().copy](#typeliteralcopy)
        - [TypeLiteral().get_import_record](#typeliteralget_import_record)
        - [TypeLiteral().render](#typeliteralrender)

## TypeLiteral

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L14)

```python
class TypeLiteral(FakeAnnotation):
    def __init__(*children: Any) -> None:
```

Wrapper for `Literal` type annotations like `Literal['a', 'b']`

#### Arguments

- `children` - Literal values.

### TypeLiteral().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L33)

```python
def copy() -> TypeLiteral:
```

### TypeLiteral().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L30)

```python
def get_import_record() -> ImportRecord:
```

### TypeLiteral().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L26)

```python
def render() -> str:
```
