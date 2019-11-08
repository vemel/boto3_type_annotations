# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.pinpoint_sms_voice.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Pinpoint Sms Voice](index.md#pinpoint-sms-voice) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_configuration_set](#clientcreate_configuration_set)
        - [Client().create_configuration_set_event_destination](#clientcreate_configuration_set_event_destination)
        - [Client().delete_configuration_set](#clientdelete_configuration_set)
        - [Client().delete_configuration_set_event_destination](#clientdelete_configuration_set_event_destination)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_configuration_set_event_destinations](#clientget_configuration_set_event_destinations)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().send_voice_message](#clientsend_voice_message)
        - [Client().update_configuration_set_event_destination](#clientupdate_configuration_set_event_destination)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_configuration_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L18)

```python
def create_configuration_set(
    ConfigurationSetName: str = None,
) -> Dict[str, Any]:
```

### Client().create_configuration_set_event_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L24)

```python
def create_configuration_set_event_destination(
    ConfigurationSetName: str,
    EventDestination: Dict[str, Any] = None,
    EventDestinationName: str = None,
) -> Dict[str, Any]:
```

### Client().delete_configuration_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L33)

```python
def delete_configuration_set(ConfigurationSetName: str) -> Dict[str, Any]:
```

### Client().delete_configuration_set_event_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L37)

```python
def delete_configuration_set_event_destination(
    ConfigurationSetName: str,
    EventDestinationName: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L43)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_configuration_set_event_destinations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L53)

```python
def get_configuration_set_event_destinations(
    ConfigurationSetName: str,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L59)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L63)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().send_voice_message

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L67)

```python
def send_voice_message(
    CallerId: str = None,
    ConfigurationSetName: str = None,
    Content: Dict[str, Any] = None,
    DestinationPhoneNumber: str = None,
    OriginationPhoneNumber: str = None,
) -> Dict[str, Any]:
```

### Client().update_configuration_set_event_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_sms_voice/client.py#L78)

```python
def update_configuration_set_event_destination(
    ConfigurationSetName: str,
    EventDestinationName: str,
    EventDestination: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
