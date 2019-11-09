# Renderer

> Auto-generated documentation for [builder.mypy_boto3_builder.import_helpers.renderer](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/renderer.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / Renderer
    - [ImportRecordRenderer](#importrecordrenderer)
        - [ImportRecordRenderer().generate_lines](#importrecordrenderergenerate_lines)
        - [ImportRecordRenderer().get_localized](#importrecordrendererget_localized)

## ImportRecordRenderer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/renderer.py#L12)

```python
class ImportRecordRenderer():
    def __init__(
        module_name: str,
        default_import_records: Iterable[ImportRecord] = (),
    ) -> None:
```

### ImportRecordRenderer().generate_lines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/renderer.py#L68)

```python
def generate_lines(
    import_records: Iterable[ImportRecord] = (),
    type_annotations: Iterable[TypeAnnotation] = (),
) -> Generator[str, None, None]:
```

### ImportRecordRenderer().get_localized

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/import_helpers/renderer.py#L60)

```python
def get_localized(import_record: ImportRecord) -> ImportRecord:
```
