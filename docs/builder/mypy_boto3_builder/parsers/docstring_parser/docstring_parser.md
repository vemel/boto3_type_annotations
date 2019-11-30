# DocstringParser

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.docstring_parser.docstring_parser](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py) module.

Botocore docstring parser.

- [mypy-boto3](../../../../README.md#mypy_boto3) / [Modules](../../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / DocstringParser
    - [DocstringParser](#docstringparser)
        - [DocstringParser().get_arguments](#docstringparserget_arguments)
        - [DocstringParser().get_return_type](#docstringparserget_return_type)
        - [DocstringParser.parse_type](#docstringparserparse_type)

## DocstringParser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L25)

```python
class DocstringParser():
    def __init__(prefix: str, arguments: List[Argument]) -> None:
```

Botocore docstring parser.

### DocstringParser().get_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L166)

```python
def get_arguments(input_string: str) -> List[Argument]:
```

### DocstringParser().get_return_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L240)

```python
def get_return_type(input_string: str) -> FakeAnnotation:
```

### DocstringParser.parse_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L265)

```python
@staticmethod
def parse_type(type_str: str, name: Optional[str] = None) -> FakeAnnotation:
```
