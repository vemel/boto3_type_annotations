# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iotevents.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iotevents](index.md#iotevents) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_detector_model](#clientcreate_detector_model)
        - [Client().create_input](#clientcreate_input)
        - [Client().delete_detector_model](#clientdelete_detector_model)
        - [Client().delete_input](#clientdelete_input)
        - [Client().describe_detector_model](#clientdescribe_detector_model)
        - [Client().describe_input](#clientdescribe_input)
        - [Client().describe_logging_options](#clientdescribe_logging_options)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_detector_model_versions](#clientlist_detector_model_versions)
        - [Client().list_detector_models](#clientlist_detector_models)
        - [Client().list_inputs](#clientlist_inputs)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_logging_options](#clientput_logging_options)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_detector_model](#clientupdate_detector_model)
        - [Client().update_input](#clientupdate_input)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_detector_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L19)

```python
def create_detector_model(
    detectorModelName: str,
    detectorModelDefinition: Dict[str, Any],
    roleArn: str,
    detectorModelDescription: str = None,
    key: str = None,
    tags: List[Any] = None,
    evaluationMethod: str = None,
) -> Dict[str, Any]:
```

### Client().create_input

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L32)

```python
def create_input(
    inputName: str,
    inputDefinition: Dict[str, Any],
    inputDescription: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_detector_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L42)

```python
def delete_detector_model(detectorModelName: str) -> Dict[str, Any]:
```

### Client().delete_input

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L46)

```python
def delete_input(inputName: str) -> Dict[str, Any]:
```

### Client().describe_detector_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L50)

```python
def describe_detector_model(
    detectorModelName: str,
    detectorModelVersion: str = None,
) -> Dict[str, Any]:
```

### Client().describe_input

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L56)

```python
def describe_input(inputName: str) -> Dict[str, Any]:
```

### Client().describe_logging_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L60)

```python
def describe_logging_options() -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L64)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L74)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L78)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_detector_model_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L82)

```python
def list_detector_model_versions(
    detectorModelName: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_detector_models

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L88)

```python
def list_detector_models(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_inputs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L94)

```python
def list_inputs(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L100)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().put_logging_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L104)

```python
def put_logging_options(loggingOptions: Dict[str, Any]) -> None:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L108)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L112)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_detector_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L116)

```python
def update_detector_model(
    detectorModelName: str,
    detectorModelDefinition: Dict[str, Any],
    roleArn: str,
    detectorModelDescription: str = None,
    evaluationMethod: str = None,
) -> Dict[str, Any]:
```

### Client().update_input

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotevents/client.py#L127)

```python
def update_input(
    inputName: str,
    inputDefinition: Dict[str, Any],
    inputDescription: str = None,
) -> Dict[str, Any]:
```
