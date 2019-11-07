from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeAggregateComplianceByConfigRules(Paginator):
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        Filters: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeAggregationAuthorizations(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeComplianceByConfigRule(Paginator):
    def paginate(
        self,
        ConfigRuleNames: Optional[List] = None,
        ComplianceTypes: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeComplianceByResource(Paginator):
    def paginate(
        self,
        ResourceType: Optional[str] = None,
        ResourceId: Optional[str] = None,
        ComplianceTypes: Optional[List] = None,
        Limit: Optional[int] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeConfigRuleEvaluationStatus(Paginator):
    def paginate(
        self,
        ConfigRuleNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeConfigRules(Paginator):
    def paginate(
        self,
        ConfigRuleNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeConfigurationAggregatorSourcesStatus(Paginator):
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        UpdateStatus: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeConfigurationAggregators(Paginator):
    def paginate(
        self,
        ConfigurationAggregatorNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribePendingAggregationRequests(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeRemediationExecutionStatus(Paginator):
    def paginate(
        self,
        ConfigRuleName: str,
        ResourceKeys: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeRetentionConfigurations(Paginator):
    def paginate(
        self,
        RetentionConfigurationNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetAggregateComplianceDetailsByConfigRule(Paginator):
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetComplianceDetailsByConfigRule(Paginator):
    def paginate(
        self,
        ConfigRuleName: str,
        ComplianceTypes: Optional[List] = None,
        Limit: Optional[int] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetComplianceDetailsByResource(Paginator):
    def paginate(
        self,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetResourceConfigHistory(Paginator):
    def paginate(
        self,
        resourceType: str,
        resourceId: str,
        laterTime: Optional[datetime] = None,
        earlierTime: Optional[datetime] = None,
        chronologicalOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAggregateDiscoveredResources(Paginator):
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ResourceType: str,
        Filters: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDiscoveredResources(Paginator):
    def paginate(
        self,
        resourceType: str,
        resourceIds: Optional[List] = None,
        resourceName: Optional[str] = None,
        limit: Optional[int] = None,
        includeDeletedResources: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

