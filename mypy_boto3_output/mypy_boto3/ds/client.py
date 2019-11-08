from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def accept_shared_directory(self, SharedDirectoryId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_ip_routes(
        self,
        DirectoryId: str,
        IpRoutes: List[Any],
        UpdateSecurityGroupForDirectoryControllers: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_tags_to_resource(self, ResourceId: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_schema_extension(
        self, DirectoryId: str, SchemaExtensionId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def connect_directory(
        self,
        Name: str,
        Password: str,
        Size: str,
        ConnectSettings: Dict[str, Any],
        ShortName: str = None,
        Description: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_alias(self, DirectoryId: str, Alias: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_computer(
        self,
        DirectoryId: str,
        ComputerName: str,
        Password: str,
        OrganizationalUnitDistinguishedName: str = None,
        ComputerAttributes: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_directory(
        self,
        Name: str,
        Password: str,
        Size: str,
        ShortName: str = None,
        Description: str = None,
        VpcSettings: Dict[str, Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_log_subscription(
        self, DirectoryId: str, LogGroupName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_microsoft_ad(
        self,
        Name: str,
        Password: str,
        VpcSettings: Dict[str, Any],
        ShortName: str = None,
        Description: str = None,
        Edition: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_snapshot(self, DirectoryId: str, Name: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_trust(
        self,
        DirectoryId: str,
        RemoteDomainName: str,
        TrustPassword: str,
        TrustDirection: str,
        TrustType: str = None,
        ConditionalForwarderIpAddrs: List[Any] = None,
        SelectiveAuth: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_directory(self, DirectoryId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_log_subscription(self, DirectoryId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_snapshot(self, SnapshotId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_trust(
        self, TrustId: str, DeleteAssociatedConditionalForwarder: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_event_topic(
        self, DirectoryId: str, TopicName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_conditional_forwarders(
        self, DirectoryId: str, RemoteDomainNames: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_directories(
        self, DirectoryIds: List[Any] = None, NextToken: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_domain_controllers(
        self,
        DirectoryId: str,
        DomainControllerIds: List[Any] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_event_topics(
        self, DirectoryId: str = None, TopicNames: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_shared_directories(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[Any] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_snapshots(
        self,
        DirectoryId: str = None,
        SnapshotIds: List[Any] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_trusts(
        self,
        DirectoryId: str = None,
        TrustIds: List[Any] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_radius(self, DirectoryId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_sso(
        self, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_radius(
        self, DirectoryId: str, RadiusSettings: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_sso(
        self, DirectoryId: str, UserName: str = None, Password: str = None
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
    def get_directory_limits(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_snapshot_limits(self, DirectoryId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_ip_routes(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_log_subscriptions(
        self, DirectoryId: str = None, NextToken: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_schema_extensions(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, ResourceId: str, NextToken: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_event_topic(self, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reject_shared_directory(self, SharedDirectoryId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_ip_routes(self, DirectoryId: str, CidrIps: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags_from_resource(
        self, ResourceId: str, TagKeys: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reset_user_password(
        self, DirectoryId: str, UserName: str, NewPassword: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_from_snapshot(self, SnapshotId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def share_directory(
        self,
        DirectoryId: str,
        ShareTarget: Dict[str, Any],
        ShareMethod: str,
        ShareNotes: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_schema_extension(
        self,
        DirectoryId: str,
        CreateSnapshotBeforeSchemaExtension: bool,
        LdifContent: str,
        Description: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def unshare_directory(
        self, DirectoryId: str, UnshareTarget: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_number_of_domain_controllers(
        self, DirectoryId: str, DesiredNumber: int
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_radius(
        self, DirectoryId: str, RadiusSettings: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_trust(self, TrustId: str, SelectiveAuth: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def verify_trust(self, TrustId: str) -> Dict[str, Any]:
        pass
