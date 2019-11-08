# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.efs.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Efs](index.md#efs) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_file_system](#clientcreate_file_system)
        - [Client().create_mount_target](#clientcreate_mount_target)
        - [Client().create_tags](#clientcreate_tags)
        - [Client().delete_file_system](#clientdelete_file_system)
        - [Client().delete_mount_target](#clientdelete_mount_target)
        - [Client().delete_tags](#clientdelete_tags)
        - [Client().describe_file_systems](#clientdescribe_file_systems)
        - [Client().describe_lifecycle_configuration](#clientdescribe_lifecycle_configuration)
        - [Client().describe_mount_target_security_groups](#clientdescribe_mount_target_security_groups)
        - [Client().describe_mount_targets](#clientdescribe_mount_targets)
        - [Client().describe_tags](#clientdescribe_tags)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().modify_mount_target_security_groups](#clientmodify_mount_target_security_groups)
        - [Client().put_lifecycle_configuration](#clientput_lifecycle_configuration)
        - [Client().update_file_system](#clientupdate_file_system)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_file_system

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L19)

```python
def create_file_system(
    CreationToken: str,
    PerformanceMode: str = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
    ThroughputMode: str = None,
    ProvisionedThroughputInMibps: float = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_mount_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L32)

```python
def create_mount_target(
    FileSystemId: str,
    SubnetId: str,
    IpAddress: str = None,
    SecurityGroups: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L42)

```python
def create_tags(FileSystemId: str, Tags: List[Any]) -> None:
```

### Client().delete_file_system

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L46)

```python
def delete_file_system(FileSystemId: str) -> None:
```

### Client().delete_mount_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L50)

```python
def delete_mount_target(MountTargetId: str) -> None:
```

### Client().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L54)

```python
def delete_tags(FileSystemId: str, TagKeys: List[Any]) -> None:
```

### Client().describe_file_systems

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L58)

```python
def describe_file_systems(
    MaxItems: int = None,
    Marker: str = None,
    CreationToken: str = None,
    FileSystemId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_lifecycle_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L68)

```python
def describe_lifecycle_configuration(FileSystemId: str) -> Dict[str, Any]:
```

### Client().describe_mount_target_security_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L72)

```python
def describe_mount_target_security_groups(
    MountTargetId: str,
) -> Dict[str, Any]:
```

### Client().describe_mount_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L78)

```python
def describe_mount_targets(
    MaxItems: int = None,
    Marker: str = None,
    FileSystemId: str = None,
    MountTargetId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L88)

```python
def describe_tags(
    FileSystemId: str,
    MaxItems: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L94)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L104)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L108)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().modify_mount_target_security_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L112)

```python
def modify_mount_target_security_groups(
    MountTargetId: str,
    SecurityGroups: List[Any] = None,
) -> None:
```

### Client().put_lifecycle_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L118)

```python
def put_lifecycle_configuration(
    FileSystemId: str,
    LifecyclePolicies: List[Any],
) -> Dict[str, Any]:
```

### Client().update_file_system

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/client.py#L124)

```python
def update_file_system(
    FileSystemId: str,
    ThroughputMode: str = None,
    ProvisionedThroughputInMibps: float = None,
) -> Dict[str, Any]:
```
