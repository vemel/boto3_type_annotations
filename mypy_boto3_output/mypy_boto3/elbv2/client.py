from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_listener_certificates(
        self, ListenerArn: str, Certificates: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_tags(self, ResourceArns: List[Any], Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_listener(
        self,
        LoadBalancerArn: str,
        Protocol: str,
        Port: int,
        DefaultActions: List[Any],
        SslPolicy: str = None,
        Certificates: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_load_balancer(
        self,
        Name: str,
        Subnets: List[Any] = None,
        SubnetMappings: List[Any] = None,
        SecurityGroups: List[Any] = None,
        Scheme: str = None,
        Tags: List[Any] = None,
        Type: str = None,
        IpAddressType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_rule(
        self, ListenerArn: str, Conditions: List[Any], Priority: int, Actions: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_target_group(
        self,
        Name: str,
        Protocol: str = None,
        Port: int = None,
        VpcId: str = None,
        HealthCheckProtocol: str = None,
        HealthCheckPort: str = None,
        HealthCheckEnabled: bool = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        HealthCheckTimeoutSeconds: int = None,
        HealthyThresholdCount: int = None,
        UnhealthyThresholdCount: int = None,
        Matcher: Dict[str, Any] = None,
        TargetType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_listener(self, ListenerArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_load_balancer(self, LoadBalancerArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_rule(self, RuleArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_target_group(self, TargetGroupArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_targets(
        self, TargetGroupArn: str, Targets: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_account_limits(
        self, Marker: str = None, PageSize: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_listener_certificates(
        self, ListenerArn: str, Marker: str = None, PageSize: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_listeners(
        self,
        LoadBalancerArn: str = None,
        ListenerArns: List[Any] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_load_balancer_attributes(self, LoadBalancerArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_load_balancers(
        self,
        LoadBalancerArns: List[Any] = None,
        Names: List[Any] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_rules(
        self,
        ListenerArn: str = None,
        RuleArns: List[Any] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_ssl_policies(
        self, Names: List[Any] = None, Marker: str = None, PageSize: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_tags(self, ResourceArns: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_target_group_attributes(self, TargetGroupArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_target_groups(
        self,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[Any] = None,
        Names: List[Any] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_target_health(
        self, TargetGroupArn: str, Targets: List[Any] = None
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
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def modify_listener(
        self,
        ListenerArn: str,
        Port: int = None,
        Protocol: str = None,
        SslPolicy: str = None,
        Certificates: List[Any] = None,
        DefaultActions: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_load_balancer_attributes(
        self, LoadBalancerArn: str, Attributes: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_rule(
        self, RuleArn: str, Conditions: List[Any] = None, Actions: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_target_group(
        self,
        TargetGroupArn: str,
        HealthCheckProtocol: str = None,
        HealthCheckPort: str = None,
        HealthCheckPath: str = None,
        HealthCheckEnabled: bool = None,
        HealthCheckIntervalSeconds: int = None,
        HealthCheckTimeoutSeconds: int = None,
        HealthyThresholdCount: int = None,
        UnhealthyThresholdCount: int = None,
        Matcher: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_target_group_attributes(
        self, TargetGroupArn: str, Attributes: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_targets(
        self, TargetGroupArn: str, Targets: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_listener_certificates(
        self, ListenerArn: str, Certificates: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags(
        self, ResourceArns: List[Any], TagKeys: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_ip_address_type(
        self, LoadBalancerArn: str, IpAddressType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_rule_priorities(self, RulePriorities: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_security_groups(
        self, LoadBalancerArn: str, SecurityGroups: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_subnets(
        self,
        LoadBalancerArn: str,
        Subnets: List[Any] = None,
        SubnetMappings: List[Any] = None,
    ) -> Dict[str, Any]:
        pass
