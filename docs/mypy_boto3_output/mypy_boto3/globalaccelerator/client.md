# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.globalaccelerator.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Globalaccelerator](index.md#globalaccelerator) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_accelerator](#clientcreate_accelerator)
        - [Client().create_endpoint_group](#clientcreate_endpoint_group)
        - [Client().create_listener](#clientcreate_listener)
        - [Client().delete_accelerator](#clientdelete_accelerator)
        - [Client().delete_endpoint_group](#clientdelete_endpoint_group)
        - [Client().delete_listener](#clientdelete_listener)
        - [Client().describe_accelerator](#clientdescribe_accelerator)
        - [Client().describe_accelerator_attributes](#clientdescribe_accelerator_attributes)
        - [Client().describe_endpoint_group](#clientdescribe_endpoint_group)
        - [Client().describe_listener](#clientdescribe_listener)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_accelerators](#clientlist_accelerators)
        - [Client().list_endpoint_groups](#clientlist_endpoint_groups)
        - [Client().list_listeners](#clientlist_listeners)
        - [Client().update_accelerator](#clientupdate_accelerator)
        - [Client().update_accelerator_attributes](#clientupdate_accelerator_attributes)
        - [Client().update_endpoint_group](#clientupdate_endpoint_group)
        - [Client().update_listener](#clientupdate_listener)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_accelerator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L19)

```python
def create_accelerator(
    Name: str,
    IdempotencyToken: str,
    IpAddressType: str = None,
    Enabled: bool = None,
) -> Dict[str, Any]:
```

### Client().create_endpoint_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L29)

```python
def create_endpoint_group(
    ListenerArn: str,
    EndpointGroupRegion: str,
    IdempotencyToken: str,
    EndpointConfigurations: List[Any] = None,
    TrafficDialPercentage: float = None,
    HealthCheckPort: int = None,
    HealthCheckProtocol: str = None,
    HealthCheckPath: str = None,
    HealthCheckIntervalSeconds: int = None,
    ThresholdCount: int = None,
) -> Dict[str, Any]:
```

### Client().create_listener

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L45)

```python
def create_listener(
    AcceleratorArn: str,
    PortRanges: List[Any],
    Protocol: str,
    IdempotencyToken: str,
    ClientAffinity: str = None,
) -> Dict[str, Any]:
```

### Client().delete_accelerator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L56)

```python
def delete_accelerator(AcceleratorArn: str) -> None:
```

### Client().delete_endpoint_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L60)

```python
def delete_endpoint_group(EndpointGroupArn: str) -> None:
```

### Client().delete_listener

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L64)

```python
def delete_listener(ListenerArn: str) -> None:
```

### Client().describe_accelerator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L68)

```python
def describe_accelerator(AcceleratorArn: str) -> Dict[str, Any]:
```

### Client().describe_accelerator_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L72)

```python
def describe_accelerator_attributes(AcceleratorArn: str) -> Dict[str, Any]:
```

### Client().describe_endpoint_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L76)

```python
def describe_endpoint_group(EndpointGroupArn: str) -> Dict[str, Any]:
```

### Client().describe_listener

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L80)

```python
def describe_listener(ListenerArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L84)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L94)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L98)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_accelerators

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L102)

```python
def list_accelerators(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_endpoint_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L108)

```python
def list_endpoint_groups(
    ListenerArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_listeners

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L114)

```python
def list_listeners(
    AcceleratorArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().update_accelerator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L120)

```python
def update_accelerator(
    AcceleratorArn: str,
    Name: str = None,
    IpAddressType: str = None,
    Enabled: bool = None,
) -> Dict[str, Any]:
```

### Client().update_accelerator_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L130)

```python
def update_accelerator_attributes(
    AcceleratorArn: str,
    FlowLogsEnabled: bool = None,
    FlowLogsS3Bucket: str = None,
    FlowLogsS3Prefix: str = None,
) -> Dict[str, Any]:
```

### Client().update_endpoint_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L140)

```python
def update_endpoint_group(
    EndpointGroupArn: str,
    EndpointConfigurations: List[Any] = None,
    TrafficDialPercentage: float = None,
    HealthCheckPort: int = None,
    HealthCheckProtocol: str = None,
    HealthCheckPath: str = None,
    HealthCheckIntervalSeconds: int = None,
    ThresholdCount: int = None,
) -> Dict[str, Any]:
```

### Client().update_listener

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/client.py#L154)

```python
def update_listener(
    ListenerArn: str,
    PortRanges: List[Any] = None,
    Protocol: str = None,
    ClientAffinity: str = None,
) -> Dict[str, Any]:
```
