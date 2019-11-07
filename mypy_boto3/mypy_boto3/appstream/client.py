from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_fleet(
        self,
        FleetName: str,
        StackName: str,
    ) -> Dict:
        pass


    def batch_associate_user_stack(
        self,
        UserStackAssociations: List,
    ) -> Dict:
        pass


    def batch_disassociate_user_stack(
        self,
        UserStackAssociations: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def copy_image(
        self,
        SourceImageName: str,
        DestinationImageName: str,
        DestinationRegion: str,
        DestinationImageDescription: Optional[str] = None,
    ) -> Dict:
        pass


    def create_directory_config(
        self,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List,
        ServiceAccountCredentials: Dict,
    ) -> Dict:
        pass


    def create_fleet(
        self,
        Name: str,
        InstanceType: str,
        ComputeCapacity: Dict,
        ImageName: Optional[str] = None,
        ImageArn: Optional[str] = None,
        FleetType: Optional[str] = None,
        VpcConfig: Optional[Dict] = None,
        MaxUserDurationInSeconds: Optional[int] = None,
        DisconnectTimeoutInSeconds: Optional[int] = None,
        Description: Optional[str] = None,
        DisplayName: Optional[str] = None,
        EnableDefaultInternetAccess: Optional[bool] = None,
        DomainJoinInfo: Optional[Dict] = None,
        Tags: Optional[Dict] = None,
        IdleDisconnectTimeoutInSeconds: Optional[int] = None,
        IamRoleArn: Optional[str] = None,
    ) -> Dict:
        pass


    def create_image_builder(
        self,
        Name: str,
        InstanceType: str,
        ImageName: Optional[str] = None,
        ImageArn: Optional[str] = None,
        Description: Optional[str] = None,
        DisplayName: Optional[str] = None,
        VpcConfig: Optional[Dict] = None,
        IamRoleArn: Optional[str] = None,
        EnableDefaultInternetAccess: Optional[bool] = None,
        DomainJoinInfo: Optional[Dict] = None,
        AppstreamAgentVersion: Optional[str] = None,
        Tags: Optional[Dict] = None,
        AccessEndpoints: Optional[List] = None,
    ) -> Dict:
        pass


    def create_image_builder_streaming_url(
        self,
        Name: str,
        Validity: Optional[int] = None,
    ) -> Dict:
        pass


    def create_stack(
        self,
        Name: str,
        Description: Optional[str] = None,
        DisplayName: Optional[str] = None,
        StorageConnectors: Optional[List] = None,
        RedirectURL: Optional[str] = None,
        FeedbackURL: Optional[str] = None,
        UserSettings: Optional[List] = None,
        ApplicationSettings: Optional[Dict] = None,
        Tags: Optional[Dict] = None,
        AccessEndpoints: Optional[List] = None,
        EmbedHostDomains: Optional[List] = None,
    ) -> Dict:
        pass


    def create_streaming_url(
        self,
        StackName: str,
        FleetName: str,
        UserId: str,
        ApplicationId: Optional[str] = None,
        Validity: Optional[int] = None,
        SessionContext: Optional[str] = None,
    ) -> Dict:
        pass


    def create_usage_report_subscription(
        self,
    ) -> Dict:
        pass


    def create_user(
        self,
        UserName: str,
        AuthenticationType: str,
        MessageAction: Optional[str] = None,
        FirstName: Optional[str] = None,
        LastName: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_directory_config(
        self,
        DirectoryName: str,
    ) -> Dict:
        pass


    def delete_fleet(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_image(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_image_builder(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_image_permissions(
        self,
        Name: str,
        SharedAccountId: str,
    ) -> Dict:
        pass


    def delete_stack(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_usage_report_subscription(
        self,
    ) -> Dict:
        pass


    def delete_user(
        self,
        UserName: str,
        AuthenticationType: str,
    ) -> Dict:
        pass


    def describe_directory_configs(
        self,
        DirectoryNames: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_fleets(
        self,
        Names: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_image_builders(
        self,
        Names: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_image_permissions(
        self,
        Name: str,
        MaxResults: Optional[int] = None,
        SharedAwsAccountIds: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_images(
        self,
        Names: Optional[List] = None,
        Arns: Optional[List] = None,
        Type: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_sessions(
        self,
        StackName: str,
        FleetName: str,
        UserId: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
        AuthenticationType: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_stacks(
        self,
        Names: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_usage_report_subscriptions(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_user_stack_associations(
        self,
        StackName: Optional[str] = None,
        UserName: Optional[str] = None,
        AuthenticationType: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_users(
        self,
        AuthenticationType: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def disable_user(
        self,
        UserName: str,
        AuthenticationType: str,
    ) -> Dict:
        pass


    def disassociate_fleet(
        self,
        FleetName: str,
        StackName: str,
    ) -> Dict:
        pass


    def enable_user(
        self,
        UserName: str,
        AuthenticationType: str,
    ) -> Dict:
        pass


    def expire_session(
        self,
        SessionId: str,
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


    def list_associated_fleets(
        self,
        StackName: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_associated_stacks(
        self,
        FleetName: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def start_fleet(
        self,
        Name: str,
    ) -> Dict:
        pass


    def start_image_builder(
        self,
        Name: str,
        AppstreamAgentVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_fleet(
        self,
        Name: str,
    ) -> Dict:
        pass


    def stop_image_builder(
        self,
        Name: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_directory_config(
        self,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: Optional[List] = None,
        ServiceAccountCredentials: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_fleet(
        self,
        ImageName: Optional[str] = None,
        ImageArn: Optional[str] = None,
        Name: Optional[str] = None,
        InstanceType: Optional[str] = None,
        ComputeCapacity: Optional[Dict] = None,
        VpcConfig: Optional[Dict] = None,
        MaxUserDurationInSeconds: Optional[int] = None,
        DisconnectTimeoutInSeconds: Optional[int] = None,
        DeleteVpcConfig: Optional[bool] = None,
        Description: Optional[str] = None,
        DisplayName: Optional[str] = None,
        EnableDefaultInternetAccess: Optional[bool] = None,
        DomainJoinInfo: Optional[Dict] = None,
        IdleDisconnectTimeoutInSeconds: Optional[int] = None,
        AttributesToDelete: Optional[List] = None,
        IamRoleArn: Optional[str] = None,
    ) -> Dict:
        pass


    def update_image_permissions(
        self,
        Name: str,
        SharedAccountId: str,
        ImagePermissions: Dict,
    ) -> Dict:
        pass


    def update_stack(
        self,
        Name: str,
        DisplayName: Optional[str] = None,
        Description: Optional[str] = None,
        StorageConnectors: Optional[List] = None,
        DeleteStorageConnectors: Optional[bool] = None,
        RedirectURL: Optional[str] = None,
        FeedbackURL: Optional[str] = None,
        AttributesToDelete: Optional[List] = None,
        UserSettings: Optional[List] = None,
        ApplicationSettings: Optional[Dict] = None,
        AccessEndpoints: Optional[List] = None,
        EmbedHostDomains: Optional[List] = None,
    ) -> Dict:
        pass

