# InternalImport

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.internal_import](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py) module.

Wrapper for simple type annotations from this module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / InternalImport
    - [InternalImport](#internalimport)
        - [InternalImport().copy](#internalimportcopy)
        - [InternalImport().get_import_record](#internalimportget_import_record)
        - [InternalImport().render](#internalimportrender)
        - [InternalImport().scope](#internalimportscope)

## InternalImport

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py#L16)

```python
class InternalImport(FakeAnnotation):
    def __init__(
        name: str,
        service_name: Optional[ServiceName] = None,
        module_name: ServiceModuleName = ServiceModuleName.service_resource,
    ) -> None:
```

Wrapper for simple type annotations from this module.

#### Arguments

- `name` - Import name.
- `service_name` - Service that import belongs to.
- `module_name` - Service module name.

### InternalImport().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py#L62)

```python
def copy() -> 'InternalImport':
```

Create a copy of type annotation wrapper.

### InternalImport().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py#L49)

```python
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

### InternalImport().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py#L36)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

### InternalImport().scope

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py#L45)

```python
@property
def scope() -> str:
```
