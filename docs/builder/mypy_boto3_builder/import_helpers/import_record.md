# ImportRecord

> Auto-generated documentation for [builder.mypy_boto3_builder.import_helpers.import_record](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py) module.

Helper for Python import strings.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / ImportRecord
    - [ImportRecord](#importrecord)
        - [ImportRecord.empty](#importrecordempty)
        - [ImportRecord().get_external](#importrecordget_external)
        - [ImportRecord().get_local_name](#importrecordget_local_name)
        - [ImportRecord().is_builtins](#importrecordis_builtins)
        - [ImportRecord().is_internal](#importrecordis_internal)
        - [ImportRecord().is_local](#importrecordis_local)
        - [ImportRecord().is_third_party](#importrecordis_third_party)
        - [ImportRecord().is_type_defs](#importrecordis_type_defs)
        - [ImportRecord().render](#importrecordrender)

## ImportRecord

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L14)

```python
dataclass
total_ordering
class ImportRecord():
    def __init__(source: str, name: str = '', alias: str = '') -> None:
```

Helper for Python import strings.

#### Arguments

- `source` - Source of import.
- `name` - Import name.
- `alias` - Import local name.

### ImportRecord.empty

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L42)

```python
@classmethod
def empty() -> ImportRecord:
```

### ImportRecord().get_external

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L140)

```python
def get_external(_module_name: str) -> ImportRecord:
```

Get itself.

Overriden by `InternalImportRecord`.

### ImportRecord().get_local_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L91)

```python
def get_local_name() -> str:
```

Get local import name.

### ImportRecord().is_builtins

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L97)

```python
def is_builtins() -> bool:
```

Whether import is from Python `builtins` module.

### ImportRecord().is_internal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L134)

```python
def is_internal() -> bool:
```

Whether import is internal and requires [ImportRecord().get_external](#importrecordget_external) call before rendering.

### ImportRecord().is_local

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L119)

```python
def is_local() -> bool:
```

Whether import is from local module.

### ImportRecord().is_third_party

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L109)

```python
def is_third_party() -> bool:
```

Whether import is from 3rd party module.

### ImportRecord().is_type_defs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L103)

```python
def is_type_defs() -> bool:
```

Whether import is from `type_defs` module.

### ImportRecord().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L46)

```python
def render() -> str:
```
