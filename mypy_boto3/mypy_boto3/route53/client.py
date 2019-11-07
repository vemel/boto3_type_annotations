from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_vpc_with_hosted_zone(
        self,
        HostedZoneId: str,
        VPC: Dict,
        Comment: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def change_resource_record_sets(
        self,
        HostedZoneId: str,
        ChangeBatch: Dict,
    ) -> Dict:
        pass


    def change_tags_for_resource(
        self,
        ResourceType: str,
        ResourceId: str,
        AddTags: Optional[List] = None,
        RemoveTagKeys: Optional[List] = None,
    ) -> Dict:
        pass


    def create_health_check(
        self,
        CallerReference: str,
        HealthCheckConfig: Dict,
    ) -> Dict:
        pass


    def create_hosted_zone(
        self,
        Name: str,
        CallerReference: str,
        VPC: Optional[Dict] = None,
        HostedZoneConfig: Optional[Dict] = None,
        DelegationSetId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_query_logging_config(
        self,
        HostedZoneId: str,
        CloudWatchLogsLogGroupArn: str,
    ) -> Dict:
        pass


    def create_reusable_delegation_set(
        self,
        CallerReference: str,
        HostedZoneId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_traffic_policy(
        self,
        Name: str,
        Document: str,
        Comment: Optional[str] = None,
    ) -> Dict:
        pass


    def create_traffic_policy_instance(
        self,
        HostedZoneId: str,
        Name: str,
        TTL: int,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
    ) -> Dict:
        pass


    def create_traffic_policy_version(
        self,
        Id: str,
        Document: str,
        Comment: Optional[str] = None,
    ) -> Dict:
        pass


    def create_vpc_association_authorization(
        self,
        HostedZoneId: str,
        VPC: Dict,
    ) -> Dict:
        pass


    def delete_health_check(
        self,
        HealthCheckId: str,
    ) -> Dict:
        pass


    def delete_hosted_zone(
        self,
        Id: str,
    ) -> Dict:
        pass


    def delete_query_logging_config(
        self,
        Id: str,
    ) -> Dict:
        pass


    def delete_reusable_delegation_set(
        self,
        Id: str,
    ) -> Dict:
        pass


    def delete_traffic_policy(
        self,
        Id: str,
        Version: int,
    ) -> Dict:
        pass


    def delete_traffic_policy_instance(
        self,
        Id: str,
    ) -> Dict:
        pass


    def delete_vpc_association_authorization(
        self,
        HostedZoneId: str,
        VPC: Dict,
    ) -> Dict:
        pass


    def disassociate_vpc_from_hosted_zone(
        self,
        HostedZoneId: str,
        VPC: Dict,
        Comment: Optional[str] = None,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_account_limit(
        self,
        Type: str,
    ) -> Dict:
        pass


    def get_change(
        self,
        Id: str,
    ) -> Dict:
        pass


    def get_checker_ip_ranges(
        self,
    ) -> Dict:
        pass


    def get_geo_location(
        self,
        ContinentCode: Optional[str] = None,
        CountryCode: Optional[str] = None,
        SubdivisionCode: Optional[str] = None,
    ) -> Dict:
        pass


    def get_health_check(
        self,
        HealthCheckId: str,
    ) -> Dict:
        pass


    def get_health_check_count(
        self,
    ) -> Dict:
        pass


    def get_health_check_last_failure_reason(
        self,
        HealthCheckId: str,
    ) -> Dict:
        pass


    def get_health_check_status(
        self,
        HealthCheckId: str,
    ) -> Dict:
        pass


    def get_hosted_zone(
        self,
        Id: str,
    ) -> Dict:
        pass


    def get_hosted_zone_count(
        self,
    ) -> Dict:
        pass


    def get_hosted_zone_limit(
        self,
        Type: str,
        HostedZoneId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_query_logging_config(
        self,
        Id: str,
    ) -> Dict:
        pass


    def get_reusable_delegation_set(
        self,
        Id: str,
    ) -> Dict:
        pass


    def get_reusable_delegation_set_limit(
        self,
        Type: str,
        DelegationSetId: str,
    ) -> Dict:
        pass


    def get_traffic_policy(
        self,
        Id: str,
        Version: int,
    ) -> Dict:
        pass


    def get_traffic_policy_instance(
        self,
        Id: str,
    ) -> Dict:
        pass


    def get_traffic_policy_instance_count(
        self,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_geo_locations(
        self,
        StartContinentCode: Optional[str] = None,
        StartCountryCode: Optional[str] = None,
        StartSubdivisionCode: Optional[str] = None,
        MaxItems: Optional[str] = None,
    ) -> Dict:
        pass


    def list_health_checks(
        self,
        Marker: Optional[str] = None,
        MaxItems: Optional[str] = None,
    ) -> Dict:
        pass


    def list_hosted_zones(
        self,
        Marker: Optional[str] = None,
        MaxItems: Optional[str] = None,
        DelegationSetId: Optional[str] = None,
    ) -> Dict:
        pass


    def list_hosted_zones_by_name(
        self,
        DNSName: Optional[str] = None,
        HostedZoneId: Optional[str] = None,
        MaxItems: Optional[str] = None,
    ) -> Dict:
        pass


    def list_query_logging_configs(
        self,
        HostedZoneId: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[str] = None,
    ) -> Dict:
        pass


    def list_resource_record_sets(
        self,
        HostedZoneId: str,
        StartRecordName: Optional[str] = None,
        StartRecordType: Optional[str] = None,
        StartRecordIdentifier: Optional[str] = None,
        MaxItems: Optional[str] = None,
    ) -> Dict:
        pass


    def list_reusable_delegation_sets(
        self,
        Marker: Optional[str] = None,
        MaxItems: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceType: str,
        ResourceId: str,
    ) -> Dict:
        pass


    def list_tags_for_resources(
        self,
        ResourceType: str,
        ResourceIds: List,
    ) -> Dict:
        pass


    def list_traffic_policies(
        self,
        TrafficPolicyIdMarker: Optional[str] = None,
        MaxItems: Optional[str] = None,
    ) -> Dict:
        pass


    def list_traffic_policy_instances(
        self,
        HostedZoneIdMarker: Optional[str] = None,
        TrafficPolicyInstanceNameMarker: Optional[str] = None,
        TrafficPolicyInstanceTypeMarker: Optional[str] = None,
        MaxItems: Optional[str] = None,
    ) -> Dict:
        pass


    def list_traffic_policy_instances_by_hosted_zone(
        self,
        HostedZoneId: str,
        TrafficPolicyInstanceNameMarker: Optional[str] = None,
        TrafficPolicyInstanceTypeMarker: Optional[str] = None,
        MaxItems: Optional[str] = None,
    ) -> Dict:
        pass


    def list_traffic_policy_instances_by_policy(
        self,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
        HostedZoneIdMarker: Optional[str] = None,
        TrafficPolicyInstanceNameMarker: Optional[str] = None,
        TrafficPolicyInstanceTypeMarker: Optional[str] = None,
        MaxItems: Optional[str] = None,
    ) -> Dict:
        pass


    def list_traffic_policy_versions(
        self,
        Id: str,
        TrafficPolicyVersionMarker: Optional[str] = None,
        MaxItems: Optional[str] = None,
    ) -> Dict:
        pass


    def list_vpc_association_authorizations(
        self,
        HostedZoneId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[str] = None,
    ) -> Dict:
        pass


    def test_dns_answer(
        self,
        HostedZoneId: str,
        RecordName: str,
        RecordType: str,
        ResolverIP: Optional[str] = None,
        EDNS0ClientSubnetIP: Optional[str] = None,
        EDNS0ClientSubnetMask: Optional[str] = None,
    ) -> Dict:
        pass


    def update_health_check(
        self,
        HealthCheckId: str,
        HealthCheckVersion: Optional[int] = None,
        IPAddress: Optional[str] = None,
        Port: Optional[int] = None,
        ResourcePath: Optional[str] = None,
        FullyQualifiedDomainName: Optional[str] = None,
        SearchString: Optional[str] = None,
        FailureThreshold: Optional[int] = None,
        Inverted: Optional[bool] = None,
        Disabled: Optional[bool] = None,
        HealthThreshold: Optional[int] = None,
        ChildHealthChecks: Optional[List] = None,
        EnableSNI: Optional[bool] = None,
        Regions: Optional[List] = None,
        AlarmIdentifier: Optional[Dict] = None,
        InsufficientDataHealthStatus: Optional[str] = None,
        ResetElements: Optional[List] = None,
    ) -> Dict:
        pass


    def update_hosted_zone_comment(
        self,
        Id: str,
        Comment: Optional[str] = None,
    ) -> Dict:
        pass


    def update_traffic_policy_comment(
        self,
        Id: str,
        Version: int,
        Comment: str,
    ) -> Dict:
        pass


    def update_traffic_policy_instance(
        self,
        Id: str,
        TTL: int,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
    ) -> Dict:
        pass

