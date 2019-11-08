# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.config.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Config](index.md#config) / Client
    - [Client](#client)
        - [Client().batch_get_aggregate_resource_config](#clientbatch_get_aggregate_resource_config)
        - [Client().batch_get_resource_config](#clientbatch_get_resource_config)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_aggregation_authorization](#clientdelete_aggregation_authorization)
        - [Client().delete_config_rule](#clientdelete_config_rule)
        - [Client().delete_configuration_aggregator](#clientdelete_configuration_aggregator)
        - [Client().delete_configuration_recorder](#clientdelete_configuration_recorder)
        - [Client().delete_delivery_channel](#clientdelete_delivery_channel)
        - [Client().delete_evaluation_results](#clientdelete_evaluation_results)
        - [Client().delete_organization_config_rule](#clientdelete_organization_config_rule)
        - [Client().delete_pending_aggregation_request](#clientdelete_pending_aggregation_request)
        - [Client().delete_remediation_configuration](#clientdelete_remediation_configuration)
        - [Client().delete_remediation_exceptions](#clientdelete_remediation_exceptions)
        - [Client().delete_retention_configuration](#clientdelete_retention_configuration)
        - [Client().deliver_config_snapshot](#clientdeliver_config_snapshot)
        - [Client().describe_aggregate_compliance_by_config_rules](#clientdescribe_aggregate_compliance_by_config_rules)
        - [Client().describe_aggregation_authorizations](#clientdescribe_aggregation_authorizations)
        - [Client().describe_compliance_by_config_rule](#clientdescribe_compliance_by_config_rule)
        - [Client().describe_compliance_by_resource](#clientdescribe_compliance_by_resource)
        - [Client().describe_config_rule_evaluation_status](#clientdescribe_config_rule_evaluation_status)
        - [Client().describe_config_rules](#clientdescribe_config_rules)
        - [Client().describe_configuration_aggregator_sources_status](#clientdescribe_configuration_aggregator_sources_status)
        - [Client().describe_configuration_aggregators](#clientdescribe_configuration_aggregators)
        - [Client().describe_configuration_recorder_status](#clientdescribe_configuration_recorder_status)
        - [Client().describe_configuration_recorders](#clientdescribe_configuration_recorders)
        - [Client().describe_delivery_channel_status](#clientdescribe_delivery_channel_status)
        - [Client().describe_delivery_channels](#clientdescribe_delivery_channels)
        - [Client().describe_organization_config_rule_statuses](#clientdescribe_organization_config_rule_statuses)
        - [Client().describe_organization_config_rules](#clientdescribe_organization_config_rules)
        - [Client().describe_pending_aggregation_requests](#clientdescribe_pending_aggregation_requests)
        - [Client().describe_remediation_configurations](#clientdescribe_remediation_configurations)
        - [Client().describe_remediation_exceptions](#clientdescribe_remediation_exceptions)
        - [Client().describe_remediation_execution_status](#clientdescribe_remediation_execution_status)
        - [Client().describe_retention_configurations](#clientdescribe_retention_configurations)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_aggregate_compliance_details_by_config_rule](#clientget_aggregate_compliance_details_by_config_rule)
        - [Client().get_aggregate_config_rule_compliance_summary](#clientget_aggregate_config_rule_compliance_summary)
        - [Client().get_aggregate_discovered_resource_counts](#clientget_aggregate_discovered_resource_counts)
        - [Client().get_aggregate_resource_config](#clientget_aggregate_resource_config)
        - [Client().get_compliance_details_by_config_rule](#clientget_compliance_details_by_config_rule)
        - [Client().get_compliance_details_by_resource](#clientget_compliance_details_by_resource)
        - [Client().get_compliance_summary_by_config_rule](#clientget_compliance_summary_by_config_rule)
        - [Client().get_compliance_summary_by_resource_type](#clientget_compliance_summary_by_resource_type)
        - [Client().get_discovered_resource_counts](#clientget_discovered_resource_counts)
        - [Client().get_organization_config_rule_detailed_status](#clientget_organization_config_rule_detailed_status)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_resource_config_history](#clientget_resource_config_history)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_aggregate_discovered_resources](#clientlist_aggregate_discovered_resources)
        - [Client().list_discovered_resources](#clientlist_discovered_resources)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_aggregation_authorization](#clientput_aggregation_authorization)
        - [Client().put_config_rule](#clientput_config_rule)
        - [Client().put_configuration_aggregator](#clientput_configuration_aggregator)
        - [Client().put_configuration_recorder](#clientput_configuration_recorder)
        - [Client().put_delivery_channel](#clientput_delivery_channel)
        - [Client().put_evaluations](#clientput_evaluations)
        - [Client().put_organization_config_rule](#clientput_organization_config_rule)
        - [Client().put_remediation_configurations](#clientput_remediation_configurations)
        - [Client().put_remediation_exceptions](#clientput_remediation_exceptions)
        - [Client().put_retention_configuration](#clientput_retention_configuration)
        - [Client().select_resource_config](#clientselect_resource_config)
        - [Client().start_config_rules_evaluation](#clientstart_config_rules_evaluation)
        - [Client().start_configuration_recorder](#clientstart_configuration_recorder)
        - [Client().start_remediation_execution](#clientstart_remediation_execution)
        - [Client().stop_configuration_recorder](#clientstop_configuration_recorder)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L13)

```python
class Client(BaseClient):
```

### Client().batch_get_aggregate_resource_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L16)

```python
def batch_get_aggregate_resource_config(
    ConfigurationAggregatorName: str,
    ResourceIdentifiers: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_get_resource_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L22)

```python
def batch_get_resource_config(resourceKeys: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L26)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_aggregation_authorization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L30)

```python
def delete_aggregation_authorization(
    AuthorizedAccountId: str,
    AuthorizedAwsRegion: str,
) -> None:
```

### Client().delete_config_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L36)

```python
def delete_config_rule(ConfigRuleName: str) -> None:
```

### Client().delete_configuration_aggregator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L40)

```python
def delete_configuration_aggregator(ConfigurationAggregatorName: str) -> None:
```

### Client().delete_configuration_recorder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L44)

```python
def delete_configuration_recorder(ConfigurationRecorderName: str) -> None:
```

### Client().delete_delivery_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L48)

```python
def delete_delivery_channel(DeliveryChannelName: str) -> None:
```

### Client().delete_evaluation_results

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L52)

```python
def delete_evaluation_results(ConfigRuleName: str) -> Dict[str, Any]:
```

### Client().delete_organization_config_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L56)

```python
def delete_organization_config_rule(OrganizationConfigRuleName: str) -> None:
```

### Client().delete_pending_aggregation_request

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L60)

```python
def delete_pending_aggregation_request(
    RequesterAccountId: str,
    RequesterAwsRegion: str,
) -> None:
```

### Client().delete_remediation_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L66)

```python
def delete_remediation_configuration(
    ConfigRuleName: str,
    ResourceType: str = None,
) -> Dict[str, Any]:
```

### Client().delete_remediation_exceptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L72)

```python
def delete_remediation_exceptions(
    ConfigRuleName: str,
    ResourceKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().delete_retention_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L78)

```python
def delete_retention_configuration(RetentionConfigurationName: str) -> None:
```

### Client().deliver_config_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L82)

```python
def deliver_config_snapshot(deliveryChannelName: str) -> Dict[str, Any]:
```

### Client().describe_aggregate_compliance_by_config_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L86)

```python
def describe_aggregate_compliance_by_config_rules(
    ConfigurationAggregatorName: str,
    Filters: Dict[str, Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_aggregation_authorizations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L96)

```python
def describe_aggregation_authorizations(
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_compliance_by_config_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L102)

```python
def describe_compliance_by_config_rule(
    ConfigRuleNames: List[Any] = None,
    ComplianceTypes: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_compliance_by_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L111)

```python
def describe_compliance_by_resource(
    ResourceType: str = None,
    ResourceId: str = None,
    ComplianceTypes: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_config_rule_evaluation_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L122)

```python
def describe_config_rule_evaluation_status(
    ConfigRuleNames: List[Any] = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_config_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L131)

```python
def describe_config_rules(
    ConfigRuleNames: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_configuration_aggregator_sources_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L137)

```python
def describe_configuration_aggregator_sources_status(
    ConfigurationAggregatorName: str,
    UpdateStatus: List[Any] = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_configuration_aggregators

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L147)

```python
def describe_configuration_aggregators(
    ConfigurationAggregatorNames: List[Any] = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_configuration_recorder_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L156)

```python
def describe_configuration_recorder_status(
    ConfigurationRecorderNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_configuration_recorders

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L162)

```python
def describe_configuration_recorders(
    ConfigurationRecorderNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_delivery_channel_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L168)

```python
def describe_delivery_channel_status(
    DeliveryChannelNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_delivery_channels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L174)

```python
def describe_delivery_channels(
    DeliveryChannelNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_organization_config_rule_statuses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L180)

```python
def describe_organization_config_rule_statuses(
    OrganizationConfigRuleNames: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_organization_config_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L189)

```python
def describe_organization_config_rules(
    OrganizationConfigRuleNames: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_pending_aggregation_requests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L198)

```python
def describe_pending_aggregation_requests(
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_remediation_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L204)

```python
def describe_remediation_configurations(
    ConfigRuleNames: List[Any],
) -> Dict[str, Any]:
```

### Client().describe_remediation_exceptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L210)

```python
def describe_remediation_exceptions(
    ConfigRuleName: str,
    ResourceKeys: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_remediation_execution_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L220)

```python
def describe_remediation_execution_status(
    ConfigRuleName: str,
    ResourceKeys: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_retention_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L230)

```python
def describe_retention_configurations(
    RetentionConfigurationNames: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L236)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_aggregate_compliance_details_by_config_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L246)

```python
def get_aggregate_compliance_details_by_config_rule(
    ConfigurationAggregatorName: str,
    ConfigRuleName: str,
    AccountId: str,
    AwsRegion: str,
    ComplianceType: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_aggregate_config_rule_compliance_summary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L259)

```python
def get_aggregate_config_rule_compliance_summary(
    ConfigurationAggregatorName: str,
    Filters: Dict[str, Any] = None,
    GroupByKey: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_aggregate_discovered_resource_counts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L270)

```python
def get_aggregate_discovered_resource_counts(
    ConfigurationAggregatorName: str,
    Filters: Dict[str, Any] = None,
    GroupByKey: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_aggregate_resource_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L281)

```python
def get_aggregate_resource_config(
    ConfigurationAggregatorName: str,
    ResourceIdentifier: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().get_compliance_details_by_config_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L287)

```python
def get_compliance_details_by_config_rule(
    ConfigRuleName: str,
    ComplianceTypes: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_compliance_details_by_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L297)

```python
def get_compliance_details_by_resource(
    ResourceType: str,
    ResourceId: str,
    ComplianceTypes: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_compliance_summary_by_config_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L307)

```python
def get_compliance_summary_by_config_rule() -> Dict[str, Any]:
```

### Client().get_compliance_summary_by_resource_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L311)

```python
def get_compliance_summary_by_resource_type(
    ResourceTypes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_discovered_resource_counts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L317)

```python
def get_discovered_resource_counts(
    resourceTypes: List[Any] = None,
    limit: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_organization_config_rule_detailed_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L323)

```python
def get_organization_config_rule_detailed_status(
    OrganizationConfigRuleName: str,
    Filters: Dict[str, Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L333)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_resource_config_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L337)

```python
def get_resource_config_history(
    resourceType: str,
    resourceId: str,
    laterTime: datetime = None,
    earlierTime: datetime = None,
    chronologicalOrder: str = None,
    limit: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L350)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_aggregate_discovered_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L354)

```python
def list_aggregate_discovered_resources(
    ConfigurationAggregatorName: str,
    ResourceType: str,
    Filters: Dict[str, Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_discovered_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L365)

```python
def list_discovered_resources(
    resourceType: str,
    resourceIds: List[Any] = None,
    resourceName: str = None,
    limit: int = None,
    includeDeletedResources: bool = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L377)

```python
def list_tags_for_resource(
    ResourceArn: str,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_aggregation_authorization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L383)

```python
def put_aggregation_authorization(
    AuthorizedAccountId: str,
    AuthorizedAwsRegion: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().put_config_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L389)

```python
def put_config_rule(
    ConfigRule: Dict[str, Any],
    Tags: List[Any] = None,
) -> None:
```

### Client().put_configuration_aggregator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L395)

```python
def put_configuration_aggregator(
    ConfigurationAggregatorName: str,
    AccountAggregationSources: List[Any] = None,
    OrganizationAggregationSource: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().put_configuration_recorder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L405)

```python
def put_configuration_recorder(ConfigurationRecorder: Dict[str, Any]) -> None:
```

### Client().put_delivery_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L409)

```python
def put_delivery_channel(DeliveryChannel: Dict[str, Any]) -> None:
```

### Client().put_evaluations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L413)

```python
def put_evaluations(
    ResultToken: str,
    Evaluations: List[Any] = None,
    TestMode: bool = None,
) -> Dict[str, Any]:
```

### Client().put_organization_config_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L419)

```python
def put_organization_config_rule(
    OrganizationConfigRuleName: str,
    OrganizationManagedRuleMetadata: Dict[str, Any] = None,
    OrganizationCustomRuleMetadata: Dict[str, Any] = None,
    ExcludedAccounts: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().put_remediation_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L429)

```python
def put_remediation_configurations(
    RemediationConfigurations: List[Any],
) -> Dict[str, Any]:
```

### Client().put_remediation_exceptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L435)

```python
def put_remediation_exceptions(
    ConfigRuleName: str,
    ResourceKeys: List[Any],
    Message: str = None,
    ExpirationTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().put_retention_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L445)

```python
def put_retention_configuration(RetentionPeriodInDays: int) -> Dict[str, Any]:
```

### Client().select_resource_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L449)

```python
def select_resource_config(
    Expression: str,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().start_config_rules_evaluation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L455)

```python
def start_config_rules_evaluation(
    ConfigRuleNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().start_configuration_recorder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L461)

```python
def start_configuration_recorder(ConfigurationRecorderName: str) -> None:
```

### Client().start_remediation_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L465)

```python
def start_remediation_execution(
    ConfigRuleName: str,
    ResourceKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().stop_configuration_recorder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L471)

```python
def stop_configuration_recorder(ConfigurationRecorderName: str) -> None:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L475)

```python
def tag_resource(ResourceArn: str, Tags: List[Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/client.py#L479)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```
