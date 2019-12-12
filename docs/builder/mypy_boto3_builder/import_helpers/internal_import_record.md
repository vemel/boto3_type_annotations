# InternalImportRecord

> Auto-generated documentation for [builder.mypy_boto3_builder.import_helpers.internal_import_record](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/internal_import_record.py) module.

Helper for Python import strings with not set master module name.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / InternalImportRecord
    - [InternalImportRecord](#internalimportrecord)
        - [InternalImportRecord().get_external](#internalimportrecordget_external)

## InternalImportRecord

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/internal_import_record.py#L9)

```python
class InternalImportRecord(ImportRecord):
    def __init__(
        service_module_name: ServiceModuleName,
        name: str = '',
        alias: str = '',
    ):
```

Helper for Python import strings with not set master module name.

#### Arguments

- `service_module_name` - Service module name.
- `name` - Import name.
- `alias` - Import local name.

### InternalImportRecord().get_external

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/internal_import_record.py#L24)

```python
def get_external(module_name: str) -> ImportRecord:
```

Get full import record with `module_name` set as master module.

#### Arguments

- `module_name` - Master module import string.

#### Returns

A new non-internal ImportRecord.
