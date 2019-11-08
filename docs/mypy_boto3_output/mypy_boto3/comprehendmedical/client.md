# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.comprehendmedical.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Comprehendmedical](index.md#comprehendmedical) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().describe_entities_detection_v2_job](#clientdescribe_entities_detection_v2_job)
        - [Client().describe_phi_detection_job](#clientdescribe_phi_detection_job)
        - [Client().detect_entities](#clientdetect_entities)
        - [Client().detect_entities_v2](#clientdetect_entities_v2)
        - [Client().detect_phi](#clientdetect_phi)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_entities_detection_v2_jobs](#clientlist_entities_detection_v2_jobs)
        - [Client().list_phi_detection_jobs](#clientlist_phi_detection_jobs)
        - [Client().start_entities_detection_v2_job](#clientstart_entities_detection_v2_job)
        - [Client().start_phi_detection_job](#clientstart_phi_detection_job)
        - [Client().stop_entities_detection_v2_job](#clientstop_entities_detection_v2_job)
        - [Client().stop_phi_detection_job](#clientstop_phi_detection_job)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().describe_entities_detection_v2_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L18)

```python
def describe_entities_detection_v2_job(JobId: str) -> Dict[str, Any]:
```

### Client().describe_phi_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L22)

```python
def describe_phi_detection_job(JobId: str) -> Dict[str, Any]:
```

### Client().detect_entities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L26)

```python
def detect_entities(Text: str) -> Dict[str, Any]:
```

### Client().detect_entities_v2

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L30)

```python
def detect_entities_v2(Text: str) -> Dict[str, Any]:
```

### Client().detect_phi

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L34)

```python
def detect_phi(Text: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L38)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L48)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L52)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_entities_detection_v2_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L56)

```python
def list_entities_detection_v2_jobs(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_phi_detection_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L65)

```python
def list_phi_detection_jobs(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().start_entities_detection_v2_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L74)

```python
def start_entities_detection_v2_job(
    InputDataConfig: Dict[str, Any],
    OutputDataConfig: Dict[str, Any],
    DataAccessRoleArn: str,
    LanguageCode: str,
    JobName: str = None,
    ClientRequestToken: str = None,
    KMSKey: str = None,
) -> Dict[str, Any]:
```

### Client().start_phi_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L87)

```python
def start_phi_detection_job(
    InputDataConfig: Dict[str, Any],
    OutputDataConfig: Dict[str, Any],
    DataAccessRoleArn: str,
    LanguageCode: str,
    JobName: str = None,
    ClientRequestToken: str = None,
    KMSKey: str = None,
) -> Dict[str, Any]:
```

### Client().stop_entities_detection_v2_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L100)

```python
def stop_entities_detection_v2_job(JobId: str) -> Dict[str, Any]:
```

### Client().stop_phi_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehendmedical/client.py#L104)

```python
def stop_phi_detection_job(JobId: str) -> Dict[str, Any]:
```
