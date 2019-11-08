# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.appstream.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Appstream](index.md#appstream) / Client
    - [Client](#client)
        - [Client().associate_fleet](#clientassociate_fleet)
        - [Client().batch_associate_user_stack](#clientbatch_associate_user_stack)
        - [Client().batch_disassociate_user_stack](#clientbatch_disassociate_user_stack)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().copy_image](#clientcopy_image)
        - [Client().create_directory_config](#clientcreate_directory_config)
        - [Client().create_fleet](#clientcreate_fleet)
        - [Client().create_image_builder](#clientcreate_image_builder)
        - [Client().create_image_builder_streaming_url](#clientcreate_image_builder_streaming_url)
        - [Client().create_stack](#clientcreate_stack)
        - [Client().create_streaming_url](#clientcreate_streaming_url)
        - [Client().create_usage_report_subscription](#clientcreate_usage_report_subscription)
        - [Client().create_user](#clientcreate_user)
        - [Client().delete_directory_config](#clientdelete_directory_config)
        - [Client().delete_fleet](#clientdelete_fleet)
        - [Client().delete_image](#clientdelete_image)
        - [Client().delete_image_builder](#clientdelete_image_builder)
        - [Client().delete_image_permissions](#clientdelete_image_permissions)
        - [Client().delete_stack](#clientdelete_stack)
        - [Client().delete_usage_report_subscription](#clientdelete_usage_report_subscription)
        - [Client().delete_user](#clientdelete_user)
        - [Client().describe_directory_configs](#clientdescribe_directory_configs)
        - [Client().describe_fleets](#clientdescribe_fleets)
        - [Client().describe_image_builders](#clientdescribe_image_builders)
        - [Client().describe_image_permissions](#clientdescribe_image_permissions)
        - [Client().describe_images](#clientdescribe_images)
        - [Client().describe_sessions](#clientdescribe_sessions)
        - [Client().describe_stacks](#clientdescribe_stacks)
        - [Client().describe_usage_report_subscriptions](#clientdescribe_usage_report_subscriptions)
        - [Client().describe_user_stack_associations](#clientdescribe_user_stack_associations)
        - [Client().describe_users](#clientdescribe_users)
        - [Client().disable_user](#clientdisable_user)
        - [Client().disassociate_fleet](#clientdisassociate_fleet)
        - [Client().enable_user](#clientenable_user)
        - [Client().expire_session](#clientexpire_session)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_associated_fleets](#clientlist_associated_fleets)
        - [Client().list_associated_stacks](#clientlist_associated_stacks)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().start_fleet](#clientstart_fleet)
        - [Client().start_image_builder](#clientstart_image_builder)
        - [Client().stop_fleet](#clientstop_fleet)
        - [Client().stop_image_builder](#clientstop_image_builder)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_directory_config](#clientupdate_directory_config)
        - [Client().update_fleet](#clientupdate_fleet)
        - [Client().update_image_permissions](#clientupdate_image_permissions)
        - [Client().update_stack](#clientupdate_stack)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L15)

```python
def associate_fleet(FleetName: str, StackName: str) -> Dict[str, Any]:
```

### Client().batch_associate_user_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L19)

```python
def batch_associate_user_stack(
    UserStackAssociations: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_disassociate_user_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L25)

```python
def batch_disassociate_user_stack(
    UserStackAssociations: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L31)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().copy_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L35)

```python
def copy_image(
    SourceImageName: str,
    DestinationImageName: str,
    DestinationRegion: str,
    DestinationImageDescription: str = None,
) -> Dict[str, Any]:
```

### Client().create_directory_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L45)

```python
def create_directory_config(
    DirectoryName: str,
    OrganizationalUnitDistinguishedNames: List[Any],
    ServiceAccountCredentials: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L54)

```python
def create_fleet(
    Name: str,
    InstanceType: str,
    ComputeCapacity: Dict[str, Any],
    ImageName: str = None,
    ImageArn: str = None,
    FleetType: str = None,
    VpcConfig: Dict[str, Any] = None,
    MaxUserDurationInSeconds: int = None,
    DisconnectTimeoutInSeconds: int = None,
    Description: str = None,
    DisplayName: str = None,
    EnableDefaultInternetAccess: bool = None,
    DomainJoinInfo: Dict[str, Any] = None,
    Tags: Dict[str, Any] = None,
    IdleDisconnectTimeoutInSeconds: int = None,
    IamRoleArn: str = None,
) -> Dict[str, Any]:
```

### Client().create_image_builder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L76)

```python
def create_image_builder(
    Name: str,
    InstanceType: str,
    ImageName: str = None,
    ImageArn: str = None,
    Description: str = None,
    DisplayName: str = None,
    VpcConfig: Dict[str, Any] = None,
    IamRoleArn: str = None,
    EnableDefaultInternetAccess: bool = None,
    DomainJoinInfo: Dict[str, Any] = None,
    AppstreamAgentVersion: str = None,
    Tags: Dict[str, Any] = None,
    AccessEndpoints: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_image_builder_streaming_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L95)

```python
def create_image_builder_streaming_url(
    Name: str,
    Validity: int = None,
) -> Dict[str, Any]:
```

### Client().create_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L101)

```python
def create_stack(
    Name: str,
    Description: str = None,
    DisplayName: str = None,
    StorageConnectors: List[Any] = None,
    RedirectURL: str = None,
    FeedbackURL: str = None,
    UserSettings: List[Any] = None,
    ApplicationSettings: Dict[str, Any] = None,
    Tags: Dict[str, Any] = None,
    AccessEndpoints: List[Any] = None,
    EmbedHostDomains: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_streaming_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L118)

```python
def create_streaming_url(
    StackName: str,
    FleetName: str,
    UserId: str,
    ApplicationId: str = None,
    Validity: int = None,
    SessionContext: str = None,
) -> Dict[str, Any]:
```

### Client().create_usage_report_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L130)

```python
def create_usage_report_subscription() -> Dict[str, Any]:
```

### Client().create_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L134)

```python
def create_user(
    UserName: str,
    AuthenticationType: str,
    MessageAction: str = None,
    FirstName: str = None,
    LastName: str = None,
) -> Dict[str, Any]:
```

### Client().delete_directory_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L145)

```python
def delete_directory_config(DirectoryName: str) -> Dict[str, Any]:
```

### Client().delete_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L149)

```python
def delete_fleet(Name: str) -> Dict[str, Any]:
```

### Client().delete_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L153)

```python
def delete_image(Name: str) -> Dict[str, Any]:
```

### Client().delete_image_builder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L157)

```python
def delete_image_builder(Name: str) -> Dict[str, Any]:
```

### Client().delete_image_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L161)

```python
def delete_image_permissions(
    Name: str,
    SharedAccountId: str,
) -> Dict[str, Any]:
```

### Client().delete_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L167)

```python
def delete_stack(Name: str) -> Dict[str, Any]:
```

### Client().delete_usage_report_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L171)

```python
def delete_usage_report_subscription() -> Dict[str, Any]:
```

### Client().delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L175)

```python
def delete_user(UserName: str, AuthenticationType: str) -> Dict[str, Any]:
```

### Client().describe_directory_configs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L179)

```python
def describe_directory_configs(
    DirectoryNames: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_fleets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L188)

```python
def describe_fleets(
    Names: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_image_builders

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L194)

```python
def describe_image_builders(
    Names: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_image_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L200)

```python
def describe_image_permissions(
    Name: str,
    MaxResults: int = None,
    SharedAwsAccountIds: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_images

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L210)

```python
def describe_images(
    Names: List[Any] = None,
    Arns: List[Any] = None,
    Type: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_sessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L221)

```python
def describe_sessions(
    StackName: str,
    FleetName: str,
    UserId: str = None,
    NextToken: str = None,
    Limit: int = None,
    AuthenticationType: str = None,
) -> Dict[str, Any]:
```

### Client().describe_stacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L233)

```python
def describe_stacks(
    Names: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_usage_report_subscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L239)

```python
def describe_usage_report_subscriptions(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_user_stack_associations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L245)

```python
def describe_user_stack_associations(
    StackName: str = None,
    UserName: str = None,
    AuthenticationType: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L256)

```python
def describe_users(
    AuthenticationType: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().disable_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L262)

```python
def disable_user(UserName: str, AuthenticationType: str) -> Dict[str, Any]:
```

### Client().disassociate_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L266)

```python
def disassociate_fleet(FleetName: str, StackName: str) -> Dict[str, Any]:
```

### Client().enable_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L270)

```python
def enable_user(UserName: str, AuthenticationType: str) -> Dict[str, Any]:
```

### Client().expire_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L274)

```python
def expire_session(SessionId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L278)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L288)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L292)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_associated_fleets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L296)

```python
def list_associated_fleets(
    StackName: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_associated_stacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L302)

```python
def list_associated_stacks(
    FleetName: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L308)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().start_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L312)

```python
def start_fleet(Name: str) -> Dict[str, Any]:
```

### Client().start_image_builder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L316)

```python
def start_image_builder(
    Name: str,
    AppstreamAgentVersion: str = None,
) -> Dict[str, Any]:
```

### Client().stop_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L322)

```python
def stop_fleet(Name: str) -> Dict[str, Any]:
```

### Client().stop_image_builder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L326)

```python
def stop_image_builder(Name: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L330)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L334)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_directory_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L338)

```python
def update_directory_config(
    DirectoryName: str,
    OrganizationalUnitDistinguishedNames: List[Any] = None,
    ServiceAccountCredentials: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L347)

```python
def update_fleet(
    ImageName: str = None,
    ImageArn: str = None,
    Name: str = None,
    InstanceType: str = None,
    ComputeCapacity: Dict[str, Any] = None,
    VpcConfig: Dict[str, Any] = None,
    MaxUserDurationInSeconds: int = None,
    DisconnectTimeoutInSeconds: int = None,
    DeleteVpcConfig: bool = None,
    Description: str = None,
    DisplayName: str = None,
    EnableDefaultInternetAccess: bool = None,
    DomainJoinInfo: Dict[str, Any] = None,
    IdleDisconnectTimeoutInSeconds: int = None,
    AttributesToDelete: List[Any] = None,
    IamRoleArn: str = None,
) -> Dict[str, Any]:
```

### Client().update_image_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L369)

```python
def update_image_permissions(
    Name: str,
    SharedAccountId: str,
    ImagePermissions: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/client.py#L375)

```python
def update_stack(
    Name: str,
    DisplayName: str = None,
    Description: str = None,
    StorageConnectors: List[Any] = None,
    DeleteStorageConnectors: bool = None,
    RedirectURL: str = None,
    FeedbackURL: str = None,
    AttributesToDelete: List[Any] = None,
    UserSettings: List[Any] = None,
    ApplicationSettings: Dict[str, Any] = None,
    AccessEndpoints: List[Any] = None,
    EmbedHostDomains: List[Any] = None,
) -> Dict[str, Any]:
```
