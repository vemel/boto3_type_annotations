# TypeLiteral

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.type_literal](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeLiteral
    - [TypeLiteral](#typeliteral)
        - [TypeLiteral().get_import_record](#typeliteralget_import_record)
        - [TypeLiteral().render](#typeliteralrender)

## TypeLiteral

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L8)

```python
class TypeLiteral(FakeAnnotation):
    def __init__(*children: str) -> None:
```

### TypeLiteral().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L17)

```python
def get_import_record() -> ImportRecord:
```

### TypeLiteral().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/type_literal.py#L13)

```python
def render() -> str:
```
