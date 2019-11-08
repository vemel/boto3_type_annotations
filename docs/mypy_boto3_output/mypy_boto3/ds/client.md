# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ds.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ds](index.md#ds) / Client
    - [Client](#client)
        - [Client().accept_shared_directory](#clientaccept_shared_directory)
        - [Client().add_ip_routes](#clientadd_ip_routes)
        - [Client().add_tags_to_resource](#clientadd_tags_to_resource)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_schema_extension](#clientcancel_schema_extension)
        - [Client().connect_directory](#clientconnect_directory)
        - [Client().create_alias](#clientcreate_alias)
        - [Client().create_computer](#clientcreate_computer)
        - [Client().create_conditional_forwarder](#clientcreate_conditional_forwarder)
        - [Client().create_directory](#clientcreate_directory)
        - [Client().create_log_subscription](#clientcreate_log_subscription)
        - [Client().create_microsoft_ad](#clientcreate_microsoft_ad)
        - [Client().create_snapshot](#clientcreate_snapshot)
        - [Client().create_trust](#clientcreate_trust)
        - [Client().delete_conditional_forwarder](#clientdelete_conditional_forwarder)
        - [Client().delete_directory](#clientdelete_directory)
        - [Client().delete_log_subscription](#clientdelete_log_subscription)
        - [Client().delete_snapshot](#clientdelete_snapshot)
        - [Client().delete_trust](#clientdelete_trust)
        - [Client().deregister_event_topic](#clientderegister_event_topic)
        - [Client().describe_conditional_forwarders](#clientdescribe_conditional_forwarders)
        - [Client().describe_directories](#clientdescribe_directories)
        - [Client().describe_domain_controllers](#clientdescribe_domain_controllers)
        - [Client().describe_event_topics](#clientdescribe_event_topics)
        - [Client().describe_shared_directories](#clientdescribe_shared_directories)
        - [Client().describe_snapshots](#clientdescribe_snapshots)
        - [Client().describe_trusts](#clientdescribe_trusts)
        - [Client().disable_radius](#clientdisable_radius)
        - [Client().disable_sso](#clientdisable_sso)
        - [Client().enable_radius](#clientenable_radius)
        - [Client().enable_sso](#clientenable_sso)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_directory_limits](#clientget_directory_limits)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_snapshot_limits](#clientget_snapshot_limits)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_ip_routes](#clientlist_ip_routes)
        - [Client().list_log_subscriptions](#clientlist_log_subscriptions)
        - [Client().list_schema_extensions](#clientlist_schema_extensions)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().register_event_topic](#clientregister_event_topic)
        - [Client().reject_shared_directory](#clientreject_shared_directory)
        - [Client().remove_ip_routes](#clientremove_ip_routes)
        - [Client().remove_tags_from_resource](#clientremove_tags_from_resource)
        - [Client().reset_user_password](#clientreset_user_password)
        - [Client().restore_from_snapshot](#clientrestore_from_snapshot)
        - [Client().share_directory](#clientshare_directory)
        - [Client().start_schema_extension](#clientstart_schema_extension)
        - [Client().unshare_directory](#clientunshare_directory)
        - [Client().update_conditional_forwarder](#clientupdate_conditional_forwarder)
        - [Client().update_number_of_domain_controllers](#clientupdate_number_of_domain_controllers)
        - [Client().update_radius](#clientupdate_radius)
        - [Client().update_trust](#clientupdate_trust)
        - [Client().verify_trust](#clientverify_trust)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L12)

```python
class Client(BaseClient):
```

### Client().accept_shared_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L15)

```python
def accept_shared_directory(SharedDirectoryId: str) -> Dict[str, Any]:
```

### Client().add_ip_routes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L19)

```python
def add_ip_routes(
    DirectoryId: str,
    IpRoutes: List[Any],
    UpdateSecurityGroupForDirectoryControllers: bool = None,
) -> Dict[str, Any]:
```

### Client().add_tags_to_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L28)

```python
def add_tags_to_resource(ResourceId: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L32)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_schema_extension

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L36)

```python
def cancel_schema_extension(
    DirectoryId: str,
    SchemaExtensionId: str,
) -> Dict[str, Any]:
```

### Client().connect_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L42)

```python
def connect_directory(
    Name: str,
    Password: str,
    Size: str,
    ConnectSettings: Dict[str, Any],
    ShortName: str = None,
    Description: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L55)

```python
def create_alias(DirectoryId: str, Alias: str) -> Dict[str, Any]:
```

### Client().create_computer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L59)

```python
def create_computer(
    DirectoryId: str,
    ComputerName: str,
    Password: str,
    OrganizationalUnitDistinguishedName: str = None,
    ComputerAttributes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_conditional_forwarder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L70)

```python
def create_conditional_forwarder(
    DirectoryId: str,
    RemoteDomainName: str,
    DnsIpAddrs: List[Any],
) -> Dict[str, Any]:
```

### Client().create_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L76)

```python
def create_directory(
    Name: str,
    Password: str,
    Size: str,
    ShortName: str = None,
    Description: str = None,
    VpcSettings: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_log_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L89)

```python
def create_log_subscription(
    DirectoryId: str,
    LogGroupName: str,
) -> Dict[str, Any]:
```

### Client().create_microsoft_ad

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L95)

```python
def create_microsoft_ad(
    Name: str,
    Password: str,
    VpcSettings: Dict[str, Any],
    ShortName: str = None,
    Description: str = None,
    Edition: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L108)

```python
def create_snapshot(DirectoryId: str, Name: str = None) -> Dict[str, Any]:
```

### Client().create_trust

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L112)

```python
def create_trust(
    DirectoryId: str,
    RemoteDomainName: str,
    TrustPassword: str,
    TrustDirection: str,
    TrustType: str = None,
    ConditionalForwarderIpAddrs: List[Any] = None,
    SelectiveAuth: str = None,
) -> Dict[str, Any]:
```

### Client().delete_conditional_forwarder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L125)

```python
def delete_conditional_forwarder(
    DirectoryId: str,
    RemoteDomainName: str,
) -> Dict[str, Any]:
```

### Client().delete_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L131)

```python
def delete_directory(DirectoryId: str) -> Dict[str, Any]:
```

### Client().delete_log_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L135)

```python
def delete_log_subscription(DirectoryId: str) -> Dict[str, Any]:
```

### Client().delete_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L139)

```python
def delete_snapshot(SnapshotId: str) -> Dict[str, Any]:
```

### Client().delete_trust

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L143)

```python
def delete_trust(
    TrustId: str,
    DeleteAssociatedConditionalForwarder: bool = None,
) -> Dict[str, Any]:
```

### Client().deregister_event_topic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L149)

```python
def deregister_event_topic(
    DirectoryId: str,
    TopicName: str,
) -> Dict[str, Any]:
```

### Client().describe_conditional_forwarders

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L155)

```python
def describe_conditional_forwarders(
    DirectoryId: str,
    RemoteDomainNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_directories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L161)

```python
def describe_directories(
    DirectoryIds: List[Any] = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_domain_controllers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L167)

```python
def describe_domain_controllers(
    DirectoryId: str,
    DomainControllerIds: List[Any] = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_event_topics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L177)

```python
def describe_event_topics(
    DirectoryId: str = None,
    TopicNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_shared_directories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L183)

```python
def describe_shared_directories(
    OwnerDirectoryId: str,
    SharedDirectoryIds: List[Any] = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L193)

```python
def describe_snapshots(
    DirectoryId: str = None,
    SnapshotIds: List[Any] = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_trusts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L203)

```python
def describe_trusts(
    DirectoryId: str = None,
    TrustIds: List[Any] = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().disable_radius

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L213)

```python
def disable_radius(DirectoryId: str) -> Dict[str, Any]:
```

### Client().disable_sso

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L217)

```python
def disable_sso(
    DirectoryId: str,
    UserName: str = None,
    Password: str = None,
) -> Dict[str, Any]:
```

### Client().enable_radius

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L223)

```python
def enable_radius(
    DirectoryId: str,
    RadiusSettings: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().enable_sso

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L229)

```python
def enable_sso(
    DirectoryId: str,
    UserName: str = None,
    Password: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L235)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_directory_limits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L245)

```python
def get_directory_limits() -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L249)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_snapshot_limits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L253)

```python
def get_snapshot_limits(DirectoryId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L257)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_ip_routes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L261)

```python
def list_ip_routes(
    DirectoryId: str,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_log_subscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L267)

```python
def list_log_subscriptions(
    DirectoryId: str = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_schema_extensions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L273)

```python
def list_schema_extensions(
    DirectoryId: str,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L279)

```python
def list_tags_for_resource(
    ResourceId: str,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().register_event_topic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L285)

```python
def register_event_topic(DirectoryId: str, TopicName: str) -> Dict[str, Any]:
```

### Client().reject_shared_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L289)

```python
def reject_shared_directory(SharedDirectoryId: str) -> Dict[str, Any]:
```

### Client().remove_ip_routes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L293)

```python
def remove_ip_routes(DirectoryId: str, CidrIps: List[Any]) -> Dict[str, Any]:
```

### Client().remove_tags_from_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L297)

```python
def remove_tags_from_resource(
    ResourceId: str,
    TagKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().reset_user_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L303)

```python
def reset_user_password(
    DirectoryId: str,
    UserName: str,
    NewPassword: str,
) -> Dict[str, Any]:
```

### Client().restore_from_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L309)

```python
def restore_from_snapshot(SnapshotId: str) -> Dict[str, Any]:
```

### Client().share_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L313)

```python
def share_directory(
    DirectoryId: str,
    ShareTarget: Dict[str, Any],
    ShareMethod: str,
    ShareNotes: str = None,
) -> Dict[str, Any]:
```

### Client().start_schema_extension

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L323)

```python
def start_schema_extension(
    DirectoryId: str,
    CreateSnapshotBeforeSchemaExtension: bool,
    LdifContent: str,
    Description: str,
) -> Dict[str, Any]:
```

### Client().unshare_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L333)

```python
def unshare_directory(
    DirectoryId: str,
    UnshareTarget: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_conditional_forwarder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L339)

```python
def update_conditional_forwarder(
    DirectoryId: str,
    RemoteDomainName: str,
    DnsIpAddrs: List[Any],
) -> Dict[str, Any]:
```

### Client().update_number_of_domain_controllers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L345)

```python
def update_number_of_domain_controllers(
    DirectoryId: str,
    DesiredNumber: int,
) -> Dict[str, Any]:
```

### Client().update_radius

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L351)

```python
def update_radius(
    DirectoryId: str,
    RadiusSettings: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_trust

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L357)

```python
def update_trust(TrustId: str, SelectiveAuth: str = None) -> Dict[str, Any]:
```

### Client().verify_trust

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/client.py#L361)

```python
def verify_trust(TrustId: str) -> Dict[str, Any]:
```
