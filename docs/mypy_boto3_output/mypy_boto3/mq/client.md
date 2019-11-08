# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mq.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mq](index.md#mq) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_broker](#clientcreate_broker)
        - [Client().create_configuration](#clientcreate_configuration)
        - [Client().create_tags](#clientcreate_tags)
        - [Client().create_user](#clientcreate_user)
        - [Client().delete_broker](#clientdelete_broker)
        - [Client().delete_tags](#clientdelete_tags)
        - [Client().delete_user](#clientdelete_user)
        - [Client().describe_broker](#clientdescribe_broker)
        - [Client().describe_broker_engine_types](#clientdescribe_broker_engine_types)
        - [Client().describe_broker_instance_options](#clientdescribe_broker_instance_options)
        - [Client().describe_configuration](#clientdescribe_configuration)
        - [Client().describe_configuration_revision](#clientdescribe_configuration_revision)
        - [Client().describe_user](#clientdescribe_user)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_brokers](#clientlist_brokers)
        - [Client().list_configuration_revisions](#clientlist_configuration_revisions)
        - [Client().list_configurations](#clientlist_configurations)
        - [Client().list_tags](#clientlist_tags)
        - [Client().list_users](#clientlist_users)
        - [Client().reboot_broker](#clientreboot_broker)
        - [Client().update_broker](#clientupdate_broker)
        - [Client().update_configuration](#clientupdate_configuration)
        - [Client().update_user](#clientupdate_user)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_broker

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L19)

```python
def create_broker(
    AutoMinorVersionUpgrade: bool = None,
    BrokerName: str = None,
    Configuration: Dict[str, Any] = None,
    CreatorRequestId: str = None,
    DeploymentMode: str = None,
    EncryptionOptions: Dict[str, Any] = None,
    EngineType: str = None,
    EngineVersion: str = None,
    HostInstanceType: str = None,
    Logs: Dict[str, Any] = None,
    MaintenanceWindowStartTime: Dict[str, Any] = None,
    PubliclyAccessible: bool = None,
    SecurityGroups: List[Any] = None,
    SubnetIds: List[Any] = None,
    Tags: Dict[str, Any] = None,
    Users: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L41)

```python
def create_configuration(
    EngineType: str = None,
    EngineVersion: str = None,
    Name: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L51)

```python
def create_tags(ResourceArn: str, Tags: Dict[str, Any] = None) -> None:
```

### Client().create_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L55)

```python
def create_user(
    BrokerId: str,
    Username: str,
    ConsoleAccess: bool = None,
    Groups: List[Any] = None,
    Password: str = None,
) -> Dict[str, Any]:
```

### Client().delete_broker

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L66)

```python
def delete_broker(BrokerId: str) -> Dict[str, Any]:
```

### Client().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L70)

```python
def delete_tags(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L74)

```python
def delete_user(BrokerId: str, Username: str) -> Dict[str, Any]:
```

### Client().describe_broker

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L78)

```python
def describe_broker(BrokerId: str) -> Dict[str, Any]:
```

### Client().describe_broker_engine_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L82)

```python
def describe_broker_engine_types(
    EngineType: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_broker_instance_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L88)

```python
def describe_broker_instance_options(
    EngineType: str = None,
    HostInstanceType: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L98)

```python
def describe_configuration(ConfigurationId: str) -> Dict[str, Any]:
```

### Client().describe_configuration_revision

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L102)

```python
def describe_configuration_revision(
    ConfigurationId: str,
    ConfigurationRevision: str,
) -> Dict[str, Any]:
```

### Client().describe_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L108)

```python
def describe_user(BrokerId: str, Username: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L112)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L122)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L126)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_brokers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L130)

```python
def list_brokers(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_configuration_revisions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L136)

```python
def list_configuration_revisions(
    ConfigurationId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L142)

```python
def list_configurations(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L148)

```python
def list_tags(ResourceArn: str) -> Dict[str, Any]:
```

### Client().list_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L152)

```python
def list_users(
    BrokerId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().reboot_broker

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L158)

```python
def reboot_broker(BrokerId: str) -> Dict[str, Any]:
```

### Client().update_broker

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L162)

```python
def update_broker(
    BrokerId: str,
    AutoMinorVersionUpgrade: bool = None,
    Configuration: Dict[str, Any] = None,
    EngineVersion: str = None,
    HostInstanceType: str = None,
    Logs: Dict[str, Any] = None,
    SecurityGroups: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L175)

```python
def update_configuration(
    ConfigurationId: str,
    Data: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().update_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mq/client.py#L181)

```python
def update_user(
    BrokerId: str,
    Username: str,
    ConsoleAccess: bool = None,
    Groups: List[Any] = None,
    Password: str = None,
) -> Dict[str, Any]:
```
