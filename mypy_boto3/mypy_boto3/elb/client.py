from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags(
        self,
        LoadBalancerNames: List,
        Tags: List,
    ) -> Dict:
        pass


    def apply_security_groups_to_load_balancer(
        self,
        LoadBalancerName: str,
        SecurityGroups: List,
    ) -> Dict:
        pass


    def attach_load_balancer_to_subnets(
        self,
        LoadBalancerName: str,
        Subnets: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def configure_health_check(
        self,
        LoadBalancerName: str,
        HealthCheck: Dict,
    ) -> Dict:
        pass


    def create_app_cookie_stickiness_policy(
        self,
        LoadBalancerName: str,
        PolicyName: str,
        CookieName: str,
    ) -> Dict:
        pass


    def create_lb_cookie_stickiness_policy(
        self,
        LoadBalancerName: str,
        PolicyName: str,
        CookieExpirationPeriod: Optional[int] = None,
    ) -> Dict:
        pass


    def create_load_balancer(
        self,
        LoadBalancerName: str,
        Listeners: List,
        AvailabilityZones: Optional[List] = None,
        Subnets: Optional[List] = None,
        SecurityGroups: Optional[List] = None,
        Scheme: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_load_balancer_listeners(
        self,
        LoadBalancerName: str,
        Listeners: List,
    ) -> Dict:
        pass


    def create_load_balancer_policy(
        self,
        LoadBalancerName: str,
        PolicyName: str,
        PolicyTypeName: str,
        PolicyAttributes: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_load_balancer(
        self,
        LoadBalancerName: str,
    ) -> Dict:
        pass


    def delete_load_balancer_listeners(
        self,
        LoadBalancerName: str,
        LoadBalancerPorts: List,
    ) -> Dict:
        pass


    def delete_load_balancer_policy(
        self,
        LoadBalancerName: str,
        PolicyName: str,
    ) -> Dict:
        pass


    def deregister_instances_from_load_balancer(
        self,
        LoadBalancerName: str,
        Instances: List,
    ) -> Dict:
        pass


    def describe_account_limits(
        self,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_instance_health(
        self,
        LoadBalancerName: str,
        Instances: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_load_balancer_attributes(
        self,
        LoadBalancerName: str,
    ) -> Dict:
        pass


    def describe_load_balancer_policies(
        self,
        LoadBalancerName: Optional[str] = None,
        PolicyNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_load_balancer_policy_types(
        self,
        PolicyTypeNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_load_balancers(
        self,
        LoadBalancerNames: Optional[List] = None,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_tags(
        self,
        LoadBalancerNames: List,
    ) -> Dict:
        pass


    def detach_load_balancer_from_subnets(
        self,
        LoadBalancerName: str,
        Subnets: List,
    ) -> Dict:
        pass


    def disable_availability_zones_for_load_balancer(
        self,
        LoadBalancerName: str,
        AvailabilityZones: List,
    ) -> Dict:
        pass


    def enable_availability_zones_for_load_balancer(
        self,
        LoadBalancerName: str,
        AvailabilityZones: List,
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


    def modify_load_balancer_attributes(
        self,
        LoadBalancerName: str,
        LoadBalancerAttributes: Dict,
    ) -> Dict:
        pass


    def register_instances_with_load_balancer(
        self,
        LoadBalancerName: str,
        Instances: List,
    ) -> Dict:
        pass


    def remove_tags(
        self,
        LoadBalancerNames: List,
        Tags: List,
    ) -> Dict:
        pass


    def set_load_balancer_listener_ssl_certificate(
        self,
        LoadBalancerName: str,
        LoadBalancerPort: int,
        SSLCertificateId: str,
    ) -> Dict:
        pass


    def set_load_balancer_policies_for_backend_server(
        self,
        LoadBalancerName: str,
        InstancePort: int,
        PolicyNames: List,
    ) -> Dict:
        pass


    def set_load_balancer_policies_of_listener(
        self,
        LoadBalancerName: str,
        LoadBalancerPort: int,
        PolicyNames: List,
    ) -> Dict:
        pass

