# ServicePackage

> Auto-generated documentation for [builder.mypy_boto3_builder.structures.service_package](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServicePackage
    - [ServicePackage](#servicepackage)
        - [ServicePackage().extract_typed_dicts](#servicepackageextract_typed_dicts)
        - [ServicePackage().get_client_required_import_record_groups](#servicepackageget_client_required_import_record_groups)
        - [ServicePackage().get_helpers_import_record_groups](#servicepackageget_helpers_import_record_groups)
        - [ServicePackage().get_init_all_names](#servicepackageget_init_all_names)
        - [ServicePackage().get_init_import_record_groups](#servicepackageget_init_import_record_groups)
        - [ServicePackage().get_paginator_required_import_record_groups](#servicepackageget_paginator_required_import_record_groups)
        - [ServicePackage().get_service_resource_required_import_record_groups](#servicepackageget_service_resource_required_import_record_groups)
        - [ServicePackage().get_type_defs_required_import_record_groups](#servicepackageget_type_defs_required_import_record_groups)
        - [ServicePackage().get_types](#servicepackageget_types)
        - [ServicePackage().get_waiter_required_import_record_groups](#servicepackageget_waiter_required_import_record_groups)

## ServicePackage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L19)

```python
dataclass
class ServicePackage(Package):
```

### ServicePackage().extract_typed_dicts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L29)

```python
def extract_typed_dicts(
    type_annotations: Iterable[FakeAnnotation],
    added: Dict[str, TypeTypedDict],
) -> List[TypeTypedDict]:
```

### ServicePackage().get_client_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L139)

```python
def get_client_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_helpers_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L208)

```python
def get_helpers_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_init_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L125)

```python
def get_init_all_names() -> List[str]:
```

### ServicePackage().get_init_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L65)

```python
def get_init_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_paginator_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L166)

```python
def get_paginator_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_service_resource_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L152)

```python
def get_service_resource_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_type_defs_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L186)

```python
def get_type_defs_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L54)

```python
def get_types() -> Set[FakeAnnotation]:
```

### ServicePackage().get_waiter_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_package.py#L176)

```python
def get_waiter_required_import_record_groups() -> List[ImportRecordGroup]:
```
