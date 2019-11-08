# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudhsmv2.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudhsmv2](index.md#cloudhsmv2) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().copy_backup_to_region](#clientcopy_backup_to_region)
        - [Client().create_cluster](#clientcreate_cluster)
        - [Client().create_hsm](#clientcreate_hsm)
        - [Client().delete_backup](#clientdelete_backup)
        - [Client().delete_cluster](#clientdelete_cluster)
        - [Client().delete_hsm](#clientdelete_hsm)
        - [Client().describe_backups](#clientdescribe_backups)
        - [Client().describe_clusters](#clientdescribe_clusters)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().initialize_cluster](#clientinitialize_cluster)
        - [Client().list_tags](#clientlist_tags)
        - [Client().restore_backup](#clientrestore_backup)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().copy_backup_to_region

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L19)

```python
def copy_backup_to_region(
    DestinationRegion: str,
    BackupId: str,
) -> Dict[str, Any]:
```

### Client().create_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L25)

```python
def create_cluster(
    SubnetIds: List[Any],
    HsmType: str,
    SourceBackupId: str = None,
) -> Dict[str, Any]:
```

### Client().create_hsm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L31)

```python
def create_hsm(
    ClusterId: str,
    AvailabilityZone: str,
    IpAddress: str = None,
) -> Dict[str, Any]:
```

### Client().delete_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L37)

```python
def delete_backup(BackupId: str) -> Dict[str, Any]:
```

### Client().delete_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L41)

```python
def delete_cluster(ClusterId: str) -> Dict[str, Any]:
```

### Client().delete_hsm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L45)

```python
def delete_hsm(
    ClusterId: str,
    HsmId: str = None,
    EniId: str = None,
    EniIp: str = None,
) -> Dict[str, Any]:
```

### Client().describe_backups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L51)

```python
def describe_backups(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: Dict[str, Any] = None,
    SortAscending: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L61)

```python
def describe_clusters(
    Filters: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L70)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L80)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L84)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().initialize_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L88)

```python
def initialize_cluster(
    ClusterId: str,
    SignedCert: str,
    TrustAnchor: str,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L94)

```python
def list_tags(
    ResourceId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().restore_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L100)

```python
def restore_backup(BackupId: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L104)

```python
def tag_resource(ResourceId: str, TagList: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/client.py#L108)

```python
def untag_resource(ResourceId: str, TagKeyList: List[Any]) -> Dict[str, Any]:
```
