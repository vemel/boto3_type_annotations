from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_web_acl(self, WebACLId: str, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_byte_match_set(self, Name: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_geo_match_set(self, Name: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_ip_set(self, Name: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_rate_based_rule(
        self,
        Name: str,
        MetricName: str,
        RateKey: str,
        RateLimit: int,
        ChangeToken: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_regex_match_set(self, Name: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_regex_pattern_set(self, Name: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_rule(
        self, Name: str, MetricName: str, ChangeToken: str, Tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_rule_group(
        self, Name: str, MetricName: str, ChangeToken: str, Tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_size_constraint_set(self, Name: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_sql_injection_match_set(
        self, Name: str, ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_web_acl(
        self,
        Name: str,
        MetricName: str,
        DefaultAction: Dict[str, Any],
        ChangeToken: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_xss_match_set(self, Name: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_byte_match_set(
        self, ByteMatchSetId: str, ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_geo_match_set(
        self, GeoMatchSetId: str, ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_ip_set(self, IPSetId: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_logging_configuration(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_permission_policy(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_rate_based_rule(self, RuleId: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_regex_match_set(
        self, RegexMatchSetId: str, ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_regex_pattern_set(
        self, RegexPatternSetId: str, ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_rule(self, RuleId: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_rule_group(self, RuleGroupId: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_size_constraint_set(
        self, SizeConstraintSetId: str, ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_sql_injection_match_set(
        self, SqlInjectionMatchSetId: str, ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_web_acl(self, WebACLId: str, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_xss_match_set(
        self, XssMatchSetId: str, ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_web_acl(self, ResourceArn: str) -> Dict[str, Any]:
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
    def get_byte_match_set(self, ByteMatchSetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_change_token(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_change_token_status(self, ChangeToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_geo_match_set(self, GeoMatchSetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_ip_set(self, IPSetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_logging_configuration(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_permission_policy(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_rate_based_rule(self, RuleId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_rate_based_rule_managed_keys(
        self, RuleId: str, NextMarker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_regex_match_set(self, RegexMatchSetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_regex_pattern_set(self, RegexPatternSetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_rule(self, RuleId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_rule_group(self, RuleGroupId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_sampled_requests(
        self, WebAclId: str, RuleId: str, TimeWindow: Dict[str, Any], MaxItems: int
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_size_constraint_set(self, SizeConstraintSetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_sql_injection_match_set(
        self, SqlInjectionMatchSetId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def get_web_acl(self, WebACLId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_web_acl_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_xss_match_set(self, XssMatchSetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_activated_rules_in_rule_group(
        self, RuleGroupId: str = None, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_byte_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_geo_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_ip_sets(self, NextMarker: str = None, Limit: int = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_logging_configurations(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_rate_based_rules(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_regex_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_regex_pattern_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resources_for_web_acl(
        self, WebACLId: str, ResourceType: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_rule_groups(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_rules(self, NextMarker: str = None, Limit: int = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_size_constraint_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_sql_injection_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_subscribed_rule_groups(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, ResourceARN: str, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_web_acls(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_xss_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_logging_configuration(
        self, LoggingConfiguration: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_permission_policy(self, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_byte_match_set(
        self, ByteMatchSetId: str, ChangeToken: str, Updates: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_geo_match_set(
        self, GeoMatchSetId: str, ChangeToken: str, Updates: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_ip_set(
        self, IPSetId: str, ChangeToken: str, Updates: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_rate_based_rule(
        self, RuleId: str, ChangeToken: str, Updates: List[Any], RateLimit: int
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_regex_match_set(
        self, RegexMatchSetId: str, Updates: List[Any], ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_regex_pattern_set(
        self, RegexPatternSetId: str, Updates: List[Any], ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_rule(
        self, RuleId: str, ChangeToken: str, Updates: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_rule_group(
        self, RuleGroupId: str, Updates: List[Any], ChangeToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_size_constraint_set(
        self, SizeConstraintSetId: str, ChangeToken: str, Updates: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_sql_injection_match_set(
        self, SqlInjectionMatchSetId: str, ChangeToken: str, Updates: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_web_acl(
        self,
        WebACLId: str,
        ChangeToken: str,
        Updates: List[Any] = None,
        DefaultAction: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_xss_match_set(
        self, XssMatchSetId: str, ChangeToken: str, Updates: List[Any]
    ) -> Dict[str, Any]:
        pass
