# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kafka.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kafka](index.md#kafka) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_cluster](#clientcreate_cluster)
        - [Client().create_configuration](#clientcreate_configuration)
        - [Client().delete_cluster](#clientdelete_cluster)
        - [Client().describe_cluster](#clientdescribe_cluster)
        - [Client().describe_cluster_operation](#clientdescribe_cluster_operation)
        - [Client().describe_configuration](#clientdescribe_configuration)
        - [Client().describe_configuration_revision](#clientdescribe_configuration_revision)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_bootstrap_brokers](#clientget_bootstrap_brokers)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_cluster_operations](#clientlist_cluster_operations)
        - [Client().list_clusters](#clientlist_clusters)
        - [Client().list_configuration_revisions](#clientlist_configuration_revisions)
        - [Client().list_configurations](#clientlist_configurations)
        - [Client().list_nodes](#clientlist_nodes)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_broker_count](#clientupdate_broker_count)
        - [Client().update_broker_storage](#clientupdate_broker_storage)
        - [Client().update_cluster_configuration](#clientupdate_cluster_configuration)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L19)

```python
def create_cluster(
    BrokerNodeGroupInfo: Dict[str, Any],
    ClusterName: str,
    KafkaVersion: str,
    NumberOfBrokerNodes: int,
    ClientAuthentication: Dict[str, Any] = None,
    ConfigurationInfo: Dict[str, Any] = None,
    EncryptionInfo: Dict[str, Any] = None,
    EnhancedMonitoring: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L34)

```python
def create_configuration(
    KafkaVersions: List[Any],
    Name: str,
    ServerProperties: bytes,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().delete_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L44)

```python
def delete_cluster(
    ClusterArn: str,
    CurrentVersion: str = None,
) -> Dict[str, Any]:
```

### Client().describe_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L50)

```python
def describe_cluster(ClusterArn: str) -> Dict[str, Any]:
```

### Client().describe_cluster_operation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L54)

```python
def describe_cluster_operation(ClusterOperationArn: str) -> Dict[str, Any]:
```

### Client().describe_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L58)

```python
def describe_configuration(Arn: str) -> Dict[str, Any]:
```

### Client().describe_configuration_revision

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L62)

```python
def describe_configuration_revision(
    Arn: str,
    Revision: int,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L68)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_bootstrap_brokers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L78)

```python
def get_bootstrap_brokers(ClusterArn: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L82)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L86)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_cluster_operations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L90)

```python
def list_cluster_operations(
    ClusterArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L96)

```python
def list_clusters(
    ClusterNameFilter: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_configuration_revisions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L105)

```python
def list_configuration_revisions(
    Arn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L111)

```python
def list_configurations(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_nodes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L117)

```python
def list_nodes(
    ClusterArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L123)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L127)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L131)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().update_broker_count

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L135)

```python
def update_broker_count(
    ClusterArn: str,
    CurrentVersion: str,
    TargetNumberOfBrokerNodes: int,
) -> Dict[str, Any]:
```

### Client().update_broker_storage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L141)

```python
def update_broker_storage(
    ClusterArn: str,
    CurrentVersion: str,
    TargetBrokerEBSVolumeInfo: List[Any],
) -> Dict[str, Any]:
```

### Client().update_cluster_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/client.py#L147)

```python
def update_cluster_configuration(
    ClusterArn: str,
    ConfigurationInfo: Dict[str, Any],
    CurrentVersion: str,
) -> Dict[str, Any]:
```
