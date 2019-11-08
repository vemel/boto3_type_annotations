# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.workspaces.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Workspaces](index.md#workspaces) / Client
    - [Client](#client)
        - [Client().associate_ip_groups](#clientassociate_ip_groups)
        - [Client().authorize_ip_rules](#clientauthorize_ip_rules)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().copy_workspace_image](#clientcopy_workspace_image)
        - [Client().create_ip_group](#clientcreate_ip_group)
        - [Client().create_tags](#clientcreate_tags)
        - [Client().create_workspaces](#clientcreate_workspaces)
        - [Client().delete_ip_group](#clientdelete_ip_group)
        - [Client().delete_tags](#clientdelete_tags)
        - [Client().delete_workspace_image](#clientdelete_workspace_image)
        - [Client().describe_account](#clientdescribe_account)
        - [Client().describe_account_modifications](#clientdescribe_account_modifications)
        - [Client().describe_client_properties](#clientdescribe_client_properties)
        - [Client().describe_ip_groups](#clientdescribe_ip_groups)
        - [Client().describe_tags](#clientdescribe_tags)
        - [Client().describe_workspace_bundles](#clientdescribe_workspace_bundles)
        - [Client().describe_workspace_directories](#clientdescribe_workspace_directories)
        - [Client().describe_workspace_images](#clientdescribe_workspace_images)
        - [Client().describe_workspace_snapshots](#clientdescribe_workspace_snapshots)
        - [Client().describe_workspaces](#clientdescribe_workspaces)
        - [Client().describe_workspaces_connection_status](#clientdescribe_workspaces_connection_status)
        - [Client().disassociate_ip_groups](#clientdisassociate_ip_groups)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_workspace_image](#clientimport_workspace_image)
        - [Client().list_available_management_cidr_ranges](#clientlist_available_management_cidr_ranges)
        - [Client().modify_account](#clientmodify_account)
        - [Client().modify_client_properties](#clientmodify_client_properties)
        - [Client().modify_workspace_properties](#clientmodify_workspace_properties)
        - [Client().modify_workspace_state](#clientmodify_workspace_state)
        - [Client().reboot_workspaces](#clientreboot_workspaces)
        - [Client().rebuild_workspaces](#clientrebuild_workspaces)
        - [Client().restore_workspace](#clientrestore_workspace)
        - [Client().revoke_ip_rules](#clientrevoke_ip_rules)
        - [Client().start_workspaces](#clientstart_workspaces)
        - [Client().stop_workspaces](#clientstop_workspaces)
        - [Client().terminate_workspaces](#clientterminate_workspaces)
        - [Client().update_rules_of_ip_group](#clientupdate_rules_of_ip_group)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_ip_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L15)

```python
def associate_ip_groups(
    DirectoryId: str,
    GroupIds: List[Any],
) -> Dict[str, Any]:
```

### Client().authorize_ip_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L21)

```python
def authorize_ip_rules(GroupId: str, UserRules: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L25)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().copy_workspace_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L29)

```python
def copy_workspace_image(
    Name: str,
    SourceImageId: str,
    SourceRegion: str,
    Description: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_ip_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L40)

```python
def create_ip_group(
    GroupName: str,
    GroupDesc: str = None,
    UserRules: List[Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L50)

```python
def create_tags(ResourceId: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().create_workspaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L54)

```python
def create_workspaces(Workspaces: List[Any]) -> Dict[str, Any]:
```

### Client().delete_ip_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L58)

```python
def delete_ip_group(GroupId: str) -> Dict[str, Any]:
```

### Client().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L62)

```python
def delete_tags(ResourceId: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().delete_workspace_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L66)

```python
def delete_workspace_image(ImageId: str) -> Dict[str, Any]:
```

### Client().describe_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L70)

```python
def describe_account() -> Dict[str, Any]:
```

### Client().describe_account_modifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L74)

```python
def describe_account_modifications(NextToken: str = None) -> Dict[str, Any]:
```

### Client().describe_client_properties

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L78)

```python
def describe_client_properties(ResourceIds: List[Any]) -> Dict[str, Any]:
```

### Client().describe_ip_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L82)

```python
def describe_ip_groups(
    GroupIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L88)

```python
def describe_tags(ResourceId: str) -> Dict[str, Any]:
```

### Client().describe_workspace_bundles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L92)

```python
def describe_workspace_bundles(
    BundleIds: List[Any] = None,
    Owner: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_workspace_directories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L98)

```python
def describe_workspace_directories(
    DirectoryIds: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_workspace_images

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L104)

```python
def describe_workspace_images(
    ImageIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_workspace_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L110)

```python
def describe_workspace_snapshots(WorkspaceId: str) -> Dict[str, Any]:
```

### Client().describe_workspaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L114)

```python
def describe_workspaces(
    WorkspaceIds: List[Any] = None,
    DirectoryId: str = None,
    UserName: str = None,
    BundleId: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_workspaces_connection_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L126)

```python
def describe_workspaces_connection_status(
    WorkspaceIds: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().disassociate_ip_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L132)

```python
def disassociate_ip_groups(
    DirectoryId: str,
    GroupIds: List[Any],
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L138)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L148)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L152)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_workspace_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L156)

```python
def import_workspace_image(
    Ec2ImageId: str,
    IngestionProcess: str,
    ImageName: str,
    ImageDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_available_management_cidr_ranges

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L167)

```python
def list_available_management_cidr_ranges(
    ManagementCidrRangeConstraint: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().modify_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L176)

```python
def modify_account(
    DedicatedTenancySupport: str = None,
    DedicatedTenancyManagementCidrRange: str = None,
) -> Dict[str, Any]:
```

### Client().modify_client_properties

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L184)

```python
def modify_client_properties(
    ResourceId: str,
    ClientProperties: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().modify_workspace_properties

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L190)

```python
def modify_workspace_properties(
    WorkspaceId: str,
    WorkspaceProperties: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().modify_workspace_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L196)

```python
def modify_workspace_state(
    WorkspaceId: str,
    WorkspaceState: str,
) -> Dict[str, Any]:
```

### Client().reboot_workspaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L202)

```python
def reboot_workspaces(RebootWorkspaceRequests: List[Any]) -> Dict[str, Any]:
```

### Client().rebuild_workspaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L206)

```python
def rebuild_workspaces(RebuildWorkspaceRequests: List[Any]) -> Dict[str, Any]:
```

### Client().restore_workspace

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L210)

```python
def restore_workspace(WorkspaceId: str) -> Dict[str, Any]:
```

### Client().revoke_ip_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L214)

```python
def revoke_ip_rules(GroupId: str, UserRules: List[Any]) -> Dict[str, Any]:
```

### Client().start_workspaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L218)

```python
def start_workspaces(StartWorkspaceRequests: List[Any]) -> Dict[str, Any]:
```

### Client().stop_workspaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L222)

```python
def stop_workspaces(StopWorkspaceRequests: List[Any]) -> Dict[str, Any]:
```

### Client().terminate_workspaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L226)

```python
def terminate_workspaces(
    TerminateWorkspaceRequests: List[Any],
) -> Dict[str, Any]:
```

### Client().update_rules_of_ip_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/client.py#L232)

```python
def update_rules_of_ip_group(
    GroupId: str,
    UserRules: List[Any],
) -> Dict[str, Any]:
```
