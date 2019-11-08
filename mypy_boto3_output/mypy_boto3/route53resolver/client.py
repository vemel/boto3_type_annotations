from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_resolver_endpoint_ip_address(
        self, ResolverEndpointId: str, IpAddress: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_resolver_rule(
        self, ResolverRuleId: str, VPCId: str, Name: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_resolver_endpoint(
        self,
        CreatorRequestId: str,
        SecurityGroupIds: List[Any],
        Direction: str,
        IpAddresses: List[Any],
        Name: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_resolver_rule(
        self,
        CreatorRequestId: str,
        RuleType: str,
        DomainName: str,
        Name: str = None,
        TargetIps: List[Any] = None,
        ResolverEndpointId: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_resolver_endpoint(self, ResolverEndpointId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_resolver_rule(self, ResolverRuleId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_resolver_endpoint_ip_address(
        self, ResolverEndpointId: str, IpAddress: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_resolver_rule(
        self, VPCId: str, ResolverRuleId: str
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
    def get_resolver_endpoint(self, ResolverEndpointId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_resolver_rule(self, ResolverRuleId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_resolver_rule_association(
        self, ResolverRuleAssociationId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_resolver_rule_policy(self, Arn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_resolver_endpoint_ip_addresses(
        self, ResolverEndpointId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resolver_endpoints(
        self, MaxResults: int = None, NextToken: str = None, Filters: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resolver_rule_associations(
        self, MaxResults: int = None, NextToken: str = None, Filters: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resolver_rules(
        self, MaxResults: int = None, NextToken: str = None, Filters: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_resolver_rule_policy(
        self, Arn: str, ResolverRulePolicy: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_resolver_endpoint(
        self, ResolverEndpointId: str, Name: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_resolver_rule(
        self, ResolverRuleId: str, Config: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass
