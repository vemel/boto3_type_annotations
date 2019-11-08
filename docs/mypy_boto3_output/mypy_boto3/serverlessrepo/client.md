# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.serverlessrepo.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Serverlessrepo](index.md#serverlessrepo) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_application](#clientcreate_application)
        - [Client().create_application_version](#clientcreate_application_version)
        - [Client().create_cloud_formation_change_set](#clientcreate_cloud_formation_change_set)
        - [Client().create_cloud_formation_template](#clientcreate_cloud_formation_template)
        - [Client().delete_application](#clientdelete_application)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_application](#clientget_application)
        - [Client().get_application_policy](#clientget_application_policy)
        - [Client().get_cloud_formation_template](#clientget_cloud_formation_template)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_application_dependencies](#clientlist_application_dependencies)
        - [Client().list_application_versions](#clientlist_application_versions)
        - [Client().list_applications](#clientlist_applications)
        - [Client().put_application_policy](#clientput_application_policy)
        - [Client().update_application](#clientupdate_application)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L19)

```python
def create_application(
    Author: str,
    Description: str,
    Name: str,
    HomePageUrl: str = None,
    Labels: List[Any] = None,
    LicenseBody: str = None,
    LicenseUrl: str = None,
    ReadmeBody: str = None,
    ReadmeUrl: str = None,
    SemanticVersion: str = None,
    SourceCodeArchiveUrl: str = None,
    SourceCodeUrl: str = None,
    SpdxLicenseId: str = None,
    TemplateBody: str = None,
    TemplateUrl: str = None,
) -> Dict[str, Any]:
```

### Client().create_application_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L40)

```python
def create_application_version(
    ApplicationId: str,
    SemanticVersion: str,
    SourceCodeArchiveUrl: str = None,
    SourceCodeUrl: str = None,
    TemplateBody: str = None,
    TemplateUrl: str = None,
) -> Dict[str, Any]:
```

### Client().create_cloud_formation_change_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L52)

```python
def create_cloud_formation_change_set(
    ApplicationId: str,
    StackName: str,
    Capabilities: List[Any] = None,
    ChangeSetName: str = None,
    ClientToken: str = None,
    Description: str = None,
    NotificationArns: List[Any] = None,
    ParameterOverrides: List[Any] = None,
    ResourceTypes: List[Any] = None,
    RollbackConfiguration: Dict[str, Any] = None,
    SemanticVersion: str = None,
    Tags: List[Any] = None,
    TemplateId: str = None,
) -> Dict[str, Any]:
```

### Client().create_cloud_formation_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L71)

```python
def create_cloud_formation_template(
    ApplicationId: str,
    SemanticVersion: str = None,
) -> Dict[str, Any]:
```

### Client().delete_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L77)

```python
def delete_application(ApplicationId: str) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L81)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L91)

```python
def get_application(
    ApplicationId: str,
    SemanticVersion: str = None,
) -> Dict[str, Any]:
```

### Client().get_application_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L97)

```python
def get_application_policy(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_cloud_formation_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L101)

```python
def get_cloud_formation_template(
    ApplicationId: str,
    TemplateId: str,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L107)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L111)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_application_dependencies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L115)

```python
def list_application_dependencies(
    ApplicationId: str,
    MaxItems: int = None,
    NextToken: str = None,
    SemanticVersion: str = None,
) -> Dict[str, Any]:
```

### Client().list_application_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L125)

```python
def list_application_versions(
    ApplicationId: str,
    MaxItems: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L131)

```python
def list_applications(
    MaxItems: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_application_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L137)

```python
def put_application_policy(
    ApplicationId: str,
    Statements: List[Any],
) -> Dict[str, Any]:
```

### Client().update_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/client.py#L143)

```python
def update_application(
    ApplicationId: str,
    Author: str = None,
    Description: str = None,
    HomePageUrl: str = None,
    Labels: List[Any] = None,
    ReadmeBody: str = None,
    ReadmeUrl: str = None,
) -> Dict[str, Any]:
```
