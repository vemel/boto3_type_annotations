# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.opsworks.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Opsworks](index.md#opsworks) / Client
    - [Client](#client)
        - [Client().assign_instance](#clientassign_instance)
        - [Client().assign_volume](#clientassign_volume)
        - [Client().associate_elastic_ip](#clientassociate_elastic_ip)
        - [Client().attach_elastic_load_balancer](#clientattach_elastic_load_balancer)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().clone_stack](#clientclone_stack)
        - [Client().create_app](#clientcreate_app)
        - [Client().create_deployment](#clientcreate_deployment)
        - [Client().create_instance](#clientcreate_instance)
        - [Client().create_layer](#clientcreate_layer)
        - [Client().create_stack](#clientcreate_stack)
        - [Client().create_user_profile](#clientcreate_user_profile)
        - [Client().delete_app](#clientdelete_app)
        - [Client().delete_instance](#clientdelete_instance)
        - [Client().delete_layer](#clientdelete_layer)
        - [Client().delete_stack](#clientdelete_stack)
        - [Client().delete_user_profile](#clientdelete_user_profile)
        - [Client().deregister_ecs_cluster](#clientderegister_ecs_cluster)
        - [Client().deregister_elastic_ip](#clientderegister_elastic_ip)
        - [Client().deregister_instance](#clientderegister_instance)
        - [Client().deregister_rds_db_instance](#clientderegister_rds_db_instance)
        - [Client().deregister_volume](#clientderegister_volume)
        - [Client().describe_agent_versions](#clientdescribe_agent_versions)
        - [Client().describe_apps](#clientdescribe_apps)
        - [Client().describe_commands](#clientdescribe_commands)
        - [Client().describe_deployments](#clientdescribe_deployments)
        - [Client().describe_ecs_clusters](#clientdescribe_ecs_clusters)
        - [Client().describe_elastic_ips](#clientdescribe_elastic_ips)
        - [Client().describe_elastic_load_balancers](#clientdescribe_elastic_load_balancers)
        - [Client().describe_instances](#clientdescribe_instances)
        - [Client().describe_layers](#clientdescribe_layers)
        - [Client().describe_load_based_auto_scaling](#clientdescribe_load_based_auto_scaling)
        - [Client().describe_my_user_profile](#clientdescribe_my_user_profile)
        - [Client().describe_operating_systems](#clientdescribe_operating_systems)
        - [Client().describe_permissions](#clientdescribe_permissions)
        - [Client().describe_raid_arrays](#clientdescribe_raid_arrays)
        - [Client().describe_rds_db_instances](#clientdescribe_rds_db_instances)
        - [Client().describe_service_errors](#clientdescribe_service_errors)
        - [Client().describe_stack_provisioning_parameters](#clientdescribe_stack_provisioning_parameters)
        - [Client().describe_stack_summary](#clientdescribe_stack_summary)
        - [Client().describe_stacks](#clientdescribe_stacks)
        - [Client().describe_time_based_auto_scaling](#clientdescribe_time_based_auto_scaling)
        - [Client().describe_user_profiles](#clientdescribe_user_profiles)
        - [Client().describe_volumes](#clientdescribe_volumes)
        - [Client().detach_elastic_load_balancer](#clientdetach_elastic_load_balancer)
        - [Client().disassociate_elastic_ip](#clientdisassociate_elastic_ip)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_hostname_suggestion](#clientget_hostname_suggestion)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().grant_access](#clientgrant_access)
        - [Client().list_tags](#clientlist_tags)
        - [Client().reboot_instance](#clientreboot_instance)
        - [Client().register_ecs_cluster](#clientregister_ecs_cluster)
        - [Client().register_elastic_ip](#clientregister_elastic_ip)
        - [Client().register_instance](#clientregister_instance)
        - [Client().register_rds_db_instance](#clientregister_rds_db_instance)
        - [Client().register_volume](#clientregister_volume)
        - [Client().set_load_based_auto_scaling](#clientset_load_based_auto_scaling)
        - [Client().set_permission](#clientset_permission)
        - [Client().set_time_based_auto_scaling](#clientset_time_based_auto_scaling)
        - [Client().start_instance](#clientstart_instance)
        - [Client().start_stack](#clientstart_stack)
        - [Client().stop_instance](#clientstop_instance)
        - [Client().stop_stack](#clientstop_stack)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().unassign_instance](#clientunassign_instance)
        - [Client().unassign_volume](#clientunassign_volume)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_app](#clientupdate_app)
        - [Client().update_elastic_ip](#clientupdate_elastic_ip)
        - [Client().update_instance](#clientupdate_instance)
        - [Client().update_layer](#clientupdate_layer)
        - [Client().update_my_user_profile](#clientupdate_my_user_profile)
        - [Client().update_rds_db_instance](#clientupdate_rds_db_instance)
        - [Client().update_stack](#clientupdate_stack)
        - [Client().update_user_profile](#clientupdate_user_profile)
        - [Client().update_volume](#clientupdate_volume)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L12)

```python
class Client(BaseClient):
```

### Client().assign_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L15)

```python
def assign_instance(InstanceId: str, LayerIds: List[Any]) -> None:
```

### Client().assign_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L19)

```python
def assign_volume(VolumeId: str, InstanceId: str = None) -> None:
```

### Client().associate_elastic_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L23)

```python
def associate_elastic_ip(ElasticIp: str, InstanceId: str = None) -> None:
```

### Client().attach_elastic_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L27)

```python
def attach_elastic_load_balancer(
    ElasticLoadBalancerName: str,
    LayerId: str,
) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L33)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().clone_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L37)

```python
def clone_stack(
    SourceStackId: str,
    ServiceRoleArn: str,
    Name: str = None,
    Region: str = None,
    VpcId: str = None,
    Attributes: Dict[str, Any] = None,
    DefaultInstanceProfileArn: str = None,
    DefaultOs: str = None,
    HostnameTheme: str = None,
    DefaultAvailabilityZone: str = None,
    DefaultSubnetId: str = None,
    CustomJson: str = None,
    ConfigurationManager: Dict[str, Any] = None,
    ChefConfiguration: Dict[str, Any] = None,
    UseCustomCookbooks: bool = None,
    UseOpsworksSecurityGroups: bool = None,
    CustomCookbooksSource: Dict[str, Any] = None,
    DefaultSshKeyName: str = None,
    ClonePermissions: bool = None,
    CloneAppIds: List[Any] = None,
    DefaultRootDeviceType: str = None,
    AgentVersion: str = None,
) -> Dict[str, Any]:
```

### Client().create_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L65)

```python
def create_app(
    StackId: str,
    Name: str,
    Type: str,
    Shortname: str = None,
    Description: str = None,
    DataSources: List[Any] = None,
    AppSource: Dict[str, Any] = None,
    Domains: List[Any] = None,
    EnableSsl: bool = None,
    SslConfiguration: Dict[str, Any] = None,
    Attributes: Dict[str, Any] = None,
    Environment: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L83)

```python
def create_deployment(
    StackId: str,
    Command: Dict[str, Any],
    AppId: str = None,
    InstanceIds: List[Any] = None,
    LayerIds: List[Any] = None,
    Comment: str = None,
    CustomJson: str = None,
) -> Dict[str, Any]:
```

### Client().create_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L96)

```python
def create_instance(
    StackId: str,
    LayerIds: List[Any],
    InstanceType: str,
    AutoScalingType: str = None,
    Hostname: str = None,
    Os: str = None,
    AmiId: str = None,
    SshKeyName: str = None,
    AvailabilityZone: str = None,
    VirtualizationType: str = None,
    SubnetId: str = None,
    Architecture: str = None,
    RootDeviceType: str = None,
    BlockDeviceMappings: List[Any] = None,
    InstallUpdatesOnBoot: bool = None,
    EbsOptimized: bool = None,
    AgentVersion: str = None,
    Tenancy: str = None,
) -> Dict[str, Any]:
```

### Client().create_layer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L120)

```python
def create_layer(
    StackId: str,
    Type: str,
    Name: str,
    Shortname: str,
    Attributes: Dict[str, Any] = None,
    CloudWatchLogsConfiguration: Dict[str, Any] = None,
    CustomInstanceProfileArn: str = None,
    CustomJson: str = None,
    CustomSecurityGroupIds: List[Any] = None,
    Packages: List[Any] = None,
    VolumeConfigurations: List[Any] = None,
    EnableAutoHealing: bool = None,
    AutoAssignElasticIps: bool = None,
    AutoAssignPublicIps: bool = None,
    CustomRecipes: Dict[str, Any] = None,
    InstallUpdatesOnBoot: bool = None,
    UseEbsOptimizedInstances: bool = None,
    LifecycleEventConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L144)

```python
def create_stack(
    Name: str,
    Region: str,
    ServiceRoleArn: str,
    DefaultInstanceProfileArn: str,
    VpcId: str = None,
    Attributes: Dict[str, Any] = None,
    DefaultOs: str = None,
    HostnameTheme: str = None,
    DefaultAvailabilityZone: str = None,
    DefaultSubnetId: str = None,
    CustomJson: str = None,
    ConfigurationManager: Dict[str, Any] = None,
    ChefConfiguration: Dict[str, Any] = None,
    UseCustomCookbooks: bool = None,
    UseOpsworksSecurityGroups: bool = None,
    CustomCookbooksSource: Dict[str, Any] = None,
    DefaultSshKeyName: str = None,
    DefaultRootDeviceType: str = None,
    AgentVersion: str = None,
) -> Dict[str, Any]:
```

### Client().create_user_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L169)

```python
def create_user_profile(
    IamUserArn: str,
    SshUsername: str = None,
    SshPublicKey: str = None,
    AllowSelfManagement: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L179)

```python
def delete_app(AppId: str) -> None:
```

### Client().delete_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L183)

```python
def delete_instance(
    InstanceId: str,
    DeleteElasticIp: bool = None,
    DeleteVolumes: bool = None,
) -> None:
```

### Client().delete_layer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L189)

```python
def delete_layer(LayerId: str) -> None:
```

### Client().delete_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L193)

```python
def delete_stack(StackId: str) -> None:
```

### Client().delete_user_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L197)

```python
def delete_user_profile(IamUserArn: str) -> None:
```

### Client().deregister_ecs_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L201)

```python
def deregister_ecs_cluster(EcsClusterArn: str) -> None:
```

### Client().deregister_elastic_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L205)

```python
def deregister_elastic_ip(ElasticIp: str) -> None:
```

### Client().deregister_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L209)

```python
def deregister_instance(InstanceId: str) -> None:
```

### Client().deregister_rds_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L213)

```python
def deregister_rds_db_instance(RdsDbInstanceArn: str) -> None:
```

### Client().deregister_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L217)

```python
def deregister_volume(VolumeId: str) -> None:
```

### Client().describe_agent_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L221)

```python
def describe_agent_versions(
    StackId: str = None,
    ConfigurationManager: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_apps

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L227)

```python
def describe_apps(
    StackId: str = None,
    AppIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_commands

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L233)

```python
def describe_commands(
    DeploymentId: str = None,
    InstanceId: str = None,
    CommandIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_deployments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L242)

```python
def describe_deployments(
    StackId: str = None,
    AppId: str = None,
    DeploymentIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_ecs_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L248)

```python
def describe_ecs_clusters(
    EcsClusterArns: List[Any] = None,
    StackId: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_elastic_ips

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L258)

```python
def describe_elastic_ips(
    InstanceId: str = None,
    StackId: str = None,
    Ips: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_elastic_load_balancers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L264)

```python
def describe_elastic_load_balancers(
    StackId: str = None,
    LayerIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L270)

```python
def describe_instances(
    StackId: str = None,
    LayerId: str = None,
    InstanceIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_layers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L276)

```python
def describe_layers(
    StackId: str = None,
    LayerIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_load_based_auto_scaling

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L282)

```python
def describe_load_based_auto_scaling(LayerIds: List[Any]) -> Dict[str, Any]:
```

### Client().describe_my_user_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L286)

```python
def describe_my_user_profile() -> Dict[str, Any]:
```

### Client().describe_operating_systems

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L290)

```python
def describe_operating_systems() -> Dict[str, Any]:
```

### Client().describe_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L294)

```python
def describe_permissions(
    IamUserArn: str = None,
    StackId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_raid_arrays

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L300)

```python
def describe_raid_arrays(
    InstanceId: str = None,
    StackId: str = None,
    RaidArrayIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_rds_db_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L309)

```python
def describe_rds_db_instances(
    StackId: str,
    RdsDbInstanceArns: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_service_errors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L315)

```python
def describe_service_errors(
    StackId: str = None,
    InstanceId: str = None,
    ServiceErrorIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_stack_provisioning_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L324)

```python
def describe_stack_provisioning_parameters(StackId: str) -> Dict[str, Any]:
```

### Client().describe_stack_summary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L328)

```python
def describe_stack_summary(StackId: str) -> Dict[str, Any]:
```

### Client().describe_stacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L332)

```python
def describe_stacks(StackIds: List[Any] = None) -> Dict[str, Any]:
```

### Client().describe_time_based_auto_scaling

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L336)

```python
def describe_time_based_auto_scaling(
    InstanceIds: List[Any],
) -> Dict[str, Any]:
```

### Client().describe_user_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L342)

```python
def describe_user_profiles(IamUserArns: List[Any] = None) -> Dict[str, Any]:
```

### Client().describe_volumes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L346)

```python
def describe_volumes(
    InstanceId: str = None,
    StackId: str = None,
    RaidArrayId: str = None,
    VolumeIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().detach_elastic_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L356)

```python
def detach_elastic_load_balancer(
    ElasticLoadBalancerName: str,
    LayerId: str,
) -> None:
```

### Client().disassociate_elastic_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L362)

```python
def disassociate_elastic_ip(ElasticIp: str) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L366)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_hostname_suggestion

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L376)

```python
def get_hostname_suggestion(LayerId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L380)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L384)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().grant_access

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L388)

```python
def grant_access(
    InstanceId: str,
    ValidForInMinutes: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L394)

```python
def list_tags(
    ResourceArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().reboot_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L400)

```python
def reboot_instance(InstanceId: str) -> None:
```

### Client().register_ecs_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L404)

```python
def register_ecs_cluster(EcsClusterArn: str, StackId: str) -> Dict[str, Any]:
```

### Client().register_elastic_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L408)

```python
def register_elastic_ip(ElasticIp: str, StackId: str) -> Dict[str, Any]:
```

### Client().register_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L412)

```python
def register_instance(
    StackId: str,
    Hostname: str = None,
    PublicIp: str = None,
    PrivateIp: str = None,
    RsaPublicKey: str = None,
    RsaPublicKeyFingerprint: str = None,
    InstanceIdentity: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().register_rds_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L425)

```python
def register_rds_db_instance(
    StackId: str,
    RdsDbInstanceArn: str,
    DbUser: str,
    DbPassword: str,
) -> None:
```

### Client().register_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L431)

```python
def register_volume(StackId: str, Ec2VolumeId: str = None) -> Dict[str, Any]:
```

### Client().set_load_based_auto_scaling

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L435)

```python
def set_load_based_auto_scaling(
    LayerId: str,
    Enable: bool = None,
    UpScaling: Dict[str, Any] = None,
    DownScaling: Dict[str, Any] = None,
) -> None:
```

### Client().set_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L445)

```python
def set_permission(
    StackId: str,
    IamUserArn: str,
    AllowSsh: bool = None,
    AllowSudo: bool = None,
    Level: str = None,
) -> None:
```

### Client().set_time_based_auto_scaling

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L456)

```python
def set_time_based_auto_scaling(
    InstanceId: str,
    AutoScalingSchedule: Dict[str, Any] = None,
) -> None:
```

### Client().start_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L462)

```python
def start_instance(InstanceId: str) -> None:
```

### Client().start_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L466)

```python
def start_stack(StackId: str) -> None:
```

### Client().stop_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L470)

```python
def stop_instance(InstanceId: str, Force: bool = None) -> None:
```

### Client().stop_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L474)

```python
def stop_stack(StackId: str) -> None:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L478)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> None:
```

### Client().unassign_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L482)

```python
def unassign_instance(InstanceId: str) -> None:
```

### Client().unassign_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L486)

```python
def unassign_volume(VolumeId: str) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L490)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().update_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L494)

```python
def update_app(
    AppId: str,
    Name: str = None,
    Description: str = None,
    DataSources: List[Any] = None,
    Type: str = None,
    AppSource: Dict[str, Any] = None,
    Domains: List[Any] = None,
    EnableSsl: bool = None,
    SslConfiguration: Dict[str, Any] = None,
    Attributes: Dict[str, Any] = None,
    Environment: List[Any] = None,
) -> None:
```

### Client().update_elastic_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L511)

```python
def update_elastic_ip(ElasticIp: str, Name: str = None) -> None:
```

### Client().update_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L515)

```python
def update_instance(
    InstanceId: str,
    LayerIds: List[Any] = None,
    InstanceType: str = None,
    AutoScalingType: str = None,
    Hostname: str = None,
    Os: str = None,
    AmiId: str = None,
    SshKeyName: str = None,
    Architecture: str = None,
    InstallUpdatesOnBoot: bool = None,
    EbsOptimized: bool = None,
    AgentVersion: str = None,
) -> None:
```

### Client().update_layer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L533)

```python
def update_layer(
    LayerId: str,
    Name: str = None,
    Shortname: str = None,
    Attributes: Dict[str, Any] = None,
    CloudWatchLogsConfiguration: Dict[str, Any] = None,
    CustomInstanceProfileArn: str = None,
    CustomJson: str = None,
    CustomSecurityGroupIds: List[Any] = None,
    Packages: List[Any] = None,
    VolumeConfigurations: List[Any] = None,
    EnableAutoHealing: bool = None,
    AutoAssignElasticIps: bool = None,
    AutoAssignPublicIps: bool = None,
    CustomRecipes: Dict[str, Any] = None,
    InstallUpdatesOnBoot: bool = None,
    UseEbsOptimizedInstances: bool = None,
    LifecycleEventConfiguration: Dict[str, Any] = None,
) -> None:
```

### Client().update_my_user_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L556)

```python
def update_my_user_profile(SshPublicKey: str = None) -> None:
```

### Client().update_rds_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L560)

```python
def update_rds_db_instance(
    RdsDbInstanceArn: str,
    DbUser: str = None,
    DbPassword: str = None,
) -> None:
```

### Client().update_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L566)

```python
def update_stack(
    StackId: str,
    Name: str = None,
    Attributes: Dict[str, Any] = None,
    ServiceRoleArn: str = None,
    DefaultInstanceProfileArn: str = None,
    DefaultOs: str = None,
    HostnameTheme: str = None,
    DefaultAvailabilityZone: str = None,
    DefaultSubnetId: str = None,
    CustomJson: str = None,
    ConfigurationManager: Dict[str, Any] = None,
    ChefConfiguration: Dict[str, Any] = None,
    UseCustomCookbooks: bool = None,
    CustomCookbooksSource: Dict[str, Any] = None,
    DefaultSshKeyName: str = None,
    DefaultRootDeviceType: str = None,
    UseOpsworksSecurityGroups: bool = None,
    AgentVersion: str = None,
) -> None:
```

### Client().update_user_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L590)

```python
def update_user_profile(
    IamUserArn: str,
    SshUsername: str = None,
    SshPublicKey: str = None,
    AllowSelfManagement: bool = None,
) -> None:
```

### Client().update_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/client.py#L600)

```python
def update_volume(
    VolumeId: str,
    Name: str = None,
    MountPoint: str = None,
) -> None:
```
