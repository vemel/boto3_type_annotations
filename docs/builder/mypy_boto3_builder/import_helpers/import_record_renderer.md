# ImportRecordRenderer

> Auto-generated documentation for [builder.mypy_boto3_builder.import_helpers.import_record_renderer](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record_renderer.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / ImportRecordRenderer
    - [ImportRecordRenderer](#importrecordrenderer)
        - [ImportRecordRenderer().generate_lines](#importrecordrenderergenerate_lines)

## ImportRecordRenderer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record_renderer.py#L9)

```python
class ImportRecordRenderer():
    def __init__(
        local_modules: Iterable[str],
        common_import_records: Iterable[ImportRecord] = (),
    ) -> None:
```

### ImportRecordRenderer().generate_lines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/import_record_renderer.py#L40)

```python
def generate_lines(
    type_annotations: Iterable[FakeAnnotation] = (),
) -> Generator[str, None, None]:
```
