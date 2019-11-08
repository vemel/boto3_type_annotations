# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.medialive.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Medialive](index.md#medialive) / Client
    - [Client](#client)
        - [Client().batch_update_schedule](#clientbatch_update_schedule)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_channel](#clientcreate_channel)
        - [Client().create_input](#clientcreate_input)
        - [Client().create_input_security_group](#clientcreate_input_security_group)
        - [Client().create_tags](#clientcreate_tags)
        - [Client().delete_channel](#clientdelete_channel)
        - [Client().delete_input](#clientdelete_input)
        - [Client().delete_input_security_group](#clientdelete_input_security_group)
        - [Client().delete_reservation](#clientdelete_reservation)
        - [Client().delete_schedule](#clientdelete_schedule)
        - [Client().delete_tags](#clientdelete_tags)
        - [Client().describe_channel](#clientdescribe_channel)
        - [Client().describe_input](#clientdescribe_input)
        - [Client().describe_input_security_group](#clientdescribe_input_security_group)
        - [Client().describe_offering](#clientdescribe_offering)
        - [Client().describe_reservation](#clientdescribe_reservation)
        - [Client().describe_schedule](#clientdescribe_schedule)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_channels](#clientlist_channels)
        - [Client().list_input_security_groups](#clientlist_input_security_groups)
        - [Client().list_inputs](#clientlist_inputs)
        - [Client().list_offerings](#clientlist_offerings)
        - [Client().list_reservations](#clientlist_reservations)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().purchase_offering](#clientpurchase_offering)
        - [Client().start_channel](#clientstart_channel)
        - [Client().stop_channel](#clientstop_channel)
        - [Client().update_channel](#clientupdate_channel)
        - [Client().update_channel_class](#clientupdate_channel_class)
        - [Client().update_input](#clientupdate_input)
        - [Client().update_input_security_group](#clientupdate_input_security_group)
        - [Client().update_reservation](#clientupdate_reservation)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_update_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L15)

```python
def batch_update_schedule(
    ChannelId: str,
    Creates: Dict[str, Any] = None,
    Deletes: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L24)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L28)

```python
def create_channel(
    ChannelClass: str = None,
    Destinations: List[Any] = None,
    EncoderSettings: Dict[str, Any] = None,
    InputAttachments: List[Any] = None,
    InputSpecification: Dict[str, Any] = None,
    LogLevel: str = None,
    Name: str = None,
    RequestId: str = None,
    Reserved: str = None,
    RoleArn: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_input

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L45)

```python
def create_input(
    Destinations: List[Any] = None,
    InputSecurityGroups: List[Any] = None,
    MediaConnectFlows: List[Any] = None,
    Name: str = None,
    RequestId: str = None,
    RoleArn: str = None,
    Sources: List[Any] = None,
    Tags: Dict[str, Any] = None,
    Type: str = None,
    Vpc: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_input_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L61)

```python
def create_input_security_group(
    Tags: Dict[str, Any] = None,
    WhitelistRules: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L67)

```python
def create_tags(ResourceArn: str, Tags: Dict[str, Any] = None) -> None:
```

### Client().delete_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L71)

```python
def delete_channel(ChannelId: str) -> Dict[str, Any]:
```

### Client().delete_input

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L75)

```python
def delete_input(InputId: str) -> Dict[str, Any]:
```

### Client().delete_input_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L79)

```python
def delete_input_security_group(InputSecurityGroupId: str) -> Dict[str, Any]:
```

### Client().delete_reservation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L83)

```python
def delete_reservation(ReservationId: str) -> Dict[str, Any]:
```

### Client().delete_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L87)

```python
def delete_schedule(ChannelId: str) -> Dict[str, Any]:
```

### Client().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L91)

```python
def delete_tags(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().describe_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L95)

```python
def describe_channel(ChannelId: str) -> Dict[str, Any]:
```

### Client().describe_input

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L99)

```python
def describe_input(InputId: str) -> Dict[str, Any]:
```

### Client().describe_input_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L103)

```python
def describe_input_security_group(
    InputSecurityGroupId: str,
) -> Dict[str, Any]:
```

### Client().describe_offering

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L109)

```python
def describe_offering(OfferingId: str) -> Dict[str, Any]:
```

### Client().describe_reservation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L113)

```python
def describe_reservation(ReservationId: str) -> Dict[str, Any]:
```

### Client().describe_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L117)

```python
def describe_schedule(
    ChannelId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L123)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L133)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L137)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_channels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L141)

```python
def list_channels(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_input_security_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L147)

```python
def list_input_security_groups(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_inputs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L153)

```python
def list_inputs(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_offerings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L159)

```python
def list_offerings(
    ChannelClass: str = None,
    ChannelConfiguration: str = None,
    Codec: str = None,
    MaxResults: int = None,
    MaximumBitrate: str = None,
    MaximumFramerate: str = None,
    NextToken: str = None,
    Resolution: str = None,
    ResourceType: str = None,
    SpecialFeature: str = None,
    VideoQuality: str = None,
) -> Dict[str, Any]:
```

### Client().list_reservations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L176)

```python
def list_reservations(
    ChannelClass: str = None,
    Codec: str = None,
    MaxResults: int = None,
    MaximumBitrate: str = None,
    MaximumFramerate: str = None,
    NextToken: str = None,
    Resolution: str = None,
    ResourceType: str = None,
    SpecialFeature: str = None,
    VideoQuality: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L192)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().purchase_offering

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L196)

```python
def purchase_offering(
    Count: int,
    OfferingId: str,
    Name: str = None,
    RequestId: str = None,
    Start: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().start_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L208)

```python
def start_channel(ChannelId: str) -> Dict[str, Any]:
```

### Client().stop_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L212)

```python
def stop_channel(ChannelId: str) -> Dict[str, Any]:
```

### Client().update_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L216)

```python
def update_channel(
    ChannelId: str,
    Destinations: List[Any] = None,
    EncoderSettings: Dict[str, Any] = None,
    InputAttachments: List[Any] = None,
    InputSpecification: Dict[str, Any] = None,
    LogLevel: str = None,
    Name: str = None,
    RoleArn: str = None,
) -> Dict[str, Any]:
```

### Client().update_channel_class

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L230)

```python
def update_channel_class(
    ChannelClass: str,
    ChannelId: str,
    Destinations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_input

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L236)

```python
def update_input(
    InputId: str,
    Destinations: List[Any] = None,
    InputSecurityGroups: List[Any] = None,
    MediaConnectFlows: List[Any] = None,
    Name: str = None,
    RoleArn: str = None,
    Sources: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_input_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L249)

```python
def update_input_security_group(
    InputSecurityGroupId: str,
    Tags: Dict[str, Any] = None,
    WhitelistRules: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_reservation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/client.py#L258)

```python
def update_reservation(
    ReservationId: str,
    Name: str = None,
) -> Dict[str, Any]:
```
