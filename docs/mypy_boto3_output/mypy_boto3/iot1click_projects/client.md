# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iot1click_projects.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iot1click Projects](index.md#iot1click-projects) / Client
    - [Client](#client)
        - [Client().associate_device_with_placement](#clientassociate_device_with_placement)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_placement](#clientcreate_placement)
        - [Client().create_project](#clientcreate_project)
        - [Client().delete_placement](#clientdelete_placement)
        - [Client().delete_project](#clientdelete_project)
        - [Client().describe_placement](#clientdescribe_placement)
        - [Client().describe_project](#clientdescribe_project)
        - [Client().disassociate_device_from_placement](#clientdisassociate_device_from_placement)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_devices_in_placement](#clientget_devices_in_placement)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_placements](#clientlist_placements)
        - [Client().list_projects](#clientlist_projects)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_placement](#clientupdate_placement)
        - [Client().update_project](#clientupdate_project)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_device_with_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L15)

```python
def associate_device_with_placement(
    projectName: str,
    placementName: str,
    deviceId: str,
    deviceTemplateName: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L25)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L29)

```python
def create_placement(
    placementName: str,
    projectName: str,
    attributes: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L35)

```python
def create_project(
    projectName: str,
    description: str = None,
    placementTemplate: Dict[str, Any] = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L45)

```python
def delete_placement(placementName: str, projectName: str) -> Dict[str, Any]:
```

### Client().delete_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L49)

```python
def delete_project(projectName: str) -> Dict[str, Any]:
```

### Client().describe_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L53)

```python
def describe_placement(
    placementName: str,
    projectName: str,
) -> Dict[str, Any]:
```

### Client().describe_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L59)

```python
def describe_project(projectName: str) -> Dict[str, Any]:
```

### Client().disassociate_device_from_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L63)

```python
def disassociate_device_from_placement(
    projectName: str,
    placementName: str,
    deviceTemplateName: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L69)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_devices_in_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L79)

```python
def get_devices_in_placement(
    projectName: str,
    placementName: str,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L85)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L89)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_placements

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L93)

```python
def list_placements(
    projectName: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_projects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L99)

```python
def list_projects(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L105)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L109)

```python
def tag_resource(resourceArn: str, tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L113)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L117)

```python
def update_placement(
    placementName: str,
    projectName: str,
    attributes: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/client.py#L123)

```python
def update_project(
    projectName: str,
    description: str = None,
    placementTemplate: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
