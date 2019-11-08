from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_vpc_with_hosted_zone(
        self, HostedZoneId: str, VPC: Dict[str, Any], Comment: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def change_resource_record_sets(
        self, HostedZoneId: str, ChangeBatch: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def change_tags_for_resource(
        self,
        ResourceType: str,
        ResourceId: str,
        AddTags: List[Any] = None,
        RemoveTagKeys: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_health_check(
        self, CallerReference: str, HealthCheckConfig: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_hosted_zone(
        self,
        Name: str,
        CallerReference: str,
        VPC: Dict[str, Any] = None,
        HostedZoneConfig: Dict[str, Any] = None,
        DelegationSetId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_query_logging_config(
        self, HostedZoneId: str, CloudWatchLogsLogGroupArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_reusable_delegation_set(
        self, CallerReference: str, HostedZoneId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_traffic_policy(
        self, Name: str, Document: str, Comment: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_traffic_policy_instance(
        self,
        HostedZoneId: str,
        Name: str,
        TTL: int,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_traffic_policy_version(
        self, Id: str, Document: str, Comment: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_vpc_association_authorization(
        self, HostedZoneId: str, VPC: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_health_check(self, HealthCheckId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_hosted_zone(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_query_logging_config(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_reusable_delegation_set(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_traffic_policy(self, Id: str, Version: int) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_traffic_policy_instance(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_vpc_association_authorization(
        self, HostedZoneId: str, VPC: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_vpc_from_hosted_zone(
        self, HostedZoneId: str, VPC: Dict[str, Any], Comment: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_account_limit(self, Type: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_change(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_checker_ip_ranges(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_geo_location(
        self,
        ContinentCode: str = None,
        CountryCode: str = None,
        SubdivisionCode: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_health_check(self, HealthCheckId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_health_check_count(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_health_check_last_failure_reason(
        self, HealthCheckId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_health_check_status(self, HealthCheckId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_hosted_zone(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_hosted_zone_count(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_hosted_zone_limit(self, Type: str, HostedZoneId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_query_logging_config(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_reusable_delegation_set(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_reusable_delegation_set_limit(
        self, Type: str, DelegationSetId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_traffic_policy(self, Id: str, Version: int) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_traffic_policy_instance(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_traffic_policy_instance_count(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_geo_locations(
        self,
        StartContinentCode: str = None,
        StartCountryCode: str = None,
        StartSubdivisionCode: str = None,
        MaxItems: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_health_checks(
        self, Marker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_hosted_zones(
        self, Marker: str = None, MaxItems: str = None, DelegationSetId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_hosted_zones_by_name(
        self, DNSName: str = None, HostedZoneId: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_query_logging_configs(
        self, HostedZoneId: str = None, NextToken: str = None, MaxResults: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resource_record_sets(
        self,
        HostedZoneId: str,
        StartRecordName: str = None,
        StartRecordType: str = None,
        StartRecordIdentifier: str = None,
        MaxItems: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_reusable_delegation_sets(
        self, Marker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, ResourceType: str, ResourceId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resources(
        self, ResourceType: str, ResourceIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_traffic_policies(
        self, TrafficPolicyIdMarker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_traffic_policy_instances(
        self,
        HostedZoneIdMarker: str = None,
        TrafficPolicyInstanceNameMarker: str = None,
        TrafficPolicyInstanceTypeMarker: str = None,
        MaxItems: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_traffic_policy_instances_by_hosted_zone(
        self,
        HostedZoneId: str,
        TrafficPolicyInstanceNameMarker: str = None,
        TrafficPolicyInstanceTypeMarker: str = None,
        MaxItems: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_traffic_policy_instances_by_policy(
        self,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
        HostedZoneIdMarker: str = None,
        TrafficPolicyInstanceNameMarker: str = None,
        TrafficPolicyInstanceTypeMarker: str = None,
        MaxItems: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_traffic_policy_versions(
        self, Id: str, TrafficPolicyVersionMarker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_vpc_association_authorizations(
        self, HostedZoneId: str, NextToken: str = None, MaxResults: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def test_dns_answer(
        self,
        HostedZoneId: str,
        RecordName: str,
        RecordType: str,
        ResolverIP: str = None,
        EDNS0ClientSubnetIP: str = None,
        EDNS0ClientSubnetMask: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_health_check(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def update_hosted_zone_comment(
        self, Id: str, Comment: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_traffic_policy_comment(
        self, Id: str, Version: int, Comment: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_traffic_policy_instance(
        self, Id: str, TTL: int, TrafficPolicyId: str, TrafficPolicyVersion: int
    ) -> Dict[str, Any]:
        pass
