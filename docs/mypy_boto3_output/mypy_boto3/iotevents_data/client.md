# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iotevents_data.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents_data/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iotevents Data](index.md#iotevents-data) / Client
    - [Client](#client)
        - [Client().batch_put_message](#clientbatch_put_message)
        - [Client().batch_update_detector](#clientbatch_update_detector)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().describe_detector](#clientdescribe_detector)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_detectors](#clientlist_detectors)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents_data/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_put_message

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents_data/client.py#L15)

```python
def batch_put_message(messages: List[Any]) -> Dict[str, Any]:
```

### Client().batch_update_detector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents_data/client.py#L19)

```python
def batch_update_detector(detectors: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents_data/client.py#L23)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().describe_detector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents_data/client.py#L27)

```python
def describe_detector(
    detectorModelName: str,
    keyValue: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents_data/client.py#L33)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents_data/client.py#L43)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents_data/client.py#L47)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_detectors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents_data/client.py#L51)

```python
def list_detectors(
    detectorModelName: str,
    stateName: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```
