# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.importexport.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Importexport](index.md#importexport) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_job](#clientcancel_job)
        - [Client().create_job](#clientcreate_job)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_shipping_label](#clientget_shipping_label)
        - [Client().get_status](#clientget_status)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_jobs](#clientlist_jobs)
        - [Client().update_job](#clientupdate_job)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L19)

```python
def cancel_job(JobId: str, APIVersion: str = None) -> Dict[str, Any]:
```

### Client().create_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L23)

```python
def create_job(
    JobType: str,
    Manifest: str,
    ValidateOnly: bool,
    ManifestAddendum: str = None,
    APIVersion: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L34)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L44)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_shipping_label

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L48)

```python
def get_shipping_label(
    jobIds: List[Any],
    name: str = None,
    company: str = None,
    phoneNumber: str = None,
    country: str = None,
    stateOrProvince: str = None,
    city: str = None,
    postalCode: str = None,
    street1: str = None,
    street2: str = None,
    street3: str = None,
    APIVersion: str = None,
) -> Dict[str, Any]:
```

### Client().get_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L66)

```python
def get_status(JobId: str, APIVersion: str = None) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L70)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L74)

```python
def list_jobs(
    MaxJobs: int = None,
    Marker: str = None,
    APIVersion: str = None,
) -> Dict[str, Any]:
```

### Client().update_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/importexport/client.py#L80)

```python
def update_job(
    JobId: str,
    Manifest: str,
    JobType: str,
    ValidateOnly: bool,
    APIVersion: str = None,
) -> Dict[str, Any]:
```
