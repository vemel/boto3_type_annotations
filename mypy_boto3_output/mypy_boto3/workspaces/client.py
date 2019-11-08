from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_ip_groups(
        self, DirectoryId: str, GroupIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def authorize_ip_rules(self, GroupId: str, UserRules: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def copy_workspace_image(
        self,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        Description: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_ip_group(
        self,
        GroupName: str,
        GroupDesc: str = None,
        UserRules: List[Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_tags(self, ResourceId: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_workspaces(self, Workspaces: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_ip_group(self, GroupId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_tags(self, ResourceId: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_workspace_image(self, ImageId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_account(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_account_modifications(self, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_client_properties(self, ResourceIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_ip_groups(
        self, GroupIds: List[Any] = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_tags(self, ResourceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_workspace_bundles(
        self, BundleIds: List[Any] = None, Owner: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_workspace_directories(
        self, DirectoryIds: List[Any] = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_workspace_images(
        self, ImageIds: List[Any] = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_workspace_snapshots(self, WorkspaceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_workspaces(
        self,
        WorkspaceIds: List[Any] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_workspaces_connection_status(
        self, WorkspaceIds: List[Any] = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_ip_groups(
        self, DirectoryId: str, GroupIds: List[Any]
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
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def import_workspace_image(
        self,
        Ec2ImageId: str,
        IngestionProcess: str,
        ImageName: str,
        ImageDescription: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_available_management_cidr_ranges(
        self,
        ManagementCidrRangeConstraint: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_account(
        self,
        DedicatedTenancySupport: str = None,
        DedicatedTenancyManagementCidrRange: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_client_properties(
        self, ResourceId: str, ClientProperties: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_workspace_properties(
        self, WorkspaceId: str, WorkspaceProperties: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_workspace_state(
        self, WorkspaceId: str, WorkspaceState: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot_workspaces(self, RebootWorkspaceRequests: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def rebuild_workspaces(self, RebuildWorkspaceRequests: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_workspace(self, WorkspaceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def revoke_ip_rules(self, GroupId: str, UserRules: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_workspaces(self, StartWorkspaceRequests: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_workspaces(self, StopWorkspaceRequests: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def terminate_workspaces(
        self, TerminateWorkspaceRequests: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_rules_of_ip_group(
        self, GroupId: str, UserRules: List[Any]
    ) -> Dict[str, Any]:
        pass
