# ImportRecord

> Auto-generated documentation for [builder.mypy_boto3_builder.import_helpers.import_record](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / ImportRecord
    - [ImportRecord](#importrecord)
        - [ImportRecord().get_local_name](#importrecordget_local_name)
        - [ImportRecord().render](#importrecordrender)

## ImportRecord

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L9)

```python
dataclass
class ImportRecord():
    def __init__(source: str, name: str = '', alias: str = '') -> None:
```

### ImportRecord().get_local_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L43)

```python
def get_local_name() -> str:
```

### ImportRecord().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record.py#L40)

```python
def render() -> str:
```
