from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_ip_groups(
        self,
        DirectoryId: str,
        GroupIds: List,
    ) -> Dict:
        pass


    def authorize_ip_rules(
        self,
        GroupId: str,
        UserRules: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def copy_workspace_image(
        self,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        Description: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_ip_group(
        self,
        GroupName: str,
        GroupDesc: Optional[str] = None,
        UserRules: Optional[List] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_tags(
        self,
        ResourceId: str,
        Tags: List,
    ) -> Dict:
        pass


    def create_workspaces(
        self,
        Workspaces: List,
    ) -> Dict:
        pass


    def delete_ip_group(
        self,
        GroupId: str,
    ) -> Dict:
        pass


    def delete_tags(
        self,
        ResourceId: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def delete_workspace_image(
        self,
        ImageId: str,
    ) -> Dict:
        pass


    def describe_account(
        self,
    ) -> Dict:
        pass


    def describe_account_modifications(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_client_properties(
        self,
        ResourceIds: List,
    ) -> Dict:
        pass


    def describe_ip_groups(
        self,
        GroupIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_tags(
        self,
        ResourceId: str,
    ) -> Dict:
        pass


    def describe_workspace_bundles(
        self,
        BundleIds: Optional[List] = None,
        Owner: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_workspace_directories(
        self,
        DirectoryIds: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_workspace_images(
        self,
        ImageIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_workspace_snapshots(
        self,
        WorkspaceId: str,
    ) -> Dict:
        pass


    def describe_workspaces(
        self,
        WorkspaceIds: Optional[List] = None,
        DirectoryId: Optional[str] = None,
        UserName: Optional[str] = None,
        BundleId: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_workspaces_connection_status(
        self,
        WorkspaceIds: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_ip_groups(
        self,
        DirectoryId: str,
        GroupIds: List,
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


    def import_workspace_image(
        self,
        Ec2ImageId: str,
        IngestionProcess: str,
        ImageName: str,
        ImageDescription: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def list_available_management_cidr_ranges(
        self,
        ManagementCidrRangeConstraint: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_account(
        self,
        DedicatedTenancySupport: Optional[str] = None,
        DedicatedTenancyManagementCidrRange: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_client_properties(
        self,
        ResourceId: str,
        ClientProperties: Dict,
    ) -> Dict:
        pass


    def modify_workspace_properties(
        self,
        WorkspaceId: str,
        WorkspaceProperties: Dict,
    ) -> Dict:
        pass


    def modify_workspace_state(
        self,
        WorkspaceId: str,
        WorkspaceState: str,
    ) -> Dict:
        pass


    def reboot_workspaces(
        self,
        RebootWorkspaceRequests: List,
    ) -> Dict:
        pass


    def rebuild_workspaces(
        self,
        RebuildWorkspaceRequests: List,
    ) -> Dict:
        pass


    def restore_workspace(
        self,
        WorkspaceId: str,
    ) -> Dict:
        pass


    def revoke_ip_rules(
        self,
        GroupId: str,
        UserRules: List,
    ) -> Dict:
        pass


    def start_workspaces(
        self,
        StartWorkspaceRequests: List,
    ) -> Dict:
        pass


    def stop_workspaces(
        self,
        StopWorkspaceRequests: List,
    ) -> Dict:
        pass


    def terminate_workspaces(
        self,
        TerminateWorkspaceRequests: List,
    ) -> Dict:
        pass


    def update_rules_of_ip_group(
        self,
        GroupId: str,
        UserRules: List,
    ) -> Dict:
        pass

