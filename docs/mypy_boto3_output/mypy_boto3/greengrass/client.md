# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.greengrass.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Greengrass](index.md#greengrass) / Client
    - [Client](#client)
        - [Client().associate_role_to_group](#clientassociate_role_to_group)
        - [Client().associate_service_role_to_account](#clientassociate_service_role_to_account)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_connector_definition](#clientcreate_connector_definition)
        - [Client().create_connector_definition_version](#clientcreate_connector_definition_version)
        - [Client().create_core_definition](#clientcreate_core_definition)
        - [Client().create_core_definition_version](#clientcreate_core_definition_version)
        - [Client().create_deployment](#clientcreate_deployment)
        - [Client().create_device_definition](#clientcreate_device_definition)
        - [Client().create_device_definition_version](#clientcreate_device_definition_version)
        - [Client().create_function_definition](#clientcreate_function_definition)
        - [Client().create_function_definition_version](#clientcreate_function_definition_version)
        - [Client().create_group](#clientcreate_group)
        - [Client().create_group_certificate_authority](#clientcreate_group_certificate_authority)
        - [Client().create_group_version](#clientcreate_group_version)
        - [Client().create_logger_definition](#clientcreate_logger_definition)
        - [Client().create_logger_definition_version](#clientcreate_logger_definition_version)
        - [Client().create_resource_definition](#clientcreate_resource_definition)
        - [Client().create_resource_definition_version](#clientcreate_resource_definition_version)
        - [Client().create_software_update_job](#clientcreate_software_update_job)
        - [Client().create_subscription_definition](#clientcreate_subscription_definition)
        - [Client().create_subscription_definition_version](#clientcreate_subscription_definition_version)
        - [Client().delete_connector_definition](#clientdelete_connector_definition)
        - [Client().delete_core_definition](#clientdelete_core_definition)
        - [Client().delete_device_definition](#clientdelete_device_definition)
        - [Client().delete_function_definition](#clientdelete_function_definition)
        - [Client().delete_group](#clientdelete_group)
        - [Client().delete_logger_definition](#clientdelete_logger_definition)
        - [Client().delete_resource_definition](#clientdelete_resource_definition)
        - [Client().delete_subscription_definition](#clientdelete_subscription_definition)
        - [Client().disassociate_role_from_group](#clientdisassociate_role_from_group)
        - [Client().disassociate_service_role_from_account](#clientdisassociate_service_role_from_account)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_associated_role](#clientget_associated_role)
        - [Client().get_bulk_deployment_status](#clientget_bulk_deployment_status)
        - [Client().get_connectivity_info](#clientget_connectivity_info)
        - [Client().get_connector_definition](#clientget_connector_definition)
        - [Client().get_connector_definition_version](#clientget_connector_definition_version)
        - [Client().get_core_definition](#clientget_core_definition)
        - [Client().get_core_definition_version](#clientget_core_definition_version)
        - [Client().get_deployment_status](#clientget_deployment_status)
        - [Client().get_device_definition](#clientget_device_definition)
        - [Client().get_device_definition_version](#clientget_device_definition_version)
        - [Client().get_function_definition](#clientget_function_definition)
        - [Client().get_function_definition_version](#clientget_function_definition_version)
        - [Client().get_group](#clientget_group)
        - [Client().get_group_certificate_authority](#clientget_group_certificate_authority)
        - [Client().get_group_certificate_configuration](#clientget_group_certificate_configuration)
        - [Client().get_group_version](#clientget_group_version)
        - [Client().get_logger_definition](#clientget_logger_definition)
        - [Client().get_logger_definition_version](#clientget_logger_definition_version)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_resource_definition](#clientget_resource_definition)
        - [Client().get_resource_definition_version](#clientget_resource_definition_version)
        - [Client().get_service_role_for_account](#clientget_service_role_for_account)
        - [Client().get_subscription_definition](#clientget_subscription_definition)
        - [Client().get_subscription_definition_version](#clientget_subscription_definition_version)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_bulk_deployment_detailed_reports](#clientlist_bulk_deployment_detailed_reports)
        - [Client().list_bulk_deployments](#clientlist_bulk_deployments)
        - [Client().list_connector_definition_versions](#clientlist_connector_definition_versions)
        - [Client().list_connector_definitions](#clientlist_connector_definitions)
        - [Client().list_core_definition_versions](#clientlist_core_definition_versions)
        - [Client().list_core_definitions](#clientlist_core_definitions)
        - [Client().list_deployments](#clientlist_deployments)
        - [Client().list_device_definition_versions](#clientlist_device_definition_versions)
        - [Client().list_device_definitions](#clientlist_device_definitions)
        - [Client().list_function_definition_versions](#clientlist_function_definition_versions)
        - [Client().list_function_definitions](#clientlist_function_definitions)
        - [Client().list_group_certificate_authorities](#clientlist_group_certificate_authorities)
        - [Client().list_group_versions](#clientlist_group_versions)
        - [Client().list_groups](#clientlist_groups)
        - [Client().list_logger_definition_versions](#clientlist_logger_definition_versions)
        - [Client().list_logger_definitions](#clientlist_logger_definitions)
        - [Client().list_resource_definition_versions](#clientlist_resource_definition_versions)
        - [Client().list_resource_definitions](#clientlist_resource_definitions)
        - [Client().list_subscription_definition_versions](#clientlist_subscription_definition_versions)
        - [Client().list_subscription_definitions](#clientlist_subscription_definitions)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().reset_deployments](#clientreset_deployments)
        - [Client().start_bulk_deployment](#clientstart_bulk_deployment)
        - [Client().stop_bulk_deployment](#clientstop_bulk_deployment)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_connectivity_info](#clientupdate_connectivity_info)
        - [Client().update_connector_definition](#clientupdate_connector_definition)
        - [Client().update_core_definition](#clientupdate_core_definition)
        - [Client().update_device_definition](#clientupdate_device_definition)
        - [Client().update_function_definition](#clientupdate_function_definition)
        - [Client().update_group](#clientupdate_group)
        - [Client().update_group_certificate_configuration](#clientupdate_group_certificate_configuration)
        - [Client().update_logger_definition](#clientupdate_logger_definition)
        - [Client().update_resource_definition](#clientupdate_resource_definition)
        - [Client().update_subscription_definition](#clientupdate_subscription_definition)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_role_to_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L15)

```python
def associate_role_to_group(GroupId: str, RoleArn: str) -> Dict[str, Any]:
```

### Client().associate_service_role_to_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L19)

```python
def associate_service_role_to_account(RoleArn: str) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L23)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_connector_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L27)

```python
def create_connector_definition(
    AmznClientToken: str = None,
    InitialVersion: Dict[str, Any] = None,
    Name: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_connector_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L37)

```python
def create_connector_definition_version(
    ConnectorDefinitionId: str,
    AmznClientToken: str = None,
    Connectors: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_core_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L46)

```python
def create_core_definition(
    AmznClientToken: str = None,
    InitialVersion: Dict[str, Any] = None,
    Name: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_core_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L56)

```python
def create_core_definition_version(
    CoreDefinitionId: str,
    AmznClientToken: str = None,
    Cores: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L65)

```python
def create_deployment(
    DeploymentType: str,
    GroupId: str,
    AmznClientToken: str = None,
    DeploymentId: str = None,
    GroupVersionId: str = None,
) -> Dict[str, Any]:
```

### Client().create_device_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L76)

```python
def create_device_definition(
    AmznClientToken: str = None,
    InitialVersion: Dict[str, Any] = None,
    Name: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_device_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L86)

```python
def create_device_definition_version(
    DeviceDefinitionId: str,
    AmznClientToken: str = None,
    Devices: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_function_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L95)

```python
def create_function_definition(
    AmznClientToken: str = None,
    InitialVersion: Dict[str, Any] = None,
    Name: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_function_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L105)

```python
def create_function_definition_version(
    FunctionDefinitionId: str,
    AmznClientToken: str = None,
    DefaultConfig: Dict[str, Any] = None,
    Functions: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L115)

```python
def create_group(
    AmznClientToken: str = None,
    InitialVersion: Dict[str, Any] = None,
    Name: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_group_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L125)

```python
def create_group_certificate_authority(
    GroupId: str,
    AmznClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_group_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L131)

```python
def create_group_version(
    GroupId: str,
    AmznClientToken: str = None,
    ConnectorDefinitionVersionArn: str = None,
    CoreDefinitionVersionArn: str = None,
    DeviceDefinitionVersionArn: str = None,
    FunctionDefinitionVersionArn: str = None,
    LoggerDefinitionVersionArn: str = None,
    ResourceDefinitionVersionArn: str = None,
    SubscriptionDefinitionVersionArn: str = None,
) -> Dict[str, Any]:
```

### Client().create_logger_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L146)

```python
def create_logger_definition(
    AmznClientToken: str = None,
    InitialVersion: Dict[str, Any] = None,
    Name: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_logger_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L156)

```python
def create_logger_definition_version(
    LoggerDefinitionId: str,
    AmznClientToken: str = None,
    Loggers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_resource_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L165)

```python
def create_resource_definition(
    AmznClientToken: str = None,
    InitialVersion: Dict[str, Any] = None,
    Name: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_resource_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L175)

```python
def create_resource_definition_version(
    ResourceDefinitionId: str,
    AmznClientToken: str = None,
    Resources: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_software_update_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L184)

```python
def create_software_update_job(
    S3UrlSignerRole: str,
    SoftwareToUpdate: str,
    UpdateTargets: List[Any],
    UpdateTargetsArchitecture: str,
    UpdateTargetsOperatingSystem: str,
    AmznClientToken: str = None,
    UpdateAgentLogLevel: str = None,
) -> Dict[str, Any]:
```

### Client().create_subscription_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L197)

```python
def create_subscription_definition(
    AmznClientToken: str = None,
    InitialVersion: Dict[str, Any] = None,
    Name: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_subscription_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L207)

```python
def create_subscription_definition_version(
    SubscriptionDefinitionId: str,
    AmznClientToken: str = None,
    Subscriptions: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_connector_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L216)

```python
def delete_connector_definition(ConnectorDefinitionId: str) -> Dict[str, Any]:
```

### Client().delete_core_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L220)

```python
def delete_core_definition(CoreDefinitionId: str) -> Dict[str, Any]:
```

### Client().delete_device_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L224)

```python
def delete_device_definition(DeviceDefinitionId: str) -> Dict[str, Any]:
```

### Client().delete_function_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L228)

```python
def delete_function_definition(FunctionDefinitionId: str) -> Dict[str, Any]:
```

### Client().delete_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L232)

```python
def delete_group(GroupId: str) -> Dict[str, Any]:
```

### Client().delete_logger_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L236)

```python
def delete_logger_definition(LoggerDefinitionId: str) -> Dict[str, Any]:
```

### Client().delete_resource_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L240)

```python
def delete_resource_definition(ResourceDefinitionId: str) -> Dict[str, Any]:
```

### Client().delete_subscription_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L244)

```python
def delete_subscription_definition(
    SubscriptionDefinitionId: str,
) -> Dict[str, Any]:
```

### Client().disassociate_role_from_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L250)

```python
def disassociate_role_from_group(GroupId: str) -> Dict[str, Any]:
```

### Client().disassociate_service_role_from_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L254)

```python
def disassociate_service_role_from_account() -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L258)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_associated_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L268)

```python
def get_associated_role(GroupId: str) -> Dict[str, Any]:
```

### Client().get_bulk_deployment_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L272)

```python
def get_bulk_deployment_status(BulkDeploymentId: str) -> Dict[str, Any]:
```

### Client().get_connectivity_info

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L276)

```python
def get_connectivity_info(ThingName: str) -> Dict[str, Any]:
```

### Client().get_connector_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L280)

```python
def get_connector_definition(ConnectorDefinitionId: str) -> Dict[str, Any]:
```

### Client().get_connector_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L284)

```python
def get_connector_definition_version(
    ConnectorDefinitionId: str,
    ConnectorDefinitionVersionId: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_core_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L293)

```python
def get_core_definition(CoreDefinitionId: str) -> Dict[str, Any]:
```

### Client().get_core_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L297)

```python
def get_core_definition_version(
    CoreDefinitionId: str,
    CoreDefinitionVersionId: str,
) -> Dict[str, Any]:
```

### Client().get_deployment_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L303)

```python
def get_deployment_status(DeploymentId: str, GroupId: str) -> Dict[str, Any]:
```

### Client().get_device_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L307)

```python
def get_device_definition(DeviceDefinitionId: str) -> Dict[str, Any]:
```

### Client().get_device_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L311)

```python
def get_device_definition_version(
    DeviceDefinitionId: str,
    DeviceDefinitionVersionId: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_function_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L320)

```python
def get_function_definition(FunctionDefinitionId: str) -> Dict[str, Any]:
```

### Client().get_function_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L324)

```python
def get_function_definition_version(
    FunctionDefinitionId: str,
    FunctionDefinitionVersionId: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L333)

```python
def get_group(GroupId: str) -> Dict[str, Any]:
```

### Client().get_group_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L337)

```python
def get_group_certificate_authority(
    CertificateAuthorityId: str,
    GroupId: str,
) -> Dict[str, Any]:
```

### Client().get_group_certificate_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L343)

```python
def get_group_certificate_configuration(GroupId: str) -> Dict[str, Any]:
```

### Client().get_group_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L347)

```python
def get_group_version(GroupId: str, GroupVersionId: str) -> Dict[str, Any]:
```

### Client().get_logger_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L351)

```python
def get_logger_definition(LoggerDefinitionId: str) -> Dict[str, Any]:
```

### Client().get_logger_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L355)

```python
def get_logger_definition_version(
    LoggerDefinitionId: str,
    LoggerDefinitionVersionId: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L364)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_resource_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L368)

```python
def get_resource_definition(ResourceDefinitionId: str) -> Dict[str, Any]:
```

### Client().get_resource_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L372)

```python
def get_resource_definition_version(
    ResourceDefinitionId: str,
    ResourceDefinitionVersionId: str,
) -> Dict[str, Any]:
```

### Client().get_service_role_for_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L378)

```python
def get_service_role_for_account() -> Dict[str, Any]:
```

### Client().get_subscription_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L382)

```python
def get_subscription_definition(
    SubscriptionDefinitionId: str,
) -> Dict[str, Any]:
```

### Client().get_subscription_definition_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L388)

```python
def get_subscription_definition_version(
    SubscriptionDefinitionId: str,
    SubscriptionDefinitionVersionId: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L397)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_bulk_deployment_detailed_reports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L401)

```python
def list_bulk_deployment_detailed_reports(
    BulkDeploymentId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_bulk_deployments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L407)

```python
def list_bulk_deployments(
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_connector_definition_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L413)

```python
def list_connector_definition_versions(
    ConnectorDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_connector_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L419)

```python
def list_connector_definitions(
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_core_definition_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L425)

```python
def list_core_definition_versions(
    CoreDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_core_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L431)

```python
def list_core_definitions(
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_deployments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L437)

```python
def list_deployments(
    GroupId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_device_definition_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L443)

```python
def list_device_definition_versions(
    DeviceDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_device_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L449)

```python
def list_device_definitions(
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_function_definition_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L455)

```python
def list_function_definition_versions(
    FunctionDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_function_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L461)

```python
def list_function_definitions(
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_group_certificate_authorities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L467)

```python
def list_group_certificate_authorities(GroupId: str) -> Dict[str, Any]:
```

### Client().list_group_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L471)

```python
def list_group_versions(
    GroupId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L477)

```python
def list_groups(
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_logger_definition_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L483)

```python
def list_logger_definition_versions(
    LoggerDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_logger_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L489)

```python
def list_logger_definitions(
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_resource_definition_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L495)

```python
def list_resource_definition_versions(
    ResourceDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_resource_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L501)

```python
def list_resource_definitions(
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_subscription_definition_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L507)

```python
def list_subscription_definition_versions(
    SubscriptionDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_subscription_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L516)

```python
def list_subscription_definitions(
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L522)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().reset_deployments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L526)

```python
def reset_deployments(
    GroupId: str,
    AmznClientToken: str = None,
    Force: bool = None,
) -> Dict[str, Any]:
```

### Client().start_bulk_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L532)

```python
def start_bulk_deployment(
    ExecutionRoleArn: str,
    InputFileUri: str,
    AmznClientToken: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().stop_bulk_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L542)

```python
def stop_bulk_deployment(BulkDeploymentId: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L546)

```python
def tag_resource(ResourceArn: str, tags: Dict[str, Any] = None) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L550)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().update_connectivity_info

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L554)

```python
def update_connectivity_info(
    ThingName: str,
    ConnectivityInfo: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_connector_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L560)

```python
def update_connector_definition(
    ConnectorDefinitionId: str,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().update_core_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L566)

```python
def update_core_definition(
    CoreDefinitionId: str,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().update_device_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L572)

```python
def update_device_definition(
    DeviceDefinitionId: str,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().update_function_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L578)

```python
def update_function_definition(
    FunctionDefinitionId: str,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().update_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L584)

```python
def update_group(GroupId: str, Name: str = None) -> Dict[str, Any]:
```

### Client().update_group_certificate_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L588)

```python
def update_group_certificate_configuration(
    GroupId: str,
    CertificateExpiryInMilliseconds: str = None,
) -> Dict[str, Any]:
```

### Client().update_logger_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L594)

```python
def update_logger_definition(
    LoggerDefinitionId: str,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().update_resource_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L600)

```python
def update_resource_definition(
    ResourceDefinitionId: str,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().update_subscription_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/greengrass/client.py#L606)

```python
def update_subscription_definition(
    SubscriptionDefinitionId: str,
    Name: str = None,
) -> Dict[str, Any]:
```
