# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.s3control.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [S3control](index.md#s3control) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_job](#clientcreate_job)
        - [Client().delete_public_access_block](#clientdelete_public_access_block)
        - [Client().describe_job](#clientdescribe_job)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_public_access_block](#clientget_public_access_block)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_jobs](#clientlist_jobs)
        - [Client().put_public_access_block](#clientput_public_access_block)
        - [Client().update_job_priority](#clientupdate_job_priority)
        - [Client().update_job_status](#clientupdate_job_status)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L19)

```python
def create_job(
    AccountId: str,
    Operation: Dict[str, Any],
    Report: Dict[str, Any],
    ClientRequestToken: str,
    Manifest: Dict[str, Any],
    Priority: int,
    RoleArn: str,
    ConfirmationRequired: bool = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().delete_public_access_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L34)

```python
def delete_public_access_block(AccountId: str) -> None:
```

### Client().describe_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L38)

```python
def describe_job(AccountId: str, JobId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L42)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L52)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_public_access_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L56)

```python
def get_public_access_block(AccountId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L60)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L64)

```python
def list_jobs(
    AccountId: str,
    JobStatuses: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().put_public_access_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L74)

```python
def put_public_access_block(
    PublicAccessBlockConfiguration: Dict[str, Any],
    AccountId: str,
) -> None:
```

### Client().update_job_priority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L80)

```python
def update_job_priority(
    AccountId: str,
    JobId: str,
    Priority: int,
) -> Dict[str, Any]:
```

### Client().update_job_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3control/client.py#L86)

```python
def update_job_status(
    AccountId: str,
    JobId: str,
    RequestedJobStatus: str,
    StatusUpdateReason: str = None,
) -> Dict[str, Any]:
```
