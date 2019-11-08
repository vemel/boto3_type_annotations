# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iot.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iot](index.md#iot) / Client
    - [Client](#client)
        - [Client().accept_certificate_transfer](#clientaccept_certificate_transfer)
        - [Client().add_thing_to_billing_group](#clientadd_thing_to_billing_group)
        - [Client().add_thing_to_thing_group](#clientadd_thing_to_thing_group)
        - [Client().associate_targets_with_job](#clientassociate_targets_with_job)
        - [Client().attach_policy](#clientattach_policy)
        - [Client().attach_principal_policy](#clientattach_principal_policy)
        - [Client().attach_security_profile](#clientattach_security_profile)
        - [Client().attach_thing_principal](#clientattach_thing_principal)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_audit_mitigation_actions_task](#clientcancel_audit_mitigation_actions_task)
        - [Client().cancel_audit_task](#clientcancel_audit_task)
        - [Client().cancel_certificate_transfer](#clientcancel_certificate_transfer)
        - [Client().cancel_job](#clientcancel_job)
        - [Client().cancel_job_execution](#clientcancel_job_execution)
        - [Client().clear_default_authorizer](#clientclear_default_authorizer)
        - [Client().create_authorizer](#clientcreate_authorizer)
        - [Client().create_billing_group](#clientcreate_billing_group)
        - [Client().create_certificate_from_csr](#clientcreate_certificate_from_csr)
        - [Client().create_dynamic_thing_group](#clientcreate_dynamic_thing_group)
        - [Client().create_job](#clientcreate_job)
        - [Client().create_keys_and_certificate](#clientcreate_keys_and_certificate)
        - [Client().create_mitigation_action](#clientcreate_mitigation_action)
        - [Client().create_ota_update](#clientcreate_ota_update)
        - [Client().create_policy](#clientcreate_policy)
        - [Client().create_policy_version](#clientcreate_policy_version)
        - [Client().create_role_alias](#clientcreate_role_alias)
        - [Client().create_scheduled_audit](#clientcreate_scheduled_audit)
        - [Client().create_security_profile](#clientcreate_security_profile)
        - [Client().create_stream](#clientcreate_stream)
        - [Client().create_thing](#clientcreate_thing)
        - [Client().create_thing_group](#clientcreate_thing_group)
        - [Client().create_thing_type](#clientcreate_thing_type)
        - [Client().create_topic_rule](#clientcreate_topic_rule)
        - [Client().delete_account_audit_configuration](#clientdelete_account_audit_configuration)
        - [Client().delete_authorizer](#clientdelete_authorizer)
        - [Client().delete_billing_group](#clientdelete_billing_group)
        - [Client().delete_ca_certificate](#clientdelete_ca_certificate)
        - [Client().delete_certificate](#clientdelete_certificate)
        - [Client().delete_dynamic_thing_group](#clientdelete_dynamic_thing_group)
        - [Client().delete_job](#clientdelete_job)
        - [Client().delete_job_execution](#clientdelete_job_execution)
        - [Client().delete_mitigation_action](#clientdelete_mitigation_action)
        - [Client().delete_ota_update](#clientdelete_ota_update)
        - [Client().delete_policy](#clientdelete_policy)
        - [Client().delete_policy_version](#clientdelete_policy_version)
        - [Client().delete_registration_code](#clientdelete_registration_code)
        - [Client().delete_role_alias](#clientdelete_role_alias)
        - [Client().delete_scheduled_audit](#clientdelete_scheduled_audit)
        - [Client().delete_security_profile](#clientdelete_security_profile)
        - [Client().delete_stream](#clientdelete_stream)
        - [Client().delete_thing](#clientdelete_thing)
        - [Client().delete_thing_group](#clientdelete_thing_group)
        - [Client().delete_thing_type](#clientdelete_thing_type)
        - [Client().delete_topic_rule](#clientdelete_topic_rule)
        - [Client().delete_v2_logging_level](#clientdelete_v2_logging_level)
        - [Client().deprecate_thing_type](#clientdeprecate_thing_type)
        - [Client().describe_account_audit_configuration](#clientdescribe_account_audit_configuration)
        - [Client().describe_audit_finding](#clientdescribe_audit_finding)
        - [Client().describe_audit_mitigation_actions_task](#clientdescribe_audit_mitigation_actions_task)
        - [Client().describe_audit_task](#clientdescribe_audit_task)
        - [Client().describe_authorizer](#clientdescribe_authorizer)
        - [Client().describe_billing_group](#clientdescribe_billing_group)
        - [Client().describe_ca_certificate](#clientdescribe_ca_certificate)
        - [Client().describe_certificate](#clientdescribe_certificate)
        - [Client().describe_default_authorizer](#clientdescribe_default_authorizer)
        - [Client().describe_endpoint](#clientdescribe_endpoint)
        - [Client().describe_event_configurations](#clientdescribe_event_configurations)
        - [Client().describe_index](#clientdescribe_index)
        - [Client().describe_job](#clientdescribe_job)
        - [Client().describe_job_execution](#clientdescribe_job_execution)
        - [Client().describe_mitigation_action](#clientdescribe_mitigation_action)
        - [Client().describe_role_alias](#clientdescribe_role_alias)
        - [Client().describe_scheduled_audit](#clientdescribe_scheduled_audit)
        - [Client().describe_security_profile](#clientdescribe_security_profile)
        - [Client().describe_stream](#clientdescribe_stream)
        - [Client().describe_thing](#clientdescribe_thing)
        - [Client().describe_thing_group](#clientdescribe_thing_group)
        - [Client().describe_thing_registration_task](#clientdescribe_thing_registration_task)
        - [Client().describe_thing_type](#clientdescribe_thing_type)
        - [Client().detach_policy](#clientdetach_policy)
        - [Client().detach_principal_policy](#clientdetach_principal_policy)
        - [Client().detach_security_profile](#clientdetach_security_profile)
        - [Client().detach_thing_principal](#clientdetach_thing_principal)
        - [Client().disable_topic_rule](#clientdisable_topic_rule)
        - [Client().enable_topic_rule](#clientenable_topic_rule)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_effective_policies](#clientget_effective_policies)
        - [Client().get_indexing_configuration](#clientget_indexing_configuration)
        - [Client().get_job_document](#clientget_job_document)
        - [Client().get_logging_options](#clientget_logging_options)
        - [Client().get_ota_update](#clientget_ota_update)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_policy](#clientget_policy)
        - [Client().get_policy_version](#clientget_policy_version)
        - [Client().get_registration_code](#clientget_registration_code)
        - [Client().get_statistics](#clientget_statistics)
        - [Client().get_topic_rule](#clientget_topic_rule)
        - [Client().get_v2_logging_options](#clientget_v2_logging_options)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_active_violations](#clientlist_active_violations)
        - [Client().list_attached_policies](#clientlist_attached_policies)
        - [Client().list_audit_findings](#clientlist_audit_findings)
        - [Client().list_audit_mitigation_actions_executions](#clientlist_audit_mitigation_actions_executions)
        - [Client().list_audit_mitigation_actions_tasks](#clientlist_audit_mitigation_actions_tasks)
        - [Client().list_audit_tasks](#clientlist_audit_tasks)
        - [Client().list_authorizers](#clientlist_authorizers)
        - [Client().list_billing_groups](#clientlist_billing_groups)
        - [Client().list_ca_certificates](#clientlist_ca_certificates)
        - [Client().list_certificates](#clientlist_certificates)
        - [Client().list_certificates_by_ca](#clientlist_certificates_by_ca)
        - [Client().list_indices](#clientlist_indices)
        - [Client().list_job_executions_for_job](#clientlist_job_executions_for_job)
        - [Client().list_job_executions_for_thing](#clientlist_job_executions_for_thing)
        - [Client().list_jobs](#clientlist_jobs)
        - [Client().list_mitigation_actions](#clientlist_mitigation_actions)
        - [Client().list_ota_updates](#clientlist_ota_updates)
        - [Client().list_outgoing_certificates](#clientlist_outgoing_certificates)
        - [Client().list_policies](#clientlist_policies)
        - [Client().list_policy_principals](#clientlist_policy_principals)
        - [Client().list_policy_versions](#clientlist_policy_versions)
        - [Client().list_principal_policies](#clientlist_principal_policies)
        - [Client().list_principal_things](#clientlist_principal_things)
        - [Client().list_role_aliases](#clientlist_role_aliases)
        - [Client().list_scheduled_audits](#clientlist_scheduled_audits)
        - [Client().list_security_profiles](#clientlist_security_profiles)
        - [Client().list_security_profiles_for_target](#clientlist_security_profiles_for_target)
        - [Client().list_streams](#clientlist_streams)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_targets_for_policy](#clientlist_targets_for_policy)
        - [Client().list_targets_for_security_profile](#clientlist_targets_for_security_profile)
        - [Client().list_thing_groups](#clientlist_thing_groups)
        - [Client().list_thing_groups_for_thing](#clientlist_thing_groups_for_thing)
        - [Client().list_thing_principals](#clientlist_thing_principals)
        - [Client().list_thing_registration_task_reports](#clientlist_thing_registration_task_reports)
        - [Client().list_thing_registration_tasks](#clientlist_thing_registration_tasks)
        - [Client().list_thing_types](#clientlist_thing_types)
        - [Client().list_things](#clientlist_things)
        - [Client().list_things_in_billing_group](#clientlist_things_in_billing_group)
        - [Client().list_things_in_thing_group](#clientlist_things_in_thing_group)
        - [Client().list_topic_rules](#clientlist_topic_rules)
        - [Client().list_v2_logging_levels](#clientlist_v2_logging_levels)
        - [Client().list_violation_events](#clientlist_violation_events)
        - [Client().register_ca_certificate](#clientregister_ca_certificate)
        - [Client().register_certificate](#clientregister_certificate)
        - [Client().register_thing](#clientregister_thing)
        - [Client().reject_certificate_transfer](#clientreject_certificate_transfer)
        - [Client().remove_thing_from_billing_group](#clientremove_thing_from_billing_group)
        - [Client().remove_thing_from_thing_group](#clientremove_thing_from_thing_group)
        - [Client().replace_topic_rule](#clientreplace_topic_rule)
        - [Client().search_index](#clientsearch_index)
        - [Client().set_default_authorizer](#clientset_default_authorizer)
        - [Client().set_default_policy_version](#clientset_default_policy_version)
        - [Client().set_logging_options](#clientset_logging_options)
        - [Client().set_v2_logging_level](#clientset_v2_logging_level)
        - [Client().set_v2_logging_options](#clientset_v2_logging_options)
        - [Client().start_audit_mitigation_actions_task](#clientstart_audit_mitigation_actions_task)
        - [Client().start_on_demand_audit_task](#clientstart_on_demand_audit_task)
        - [Client().start_thing_registration_task](#clientstart_thing_registration_task)
        - [Client().stop_thing_registration_task](#clientstop_thing_registration_task)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().test_authorization](#clienttest_authorization)
        - [Client().test_invoke_authorizer](#clienttest_invoke_authorizer)
        - [Client().transfer_certificate](#clienttransfer_certificate)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_account_audit_configuration](#clientupdate_account_audit_configuration)
        - [Client().update_authorizer](#clientupdate_authorizer)
        - [Client().update_billing_group](#clientupdate_billing_group)
        - [Client().update_ca_certificate](#clientupdate_ca_certificate)
        - [Client().update_certificate](#clientupdate_certificate)
        - [Client().update_dynamic_thing_group](#clientupdate_dynamic_thing_group)
        - [Client().update_event_configurations](#clientupdate_event_configurations)
        - [Client().update_indexing_configuration](#clientupdate_indexing_configuration)
        - [Client().update_job](#clientupdate_job)
        - [Client().update_mitigation_action](#clientupdate_mitigation_action)
        - [Client().update_role_alias](#clientupdate_role_alias)
        - [Client().update_scheduled_audit](#clientupdate_scheduled_audit)
        - [Client().update_security_profile](#clientupdate_security_profile)
        - [Client().update_stream](#clientupdate_stream)
        - [Client().update_thing](#clientupdate_thing)
        - [Client().update_thing_group](#clientupdate_thing_group)
        - [Client().update_thing_groups_for_thing](#clientupdate_thing_groups_for_thing)
        - [Client().validate_security_profile_behaviors](#clientvalidate_security_profile_behaviors)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L13)

```python
class Client(BaseClient):
```

### Client().accept_certificate_transfer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L16)

```python
def accept_certificate_transfer(
    certificateId: str,
    setAsActive: bool = None,
) -> None:
```

### Client().add_thing_to_billing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L22)

```python
def add_thing_to_billing_group(
    billingGroupName: str = None,
    billingGroupArn: str = None,
    thingName: str = None,
    thingArn: str = None,
) -> Dict[str, Any]:
```

### Client().add_thing_to_thing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L32)

```python
def add_thing_to_thing_group(
    thingGroupName: str = None,
    thingGroupArn: str = None,
    thingName: str = None,
    thingArn: str = None,
    overrideDynamicGroups: bool = None,
) -> Dict[str, Any]:
```

### Client().associate_targets_with_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L43)

```python
def associate_targets_with_job(
    targets: List[Any],
    jobId: str,
    comment: str = None,
) -> Dict[str, Any]:
```

### Client().attach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L49)

```python
def attach_policy(policyName: str, target: str) -> None:
```

### Client().attach_principal_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L53)

```python
def attach_principal_policy(policyName: str, principal: str) -> None:
```

### Client().attach_security_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L57)

```python
def attach_security_profile(
    securityProfileName: str,
    securityProfileTargetArn: str,
) -> Dict[str, Any]:
```

### Client().attach_thing_principal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L63)

```python
def attach_thing_principal(thingName: str, principal: str) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L67)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_audit_mitigation_actions_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L71)

```python
def cancel_audit_mitigation_actions_task(taskId: str) -> Dict[str, Any]:
```

### Client().cancel_audit_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L75)

```python
def cancel_audit_task(taskId: str) -> Dict[str, Any]:
```

### Client().cancel_certificate_transfer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L79)

```python
def cancel_certificate_transfer(certificateId: str) -> None:
```

### Client().cancel_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L83)

```python
def cancel_job(
    jobId: str,
    reasonCode: str = None,
    comment: str = None,
    force: bool = None,
) -> Dict[str, Any]:
```

### Client().cancel_job_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L93)

```python
def cancel_job_execution(
    jobId: str,
    thingName: str,
    force: bool = None,
    expectedVersion: int = None,
    statusDetails: Dict[str, Any] = None,
) -> None:
```

### Client().clear_default_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L104)

```python
def clear_default_authorizer() -> Dict[str, Any]:
```

### Client().create_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L108)

```python
def create_authorizer(
    authorizerName: str,
    authorizerFunctionArn: str,
    tokenKeyName: str,
    tokenSigningPublicKeys: Dict[str, Any],
    status: str = None,
) -> Dict[str, Any]:
```

### Client().create_billing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L119)

```python
def create_billing_group(
    billingGroupName: str,
    billingGroupProperties: Dict[str, Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_certificate_from_csr

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L128)

```python
def create_certificate_from_csr(
    certificateSigningRequest: str,
    setAsActive: bool = None,
) -> Dict[str, Any]:
```

### Client().create_dynamic_thing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L134)

```python
def create_dynamic_thing_group(
    thingGroupName: str,
    queryString: str,
    thingGroupProperties: Dict[str, Any] = None,
    indexName: str = None,
    queryVersion: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L146)

```python
def create_job(
    jobId: str,
    targets: List[Any],
    documentSource: str = None,
    document: str = None,
    description: str = None,
    presignedUrlConfig: Dict[str, Any] = None,
    targetSelection: str = None,
    jobExecutionsRolloutConfig: Dict[str, Any] = None,
    abortConfig: Dict[str, Any] = None,
    timeoutConfig: Dict[str, Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_keys_and_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L163)

```python
def create_keys_and_certificate(setAsActive: bool = None) -> Dict[str, Any]:
```

### Client().create_mitigation_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L167)

```python
def create_mitigation_action(
    actionName: str,
    roleArn: str,
    actionParams: Dict[str, Any],
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_ota_update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L177)

```python
def create_ota_update(
    otaUpdateId: str,
    targets: List[Any],
    files: List[Any],
    roleArn: str,
    description: str = None,
    targetSelection: str = None,
    awsJobExecutionsRolloutConfig: Dict[str, Any] = None,
    additionalParameters: Dict[str, Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L192)

```python
def create_policy(policyName: str, policyDocument: str) -> Dict[str, Any]:
```

### Client().create_policy_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L196)

```python
def create_policy_version(
    policyName: str,
    policyDocument: str,
    setAsDefault: bool = None,
) -> Dict[str, Any]:
```

### Client().create_role_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L202)

```python
def create_role_alias(
    roleAlias: str,
    roleArn: str,
    credentialDurationSeconds: int = None,
) -> Dict[str, Any]:
```

### Client().create_scheduled_audit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L208)

```python
def create_scheduled_audit(
    frequency: str,
    targetCheckNames: List[Any],
    scheduledAuditName: str,
    dayOfMonth: str = None,
    dayOfWeek: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_security_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L220)

```python
def create_security_profile(
    securityProfileName: str,
    securityProfileDescription: str = None,
    behaviors: List[Any] = None,
    alertTargets: Dict[str, Any] = None,
    additionalMetricsToRetain: List[Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L232)

```python
def create_stream(
    streamId: str,
    files: List[Any],
    roleArn: str,
    description: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_thing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L243)

```python
def create_thing(
    thingName: str,
    thingTypeName: str = None,
    attributePayload: Dict[str, Any] = None,
    billingGroupName: str = None,
) -> Dict[str, Any]:
```

### Client().create_thing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L253)

```python
def create_thing_group(
    thingGroupName: str,
    parentGroupName: str = None,
    thingGroupProperties: Dict[str, Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_thing_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L263)

```python
def create_thing_type(
    thingTypeName: str,
    thingTypeProperties: Dict[str, Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_topic_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L272)

```python
def create_topic_rule(
    ruleName: str,
    topicRulePayload: Dict[str, Any],
    tags: str = None,
) -> None:
```

### Client().delete_account_audit_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L278)

```python
def delete_account_audit_configuration(
    deleteScheduledAudits: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L284)

```python
def delete_authorizer(authorizerName: str) -> Dict[str, Any]:
```

### Client().delete_billing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L288)

```python
def delete_billing_group(
    billingGroupName: str,
    expectedVersion: int = None,
) -> Dict[str, Any]:
```

### Client().delete_ca_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L294)

```python
def delete_ca_certificate(certificateId: str) -> Dict[str, Any]:
```

### Client().delete_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L298)

```python
def delete_certificate(certificateId: str, forceDelete: bool = None) -> None:
```

### Client().delete_dynamic_thing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L302)

```python
def delete_dynamic_thing_group(
    thingGroupName: str,
    expectedVersion: int = None,
) -> Dict[str, Any]:
```

### Client().delete_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L308)

```python
def delete_job(jobId: str, force: bool = None) -> None:
```

### Client().delete_job_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L312)

```python
def delete_job_execution(
    jobId: str,
    thingName: str,
    executionNumber: int,
    force: bool = None,
) -> None:
```

### Client().delete_mitigation_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L318)

```python
def delete_mitigation_action(actionName: str) -> Dict[str, Any]:
```

### Client().delete_ota_update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L322)

```python
def delete_ota_update(
    otaUpdateId: str,
    deleteStream: bool = None,
    forceDeleteAWSJob: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L331)

```python
def delete_policy(policyName: str) -> None:
```

### Client().delete_policy_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L335)

```python
def delete_policy_version(policyName: str, policyVersionId: str) -> None:
```

### Client().delete_registration_code

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L339)

```python
def delete_registration_code() -> Dict[str, Any]:
```

### Client().delete_role_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L343)

```python
def delete_role_alias(roleAlias: str) -> Dict[str, Any]:
```

### Client().delete_scheduled_audit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L347)

```python
def delete_scheduled_audit(scheduledAuditName: str) -> Dict[str, Any]:
```

### Client().delete_security_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L351)

```python
def delete_security_profile(
    securityProfileName: str,
    expectedVersion: int = None,
) -> Dict[str, Any]:
```

### Client().delete_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L357)

```python
def delete_stream(streamId: str) -> Dict[str, Any]:
```

### Client().delete_thing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L361)

```python
def delete_thing(
    thingName: str,
    expectedVersion: int = None,
) -> Dict[str, Any]:
```

### Client().delete_thing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L367)

```python
def delete_thing_group(
    thingGroupName: str,
    expectedVersion: int = None,
) -> Dict[str, Any]:
```

### Client().delete_thing_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L373)

```python
def delete_thing_type(thingTypeName: str) -> Dict[str, Any]:
```

### Client().delete_topic_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L377)

```python
def delete_topic_rule(ruleName: str) -> None:
```

### Client().delete_v2_logging_level

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L381)

```python
def delete_v2_logging_level(targetType: str, targetName: str) -> None:
```

### Client().deprecate_thing_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L385)

```python
def deprecate_thing_type(
    thingTypeName: str,
    undoDeprecate: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_account_audit_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L391)

```python
def describe_account_audit_configuration() -> Dict[str, Any]:
```

### Client().describe_audit_finding

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L395)

```python
def describe_audit_finding(findingId: str) -> Dict[str, Any]:
```

### Client().describe_audit_mitigation_actions_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L399)

```python
def describe_audit_mitigation_actions_task(taskId: str) -> Dict[str, Any]:
```

### Client().describe_audit_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L403)

```python
def describe_audit_task(taskId: str) -> Dict[str, Any]:
```

### Client().describe_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L407)

```python
def describe_authorizer(authorizerName: str) -> Dict[str, Any]:
```

### Client().describe_billing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L411)

```python
def describe_billing_group(billingGroupName: str) -> Dict[str, Any]:
```

### Client().describe_ca_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L415)

```python
def describe_ca_certificate(certificateId: str) -> Dict[str, Any]:
```

### Client().describe_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L419)

```python
def describe_certificate(certificateId: str) -> Dict[str, Any]:
```

### Client().describe_default_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L423)

```python
def describe_default_authorizer() -> Dict[str, Any]:
```

### Client().describe_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L427)

```python
def describe_endpoint(endpointType: str = None) -> Dict[str, Any]:
```

### Client().describe_event_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L431)

```python
def describe_event_configurations() -> Dict[str, Any]:
```

### Client().describe_index

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L435)

```python
def describe_index(indexName: str) -> Dict[str, Any]:
```

### Client().describe_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L439)

```python
def describe_job(jobId: str) -> Dict[str, Any]:
```

### Client().describe_job_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L443)

```python
def describe_job_execution(
    jobId: str,
    thingName: str,
    executionNumber: int = None,
) -> Dict[str, Any]:
```

### Client().describe_mitigation_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L449)

```python
def describe_mitigation_action(actionName: str) -> Dict[str, Any]:
```

### Client().describe_role_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L453)

```python
def describe_role_alias(roleAlias: str) -> Dict[str, Any]:
```

### Client().describe_scheduled_audit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L457)

```python
def describe_scheduled_audit(scheduledAuditName: str) -> Dict[str, Any]:
```

### Client().describe_security_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L461)

```python
def describe_security_profile(securityProfileName: str) -> Dict[str, Any]:
```

### Client().describe_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L465)

```python
def describe_stream(streamId: str) -> Dict[str, Any]:
```

### Client().describe_thing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L469)

```python
def describe_thing(thingName: str) -> Dict[str, Any]:
```

### Client().describe_thing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L473)

```python
def describe_thing_group(thingGroupName: str) -> Dict[str, Any]:
```

### Client().describe_thing_registration_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L477)

```python
def describe_thing_registration_task(taskId: str) -> Dict[str, Any]:
```

### Client().describe_thing_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L481)

```python
def describe_thing_type(thingTypeName: str) -> Dict[str, Any]:
```

### Client().detach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L485)

```python
def detach_policy(policyName: str, target: str) -> None:
```

### Client().detach_principal_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L489)

```python
def detach_principal_policy(policyName: str, principal: str) -> None:
```

### Client().detach_security_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L493)

```python
def detach_security_profile(
    securityProfileName: str,
    securityProfileTargetArn: str,
) -> Dict[str, Any]:
```

### Client().detach_thing_principal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L499)

```python
def detach_thing_principal(thingName: str, principal: str) -> Dict[str, Any]:
```

### Client().disable_topic_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L503)

```python
def disable_topic_rule(ruleName: str) -> None:
```

### Client().enable_topic_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L507)

```python
def enable_topic_rule(ruleName: str) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L511)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_effective_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L521)

```python
def get_effective_policies(
    principal: str = None,
    cognitoIdentityPoolId: str = None,
    thingName: str = None,
) -> Dict[str, Any]:
```

### Client().get_indexing_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L530)

```python
def get_indexing_configuration() -> Dict[str, Any]:
```

### Client().get_job_document

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L534)

```python
def get_job_document(jobId: str) -> Dict[str, Any]:
```

### Client().get_logging_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L538)

```python
def get_logging_options() -> Dict[str, Any]:
```

### Client().get_ota_update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L542)

```python
def get_ota_update(otaUpdateId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L546)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L550)

```python
def get_policy(policyName: str) -> Dict[str, Any]:
```

### Client().get_policy_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L554)

```python
def get_policy_version(
    policyName: str,
    policyVersionId: str,
) -> Dict[str, Any]:
```

### Client().get_registration_code

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L560)

```python
def get_registration_code() -> Dict[str, Any]:
```

### Client().get_statistics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L564)

```python
def get_statistics(
    queryString: str,
    indexName: str = None,
    aggregationField: str = None,
    queryVersion: str = None,
) -> Dict[str, Any]:
```

### Client().get_topic_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L574)

```python
def get_topic_rule(ruleName: str) -> Dict[str, Any]:
```

### Client().get_v2_logging_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L578)

```python
def get_v2_logging_options() -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L582)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_active_violations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L586)

```python
def list_active_violations(
    thingName: str = None,
    securityProfileName: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_attached_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L596)

```python
def list_attached_policies(
    target: str,
    recursive: bool = None,
    marker: str = None,
    pageSize: int = None,
) -> Dict[str, Any]:
```

### Client().list_audit_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L606)

```python
def list_audit_findings(
    taskId: str = None,
    checkName: str = None,
    resourceIdentifier: Dict[str, Any] = None,
    maxResults: int = None,
    nextToken: str = None,
    startTime: datetime = None,
    endTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().list_audit_mitigation_actions_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L619)

```python
def list_audit_mitigation_actions_executions(
    taskId: str,
    findingId: str,
    actionStatus: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_audit_mitigation_actions_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L630)

```python
def list_audit_mitigation_actions_tasks(
    startTime: datetime,
    endTime: datetime,
    auditTaskId: str = None,
    findingId: str = None,
    taskStatus: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_audit_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L643)

```python
def list_audit_tasks(
    startTime: datetime,
    endTime: datetime,
    taskType: str = None,
    taskStatus: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_authorizers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L655)

```python
def list_authorizers(
    pageSize: int = None,
    marker: str = None,
    ascendingOrder: bool = None,
    status: str = None,
) -> Dict[str, Any]:
```

### Client().list_billing_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L665)

```python
def list_billing_groups(
    nextToken: str = None,
    maxResults: int = None,
    namePrefixFilter: str = None,
) -> Dict[str, Any]:
```

### Client().list_ca_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L674)

```python
def list_ca_certificates(
    pageSize: int = None,
    marker: str = None,
    ascendingOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L680)

```python
def list_certificates(
    pageSize: int = None,
    marker: str = None,
    ascendingOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_certificates_by_ca

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L686)

```python
def list_certificates_by_ca(
    caCertificateId: str,
    pageSize: int = None,
    marker: str = None,
    ascendingOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_indices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L696)

```python
def list_indices(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_job_executions_for_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L702)

```python
def list_job_executions_for_job(
    jobId: str,
    status: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_job_executions_for_thing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L712)

```python
def list_job_executions_for_thing(
    thingName: str,
    status: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L722)

```python
def list_jobs(
    status: str = None,
    targetSelection: str = None,
    maxResults: int = None,
    nextToken: str = None,
    thingGroupName: str = None,
    thingGroupId: str = None,
) -> Dict[str, Any]:
```

### Client().list_mitigation_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L734)

```python
def list_mitigation_actions(
    actionType: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_ota_updates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L740)

```python
def list_ota_updates(
    maxResults: int = None,
    nextToken: str = None,
    otaUpdateStatus: str = None,
) -> Dict[str, Any]:
```

### Client().list_outgoing_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L746)

```python
def list_outgoing_certificates(
    pageSize: int = None,
    marker: str = None,
    ascendingOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L752)

```python
def list_policies(
    marker: str = None,
    pageSize: int = None,
    ascendingOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_policy_principals

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L758)

```python
def list_policy_principals(
    policyName: str,
    marker: str = None,
    pageSize: int = None,
    ascendingOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_policy_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L768)

```python
def list_policy_versions(policyName: str) -> Dict[str, Any]:
```

### Client().list_principal_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L772)

```python
def list_principal_policies(
    principal: str,
    marker: str = None,
    pageSize: int = None,
    ascendingOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_principal_things

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L782)

```python
def list_principal_things(
    principal: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_role_aliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L788)

```python
def list_role_aliases(
    pageSize: int = None,
    marker: str = None,
    ascendingOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_scheduled_audits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L794)

```python
def list_scheduled_audits(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_security_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L800)

```python
def list_security_profiles(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_security_profiles_for_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L806)

```python
def list_security_profiles_for_target(
    securityProfileTargetArn: str,
    nextToken: str = None,
    maxResults: int = None,
    recursive: bool = None,
) -> Dict[str, Any]:
```

### Client().list_streams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L816)

```python
def list_streams(
    maxResults: int = None,
    nextToken: str = None,
    ascendingOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L822)

```python
def list_tags_for_resource(
    resourceArn: str,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_targets_for_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L828)

```python
def list_targets_for_policy(
    policyName: str,
    marker: str = None,
    pageSize: int = None,
) -> Dict[str, Any]:
```

### Client().list_targets_for_security_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L834)

```python
def list_targets_for_security_profile(
    securityProfileName: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_thing_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L840)

```python
def list_thing_groups(
    nextToken: str = None,
    maxResults: int = None,
    parentGroup: str = None,
    namePrefixFilter: str = None,
    recursive: bool = None,
) -> Dict[str, Any]:
```

### Client().list_thing_groups_for_thing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L851)

```python
def list_thing_groups_for_thing(
    thingName: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_thing_principals

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L857)

```python
def list_thing_principals(thingName: str) -> Dict[str, Any]:
```

### Client().list_thing_registration_task_reports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L861)

```python
def list_thing_registration_task_reports(
    taskId: str,
    reportType: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_thing_registration_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L871)

```python
def list_thing_registration_tasks(
    nextToken: str = None,
    maxResults: int = None,
    status: str = None,
) -> Dict[str, Any]:
```

### Client().list_thing_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L877)

```python
def list_thing_types(
    nextToken: str = None,
    maxResults: int = None,
    thingTypeName: str = None,
) -> Dict[str, Any]:
```

### Client().list_things

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L883)

```python
def list_things(
    nextToken: str = None,
    maxResults: int = None,
    attributeName: str = None,
    attributeValue: str = None,
    thingTypeName: str = None,
) -> Dict[str, Any]:
```

### Client().list_things_in_billing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L894)

```python
def list_things_in_billing_group(
    billingGroupName: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_things_in_thing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L900)

```python
def list_things_in_thing_group(
    thingGroupName: str,
    recursive: bool = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_topic_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L910)

```python
def list_topic_rules(
    topic: str = None,
    maxResults: int = None,
    nextToken: str = None,
    ruleDisabled: bool = None,
) -> Dict[str, Any]:
```

### Client().list_v2_logging_levels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L920)

```python
def list_v2_logging_levels(
    targetType: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_violation_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L926)

```python
def list_violation_events(
    startTime: datetime,
    endTime: datetime,
    thingName: str = None,
    securityProfileName: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().register_ca_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L938)

```python
def register_ca_certificate(
    caCertificate: str,
    verificationCertificate: str,
    setAsActive: bool = None,
    allowAutoRegistration: bool = None,
    registrationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().register_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L949)

```python
def register_certificate(
    certificatePem: str,
    caCertificatePem: str = None,
    setAsActive: bool = None,
    status: str = None,
) -> Dict[str, Any]:
```

### Client().register_thing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L959)

```python
def register_thing(
    templateBody: str,
    parameters: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().reject_certificate_transfer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L965)

```python
def reject_certificate_transfer(
    certificateId: str,
    rejectReason: str = None,
) -> None:
```

### Client().remove_thing_from_billing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L971)

```python
def remove_thing_from_billing_group(
    billingGroupName: str = None,
    billingGroupArn: str = None,
    thingName: str = None,
    thingArn: str = None,
) -> Dict[str, Any]:
```

### Client().remove_thing_from_thing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L981)

```python
def remove_thing_from_thing_group(
    thingGroupName: str = None,
    thingGroupArn: str = None,
    thingName: str = None,
    thingArn: str = None,
) -> Dict[str, Any]:
```

### Client().replace_topic_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L991)

```python
def replace_topic_rule(
    ruleName: str,
    topicRulePayload: Dict[str, Any],
) -> None:
```

### Client().search_index

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L997)

```python
def search_index(
    queryString: str,
    indexName: str = None,
    nextToken: str = None,
    maxResults: int = None,
    queryVersion: str = None,
) -> Dict[str, Any]:
```

### Client().set_default_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1008)

```python
def set_default_authorizer(authorizerName: str) -> Dict[str, Any]:
```

### Client().set_default_policy_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1012)

```python
def set_default_policy_version(policyName: str, policyVersionId: str) -> None:
```

### Client().set_logging_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1016)

```python
def set_logging_options(loggingOptionsPayload: Dict[str, Any]) -> None:
```

### Client().set_v2_logging_level

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1020)

```python
def set_v2_logging_level(logTarget: Dict[str, Any], logLevel: str) -> None:
```

### Client().set_v2_logging_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1024)

```python
def set_v2_logging_options(
    roleArn: str = None,
    defaultLogLevel: str = None,
    disableAllLogs: bool = None,
) -> None:
```

### Client().start_audit_mitigation_actions_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1033)

```python
def start_audit_mitigation_actions_task(
    taskId: str,
    target: Dict[str, Any],
    auditCheckToActionsMapping: Dict[str, Any],
    clientRequestToken: str,
) -> Dict[str, Any]:
```

### Client().start_on_demand_audit_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1043)

```python
def start_on_demand_audit_task(targetCheckNames: List[Any]) -> Dict[str, Any]:
```

### Client().start_thing_registration_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1047)

```python
def start_thing_registration_task(
    templateBody: str,
    inputFileBucket: str,
    inputFileKey: str,
    roleArn: str,
) -> Dict[str, Any]:
```

### Client().stop_thing_registration_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1053)

```python
def stop_thing_registration_task(taskId: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1057)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().test_authorization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1061)

```python
def test_authorization(
    authInfos: List[Any],
    principal: str = None,
    cognitoIdentityPoolId: str = None,
    clientId: str = None,
    policyNamesToAdd: List[Any] = None,
    policyNamesToSkip: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().test_invoke_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1073)

```python
def test_invoke_authorizer(
    authorizerName: str,
    token: str,
    tokenSignature: str,
) -> Dict[str, Any]:
```

### Client().transfer_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1079)

```python
def transfer_certificate(
    certificateId: str,
    targetAwsAccount: str,
    transferMessage: str = None,
) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1085)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_account_audit_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1089)

```python
def update_account_audit_configuration(
    roleArn: str = None,
    auditNotificationTargetConfigurations: Dict[str, Any] = None,
    auditCheckConfigurations: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1098)

```python
def update_authorizer(
    authorizerName: str,
    authorizerFunctionArn: str = None,
    tokenKeyName: str = None,
    tokenSigningPublicKeys: Dict[str, Any] = None,
    status: str = None,
) -> Dict[str, Any]:
```

### Client().update_billing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1109)

```python
def update_billing_group(
    billingGroupName: str,
    billingGroupProperties: Dict[str, Any],
    expectedVersion: int = None,
) -> Dict[str, Any]:
```

### Client().update_ca_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1118)

```python
def update_ca_certificate(
    certificateId: str,
    newStatus: str = None,
    newAutoRegistrationStatus: str = None,
    registrationConfig: Dict[str, Any] = None,
    removeAutoRegistration: bool = None,
) -> None:
```

### Client().update_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1129)

```python
def update_certificate(certificateId: str, newStatus: str) -> None:
```

### Client().update_dynamic_thing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1133)

```python
def update_dynamic_thing_group(
    thingGroupName: str,
    thingGroupProperties: Dict[str, Any],
    expectedVersion: int = None,
    indexName: str = None,
    queryString: str = None,
    queryVersion: str = None,
) -> Dict[str, Any]:
```

### Client().update_event_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1145)

```python
def update_event_configurations(
    eventConfigurations: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_indexing_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1151)

```python
def update_indexing_configuration(
    thingIndexingConfiguration: Dict[str, Any] = None,
    thingGroupIndexingConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1159)

```python
def update_job(
    jobId: str,
    description: str = None,
    presignedUrlConfig: Dict[str, Any] = None,
    jobExecutionsRolloutConfig: Dict[str, Any] = None,
    abortConfig: Dict[str, Any] = None,
    timeoutConfig: Dict[str, Any] = None,
) -> None:
```

### Client().update_mitigation_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1171)

```python
def update_mitigation_action(
    actionName: str,
    roleArn: str = None,
    actionParams: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_role_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1177)

```python
def update_role_alias(
    roleAlias: str,
    roleArn: str = None,
    credentialDurationSeconds: int = None,
) -> Dict[str, Any]:
```

### Client().update_scheduled_audit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1183)

```python
def update_scheduled_audit(
    scheduledAuditName: str,
    frequency: str = None,
    dayOfMonth: str = None,
    dayOfWeek: str = None,
    targetCheckNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_security_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1194)

```python
def update_security_profile(
    securityProfileName: str,
    securityProfileDescription: str = None,
    behaviors: List[Any] = None,
    alertTargets: Dict[str, Any] = None,
    additionalMetricsToRetain: List[Any] = None,
    deleteBehaviors: bool = None,
    deleteAlertTargets: bool = None,
    deleteAdditionalMetricsToRetain: bool = None,
    expectedVersion: int = None,
) -> Dict[str, Any]:
```

### Client().update_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1209)

```python
def update_stream(
    streamId: str,
    description: str = None,
    files: List[Any] = None,
    roleArn: str = None,
) -> Dict[str, Any]:
```

### Client().update_thing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1219)

```python
def update_thing(
    thingName: str,
    thingTypeName: str = None,
    attributePayload: Dict[str, Any] = None,
    expectedVersion: int = None,
    removeThingType: bool = None,
) -> Dict[str, Any]:
```

### Client().update_thing_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1230)

```python
def update_thing_group(
    thingGroupName: str,
    thingGroupProperties: Dict[str, Any],
    expectedVersion: int = None,
) -> Dict[str, Any]:
```

### Client().update_thing_groups_for_thing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1239)

```python
def update_thing_groups_for_thing(
    thingName: str = None,
    thingGroupsToAdd: List[Any] = None,
    thingGroupsToRemove: List[Any] = None,
    overrideDynamicGroups: bool = None,
) -> Dict[str, Any]:
```

### Client().validate_security_profile_behaviors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/client.py#L1249)

```python
def validate_security_profile_behaviors(
    behaviors: List[Any],
) -> Dict[str, Any]:
```
