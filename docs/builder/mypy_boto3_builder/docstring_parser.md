# DocstringParser

> Auto-generated documentation for [builder.mypy_boto3_builder.docstring_parser](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py) module.

Boto3 docstring parser for arguemnts and return type annotations.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / DocstringParser
    - [DocstringParser](#docstringparser)
        - [DocstringParser().enrich_arguments](#docstringparserenrich_arguments)
        - [DocstringParser().get_docless_method_arguments](#docstringparserget_docless_method_arguments)
        - [DocstringParser().get_function_arguments](#docstringparserget_function_arguments)
        - [DocstringParser().get_return_type](#docstringparserget_return_type)
        - [DocstringParser().parse_any_syntax](#docstringparserparse_any_syntax)
        - [DocstringParser().parse_dict_syntax](#docstringparserparse_dict_syntax)
        - [DocstringParser().parse_syntax](#docstringparserparse_syntax)
        - [DocstringParser.parse_type](#docstringparserparse_type)
        - [DocstringParser().parse_typed_dict_syntax](#docstringparserparse_typed_dict_syntax)
    - [main](#main)

## DocstringParser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L25)

```python
class DocstringParser():
    def __init__() -> None:
```

### DocstringParser().enrich_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L152)

```python
def enrich_arguments(
    docstring: str,
    arguments: List[Argument],
    prefix: str,
) -> None:
```

### DocstringParser().get_docless_method_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L101)

```python
def get_docless_method_arguments(
    method_name: str,
) -> Optional[List[Argument]]:
```

### DocstringParser().get_function_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L141)

```python
def get_function_arguments(func: FunctionType) -> List[Argument]:
```

### DocstringParser().get_return_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L50)

```python
def get_return_type(docstring: str, prefix: str) -> FakeAnnotation:
```

### DocstringParser().parse_any_syntax

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L213)

```python
def parse_any_syntax(
    name: str,
    lines: List[str],
    prefix: str,
) -> FakeAnnotation:
```

### DocstringParser().parse_dict_syntax

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L249)

```python
def parse_dict_syntax(
    name: str,
    parent_type: FakeAnnotation,
    lines: List[str],
    prefix: str,
) -> FakeAnnotation:
```

### DocstringParser().parse_syntax

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L235)

```python
def parse_syntax(
    name: str,
    parent_type: FakeAnnotation,
    lines: List[str],
    prefix: str,
) -> FakeAnnotation:
```

### DocstringParser.parse_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L200)

```python
@staticmethod
def parse_type(type_str: str, name: Optional[str] = None) -> FakeAnnotation:
```

### DocstringParser().parse_typed_dict_syntax

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L267)

```python
def parse_typed_dict_syntax(
    name: str,
    lines: List[str],
    prefix: str,
) -> TypeTypedDict:
```

## main

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/docstring_parser.py#L296)

```python
def main() -> None:
```
