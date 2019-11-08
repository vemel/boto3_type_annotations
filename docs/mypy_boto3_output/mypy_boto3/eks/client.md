# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.eks.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Eks](index.md#eks) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_cluster](#clientcreate_cluster)
        - [Client().delete_cluster](#clientdelete_cluster)
        - [Client().describe_cluster](#clientdescribe_cluster)
        - [Client().describe_update](#clientdescribe_update)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_clusters](#clientlist_clusters)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_updates](#clientlist_updates)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_cluster_config](#clientupdate_cluster_config)
        - [Client().update_cluster_version](#clientupdate_cluster_version)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L19)

```python
def create_cluster(
    name: str,
    roleArn: str,
    resourcesVpcConfig: Dict[str, Any],
    version: str = None,
    logging: Dict[str, Any] = None,
    clientRequestToken: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L32)

```python
def delete_cluster(name: str) -> Dict[str, Any]:
```

### Client().describe_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L36)

```python
def describe_cluster(name: str) -> Dict[str, Any]:
```

### Client().describe_update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L40)

```python
def describe_update(name: str, updateId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L44)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L54)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L58)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L62)

```python
def list_clusters(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L68)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().list_updates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L72)

```python
def list_updates(
    name: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L78)

```python
def tag_resource(resourceArn: str, tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L82)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_cluster_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L86)

```python
def update_cluster_config(
    name: str,
    resourcesVpcConfig: Dict[str, Any] = None,
    logging: Dict[str, Any] = None,
    clientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().update_cluster_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/client.py#L96)

```python
def update_cluster_version(
    name: str,
    version: str,
    clientRequestToken: str = None,
) -> Dict[str, Any]:
```
