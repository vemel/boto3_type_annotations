# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.opsworkscm.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Opsworkscm](index.md#opsworkscm) / Client
    - [Client](#client)
        - [Client().associate_node](#clientassociate_node)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_backup](#clientcreate_backup)
        - [Client().create_server](#clientcreate_server)
        - [Client().delete_backup](#clientdelete_backup)
        - [Client().delete_server](#clientdelete_server)
        - [Client().describe_account_attributes](#clientdescribe_account_attributes)
        - [Client().describe_backups](#clientdescribe_backups)
        - [Client().describe_events](#clientdescribe_events)
        - [Client().describe_node_association_status](#clientdescribe_node_association_status)
        - [Client().describe_servers](#clientdescribe_servers)
        - [Client().disassociate_node](#clientdisassociate_node)
        - [Client().export_server_engine_attribute](#clientexport_server_engine_attribute)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().restore_server](#clientrestore_server)
        - [Client().start_maintenance](#clientstart_maintenance)
        - [Client().update_server](#clientupdate_server)
        - [Client().update_server_engine_attributes](#clientupdate_server_engine_attributes)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_node

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L15)

```python
def associate_node(
    ServerName: str,
    NodeName: str,
    EngineAttributes: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L21)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L25)

```python
def create_backup(ServerName: str, Description: str = None) -> Dict[str, Any]:
```

### Client().create_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L29)

```python
def create_server(
    ServerName: str,
    InstanceProfileArn: str,
    InstanceType: str,
    ServiceRoleArn: str,
    AssociatePublicIpAddress: bool = None,
    CustomDomain: str = None,
    CustomCertificate: str = None,
    CustomPrivateKey: str = None,
    DisableAutomatedBackup: bool = None,
    Engine: str = None,
    EngineModel: str = None,
    EngineVersion: str = None,
    EngineAttributes: List[Any] = None,
    BackupRetentionCount: int = None,
    KeyPair: str = None,
    PreferredMaintenanceWindow: str = None,
    PreferredBackupWindow: str = None,
    SecurityGroupIds: List[Any] = None,
    SubnetIds: List[Any] = None,
    BackupId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L55)

```python
def delete_backup(BackupId: str) -> Dict[str, Any]:
```

### Client().delete_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L59)

```python
def delete_server(ServerName: str) -> Dict[str, Any]:
```

### Client().describe_account_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L63)

```python
def describe_account_attributes() -> Dict[str, Any]:
```

### Client().describe_backups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L67)

```python
def describe_backups(
    BackupId: str = None,
    ServerName: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L77)

```python
def describe_events(
    ServerName: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_node_association_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L83)

```python
def describe_node_association_status(
    NodeAssociationStatusToken: str,
    ServerName: str,
) -> Dict[str, Any]:
```

### Client().describe_servers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L89)

```python
def describe_servers(
    ServerName: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().disassociate_node

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L95)

```python
def disassociate_node(
    ServerName: str,
    NodeName: str,
    EngineAttributes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().export_server_engine_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L101)

```python
def export_server_engine_attribute(
    ExportAttributeName: str,
    ServerName: str,
    InputAttributes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L110)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L120)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L124)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().restore_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L128)

```python
def restore_server(
    BackupId: str,
    ServerName: str,
    InstanceType: str = None,
    KeyPair: str = None,
) -> Dict[str, Any]:
```

### Client().start_maintenance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L138)

```python
def start_maintenance(
    ServerName: str,
    EngineAttributes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L144)

```python
def update_server(
    ServerName: str,
    DisableAutomatedBackup: bool = None,
    BackupRetentionCount: int = None,
    PreferredMaintenanceWindow: str = None,
    PreferredBackupWindow: str = None,
) -> Dict[str, Any]:
```

### Client().update_server_engine_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/client.py#L155)

```python
def update_server_engine_attributes(
    ServerName: str,
    AttributeName: str,
    AttributeValue: str = None,
) -> Dict[str, Any]:
```
