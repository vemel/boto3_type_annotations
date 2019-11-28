# SyntaxParser

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.syntax_parser](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/syntax_parser.py) module.

Botocore request syntax parser.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / SyntaxParser
    - [SyntaxParser](#syntaxparser)
        - [SyntaxParser.parse_docstring](#syntaxparserparse_docstring)

## SyntaxParser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/syntax_parser.py#L31)

```python
class SyntaxParser():
```

Botocore request syntax parser.

### SyntaxParser.parse_docstring

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/syntax_parser.py#L170)

```python
@classmethod
def parse_docstring(
    input_string: str,
    typed_dict_prefix: str,
) -> Dict[str, FakeAnnotation]:
```

Parse type annotations for request arguments.

#### Arguments

- `input_string` - Request syntax from dotocore docs.
- `typed_dict_prefix` - Prefix for TypedDict classes.

#### Returns

Mapping of argument name to its type annotation.
