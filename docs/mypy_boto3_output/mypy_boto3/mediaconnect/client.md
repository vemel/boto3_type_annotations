# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mediaconnect.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mediaconnect](index.md#mediaconnect) / Client
    - [Client](#client)
        - [Client().add_flow_outputs](#clientadd_flow_outputs)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_flow](#clientcreate_flow)
        - [Client().delete_flow](#clientdelete_flow)
        - [Client().describe_flow](#clientdescribe_flow)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().grant_flow_entitlements](#clientgrant_flow_entitlements)
        - [Client().list_entitlements](#clientlist_entitlements)
        - [Client().list_flows](#clientlist_flows)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().remove_flow_output](#clientremove_flow_output)
        - [Client().revoke_flow_entitlement](#clientrevoke_flow_entitlement)
        - [Client().start_flow](#clientstart_flow)
        - [Client().stop_flow](#clientstop_flow)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_flow_entitlement](#clientupdate_flow_entitlement)
        - [Client().update_flow_output](#clientupdate_flow_output)
        - [Client().update_flow_source](#clientupdate_flow_source)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_flow_outputs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L15)

```python
def add_flow_outputs(FlowArn: str, Outputs: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_flow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L23)

```python
def create_flow(
    Name: str,
    Source: Dict[str, Any],
    AvailabilityZone: str = None,
    Entitlements: List[Any] = None,
    Outputs: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_flow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L34)

```python
def delete_flow(FlowArn: str) -> Dict[str, Any]:
```

### Client().describe_flow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L38)

```python
def describe_flow(FlowArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L42)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L52)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L56)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().grant_flow_entitlements

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L60)

```python
def grant_flow_entitlements(
    Entitlements: List[Any],
    FlowArn: str,
) -> Dict[str, Any]:
```

### Client().list_entitlements

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L66)

```python
def list_entitlements(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_flows

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L72)

```python
def list_flows(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L78)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().remove_flow_output

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L82)

```python
def remove_flow_output(FlowArn: str, OutputArn: str) -> Dict[str, Any]:
```

### Client().revoke_flow_entitlement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L86)

```python
def revoke_flow_entitlement(
    EntitlementArn: str,
    FlowArn: str,
) -> Dict[str, Any]:
```

### Client().start_flow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L92)

```python
def start_flow(FlowArn: str) -> Dict[str, Any]:
```

### Client().stop_flow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L96)

```python
def stop_flow(FlowArn: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L100)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L104)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().update_flow_entitlement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L108)

```python
def update_flow_entitlement(
    EntitlementArn: str,
    FlowArn: str,
    Description: str = None,
    Encryption: Dict[str, Any] = None,
    Subscribers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_flow_output

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L119)

```python
def update_flow_output(
    FlowArn: str,
    OutputArn: str,
    CidrAllowList: List[Any] = None,
    Description: str = None,
    Destination: str = None,
    Encryption: Dict[str, Any] = None,
    MaxLatency: int = None,
    Port: int = None,
    Protocol: str = None,
    RemoteId: str = None,
    SmoothingLatency: int = None,
    StreamId: str = None,
) -> Dict[str, Any]:
```

### Client().update_flow_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconnect/client.py#L137)

```python
def update_flow_source(
    FlowArn: str,
    SourceArn: str,
    Decryption: Dict[str, Any] = None,
    Description: str = None,
    EntitlementArn: str = None,
    IngestPort: int = None,
    MaxBitrate: int = None,
    MaxLatency: int = None,
    Protocol: str = None,
    StreamId: str = None,
    WhitelistCidr: str = None,
) -> Dict[str, Any]:
```
