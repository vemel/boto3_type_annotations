# ServiceResource

> Auto-generated documentation for [builder.mypy_boto3_builder.structures.service_resource](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_resource.py) module.

Boto3 ServiceResource.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServiceResource
    - [ServiceResource](#serviceresource)
        - [ServiceResource().get_all_names](#serviceresourceget_all_names)
        - [ServiceResource().get_collections](#serviceresourceget_collections)
        - [ServiceResource().get_import_records](#serviceresourceget_import_records)
        - [ServiceResource().get_types](#serviceresourceget_types)

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_resource.py#L18)

```python
dataclass
class ServiceResource(ClassRecord):
```

Boto3 ServiceResource.

### ServiceResource().get_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_resource.py#L61)

```python
def get_all_names() -> List[str]:
```

### ServiceResource().get_collections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_resource.py#L69)

```python
def get_collections() -> List[Collection]:
```

### ServiceResource().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_resource.py#L51)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/service_resource.py#L42)

```python
def get_types() -> Set[FakeAnnotation]:
```
