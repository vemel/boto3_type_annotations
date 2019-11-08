# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.emr.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Emr](index.md#emr) / Client
    - [Client](#client)
        - [Client().add_instance_fleet](#clientadd_instance_fleet)
        - [Client().add_instance_groups](#clientadd_instance_groups)
        - [Client().add_job_flow_steps](#clientadd_job_flow_steps)
        - [Client().add_tags](#clientadd_tags)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_steps](#clientcancel_steps)
        - [Client().create_security_configuration](#clientcreate_security_configuration)
        - [Client().delete_security_configuration](#clientdelete_security_configuration)
        - [Client().describe_cluster](#clientdescribe_cluster)
        - [Client().describe_job_flows](#clientdescribe_job_flows)
        - [Client().describe_security_configuration](#clientdescribe_security_configuration)
        - [Client().describe_step](#clientdescribe_step)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_block_public_access_configuration](#clientget_block_public_access_configuration)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_bootstrap_actions](#clientlist_bootstrap_actions)
        - [Client().list_clusters](#clientlist_clusters)
        - [Client().list_instance_fleets](#clientlist_instance_fleets)
        - [Client().list_instance_groups](#clientlist_instance_groups)
        - [Client().list_instances](#clientlist_instances)
        - [Client().list_security_configurations](#clientlist_security_configurations)
        - [Client().list_steps](#clientlist_steps)
        - [Client().modify_instance_fleet](#clientmodify_instance_fleet)
        - [Client().modify_instance_groups](#clientmodify_instance_groups)
        - [Client().put_auto_scaling_policy](#clientput_auto_scaling_policy)
        - [Client().put_block_public_access_configuration](#clientput_block_public_access_configuration)
        - [Client().remove_auto_scaling_policy](#clientremove_auto_scaling_policy)
        - [Client().remove_tags](#clientremove_tags)
        - [Client().run_job_flow](#clientrun_job_flow)
        - [Client().set_termination_protection](#clientset_termination_protection)
        - [Client().set_visible_to_all_users](#clientset_visible_to_all_users)
        - [Client().terminate_job_flows](#clientterminate_job_flows)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_instance_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L16)

```python
def add_instance_fleet(
    ClusterId: str,
    InstanceFleet: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().add_instance_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L22)

```python
def add_instance_groups(
    InstanceGroups: List[Any],
    JobFlowId: str,
) -> Dict[str, Any]:
```

### Client().add_job_flow_steps

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L28)

```python
def add_job_flow_steps(JobFlowId: str, Steps: List[Any]) -> Dict[str, Any]:
```

### Client().add_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L32)

```python
def add_tags(ResourceId: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L36)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_steps

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L40)

```python
def cancel_steps(
    ClusterId: str = None,
    StepIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_security_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L46)

```python
def create_security_configuration(
    Name: str,
    SecurityConfiguration: str,
) -> Dict[str, Any]:
```

### Client().delete_security_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L52)

```python
def delete_security_configuration(Name: str) -> Dict[str, Any]:
```

### Client().describe_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L56)

```python
def describe_cluster(ClusterId: str) -> Dict[str, Any]:
```

### Client().describe_job_flows

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L60)

```python
def describe_job_flows(
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    JobFlowIds: List[Any] = None,
    JobFlowStates: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_security_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L70)

```python
def describe_security_configuration(Name: str) -> Dict[str, Any]:
```

### Client().describe_step

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L74)

```python
def describe_step(ClusterId: str, StepId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L78)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_block_public_access_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L88)

```python
def get_block_public_access_configuration() -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L92)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L96)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_bootstrap_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L100)

```python
def list_bootstrap_actions(
    ClusterId: str,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L106)

```python
def list_clusters(
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    ClusterStates: List[Any] = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_instance_fleets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L116)

```python
def list_instance_fleets(
    ClusterId: str,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_instance_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L122)

```python
def list_instance_groups(
    ClusterId: str,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L128)

```python
def list_instances(
    ClusterId: str,
    InstanceGroupId: str = None,
    InstanceGroupTypes: List[Any] = None,
    InstanceFleetId: str = None,
    InstanceFleetType: str = None,
    InstanceStates: List[Any] = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_security_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L141)

```python
def list_security_configurations(Marker: str = None) -> Dict[str, Any]:
```

### Client().list_steps

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L145)

```python
def list_steps(
    ClusterId: str,
    StepStates: List[Any] = None,
    StepIds: List[Any] = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().modify_instance_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L155)

```python
def modify_instance_fleet(
    ClusterId: str,
    InstanceFleet: Dict[str, Any],
) -> None:
```

### Client().modify_instance_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L161)

```python
def modify_instance_groups(
    ClusterId: str = None,
    InstanceGroups: List[Any] = None,
) -> None:
```

### Client().put_auto_scaling_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L167)

```python
def put_auto_scaling_policy(
    ClusterId: str,
    InstanceGroupId: str,
    AutoScalingPolicy: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_block_public_access_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L173)

```python
def put_block_public_access_configuration(
    BlockPublicAccessConfiguration: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().remove_auto_scaling_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L179)

```python
def remove_auto_scaling_policy(
    ClusterId: str,
    InstanceGroupId: str,
) -> Dict[str, Any]:
```

### Client().remove_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L185)

```python
def remove_tags(ResourceId: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().run_job_flow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L189)

```python
def run_job_flow(
    Name: str,
    Instances: Dict[str, Any],
    LogUri: str = None,
    AdditionalInfo: str = None,
    AmiVersion: str = None,
    ReleaseLabel: str = None,
    Steps: List[Any] = None,
    BootstrapActions: List[Any] = None,
    SupportedProducts: List[Any] = None,
    NewSupportedProducts: List[Any] = None,
    Applications: List[Any] = None,
    Configurations: List[Any] = None,
    VisibleToAllUsers: bool = None,
    JobFlowRole: str = None,
    ServiceRole: str = None,
    Tags: List[Any] = None,
    SecurityConfiguration: str = None,
    AutoScalingRole: str = None,
    ScaleDownBehavior: str = None,
    CustomAmiId: str = None,
    EbsRootVolumeSize: int = None,
    RepoUpgradeOnBoot: str = None,
    KerberosAttributes: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().set_termination_protection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L218)

```python
def set_termination_protection(
    JobFlowIds: List[Any],
    TerminationProtected: bool,
) -> None:
```

### Client().set_visible_to_all_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L224)

```python
def set_visible_to_all_users(
    JobFlowIds: List[Any],
    VisibleToAllUsers: bool,
) -> None:
```

### Client().terminate_job_flows

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/client.py#L230)

```python
def terminate_job_flows(JobFlowIds: List[Any]) -> None:
```
