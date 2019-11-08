# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codestar.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codestar](index.md#codestar) / Client
    - [Client](#client)
        - [Client().associate_team_member](#clientassociate_team_member)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_project](#clientcreate_project)
        - [Client().create_user_profile](#clientcreate_user_profile)
        - [Client().delete_project](#clientdelete_project)
        - [Client().delete_user_profile](#clientdelete_user_profile)
        - [Client().describe_project](#clientdescribe_project)
        - [Client().describe_user_profile](#clientdescribe_user_profile)
        - [Client().disassociate_team_member](#clientdisassociate_team_member)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_projects](#clientlist_projects)
        - [Client().list_resources](#clientlist_resources)
        - [Client().list_tags_for_project](#clientlist_tags_for_project)
        - [Client().list_team_members](#clientlist_team_members)
        - [Client().list_user_profiles](#clientlist_user_profiles)
        - [Client().tag_project](#clienttag_project)
        - [Client().untag_project](#clientuntag_project)
        - [Client().update_project](#clientupdate_project)
        - [Client().update_team_member](#clientupdate_team_member)
        - [Client().update_user_profile](#clientupdate_user_profile)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_team_member

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L15)

```python
def associate_team_member(
    projectId: str,
    userArn: str,
    projectRole: str,
    clientRequestToken: str = None,
    remoteAccessAllowed: bool = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L26)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L30)

```python
def create_project(
    name: str,
    id: str,
    description: str = None,
    clientRequestToken: str = None,
    sourceCode: List[Any] = None,
    toolchain: Dict[str, Any] = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_user_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L43)

```python
def create_user_profile(
    userArn: str,
    displayName: str,
    emailAddress: str,
    sshPublicKey: str = None,
) -> Dict[str, Any]:
```

### Client().delete_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L53)

```python
def delete_project(
    id: str,
    clientRequestToken: str = None,
    deleteStack: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_user_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L59)

```python
def delete_user_profile(userArn: str) -> Dict[str, Any]:
```

### Client().describe_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L63)

```python
def describe_project(id: str) -> Dict[str, Any]:
```

### Client().describe_user_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L67)

```python
def describe_user_profile(userArn: str) -> Dict[str, Any]:
```

### Client().disassociate_team_member

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L71)

```python
def disassociate_team_member(projectId: str, userArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L75)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L85)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L89)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_projects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L93)

```python
def list_projects(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L99)

```python
def list_resources(
    projectId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L105)

```python
def list_tags_for_project(
    id: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_team_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L111)

```python
def list_team_members(
    projectId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_user_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L117)

```python
def list_user_profiles(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().tag_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L123)

```python
def tag_project(id: str, tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L127)

```python
def untag_project(id: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().update_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L131)

```python
def update_project(
    id: str,
    name: str = None,
    description: str = None,
) -> Dict[str, Any]:
```

### Client().update_team_member

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L137)

```python
def update_team_member(
    projectId: str,
    userArn: str,
    projectRole: str = None,
    remoteAccessAllowed: bool = None,
) -> Dict[str, Any]:
```

### Client().update_user_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/client.py#L147)

```python
def update_user_profile(
    userArn: str,
    displayName: str = None,
    emailAddress: str = None,
    sshPublicKey: str = None,
) -> Dict[str, Any]:
```
