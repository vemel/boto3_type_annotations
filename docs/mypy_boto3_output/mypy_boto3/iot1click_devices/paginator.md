# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iot1click_devices.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iot1click Devices](index.md#iot1click-devices) / Paginator
    - [ListDeviceEvents](#listdeviceevents)
        - [ListDeviceEvents().paginate](#listdeviceeventspaginate)
    - [ListDevices](#listdevices)
        - [ListDevices().paginate](#listdevicespaginate)

## ListDeviceEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/paginator.py#L10)

```python
class ListDeviceEvents(Paginator):
```

### ListDeviceEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/paginator.py#L13)

```python
def paginate(
    DeviceId: str,
    FromTimeStamp: datetime,
    ToTimeStamp: datetime,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDevices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/paginator.py#L23)

```python
class ListDevices(Paginator):
```

### ListDevices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_devices/paginator.py#L26)

```python
def paginate(
    DeviceType: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
