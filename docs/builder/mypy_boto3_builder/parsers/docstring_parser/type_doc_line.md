# TypeDocLine

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.docstring_parser.type_doc_line](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py) module.

Structure for parsed as dict `:type:` or `:rtype:` nested lines.

- [mypy-boto3](../../../../README.md#mypy_boto3) / [Modules](../../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / TypeDocLine
    - [TypeDocLine](#typedocline)
        - [TypeDocLine().indented](#typedoclineindented)
        - [TypeDocLine().render](#typedoclinerender)
        - [TypeDocLine().required](#typedoclinerequired)

## TypeDocLine

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L9)

```python
class TypeDocLine():
    def __init__(
        name: str = '',
        type_name: str = '',
        line: Iterable[str] = tuple(),
        description: str = '',
        indented: Iterable[Any] = tuple(),
    ) -> None:
```

Structure for parsed as dict `:type:` or `:rtype:` nested lines.

### TypeDocLine().indented

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L28)

```python
@property
def indented() -> List[TypeDocLine]:
```

### TypeDocLine().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L39)

```python
def render() -> str:
```

### TypeDocLine().required

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L35)

```python
@property
def required() -> bool:
```
