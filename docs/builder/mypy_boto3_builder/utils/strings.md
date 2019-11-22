# Strings

> Auto-generated documentation for [builder.mypy_boto3_builder.utils.strings](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/utils/strings.py) module.

Multiple string utils collection.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](index.md#utils) / Strings
    - [clean_doc](#clean_doc)
    - [get_class_prefix](#get_class_prefix)

#### Attributes

- `RE_BACKSLASH` - Regexp to replace single backslashes: `re.compile('\\\\{1,2}')`

## clean_doc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/utils/strings.py#L13)

```python
def clean_doc(doc: Optional[str]) -> str:
```

Clean docstring to be safely rendered.

- If `doc` is not set, returns an empty docstring.
- Returns extra empty lines.
- Escapes backslashes.
- Replace trible doublequotes with triple single quotes.
- Tries to fit docstring to `LINE_LENGTH`

#### Arguments

- `doc` - Instance docstring.

#### Returns

Cleaned docstring.

## get_class_prefix

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/utils/strings.py#L82)

```python
def get_class_prefix(func_name: str) -> str:
```

Get a valid Python class prefix from `func_name`.

#### Arguments

- `func_name` - Any string.

#### Returns

String with a class prefix.
