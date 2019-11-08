# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iot1click_devices.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iot1click Devices](index.md#iot1click-devices) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().claim_devices_by_claim_code](#clientclaim_devices_by_claim_code)
        - [Client().describe_device](#clientdescribe_device)
        - [Client().finalize_device_claim](#clientfinalize_device_claim)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_device_methods](#clientget_device_methods)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().initiate_device_claim](#clientinitiate_device_claim)
        - [Client().invoke_device_method](#clientinvoke_device_method)
        - [Client().list_device_events](#clientlist_device_events)
        - [Client().list_devices](#clientlist_devices)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().unclaim_device](#clientunclaim_device)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_device_state](#clientupdate_device_state)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().claim_devices_by_claim_code

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L20)

```python
def claim_devices_by_claim_code(ClaimCode: str) -> Dict[str, Any]:
```

### Client().describe_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L24)

```python
def describe_device(DeviceId: str) -> Dict[str, Any]:
```

### Client().finalize_device_claim

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L28)

```python
def finalize_device_claim(
    DeviceId: str,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L34)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_device_methods

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L44)

```python
def get_device_methods(DeviceId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L48)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L52)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().initiate_device_claim

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L56)

```python
def initiate_device_claim(DeviceId: str) -> Dict[str, Any]:
```

### Client().invoke_device_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L60)

```python
def invoke_device_method(
    DeviceId: str,
    DeviceMethod: Dict[str, Any] = None,
    DeviceMethodParameters: str = None,
) -> Dict[str, Any]:
```

### Client().list_device_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L69)

```python
def list_device_events(
    DeviceId: str,
    FromTimeStamp: datetime,
    ToTimeStamp: datetime,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L80)

```python
def list_devices(
    DeviceType: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L86)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L90)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> None:
```

### Client().unclaim_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L94)

```python
def unclaim_device(DeviceId: str) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L98)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().update_device_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/client.py#L102)

```python
def update_device_state(
    DeviceId: str,
    Enabled: bool = None,
) -> Dict[str, Any]:
```
