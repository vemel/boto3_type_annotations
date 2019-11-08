from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_tags(self, LoadBalancerNames: List[Any], Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def apply_security_groups_to_load_balancer(
        self, LoadBalancerName: str, SecurityGroups: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_load_balancer_to_subnets(
        self, LoadBalancerName: str, Subnets: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def configure_health_check(
        self, LoadBalancerName: str, HealthCheck: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_app_cookie_stickiness_policy(
        self, LoadBalancerName: str, PolicyName: str, CookieName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_lb_cookie_stickiness_policy(
        self, LoadBalancerName: str, PolicyName: str, CookieExpirationPeriod: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_load_balancer(
        self,
        LoadBalancerName: str,
        Listeners: List[Any],
        AvailabilityZones: List[Any] = None,
        Subnets: List[Any] = None,
        SecurityGroups: List[Any] = None,
        Scheme: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_load_balancer_listeners(
        self, LoadBalancerName: str, Listeners: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_load_balancer_policy(
        self,
        LoadBalancerName: str,
        PolicyName: str,
        PolicyTypeName: str,
        PolicyAttributes: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_load_balancer(self, LoadBalancerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_load_balancer_listeners(
        self, LoadBalancerName: str, LoadBalancerPorts: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_load_balancer_policy(
        self, LoadBalancerName: str, PolicyName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_instances_from_load_balancer(
        self, LoadBalancerName: str, Instances: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_account_limits(
        self, Marker: str = None, PageSize: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_instance_health(
        self, LoadBalancerName: str, Instances: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_load_balancer_attributes(
        self, LoadBalancerName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_load_balancer_policies(
        self, LoadBalancerName: str = None, PolicyNames: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_load_balancer_policy_types(
        self, PolicyTypeNames: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_load_balancers(
        self,
        LoadBalancerNames: List[Any] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_tags(self, LoadBalancerNames: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_load_balancer_from_subnets(
        self, LoadBalancerName: str, Subnets: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_availability_zones_for_load_balancer(
        self, LoadBalancerName: str, AvailabilityZones: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_availability_zones_for_load_balancer(
        self, LoadBalancerName: str, AvailabilityZones: List[Any]
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
    def modify_load_balancer_attributes(
        self, LoadBalancerName: str, LoadBalancerAttributes: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_instances_with_load_balancer(
        self, LoadBalancerName: str, Instances: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags(
        self, LoadBalancerNames: List[Any], Tags: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_load_balancer_listener_ssl_certificate(
        self, LoadBalancerName: str, LoadBalancerPort: int, SSLCertificateId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_load_balancer_policies_for_backend_server(
        self, LoadBalancerName: str, InstancePort: int, PolicyNames: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_load_balancer_policies_of_listener(
        self, LoadBalancerName: str, LoadBalancerPort: int, PolicyNames: List[Any]
    ) -> Dict[str, Any]:
        pass
