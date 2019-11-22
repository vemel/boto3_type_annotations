# ImportString

> Auto-generated documentation for [builder.mypy_boto3_builder.import_helpers.import_string](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_string.py) module.

Wrapper for Python import strings.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / ImportString
    - [ImportString](#importstring)
        - [ImportString.empty](#importstringempty)
        - [ImportString.from_str](#importstringfrom_str)
        - [ImportString().master_name](#importstringmaster_name)
        - [ImportString().render](#importstringrender)
        - [ImportString().startswith](#importstringstartswith)

## ImportString

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_string.py#L9)

```python
class ImportString():
    def __init__(master_name: str, *parts: str) -> None:
```

Wrapper for Python import strings.

#### Arguments

- `import_string` - Wrapped import string.

#### Examples

```python
import_string = ImportString('my.name')

str(import_string)
'my.name'

import_string.render()
'my.name'

import_string.parts.append('test')
import_string.render()
'my.name.test'
```

### ImportString.empty

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_string.py#L43)

```python
@classmethod
def empty() -> ImportString:
```

### ImportString.from_str

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_string.py#L39)

```python
@classmethod
def from_str(import_string: str) -> ImportString:
```

### ImportString().master_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_string.py#L109)

```python
@property
def master_name() -> str:
```

Get first import string part or `builtins`.

### ImportString().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_string.py#L100)

```python
def render() -> str:
```

Render to string.

#### Returns

Ready to use import string.

### ImportString().startswith

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_string.py#L68)

```python
def startswith(other: ImportString) -> bool:
```

Check if import string starts with `other`.

#### Examples

```python
ImportString('my', 'name').startswith(ImportString('my'))
True

ImportString('my_module', 'name').startswith(ImportString('my'))
False

ImportString('my', 'name').startswith(ImportString('my, 'name'))
True

ImportString('my', 'name').startswith(ImportString.empty())
True
```

#### Arguments

- `other` - Other import string.
