# Boto3StubsPackage

> Auto-generated documentation for [builder.mypy_boto3_builder.structures.boto3_stubs_package](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/boto3_stubs_package.py) module.

Structure for boto3-stubs module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Boto3StubsPackage
    - [Boto3StubsPackage](#boto3stubspackage)
        - [Boto3StubsPackage().essential_service_names](#boto3stubspackageessential_service_names)
        - [Boto3StubsPackage().get_init_required_import_record_groups](#boto3stubspackageget_init_required_import_record_groups)
        - [Boto3StubsPackage().get_session_required_import_record_groups](#boto3stubspackageget_session_required_import_record_groups)

## Boto3StubsPackage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/boto3_stubs_package.py#L19)

```python
dataclass
class Boto3StubsPackage(Package):
```

Structure for boto3-stubs module.

### Boto3StubsPackage().essential_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/boto3_stubs_package.py#L34)

```python
@property
def essential_service_names() -> List[ServiceName]:
```

### Boto3StubsPackage().get_init_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/boto3_stubs_package.py#L42)

```python
def get_init_required_import_record_groups() -> List[ImportRecordGroup]:
```

### Boto3StubsPackage().get_session_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/boto3_stubs_package.py#L64)

```python
def get_session_required_import_record_groups() -> List[ImportRecordGroup]:
```