# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloud9.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloud9](index.md#cloud9) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_environment_ec2](#clientcreate_environment_ec2)
        - [Client().create_environment_membership](#clientcreate_environment_membership)
        - [Client().delete_environment](#clientdelete_environment)
        - [Client().delete_environment_membership](#clientdelete_environment_membership)
        - [Client().describe_environment_memberships](#clientdescribe_environment_memberships)
        - [Client().describe_environment_status](#clientdescribe_environment_status)
        - [Client().describe_environments](#clientdescribe_environments)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_environments](#clientlist_environments)
        - [Client().update_environment](#clientupdate_environment)
        - [Client().update_environment_membership](#clientupdate_environment_membership)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_environment_ec2

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L19)

```python
def create_environment_ec2(
    name: str,
    instanceType: str,
    description: str = None,
    clientRequestToken: str = None,
    subnetId: str = None,
    automaticStopTimeMinutes: int = None,
    ownerArn: str = None,
) -> Dict[str, Any]:
```

### Client().create_environment_membership

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L32)

```python
def create_environment_membership(
    environmentId: str,
    userArn: str,
    permissions: str,
) -> Dict[str, Any]:
```

### Client().delete_environment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L38)

```python
def delete_environment(environmentId: str) -> Dict[str, Any]:
```

### Client().delete_environment_membership

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L42)

```python
def delete_environment_membership(
    environmentId: str,
    userArn: str,
) -> Dict[str, Any]:
```

### Client().describe_environment_memberships

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L48)

```python
def describe_environment_memberships(
    userArn: str = None,
    environmentId: str = None,
    permissions: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_environment_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L59)

```python
def describe_environment_status(environmentId: str) -> Dict[str, Any]:
```

### Client().describe_environments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L63)

```python
def describe_environments(environmentIds: List[Any]) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L67)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L77)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L81)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_environments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L85)

```python
def list_environments(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().update_environment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L91)

```python
def update_environment(
    environmentId: str,
    name: str = None,
    description: str = None,
) -> Dict[str, Any]:
```

### Client().update_environment_membership

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/client.py#L97)

```python
def update_environment_membership(
    environmentId: str,
    userArn: str,
    permissions: str,
) -> Dict[str, Any]:
```
