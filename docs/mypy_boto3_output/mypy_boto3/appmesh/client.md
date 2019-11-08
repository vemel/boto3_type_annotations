# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.appmesh.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Appmesh](index.md#appmesh) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_mesh](#clientcreate_mesh)
        - [Client().create_route](#clientcreate_route)
        - [Client().create_virtual_node](#clientcreate_virtual_node)
        - [Client().create_virtual_router](#clientcreate_virtual_router)
        - [Client().create_virtual_service](#clientcreate_virtual_service)
        - [Client().delete_mesh](#clientdelete_mesh)
        - [Client().delete_route](#clientdelete_route)
        - [Client().delete_virtual_node](#clientdelete_virtual_node)
        - [Client().delete_virtual_router](#clientdelete_virtual_router)
        - [Client().delete_virtual_service](#clientdelete_virtual_service)
        - [Client().describe_mesh](#clientdescribe_mesh)
        - [Client().describe_route](#clientdescribe_route)
        - [Client().describe_virtual_node](#clientdescribe_virtual_node)
        - [Client().describe_virtual_router](#clientdescribe_virtual_router)
        - [Client().describe_virtual_service](#clientdescribe_virtual_service)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_meshes](#clientlist_meshes)
        - [Client().list_routes](#clientlist_routes)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_virtual_nodes](#clientlist_virtual_nodes)
        - [Client().list_virtual_routers](#clientlist_virtual_routers)
        - [Client().list_virtual_services](#clientlist_virtual_services)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_mesh](#clientupdate_mesh)
        - [Client().update_route](#clientupdate_route)
        - [Client().update_virtual_node](#clientupdate_virtual_node)
        - [Client().update_virtual_router](#clientupdate_virtual_router)
        - [Client().update_virtual_service](#clientupdate_virtual_service)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_mesh

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L19)

```python
def create_mesh(
    meshName: str,
    clientToken: str = None,
    spec: Dict[str, Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L29)

```python
def create_route(
    meshName: str,
    routeName: str,
    spec: Dict[str, Any],
    virtualRouterName: str,
    clientToken: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_virtual_node

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L41)

```python
def create_virtual_node(
    meshName: str,
    spec: Dict[str, Any],
    virtualNodeName: str,
    clientToken: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_virtual_router

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L52)

```python
def create_virtual_router(
    meshName: str,
    spec: Dict[str, Any],
    virtualRouterName: str,
    clientToken: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_virtual_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L63)

```python
def create_virtual_service(
    meshName: str,
    spec: Dict[str, Any],
    virtualServiceName: str,
    clientToken: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_mesh

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L74)

```python
def delete_mesh(meshName: str) -> Dict[str, Any]:
```

### Client().delete_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L78)

```python
def delete_route(
    meshName: str,
    routeName: str,
    virtualRouterName: str,
) -> Dict[str, Any]:
```

### Client().delete_virtual_node

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L84)

```python
def delete_virtual_node(
    meshName: str,
    virtualNodeName: str,
) -> Dict[str, Any]:
```

### Client().delete_virtual_router

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L90)

```python
def delete_virtual_router(
    meshName: str,
    virtualRouterName: str,
) -> Dict[str, Any]:
```

### Client().delete_virtual_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L96)

```python
def delete_virtual_service(
    meshName: str,
    virtualServiceName: str,
) -> Dict[str, Any]:
```

### Client().describe_mesh

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L102)

```python
def describe_mesh(meshName: str) -> Dict[str, Any]:
```

### Client().describe_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L106)

```python
def describe_route(
    meshName: str,
    routeName: str,
    virtualRouterName: str,
) -> Dict[str, Any]:
```

### Client().describe_virtual_node

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L112)

```python
def describe_virtual_node(
    meshName: str,
    virtualNodeName: str,
) -> Dict[str, Any]:
```

### Client().describe_virtual_router

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L118)

```python
def describe_virtual_router(
    meshName: str,
    virtualRouterName: str,
) -> Dict[str, Any]:
```

### Client().describe_virtual_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L124)

```python
def describe_virtual_service(
    meshName: str,
    virtualServiceName: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L130)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L140)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L144)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_meshes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L148)

```python
def list_meshes(limit: int = None, nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_routes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L152)

```python
def list_routes(
    meshName: str,
    virtualRouterName: str,
    limit: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L162)

```python
def list_tags_for_resource(
    resourceArn: str,
    limit: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_virtual_nodes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L168)

```python
def list_virtual_nodes(
    meshName: str,
    limit: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_virtual_routers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L174)

```python
def list_virtual_routers(
    meshName: str,
    limit: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_virtual_services

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L180)

```python
def list_virtual_services(
    meshName: str,
    limit: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L186)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L190)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_mesh

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L194)

```python
def update_mesh(
    meshName: str,
    clientToken: str = None,
    spec: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L200)

```python
def update_route(
    meshName: str,
    routeName: str,
    spec: Dict[str, Any],
    virtualRouterName: str,
    clientToken: str = None,
) -> Dict[str, Any]:
```

### Client().update_virtual_node

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L211)

```python
def update_virtual_node(
    meshName: str,
    spec: Dict[str, Any],
    virtualNodeName: str,
    clientToken: str = None,
) -> Dict[str, Any]:
```

### Client().update_virtual_router

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L221)

```python
def update_virtual_router(
    meshName: str,
    spec: Dict[str, Any],
    virtualRouterName: str,
    clientToken: str = None,
) -> Dict[str, Any]:
```

### Client().update_virtual_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appmesh/client.py#L231)

```python
def update_virtual_service(
    meshName: str,
    spec: Dict[str, Any],
    virtualServiceName: str,
    clientToken: str = None,
) -> Dict[str, Any]:
```
