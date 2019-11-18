# ServiceModule

> Auto-generated documentation for [builder.mypy_boto3_builder.structures.service_module](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServiceModule
    - [ServiceModule](#servicemodule)
        - [ServiceModule().extract_typed_dicts](#servicemoduleextract_typed_dicts)
        - [ServiceModule().get_client_required_import_record_groups](#servicemoduleget_client_required_import_record_groups)
        - [ServiceModule().get_helpers_import_record_groups](#servicemoduleget_helpers_import_record_groups)
        - [ServiceModule().get_init_all_names](#servicemoduleget_init_all_names)
        - [ServiceModule().get_init_import_record_groups](#servicemoduleget_init_import_record_groups)
        - [ServiceModule().get_paginator_required_import_record_groups](#servicemoduleget_paginator_required_import_record_groups)
        - [ServiceModule().get_service_resource_required_import_record_groups](#servicemoduleget_service_resource_required_import_record_groups)
        - [ServiceModule().get_type_defs_required_import_record_groups](#servicemoduleget_type_defs_required_import_record_groups)
        - [ServiceModule().get_types](#servicemoduleget_types)
        - [ServiceModule().get_waiter_required_import_record_groups](#servicemoduleget_waiter_required_import_record_groups)

## ServiceModule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L20)

```python
dataclass
class ServiceModule(ModuleRecord):
```

### ServiceModule().extract_typed_dicts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L30)

```python
def extract_typed_dicts(
    type_annotations: Iterable[FakeAnnotation],
    added: Dict[str, TypeTypedDict],
) -> List[TypeTypedDict]:
```

### ServiceModule().get_client_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L103)

```python
def get_client_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_helpers_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L162)

```python
def get_helpers_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_init_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L93)

```python
def get_init_all_names() -> List[str]:
```

### ServiceModule().get_init_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L66)

```python
def get_init_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_paginator_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L130)

```python
def get_paginator_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_service_resource_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L116)

```python
def get_service_resource_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_type_defs_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L150)

```python
def get_type_defs_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L55)

```python
def get_types() -> Set[FakeAnnotation]:
```

### ServiceModule().get_waiter_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_module.py#L140)

```python
def get_waiter_required_import_record_groups() -> List[ImportRecordGroup]:
```
