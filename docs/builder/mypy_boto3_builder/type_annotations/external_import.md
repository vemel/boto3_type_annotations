# ExternalImport

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.external_import](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/external_import.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / ExternalImport
    - [ExternalImport](#externalimport)
        - [ExternalImport().copy](#externalimportcopy)
        - [ExternalImport().get_import_record](#externalimportget_import_record)
        - [ExternalImport().render](#externalimportrender)

## ExternalImport

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/external_import.py#L7)

```python
class ExternalImport(FakeAnnotation):
    def __init__(source: str, name: str = '', alias: str = '') -> None:
```

### ExternalImport().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/external_import.py#L20)

```python
def copy() -> ExternalImport:
```

### ExternalImport().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/external_import.py#L17)

```python
def get_import_record() -> ImportRecord:
```

### ExternalImport().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/external_import.py#L14)

```python
def render() -> str:
```
