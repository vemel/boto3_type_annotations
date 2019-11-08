# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.devicefarm.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Devicefarm](index.md#devicefarm) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_device_pool](#clientcreate_device_pool)
        - [Client().create_instance_profile](#clientcreate_instance_profile)
        - [Client().create_network_profile](#clientcreate_network_profile)
        - [Client().create_project](#clientcreate_project)
        - [Client().create_remote_access_session](#clientcreate_remote_access_session)
        - [Client().create_upload](#clientcreate_upload)
        - [Client().create_vpce_configuration](#clientcreate_vpce_configuration)
        - [Client().delete_device_pool](#clientdelete_device_pool)
        - [Client().delete_instance_profile](#clientdelete_instance_profile)
        - [Client().delete_network_profile](#clientdelete_network_profile)
        - [Client().delete_project](#clientdelete_project)
        - [Client().delete_remote_access_session](#clientdelete_remote_access_session)
        - [Client().delete_run](#clientdelete_run)
        - [Client().delete_upload](#clientdelete_upload)
        - [Client().delete_vpce_configuration](#clientdelete_vpce_configuration)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_account_settings](#clientget_account_settings)
        - [Client().get_device](#clientget_device)
        - [Client().get_device_instance](#clientget_device_instance)
        - [Client().get_device_pool](#clientget_device_pool)
        - [Client().get_device_pool_compatibility](#clientget_device_pool_compatibility)
        - [Client().get_instance_profile](#clientget_instance_profile)
        - [Client().get_job](#clientget_job)
        - [Client().get_network_profile](#clientget_network_profile)
        - [Client().get_offering_status](#clientget_offering_status)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_project](#clientget_project)
        - [Client().get_remote_access_session](#clientget_remote_access_session)
        - [Client().get_run](#clientget_run)
        - [Client().get_suite](#clientget_suite)
        - [Client().get_test](#clientget_test)
        - [Client().get_upload](#clientget_upload)
        - [Client().get_vpce_configuration](#clientget_vpce_configuration)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().install_to_remote_access_session](#clientinstall_to_remote_access_session)
        - [Client().list_artifacts](#clientlist_artifacts)
        - [Client().list_device_instances](#clientlist_device_instances)
        - [Client().list_device_pools](#clientlist_device_pools)
        - [Client().list_devices](#clientlist_devices)
        - [Client().list_instance_profiles](#clientlist_instance_profiles)
        - [Client().list_jobs](#clientlist_jobs)
        - [Client().list_network_profiles](#clientlist_network_profiles)
        - [Client().list_offering_promotions](#clientlist_offering_promotions)
        - [Client().list_offering_transactions](#clientlist_offering_transactions)
        - [Client().list_offerings](#clientlist_offerings)
        - [Client().list_projects](#clientlist_projects)
        - [Client().list_remote_access_sessions](#clientlist_remote_access_sessions)
        - [Client().list_runs](#clientlist_runs)
        - [Client().list_samples](#clientlist_samples)
        - [Client().list_suites](#clientlist_suites)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_tests](#clientlist_tests)
        - [Client().list_unique_problems](#clientlist_unique_problems)
        - [Client().list_uploads](#clientlist_uploads)
        - [Client().list_vpce_configurations](#clientlist_vpce_configurations)
        - [Client().purchase_offering](#clientpurchase_offering)
        - [Client().renew_offering](#clientrenew_offering)
        - [Client().schedule_run](#clientschedule_run)
        - [Client().stop_job](#clientstop_job)
        - [Client().stop_remote_access_session](#clientstop_remote_access_session)
        - [Client().stop_run](#clientstop_run)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_device_instance](#clientupdate_device_instance)
        - [Client().update_device_pool](#clientupdate_device_pool)
        - [Client().update_instance_profile](#clientupdate_instance_profile)
        - [Client().update_network_profile](#clientupdate_network_profile)
        - [Client().update_project](#clientupdate_project)
        - [Client().update_upload](#clientupdate_upload)
        - [Client().update_vpce_configuration](#clientupdate_vpce_configuration)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_device_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L19)

```python
def create_device_pool(
    projectArn: str,
    name: str,
    rules: List[Any],
    description: str = None,
    maxDevices: int = None,
) -> Dict[str, Any]:
```

### Client().create_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L30)

```python
def create_instance_profile(
    name: str,
    description: str = None,
    packageCleanup: bool = None,
    excludeAppPackagesFromCleanup: List[Any] = None,
    rebootAfterUse: bool = None,
) -> Dict[str, Any]:
```

### Client().create_network_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L41)

```python
def create_network_profile(
    projectArn: str,
    name: str,
    description: str = None,
    type: str = None,
    uplinkBandwidthBits: int = None,
    downlinkBandwidthBits: int = None,
    uplinkDelayMs: int = None,
    downlinkDelayMs: int = None,
    uplinkJitterMs: int = None,
    downlinkJitterMs: int = None,
    uplinkLossPercent: int = None,
    downlinkLossPercent: int = None,
) -> Dict[str, Any]:
```

### Client().create_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L59)

```python
def create_project(
    name: str,
    defaultJobTimeoutMinutes: int = None,
) -> Dict[str, Any]:
```

### Client().create_remote_access_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L65)

```python
def create_remote_access_session(
    projectArn: str,
    deviceArn: str,
    instanceArn: str = None,
    sshPublicKey: str = None,
    remoteDebugEnabled: bool = None,
    remoteRecordEnabled: bool = None,
    remoteRecordAppArn: str = None,
    name: str = None,
    clientId: str = None,
    configuration: Dict[str, Any] = None,
    interactionMode: str = None,
    skipAppResign: bool = None,
) -> Dict[str, Any]:
```

### Client().create_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L83)

```python
def create_upload(
    projectArn: str,
    name: str,
    type: str,
    contentType: str = None,
) -> Dict[str, Any]:
```

### Client().create_vpce_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L89)

```python
def create_vpce_configuration(
    vpceConfigurationName: str,
    vpceServiceName: str,
    serviceDnsName: str,
    vpceConfigurationDescription: str = None,
) -> Dict[str, Any]:
```

### Client().delete_device_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L99)

```python
def delete_device_pool(arn: str) -> Dict[str, Any]:
```

### Client().delete_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L103)

```python
def delete_instance_profile(arn: str) -> Dict[str, Any]:
```

### Client().delete_network_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L107)

```python
def delete_network_profile(arn: str) -> Dict[str, Any]:
```

### Client().delete_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L111)

```python
def delete_project(arn: str) -> Dict[str, Any]:
```

### Client().delete_remote_access_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L115)

```python
def delete_remote_access_session(arn: str) -> Dict[str, Any]:
```

### Client().delete_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L119)

```python
def delete_run(arn: str) -> Dict[str, Any]:
```

### Client().delete_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L123)

```python
def delete_upload(arn: str) -> Dict[str, Any]:
```

### Client().delete_vpce_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L127)

```python
def delete_vpce_configuration(arn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L131)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_account_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L141)

```python
def get_account_settings() -> Dict[str, Any]:
```

### Client().get_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L145)

```python
def get_device(arn: str) -> Dict[str, Any]:
```

### Client().get_device_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L149)

```python
def get_device_instance(arn: str) -> Dict[str, Any]:
```

### Client().get_device_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L153)

```python
def get_device_pool(arn: str) -> Dict[str, Any]:
```

### Client().get_device_pool_compatibility

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L157)

```python
def get_device_pool_compatibility(
    devicePoolArn: str,
    appArn: str = None,
    testType: str = None,
    test: Dict[str, Any] = None,
    configuration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L168)

```python
def get_instance_profile(arn: str) -> Dict[str, Any]:
```

### Client().get_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L172)

```python
def get_job(arn: str) -> Dict[str, Any]:
```

### Client().get_network_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L176)

```python
def get_network_profile(arn: str) -> Dict[str, Any]:
```

### Client().get_offering_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L180)

```python
def get_offering_status(nextToken: str = None) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L184)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L188)

```python
def get_project(arn: str) -> Dict[str, Any]:
```

### Client().get_remote_access_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L192)

```python
def get_remote_access_session(arn: str) -> Dict[str, Any]:
```

### Client().get_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L196)

```python
def get_run(arn: str) -> Dict[str, Any]:
```

### Client().get_suite

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L200)

```python
def get_suite(arn: str) -> Dict[str, Any]:
```

### Client().get_test

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L204)

```python
def get_test(arn: str) -> Dict[str, Any]:
```

### Client().get_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L208)

```python
def get_upload(arn: str) -> Dict[str, Any]:
```

### Client().get_vpce_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L212)

```python
def get_vpce_configuration(arn: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L216)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().install_to_remote_access_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L220)

```python
def install_to_remote_access_session(
    remoteAccessSessionArn: str,
    appArn: str,
) -> Dict[str, Any]:
```

### Client().list_artifacts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L226)

```python
def list_artifacts(
    arn: str,
    type: str,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_device_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L232)

```python
def list_device_instances(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_device_pools

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L238)

```python
def list_device_pools(
    arn: str,
    type: str = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L244)

```python
def list_devices(
    arn: str = None,
    nextToken: str = None,
    filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_instance_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L250)

```python
def list_instance_profiles(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L256)

```python
def list_jobs(arn: str, nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_network_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L260)

```python
def list_network_profiles(
    arn: str,
    type: str = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_offering_promotions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L266)

```python
def list_offering_promotions(nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_offering_transactions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L270)

```python
def list_offering_transactions(nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_offerings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L274)

```python
def list_offerings(nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_projects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L278)

```python
def list_projects(arn: str = None, nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_remote_access_sessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L282)

```python
def list_remote_access_sessions(
    arn: str,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_runs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L288)

```python
def list_runs(arn: str, nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_samples

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L292)

```python
def list_samples(arn: str, nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_suites

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L296)

```python
def list_suites(arn: str, nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L300)

```python
def list_tags_for_resource(ResourceARN: str) -> Dict[str, Any]:
```

### Client().list_tests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L304)

```python
def list_tests(arn: str, nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_unique_problems

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L308)

```python
def list_unique_problems(arn: str, nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_uploads

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L312)

```python
def list_uploads(
    arn: str,
    type: str = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_vpce_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L318)

```python
def list_vpce_configurations(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().purchase_offering

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L324)

```python
def purchase_offering(
    offeringId: str = None,
    quantity: int = None,
    offeringPromotionId: str = None,
) -> Dict[str, Any]:
```

### Client().renew_offering

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L333)

```python
def renew_offering(
    offeringId: str = None,
    quantity: int = None,
) -> Dict[str, Any]:
```

### Client().schedule_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L339)

```python
def schedule_run(
    projectArn: str,
    test: Dict[str, Any],
    appArn: str = None,
    devicePoolArn: str = None,
    deviceSelectionConfiguration: Dict[str, Any] = None,
    name: str = None,
    configuration: Dict[str, Any] = None,
    executionConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().stop_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L353)

```python
def stop_job(arn: str) -> Dict[str, Any]:
```

### Client().stop_remote_access_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L357)

```python
def stop_remote_access_session(arn: str) -> Dict[str, Any]:
```

### Client().stop_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L361)

```python
def stop_run(arn: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L365)

```python
def tag_resource(ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L369)

```python
def untag_resource(ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_device_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L373)

```python
def update_device_instance(
    arn: str,
    profileArn: str = None,
    labels: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_device_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L379)

```python
def update_device_pool(
    arn: str,
    name: str = None,
    description: str = None,
    rules: List[Any] = None,
    maxDevices: int = None,
    clearMaxDevices: bool = None,
) -> Dict[str, Any]:
```

### Client().update_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L391)

```python
def update_instance_profile(
    arn: str,
    name: str = None,
    description: str = None,
    packageCleanup: bool = None,
    excludeAppPackagesFromCleanup: List[Any] = None,
    rebootAfterUse: bool = None,
) -> Dict[str, Any]:
```

### Client().update_network_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L403)

```python
def update_network_profile(
    arn: str,
    name: str = None,
    description: str = None,
    type: str = None,
    uplinkBandwidthBits: int = None,
    downlinkBandwidthBits: int = None,
    uplinkDelayMs: int = None,
    downlinkDelayMs: int = None,
    uplinkJitterMs: int = None,
    downlinkJitterMs: int = None,
    uplinkLossPercent: int = None,
    downlinkLossPercent: int = None,
) -> Dict[str, Any]:
```

### Client().update_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L421)

```python
def update_project(
    arn: str,
    name: str = None,
    defaultJobTimeoutMinutes: int = None,
) -> Dict[str, Any]:
```

### Client().update_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L427)

```python
def update_upload(
    arn: str,
    name: str = None,
    contentType: str = None,
    editContent: bool = None,
) -> Dict[str, Any]:
```

### Client().update_vpce_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/client.py#L437)

```python
def update_vpce_configuration(
    arn: str,
    vpceConfigurationName: str = None,
    vpceServiceName: str = None,
    serviceDnsName: str = None,
    vpceConfigurationDescription: str = None,
) -> Dict[str, Any]:
```
