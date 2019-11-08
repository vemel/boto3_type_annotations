# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elasticbeanstalk.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elasticbeanstalk](index.md#elasticbeanstalk) / Client
    - [Client](#client)
        - [Client().abort_environment_update](#clientabort_environment_update)
        - [Client().apply_environment_managed_action](#clientapply_environment_managed_action)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().check_dns_availability](#clientcheck_dns_availability)
        - [Client().compose_environments](#clientcompose_environments)
        - [Client().create_application](#clientcreate_application)
        - [Client().create_application_version](#clientcreate_application_version)
        - [Client().create_configuration_template](#clientcreate_configuration_template)
        - [Client().create_environment](#clientcreate_environment)
        - [Client().create_platform_version](#clientcreate_platform_version)
        - [Client().create_storage_location](#clientcreate_storage_location)
        - [Client().delete_application](#clientdelete_application)
        - [Client().delete_application_version](#clientdelete_application_version)
        - [Client().delete_configuration_template](#clientdelete_configuration_template)
        - [Client().delete_environment_configuration](#clientdelete_environment_configuration)
        - [Client().delete_platform_version](#clientdelete_platform_version)
        - [Client().describe_account_attributes](#clientdescribe_account_attributes)
        - [Client().describe_application_versions](#clientdescribe_application_versions)
        - [Client().describe_applications](#clientdescribe_applications)
        - [Client().describe_configuration_options](#clientdescribe_configuration_options)
        - [Client().describe_configuration_settings](#clientdescribe_configuration_settings)
        - [Client().describe_environment_health](#clientdescribe_environment_health)
        - [Client().describe_environment_managed_action_history](#clientdescribe_environment_managed_action_history)
        - [Client().describe_environment_managed_actions](#clientdescribe_environment_managed_actions)
        - [Client().describe_environment_resources](#clientdescribe_environment_resources)
        - [Client().describe_environments](#clientdescribe_environments)
        - [Client().describe_events](#clientdescribe_events)
        - [Client().describe_instances_health](#clientdescribe_instances_health)
        - [Client().describe_platform_version](#clientdescribe_platform_version)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_available_solution_stacks](#clientlist_available_solution_stacks)
        - [Client().list_platform_versions](#clientlist_platform_versions)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().rebuild_environment](#clientrebuild_environment)
        - [Client().request_environment_info](#clientrequest_environment_info)
        - [Client().restart_app_server](#clientrestart_app_server)
        - [Client().retrieve_environment_info](#clientretrieve_environment_info)
        - [Client().swap_environment_cnames](#clientswap_environment_cnames)
        - [Client().terminate_environment](#clientterminate_environment)
        - [Client().update_application](#clientupdate_application)
        - [Client().update_application_resource_lifecycle](#clientupdate_application_resource_lifecycle)
        - [Client().update_application_version](#clientupdate_application_version)
        - [Client().update_configuration_template](#clientupdate_configuration_template)
        - [Client().update_environment](#clientupdate_environment)
        - [Client().update_tags_for_resource](#clientupdate_tags_for_resource)
        - [Client().validate_configuration_settings](#clientvalidate_configuration_settings)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L13)

```python
class Client(BaseClient):
```

### Client().abort_environment_update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L16)

```python
def abort_environment_update(
    EnvironmentId: str = None,
    EnvironmentName: str = None,
) -> None:
```

### Client().apply_environment_managed_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L22)

```python
def apply_environment_managed_action(
    ActionId: str,
    EnvironmentName: str = None,
    EnvironmentId: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L28)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().check_dns_availability

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L32)

```python
def check_dns_availability(CNAMEPrefix: str) -> Dict[str, Any]:
```

### Client().compose_environments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L36)

```python
def compose_environments(
    ApplicationName: str = None,
    GroupName: str = None,
    VersionLabels: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L45)

```python
def create_application(
    ApplicationName: str,
    Description: str = None,
    ResourceLifecycleConfig: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_application_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L55)

```python
def create_application_version(
    ApplicationName: str,
    VersionLabel: str,
    Description: str = None,
    SourceBuildInformation: Dict[str, Any] = None,
    SourceBundle: Dict[str, Any] = None,
    BuildConfiguration: Dict[str, Any] = None,
    AutoCreateApplication: bool = None,
    Process: bool = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_configuration_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L70)

```python
def create_configuration_template(
    ApplicationName: str,
    TemplateName: str,
    SolutionStackName: str = None,
    PlatformArn: str = None,
    SourceConfiguration: Dict[str, Any] = None,
    EnvironmentId: str = None,
    Description: str = None,
    OptionSettings: List[Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_environment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L85)

```python
def create_environment(
    ApplicationName: str,
    EnvironmentName: str = None,
    GroupName: str = None,
    Description: str = None,
    CNAMEPrefix: str = None,
    Tier: Dict[str, Any] = None,
    Tags: List[Any] = None,
    VersionLabel: str = None,
    TemplateName: str = None,
    SolutionStackName: str = None,
    PlatformArn: str = None,
    OptionSettings: List[Any] = None,
    OptionsToRemove: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_platform_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L104)

```python
def create_platform_version(
    PlatformName: str,
    PlatformVersion: str,
    PlatformDefinitionBundle: Dict[str, Any],
    EnvironmentName: str = None,
    OptionSettings: List[Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_storage_location

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L116)

```python
def create_storage_location() -> Dict[str, Any]:
```

### Client().delete_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L120)

```python
def delete_application(
    ApplicationName: str,
    TerminateEnvByForce: bool = None,
) -> None:
```

### Client().delete_application_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L126)

```python
def delete_application_version(
    ApplicationName: str,
    VersionLabel: str,
    DeleteSourceBundle: bool = None,
) -> None:
```

### Client().delete_configuration_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L132)

```python
def delete_configuration_template(
    ApplicationName: str,
    TemplateName: str,
) -> None:
```

### Client().delete_environment_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L138)

```python
def delete_environment_configuration(
    ApplicationName: str,
    EnvironmentName: str,
) -> None:
```

### Client().delete_platform_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L144)

```python
def delete_platform_version(PlatformArn: str = None) -> Dict[str, Any]:
```

### Client().describe_account_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L148)

```python
def describe_account_attributes() -> Dict[str, Any]:
```

### Client().describe_application_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L152)

```python
def describe_application_versions(
    ApplicationName: str = None,
    VersionLabels: List[Any] = None,
    MaxRecords: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L162)

```python
def describe_applications(
    ApplicationNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_configuration_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L168)

```python
def describe_configuration_options(
    ApplicationName: str = None,
    TemplateName: str = None,
    EnvironmentName: str = None,
    SolutionStackName: str = None,
    PlatformArn: str = None,
    Options: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_configuration_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L180)

```python
def describe_configuration_settings(
    ApplicationName: str,
    TemplateName: str = None,
    EnvironmentName: str = None,
) -> Dict[str, Any]:
```

### Client().describe_environment_health

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L189)

```python
def describe_environment_health(
    EnvironmentName: str = None,
    EnvironmentId: str = None,
    AttributeNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_environment_managed_action_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L198)

```python
def describe_environment_managed_action_history(
    EnvironmentId: str = None,
    EnvironmentName: str = None,
    NextToken: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().describe_environment_managed_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L208)

```python
def describe_environment_managed_actions(
    EnvironmentName: str = None,
    EnvironmentId: str = None,
    Status: str = None,
) -> Dict[str, Any]:
```

### Client().describe_environment_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L214)

```python
def describe_environment_resources(
    EnvironmentId: str = None,
    EnvironmentName: str = None,
) -> Dict[str, Any]:
```

### Client().describe_environments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L220)

```python
def describe_environments(
    ApplicationName: str = None,
    VersionLabel: str = None,
    EnvironmentIds: List[Any] = None,
    EnvironmentNames: List[Any] = None,
    IncludeDeleted: bool = None,
    IncludedDeletedBackTo: datetime = None,
    MaxRecords: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L234)

```python
def describe_events(
    ApplicationName: str = None,
    VersionLabel: str = None,
    TemplateName: str = None,
    EnvironmentId: str = None,
    EnvironmentName: str = None,
    PlatformArn: str = None,
    RequestId: str = None,
    Severity: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    MaxRecords: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_instances_health

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L252)

```python
def describe_instances_health(
    EnvironmentName: str = None,
    EnvironmentId: str = None,
    AttributeNames: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_platform_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L262)

```python
def describe_platform_version(PlatformArn: str = None) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L266)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L276)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L280)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_available_solution_stacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L284)

```python
def list_available_solution_stacks() -> Dict[str, Any]:
```

### Client().list_platform_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L288)

```python
def list_platform_versions(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L294)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().rebuild_environment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L298)

```python
def rebuild_environment(
    EnvironmentId: str = None,
    EnvironmentName: str = None,
) -> None:
```

### Client().request_environment_info

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L304)

```python
def request_environment_info(
    InfoType: str,
    EnvironmentId: str = None,
    EnvironmentName: str = None,
) -> None:
```

### Client().restart_app_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L310)

```python
def restart_app_server(
    EnvironmentId: str = None,
    EnvironmentName: str = None,
) -> None:
```

### Client().retrieve_environment_info

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L316)

```python
def retrieve_environment_info(
    InfoType: str,
    EnvironmentId: str = None,
    EnvironmentName: str = None,
) -> Dict[str, Any]:
```

### Client().swap_environment_cnames

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L322)

```python
def swap_environment_cnames(
    SourceEnvironmentId: str = None,
    SourceEnvironmentName: str = None,
    DestinationEnvironmentId: str = None,
    DestinationEnvironmentName: str = None,
) -> None:
```

### Client().terminate_environment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L332)

```python
def terminate_environment(
    EnvironmentId: str = None,
    EnvironmentName: str = None,
    TerminateResources: bool = None,
    ForceTerminate: bool = None,
) -> Dict[str, Any]:
```

### Client().update_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L342)

```python
def update_application(
    ApplicationName: str,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().update_application_resource_lifecycle

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L348)

```python
def update_application_resource_lifecycle(
    ApplicationName: str,
    ResourceLifecycleConfig: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_application_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L354)

```python
def update_application_version(
    ApplicationName: str,
    VersionLabel: str,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().update_configuration_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L360)

```python
def update_configuration_template(
    ApplicationName: str,
    TemplateName: str,
    Description: str = None,
    OptionSettings: List[Any] = None,
    OptionsToRemove: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_environment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L371)

```python
def update_environment(
    ApplicationName: str = None,
    EnvironmentId: str = None,
    EnvironmentName: str = None,
    GroupName: str = None,
    Description: str = None,
    Tier: Dict[str, Any] = None,
    VersionLabel: str = None,
    TemplateName: str = None,
    SolutionStackName: str = None,
    PlatformArn: str = None,
    OptionSettings: List[Any] = None,
    OptionsToRemove: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L389)

```python
def update_tags_for_resource(
    ResourceArn: str,
    TagsToAdd: List[Any] = None,
    TagsToRemove: List[Any] = None,
) -> None:
```

### Client().validate_configuration_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/client.py#L398)

```python
def validate_configuration_settings(
    ApplicationName: str,
    OptionSettings: List[Any],
    TemplateName: str = None,
    EnvironmentName: str = None,
) -> Dict[str, Any]:
```
