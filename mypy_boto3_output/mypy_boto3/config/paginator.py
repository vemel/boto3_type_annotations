from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeAggregateComplianceByConfigRules(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        Filters: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeAggregationAuthorizations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class DescribeComplianceByConfigRule(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ConfigRuleNames: List[Any] = None,
        ComplianceTypes: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeComplianceByResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[Any] = None,
        Limit: int = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeConfigRuleEvaluationStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ConfigRuleNames: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeConfigRules(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ConfigRuleNames: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeConfigurationAggregatorSourcesStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        UpdateStatus: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeConfigurationAggregators(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ConfigurationAggregatorNames: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribePendingAggregationRequests(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class DescribeRemediationExecutionStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ConfigRuleName: str,
        ResourceKeys: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeRetentionConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        RetentionConfigurationNames: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetAggregateComplianceDetailsByConfigRule(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetComplianceDetailsByConfigRule(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ConfigRuleName: str,
        ComplianceTypes: List[Any] = None,
        Limit: int = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetComplianceDetailsByResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetResourceConfigHistory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        resourceType: str,
        resourceId: str,
        laterTime: datetime = None,
        earlierTime: datetime = None,
        chronologicalOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAggregateDiscoveredResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ResourceType: str,
        Filters: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListDiscoveredResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        resourceType: str,
        resourceIds: List[Any] = None,
        resourceName: str = None,
        limit: int = None,
        includeDeletedResources: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
