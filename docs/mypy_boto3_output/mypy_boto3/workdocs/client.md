# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.workdocs.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Workdocs](index.md#workdocs) / Client
    - [Client](#client)
        - [Client().abort_document_version_upload](#clientabort_document_version_upload)
        - [Client().activate_user](#clientactivate_user)
        - [Client().add_resource_permissions](#clientadd_resource_permissions)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_comment](#clientcreate_comment)
        - [Client().create_custom_metadata](#clientcreate_custom_metadata)
        - [Client().create_folder](#clientcreate_folder)
        - [Client().create_labels](#clientcreate_labels)
        - [Client().create_notification_subscription](#clientcreate_notification_subscription)
        - [Client().create_user](#clientcreate_user)
        - [Client().deactivate_user](#clientdeactivate_user)
        - [Client().delete_comment](#clientdelete_comment)
        - [Client().delete_custom_metadata](#clientdelete_custom_metadata)
        - [Client().delete_document](#clientdelete_document)
        - [Client().delete_folder](#clientdelete_folder)
        - [Client().delete_folder_contents](#clientdelete_folder_contents)
        - [Client().delete_labels](#clientdelete_labels)
        - [Client().delete_notification_subscription](#clientdelete_notification_subscription)
        - [Client().delete_user](#clientdelete_user)
        - [Client().describe_activities](#clientdescribe_activities)
        - [Client().describe_comments](#clientdescribe_comments)
        - [Client().describe_document_versions](#clientdescribe_document_versions)
        - [Client().describe_folder_contents](#clientdescribe_folder_contents)
        - [Client().describe_groups](#clientdescribe_groups)
        - [Client().describe_notification_subscriptions](#clientdescribe_notification_subscriptions)
        - [Client().describe_resource_permissions](#clientdescribe_resource_permissions)
        - [Client().describe_root_folders](#clientdescribe_root_folders)
        - [Client().describe_users](#clientdescribe_users)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_current_user](#clientget_current_user)
        - [Client().get_document](#clientget_document)
        - [Client().get_document_path](#clientget_document_path)
        - [Client().get_document_version](#clientget_document_version)
        - [Client().get_folder](#clientget_folder)
        - [Client().get_folder_path](#clientget_folder_path)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_resources](#clientget_resources)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().initiate_document_version_upload](#clientinitiate_document_version_upload)
        - [Client().remove_all_resource_permissions](#clientremove_all_resource_permissions)
        - [Client().remove_resource_permission](#clientremove_resource_permission)
        - [Client().update_document](#clientupdate_document)
        - [Client().update_document_version](#clientupdate_document_version)
        - [Client().update_folder](#clientupdate_folder)
        - [Client().update_user](#clientupdate_user)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L13)

```python
class Client(BaseClient):
```

### Client().abort_document_version_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L16)

```python
def abort_document_version_upload(
    DocumentId: str,
    VersionId: str,
    AuthenticationToken: str = None,
) -> None:
```

### Client().activate_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L22)

```python
def activate_user(
    UserId: str,
    AuthenticationToken: str = None,
) -> Dict[str, Any]:
```

### Client().add_resource_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L28)

```python
def add_resource_permissions(
    ResourceId: str,
    Principals: List[Any],
    AuthenticationToken: str = None,
    NotificationOptions: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L38)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_comment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L42)

```python
def create_comment(
    DocumentId: str,
    VersionId: str,
    Text: str,
    AuthenticationToken: str = None,
    ParentId: str = None,
    ThreadId: str = None,
    Visibility: str = None,
    NotifyCollaborators: bool = None,
) -> Dict[str, Any]:
```

### Client().create_custom_metadata

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L56)

```python
def create_custom_metadata(
    ResourceId: str,
    CustomMetadata: Dict[str, Any],
    AuthenticationToken: str = None,
    VersionId: str = None,
) -> Dict[str, Any]:
```

### Client().create_folder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L66)

```python
def create_folder(
    ParentFolderId: str,
    AuthenticationToken: str = None,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().create_labels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L72)

```python
def create_labels(
    ResourceId: str,
    Labels: List[Any],
    AuthenticationToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_notification_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L78)

```python
def create_notification_subscription(
    OrganizationId: str,
    Endpoint: str,
    Protocol: str,
    SubscriptionType: str,
) -> Dict[str, Any]:
```

### Client().create_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L84)

```python
def create_user(
    Username: str,
    GivenName: str,
    Surname: str,
    Password: str,
    OrganizationId: str = None,
    EmailAddress: str = None,
    TimeZoneId: str = None,
    StorageRule: Dict[str, Any] = None,
    AuthenticationToken: str = None,
) -> Dict[str, Any]:
```

### Client().deactivate_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L99)

```python
def deactivate_user(UserId: str, AuthenticationToken: str = None) -> None:
```

### Client().delete_comment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L103)

```python
def delete_comment(
    DocumentId: str,
    VersionId: str,
    CommentId: str,
    AuthenticationToken: str = None,
) -> None:
```

### Client().delete_custom_metadata

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L113)

```python
def delete_custom_metadata(
    ResourceId: str,
    AuthenticationToken: str = None,
    VersionId: str = None,
    Keys: List[Any] = None,
    DeleteAll: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_document

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L124)

```python
def delete_document(DocumentId: str, AuthenticationToken: str = None) -> None:
```

### Client().delete_folder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L128)

```python
def delete_folder(FolderId: str, AuthenticationToken: str = None) -> None:
```

### Client().delete_folder_contents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L132)

```python
def delete_folder_contents(
    FolderId: str,
    AuthenticationToken: str = None,
) -> None:
```

### Client().delete_labels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L138)

```python
def delete_labels(
    ResourceId: str,
    AuthenticationToken: str = None,
    Labels: List[Any] = None,
    DeleteAll: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_notification_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L148)

```python
def delete_notification_subscription(
    SubscriptionId: str,
    OrganizationId: str,
) -> None:
```

### Client().delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L154)

```python
def delete_user(UserId: str, AuthenticationToken: str = None) -> None:
```

### Client().describe_activities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L158)

```python
def describe_activities(
    AuthenticationToken: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    OrganizationId: str = None,
    ActivityTypes: str = None,
    ResourceId: str = None,
    UserId: str = None,
    IncludeIndirectActivities: bool = None,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_comments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L174)

```python
def describe_comments(
    DocumentId: str,
    VersionId: str,
    AuthenticationToken: str = None,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_document_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L185)

```python
def describe_document_versions(
    DocumentId: str,
    AuthenticationToken: str = None,
    Marker: str = None,
    Limit: int = None,
    Include: str = None,
    Fields: str = None,
) -> Dict[str, Any]:
```

### Client().describe_folder_contents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L197)

```python
def describe_folder_contents(
    FolderId: str,
    AuthenticationToken: str = None,
    Sort: str = None,
    Order: str = None,
    Limit: int = None,
    Marker: str = None,
    Type: str = None,
    Include: str = None,
) -> Dict[str, Any]:
```

### Client().describe_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L211)

```python
def describe_groups(
    SearchQuery: str,
    AuthenticationToken: str = None,
    OrganizationId: str = None,
    Marker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_notification_subscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L222)

```python
def describe_notification_subscriptions(
    OrganizationId: str,
    Marker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_resource_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L228)

```python
def describe_resource_permissions(
    ResourceId: str,
    AuthenticationToken: str = None,
    PrincipalId: str = None,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_root_folders

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L239)

```python
def describe_root_folders(
    AuthenticationToken: str,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L245)

```python
def describe_users(
    AuthenticationToken: str = None,
    OrganizationId: str = None,
    UserIds: str = None,
    Query: str = None,
    Include: str = None,
    Order: str = None,
    Sort: str = None,
    Marker: str = None,
    Limit: int = None,
    Fields: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L261)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_current_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L271)

```python
def get_current_user(AuthenticationToken: str) -> Dict[str, Any]:
```

### Client().get_document

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L275)

```python
def get_document(
    DocumentId: str,
    AuthenticationToken: str = None,
    IncludeCustomMetadata: bool = None,
) -> Dict[str, Any]:
```

### Client().get_document_path

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L284)

```python
def get_document_path(
    DocumentId: str,
    AuthenticationToken: str = None,
    Limit: int = None,
    Fields: str = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().get_document_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L295)

```python
def get_document_version(
    DocumentId: str,
    VersionId: str,
    AuthenticationToken: str = None,
    Fields: str = None,
    IncludeCustomMetadata: bool = None,
) -> Dict[str, Any]:
```

### Client().get_folder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L306)

```python
def get_folder(
    FolderId: str,
    AuthenticationToken: str = None,
    IncludeCustomMetadata: bool = None,
) -> Dict[str, Any]:
```

### Client().get_folder_path

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L315)

```python
def get_folder_path(
    FolderId: str,
    AuthenticationToken: str = None,
    Limit: int = None,
    Fields: str = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L326)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L330)

```python
def get_resources(
    AuthenticationToken: str = None,
    UserId: str = None,
    CollectionType: str = None,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L341)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().initiate_document_version_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L345)

```python
def initiate_document_version_upload(
    ParentFolderId: str,
    AuthenticationToken: str = None,
    Id: str = None,
    Name: str = None,
    ContentCreatedTimestamp: datetime = None,
    ContentModifiedTimestamp: datetime = None,
    ContentType: str = None,
    DocumentSizeInBytes: int = None,
) -> Dict[str, Any]:
```

### Client().remove_all_resource_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L359)

```python
def remove_all_resource_permissions(
    ResourceId: str,
    AuthenticationToken: str = None,
) -> None:
```

### Client().remove_resource_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L365)

```python
def remove_resource_permission(
    ResourceId: str,
    PrincipalId: str,
    AuthenticationToken: str = None,
    PrincipalType: str = None,
) -> None:
```

### Client().update_document

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L375)

```python
def update_document(
    DocumentId: str,
    AuthenticationToken: str = None,
    Name: str = None,
    ParentFolderId: str = None,
    ResourceState: str = None,
) -> None:
```

### Client().update_document_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L386)

```python
def update_document_version(
    DocumentId: str,
    VersionId: str,
    AuthenticationToken: str = None,
    VersionStatus: str = None,
) -> None:
```

### Client().update_folder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L396)

```python
def update_folder(
    FolderId: str,
    AuthenticationToken: str = None,
    Name: str = None,
    ParentFolderId: str = None,
    ResourceState: str = None,
) -> None:
```

### Client().update_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/client.py#L407)

```python
def update_user(
    UserId: str,
    AuthenticationToken: str = None,
    GivenName: str = None,
    Surname: str = None,
    Type: str = None,
    StorageRule: Dict[str, Any] = None,
    TimeZoneId: str = None,
    Locale: str = None,
    GrantPoweruserPrivileges: str = None,
) -> Dict[str, Any]:
```
