from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_shared_directory(
        self,
        SharedDirectoryId: str,
    ) -> Dict:
        pass


    def add_ip_routes(
        self,
        DirectoryId: str,
        IpRoutes: List,
        UpdateSecurityGroupForDirectoryControllers: Optional[bool] = None,
    ) -> Dict:
        pass


    def add_tags_to_resource(
        self,
        ResourceId: str,
        Tags: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_schema_extension(
        self,
        DirectoryId: str,
        SchemaExtensionId: str,
    ) -> Dict:
        pass


    def connect_directory(
        self,
        Name: str,
        Password: str,
        Size: str,
        ConnectSettings: Dict,
        ShortName: Optional[str] = None,
        Description: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_alias(
        self,
        DirectoryId: str,
        Alias: str,
    ) -> Dict:
        pass


    def create_computer(
        self,
        DirectoryId: str,
        ComputerName: str,
        Password: str,
        OrganizationalUnitDistinguishedName: Optional[str] = None,
        ComputerAttributes: Optional[List] = None,
    ) -> Dict:
        pass


    def create_conditional_forwarder(
        self,
        DirectoryId: str,
        RemoteDomainName: str,
        DnsIpAddrs: List,
    ) -> Dict:
        pass


    def create_directory(
        self,
        Name: str,
        Password: str,
        Size: str,
        ShortName: Optional[str] = None,
        Description: Optional[str] = None,
        VpcSettings: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_log_subscription(
        self,
        DirectoryId: str,
        LogGroupName: str,
    ) -> Dict:
        pass


    def create_microsoft_ad(
        self,
        Name: str,
        Password: str,
        VpcSettings: Dict,
        ShortName: Optional[str] = None,
        Description: Optional[str] = None,
        Edition: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_snapshot(
        self,
        DirectoryId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def create_trust(
        self,
        DirectoryId: str,
        RemoteDomainName: str,
        TrustPassword: str,
        TrustDirection: str,
        TrustType: Optional[str] = None,
        ConditionalForwarderIpAddrs: Optional[List] = None,
        SelectiveAuth: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_conditional_forwarder(
        self,
        DirectoryId: str,
        RemoteDomainName: str,
    ) -> Dict:
        pass


    def delete_directory(
        self,
        DirectoryId: str,
    ) -> Dict:
        pass


    def delete_log_subscription(
        self,
        DirectoryId: str,
    ) -> Dict:
        pass


    def delete_snapshot(
        self,
        SnapshotId: str,
    ) -> Dict:
        pass


    def delete_trust(
        self,
        TrustId: str,
        DeleteAssociatedConditionalForwarder: Optional[bool] = None,
    ) -> Dict:
        pass


    def deregister_event_topic(
        self,
        DirectoryId: str,
        TopicName: str,
    ) -> Dict:
        pass


    def describe_conditional_forwarders(
        self,
        DirectoryId: str,
        RemoteDomainNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_directories(
        self,
        DirectoryIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_domain_controllers(
        self,
        DirectoryId: str,
        DomainControllerIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_event_topics(
        self,
        DirectoryId: Optional[str] = None,
        TopicNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_shared_directories(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_snapshots(
        self,
        DirectoryId: Optional[str] = None,
        SnapshotIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_trusts(
        self,
        DirectoryId: Optional[str] = None,
        TrustIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def disable_radius(
        self,
        DirectoryId: str,
    ) -> Dict:
        pass


    def disable_sso(
        self,
        DirectoryId: str,
        UserName: Optional[str] = None,
        Password: Optional[str] = None,
    ) -> Dict:
        pass


    def enable_radius(
        self,
        DirectoryId: str,
        RadiusSettings: Dict,
    ) -> Dict:
        pass


    def enable_sso(
        self,
        DirectoryId: str,
        UserName: Optional[str] = None,
        Password: Optional[str] = None,
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


    def get_directory_limits(
        self,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_snapshot_limits(
        self,
        DirectoryId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_ip_routes(
        self,
        DirectoryId: str,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_log_subscriptions(
        self,
        DirectoryId: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_schema_extensions(
        self,
        DirectoryId: str,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceId: str,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def register_event_topic(
        self,
        DirectoryId: str,
        TopicName: str,
    ) -> Dict:
        pass


    def reject_shared_directory(
        self,
        SharedDirectoryId: str,
    ) -> Dict:
        pass


    def remove_ip_routes(
        self,
        DirectoryId: str,
        CidrIps: List,
    ) -> Dict:
        pass


    def remove_tags_from_resource(
        self,
        ResourceId: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def reset_user_password(
        self,
        DirectoryId: str,
        UserName: str,
        NewPassword: str,
    ) -> Dict:
        pass


    def restore_from_snapshot(
        self,
        SnapshotId: str,
    ) -> Dict:
        pass


    def share_directory(
        self,
        DirectoryId: str,
        ShareTarget: Dict,
        ShareMethod: str,
        ShareNotes: Optional[str] = None,
    ) -> Dict:
        pass


    def start_schema_extension(
        self,
        DirectoryId: str,
        CreateSnapshotBeforeSchemaExtension: bool,
        LdifContent: str,
        Description: str,
    ) -> Dict:
        pass


    def unshare_directory(
        self,
        DirectoryId: str,
        UnshareTarget: Dict,
    ) -> Dict:
        pass


    def update_conditional_forwarder(
        self,
        DirectoryId: str,
        RemoteDomainName: str,
        DnsIpAddrs: List,
    ) -> Dict:
        pass


    def update_number_of_domain_controllers(
        self,
        DirectoryId: str,
        DesiredNumber: int,
    ) -> Dict:
        pass


    def update_radius(
        self,
        DirectoryId: str,
        RadiusSettings: Dict,
    ) -> Dict:
        pass


    def update_trust(
        self,
        TrustId: str,
        SelectiveAuth: Optional[str] = None,
    ) -> Dict:
        pass


    def verify_trust(
        self,
        TrustId: str,
    ) -> Dict:
        pass

