# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.snowball.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Snowball](index.md#snowball) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_cluster](#clientcancel_cluster)
        - [Client().cancel_job](#clientcancel_job)
        - [Client().create_address](#clientcreate_address)
        - [Client().create_cluster](#clientcreate_cluster)
        - [Client().create_job](#clientcreate_job)
        - [Client().describe_address](#clientdescribe_address)
        - [Client().describe_addresses](#clientdescribe_addresses)
        - [Client().describe_cluster](#clientdescribe_cluster)
        - [Client().describe_job](#clientdescribe_job)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_job_manifest](#clientget_job_manifest)
        - [Client().get_job_unlock_code](#clientget_job_unlock_code)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_snowball_usage](#clientget_snowball_usage)
        - [Client().get_software_updates](#clientget_software_updates)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_cluster_jobs](#clientlist_cluster_jobs)
        - [Client().list_clusters](#clientlist_clusters)
        - [Client().list_compatible_images](#clientlist_compatible_images)
        - [Client().list_jobs](#clientlist_jobs)
        - [Client().update_cluster](#clientupdate_cluster)
        - [Client().update_job](#clientupdate_job)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L18)

```python
def cancel_cluster(ClusterId: str) -> Dict[str, Any]:
```

### Client().cancel_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L22)

```python
def cancel_job(JobId: str) -> Dict[str, Any]:
```

### Client().create_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L26)

```python
def create_address(Address: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().create_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L30)

```python
def create_cluster(
    JobType: str,
    Resources: Dict[str, Any],
    AddressId: str,
    RoleARN: str,
    ShippingOption: str,
    Description: str = None,
    KmsKeyARN: str = None,
    SnowballType: str = None,
    Notification: Dict[str, Any] = None,
    ForwardingAddressId: str = None,
) -> Dict[str, Any]:
```

### Client().create_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L46)

```python
def create_job(
    JobType: str = None,
    Resources: Dict[str, Any] = None,
    Description: str = None,
    AddressId: str = None,
    KmsKeyARN: str = None,
    RoleARN: str = None,
    SnowballCapacityPreference: str = None,
    ShippingOption: str = None,
    Notification: Dict[str, Any] = None,
    ClusterId: str = None,
    SnowballType: str = None,
    ForwardingAddressId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L64)

```python
def describe_address(AddressId: str) -> Dict[str, Any]:
```

### Client().describe_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L68)

```python
def describe_addresses(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L74)

```python
def describe_cluster(ClusterId: str) -> Dict[str, Any]:
```

### Client().describe_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L78)

```python
def describe_job(JobId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L82)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_job_manifest

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L92)

```python
def get_job_manifest(JobId: str) -> Dict[str, Any]:
```

### Client().get_job_unlock_code

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L96)

```python
def get_job_unlock_code(JobId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L100)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_snowball_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L104)

```python
def get_snowball_usage() -> Dict[str, Any]:
```

### Client().get_software_updates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L108)

```python
def get_software_updates(JobId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L112)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_cluster_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L116)

```python
def list_cluster_jobs(
    ClusterId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L122)

```python
def list_clusters(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_compatible_images

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L128)

```python
def list_compatible_images(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L134)

```python
def list_jobs(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().update_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L140)

```python
def update_cluster(
    ClusterId: str,
    RoleARN: str = None,
    Description: str = None,
    Resources: Dict[str, Any] = None,
    AddressId: str = None,
    ShippingOption: str = None,
    Notification: Dict[str, Any] = None,
    ForwardingAddressId: str = None,
) -> Dict[str, Any]:
```

### Client().update_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/client.py#L154)

```python
def update_job(
    JobId: str,
    RoleARN: str = None,
    Notification: Dict[str, Any] = None,
    Resources: Dict[str, Any] = None,
    AddressId: str = None,
    ShippingOption: str = None,
    Description: str = None,
    SnowballCapacityPreference: str = None,
    ForwardingAddressId: str = None,
) -> Dict[str, Any]:
```
