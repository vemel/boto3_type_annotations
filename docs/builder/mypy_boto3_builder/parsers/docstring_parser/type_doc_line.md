# TypeDocLine

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.docstring_parser.type_doc_line](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py) module.

Structure for parsed as dict `:type:` or `:rtype:` nested lines.

- [mypy-boto3](../../../../README.md#mypy_boto3) / [Modules](../../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / TypeDocLine
    - [TypeDocLine](#typedocline)
        - [TypeDocLine().indented](#typedoclineindented)
        - [TypeDocLine().render](#typedoclinerender)
        - [TypeDocLine().required](#typedoclinerequired)

## TypeDocLine

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L7)

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

#### Arguments

- `name` - Argument or TypedDict key name
- `type_name` - Argument or TypedDict key type string.
- `line` - Raw original line parts.
- `description` - Rest of line for argument or TypedDict key definition.
- `indented` - Intended lines.

### TypeDocLine().indented

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L33)

```python
@property
def indented() -> List['TypeDocLine']:
```

Get indented lines list.

#### Returns

A list of [TypeDocLine](#typedocline).

### TypeDocLine().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L53)

```python
def render() -> str:
```

Get original string with indentation.

#### Returns

A string as close as possible to original.

### TypeDocLine().required

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L46)

```python
@property
def required() -> bool:
```

Whether the argument or TypedDict key is required.
