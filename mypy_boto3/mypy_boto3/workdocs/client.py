from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def abort_document_version_upload(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: Optional[str] = None,
    ):
        pass


    def activate_user(
        self,
        UserId: str,
        AuthenticationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def add_resource_permissions(
        self,
        ResourceId: str,
        Principals: List,
        AuthenticationToken: Optional[str] = None,
        NotificationOptions: Optional[Dict] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_comment(
        self,
        DocumentId: str,
        VersionId: str,
        Text: str,
        AuthenticationToken: Optional[str] = None,
        ParentId: Optional[str] = None,
        ThreadId: Optional[str] = None,
        Visibility: Optional[str] = None,
        NotifyCollaborators: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_custom_metadata(
        self,
        ResourceId: str,
        CustomMetadata: Dict,
        AuthenticationToken: Optional[str] = None,
        VersionId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_folder(
        self,
        ParentFolderId: str,
        AuthenticationToken: Optional[str] = None,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def create_labels(
        self,
        ResourceId: str,
        Labels: List,
        AuthenticationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_notification_subscription(
        self,
        OrganizationId: str,
        Endpoint: str,
        Protocol: str,
        SubscriptionType: str,
    ) -> Dict:
        pass


    def create_user(
        self,
        Username: str,
        GivenName: str,
        Surname: str,
        Password: str,
        OrganizationId: Optional[str] = None,
        EmailAddress: Optional[str] = None,
        TimeZoneId: Optional[str] = None,
        StorageRule: Optional[Dict] = None,
        AuthenticationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def deactivate_user(
        self,
        UserId: str,
        AuthenticationToken: Optional[str] = None,
    ):
        pass


    def delete_comment(
        self,
        DocumentId: str,
        VersionId: str,
        CommentId: str,
        AuthenticationToken: Optional[str] = None,
    ):
        pass


    def delete_custom_metadata(
        self,
        ResourceId: str,
        AuthenticationToken: Optional[str] = None,
        VersionId: Optional[str] = None,
        Keys: Optional[List] = None,
        DeleteAll: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_document(
        self,
        DocumentId: str,
        AuthenticationToken: Optional[str] = None,
    ):
        pass


    def delete_folder(
        self,
        FolderId: str,
        AuthenticationToken: Optional[str] = None,
    ):
        pass


    def delete_folder_contents(
        self,
        FolderId: str,
        AuthenticationToken: Optional[str] = None,
    ):
        pass


    def delete_labels(
        self,
        ResourceId: str,
        AuthenticationToken: Optional[str] = None,
        Labels: Optional[List] = None,
        DeleteAll: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_notification_subscription(
        self,
        SubscriptionId: str,
        OrganizationId: str,
    ):
        pass


    def delete_user(
        self,
        UserId: str,
        AuthenticationToken: Optional[str] = None,
    ):
        pass


    def describe_activities(
        self,
        AuthenticationToken: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        OrganizationId: Optional[str] = None,
        ActivityTypes: Optional[str] = None,
        ResourceId: Optional[str] = None,
        UserId: Optional[str] = None,
        IncludeIndirectActivities: Optional[bool] = None,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_comments(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: Optional[str] = None,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_document_versions(
        self,
        DocumentId: str,
        AuthenticationToken: Optional[str] = None,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
        Include: Optional[str] = None,
        Fields: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_folder_contents(
        self,
        FolderId: str,
        AuthenticationToken: Optional[str] = None,
        Sort: Optional[str] = None,
        Order: Optional[str] = None,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
        Type: Optional[str] = None,
        Include: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_groups(
        self,
        SearchQuery: str,
        AuthenticationToken: Optional[str] = None,
        OrganizationId: Optional[str] = None,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_notification_subscriptions(
        self,
        OrganizationId: str,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_resource_permissions(
        self,
        ResourceId: str,
        AuthenticationToken: Optional[str] = None,
        PrincipalId: Optional[str] = None,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_root_folders(
        self,
        AuthenticationToken: str,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_users(
        self,
        AuthenticationToken: Optional[str] = None,
        OrganizationId: Optional[str] = None,
        UserIds: Optional[str] = None,
        Query: Optional[str] = None,
        Include: Optional[str] = None,
        Order: Optional[str] = None,
        Sort: Optional[str] = None,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
        Fields: Optional[str] = None,
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


    def get_current_user(
        self,
        AuthenticationToken: str,
    ) -> Dict:
        pass


    def get_document(
        self,
        DocumentId: str,
        AuthenticationToken: Optional[str] = None,
        IncludeCustomMetadata: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_document_path(
        self,
        DocumentId: str,
        AuthenticationToken: Optional[str] = None,
        Limit: Optional[int] = None,
        Fields: Optional[str] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def get_document_version(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: Optional[str] = None,
        Fields: Optional[str] = None,
        IncludeCustomMetadata: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_folder(
        self,
        FolderId: str,
        AuthenticationToken: Optional[str] = None,
        IncludeCustomMetadata: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_folder_path(
        self,
        FolderId: str,
        AuthenticationToken: Optional[str] = None,
        Limit: Optional[int] = None,
        Fields: Optional[str] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_resources(
        self,
        AuthenticationToken: Optional[str] = None,
        UserId: Optional[str] = None,
        CollectionType: Optional[str] = None,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def initiate_document_version_upload(
        self,
        ParentFolderId: str,
        AuthenticationToken: Optional[str] = None,
        Id: Optional[str] = None,
        Name: Optional[str] = None,
        ContentCreatedTimestamp: Optional[datetime] = None,
        ContentModifiedTimestamp: Optional[datetime] = None,
        ContentType: Optional[str] = None,
        DocumentSizeInBytes: Optional[int] = None,
    ) -> Dict:
        pass


    def remove_all_resource_permissions(
        self,
        ResourceId: str,
        AuthenticationToken: Optional[str] = None,
    ):
        pass


    def remove_resource_permission(
        self,
        ResourceId: str,
        PrincipalId: str,
        AuthenticationToken: Optional[str] = None,
        PrincipalType: Optional[str] = None,
    ):
        pass


    def update_document(
        self,
        DocumentId: str,
        AuthenticationToken: Optional[str] = None,
        Name: Optional[str] = None,
        ParentFolderId: Optional[str] = None,
        ResourceState: Optional[str] = None,
    ):
        pass


    def update_document_version(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: Optional[str] = None,
        VersionStatus: Optional[str] = None,
    ):
        pass


    def update_folder(
        self,
        FolderId: str,
        AuthenticationToken: Optional[str] = None,
        Name: Optional[str] = None,
        ParentFolderId: Optional[str] = None,
        ResourceState: Optional[str] = None,
    ):
        pass


    def update_user(
        self,
        UserId: str,
        AuthenticationToken: Optional[str] = None,
        GivenName: Optional[str] = None,
        Surname: Optional[str] = None,
        Type: Optional[str] = None,
        StorageRule: Optional[Dict] = None,
        TimeZoneId: Optional[str] = None,
        Locale: Optional[str] = None,
        GrantPoweruserPrivileges: Optional[str] = None,
    ) -> Dict:
        pass

