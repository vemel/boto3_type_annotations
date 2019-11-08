# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mediastore.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mediastore](index.md#mediastore) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_container](#clientcreate_container)
        - [Client().delete_container](#clientdelete_container)
        - [Client().delete_container_policy](#clientdelete_container_policy)
        - [Client().delete_cors_policy](#clientdelete_cors_policy)
        - [Client().delete_lifecycle_policy](#clientdelete_lifecycle_policy)
        - [Client().describe_container](#clientdescribe_container)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_container_policy](#clientget_container_policy)
        - [Client().get_cors_policy](#clientget_cors_policy)
        - [Client().get_lifecycle_policy](#clientget_lifecycle_policy)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_containers](#clientlist_containers)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_container_policy](#clientput_container_policy)
        - [Client().put_cors_policy](#clientput_cors_policy)
        - [Client().put_lifecycle_policy](#clientput_lifecycle_policy)
        - [Client().start_access_logging](#clientstart_access_logging)
        - [Client().stop_access_logging](#clientstop_access_logging)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_container

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L19)

```python
def create_container(
    ContainerName: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_container

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L25)

```python
def delete_container(ContainerName: str) -> Dict[str, Any]:
```

### Client().delete_container_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L29)

```python
def delete_container_policy(ContainerName: str) -> Dict[str, Any]:
```

### Client().delete_cors_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L33)

```python
def delete_cors_policy(ContainerName: str) -> Dict[str, Any]:
```

### Client().delete_lifecycle_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L37)

```python
def delete_lifecycle_policy(ContainerName: str) -> Dict[str, Any]:
```

### Client().describe_container

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L41)

```python
def describe_container(ContainerName: str = None) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L45)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_container_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L55)

```python
def get_container_policy(ContainerName: str) -> Dict[str, Any]:
```

### Client().get_cors_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L59)

```python
def get_cors_policy(ContainerName: str) -> Dict[str, Any]:
```

### Client().get_lifecycle_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L63)

```python
def get_lifecycle_policy(ContainerName: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L67)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L71)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_containers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L75)

```python
def list_containers(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L81)

```python
def list_tags_for_resource(Resource: str) -> Dict[str, Any]:
```

### Client().put_container_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L85)

```python
def put_container_policy(ContainerName: str, Policy: str) -> Dict[str, Any]:
```

### Client().put_cors_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L89)

```python
def put_cors_policy(
    ContainerName: str,
    CorsPolicy: List[Any],
) -> Dict[str, Any]:
```

### Client().put_lifecycle_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L95)

```python
def put_lifecycle_policy(
    ContainerName: str,
    LifecyclePolicy: str,
) -> Dict[str, Any]:
```

### Client().start_access_logging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L101)

```python
def start_access_logging(ContainerName: str) -> Dict[str, Any]:
```

### Client().stop_access_logging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L105)

```python
def stop_access_logging(ContainerName: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L109)

```python
def tag_resource(Resource: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore/client.py#L113)

```python
def untag_resource(Resource: str, TagKeys: List[Any]) -> Dict[str, Any]:
```
