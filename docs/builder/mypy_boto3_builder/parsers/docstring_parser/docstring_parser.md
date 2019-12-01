# DocstringParser

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.docstring_parser.docstring_parser](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py) module.

Botocore docstring parser.

- [mypy-boto3](../../../../README.md#mypy_boto3) / [Modules](../../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / DocstringParser
    - [DocstringParser](#docstringparser)
        - [DocstringParser().get_arguments](#docstringparserget_arguments)
        - [DocstringParser().get_return_type](#docstringparserget_return_type)
        - [DocstringParser.parse_type](#docstringparserparse_type)

## DocstringParser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L30)

```python
class DocstringParser():
    def __init__(prefix: str, arguments: List[Argument]) -> None:
```

Botocore docstring parser.

#### Arguments

- `prefix` - Prefix for generated TypeDict names.
- `arguments` - List of arguments extracted from argspec.

### DocstringParser().get_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L187)

```python
def get_arguments(input_string: str) -> List[Argument]:
```

Get list of function arguments with type annottions.

#### Arguments

- `input_string` - Function docstring.

#### Returns

A list of `Argument` structures.

### DocstringParser().get_return_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L297)

```python
def get_return_type(input_string: str) -> FakeAnnotation:
```

Get function return type annotation.

#### Arguments

- `input_string` - Function docstring.

#### Returns

A valid type annotation.

### DocstringParser.parse_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L333)

```python
@staticmethod
def parse_type(type_str: str, name: Optional[str] = None) -> FakeAnnotation:
```

Get type annotation from type string.

#### Arguments

- `type_str` - Type string.
- `name` - Argument name.

#### Returns

A valid type annotation.

#### Raises

- `ValueError` - If `type_str` is unknown.
