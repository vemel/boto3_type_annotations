# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codedeploy.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codedeploy](index.md#codedeploy) / Client
    - [Client](#client)
        - [Client().add_tags_to_on_premises_instances](#clientadd_tags_to_on_premises_instances)
        - [Client().batch_get_application_revisions](#clientbatch_get_application_revisions)
        - [Client().batch_get_applications](#clientbatch_get_applications)
        - [Client().batch_get_deployment_groups](#clientbatch_get_deployment_groups)
        - [Client().batch_get_deployment_instances](#clientbatch_get_deployment_instances)
        - [Client().batch_get_deployment_targets](#clientbatch_get_deployment_targets)
        - [Client().batch_get_deployments](#clientbatch_get_deployments)
        - [Client().batch_get_on_premises_instances](#clientbatch_get_on_premises_instances)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().continue_deployment](#clientcontinue_deployment)
        - [Client().create_application](#clientcreate_application)
        - [Client().create_deployment](#clientcreate_deployment)
        - [Client().create_deployment_config](#clientcreate_deployment_config)
        - [Client().create_deployment_group](#clientcreate_deployment_group)
        - [Client().delete_application](#clientdelete_application)
        - [Client().delete_deployment_config](#clientdelete_deployment_config)
        - [Client().delete_deployment_group](#clientdelete_deployment_group)
        - [Client().delete_git_hub_account_token](#clientdelete_git_hub_account_token)
        - [Client().deregister_on_premises_instance](#clientderegister_on_premises_instance)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_application](#clientget_application)
        - [Client().get_application_revision](#clientget_application_revision)
        - [Client().get_deployment](#clientget_deployment)
        - [Client().get_deployment_config](#clientget_deployment_config)
        - [Client().get_deployment_group](#clientget_deployment_group)
        - [Client().get_deployment_instance](#clientget_deployment_instance)
        - [Client().get_deployment_target](#clientget_deployment_target)
        - [Client().get_on_premises_instance](#clientget_on_premises_instance)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_application_revisions](#clientlist_application_revisions)
        - [Client().list_applications](#clientlist_applications)
        - [Client().list_deployment_configs](#clientlist_deployment_configs)
        - [Client().list_deployment_groups](#clientlist_deployment_groups)
        - [Client().list_deployment_instances](#clientlist_deployment_instances)
        - [Client().list_deployment_targets](#clientlist_deployment_targets)
        - [Client().list_deployments](#clientlist_deployments)
        - [Client().list_git_hub_account_token_names](#clientlist_git_hub_account_token_names)
        - [Client().list_on_premises_instances](#clientlist_on_premises_instances)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_lifecycle_event_hook_execution_status](#clientput_lifecycle_event_hook_execution_status)
        - [Client().register_application_revision](#clientregister_application_revision)
        - [Client().register_on_premises_instance](#clientregister_on_premises_instance)
        - [Client().remove_tags_from_on_premises_instances](#clientremove_tags_from_on_premises_instances)
        - [Client().skip_wait_time_for_instance_termination](#clientskip_wait_time_for_instance_termination)
        - [Client().stop_deployment](#clientstop_deployment)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_application](#clientupdate_application)
        - [Client().update_deployment_group](#clientupdate_deployment_group)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_tags_to_on_premises_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L15)

```python
def add_tags_to_on_premises_instances(
    tags: List[Any],
    instanceNames: List[Any],
) -> None:
```

### Client().batch_get_application_revisions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L21)

```python
def batch_get_application_revisions(
    applicationName: str,
    revisions: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_get_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L27)

```python
def batch_get_applications(applicationNames: List[Any]) -> Dict[str, Any]:
```

### Client().batch_get_deployment_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L31)

```python
def batch_get_deployment_groups(
    applicationName: str,
    deploymentGroupNames: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_get_deployment_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L37)

```python
def batch_get_deployment_instances(
    deploymentId: str,
    instanceIds: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_get_deployment_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L43)

```python
def batch_get_deployment_targets(
    deploymentId: str = None,
    targetIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().batch_get_deployments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L49)

```python
def batch_get_deployments(deploymentIds: List[Any]) -> Dict[str, Any]:
```

### Client().batch_get_on_premises_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L53)

```python
def batch_get_on_premises_instances(
    instanceNames: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L59)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().continue_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L63)

```python
def continue_deployment(
    deploymentId: str = None,
    deploymentWaitType: str = None,
) -> None:
```

### Client().create_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L69)

```python
def create_application(
    applicationName: str,
    computePlatform: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L75)

```python
def create_deployment(
    applicationName: str,
    deploymentGroupName: str = None,
    revision: Dict[str, Any] = None,
    deploymentConfigName: str = None,
    description: str = None,
    ignoreApplicationStopFailures: bool = None,
    targetInstances: Dict[str, Any] = None,
    autoRollbackConfiguration: Dict[str, Any] = None,
    updateOutdatedInstancesOnly: bool = None,
    fileExistsBehavior: str = None,
) -> Dict[str, Any]:
```

### Client().create_deployment_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L91)

```python
def create_deployment_config(
    deploymentConfigName: str,
    minimumHealthyHosts: Dict[str, Any] = None,
    trafficRoutingConfig: Dict[str, Any] = None,
    computePlatform: str = None,
) -> Dict[str, Any]:
```

### Client().create_deployment_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L101)

```python
def create_deployment_group(
    applicationName: str,
    deploymentGroupName: str,
    serviceRoleArn: str,
    deploymentConfigName: str = None,
    ec2TagFilters: List[Any] = None,
    onPremisesInstanceTagFilters: List[Any] = None,
    autoScalingGroups: List[Any] = None,
    triggerConfigurations: List[Any] = None,
    alarmConfiguration: Dict[str, Any] = None,
    autoRollbackConfiguration: Dict[str, Any] = None,
    deploymentStyle: Dict[str, Any] = None,
    blueGreenDeploymentConfiguration: Dict[str, Any] = None,
    loadBalancerInfo: Dict[str, Any] = None,
    ec2TagSet: Dict[str, Any] = None,
    ecsServices: List[Any] = None,
    onPremisesTagSet: Dict[str, Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L124)

```python
def delete_application(applicationName: str) -> None:
```

### Client().delete_deployment_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L128)

```python
def delete_deployment_config(deploymentConfigName: str) -> None:
```

### Client().delete_deployment_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L132)

```python
def delete_deployment_group(
    applicationName: str,
    deploymentGroupName: str,
) -> Dict[str, Any]:
```

### Client().delete_git_hub_account_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L138)

```python
def delete_git_hub_account_token(tokenName: str = None) -> Dict[str, Any]:
```

### Client().deregister_on_premises_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L142)

```python
def deregister_on_premises_instance(instanceName: str) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L146)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L156)

```python
def get_application(applicationName: str) -> Dict[str, Any]:
```

### Client().get_application_revision

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L160)

```python
def get_application_revision(
    applicationName: str,
    revision: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().get_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L166)

```python
def get_deployment(deploymentId: str) -> Dict[str, Any]:
```

### Client().get_deployment_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L170)

```python
def get_deployment_config(deploymentConfigName: str) -> Dict[str, Any]:
```

### Client().get_deployment_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L174)

```python
def get_deployment_group(
    applicationName: str,
    deploymentGroupName: str,
) -> Dict[str, Any]:
```

### Client().get_deployment_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L180)

```python
def get_deployment_instance(
    deploymentId: str,
    instanceId: str,
) -> Dict[str, Any]:
```

### Client().get_deployment_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L186)

```python
def get_deployment_target(
    deploymentId: str = None,
    targetId: str = None,
) -> Dict[str, Any]:
```

### Client().get_on_premises_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L192)

```python
def get_on_premises_instance(instanceName: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L196)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L200)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_application_revisions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L204)

```python
def list_application_revisions(
    applicationName: str,
    sortBy: str = None,
    sortOrder: str = None,
    s3Bucket: str = None,
    s3KeyPrefix: str = None,
    deployed: str = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L217)

```python
def list_applications(nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_deployment_configs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L221)

```python
def list_deployment_configs(nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_deployment_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L225)

```python
def list_deployment_groups(
    applicationName: str,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_deployment_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L231)

```python
def list_deployment_instances(
    deploymentId: str,
    nextToken: str = None,
    instanceStatusFilter: List[Any] = None,
    instanceTypeFilter: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_deployment_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L241)

```python
def list_deployment_targets(
    deploymentId: str = None,
    nextToken: str = None,
    targetFilters: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_deployments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L250)

```python
def list_deployments(
    applicationName: str = None,
    deploymentGroupName: str = None,
    includeOnlyStatuses: List[Any] = None,
    createTimeRange: Dict[str, Any] = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_git_hub_account_token_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L261)

```python
def list_git_hub_account_token_names(nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_on_premises_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L265)

```python
def list_on_premises_instances(
    registrationStatus: str = None,
    tagFilters: List[Any] = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L274)

```python
def list_tags_for_resource(
    ResourceArn: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_lifecycle_event_hook_execution_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L280)

```python
def put_lifecycle_event_hook_execution_status(
    deploymentId: str = None,
    lifecycleEventHookExecutionId: str = None,
    status: str = None,
) -> Dict[str, Any]:
```

### Client().register_application_revision

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L289)

```python
def register_application_revision(
    applicationName: str,
    revision: Dict[str, Any],
    description: str = None,
) -> None:
```

### Client().register_on_premises_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L295)

```python
def register_on_premises_instance(
    instanceName: str,
    iamSessionArn: str = None,
    iamUserArn: str = None,
) -> None:
```

### Client().remove_tags_from_on_premises_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L301)

```python
def remove_tags_from_on_premises_instances(
    tags: List[Any],
    instanceNames: List[Any],
) -> None:
```

### Client().skip_wait_time_for_instance_termination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L307)

```python
def skip_wait_time_for_instance_termination(deploymentId: str = None) -> None:
```

### Client().stop_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L311)

```python
def stop_deployment(
    deploymentId: str,
    autoRollbackEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L317)

```python
def tag_resource(ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L321)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L325)

```python
def update_application(
    applicationName: str = None,
    newApplicationName: str = None,
) -> None:
```

### Client().update_deployment_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/client.py#L331)

```python
def update_deployment_group(
    applicationName: str,
    currentDeploymentGroupName: str,
    newDeploymentGroupName: str = None,
    deploymentConfigName: str = None,
    ec2TagFilters: List[Any] = None,
    onPremisesInstanceTagFilters: List[Any] = None,
    autoScalingGroups: List[Any] = None,
    serviceRoleArn: str = None,
    triggerConfigurations: List[Any] = None,
    alarmConfiguration: Dict[str, Any] = None,
    autoRollbackConfiguration: Dict[str, Any] = None,
    deploymentStyle: Dict[str, Any] = None,
    blueGreenDeploymentConfiguration: Dict[str, Any] = None,
    loadBalancerInfo: Dict[str, Any] = None,
    ec2TagSet: Dict[str, Any] = None,
    ecsServices: List[Any] = None,
    onPremisesTagSet: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
