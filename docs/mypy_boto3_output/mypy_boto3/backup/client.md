# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.backup.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Backup](index.md#backup) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_backup_plan](#clientcreate_backup_plan)
        - [Client().create_backup_selection](#clientcreate_backup_selection)
        - [Client().create_backup_vault](#clientcreate_backup_vault)
        - [Client().delete_backup_plan](#clientdelete_backup_plan)
        - [Client().delete_backup_selection](#clientdelete_backup_selection)
        - [Client().delete_backup_vault](#clientdelete_backup_vault)
        - [Client().delete_backup_vault_access_policy](#clientdelete_backup_vault_access_policy)
        - [Client().delete_backup_vault_notifications](#clientdelete_backup_vault_notifications)
        - [Client().delete_recovery_point](#clientdelete_recovery_point)
        - [Client().describe_backup_job](#clientdescribe_backup_job)
        - [Client().describe_backup_vault](#clientdescribe_backup_vault)
        - [Client().describe_protected_resource](#clientdescribe_protected_resource)
        - [Client().describe_recovery_point](#clientdescribe_recovery_point)
        - [Client().describe_restore_job](#clientdescribe_restore_job)
        - [Client().export_backup_plan_template](#clientexport_backup_plan_template)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_backup_plan](#clientget_backup_plan)
        - [Client().get_backup_plan_from_json](#clientget_backup_plan_from_json)
        - [Client().get_backup_plan_from_template](#clientget_backup_plan_from_template)
        - [Client().get_backup_selection](#clientget_backup_selection)
        - [Client().get_backup_vault_access_policy](#clientget_backup_vault_access_policy)
        - [Client().get_backup_vault_notifications](#clientget_backup_vault_notifications)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_recovery_point_restore_metadata](#clientget_recovery_point_restore_metadata)
        - [Client().get_supported_resource_types](#clientget_supported_resource_types)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_backup_jobs](#clientlist_backup_jobs)
        - [Client().list_backup_plan_templates](#clientlist_backup_plan_templates)
        - [Client().list_backup_plan_versions](#clientlist_backup_plan_versions)
        - [Client().list_backup_plans](#clientlist_backup_plans)
        - [Client().list_backup_selections](#clientlist_backup_selections)
        - [Client().list_backup_vaults](#clientlist_backup_vaults)
        - [Client().list_protected_resources](#clientlist_protected_resources)
        - [Client().list_recovery_points_by_backup_vault](#clientlist_recovery_points_by_backup_vault)
        - [Client().list_recovery_points_by_resource](#clientlist_recovery_points_by_resource)
        - [Client().list_restore_jobs](#clientlist_restore_jobs)
        - [Client().list_tags](#clientlist_tags)
        - [Client().put_backup_vault_access_policy](#clientput_backup_vault_access_policy)
        - [Client().put_backup_vault_notifications](#clientput_backup_vault_notifications)
        - [Client().start_backup_job](#clientstart_backup_job)
        - [Client().start_restore_job](#clientstart_restore_job)
        - [Client().stop_backup_job](#clientstop_backup_job)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_backup_plan](#clientupdate_backup_plan)
        - [Client().update_recovery_point_lifecycle](#clientupdate_recovery_point_lifecycle)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_backup_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L20)

```python
def create_backup_plan(
    BackupPlan: Dict[str, Any],
    BackupPlanTags: Dict[str, Any] = None,
    CreatorRequestId: str = None,
) -> Dict[str, Any]:
```

### Client().create_backup_selection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L29)

```python
def create_backup_selection(
    BackupPlanId: str,
    BackupSelection: Dict[str, Any],
    CreatorRequestId: str = None,
) -> Dict[str, Any]:
```

### Client().create_backup_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L38)

```python
def create_backup_vault(
    BackupVaultName: str,
    BackupVaultTags: Dict[str, Any] = None,
    EncryptionKeyArn: str = None,
    CreatorRequestId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_backup_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L48)

```python
def delete_backup_plan(BackupPlanId: str) -> Dict[str, Any]:
```

### Client().delete_backup_selection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L52)

```python
def delete_backup_selection(BackupPlanId: str, SelectionId: str) -> None:
```

### Client().delete_backup_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L56)

```python
def delete_backup_vault(BackupVaultName: str) -> None:
```

### Client().delete_backup_vault_access_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L60)

```python
def delete_backup_vault_access_policy(BackupVaultName: str) -> None:
```

### Client().delete_backup_vault_notifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L64)

```python
def delete_backup_vault_notifications(BackupVaultName: str) -> None:
```

### Client().delete_recovery_point

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L68)

```python
def delete_recovery_point(
    BackupVaultName: str,
    RecoveryPointArn: str,
) -> None:
```

### Client().describe_backup_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L74)

```python
def describe_backup_job(BackupJobId: str) -> Dict[str, Any]:
```

### Client().describe_backup_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L78)

```python
def describe_backup_vault(BackupVaultName: str) -> Dict[str, Any]:
```

### Client().describe_protected_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L82)

```python
def describe_protected_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().describe_recovery_point

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L86)

```python
def describe_recovery_point(
    BackupVaultName: str,
    RecoveryPointArn: str,
) -> Dict[str, Any]:
```

### Client().describe_restore_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L92)

```python
def describe_restore_job(RestoreJobId: str) -> Dict[str, Any]:
```

### Client().export_backup_plan_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L96)

```python
def export_backup_plan_template(BackupPlanId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L100)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_backup_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L110)

```python
def get_backup_plan(
    BackupPlanId: str,
    VersionId: str = None,
) -> Dict[str, Any]:
```

### Client().get_backup_plan_from_json

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L116)

```python
def get_backup_plan_from_json(BackupPlanTemplateJson: str) -> Dict[str, Any]:
```

### Client().get_backup_plan_from_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L120)

```python
def get_backup_plan_from_template(
    BackupPlanTemplateId: str,
) -> Dict[str, Any]:
```

### Client().get_backup_selection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L126)

```python
def get_backup_selection(
    BackupPlanId: str,
    SelectionId: str,
) -> Dict[str, Any]:
```

### Client().get_backup_vault_access_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L132)

```python
def get_backup_vault_access_policy(BackupVaultName: str) -> Dict[str, Any]:
```

### Client().get_backup_vault_notifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L136)

```python
def get_backup_vault_notifications(BackupVaultName: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L140)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_recovery_point_restore_metadata

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L144)

```python
def get_recovery_point_restore_metadata(
    BackupVaultName: str,
    RecoveryPointArn: str,
) -> Dict[str, Any]:
```

### Client().get_supported_resource_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L150)

```python
def get_supported_resource_types() -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L154)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_backup_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L158)

```python
def list_backup_jobs(
    NextToken: str = None,
    MaxResults: int = None,
    ByResourceArn: str = None,
    ByState: str = None,
    ByBackupVaultName: str = None,
    ByCreatedBefore: datetime = None,
    ByCreatedAfter: datetime = None,
    ByResourceType: str = None,
) -> Dict[str, Any]:
```

### Client().list_backup_plan_templates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L172)

```python
def list_backup_plan_templates(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_backup_plan_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L178)

```python
def list_backup_plan_versions(
    BackupPlanId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_backup_plans

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L184)

```python
def list_backup_plans(
    NextToken: str = None,
    MaxResults: int = None,
    IncludeDeleted: bool = None,
) -> Dict[str, Any]:
```

### Client().list_backup_selections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L190)

```python
def list_backup_selections(
    BackupPlanId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_backup_vaults

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L196)

```python
def list_backup_vaults(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_protected_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L202)

```python
def list_protected_resources(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_recovery_points_by_backup_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L208)

```python
def list_recovery_points_by_backup_vault(
    BackupVaultName: str,
    NextToken: str = None,
    MaxResults: int = None,
    ByResourceArn: str = None,
    ByResourceType: str = None,
    ByBackupPlanId: str = None,
    ByCreatedBefore: datetime = None,
    ByCreatedAfter: datetime = None,
) -> Dict[str, Any]:
```

### Client().list_recovery_points_by_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L222)

```python
def list_recovery_points_by_resource(
    ResourceArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_restore_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L228)

```python
def list_restore_jobs(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L234)

```python
def list_tags(
    ResourceArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().put_backup_vault_access_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L240)

```python
def put_backup_vault_access_policy(
    BackupVaultName: str,
    Policy: str = None,
) -> None:
```

### Client().put_backup_vault_notifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L246)

```python
def put_backup_vault_notifications(
    BackupVaultName: str,
    SNSTopicArn: str,
    BackupVaultEvents: List[Any],
) -> None:
```

### Client().start_backup_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L252)

```python
def start_backup_job(
    BackupVaultName: str,
    ResourceArn: str,
    IamRoleArn: str,
    IdempotencyToken: str = None,
    StartWindowMinutes: int = None,
    CompleteWindowMinutes: int = None,
    Lifecycle: Dict[str, Any] = None,
    RecoveryPointTags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().start_restore_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L266)

```python
def start_restore_job(
    RecoveryPointArn: str,
    Metadata: Dict[str, Any],
    IamRoleArn: str,
    IdempotencyToken: str = None,
    ResourceType: str = None,
) -> Dict[str, Any]:
```

### Client().stop_backup_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L277)

```python
def stop_backup_job(BackupJobId: str) -> None:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L281)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L285)

```python
def untag_resource(ResourceArn: str, TagKeyList: List[Any]) -> None:
```

### Client().update_backup_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L289)

```python
def update_backup_plan(
    BackupPlanId: str,
    BackupPlan: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_recovery_point_lifecycle

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/backup/client.py#L295)

```python
def update_recovery_point_lifecycle(
    BackupVaultName: str,
    RecoveryPointArn: str,
    Lifecycle: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
