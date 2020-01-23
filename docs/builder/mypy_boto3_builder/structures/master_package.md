# MasterPackage

> Auto-generated documentation for [builder.mypy_boto3_builder.structures.master_package](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/master_package.py) module.

Structure for boto3-stubs module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / MasterPackage
    - [MasterPackage](#masterpackage)
        - [MasterPackage().essential_service_names](#masterpackageessential_service_names)

## MasterPackage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/master_package.py#L14)

```python
dataclass
class MasterPackage(Package):
```

Structure for mypy-boto3 package.

### MasterPackage().essential_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/master_package.py#L25)

```python
@property
def essential_service_names() -> List[ServiceName]:
```
