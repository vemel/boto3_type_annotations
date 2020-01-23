# TypeValue

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.docstring_parser.type_value](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py) module.

Structure for parsed as dict request or response syntax values.

- [mypy-boto3](../../../../README.md#mypy_boto3) / [Modules](../../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / TypeValue
    - [TypeValue](#typevalue)
        - [TypeValue().get_type](#typevalueget_type)
        - [TypeValue().is_dict](#typevalueis_dict)
        - [TypeValue().is_func_call](#typevalueis_func_call)
        - [TypeValue().is_list](#typevalueis_list)
        - [TypeValue().is_literal](#typevalueis_literal)
        - [TypeValue().is_literal_item](#typevalueis_literal_item)
        - [TypeValue().is_plain](#typevalueis_plain)
        - [TypeValue().is_set](#typevalueis_set)
        - [TypeValue().is_union](#typevalueis_union)

## TypeValue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L18)

```python
class TypeValue():
    def __init__(prefix: str, value: Dict[str, Any]) -> None:
```

Structure for parsed as dict request or response syntax values.

### TypeValue().get_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L186)

```python
def get_type() -> FakeAnnotation:
```

### TypeValue().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L46)

```python
def is_dict() -> bool:
```

### TypeValue().is_func_call

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L61)

```python
def is_func_call() -> bool:
```

### TypeValue().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L49)

```python
def is_list() -> bool:
```

### TypeValue().is_literal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L52)

```python
def is_literal() -> bool:
```

### TypeValue().is_literal_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L155)

```python
def is_literal_item() -> bool:
```

### TypeValue().is_plain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L64)

```python
def is_plain() -> bool:
```

### TypeValue().is_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L55)

```python
def is_set() -> bool:
```

### TypeValue().is_union

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L58)

```python
def is_union() -> bool:
```
