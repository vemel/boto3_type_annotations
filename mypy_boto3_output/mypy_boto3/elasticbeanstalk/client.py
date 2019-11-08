from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def abort_environment_update(
        self, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def apply_environment_managed_action(
        self, ActionId: str, EnvironmentName: str = None, EnvironmentId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def check_dns_availability(self, CNAMEPrefix: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def compose_environments(
        self,
        ApplicationName: str = None,
        GroupName: str = None,
        VersionLabels: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_application(
        self,
        ApplicationName: str,
        Description: str = None,
        ResourceLifecycleConfig: Dict[str, Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_application_version(
        self,
        ApplicationName: str,
        VersionLabel: str,
        Description: str = None,
        SourceBuildInformation: Dict[str, Any] = None,
        SourceBundle: Dict[str, Any] = None,
        BuildConfiguration: Dict[str, Any] = None,
        AutoCreateApplication: bool = None,
        Process: bool = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_configuration_template(
        self,
        ApplicationName: str,
        TemplateName: str,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        SourceConfiguration: Dict[str, Any] = None,
        EnvironmentId: str = None,
        Description: str = None,
        OptionSettings: List[Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_environment(
        self,
        ApplicationName: str,
        EnvironmentName: str = None,
        GroupName: str = None,
        Description: str = None,
        CNAMEPrefix: str = None,
        Tier: Dict[str, Any] = None,
        Tags: List[Any] = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        OptionSettings: List[Any] = None,
        OptionsToRemove: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_platform_version(
        self,
        PlatformName: str,
        PlatformVersion: str,
        PlatformDefinitionBundle: Dict[str, Any],
        EnvironmentName: str = None,
        OptionSettings: List[Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_storage_location(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_application(
        self, ApplicationName: str, TerminateEnvByForce: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_application_version(
        self, ApplicationName: str, VersionLabel: str, DeleteSourceBundle: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_configuration_template(
        self, ApplicationName: str, TemplateName: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_environment_configuration(
        self, ApplicationName: str, EnvironmentName: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_platform_version(self, PlatformArn: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_account_attributes(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_application_versions(
        self,
        ApplicationName: str = None,
        VersionLabels: List[Any] = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_applications(
        self, ApplicationNames: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_configuration_options(
        self,
        ApplicationName: str = None,
        TemplateName: str = None,
        EnvironmentName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        Options: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_configuration_settings(
        self,
        ApplicationName: str,
        TemplateName: str = None,
        EnvironmentName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_environment_health(
        self,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        AttributeNames: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_environment_managed_action_history(
        self,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        NextToken: str = None,
        MaxItems: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_environment_managed_actions(
        self, EnvironmentName: str = None, EnvironmentId: str = None, Status: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_environment_resources(
        self, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_environments(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[Any] = None,
        EnvironmentNames: List[Any] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_events(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PlatformArn: str = None,
        RequestId: str = None,
        Severity: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_instances_health(
        self,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        AttributeNames: List[Any] = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_platform_version(self, PlatformArn: str = None) -> Dict[str, Any]:
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
    def list_available_solution_stacks(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_platform_versions(
        self, Filters: List[Any] = None, MaxRecords: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def rebuild_environment(
        self, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def request_environment_info(
        self, InfoType: str, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def restart_app_server(
        self, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def retrieve_environment_info(
        self, InfoType: str, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def swap_environment_cnames(
        self,
        SourceEnvironmentId: str = None,
        SourceEnvironmentName: str = None,
        DestinationEnvironmentId: str = None,
        DestinationEnvironmentName: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def terminate_environment(
        self,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        TerminateResources: bool = None,
        ForceTerminate: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_application(
        self, ApplicationName: str, Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_application_resource_lifecycle(
        self, ApplicationName: str, ResourceLifecycleConfig: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_application_version(
        self, ApplicationName: str, VersionLabel: str, Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_configuration_template(
        self,
        ApplicationName: str,
        TemplateName: str,
        Description: str = None,
        OptionSettings: List[Any] = None,
        OptionsToRemove: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_environment(
        self,
        ApplicationName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        GroupName: str = None,
        Description: str = None,
        Tier: Dict[str, Any] = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        OptionSettings: List[Any] = None,
        OptionsToRemove: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_tags_for_resource(
        self,
        ResourceArn: str,
        TagsToAdd: List[Any] = None,
        TagsToRemove: List[Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def validate_configuration_settings(
        self,
        ApplicationName: str,
        OptionSettings: List[Any],
        TemplateName: str = None,
        EnvironmentName: str = None,
    ) -> Dict[str, Any]:
        pass
