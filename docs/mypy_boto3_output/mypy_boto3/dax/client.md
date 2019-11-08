# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dax.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dax](index.md#dax) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_cluster](#clientcreate_cluster)
        - [Client().create_parameter_group](#clientcreate_parameter_group)
        - [Client().create_subnet_group](#clientcreate_subnet_group)
        - [Client().decrease_replication_factor](#clientdecrease_replication_factor)
        - [Client().delete_cluster](#clientdelete_cluster)
        - [Client().delete_parameter_group](#clientdelete_parameter_group)
        - [Client().delete_subnet_group](#clientdelete_subnet_group)
        - [Client().describe_clusters](#clientdescribe_clusters)
        - [Client().describe_default_parameters](#clientdescribe_default_parameters)
        - [Client().describe_events](#clientdescribe_events)
        - [Client().describe_parameter_groups](#clientdescribe_parameter_groups)
        - [Client().describe_parameters](#clientdescribe_parameters)
        - [Client().describe_subnet_groups](#clientdescribe_subnet_groups)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().increase_replication_factor](#clientincrease_replication_factor)
        - [Client().list_tags](#clientlist_tags)
        - [Client().reboot_node](#clientreboot_node)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_cluster](#clientupdate_cluster)
        - [Client().update_parameter_group](#clientupdate_parameter_group)
        - [Client().update_subnet_group](#clientupdate_subnet_group)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L20)

```python
def create_cluster(
    ClusterName: str,
    NodeType: str,
    ReplicationFactor: int,
    IamRoleArn: str,
    Description: str = None,
    AvailabilityZones: List[Any] = None,
    SubnetGroupName: str = None,
    SecurityGroupIds: List[Any] = None,
    PreferredMaintenanceWindow: str = None,
    NotificationTopicArn: str = None,
    ParameterGroupName: str = None,
    Tags: List[Any] = None,
    SSESpecification: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L39)

```python
def create_parameter_group(
    ParameterGroupName: str,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().create_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L45)

```python
def create_subnet_group(
    SubnetGroupName: str,
    SubnetIds: List[Any],
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().decrease_replication_factor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L51)

```python
def decrease_replication_factor(
    ClusterName: str,
    NewReplicationFactor: int,
    AvailabilityZones: List[Any] = None,
    NodeIdsToRemove: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L61)

```python
def delete_cluster(ClusterName: str) -> Dict[str, Any]:
```

### Client().delete_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L65)

```python
def delete_parameter_group(ParameterGroupName: str) -> Dict[str, Any]:
```

### Client().delete_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L69)

```python
def delete_subnet_group(SubnetGroupName: str) -> Dict[str, Any]:
```

### Client().describe_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L73)

```python
def describe_clusters(
    ClusterNames: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_default_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L82)

```python
def describe_default_parameters(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L88)

```python
def describe_events(
    SourceName: str = None,
    SourceType: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_parameter_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L101)

```python
def describe_parameter_groups(
    ParameterGroupNames: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L110)

```python
def describe_parameters(
    ParameterGroupName: str,
    Source: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_subnet_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L120)

```python
def describe_subnet_groups(
    SubnetGroupNames: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L129)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L139)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L143)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().increase_replication_factor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L147)

```python
def increase_replication_factor(
    ClusterName: str,
    NewReplicationFactor: int,
    AvailabilityZones: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L156)

```python
def list_tags(ResourceName: str, NextToken: str = None) -> Dict[str, Any]:
```

### Client().reboot_node

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L160)

```python
def reboot_node(ClusterName: str, NodeId: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L164)

```python
def tag_resource(ResourceName: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L168)

```python
def untag_resource(ResourceName: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L172)

```python
def update_cluster(
    ClusterName: str,
    Description: str = None,
    PreferredMaintenanceWindow: str = None,
    NotificationTopicArn: str = None,
    NotificationTopicStatus: str = None,
    ParameterGroupName: str = None,
    SecurityGroupIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L185)

```python
def update_parameter_group(
    ParameterGroupName: str,
    ParameterNameValues: List[Any],
) -> Dict[str, Any]:
```

### Client().update_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/client.py#L191)

```python
def update_subnet_group(
    SubnetGroupName: str,
    Description: str = None,
    SubnetIds: List[Any] = None,
) -> Dict[str, Any]:
```
