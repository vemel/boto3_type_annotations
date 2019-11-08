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
    def abort_document_version_upload(
        self, DocumentId: str, VersionId: str, AuthenticationToken: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def activate_user(
        self, UserId: str, AuthenticationToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_resource_permissions(
        self,
        ResourceId: str,
        Principals: List[Any],
        AuthenticationToken: str = None,
        NotificationOptions: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_comment(
        self,
        DocumentId: str,
        VersionId: str,
        Text: str,
        AuthenticationToken: str = None,
        ParentId: str = None,
        ThreadId: str = None,
        Visibility: str = None,
        NotifyCollaborators: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_custom_metadata(
        self,
        ResourceId: str,
        CustomMetadata: Dict[str, Any],
        AuthenticationToken: str = None,
        VersionId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_folder(
        self, ParentFolderId: str, AuthenticationToken: str = None, Name: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_labels(
        self, ResourceId: str, Labels: List[Any], AuthenticationToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_notification_subscription(
        self, OrganizationId: str, Endpoint: str, Protocol: str, SubscriptionType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_user(
        self,
        Username: str,
        GivenName: str,
        Surname: str,
        Password: str,
        OrganizationId: str = None,
        EmailAddress: str = None,
        TimeZoneId: str = None,
        StorageRule: Dict[str, Any] = None,
        AuthenticationToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deactivate_user(self, UserId: str, AuthenticationToken: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_comment(
        self,
        DocumentId: str,
        VersionId: str,
        CommentId: str,
        AuthenticationToken: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_custom_metadata(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        VersionId: str = None,
        Keys: List[Any] = None,
        DeleteAll: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_document(self, DocumentId: str, AuthenticationToken: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_folder(self, FolderId: str, AuthenticationToken: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_folder_contents(
        self, FolderId: str, AuthenticationToken: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_labels(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        Labels: List[Any] = None,
        DeleteAll: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_notification_subscription(
        self, SubscriptionId: str, OrganizationId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_user(self, UserId: str, AuthenticationToken: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_activities(
        self,
        AuthenticationToken: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OrganizationId: str = None,
        ActivityTypes: str = None,
        ResourceId: str = None,
        UserId: str = None,
        IncludeIndirectActivities: bool = None,
        Limit: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_comments(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_document_versions(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Marker: str = None,
        Limit: int = None,
        Include: str = None,
        Fields: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_folder_contents(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Sort: str = None,
        Order: str = None,
        Limit: int = None,
        Marker: str = None,
        Type: str = None,
        Include: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_groups(
        self,
        SearchQuery: str,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        Marker: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_notification_subscriptions(
        self, OrganizationId: str, Marker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_resource_permissions(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        PrincipalId: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_root_folders(
        self, AuthenticationToken: str, Limit: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_users(
        self,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        UserIds: str = None,
        Query: str = None,
        Include: str = None,
        Order: str = None,
        Sort: str = None,
        Marker: str = None,
        Limit: int = None,
        Fields: str = None,
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
    def get_current_user(self, AuthenticationToken: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_document(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        IncludeCustomMetadata: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_document_path(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Fields: str = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_document_version(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        Fields: str = None,
        IncludeCustomMetadata: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_folder(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        IncludeCustomMetadata: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_folder_path(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Fields: str = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_resources(
        self,
        AuthenticationToken: str = None,
        UserId: str = None,
        CollectionType: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def initiate_document_version_upload(
        self,
        ParentFolderId: str,
        AuthenticationToken: str = None,
        Id: str = None,
        Name: str = None,
        ContentCreatedTimestamp: datetime = None,
        ContentModifiedTimestamp: datetime = None,
        ContentType: str = None,
        DocumentSizeInBytes: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_all_resource_permissions(
        self, ResourceId: str, AuthenticationToken: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def remove_resource_permission(
        self,
        ResourceId: str,
        PrincipalId: str,
        AuthenticationToken: str = None,
        PrincipalType: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_document(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Name: str = None,
        ParentFolderId: str = None,
        ResourceState: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_document_version(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        VersionStatus: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_folder(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Name: str = None,
        ParentFolderId: str = None,
        ResourceState: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_user(
        self,
        UserId: str,
        AuthenticationToken: str = None,
        GivenName: str = None,
        Surname: str = None,
        Type: str = None,
        StorageRule: Dict[str, Any] = None,
        TimeZoneId: str = None,
        Locale: str = None,
        GrantPoweruserPrivileges: str = None,
    ) -> Dict[str, Any]:
        pass
