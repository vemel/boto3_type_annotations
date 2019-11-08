from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_fleet(self, FleetName: str, StackName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_associate_user_stack(
        self, UserStackAssociations: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_disassociate_user_stack(
        self, UserStackAssociations: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def copy_image(
        self,
        SourceImageName: str,
        DestinationImageName: str,
        DestinationRegion: str,
        DestinationImageDescription: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_directory_config(
        self,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[Any],
        ServiceAccountCredentials: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_fleet(
        self,
        Name: str,
        InstanceType: str,
        ComputeCapacity: Dict[str, Any],
        ImageName: str = None,
        ImageArn: str = None,
        FleetType: str = None,
        VpcConfig: Dict[str, Any] = None,
        MaxUserDurationInSeconds: int = None,
        DisconnectTimeoutInSeconds: int = None,
        Description: str = None,
        DisplayName: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: Dict[str, Any] = None,
        Tags: Dict[str, Any] = None,
        IdleDisconnectTimeoutInSeconds: int = None,
        IamRoleArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_image_builder(
        self,
        Name: str,
        InstanceType: str,
        ImageName: str = None,
        ImageArn: str = None,
        Description: str = None,
        DisplayName: str = None,
        VpcConfig: Dict[str, Any] = None,
        IamRoleArn: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: Dict[str, Any] = None,
        AppstreamAgentVersion: str = None,
        Tags: Dict[str, Any] = None,
        AccessEndpoints: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_image_builder_streaming_url(
        self, Name: str, Validity: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_stack(
        self,
        Name: str,
        Description: str = None,
        DisplayName: str = None,
        StorageConnectors: List[Any] = None,
        RedirectURL: str = None,
        FeedbackURL: str = None,
        UserSettings: List[Any] = None,
        ApplicationSettings: Dict[str, Any] = None,
        Tags: Dict[str, Any] = None,
        AccessEndpoints: List[Any] = None,
        EmbedHostDomains: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_streaming_url(
        self,
        StackName: str,
        FleetName: str,
        UserId: str,
        ApplicationId: str = None,
        Validity: int = None,
        SessionContext: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_usage_report_subscription(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_user(
        self,
        UserName: str,
        AuthenticationType: str,
        MessageAction: str = None,
        FirstName: str = None,
        LastName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_directory_config(self, DirectoryName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_fleet(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_image(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_image_builder(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_image_permissions(
        self, Name: str, SharedAccountId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_stack(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_usage_report_subscription(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_user(self, UserName: str, AuthenticationType: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_directory_configs(
        self,
        DirectoryNames: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_fleets(
        self, Names: List[Any] = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_image_builders(
        self, Names: List[Any] = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_image_permissions(
        self,
        Name: str,
        MaxResults: int = None,
        SharedAwsAccountIds: List[Any] = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_images(
        self,
        Names: List[Any] = None,
        Arns: List[Any] = None,
        Type: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_sessions(
        self,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        NextToken: str = None,
        Limit: int = None,
        AuthenticationType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stacks(
        self, Names: List[Any] = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_usage_report_subscriptions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_user_stack_associations(
        self,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_users(
        self, AuthenticationType: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_user(self, UserName: str, AuthenticationType: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_fleet(self, FleetName: str, StackName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_user(self, UserName: str, AuthenticationType: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def expire_session(self, SessionId: str) -> Dict[str, Any]:
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
    def list_associated_fleets(
        self, StackName: str, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_associated_stacks(
        self, FleetName: str, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_fleet(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_image_builder(
        self, Name: str, AppstreamAgentVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_fleet(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_image_builder(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_directory_config(
        self,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[Any] = None,
        ServiceAccountCredentials: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_fleet(
        self,
        ImageName: str = None,
        ImageArn: str = None,
        Name: str = None,
        InstanceType: str = None,
        ComputeCapacity: Dict[str, Any] = None,
        VpcConfig: Dict[str, Any] = None,
        MaxUserDurationInSeconds: int = None,
        DisconnectTimeoutInSeconds: int = None,
        DeleteVpcConfig: bool = None,
        Description: str = None,
        DisplayName: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: Dict[str, Any] = None,
        IdleDisconnectTimeoutInSeconds: int = None,
        AttributesToDelete: List[Any] = None,
        IamRoleArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_image_permissions(
        self, Name: str, SharedAccountId: str, ImagePermissions: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_stack(
        self,
        Name: str,
        DisplayName: str = None,
        Description: str = None,
        StorageConnectors: List[Any] = None,
        DeleteStorageConnectors: bool = None,
        RedirectURL: str = None,
        FeedbackURL: str = None,
        AttributesToDelete: List[Any] = None,
        UserSettings: List[Any] = None,
        ApplicationSettings: Dict[str, Any] = None,
        AccessEndpoints: List[Any] = None,
        EmbedHostDomains: List[Any] = None,
    ) -> Dict[str, Any]:
        pass
