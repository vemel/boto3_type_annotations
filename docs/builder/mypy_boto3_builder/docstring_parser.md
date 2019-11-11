# DocstringParser

> Auto-generated documentation for [builder.mypy_boto3_builder.docstring_parser](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / DocstringParser
    - [DocstringParser](#docstringparser)
        - [DocstringParser.get_arguments](#docstringparserget_arguments)
        - [DocstringParser.get_return_type](#docstringparserget_return_type)
        - [DocstringParser.parse_type](#docstringparserparse_type)

## DocstringParser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L10)

```python
class DocstringParser():
```

### DocstringParser.get_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L27)

```python
@classmethod
def get_arguments(docstring: str) -> List[Argument]:
```

### DocstringParser.get_return_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L15)

```python
@classmethod
def get_return_type(docstring: str) -> FakeAnnotation:
```

### DocstringParser.parse_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L58)

```python
@staticmethod
def parse_type(type_str: str) -> FakeAnnotation:
```
