# ImportRecordGroup

> Auto-generated documentation for [builder.mypy_boto3_builder.import_helpers.import_record_group](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record_group.py) module.

Grouped by `source` import records for nicer rendering.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / ImportRecordGroup
    - [ImportRecordGroup](#importrecordgroup)
        - [ImportRecordGroup.from_import_records](#importrecordgroupfrom_import_records)
        - [ImportRecordGroup().is_builtins](#importrecordgroupis_builtins)

## ImportRecordGroup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record_group.py#L12)

```python
class ImportRecordGroup():
    def __init__(
        source: ImportString,
        import_records: Iterable[ImportRecord],
    ) -> None:
```

Grouped by `source` import records for nicer rendering.

#### Arguments

- `source` - Common source for import records.
- `import_records` - Grouped import records.

### ImportRecordGroup.from_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record_group.py#L27)

```python
@classmethod
def from_import_records(
    import_records: Iterable[ImportRecord],
) -> List[ImportRecordGroup]:
```

Get groups from `ImportRecord` list.

#### Arguments

- `import_records` - Import records list.

#### Returns

A list of generated [ImportRecordGroup](#importrecordgroup).

### ImportRecordGroup().is_builtins

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record_group.py#L56)

```python
def is_builtins() -> bool:
```
