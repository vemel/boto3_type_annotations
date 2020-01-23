# ExternalImport

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.external_import](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/external_import.py) module.

Wrapper for type annotations imported from 3rd party libraries, like `boto3.service.Service`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / ExternalImport
    - [ExternalImport](#externalimport)
        - [ExternalImport().copy](#externalimportcopy)
        - [ExternalImport().get_import_record](#externalimportget_import_record)
        - [ExternalImport().render](#externalimportrender)

## ExternalImport

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/external_import.py#L9)

```python
class ExternalImport(FakeAnnotation):
    def __init__(
        source: ImportString,
        name: str = '',
        alias: str = '',
    ) -> None:
```

Wrapper for type annotations imported from 3rd party libraries, like
`boto3.service.Service`.

#### Arguments

- `source` - Module import string.
- `name` - Import name.
- `alias` - Import local name.

### ExternalImport().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/external_import.py#L41)

```python
def copy() -> 'ExternalImport':
```

Create a copy of type annotation wrapper.

### ExternalImport().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/external_import.py#L35)

```python
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

### ExternalImport().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/external_import.py#L26)

```python
def render(parent_name: str = '') -> str:
```

Get string with local name to use.

#### Returns

Import record local name.
