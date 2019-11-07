from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def abort_environment_update(
        self,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
    ):
        pass


    def apply_environment_managed_action(
        self,
        ActionId: str,
        EnvironmentName: Optional[str] = None,
        EnvironmentId: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def check_dns_availability(
        self,
        CNAMEPrefix: str,
    ) -> Dict:
        pass


    def compose_environments(
        self,
        ApplicationName: Optional[str] = None,
        GroupName: Optional[str] = None,
        VersionLabels: Optional[List] = None,
    ) -> Dict:
        pass


    def create_application(
        self,
        ApplicationName: str,
        Description: Optional[str] = None,
        ResourceLifecycleConfig: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_application_version(
        self,
        ApplicationName: str,
        VersionLabel: str,
        Description: Optional[str] = None,
        SourceBuildInformation: Optional[Dict] = None,
        SourceBundle: Optional[Dict] = None,
        BuildConfiguration: Optional[Dict] = None,
        AutoCreateApplication: Optional[bool] = None,
        Process: Optional[bool] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_configuration_template(
        self,
        ApplicationName: str,
        TemplateName: str,
        SolutionStackName: Optional[str] = None,
        PlatformArn: Optional[str] = None,
        SourceConfiguration: Optional[Dict] = None,
        EnvironmentId: Optional[str] = None,
        Description: Optional[str] = None,
        OptionSettings: Optional[List] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_environment(
        self,
        ApplicationName: str,
        EnvironmentName: Optional[str] = None,
        GroupName: Optional[str] = None,
        Description: Optional[str] = None,
        CNAMEPrefix: Optional[str] = None,
        Tier: Optional[Dict] = None,
        Tags: Optional[List] = None,
        VersionLabel: Optional[str] = None,
        TemplateName: Optional[str] = None,
        SolutionStackName: Optional[str] = None,
        PlatformArn: Optional[str] = None,
        OptionSettings: Optional[List] = None,
        OptionsToRemove: Optional[List] = None,
    ) -> Dict:
        pass


    def create_platform_version(
        self,
        PlatformName: str,
        PlatformVersion: str,
        PlatformDefinitionBundle: Dict,
        EnvironmentName: Optional[str] = None,
        OptionSettings: Optional[List] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_storage_location(
        self,
    ) -> Dict:
        pass


    def delete_application(
        self,
        ApplicationName: str,
        TerminateEnvByForce: Optional[bool] = None,
    ):
        pass


    def delete_application_version(
        self,
        ApplicationName: str,
        VersionLabel: str,
        DeleteSourceBundle: Optional[bool] = None,
    ):
        pass


    def delete_configuration_template(
        self,
        ApplicationName: str,
        TemplateName: str,
    ):
        pass


    def delete_environment_configuration(
        self,
        ApplicationName: str,
        EnvironmentName: str,
    ):
        pass


    def delete_platform_version(
        self,
        PlatformArn: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_account_attributes(
        self,
    ) -> Dict:
        pass


    def describe_application_versions(
        self,
        ApplicationName: Optional[str] = None,
        VersionLabels: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_applications(
        self,
        ApplicationNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_configuration_options(
        self,
        ApplicationName: Optional[str] = None,
        TemplateName: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
        SolutionStackName: Optional[str] = None,
        PlatformArn: Optional[str] = None,
        Options: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_configuration_settings(
        self,
        ApplicationName: str,
        TemplateName: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_environment_health(
        self,
        EnvironmentName: Optional[str] = None,
        EnvironmentId: Optional[str] = None,
        AttributeNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_environment_managed_action_history(
        self,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_environment_managed_actions(
        self,
        EnvironmentName: Optional[str] = None,
        EnvironmentId: Optional[str] = None,
        Status: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_environment_resources(
        self,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_environments(
        self,
        ApplicationName: Optional[str] = None,
        VersionLabel: Optional[str] = None,
        EnvironmentIds: Optional[List] = None,
        EnvironmentNames: Optional[List] = None,
        IncludeDeleted: Optional[bool] = None,
        IncludedDeletedBackTo: Optional[datetime] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_events(
        self,
        ApplicationName: Optional[str] = None,
        VersionLabel: Optional[str] = None,
        TemplateName: Optional[str] = None,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
        PlatformArn: Optional[str] = None,
        RequestId: Optional[str] = None,
        Severity: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_instances_health(
        self,
        EnvironmentName: Optional[str] = None,
        EnvironmentId: Optional[str] = None,
        AttributeNames: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_platform_version(
        self,
        PlatformArn: Optional[str] = None,
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


    def list_available_solution_stacks(
        self,
    ) -> Dict:
        pass


    def list_platform_versions(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def rebuild_environment(
        self,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
    ):
        pass


    def request_environment_info(
        self,
        InfoType: str,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
    ):
        pass


    def restart_app_server(
        self,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
    ):
        pass


    def retrieve_environment_info(
        self,
        InfoType: str,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
    ) -> Dict:
        pass


    def swap_environment_cnames(
        self,
        SourceEnvironmentId: Optional[str] = None,
        SourceEnvironmentName: Optional[str] = None,
        DestinationEnvironmentId: Optional[str] = None,
        DestinationEnvironmentName: Optional[str] = None,
    ):
        pass


    def terminate_environment(
        self,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
        TerminateResources: Optional[bool] = None,
        ForceTerminate: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_application(
        self,
        ApplicationName: str,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_application_resource_lifecycle(
        self,
        ApplicationName: str,
        ResourceLifecycleConfig: Dict,
    ) -> Dict:
        pass


    def update_application_version(
        self,
        ApplicationName: str,
        VersionLabel: str,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_configuration_template(
        self,
        ApplicationName: str,
        TemplateName: str,
        Description: Optional[str] = None,
        OptionSettings: Optional[List] = None,
        OptionsToRemove: Optional[List] = None,
    ) -> Dict:
        pass


    def update_environment(
        self,
        ApplicationName: Optional[str] = None,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
        GroupName: Optional[str] = None,
        Description: Optional[str] = None,
        Tier: Optional[Dict] = None,
        VersionLabel: Optional[str] = None,
        TemplateName: Optional[str] = None,
        SolutionStackName: Optional[str] = None,
        PlatformArn: Optional[str] = None,
        OptionSettings: Optional[List] = None,
        OptionsToRemove: Optional[List] = None,
    ) -> Dict:
        pass


    def update_tags_for_resource(
        self,
        ResourceArn: str,
        TagsToAdd: Optional[List] = None,
        TagsToRemove: Optional[List] = None,
    ):
        pass


    def validate_configuration_settings(
        self,
        ApplicationName: str,
        OptionSettings: List,
        TemplateName: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
    ) -> Dict:
        pass

