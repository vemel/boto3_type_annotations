# ImportRecord

> Auto-generated documentation for [builder.mypy_boto3_builder.import_helpers.import_record](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / ImportRecord
    - [ImportRecord](#importrecord)
        - [ImportRecord().get_external](#importrecordget_external)
        - [ImportRecord().get_local_name](#importrecordget_local_name)
        - [ImportRecord().is_builtins](#importrecordis_builtins)
        - [ImportRecord().is_internal](#importrecordis_internal)
        - [ImportRecord().is_local](#importrecordis_local)
        - [ImportRecord().is_third_party](#importrecordis_third_party)
        - [ImportRecord().is_type_defs](#importrecordis_type_defs)
        - [ImportRecord().package_name](#importrecordpackage_name)

## ImportRecord

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L11)

```python
dataclass
total_ordering
class ImportRecord():
    def __init__(source: str, name: str = '', alias: str = '') -> None:
```

### ImportRecord().get_external

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L107)

```python
def get_external(_module_name: str) -> ImportRecord:
```

### ImportRecord().get_local_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L76)

```python
def get_local_name() -> str:
```

### ImportRecord().is_builtins

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L79)

```python
def is_builtins() -> bool:
```

### ImportRecord().is_internal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L104)

```python
def is_internal() -> bool:
```

### ImportRecord().is_local

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L92)

```python
def is_local() -> bool:
```

### ImportRecord().is_third_party

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L85)

```python
def is_third_party() -> bool:
```

### ImportRecord().is_type_defs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L82)

```python
def is_type_defs() -> bool:
```

### ImportRecord().package_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L51)

```python
@property
def package_name() -> str:
```
