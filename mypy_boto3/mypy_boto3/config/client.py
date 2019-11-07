from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_get_aggregate_resource_config(
        self,
        ConfigurationAggregatorName: str,
        ResourceIdentifiers: List,
    ) -> Dict:
        pass


    def batch_get_resource_config(
        self,
        resourceKeys: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def delete_aggregation_authorization(
        self,
        AuthorizedAccountId: str,
        AuthorizedAwsRegion: str,
    ):
        pass


    def delete_config_rule(
        self,
        ConfigRuleName: str,
    ):
        pass


    def delete_configuration_aggregator(
        self,
        ConfigurationAggregatorName: str,
    ):
        pass


    def delete_configuration_recorder(
        self,
        ConfigurationRecorderName: str,
    ):
        pass


    def delete_delivery_channel(
        self,
        DeliveryChannelName: str,
    ):
        pass


    def delete_evaluation_results(
        self,
        ConfigRuleName: str,
    ) -> Dict:
        pass


    def delete_organization_config_rule(
        self,
        OrganizationConfigRuleName: str,
    ):
        pass


    def delete_pending_aggregation_request(
        self,
        RequesterAccountId: str,
        RequesterAwsRegion: str,
    ):
        pass


    def delete_remediation_configuration(
        self,
        ConfigRuleName: str,
        ResourceType: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_remediation_exceptions(
        self,
        ConfigRuleName: str,
        ResourceKeys: List,
    ) -> Dict:
        pass


    def delete_retention_configuration(
        self,
        RetentionConfigurationName: str,
    ):
        pass


    def deliver_config_snapshot(
        self,
        deliveryChannelName: str,
    ) -> Dict:
        pass


    def describe_aggregate_compliance_by_config_rules(
        self,
        ConfigurationAggregatorName: str,
        Filters: Optional[Dict] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_aggregation_authorizations(
        self,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_compliance_by_config_rule(
        self,
        ConfigRuleNames: Optional[List] = None,
        ComplianceTypes: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_compliance_by_resource(
        self,
        ResourceType: Optional[str] = None,
        ResourceId: Optional[str] = None,
        ComplianceTypes: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_config_rule_evaluation_status(
        self,
        ConfigRuleNames: Optional[List] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_config_rules(
        self,
        ConfigRuleNames: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_configuration_aggregator_sources_status(
        self,
        ConfigurationAggregatorName: str,
        UpdateStatus: Optional[List] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_configuration_aggregators(
        self,
        ConfigurationAggregatorNames: Optional[List] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_configuration_recorder_status(
        self,
        ConfigurationRecorderNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_configuration_recorders(
        self,
        ConfigurationRecorderNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_delivery_channel_status(
        self,
        DeliveryChannelNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_delivery_channels(
        self,
        DeliveryChannelNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_organization_config_rule_statuses(
        self,
        OrganizationConfigRuleNames: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_organization_config_rules(
        self,
        OrganizationConfigRuleNames: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_pending_aggregation_requests(
        self,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_remediation_configurations(
        self,
        ConfigRuleNames: List,
    ) -> Dict:
        pass


    def describe_remediation_exceptions(
        self,
        ConfigRuleName: str,
        ResourceKeys: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_remediation_execution_status(
        self,
        ConfigRuleName: str,
        ResourceKeys: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_retention_configurations(
        self,
        RetentionConfigurationNames: Optional[List] = None,
        NextToken: Optional[str] = None,
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


    def get_aggregate_compliance_details_by_config_rule(
        self,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_aggregate_config_rule_compliance_summary(
        self,
        ConfigurationAggregatorName: str,
        Filters: Optional[Dict] = None,
        GroupByKey: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_aggregate_discovered_resource_counts(
        self,
        ConfigurationAggregatorName: str,
        Filters: Optional[Dict] = None,
        GroupByKey: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_aggregate_resource_config(
        self,
        ConfigurationAggregatorName: str,
        ResourceIdentifier: Dict,
    ) -> Dict:
        pass


    def get_compliance_details_by_config_rule(
        self,
        ConfigRuleName: str,
        ComplianceTypes: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_compliance_details_by_resource(
        self,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_compliance_summary_by_config_rule(
        self,
    ) -> Dict:
        pass


    def get_compliance_summary_by_resource_type(
        self,
        ResourceTypes: Optional[List] = None,
    ) -> Dict:
        pass


    def get_discovered_resource_counts(
        self,
        resourceTypes: Optional[List] = None,
        limit: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_organization_config_rule_detailed_status(
        self,
        OrganizationConfigRuleName: str,
        Filters: Optional[Dict] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_resource_config_history(
        self,
        resourceType: str,
        resourceId: str,
        laterTime: Optional[datetime] = None,
        earlierTime: Optional[datetime] = None,
        chronologicalOrder: Optional[str] = None,
        limit: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_aggregate_discovered_resources(
        self,
        ConfigurationAggregatorName: str,
        ResourceType: str,
        Filters: Optional[Dict] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_discovered_resources(
        self,
        resourceType: str,
        resourceIds: Optional[List] = None,
        resourceName: Optional[str] = None,
        limit: Optional[int] = None,
        includeDeletedResources: Optional[bool] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_aggregation_authorization(
        self,
        AuthorizedAccountId: str,
        AuthorizedAwsRegion: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def put_config_rule(
        self,
        ConfigRule: Dict,
        Tags: Optional[List] = None,
    ):
        pass


    def put_configuration_aggregator(
        self,
        ConfigurationAggregatorName: str,
        AccountAggregationSources: Optional[List] = None,
        OrganizationAggregationSource: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def put_configuration_recorder(
        self,
        ConfigurationRecorder: Dict,
    ):
        pass


    def put_delivery_channel(
        self,
        DeliveryChannel: Dict,
    ):
        pass


    def put_evaluations(
        self,
        ResultToken: str,
        Evaluations: Optional[List] = None,
        TestMode: Optional[bool] = None,
    ) -> Dict:
        pass


    def put_organization_config_rule(
        self,
        OrganizationConfigRuleName: str,
        OrganizationManagedRuleMetadata: Optional[Dict] = None,
        OrganizationCustomRuleMetadata: Optional[Dict] = None,
        ExcludedAccounts: Optional[List] = None,
    ) -> Dict:
        pass


    def put_remediation_configurations(
        self,
        RemediationConfigurations: List,
    ) -> Dict:
        pass


    def put_remediation_exceptions(
        self,
        ConfigRuleName: str,
        ResourceKeys: List,
        Message: Optional[str] = None,
        ExpirationTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def put_retention_configuration(
        self,
        RetentionPeriodInDays: int,
    ) -> Dict:
        pass


    def select_resource_config(
        self,
        Expression: str,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def start_config_rules_evaluation(
        self,
        ConfigRuleNames: Optional[List] = None,
    ) -> Dict:
        pass


    def start_configuration_recorder(
        self,
        ConfigurationRecorderName: str,
    ):
        pass


    def start_remediation_execution(
        self,
        ConfigRuleName: str,
        ResourceKeys: List,
    ) -> Dict:
        pass


    def stop_configuration_recorder(
        self,
        ConfigurationRecorderName: str,
    ):
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: List,
    ):
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass

