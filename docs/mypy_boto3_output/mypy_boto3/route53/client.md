# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.route53.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Route53](index.md#route53) / Client
    - [Client](#client)
        - [Client().associate_vpc_with_hosted_zone](#clientassociate_vpc_with_hosted_zone)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().change_resource_record_sets](#clientchange_resource_record_sets)
        - [Client().change_tags_for_resource](#clientchange_tags_for_resource)
        - [Client().create_health_check](#clientcreate_health_check)
        - [Client().create_hosted_zone](#clientcreate_hosted_zone)
        - [Client().create_query_logging_config](#clientcreate_query_logging_config)
        - [Client().create_reusable_delegation_set](#clientcreate_reusable_delegation_set)
        - [Client().create_traffic_policy](#clientcreate_traffic_policy)
        - [Client().create_traffic_policy_instance](#clientcreate_traffic_policy_instance)
        - [Client().create_traffic_policy_version](#clientcreate_traffic_policy_version)
        - [Client().create_vpc_association_authorization](#clientcreate_vpc_association_authorization)
        - [Client().delete_health_check](#clientdelete_health_check)
        - [Client().delete_hosted_zone](#clientdelete_hosted_zone)
        - [Client().delete_query_logging_config](#clientdelete_query_logging_config)
        - [Client().delete_reusable_delegation_set](#clientdelete_reusable_delegation_set)
        - [Client().delete_traffic_policy](#clientdelete_traffic_policy)
        - [Client().delete_traffic_policy_instance](#clientdelete_traffic_policy_instance)
        - [Client().delete_vpc_association_authorization](#clientdelete_vpc_association_authorization)
        - [Client().disassociate_vpc_from_hosted_zone](#clientdisassociate_vpc_from_hosted_zone)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_account_limit](#clientget_account_limit)
        - [Client().get_change](#clientget_change)
        - [Client().get_checker_ip_ranges](#clientget_checker_ip_ranges)
        - [Client().get_geo_location](#clientget_geo_location)
        - [Client().get_health_check](#clientget_health_check)
        - [Client().get_health_check_count](#clientget_health_check_count)
        - [Client().get_health_check_last_failure_reason](#clientget_health_check_last_failure_reason)
        - [Client().get_health_check_status](#clientget_health_check_status)
        - [Client().get_hosted_zone](#clientget_hosted_zone)
        - [Client().get_hosted_zone_count](#clientget_hosted_zone_count)
        - [Client().get_hosted_zone_limit](#clientget_hosted_zone_limit)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_query_logging_config](#clientget_query_logging_config)
        - [Client().get_reusable_delegation_set](#clientget_reusable_delegation_set)
        - [Client().get_reusable_delegation_set_limit](#clientget_reusable_delegation_set_limit)
        - [Client().get_traffic_policy](#clientget_traffic_policy)
        - [Client().get_traffic_policy_instance](#clientget_traffic_policy_instance)
        - [Client().get_traffic_policy_instance_count](#clientget_traffic_policy_instance_count)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_geo_locations](#clientlist_geo_locations)
        - [Client().list_health_checks](#clientlist_health_checks)
        - [Client().list_hosted_zones](#clientlist_hosted_zones)
        - [Client().list_hosted_zones_by_name](#clientlist_hosted_zones_by_name)
        - [Client().list_query_logging_configs](#clientlist_query_logging_configs)
        - [Client().list_resource_record_sets](#clientlist_resource_record_sets)
        - [Client().list_reusable_delegation_sets](#clientlist_reusable_delegation_sets)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_tags_for_resources](#clientlist_tags_for_resources)
        - [Client().list_traffic_policies](#clientlist_traffic_policies)
        - [Client().list_traffic_policy_instances](#clientlist_traffic_policy_instances)
        - [Client().list_traffic_policy_instances_by_hosted_zone](#clientlist_traffic_policy_instances_by_hosted_zone)
        - [Client().list_traffic_policy_instances_by_policy](#clientlist_traffic_policy_instances_by_policy)
        - [Client().list_traffic_policy_versions](#clientlist_traffic_policy_versions)
        - [Client().list_vpc_association_authorizations](#clientlist_vpc_association_authorizations)
        - [Client().test_dns_answer](#clienttest_dns_answer)
        - [Client().update_health_check](#clientupdate_health_check)
        - [Client().update_hosted_zone_comment](#clientupdate_hosted_zone_comment)
        - [Client().update_traffic_policy_comment](#clientupdate_traffic_policy_comment)
        - [Client().update_traffic_policy_instance](#clientupdate_traffic_policy_instance)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_vpc_with_hosted_zone

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L15)

```python
def associate_vpc_with_hosted_zone(
    HostedZoneId: str,
    VPC: Dict[str, Any],
    Comment: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L21)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().change_resource_record_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L25)

```python
def change_resource_record_sets(
    HostedZoneId: str,
    ChangeBatch: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().change_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L31)

```python
def change_tags_for_resource(
    ResourceType: str,
    ResourceId: str,
    AddTags: List[Any] = None,
    RemoveTagKeys: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_health_check

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L41)

```python
def create_health_check(
    CallerReference: str,
    HealthCheckConfig: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_hosted_zone

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L47)

```python
def create_hosted_zone(
    Name: str,
    CallerReference: str,
    VPC: Dict[str, Any] = None,
    HostedZoneConfig: Dict[str, Any] = None,
    DelegationSetId: str = None,
) -> Dict[str, Any]:
```

### Client().create_query_logging_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L58)

```python
def create_query_logging_config(
    HostedZoneId: str,
    CloudWatchLogsLogGroupArn: str,
) -> Dict[str, Any]:
```

### Client().create_reusable_delegation_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L64)

```python
def create_reusable_delegation_set(
    CallerReference: str,
    HostedZoneId: str = None,
) -> Dict[str, Any]:
```

### Client().create_traffic_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L70)

```python
def create_traffic_policy(
    Name: str,
    Document: str,
    Comment: str = None,
) -> Dict[str, Any]:
```

### Client().create_traffic_policy_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L76)

```python
def create_traffic_policy_instance(
    HostedZoneId: str,
    Name: str,
    TTL: int,
    TrafficPolicyId: str,
    TrafficPolicyVersion: int,
) -> Dict[str, Any]:
```

### Client().create_traffic_policy_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L87)

```python
def create_traffic_policy_version(
    Id: str,
    Document: str,
    Comment: str = None,
) -> Dict[str, Any]:
```

### Client().create_vpc_association_authorization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L93)

```python
def create_vpc_association_authorization(
    HostedZoneId: str,
    VPC: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_health_check

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L99)

```python
def delete_health_check(HealthCheckId: str) -> Dict[str, Any]:
```

### Client().delete_hosted_zone

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L103)

```python
def delete_hosted_zone(Id: str) -> Dict[str, Any]:
```

### Client().delete_query_logging_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L107)

```python
def delete_query_logging_config(Id: str) -> Dict[str, Any]:
```

### Client().delete_reusable_delegation_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L111)

```python
def delete_reusable_delegation_set(Id: str) -> Dict[str, Any]:
```

### Client().delete_traffic_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L115)

```python
def delete_traffic_policy(Id: str, Version: int) -> Dict[str, Any]:
```

### Client().delete_traffic_policy_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L119)

```python
def delete_traffic_policy_instance(Id: str) -> Dict[str, Any]:
```

### Client().delete_vpc_association_authorization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L123)

```python
def delete_vpc_association_authorization(
    HostedZoneId: str,
    VPC: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().disassociate_vpc_from_hosted_zone

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L129)

```python
def disassociate_vpc_from_hosted_zone(
    HostedZoneId: str,
    VPC: Dict[str, Any],
    Comment: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L135)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_account_limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L145)

```python
def get_account_limit(Type: str) -> Dict[str, Any]:
```

### Client().get_change

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L149)

```python
def get_change(Id: str) -> Dict[str, Any]:
```

### Client().get_checker_ip_ranges

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L153)

```python
def get_checker_ip_ranges() -> Dict[str, Any]:
```

### Client().get_geo_location

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L157)

```python
def get_geo_location(
    ContinentCode: str = None,
    CountryCode: str = None,
    SubdivisionCode: str = None,
) -> Dict[str, Any]:
```

### Client().get_health_check

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L166)

```python
def get_health_check(HealthCheckId: str) -> Dict[str, Any]:
```

### Client().get_health_check_count

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L170)

```python
def get_health_check_count() -> Dict[str, Any]:
```

### Client().get_health_check_last_failure_reason

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L174)

```python
def get_health_check_last_failure_reason(
    HealthCheckId: str,
) -> Dict[str, Any]:
```

### Client().get_health_check_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L180)

```python
def get_health_check_status(HealthCheckId: str) -> Dict[str, Any]:
```

### Client().get_hosted_zone

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L184)

```python
def get_hosted_zone(Id: str) -> Dict[str, Any]:
```

### Client().get_hosted_zone_count

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L188)

```python
def get_hosted_zone_count() -> Dict[str, Any]:
```

### Client().get_hosted_zone_limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L192)

```python
def get_hosted_zone_limit(Type: str, HostedZoneId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L196)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_query_logging_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L200)

```python
def get_query_logging_config(Id: str) -> Dict[str, Any]:
```

### Client().get_reusable_delegation_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L204)

```python
def get_reusable_delegation_set(Id: str) -> Dict[str, Any]:
```

### Client().get_reusable_delegation_set_limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L208)

```python
def get_reusable_delegation_set_limit(
    Type: str,
    DelegationSetId: str,
) -> Dict[str, Any]:
```

### Client().get_traffic_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L214)

```python
def get_traffic_policy(Id: str, Version: int) -> Dict[str, Any]:
```

### Client().get_traffic_policy_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L218)

```python
def get_traffic_policy_instance(Id: str) -> Dict[str, Any]:
```

### Client().get_traffic_policy_instance_count

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L222)

```python
def get_traffic_policy_instance_count() -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L226)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_geo_locations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L230)

```python
def list_geo_locations(
    StartContinentCode: str = None,
    StartCountryCode: str = None,
    StartSubdivisionCode: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_health_checks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L240)

```python
def list_health_checks(
    Marker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_hosted_zones

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L246)

```python
def list_hosted_zones(
    Marker: str = None,
    MaxItems: str = None,
    DelegationSetId: str = None,
) -> Dict[str, Any]:
```

### Client().list_hosted_zones_by_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L252)

```python
def list_hosted_zones_by_name(
    DNSName: str = None,
    HostedZoneId: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_query_logging_configs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L258)

```python
def list_query_logging_configs(
    HostedZoneId: str = None,
    NextToken: str = None,
    MaxResults: str = None,
) -> Dict[str, Any]:
```

### Client().list_resource_record_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L264)

```python
def list_resource_record_sets(
    HostedZoneId: str,
    StartRecordName: str = None,
    StartRecordType: str = None,
    StartRecordIdentifier: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_reusable_delegation_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L275)

```python
def list_reusable_delegation_sets(
    Marker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L281)

```python
def list_tags_for_resource(
    ResourceType: str,
    ResourceId: str,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L287)

```python
def list_tags_for_resources(
    ResourceType: str,
    ResourceIds: List[Any],
) -> Dict[str, Any]:
```

### Client().list_traffic_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L293)

```python
def list_traffic_policies(
    TrafficPolicyIdMarker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_traffic_policy_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L299)

```python
def list_traffic_policy_instances(
    HostedZoneIdMarker: str = None,
    TrafficPolicyInstanceNameMarker: str = None,
    TrafficPolicyInstanceTypeMarker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_traffic_policy_instances_by_hosted_zone

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L309)

```python
def list_traffic_policy_instances_by_hosted_zone(
    HostedZoneId: str,
    TrafficPolicyInstanceNameMarker: str = None,
    TrafficPolicyInstanceTypeMarker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_traffic_policy_instances_by_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L319)

```python
def list_traffic_policy_instances_by_policy(
    TrafficPolicyId: str,
    TrafficPolicyVersion: int,
    HostedZoneIdMarker: str = None,
    TrafficPolicyInstanceNameMarker: str = None,
    TrafficPolicyInstanceTypeMarker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_traffic_policy_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L331)

```python
def list_traffic_policy_versions(
    Id: str,
    TrafficPolicyVersionMarker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_vpc_association_authorizations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L337)

```python
def list_vpc_association_authorizations(
    HostedZoneId: str,
    NextToken: str = None,
    MaxResults: str = None,
) -> Dict[str, Any]:
```

### Client().test_dns_answer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L343)

```python
def test_dns_answer(
    HostedZoneId: str,
    RecordName: str,
    RecordType: str,
    ResolverIP: str = None,
    EDNS0ClientSubnetIP: str = None,
    EDNS0ClientSubnetMask: str = None,
) -> Dict[str, Any]:
```

### Client().update_health_check

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L355)

```python
def update_health_check(
    HealthCheckId: str,
    HealthCheckVersion: int = None,
    IPAddress: str = None,
    Port: int = None,
    ResourcePath: str = None,
    FullyQualifiedDomainName: str = None,
    SearchString: str = None,
    FailureThreshold: int = None,
    Inverted: bool = None,
    Disabled: bool = None,
    HealthThreshold: int = None,
    ChildHealthChecks: List[Any] = None,
    EnableSNI: bool = None,
    Regions: List[Any] = None,
    AlarmIdentifier: Dict[str, Any] = None,
    InsufficientDataHealthStatus: str = None,
    ResetElements: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_hosted_zone_comment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L378)

```python
def update_hosted_zone_comment(
    Id: str,
    Comment: str = None,
) -> Dict[str, Any]:
```

### Client().update_traffic_policy_comment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L384)

```python
def update_traffic_policy_comment(
    Id: str,
    Version: int,
    Comment: str,
) -> Dict[str, Any]:
```

### Client().update_traffic_policy_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/client.py#L390)

```python
def update_traffic_policy_instance(
    Id: str,
    TTL: int,
    TrafficPolicyId: str,
    TrafficPolicyVersion: int,
) -> Dict[str, Any]:
```
