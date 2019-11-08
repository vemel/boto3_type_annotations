# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.fsx.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Fsx](index.md#fsx) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_backup](#clientcreate_backup)
        - [Client().create_file_system](#clientcreate_file_system)
        - [Client().create_file_system_from_backup](#clientcreate_file_system_from_backup)
        - [Client().delete_backup](#clientdelete_backup)
        - [Client().delete_file_system](#clientdelete_file_system)
        - [Client().describe_backups](#clientdescribe_backups)
        - [Client().describe_file_systems](#clientdescribe_file_systems)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_file_system](#clientupdate_file_system)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L19)

```python
def create_backup(
    FileSystemId: str,
    ClientRequestToken: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_file_system

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L25)

```python
def create_file_system(
    FileSystemType: str,
    StorageCapacity: int,
    SubnetIds: List[Any],
    ClientRequestToken: str = None,
    SecurityGroupIds: List[Any] = None,
    Tags: List[Any] = None,
    KmsKeyId: str = None,
    WindowsConfiguration: Dict[str, Any] = None,
    LustreConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_file_system_from_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L40)

```python
def create_file_system_from_backup(
    BackupId: str,
    SubnetIds: List[Any],
    ClientRequestToken: str = None,
    SecurityGroupIds: List[Any] = None,
    Tags: List[Any] = None,
    WindowsConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L52)

```python
def delete_backup(
    BackupId: str,
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().delete_file_system

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L58)

```python
def delete_file_system(
    FileSystemId: str,
    ClientRequestToken: str = None,
    WindowsConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_backups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L67)

```python
def describe_backups(
    BackupIds: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_file_systems

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L77)

```python
def describe_file_systems(
    FileSystemIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L86)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L96)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L100)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L104)

```python
def list_tags_for_resource(
    ResourceARN: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L110)

```python
def tag_resource(ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L114)

```python
def untag_resource(ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_file_system

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/client.py#L118)

```python
def update_file_system(
    FileSystemId: str,
    ClientRequestToken: str = None,
    WindowsConfiguration: Dict[str, Any] = None,
    LustreConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
