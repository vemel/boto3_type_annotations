# ArgSpecParser

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.docstring_parser.argspec_parser](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py) module.

Converter of function argspec to `Argument` list.

- [mypy-boto3](../../../../README.md#mypy_boto3) / [Modules](../../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / ArgSpecParser
    - [ArgSpecParser](#argspecparser)
        - [ArgSpecParser().get_function_arguments](#argspecparserget_function_arguments)

## ArgSpecParser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py#L16)

```python
class ArgSpecParser():
```

Converter of function argspec to `Argument` list.

### ArgSpecParser().get_function_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py#L52)

```python
def get_function_arguments(func: FunctionType) -> List[Argument]:
```
