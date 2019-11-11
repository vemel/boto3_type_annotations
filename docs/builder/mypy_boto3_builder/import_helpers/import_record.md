# ImportRecord

> Auto-generated documentation for [builder.mypy_boto3_builder.import_helpers.import_record](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / ImportRecord
    - [ImportRecord](#importrecord)
        - [ImportRecord().get_local_name](#importrecordget_local_name)
        - [ImportRecord().is_builtins](#importrecordis_builtins)
        - [ImportRecord().is_local](#importrecordis_local)
        - [ImportRecord().is_third_party](#importrecordis_third_party)
        - [ImportRecord().package_name](#importrecordpackage_name)
        - [ImportRecord().render](#importrecordrender)

## ImportRecord

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L11)

```python
dataclass
total_ordering
class ImportRecord():
    def __init__(source: str, name: str = '', alias: str = '') -> None:
```

### ImportRecord().get_local_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L77)

```python
def get_local_name() -> str:
```

### ImportRecord().is_builtins

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L80)

```python
def is_builtins() -> bool:
```

### ImportRecord().is_local

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L90)

```python
def is_local() -> bool:
```

### ImportRecord().is_third_party

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L83)

```python
def is_third_party() -> bool:
```

### ImportRecord().package_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L49)

```python
@property
def package_name() -> str:
```

### ImportRecord().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L74)

```python
def render() -> str:
```
