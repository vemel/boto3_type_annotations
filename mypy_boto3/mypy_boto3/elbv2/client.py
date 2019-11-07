from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_listener_certificates(
        self,
        ListenerArn: str,
        Certificates: List,
    ) -> Dict:
        pass


    def add_tags(
        self,
        ResourceArns: List,
        Tags: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_listener(
        self,
        LoadBalancerArn: str,
        Protocol: str,
        Port: int,
        DefaultActions: List,
        SslPolicy: Optional[str] = None,
        Certificates: Optional[List] = None,
    ) -> Dict:
        pass


    def create_load_balancer(
        self,
        Name: str,
        Subnets: Optional[List] = None,
        SubnetMappings: Optional[List] = None,
        SecurityGroups: Optional[List] = None,
        Scheme: Optional[str] = None,
        Tags: Optional[List] = None,
        Type: Optional[str] = None,
        IpAddressType: Optional[str] = None,
    ) -> Dict:
        pass


    def create_rule(
        self,
        ListenerArn: str,
        Conditions: List,
        Priority: int,
        Actions: List,
    ) -> Dict:
        pass


    def create_target_group(
        self,
        Name: str,
        Protocol: Optional[str] = None,
        Port: Optional[int] = None,
        VpcId: Optional[str] = None,
        HealthCheckProtocol: Optional[str] = None,
        HealthCheckPort: Optional[str] = None,
        HealthCheckEnabled: Optional[bool] = None,
        HealthCheckPath: Optional[str] = None,
        HealthCheckIntervalSeconds: Optional[int] = None,
        HealthCheckTimeoutSeconds: Optional[int] = None,
        HealthyThresholdCount: Optional[int] = None,
        UnhealthyThresholdCount: Optional[int] = None,
        Matcher: Optional[Dict] = None,
        TargetType: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_listener(
        self,
        ListenerArn: str,
    ) -> Dict:
        pass


    def delete_load_balancer(
        self,
        LoadBalancerArn: str,
    ) -> Dict:
        pass


    def delete_rule(
        self,
        RuleArn: str,
    ) -> Dict:
        pass


    def delete_target_group(
        self,
        TargetGroupArn: str,
    ) -> Dict:
        pass


    def deregister_targets(
        self,
        TargetGroupArn: str,
        Targets: List,
    ) -> Dict:
        pass


    def describe_account_limits(
        self,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_listener_certificates(
        self,
        ListenerArn: str,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_listeners(
        self,
        LoadBalancerArn: Optional[str] = None,
        ListenerArns: Optional[List] = None,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_load_balancer_attributes(
        self,
        LoadBalancerArn: str,
    ) -> Dict:
        pass


    def describe_load_balancers(
        self,
        LoadBalancerArns: Optional[List] = None,
        Names: Optional[List] = None,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_rules(
        self,
        ListenerArn: Optional[str] = None,
        RuleArns: Optional[List] = None,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_ssl_policies(
        self,
        Names: Optional[List] = None,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_tags(
        self,
        ResourceArns: List,
    ) -> Dict:
        pass


    def describe_target_group_attributes(
        self,
        TargetGroupArn: str,
    ) -> Dict:
        pass


    def describe_target_groups(
        self,
        LoadBalancerArn: Optional[str] = None,
        TargetGroupArns: Optional[List] = None,
        Names: Optional[List] = None,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_target_health(
        self,
        TargetGroupArn: str,
        Targets: Optional[List] = None,
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


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def modify_listener(
        self,
        ListenerArn: str,
        Port: Optional[int] = None,
        Protocol: Optional[str] = None,
        SslPolicy: Optional[str] = None,
        Certificates: Optional[List] = None,
        DefaultActions: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_load_balancer_attributes(
        self,
        LoadBalancerArn: str,
        Attributes: List,
    ) -> Dict:
        pass


    def modify_rule(
        self,
        RuleArn: str,
        Conditions: Optional[List] = None,
        Actions: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_target_group(
        self,
        TargetGroupArn: str,
        HealthCheckProtocol: Optional[str] = None,
        HealthCheckPort: Optional[str] = None,
        HealthCheckPath: Optional[str] = None,
        HealthCheckEnabled: Optional[bool] = None,
        HealthCheckIntervalSeconds: Optional[int] = None,
        HealthCheckTimeoutSeconds: Optional[int] = None,
        HealthyThresholdCount: Optional[int] = None,
        UnhealthyThresholdCount: Optional[int] = None,
        Matcher: Optional[Dict] = None,
    ) -> Dict:
        pass


    def modify_target_group_attributes(
        self,
        TargetGroupArn: str,
        Attributes: List,
    ) -> Dict:
        pass


    def register_targets(
        self,
        TargetGroupArn: str,
        Targets: List,
    ) -> Dict:
        pass


    def remove_listener_certificates(
        self,
        ListenerArn: str,
        Certificates: List,
    ) -> Dict:
        pass


    def remove_tags(
        self,
        ResourceArns: List,
        TagKeys: List,
    ) -> Dict:
        pass


    def set_ip_address_type(
        self,
        LoadBalancerArn: str,
        IpAddressType: str,
    ) -> Dict:
        pass


    def set_rule_priorities(
        self,
        RulePriorities: List,
    ) -> Dict:
        pass


    def set_security_groups(
        self,
        LoadBalancerArn: str,
        SecurityGroups: List,
    ) -> Dict:
        pass


    def set_subnets(
        self,
        LoadBalancerArn: str,
        Subnets: Optional[List] = None,
        SubnetMappings: Optional[List] = None,
    ) -> Dict:
        pass

