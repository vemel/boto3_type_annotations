"Main interface for workdocs type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientActivateUserResponseUserStorageStorageRuleTypeDef",
    "ClientActivateUserResponseUserStorageTypeDef",
    "ClientActivateUserResponseUserTypeDef",
    "ClientActivateUserResponseTypeDef",
    "ClientAddResourcePermissionsNotificationOptionsTypeDef",
    "ClientAddResourcePermissionsPrincipalsTypeDef",
    "ClientAddResourcePermissionsResponseShareResultsTypeDef",
    "ClientAddResourcePermissionsResponseTypeDef",
    "ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef",
    "ClientCreateCommentResponseCommentContributorStorageTypeDef",
    "ClientCreateCommentResponseCommentContributorTypeDef",
    "ClientCreateCommentResponseCommentTypeDef",
    "ClientCreateCommentResponseTypeDef",
    "ClientCreateFolderResponseMetadataTypeDef",
    "ClientCreateFolderResponseTypeDef",
    "ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef",
    "ClientCreateNotificationSubscriptionResponseTypeDef",
    "ClientCreateUserResponseUserStorageStorageRuleTypeDef",
    "ClientCreateUserResponseUserStorageTypeDef",
    "ClientCreateUserResponseUserTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserStorageRuleTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesTypeDef",
    "ClientDescribeActivitiesResponseTypeDef",
    "ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef",
    "ClientDescribeCommentsResponseCommentsContributorStorageTypeDef",
    "ClientDescribeCommentsResponseCommentsContributorTypeDef",
    "ClientDescribeCommentsResponseCommentsTypeDef",
    "ClientDescribeCommentsResponseTypeDef",
    "ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef",
    "ClientDescribeDocumentVersionsResponseTypeDef",
    "ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef",
    "ClientDescribeFolderContentsResponseDocumentsTypeDef",
    "ClientDescribeFolderContentsResponseFoldersTypeDef",
    "ClientDescribeFolderContentsResponseTypeDef",
    "ClientDescribeGroupsResponseGroupsTypeDef",
    "ClientDescribeGroupsResponseTypeDef",
    "ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef",
    "ClientDescribeNotificationSubscriptionsResponseTypeDef",
    "ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef",
    "ClientDescribeResourcePermissionsResponsePrincipalsTypeDef",
    "ClientDescribeResourcePermissionsResponseTypeDef",
    "ClientDescribeRootFoldersResponseFoldersTypeDef",
    "ClientDescribeRootFoldersResponseTypeDef",
    "ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef",
    "ClientDescribeUsersResponseUsersStorageTypeDef",
    "ClientDescribeUsersResponseUsersTypeDef",
    "ClientDescribeUsersResponseTypeDef",
    "ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef",
    "ClientGetCurrentUserResponseUserStorageTypeDef",
    "ClientGetCurrentUserResponseUserTypeDef",
    "ClientGetCurrentUserResponseTypeDef",
    "ClientGetDocumentPathResponsePathComponentsTypeDef",
    "ClientGetDocumentPathResponsePathTypeDef",
    "ClientGetDocumentPathResponseTypeDef",
    "ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef",
    "ClientGetDocumentResponseMetadataTypeDef",
    "ClientGetDocumentResponseTypeDef",
    "ClientGetDocumentVersionResponseMetadataTypeDef",
    "ClientGetDocumentVersionResponseTypeDef",
    "ClientGetFolderPathResponsePathComponentsTypeDef",
    "ClientGetFolderPathResponsePathTypeDef",
    "ClientGetFolderPathResponseTypeDef",
    "ClientGetFolderResponseMetadataTypeDef",
    "ClientGetFolderResponseTypeDef",
    "ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef",
    "ClientGetResourcesResponseDocumentsTypeDef",
    "ClientGetResourcesResponseFoldersTypeDef",
    "ClientGetResourcesResponseTypeDef",
    "ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef",
    "ClientInitiateDocumentVersionUploadResponseMetadataTypeDef",
    "ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef",
    "ClientInitiateDocumentVersionUploadResponseTypeDef",
    "ClientUpdateUserResponseUserStorageStorageRuleTypeDef",
    "ClientUpdateUserResponseUserStorageTypeDef",
    "ClientUpdateUserResponseUserTypeDef",
    "ClientUpdateUserResponseTypeDef",
    "ClientUpdateUserStorageRuleTypeDef",
    "DescribeActivitiesPaginatePaginationConfigTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesTypeDef",
    "DescribeActivitiesPaginateResponseTypeDef",
    "DescribeCommentsPaginatePaginationConfigTypeDef",
    "DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef",
    "DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef",
    "DescribeCommentsPaginateResponseCommentsContributorTypeDef",
    "DescribeCommentsPaginateResponseCommentsTypeDef",
    "DescribeCommentsPaginateResponseTypeDef",
    "DescribeDocumentVersionsPaginatePaginationConfigTypeDef",
    "DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef",
    "DescribeDocumentVersionsPaginateResponseTypeDef",
    "DescribeFolderContentsPaginatePaginationConfigTypeDef",
    "DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef",
    "DescribeFolderContentsPaginateResponseDocumentsTypeDef",
    "DescribeFolderContentsPaginateResponseFoldersTypeDef",
    "DescribeFolderContentsPaginateResponseTypeDef",
    "DescribeGroupsPaginatePaginationConfigTypeDef",
    "DescribeGroupsPaginateResponseGroupsTypeDef",
    "DescribeGroupsPaginateResponseTypeDef",
    "DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef",
    "DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef",
    "DescribeNotificationSubscriptionsPaginateResponseTypeDef",
    "DescribeResourcePermissionsPaginatePaginationConfigTypeDef",
    "DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef",
    "DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef",
    "DescribeResourcePermissionsPaginateResponseTypeDef",
    "DescribeRootFoldersPaginatePaginationConfigTypeDef",
    "DescribeRootFoldersPaginateResponseFoldersTypeDef",
    "DescribeRootFoldersPaginateResponseTypeDef",
    "DescribeUsersPaginatePaginationConfigTypeDef",
    "DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef",
    "DescribeUsersPaginateResponseUsersStorageTypeDef",
    "DescribeUsersPaginateResponseUsersTypeDef",
    "DescribeUsersPaginateResponseTypeDef",
)


_ClientActivateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "_ClientActivateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class ClientActivateUserResponseUserStorageStorageRuleTypeDef(
    _ClientActivateUserResponseUserStorageStorageRuleTypeDef
):
    """
    Type definition for `ClientActivateUserResponseUserStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_ClientActivateUserResponseUserStorageTypeDef = TypedDict(
    "_ClientActivateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientActivateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientActivateUserResponseUserStorageTypeDef(
    _ClientActivateUserResponseUserStorageTypeDef
):
    """
    Type definition for `ClientActivateUserResponseUser` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_ClientActivateUserResponseUserTypeDef = TypedDict(
    "_ClientActivateUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": ClientActivateUserResponseUserStorageTypeDef,
    },
    total=False,
)


class ClientActivateUserResponseUserTypeDef(_ClientActivateUserResponseUserTypeDef):
    """
    Type definition for `ClientActivateUserResponse` `User`

    The user information.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_ClientActivateUserResponseTypeDef = TypedDict(
    "_ClientActivateUserResponseTypeDef",
    {"User": ClientActivateUserResponseUserTypeDef},
    total=False,
)


class ClientActivateUserResponseTypeDef(_ClientActivateUserResponseTypeDef):
    """
    Type definition for `ClientActivateUser` `Response`

    - **User** *(dict) --*

      The user information.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The login name of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

      - **GivenName** *(string) --*

        The given name of the user.

      - **Surname** *(string) --*

        The surname of the user.

      - **OrganizationId** *(string) --*

        The ID of the organization.

      - **RootFolderId** *(string) --*

        The ID of the root folder.

      - **RecycleBinFolderId** *(string) --*

        The ID of the recycle bin folder.

      - **Status** *(string) --*

        The status of the user.

      - **Type** *(string) --*

        The type of user.

      - **CreatedTimestamp** *(datetime) --*

        The time when the user was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the user was modified.

      - **TimeZoneId** *(string) --*

        The time zone ID of the user.

      - **Locale** *(string) --*

        The locale of the user.

      - **Storage** *(dict) --*

        The storage for the user.

        - **StorageUtilizedInBytes** *(integer) --*

          The amount of storage used, in bytes.

        - **StorageRule** *(dict) --*

          The storage for a user.

          - **StorageAllocatedInBytes** *(integer) --*

            The amount of storage allocated, in bytes.

          - **StorageType** *(string) --*

            The type of storage.
    """


_ClientAddResourcePermissionsNotificationOptionsTypeDef = TypedDict(
    "_ClientAddResourcePermissionsNotificationOptionsTypeDef",
    {"SendEmail": bool, "EmailMessage": str},
    total=False,
)


class ClientAddResourcePermissionsNotificationOptionsTypeDef(
    _ClientAddResourcePermissionsNotificationOptionsTypeDef
):
    """
    Type definition for `ClientAddResourcePermissions` `NotificationOptions`

    The notification options.

    - **SendEmail** *(boolean) --*

      Boolean value to indicate an email notification should be sent to the receipients.

    - **EmailMessage** *(string) --*

      Text value to be included in the email body.
    """


_ClientAddResourcePermissionsPrincipalsTypeDef = TypedDict(
    "_ClientAddResourcePermissionsPrincipalsTypeDef",
    {"Id": str, "Type": str, "Role": str},
)


class ClientAddResourcePermissionsPrincipalsTypeDef(
    _ClientAddResourcePermissionsPrincipalsTypeDef
):
    """
    Type definition for `ClientAddResourcePermissions` `Principals`

    Describes the recipient type and ID, if available.

    - **Id** *(string) --* **[REQUIRED]**

      The ID of the recipient.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the recipient.

    - **Role** *(string) --* **[REQUIRED]**

      The role of the recipient.
    """


_ClientAddResourcePermissionsResponseShareResultsTypeDef = TypedDict(
    "_ClientAddResourcePermissionsResponseShareResultsTypeDef",
    {
        "PrincipalId": str,
        "InviteePrincipalId": str,
        "Role": str,
        "Status": str,
        "ShareId": str,
        "StatusMessage": str,
    },
    total=False,
)


class ClientAddResourcePermissionsResponseShareResultsTypeDef(
    _ClientAddResourcePermissionsResponseShareResultsTypeDef
):
    """
    Type definition for `ClientAddResourcePermissionsResponse` `ShareResults`

    Describes the share results of a resource.

    - **PrincipalId** *(string) --*

      The ID of the principal.

    - **InviteePrincipalId** *(string) --*

      The ID of the invited user.

    - **Role** *(string) --*

      The role.

    - **Status** *(string) --*

      The status.

    - **ShareId** *(string) --*

      The ID of the resource that was shared.

    - **StatusMessage** *(string) --*

      The status message.
    """


_ClientAddResourcePermissionsResponseTypeDef = TypedDict(
    "_ClientAddResourcePermissionsResponseTypeDef",
    {"ShareResults": List[ClientAddResourcePermissionsResponseShareResultsTypeDef]},
    total=False,
)


class ClientAddResourcePermissionsResponseTypeDef(
    _ClientAddResourcePermissionsResponseTypeDef
):
    """
    Type definition for `ClientAddResourcePermissions` `Response`

    - **ShareResults** *(list) --*

      The share results.

      - *(dict) --*

        Describes the share results of a resource.

        - **PrincipalId** *(string) --*

          The ID of the principal.

        - **InviteePrincipalId** *(string) --*

          The ID of the invited user.

        - **Role** *(string) --*

          The role.

        - **Status** *(string) --*

          The status.

        - **ShareId** *(string) --*

          The ID of the resource that was shared.

        - **StatusMessage** *(string) --*

          The status message.
    """


_ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef = TypedDict(
    "_ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef(
    _ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef
):
    """
    Type definition for `ClientCreateCommentResponseCommentContributorStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_ClientCreateCommentResponseCommentContributorStorageTypeDef = TypedDict(
    "_ClientCreateCommentResponseCommentContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientCreateCommentResponseCommentContributorStorageTypeDef(
    _ClientCreateCommentResponseCommentContributorStorageTypeDef
):
    """
    Type definition for `ClientCreateCommentResponseCommentContributor` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_ClientCreateCommentResponseCommentContributorTypeDef = TypedDict(
    "_ClientCreateCommentResponseCommentContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": ClientCreateCommentResponseCommentContributorStorageTypeDef,
    },
    total=False,
)


class ClientCreateCommentResponseCommentContributorTypeDef(
    _ClientCreateCommentResponseCommentContributorTypeDef
):
    """
    Type definition for `ClientCreateCommentResponseComment` `Contributor`

    The details of the user who made the comment.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_ClientCreateCommentResponseCommentTypeDef = TypedDict(
    "_ClientCreateCommentResponseCommentTypeDef",
    {
        "CommentId": str,
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": ClientCreateCommentResponseCommentContributorTypeDef,
        "CreatedTimestamp": datetime,
        "Status": str,
        "Visibility": str,
        "RecipientId": str,
    },
    total=False,
)


class ClientCreateCommentResponseCommentTypeDef(
    _ClientCreateCommentResponseCommentTypeDef
):
    """
    Type definition for `ClientCreateCommentResponse` `Comment`

    The comment that has been created.

    - **CommentId** *(string) --*

      The ID of the comment.

    - **ParentId** *(string) --*

      The ID of the parent comment.

    - **ThreadId** *(string) --*

      The ID of the root comment in the thread.

    - **Text** *(string) --*

      The text of the comment.

    - **Contributor** *(dict) --*

      The details of the user who made the comment.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The login name of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

      - **GivenName** *(string) --*

        The given name of the user.

      - **Surname** *(string) --*

        The surname of the user.

      - **OrganizationId** *(string) --*

        The ID of the organization.

      - **RootFolderId** *(string) --*

        The ID of the root folder.

      - **RecycleBinFolderId** *(string) --*

        The ID of the recycle bin folder.

      - **Status** *(string) --*

        The status of the user.

      - **Type** *(string) --*

        The type of user.

      - **CreatedTimestamp** *(datetime) --*

        The time when the user was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the user was modified.

      - **TimeZoneId** *(string) --*

        The time zone ID of the user.

      - **Locale** *(string) --*

        The locale of the user.

      - **Storage** *(dict) --*

        The storage for the user.

        - **StorageUtilizedInBytes** *(integer) --*

          The amount of storage used, in bytes.

        - **StorageRule** *(dict) --*

          The storage for a user.

          - **StorageAllocatedInBytes** *(integer) --*

            The amount of storage allocated, in bytes.

          - **StorageType** *(string) --*

            The type of storage.

    - **CreatedTimestamp** *(datetime) --*

      The time that the comment was created.

    - **Status** *(string) --*

      The status of the comment.

    - **Visibility** *(string) --*

      The visibility of the comment. Options are either PRIVATE, where the comment is visible
      only to the comment author and document owner and co-owners, or PUBLIC, where the comment
      is visible to document owners, co-owners, and contributors.

    - **RecipientId** *(string) --*

      If the comment is a reply to another user's comment, this field contains the user ID of the
      user being replied to.
    """


_ClientCreateCommentResponseTypeDef = TypedDict(
    "_ClientCreateCommentResponseTypeDef",
    {"Comment": ClientCreateCommentResponseCommentTypeDef},
    total=False,
)


class ClientCreateCommentResponseTypeDef(_ClientCreateCommentResponseTypeDef):
    """
    Type definition for `ClientCreateComment` `Response`

    - **Comment** *(dict) --*

      The comment that has been created.

      - **CommentId** *(string) --*

        The ID of the comment.

      - **ParentId** *(string) --*

        The ID of the parent comment.

      - **ThreadId** *(string) --*

        The ID of the root comment in the thread.

      - **Text** *(string) --*

        The text of the comment.

      - **Contributor** *(dict) --*

        The details of the user who made the comment.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The login name of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

        - **GivenName** *(string) --*

          The given name of the user.

        - **Surname** *(string) --*

          The surname of the user.

        - **OrganizationId** *(string) --*

          The ID of the organization.

        - **RootFolderId** *(string) --*

          The ID of the root folder.

        - **RecycleBinFolderId** *(string) --*

          The ID of the recycle bin folder.

        - **Status** *(string) --*

          The status of the user.

        - **Type** *(string) --*

          The type of user.

        - **CreatedTimestamp** *(datetime) --*

          The time when the user was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the user was modified.

        - **TimeZoneId** *(string) --*

          The time zone ID of the user.

        - **Locale** *(string) --*

          The locale of the user.

        - **Storage** *(dict) --*

          The storage for the user.

          - **StorageUtilizedInBytes** *(integer) --*

            The amount of storage used, in bytes.

          - **StorageRule** *(dict) --*

            The storage for a user.

            - **StorageAllocatedInBytes** *(integer) --*

              The amount of storage allocated, in bytes.

            - **StorageType** *(string) --*

              The type of storage.

      - **CreatedTimestamp** *(datetime) --*

        The time that the comment was created.

      - **Status** *(string) --*

        The status of the comment.

      - **Visibility** *(string) --*

        The visibility of the comment. Options are either PRIVATE, where the comment is visible
        only to the comment author and document owner and co-owners, or PUBLIC, where the comment
        is visible to document owners, co-owners, and contributors.

      - **RecipientId** *(string) --*

        If the comment is a reply to another user's comment, this field contains the user ID of the
        user being replied to.
    """


_ClientCreateFolderResponseMetadataTypeDef = TypedDict(
    "_ClientCreateFolderResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": str,
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class ClientCreateFolderResponseMetadataTypeDef(
    _ClientCreateFolderResponseMetadataTypeDef
):
    """
    Type definition for `ClientCreateFolderResponse` `Metadata`

    The metadata of the folder.

    - **Id** *(string) --*

      The ID of the folder.

    - **Name** *(string) --*

      The name of the folder.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the folder was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the folder was updated.

    - **ResourceState** *(string) --*

      The resource state of the folder.

    - **Signature** *(string) --*

      The unique identifier created from the subfolders and documents of the folder.

    - **Labels** *(list) --*

      List of labels on the folder.

      - *(string) --*

    - **Size** *(integer) --*

      The size of the folder metadata.

    - **LatestVersionSize** *(integer) --*

      The size of the latest version of the folder metadata.
    """


_ClientCreateFolderResponseTypeDef = TypedDict(
    "_ClientCreateFolderResponseTypeDef",
    {"Metadata": ClientCreateFolderResponseMetadataTypeDef},
    total=False,
)


class ClientCreateFolderResponseTypeDef(_ClientCreateFolderResponseTypeDef):
    """
    Type definition for `ClientCreateFolder` `Response`

    - **Metadata** *(dict) --*

      The metadata of the folder.

      - **Id** *(string) --*

        The ID of the folder.

      - **Name** *(string) --*

        The name of the folder.

      - **CreatorId** *(string) --*

        The ID of the creator.

      - **ParentFolderId** *(string) --*

        The ID of the parent folder.

      - **CreatedTimestamp** *(datetime) --*

        The time when the folder was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the folder was updated.

      - **ResourceState** *(string) --*

        The resource state of the folder.

      - **Signature** *(string) --*

        The unique identifier created from the subfolders and documents of the folder.

      - **Labels** *(list) --*

        List of labels on the folder.

        - *(string) --*

      - **Size** *(integer) --*

        The size of the folder metadata.

      - **LatestVersionSize** *(integer) --*

        The size of the latest version of the folder metadata.
    """


_ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef = TypedDict(
    "_ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)


class ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef(
    _ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef
):
    """
    Type definition for `ClientCreateNotificationSubscriptionResponse` `Subscription`

    The subscription.

    - **SubscriptionId** *(string) --*

      The ID of the subscription.

    - **EndPoint** *(string) --*

      The endpoint of the subscription.

    - **Protocol** *(string) --*

      The protocol of the subscription.
    """


_ClientCreateNotificationSubscriptionResponseTypeDef = TypedDict(
    "_ClientCreateNotificationSubscriptionResponseTypeDef",
    {"Subscription": ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef},
    total=False,
)


class ClientCreateNotificationSubscriptionResponseTypeDef(
    _ClientCreateNotificationSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientCreateNotificationSubscription` `Response`

    - **Subscription** *(dict) --*

      The subscription.

      - **SubscriptionId** *(string) --*

        The ID of the subscription.

      - **EndPoint** *(string) --*

        The endpoint of the subscription.

      - **Protocol** *(string) --*

        The protocol of the subscription.
    """


_ClientCreateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "_ClientCreateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class ClientCreateUserResponseUserStorageStorageRuleTypeDef(
    _ClientCreateUserResponseUserStorageStorageRuleTypeDef
):
    """
    Type definition for `ClientCreateUserResponseUserStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_ClientCreateUserResponseUserStorageTypeDef = TypedDict(
    "_ClientCreateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientCreateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientCreateUserResponseUserStorageTypeDef(
    _ClientCreateUserResponseUserStorageTypeDef
):
    """
    Type definition for `ClientCreateUserResponseUser` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_ClientCreateUserResponseUserTypeDef = TypedDict(
    "_ClientCreateUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": ClientCreateUserResponseUserStorageTypeDef,
    },
    total=False,
)


class ClientCreateUserResponseUserTypeDef(_ClientCreateUserResponseUserTypeDef):
    """
    Type definition for `ClientCreateUserResponse` `User`

    The user information.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef",
    {"User": ClientCreateUserResponseUserTypeDef},
    total=False,
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    Type definition for `ClientCreateUser` `Response`

    - **User** *(dict) --*

      The user information.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The login name of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

      - **GivenName** *(string) --*

        The given name of the user.

      - **Surname** *(string) --*

        The surname of the user.

      - **OrganizationId** *(string) --*

        The ID of the organization.

      - **RootFolderId** *(string) --*

        The ID of the root folder.

      - **RecycleBinFolderId** *(string) --*

        The ID of the recycle bin folder.

      - **Status** *(string) --*

        The status of the user.

      - **Type** *(string) --*

        The type of user.

      - **CreatedTimestamp** *(datetime) --*

        The time when the user was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the user was modified.

      - **TimeZoneId** *(string) --*

        The time zone ID of the user.

      - **Locale** *(string) --*

        The locale of the user.

      - **Storage** *(dict) --*

        The storage for the user.

        - **StorageUtilizedInBytes** *(integer) --*

          The amount of storage used, in bytes.

        - **StorageRule** *(dict) --*

          The storage for a user.

          - **StorageAllocatedInBytes** *(integer) --*

            The amount of storage allocated, in bytes.

          - **StorageType** *(string) --*

            The type of storage.
    """


_ClientCreateUserStorageRuleTypeDef = TypedDict(
    "_ClientCreateUserStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class ClientCreateUserStorageRuleTypeDef(_ClientCreateUserStorageRuleTypeDef):
    """
    Type definition for `ClientCreateUser` `StorageRule`

    The amount of storage for the user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributor` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivitiesCommentMetadata` `Contributor`

    The user who made the comment.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef",
    {
        "CommentId": str,
        "Contributor": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef,
        "CreatedTimestamp": datetime,
        "CommentStatus": str,
        "RecipientId": str,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivities` `CommentMetadata`

    Metadata of the commenting activity. This is an optional field and is filled for
    commenting activities.

    - **CommentId** *(string) --*

      The ID of the comment.

    - **Contributor** *(dict) --*

      The user who made the comment.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The login name of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

      - **GivenName** *(string) --*

        The given name of the user.

      - **Surname** *(string) --*

        The surname of the user.

      - **OrganizationId** *(string) --*

        The ID of the organization.

      - **RootFolderId** *(string) --*

        The ID of the root folder.

      - **RecycleBinFolderId** *(string) --*

        The ID of the recycle bin folder.

      - **Status** *(string) --*

        The status of the user.

      - **Type** *(string) --*

        The type of user.

      - **CreatedTimestamp** *(datetime) --*

        The time when the user was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the user was modified.

      - **TimeZoneId** *(string) --*

        The time zone ID of the user.

      - **Locale** *(string) --*

        The locale of the user.

      - **Storage** *(dict) --*

        The storage for the user.

        - **StorageUtilizedInBytes** *(integer) --*

          The amount of storage used, in bytes.

        - **StorageRule** *(dict) --*

          The storage for a user.

          - **StorageAllocatedInBytes** *(integer) --*

            The amount of storage allocated, in bytes.

          - **StorageType** *(string) --*

            The type of storage.

    - **CreatedTimestamp** *(datetime) --*

      The timestamp that the comment was created.

    - **CommentStatus** *(string) --*

      The status of the comment.

    - **RecipientId** *(string) --*

      The ID of the user being replied to.
    """


_ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivities` `Initiator`

    The user who performed the action.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The name of the user.

    - **GivenName** *(string) --*

      The given name of the user before a rename operation.

    - **Surname** *(string) --*

      The surname of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.
    """


_ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivitiesOriginalParent` `Owner`

    The owner of the resource.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The name of the user.

    - **GivenName** *(string) --*

      The given name of the user before a rename operation.

    - **Surname** *(string) --*

      The surname of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.
    """


_ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef",
    {
        "Type": str,
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef,
        "ParentId": str,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivities` `OriginalParent`

    The original parent of the resource. This is an optional field and is filled for move
    activities.

    - **Type** *(string) --*

      The type of resource.

    - **Name** *(string) --*

      The name of the resource.

    - **OriginalName** *(string) --*

      The original name of the resource before a rename operation.

    - **Id** *(string) --*

      The ID of the resource.

    - **VersionId** *(string) --*

      The version ID of the resource. This is an optional field and is filled for action on
      document version.

    - **Owner** *(dict) --*

      The owner of the resource.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The name of the user.

      - **GivenName** *(string) --*

        The given name of the user before a rename operation.

      - **Surname** *(string) --*

        The surname of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

    - **ParentId** *(string) --*

      The parent ID of the resource before a rename operation.
    """


_ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef",
    {"Id": str, "Name": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivitiesParticipants` `Groups`

    Describes the metadata of a user group.

    - **Id** *(string) --*

      The ID of the user group.

    - **Name** *(string) --*

      The name of the group.
    """


_ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivitiesParticipants` `Users`

    Describes the metadata of the user.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The name of the user.

    - **GivenName** *(string) --*

      The given name of the user before a rename operation.

    - **Surname** *(string) --*

      The surname of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.
    """


_ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef",
    {
        "Users": List[
            ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef
        ],
        "Groups": List[
            ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivities` `Participants`

    The list of users or groups impacted by this action. This is an optional field and is
    filled for the following sharing activities: DOCUMENT_SHARED, DOCUMENT_SHARED,
    DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.

    - **Users** *(list) --*

      The list of users.

      - *(dict) --*

        Describes the metadata of the user.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The name of the user.

        - **GivenName** *(string) --*

          The given name of the user before a rename operation.

        - **Surname** *(string) --*

          The surname of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

    - **Groups** *(list) --*

      The list of user groups.

      - *(dict) --*

        Describes the metadata of a user group.

        - **Id** *(string) --*

          The ID of the user group.

        - **Name** *(string) --*

          The name of the group.
    """


_ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivitiesResourceMetadata` `Owner`

    The owner of the resource.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The name of the user.

    - **GivenName** *(string) --*

      The given name of the user before a rename operation.

    - **Surname** *(string) --*

      The surname of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.
    """


_ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef",
    {
        "Type": str,
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef,
        "ParentId": str,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponseUserActivities` `ResourceMetadata`

    The metadata of the resource involved in the user action.

    - **Type** *(string) --*

      The type of resource.

    - **Name** *(string) --*

      The name of the resource.

    - **OriginalName** *(string) --*

      The original name of the resource before a rename operation.

    - **Id** *(string) --*

      The ID of the resource.

    - **VersionId** *(string) --*

      The version ID of the resource. This is an optional field and is filled for action on
      document version.

    - **Owner** *(dict) --*

      The owner of the resource.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The name of the user.

      - **GivenName** *(string) --*

        The given name of the user before a rename operation.

      - **Surname** *(string) --*

        The surname of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

    - **ParentId** *(string) --*

      The parent ID of the resource before a rename operation.
    """


_ClientDescribeActivitiesResponseUserActivitiesTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesTypeDef",
    {
        "Type": str,
        "TimeStamp": datetime,
        "IsIndirectActivity": bool,
        "OrganizationId": str,
        "Initiator": ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef,
        "Participants": ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef,
        "ResourceMetadata": ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef,
        "OriginalParent": ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef,
        "CommentMetadata": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesTypeDef
):
    """
    Type definition for `ClientDescribeActivitiesResponse` `UserActivities`

    Describes the activity information.

    - **Type** *(string) --*

      The activity type.

    - **TimeStamp** *(datetime) --*

      The timestamp when the action was performed.

    - **IsIndirectActivity** *(boolean) --*

      Indicates whether an activity is indirect or direct. An indirect activity results from a
      direct activity performed on a parent resource. For example, sharing a parent folder (the
      direct activity) shares all of the subfolders and documents within the parent folder (the
      indirect activity).

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **Initiator** *(dict) --*

      The user who performed the action.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The name of the user.

      - **GivenName** *(string) --*

        The given name of the user before a rename operation.

      - **Surname** *(string) --*

        The surname of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

    - **Participants** *(dict) --*

      The list of users or groups impacted by this action. This is an optional field and is
      filled for the following sharing activities: DOCUMENT_SHARED, DOCUMENT_SHARED,
      DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.

      - **Users** *(list) --*

        The list of users.

        - *(dict) --*

          Describes the metadata of the user.

          - **Id** *(string) --*

            The ID of the user.

          - **Username** *(string) --*

            The name of the user.

          - **GivenName** *(string) --*

            The given name of the user before a rename operation.

          - **Surname** *(string) --*

            The surname of the user.

          - **EmailAddress** *(string) --*

            The email address of the user.

      - **Groups** *(list) --*

        The list of user groups.

        - *(dict) --*

          Describes the metadata of a user group.

          - **Id** *(string) --*

            The ID of the user group.

          - **Name** *(string) --*

            The name of the group.

    - **ResourceMetadata** *(dict) --*

      The metadata of the resource involved in the user action.

      - **Type** *(string) --*

        The type of resource.

      - **Name** *(string) --*

        The name of the resource.

      - **OriginalName** *(string) --*

        The original name of the resource before a rename operation.

      - **Id** *(string) --*

        The ID of the resource.

      - **VersionId** *(string) --*

        The version ID of the resource. This is an optional field and is filled for action on
        document version.

      - **Owner** *(dict) --*

        The owner of the resource.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The name of the user.

        - **GivenName** *(string) --*

          The given name of the user before a rename operation.

        - **Surname** *(string) --*

          The surname of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

      - **ParentId** *(string) --*

        The parent ID of the resource before a rename operation.

    - **OriginalParent** *(dict) --*

      The original parent of the resource. This is an optional field and is filled for move
      activities.

      - **Type** *(string) --*

        The type of resource.

      - **Name** *(string) --*

        The name of the resource.

      - **OriginalName** *(string) --*

        The original name of the resource before a rename operation.

      - **Id** *(string) --*

        The ID of the resource.

      - **VersionId** *(string) --*

        The version ID of the resource. This is an optional field and is filled for action on
        document version.

      - **Owner** *(dict) --*

        The owner of the resource.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The name of the user.

        - **GivenName** *(string) --*

          The given name of the user before a rename operation.

        - **Surname** *(string) --*

          The surname of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

      - **ParentId** *(string) --*

        The parent ID of the resource before a rename operation.

    - **CommentMetadata** *(dict) --*

      Metadata of the commenting activity. This is an optional field and is filled for
      commenting activities.

      - **CommentId** *(string) --*

        The ID of the comment.

      - **Contributor** *(dict) --*

        The user who made the comment.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The login name of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

        - **GivenName** *(string) --*

          The given name of the user.

        - **Surname** *(string) --*

          The surname of the user.

        - **OrganizationId** *(string) --*

          The ID of the organization.

        - **RootFolderId** *(string) --*

          The ID of the root folder.

        - **RecycleBinFolderId** *(string) --*

          The ID of the recycle bin folder.

        - **Status** *(string) --*

          The status of the user.

        - **Type** *(string) --*

          The type of user.

        - **CreatedTimestamp** *(datetime) --*

          The time when the user was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the user was modified.

        - **TimeZoneId** *(string) --*

          The time zone ID of the user.

        - **Locale** *(string) --*

          The locale of the user.

        - **Storage** *(dict) --*

          The storage for the user.

          - **StorageUtilizedInBytes** *(integer) --*

            The amount of storage used, in bytes.

          - **StorageRule** *(dict) --*

            The storage for a user.

            - **StorageAllocatedInBytes** *(integer) --*

              The amount of storage allocated, in bytes.

            - **StorageType** *(string) --*

              The type of storage.

      - **CreatedTimestamp** *(datetime) --*

        The timestamp that the comment was created.

      - **CommentStatus** *(string) --*

        The status of the comment.

      - **RecipientId** *(string) --*

        The ID of the user being replied to.
    """


_ClientDescribeActivitiesResponseTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseTypeDef",
    {
        "UserActivities": List[ClientDescribeActivitiesResponseUserActivitiesTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeActivitiesResponseTypeDef(_ClientDescribeActivitiesResponseTypeDef):
    """
    Type definition for `ClientDescribeActivities` `Response`

    - **UserActivities** *(list) --*

      The list of activities for the specified user and time period.

      - *(dict) --*

        Describes the activity information.

        - **Type** *(string) --*

          The activity type.

        - **TimeStamp** *(datetime) --*

          The timestamp when the action was performed.

        - **IsIndirectActivity** *(boolean) --*

          Indicates whether an activity is indirect or direct. An indirect activity results from a
          direct activity performed on a parent resource. For example, sharing a parent folder (the
          direct activity) shares all of the subfolders and documents within the parent folder (the
          indirect activity).

        - **OrganizationId** *(string) --*

          The ID of the organization.

        - **Initiator** *(dict) --*

          The user who performed the action.

          - **Id** *(string) --*

            The ID of the user.

          - **Username** *(string) --*

            The name of the user.

          - **GivenName** *(string) --*

            The given name of the user before a rename operation.

          - **Surname** *(string) --*

            The surname of the user.

          - **EmailAddress** *(string) --*

            The email address of the user.

        - **Participants** *(dict) --*

          The list of users or groups impacted by this action. This is an optional field and is
          filled for the following sharing activities: DOCUMENT_SHARED, DOCUMENT_SHARED,
          DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.

          - **Users** *(list) --*

            The list of users.

            - *(dict) --*

              Describes the metadata of the user.

              - **Id** *(string) --*

                The ID of the user.

              - **Username** *(string) --*

                The name of the user.

              - **GivenName** *(string) --*

                The given name of the user before a rename operation.

              - **Surname** *(string) --*

                The surname of the user.

              - **EmailAddress** *(string) --*

                The email address of the user.

          - **Groups** *(list) --*

            The list of user groups.

            - *(dict) --*

              Describes the metadata of a user group.

              - **Id** *(string) --*

                The ID of the user group.

              - **Name** *(string) --*

                The name of the group.

        - **ResourceMetadata** *(dict) --*

          The metadata of the resource involved in the user action.

          - **Type** *(string) --*

            The type of resource.

          - **Name** *(string) --*

            The name of the resource.

          - **OriginalName** *(string) --*

            The original name of the resource before a rename operation.

          - **Id** *(string) --*

            The ID of the resource.

          - **VersionId** *(string) --*

            The version ID of the resource. This is an optional field and is filled for action on
            document version.

          - **Owner** *(dict) --*

            The owner of the resource.

            - **Id** *(string) --*

              The ID of the user.

            - **Username** *(string) --*

              The name of the user.

            - **GivenName** *(string) --*

              The given name of the user before a rename operation.

            - **Surname** *(string) --*

              The surname of the user.

            - **EmailAddress** *(string) --*

              The email address of the user.

          - **ParentId** *(string) --*

            The parent ID of the resource before a rename operation.

        - **OriginalParent** *(dict) --*

          The original parent of the resource. This is an optional field and is filled for move
          activities.

          - **Type** *(string) --*

            The type of resource.

          - **Name** *(string) --*

            The name of the resource.

          - **OriginalName** *(string) --*

            The original name of the resource before a rename operation.

          - **Id** *(string) --*

            The ID of the resource.

          - **VersionId** *(string) --*

            The version ID of the resource. This is an optional field and is filled for action on
            document version.

          - **Owner** *(dict) --*

            The owner of the resource.

            - **Id** *(string) --*

              The ID of the user.

            - **Username** *(string) --*

              The name of the user.

            - **GivenName** *(string) --*

              The given name of the user before a rename operation.

            - **Surname** *(string) --*

              The surname of the user.

            - **EmailAddress** *(string) --*

              The email address of the user.

          - **ParentId** *(string) --*

            The parent ID of the resource before a rename operation.

        - **CommentMetadata** *(dict) --*

          Metadata of the commenting activity. This is an optional field and is filled for
          commenting activities.

          - **CommentId** *(string) --*

            The ID of the comment.

          - **Contributor** *(dict) --*

            The user who made the comment.

            - **Id** *(string) --*

              The ID of the user.

            - **Username** *(string) --*

              The login name of the user.

            - **EmailAddress** *(string) --*

              The email address of the user.

            - **GivenName** *(string) --*

              The given name of the user.

            - **Surname** *(string) --*

              The surname of the user.

            - **OrganizationId** *(string) --*

              The ID of the organization.

            - **RootFolderId** *(string) --*

              The ID of the root folder.

            - **RecycleBinFolderId** *(string) --*

              The ID of the recycle bin folder.

            - **Status** *(string) --*

              The status of the user.

            - **Type** *(string) --*

              The type of user.

            - **CreatedTimestamp** *(datetime) --*

              The time when the user was created.

            - **ModifiedTimestamp** *(datetime) --*

              The time when the user was modified.

            - **TimeZoneId** *(string) --*

              The time zone ID of the user.

            - **Locale** *(string) --*

              The locale of the user.

            - **Storage** *(dict) --*

              The storage for the user.

              - **StorageUtilizedInBytes** *(integer) --*

                The amount of storage used, in bytes.

              - **StorageRule** *(dict) --*

                The storage for a user.

                - **StorageAllocatedInBytes** *(integer) --*

                  The amount of storage allocated, in bytes.

                - **StorageType** *(string) --*

                  The type of storage.

          - **CreatedTimestamp** *(datetime) --*

            The timestamp that the comment was created.

          - **CommentStatus** *(string) --*

            The status of the comment.

          - **RecipientId** *(string) --*

            The ID of the user being replied to.

    - **Marker** *(string) --*

      The marker for the next set of results.
    """


_ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef = TypedDict(
    "_ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef(
    _ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef
):
    """
    Type definition for `ClientDescribeCommentsResponseCommentsContributorStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_ClientDescribeCommentsResponseCommentsContributorStorageTypeDef = TypedDict(
    "_ClientDescribeCommentsResponseCommentsContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientDescribeCommentsResponseCommentsContributorStorageTypeDef(
    _ClientDescribeCommentsResponseCommentsContributorStorageTypeDef
):
    """
    Type definition for `ClientDescribeCommentsResponseCommentsContributor` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_ClientDescribeCommentsResponseCommentsContributorTypeDef = TypedDict(
    "_ClientDescribeCommentsResponseCommentsContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": ClientDescribeCommentsResponseCommentsContributorStorageTypeDef,
    },
    total=False,
)


class ClientDescribeCommentsResponseCommentsContributorTypeDef(
    _ClientDescribeCommentsResponseCommentsContributorTypeDef
):
    """
    Type definition for `ClientDescribeCommentsResponseComments` `Contributor`

    The details of the user who made the comment.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_ClientDescribeCommentsResponseCommentsTypeDef = TypedDict(
    "_ClientDescribeCommentsResponseCommentsTypeDef",
    {
        "CommentId": str,
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": ClientDescribeCommentsResponseCommentsContributorTypeDef,
        "CreatedTimestamp": datetime,
        "Status": str,
        "Visibility": str,
        "RecipientId": str,
    },
    total=False,
)


class ClientDescribeCommentsResponseCommentsTypeDef(
    _ClientDescribeCommentsResponseCommentsTypeDef
):
    """
    Type definition for `ClientDescribeCommentsResponse` `Comments`

    Describes a comment.

    - **CommentId** *(string) --*

      The ID of the comment.

    - **ParentId** *(string) --*

      The ID of the parent comment.

    - **ThreadId** *(string) --*

      The ID of the root comment in the thread.

    - **Text** *(string) --*

      The text of the comment.

    - **Contributor** *(dict) --*

      The details of the user who made the comment.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The login name of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

      - **GivenName** *(string) --*

        The given name of the user.

      - **Surname** *(string) --*

        The surname of the user.

      - **OrganizationId** *(string) --*

        The ID of the organization.

      - **RootFolderId** *(string) --*

        The ID of the root folder.

      - **RecycleBinFolderId** *(string) --*

        The ID of the recycle bin folder.

      - **Status** *(string) --*

        The status of the user.

      - **Type** *(string) --*

        The type of user.

      - **CreatedTimestamp** *(datetime) --*

        The time when the user was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the user was modified.

      - **TimeZoneId** *(string) --*

        The time zone ID of the user.

      - **Locale** *(string) --*

        The locale of the user.

      - **Storage** *(dict) --*

        The storage for the user.

        - **StorageUtilizedInBytes** *(integer) --*

          The amount of storage used, in bytes.

        - **StorageRule** *(dict) --*

          The storage for a user.

          - **StorageAllocatedInBytes** *(integer) --*

            The amount of storage allocated, in bytes.

          - **StorageType** *(string) --*

            The type of storage.

    - **CreatedTimestamp** *(datetime) --*

      The time that the comment was created.

    - **Status** *(string) --*

      The status of the comment.

    - **Visibility** *(string) --*

      The visibility of the comment. Options are either PRIVATE, where the comment is visible
      only to the comment author and document owner and co-owners, or PUBLIC, where the comment
      is visible to document owners, co-owners, and contributors.

    - **RecipientId** *(string) --*

      If the comment is a reply to another user's comment, this field contains the user ID of
      the user being replied to.
    """


_ClientDescribeCommentsResponseTypeDef = TypedDict(
    "_ClientDescribeCommentsResponseTypeDef",
    {"Comments": List[ClientDescribeCommentsResponseCommentsTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeCommentsResponseTypeDef(_ClientDescribeCommentsResponseTypeDef):
    """
    Type definition for `ClientDescribeComments` `Response`

    - **Comments** *(list) --*

      The list of comments for the specified document version.

      - *(dict) --*

        Describes a comment.

        - **CommentId** *(string) --*

          The ID of the comment.

        - **ParentId** *(string) --*

          The ID of the parent comment.

        - **ThreadId** *(string) --*

          The ID of the root comment in the thread.

        - **Text** *(string) --*

          The text of the comment.

        - **Contributor** *(dict) --*

          The details of the user who made the comment.

          - **Id** *(string) --*

            The ID of the user.

          - **Username** *(string) --*

            The login name of the user.

          - **EmailAddress** *(string) --*

            The email address of the user.

          - **GivenName** *(string) --*

            The given name of the user.

          - **Surname** *(string) --*

            The surname of the user.

          - **OrganizationId** *(string) --*

            The ID of the organization.

          - **RootFolderId** *(string) --*

            The ID of the root folder.

          - **RecycleBinFolderId** *(string) --*

            The ID of the recycle bin folder.

          - **Status** *(string) --*

            The status of the user.

          - **Type** *(string) --*

            The type of user.

          - **CreatedTimestamp** *(datetime) --*

            The time when the user was created.

          - **ModifiedTimestamp** *(datetime) --*

            The time when the user was modified.

          - **TimeZoneId** *(string) --*

            The time zone ID of the user.

          - **Locale** *(string) --*

            The locale of the user.

          - **Storage** *(dict) --*

            The storage for the user.

            - **StorageUtilizedInBytes** *(integer) --*

              The amount of storage used, in bytes.

            - **StorageRule** *(dict) --*

              The storage for a user.

              - **StorageAllocatedInBytes** *(integer) --*

                The amount of storage allocated, in bytes.

              - **StorageType** *(string) --*

                The type of storage.

        - **CreatedTimestamp** *(datetime) --*

          The time that the comment was created.

        - **Status** *(string) --*

          The status of the comment.

        - **Visibility** *(string) --*

          The visibility of the comment. Options are either PRIVATE, where the comment is visible
          only to the comment author and document owner and co-owners, or PUBLIC, where the comment
          is visible to document owners, co-owners, and contributors.

        - **RecipientId** *(string) --*

          If the comment is a reply to another user's comment, this field contains the user ID of
          the user being replied to.

    - **Marker** *(string) --*

      The marker for the next set of results. This marker was received from a previous call.
    """


_ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef = TypedDict(
    "_ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef(
    _ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef
):
    """
    Type definition for `ClientDescribeDocumentVersionsResponse` `DocumentVersions`

    Describes a version of a document.

    - **Id** *(string) --*

      The ID of the version.

    - **Name** *(string) --*

      The name of the version.

    - **ContentType** *(string) --*

      The content type of the document.

    - **Size** *(integer) --*

      The size of the document, in bytes.

    - **Signature** *(string) --*

      The signature of the document.

    - **Status** *(string) --*

      The status of the document.

    - **CreatedTimestamp** *(datetime) --*

      The timestamp when the document was first uploaded.

    - **ModifiedTimestamp** *(datetime) --*

      The timestamp when the document was last uploaded.

    - **ContentCreatedTimestamp** *(datetime) --*

      The timestamp when the content of the document was originally created.

    - **ContentModifiedTimestamp** *(datetime) --*

      The timestamp when the content of the document was modified.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **Thumbnail** *(dict) --*

      The thumbnail of the document.

      - *(string) --*

        - *(string) --*

    - **Source** *(dict) --*

      The source of the document.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeDocumentVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeDocumentVersionsResponseTypeDef",
    {
        "DocumentVersions": List[
            ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeDocumentVersionsResponseTypeDef(
    _ClientDescribeDocumentVersionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDocumentVersions` `Response`

    - **DocumentVersions** *(list) --*

      The document versions.

      - *(dict) --*

        Describes a version of a document.

        - **Id** *(string) --*

          The ID of the version.

        - **Name** *(string) --*

          The name of the version.

        - **ContentType** *(string) --*

          The content type of the document.

        - **Size** *(integer) --*

          The size of the document, in bytes.

        - **Signature** *(string) --*

          The signature of the document.

        - **Status** *(string) --*

          The status of the document.

        - **CreatedTimestamp** *(datetime) --*

          The timestamp when the document was first uploaded.

        - **ModifiedTimestamp** *(datetime) --*

          The timestamp when the document was last uploaded.

        - **ContentCreatedTimestamp** *(datetime) --*

          The timestamp when the content of the document was originally created.

        - **ContentModifiedTimestamp** *(datetime) --*

          The timestamp when the content of the document was modified.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **Thumbnail** *(dict) --*

          The thumbnail of the document.

          - *(string) --*

            - *(string) --*

        - **Source** *(dict) --*

          The source of the document.

          - *(string) --*

            - *(string) --*

    - **Marker** *(string) --*

      The marker to use when requesting the next set of results. If there are no additional
      results, the string is empty.
    """


_ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "_ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef(
    _ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef
):
    """
    Type definition for `ClientDescribeFolderContentsResponseDocuments` `LatestVersionMetadata`

    The latest version of the document.

    - **Id** *(string) --*

      The ID of the version.

    - **Name** *(string) --*

      The name of the version.

    - **ContentType** *(string) --*

      The content type of the document.

    - **Size** *(integer) --*

      The size of the document, in bytes.

    - **Signature** *(string) --*

      The signature of the document.

    - **Status** *(string) --*

      The status of the document.

    - **CreatedTimestamp** *(datetime) --*

      The timestamp when the document was first uploaded.

    - **ModifiedTimestamp** *(datetime) --*

      The timestamp when the document was last uploaded.

    - **ContentCreatedTimestamp** *(datetime) --*

      The timestamp when the content of the document was originally created.

    - **ContentModifiedTimestamp** *(datetime) --*

      The timestamp when the content of the document was modified.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **Thumbnail** *(dict) --*

      The thumbnail of the document.

      - *(string) --*

        - *(string) --*

    - **Source** *(dict) --*

      The source of the document.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeFolderContentsResponseDocumentsTypeDef = TypedDict(
    "_ClientDescribeFolderContentsResponseDocumentsTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef,
        "ResourceState": str,
        "Labels": List[str],
    },
    total=False,
)


class ClientDescribeFolderContentsResponseDocumentsTypeDef(
    _ClientDescribeFolderContentsResponseDocumentsTypeDef
):
    """
    Type definition for `ClientDescribeFolderContentsResponse` `Documents`

    Describes the document.

    - **Id** *(string) --*

      The ID of the document.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the document was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the document was updated.

    - **LatestVersionMetadata** *(dict) --*

      The latest version of the document.

      - **Id** *(string) --*

        The ID of the version.

      - **Name** *(string) --*

        The name of the version.

      - **ContentType** *(string) --*

        The content type of the document.

      - **Size** *(integer) --*

        The size of the document, in bytes.

      - **Signature** *(string) --*

        The signature of the document.

      - **Status** *(string) --*

        The status of the document.

      - **CreatedTimestamp** *(datetime) --*

        The timestamp when the document was first uploaded.

      - **ModifiedTimestamp** *(datetime) --*

        The timestamp when the document was last uploaded.

      - **ContentCreatedTimestamp** *(datetime) --*

        The timestamp when the content of the document was originally created.

      - **ContentModifiedTimestamp** *(datetime) --*

        The timestamp when the content of the document was modified.

      - **CreatorId** *(string) --*

        The ID of the creator.

      - **Thumbnail** *(dict) --*

        The thumbnail of the document.

        - *(string) --*

          - *(string) --*

      - **Source** *(dict) --*

        The source of the document.

        - *(string) --*

          - *(string) --*

    - **ResourceState** *(string) --*

      The resource state.

    - **Labels** *(list) --*

      List of labels on the document.

      - *(string) --*
    """


_ClientDescribeFolderContentsResponseFoldersTypeDef = TypedDict(
    "_ClientDescribeFolderContentsResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": str,
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class ClientDescribeFolderContentsResponseFoldersTypeDef(
    _ClientDescribeFolderContentsResponseFoldersTypeDef
):
    """
    Type definition for `ClientDescribeFolderContentsResponse` `Folders`

    Describes a folder.

    - **Id** *(string) --*

      The ID of the folder.

    - **Name** *(string) --*

      The name of the folder.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the folder was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the folder was updated.

    - **ResourceState** *(string) --*

      The resource state of the folder.

    - **Signature** *(string) --*

      The unique identifier created from the subfolders and documents of the folder.

    - **Labels** *(list) --*

      List of labels on the folder.

      - *(string) --*

    - **Size** *(integer) --*

      The size of the folder metadata.

    - **LatestVersionSize** *(integer) --*

      The size of the latest version of the folder metadata.
    """


_ClientDescribeFolderContentsResponseTypeDef = TypedDict(
    "_ClientDescribeFolderContentsResponseTypeDef",
    {
        "Folders": List[ClientDescribeFolderContentsResponseFoldersTypeDef],
        "Documents": List[ClientDescribeFolderContentsResponseDocumentsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeFolderContentsResponseTypeDef(
    _ClientDescribeFolderContentsResponseTypeDef
):
    """
    Type definition for `ClientDescribeFolderContents` `Response`

    - **Folders** *(list) --*

      The subfolders in the specified folder.

      - *(dict) --*

        Describes a folder.

        - **Id** *(string) --*

          The ID of the folder.

        - **Name** *(string) --*

          The name of the folder.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **ParentFolderId** *(string) --*

          The ID of the parent folder.

        - **CreatedTimestamp** *(datetime) --*

          The time when the folder was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the folder was updated.

        - **ResourceState** *(string) --*

          The resource state of the folder.

        - **Signature** *(string) --*

          The unique identifier created from the subfolders and documents of the folder.

        - **Labels** *(list) --*

          List of labels on the folder.

          - *(string) --*

        - **Size** *(integer) --*

          The size of the folder metadata.

        - **LatestVersionSize** *(integer) --*

          The size of the latest version of the folder metadata.

    - **Documents** *(list) --*

      The documents in the specified folder.

      - *(dict) --*

        Describes the document.

        - **Id** *(string) --*

          The ID of the document.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **ParentFolderId** *(string) --*

          The ID of the parent folder.

        - **CreatedTimestamp** *(datetime) --*

          The time when the document was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the document was updated.

        - **LatestVersionMetadata** *(dict) --*

          The latest version of the document.

          - **Id** *(string) --*

            The ID of the version.

          - **Name** *(string) --*

            The name of the version.

          - **ContentType** *(string) --*

            The content type of the document.

          - **Size** *(integer) --*

            The size of the document, in bytes.

          - **Signature** *(string) --*

            The signature of the document.

          - **Status** *(string) --*

            The status of the document.

          - **CreatedTimestamp** *(datetime) --*

            The timestamp when the document was first uploaded.

          - **ModifiedTimestamp** *(datetime) --*

            The timestamp when the document was last uploaded.

          - **ContentCreatedTimestamp** *(datetime) --*

            The timestamp when the content of the document was originally created.

          - **ContentModifiedTimestamp** *(datetime) --*

            The timestamp when the content of the document was modified.

          - **CreatorId** *(string) --*

            The ID of the creator.

          - **Thumbnail** *(dict) --*

            The thumbnail of the document.

            - *(string) --*

              - *(string) --*

          - **Source** *(dict) --*

            The source of the document.

            - *(string) --*

              - *(string) --*

        - **ResourceState** *(string) --*

          The resource state.

        - **Labels** *(list) --*

          List of labels on the document.

          - *(string) --*

    - **Marker** *(string) --*

      The marker to use when requesting the next set of results. If there are no additional
      results, the string is empty.
    """


_ClientDescribeGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientDescribeGroupsResponseGroupsTypeDef", {"Id": str, "Name": str}, total=False
)


class ClientDescribeGroupsResponseGroupsTypeDef(
    _ClientDescribeGroupsResponseGroupsTypeDef
):
    """
    Type definition for `ClientDescribeGroupsResponse` `Groups`

    Describes the metadata of a user group.

    - **Id** *(string) --*

      The ID of the user group.

    - **Name** *(string) --*

      The name of the group.
    """


_ClientDescribeGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeGroupsResponseTypeDef",
    {"Groups": List[ClientDescribeGroupsResponseGroupsTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeGroupsResponseTypeDef(_ClientDescribeGroupsResponseTypeDef):
    """
    Type definition for `ClientDescribeGroups` `Response`

    - **Groups** *(list) --*

      The list of groups.

      - *(dict) --*

        Describes the metadata of a user group.

        - **Id** *(string) --*

          The ID of the user group.

        - **Name** *(string) --*

          The name of the group.

    - **Marker** *(string) --*

      The marker to use when requesting the next set of results. If there are no additional
      results, the string is empty.
    """


_ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef = TypedDict(
    "_ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)


class ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef(
    _ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef
):
    """
    Type definition for `ClientDescribeNotificationSubscriptionsResponse` `Subscriptions`

    Describes a subscription.

    - **SubscriptionId** *(string) --*

      The ID of the subscription.

    - **EndPoint** *(string) --*

      The endpoint of the subscription.

    - **Protocol** *(string) --*

      The protocol of the subscription.
    """


_ClientDescribeNotificationSubscriptionsResponseTypeDef = TypedDict(
    "_ClientDescribeNotificationSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List[
            ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeNotificationSubscriptionsResponseTypeDef(
    _ClientDescribeNotificationSubscriptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeNotificationSubscriptions` `Response`

    - **Subscriptions** *(list) --*

      The subscriptions.

      - *(dict) --*

        Describes a subscription.

        - **SubscriptionId** *(string) --*

          The ID of the subscription.

        - **EndPoint** *(string) --*

          The endpoint of the subscription.

        - **Protocol** *(string) --*

          The protocol of the subscription.

    - **Marker** *(string) --*

      The marker to use when requesting the next set of results. If there are no additional
      results, the string is empty.
    """


_ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef = TypedDict(
    "_ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef",
    {"Role": str, "Type": str},
    total=False,
)


class ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef(
    _ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef
):
    """
    Type definition for `ClientDescribeResourcePermissionsResponsePrincipals` `Roles`

    Describes the permissions.

    - **Role** *(string) --*

      The role of the user.

    - **Type** *(string) --*

      The type of permissions.
    """


_ClientDescribeResourcePermissionsResponsePrincipalsTypeDef = TypedDict(
    "_ClientDescribeResourcePermissionsResponsePrincipalsTypeDef",
    {
        "Id": str,
        "Type": str,
        "Roles": List[ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef],
    },
    total=False,
)


class ClientDescribeResourcePermissionsResponsePrincipalsTypeDef(
    _ClientDescribeResourcePermissionsResponsePrincipalsTypeDef
):
    """
    Type definition for `ClientDescribeResourcePermissionsResponse` `Principals`

    Describes a resource.

    - **Id** *(string) --*

      The ID of the resource.

    - **Type** *(string) --*

      The type of resource.

    - **Roles** *(list) --*

      The permission information for the resource.

      - *(dict) --*

        Describes the permissions.

        - **Role** *(string) --*

          The role of the user.

        - **Type** *(string) --*

          The type of permissions.
    """


_ClientDescribeResourcePermissionsResponseTypeDef = TypedDict(
    "_ClientDescribeResourcePermissionsResponseTypeDef",
    {
        "Principals": List[ClientDescribeResourcePermissionsResponsePrincipalsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeResourcePermissionsResponseTypeDef(
    _ClientDescribeResourcePermissionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeResourcePermissions` `Response`

    - **Principals** *(list) --*

      The principals.

      - *(dict) --*

        Describes a resource.

        - **Id** *(string) --*

          The ID of the resource.

        - **Type** *(string) --*

          The type of resource.

        - **Roles** *(list) --*

          The permission information for the resource.

          - *(dict) --*

            Describes the permissions.

            - **Role** *(string) --*

              The role of the user.

            - **Type** *(string) --*

              The type of permissions.

    - **Marker** *(string) --*

      The marker to use when requesting the next set of results. If there are no additional
      results, the string is empty.
    """


_ClientDescribeRootFoldersResponseFoldersTypeDef = TypedDict(
    "_ClientDescribeRootFoldersResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": str,
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class ClientDescribeRootFoldersResponseFoldersTypeDef(
    _ClientDescribeRootFoldersResponseFoldersTypeDef
):
    """
    Type definition for `ClientDescribeRootFoldersResponse` `Folders`

    Describes a folder.

    - **Id** *(string) --*

      The ID of the folder.

    - **Name** *(string) --*

      The name of the folder.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the folder was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the folder was updated.

    - **ResourceState** *(string) --*

      The resource state of the folder.

    - **Signature** *(string) --*

      The unique identifier created from the subfolders and documents of the folder.

    - **Labels** *(list) --*

      List of labels on the folder.

      - *(string) --*

    - **Size** *(integer) --*

      The size of the folder metadata.

    - **LatestVersionSize** *(integer) --*

      The size of the latest version of the folder metadata.
    """


_ClientDescribeRootFoldersResponseTypeDef = TypedDict(
    "_ClientDescribeRootFoldersResponseTypeDef",
    {"Folders": List[ClientDescribeRootFoldersResponseFoldersTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeRootFoldersResponseTypeDef(
    _ClientDescribeRootFoldersResponseTypeDef
):
    """
    Type definition for `ClientDescribeRootFolders` `Response`

    - **Folders** *(list) --*

      The user's special folders.

      - *(dict) --*

        Describes a folder.

        - **Id** *(string) --*

          The ID of the folder.

        - **Name** *(string) --*

          The name of the folder.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **ParentFolderId** *(string) --*

          The ID of the parent folder.

        - **CreatedTimestamp** *(datetime) --*

          The time when the folder was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the folder was updated.

        - **ResourceState** *(string) --*

          The resource state of the folder.

        - **Signature** *(string) --*

          The unique identifier created from the subfolders and documents of the folder.

        - **Labels** *(list) --*

          List of labels on the folder.

          - *(string) --*

        - **Size** *(integer) --*

          The size of the folder metadata.

        - **LatestVersionSize** *(integer) --*

          The size of the latest version of the folder metadata.

    - **Marker** *(string) --*

      The marker for the next set of results.
    """


_ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef = TypedDict(
    "_ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef(
    _ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef
):
    """
    Type definition for `ClientDescribeUsersResponseUsersStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_ClientDescribeUsersResponseUsersStorageTypeDef = TypedDict(
    "_ClientDescribeUsersResponseUsersStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientDescribeUsersResponseUsersStorageTypeDef(
    _ClientDescribeUsersResponseUsersStorageTypeDef
):
    """
    Type definition for `ClientDescribeUsersResponseUsers` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_ClientDescribeUsersResponseUsersTypeDef = TypedDict(
    "_ClientDescribeUsersResponseUsersTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": ClientDescribeUsersResponseUsersStorageTypeDef,
    },
    total=False,
)


class ClientDescribeUsersResponseUsersTypeDef(_ClientDescribeUsersResponseUsersTypeDef):
    """
    Type definition for `ClientDescribeUsersResponse` `Users`

    Describes a user.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_ClientDescribeUsersResponseTypeDef = TypedDict(
    "_ClientDescribeUsersResponseTypeDef",
    {
        "Users": List[ClientDescribeUsersResponseUsersTypeDef],
        "TotalNumberOfUsers": int,
        "Marker": str,
    },
    total=False,
)


class ClientDescribeUsersResponseTypeDef(_ClientDescribeUsersResponseTypeDef):
    """
    Type definition for `ClientDescribeUsers` `Response`

    - **Users** *(list) --*

      The users.

      - *(dict) --*

        Describes a user.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The login name of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

        - **GivenName** *(string) --*

          The given name of the user.

        - **Surname** *(string) --*

          The surname of the user.

        - **OrganizationId** *(string) --*

          The ID of the organization.

        - **RootFolderId** *(string) --*

          The ID of the root folder.

        - **RecycleBinFolderId** *(string) --*

          The ID of the recycle bin folder.

        - **Status** *(string) --*

          The status of the user.

        - **Type** *(string) --*

          The type of user.

        - **CreatedTimestamp** *(datetime) --*

          The time when the user was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the user was modified.

        - **TimeZoneId** *(string) --*

          The time zone ID of the user.

        - **Locale** *(string) --*

          The locale of the user.

        - **Storage** *(dict) --*

          The storage for the user.

          - **StorageUtilizedInBytes** *(integer) --*

            The amount of storage used, in bytes.

          - **StorageRule** *(dict) --*

            The storage for a user.

            - **StorageAllocatedInBytes** *(integer) --*

              The amount of storage allocated, in bytes.

            - **StorageType** *(string) --*

              The type of storage.

    - **TotalNumberOfUsers** *(integer) --*

      The total number of users included in the results.

    - **Marker** *(string) --*

      The marker to use when requesting the next set of results. If there are no additional
      results, the string is empty.
    """


_ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "_ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef(
    _ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef
):
    """
    Type definition for `ClientGetCurrentUserResponseUserStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_ClientGetCurrentUserResponseUserStorageTypeDef = TypedDict(
    "_ClientGetCurrentUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientGetCurrentUserResponseUserStorageTypeDef(
    _ClientGetCurrentUserResponseUserStorageTypeDef
):
    """
    Type definition for `ClientGetCurrentUserResponseUser` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_ClientGetCurrentUserResponseUserTypeDef = TypedDict(
    "_ClientGetCurrentUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": ClientGetCurrentUserResponseUserStorageTypeDef,
    },
    total=False,
)


class ClientGetCurrentUserResponseUserTypeDef(_ClientGetCurrentUserResponseUserTypeDef):
    """
    Type definition for `ClientGetCurrentUserResponse` `User`

    Metadata of the user.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_ClientGetCurrentUserResponseTypeDef = TypedDict(
    "_ClientGetCurrentUserResponseTypeDef",
    {"User": ClientGetCurrentUserResponseUserTypeDef},
    total=False,
)


class ClientGetCurrentUserResponseTypeDef(_ClientGetCurrentUserResponseTypeDef):
    """
    Type definition for `ClientGetCurrentUser` `Response`

    - **User** *(dict) --*

      Metadata of the user.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The login name of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

      - **GivenName** *(string) --*

        The given name of the user.

      - **Surname** *(string) --*

        The surname of the user.

      - **OrganizationId** *(string) --*

        The ID of the organization.

      - **RootFolderId** *(string) --*

        The ID of the root folder.

      - **RecycleBinFolderId** *(string) --*

        The ID of the recycle bin folder.

      - **Status** *(string) --*

        The status of the user.

      - **Type** *(string) --*

        The type of user.

      - **CreatedTimestamp** *(datetime) --*

        The time when the user was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the user was modified.

      - **TimeZoneId** *(string) --*

        The time zone ID of the user.

      - **Locale** *(string) --*

        The locale of the user.

      - **Storage** *(dict) --*

        The storage for the user.

        - **StorageUtilizedInBytes** *(integer) --*

          The amount of storage used, in bytes.

        - **StorageRule** *(dict) --*

          The storage for a user.

          - **StorageAllocatedInBytes** *(integer) --*

            The amount of storage allocated, in bytes.

          - **StorageType** *(string) --*

            The type of storage.
    """


_ClientGetDocumentPathResponsePathComponentsTypeDef = TypedDict(
    "_ClientGetDocumentPathResponsePathComponentsTypeDef",
    {"Id": str, "Name": str},
    total=False,
)


class ClientGetDocumentPathResponsePathComponentsTypeDef(
    _ClientGetDocumentPathResponsePathComponentsTypeDef
):
    """
    Type definition for `ClientGetDocumentPathResponsePath` `Components`

    Describes the resource path.

    - **Id** *(string) --*

      The ID of the resource path.

    - **Name** *(string) --*

      The name of the resource path.
    """


_ClientGetDocumentPathResponsePathTypeDef = TypedDict(
    "_ClientGetDocumentPathResponsePathTypeDef",
    {"Components": List[ClientGetDocumentPathResponsePathComponentsTypeDef]},
    total=False,
)


class ClientGetDocumentPathResponsePathTypeDef(
    _ClientGetDocumentPathResponsePathTypeDef
):
    """
    Type definition for `ClientGetDocumentPathResponse` `Path`

    The path information.

    - **Components** *(list) --*

      The components of the resource path.

      - *(dict) --*

        Describes the resource path.

        - **Id** *(string) --*

          The ID of the resource path.

        - **Name** *(string) --*

          The name of the resource path.
    """


_ClientGetDocumentPathResponseTypeDef = TypedDict(
    "_ClientGetDocumentPathResponseTypeDef",
    {"Path": ClientGetDocumentPathResponsePathTypeDef},
    total=False,
)


class ClientGetDocumentPathResponseTypeDef(_ClientGetDocumentPathResponseTypeDef):
    """
    Type definition for `ClientGetDocumentPath` `Response`

    - **Path** *(dict) --*

      The path information.

      - **Components** *(list) --*

        The components of the resource path.

        - *(dict) --*

          Describes the resource path.

          - **Id** *(string) --*

            The ID of the resource path.

          - **Name** *(string) --*

            The name of the resource path.
    """


_ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef = TypedDict(
    "_ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef(
    _ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef
):
    """
    Type definition for `ClientGetDocumentResponseMetadata` `LatestVersionMetadata`

    The latest version of the document.

    - **Id** *(string) --*

      The ID of the version.

    - **Name** *(string) --*

      The name of the version.

    - **ContentType** *(string) --*

      The content type of the document.

    - **Size** *(integer) --*

      The size of the document, in bytes.

    - **Signature** *(string) --*

      The signature of the document.

    - **Status** *(string) --*

      The status of the document.

    - **CreatedTimestamp** *(datetime) --*

      The timestamp when the document was first uploaded.

    - **ModifiedTimestamp** *(datetime) --*

      The timestamp when the document was last uploaded.

    - **ContentCreatedTimestamp** *(datetime) --*

      The timestamp when the content of the document was originally created.

    - **ContentModifiedTimestamp** *(datetime) --*

      The timestamp when the content of the document was modified.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **Thumbnail** *(dict) --*

      The thumbnail of the document.

      - *(string) --*

        - *(string) --*

    - **Source** *(dict) --*

      The source of the document.

      - *(string) --*

        - *(string) --*
    """


_ClientGetDocumentResponseMetadataTypeDef = TypedDict(
    "_ClientGetDocumentResponseMetadataTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef,
        "ResourceState": str,
        "Labels": List[str],
    },
    total=False,
)


class ClientGetDocumentResponseMetadataTypeDef(
    _ClientGetDocumentResponseMetadataTypeDef
):
    """
    Type definition for `ClientGetDocumentResponse` `Metadata`

    The metadata details of the document.

    - **Id** *(string) --*

      The ID of the document.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the document was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the document was updated.

    - **LatestVersionMetadata** *(dict) --*

      The latest version of the document.

      - **Id** *(string) --*

        The ID of the version.

      - **Name** *(string) --*

        The name of the version.

      - **ContentType** *(string) --*

        The content type of the document.

      - **Size** *(integer) --*

        The size of the document, in bytes.

      - **Signature** *(string) --*

        The signature of the document.

      - **Status** *(string) --*

        The status of the document.

      - **CreatedTimestamp** *(datetime) --*

        The timestamp when the document was first uploaded.

      - **ModifiedTimestamp** *(datetime) --*

        The timestamp when the document was last uploaded.

      - **ContentCreatedTimestamp** *(datetime) --*

        The timestamp when the content of the document was originally created.

      - **ContentModifiedTimestamp** *(datetime) --*

        The timestamp when the content of the document was modified.

      - **CreatorId** *(string) --*

        The ID of the creator.

      - **Thumbnail** *(dict) --*

        The thumbnail of the document.

        - *(string) --*

          - *(string) --*

      - **Source** *(dict) --*

        The source of the document.

        - *(string) --*

          - *(string) --*

    - **ResourceState** *(string) --*

      The resource state.

    - **Labels** *(list) --*

      List of labels on the document.

      - *(string) --*
    """


_ClientGetDocumentResponseTypeDef = TypedDict(
    "_ClientGetDocumentResponseTypeDef",
    {
        "Metadata": ClientGetDocumentResponseMetadataTypeDef,
        "CustomMetadata": Dict[str, str],
    },
    total=False,
)


class ClientGetDocumentResponseTypeDef(_ClientGetDocumentResponseTypeDef):
    """
    Type definition for `ClientGetDocument` `Response`

    - **Metadata** *(dict) --*

      The metadata details of the document.

      - **Id** *(string) --*

        The ID of the document.

      - **CreatorId** *(string) --*

        The ID of the creator.

      - **ParentFolderId** *(string) --*

        The ID of the parent folder.

      - **CreatedTimestamp** *(datetime) --*

        The time when the document was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the document was updated.

      - **LatestVersionMetadata** *(dict) --*

        The latest version of the document.

        - **Id** *(string) --*

          The ID of the version.

        - **Name** *(string) --*

          The name of the version.

        - **ContentType** *(string) --*

          The content type of the document.

        - **Size** *(integer) --*

          The size of the document, in bytes.

        - **Signature** *(string) --*

          The signature of the document.

        - **Status** *(string) --*

          The status of the document.

        - **CreatedTimestamp** *(datetime) --*

          The timestamp when the document was first uploaded.

        - **ModifiedTimestamp** *(datetime) --*

          The timestamp when the document was last uploaded.

        - **ContentCreatedTimestamp** *(datetime) --*

          The timestamp when the content of the document was originally created.

        - **ContentModifiedTimestamp** *(datetime) --*

          The timestamp when the content of the document was modified.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **Thumbnail** *(dict) --*

          The thumbnail of the document.

          - *(string) --*

            - *(string) --*

        - **Source** *(dict) --*

          The source of the document.

          - *(string) --*

            - *(string) --*

      - **ResourceState** *(string) --*

        The resource state.

      - **Labels** *(list) --*

        List of labels on the document.

        - *(string) --*

    - **CustomMetadata** *(dict) --*

      The custom metadata on the document.

      - *(string) --*

        - *(string) --*
    """


_ClientGetDocumentVersionResponseMetadataTypeDef = TypedDict(
    "_ClientGetDocumentVersionResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientGetDocumentVersionResponseMetadataTypeDef(
    _ClientGetDocumentVersionResponseMetadataTypeDef
):
    """
    Type definition for `ClientGetDocumentVersionResponse` `Metadata`

    The version metadata.

    - **Id** *(string) --*

      The ID of the version.

    - **Name** *(string) --*

      The name of the version.

    - **ContentType** *(string) --*

      The content type of the document.

    - **Size** *(integer) --*

      The size of the document, in bytes.

    - **Signature** *(string) --*

      The signature of the document.

    - **Status** *(string) --*

      The status of the document.

    - **CreatedTimestamp** *(datetime) --*

      The timestamp when the document was first uploaded.

    - **ModifiedTimestamp** *(datetime) --*

      The timestamp when the document was last uploaded.

    - **ContentCreatedTimestamp** *(datetime) --*

      The timestamp when the content of the document was originally created.

    - **ContentModifiedTimestamp** *(datetime) --*

      The timestamp when the content of the document was modified.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **Thumbnail** *(dict) --*

      The thumbnail of the document.

      - *(string) --*

        - *(string) --*

    - **Source** *(dict) --*

      The source of the document.

      - *(string) --*

        - *(string) --*
    """


_ClientGetDocumentVersionResponseTypeDef = TypedDict(
    "_ClientGetDocumentVersionResponseTypeDef",
    {
        "Metadata": ClientGetDocumentVersionResponseMetadataTypeDef,
        "CustomMetadata": Dict[str, str],
    },
    total=False,
)


class ClientGetDocumentVersionResponseTypeDef(_ClientGetDocumentVersionResponseTypeDef):
    """
    Type definition for `ClientGetDocumentVersion` `Response`

    - **Metadata** *(dict) --*

      The version metadata.

      - **Id** *(string) --*

        The ID of the version.

      - **Name** *(string) --*

        The name of the version.

      - **ContentType** *(string) --*

        The content type of the document.

      - **Size** *(integer) --*

        The size of the document, in bytes.

      - **Signature** *(string) --*

        The signature of the document.

      - **Status** *(string) --*

        The status of the document.

      - **CreatedTimestamp** *(datetime) --*

        The timestamp when the document was first uploaded.

      - **ModifiedTimestamp** *(datetime) --*

        The timestamp when the document was last uploaded.

      - **ContentCreatedTimestamp** *(datetime) --*

        The timestamp when the content of the document was originally created.

      - **ContentModifiedTimestamp** *(datetime) --*

        The timestamp when the content of the document was modified.

      - **CreatorId** *(string) --*

        The ID of the creator.

      - **Thumbnail** *(dict) --*

        The thumbnail of the document.

        - *(string) --*

          - *(string) --*

      - **Source** *(dict) --*

        The source of the document.

        - *(string) --*

          - *(string) --*

    - **CustomMetadata** *(dict) --*

      The custom metadata on the document version.

      - *(string) --*

        - *(string) --*
    """


_ClientGetFolderPathResponsePathComponentsTypeDef = TypedDict(
    "_ClientGetFolderPathResponsePathComponentsTypeDef",
    {"Id": str, "Name": str},
    total=False,
)


class ClientGetFolderPathResponsePathComponentsTypeDef(
    _ClientGetFolderPathResponsePathComponentsTypeDef
):
    """
    Type definition for `ClientGetFolderPathResponsePath` `Components`

    Describes the resource path.

    - **Id** *(string) --*

      The ID of the resource path.

    - **Name** *(string) --*

      The name of the resource path.
    """


_ClientGetFolderPathResponsePathTypeDef = TypedDict(
    "_ClientGetFolderPathResponsePathTypeDef",
    {"Components": List[ClientGetFolderPathResponsePathComponentsTypeDef]},
    total=False,
)


class ClientGetFolderPathResponsePathTypeDef(_ClientGetFolderPathResponsePathTypeDef):
    """
    Type definition for `ClientGetFolderPathResponse` `Path`

    The path information.

    - **Components** *(list) --*

      The components of the resource path.

      - *(dict) --*

        Describes the resource path.

        - **Id** *(string) --*

          The ID of the resource path.

        - **Name** *(string) --*

          The name of the resource path.
    """


_ClientGetFolderPathResponseTypeDef = TypedDict(
    "_ClientGetFolderPathResponseTypeDef",
    {"Path": ClientGetFolderPathResponsePathTypeDef},
    total=False,
)


class ClientGetFolderPathResponseTypeDef(_ClientGetFolderPathResponseTypeDef):
    """
    Type definition for `ClientGetFolderPath` `Response`

    - **Path** *(dict) --*

      The path information.

      - **Components** *(list) --*

        The components of the resource path.

        - *(dict) --*

          Describes the resource path.

          - **Id** *(string) --*

            The ID of the resource path.

          - **Name** *(string) --*

            The name of the resource path.
    """


_ClientGetFolderResponseMetadataTypeDef = TypedDict(
    "_ClientGetFolderResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": str,
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class ClientGetFolderResponseMetadataTypeDef(_ClientGetFolderResponseMetadataTypeDef):
    """
    Type definition for `ClientGetFolderResponse` `Metadata`

    The metadata of the folder.

    - **Id** *(string) --*

      The ID of the folder.

    - **Name** *(string) --*

      The name of the folder.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the folder was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the folder was updated.

    - **ResourceState** *(string) --*

      The resource state of the folder.

    - **Signature** *(string) --*

      The unique identifier created from the subfolders and documents of the folder.

    - **Labels** *(list) --*

      List of labels on the folder.

      - *(string) --*

    - **Size** *(integer) --*

      The size of the folder metadata.

    - **LatestVersionSize** *(integer) --*

      The size of the latest version of the folder metadata.
    """


_ClientGetFolderResponseTypeDef = TypedDict(
    "_ClientGetFolderResponseTypeDef",
    {
        "Metadata": ClientGetFolderResponseMetadataTypeDef,
        "CustomMetadata": Dict[str, str],
    },
    total=False,
)


class ClientGetFolderResponseTypeDef(_ClientGetFolderResponseTypeDef):
    """
    Type definition for `ClientGetFolder` `Response`

    - **Metadata** *(dict) --*

      The metadata of the folder.

      - **Id** *(string) --*

        The ID of the folder.

      - **Name** *(string) --*

        The name of the folder.

      - **CreatorId** *(string) --*

        The ID of the creator.

      - **ParentFolderId** *(string) --*

        The ID of the parent folder.

      - **CreatedTimestamp** *(datetime) --*

        The time when the folder was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the folder was updated.

      - **ResourceState** *(string) --*

        The resource state of the folder.

      - **Signature** *(string) --*

        The unique identifier created from the subfolders and documents of the folder.

      - **Labels** *(list) --*

        List of labels on the folder.

        - *(string) --*

      - **Size** *(integer) --*

        The size of the folder metadata.

      - **LatestVersionSize** *(integer) --*

        The size of the latest version of the folder metadata.

    - **CustomMetadata** *(dict) --*

      The custom metadata on the folder.

      - *(string) --*

        - *(string) --*
    """


_ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "_ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef(
    _ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef
):
    """
    Type definition for `ClientGetResourcesResponseDocuments` `LatestVersionMetadata`

    The latest version of the document.

    - **Id** *(string) --*

      The ID of the version.

    - **Name** *(string) --*

      The name of the version.

    - **ContentType** *(string) --*

      The content type of the document.

    - **Size** *(integer) --*

      The size of the document, in bytes.

    - **Signature** *(string) --*

      The signature of the document.

    - **Status** *(string) --*

      The status of the document.

    - **CreatedTimestamp** *(datetime) --*

      The timestamp when the document was first uploaded.

    - **ModifiedTimestamp** *(datetime) --*

      The timestamp when the document was last uploaded.

    - **ContentCreatedTimestamp** *(datetime) --*

      The timestamp when the content of the document was originally created.

    - **ContentModifiedTimestamp** *(datetime) --*

      The timestamp when the content of the document was modified.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **Thumbnail** *(dict) --*

      The thumbnail of the document.

      - *(string) --*

        - *(string) --*

    - **Source** *(dict) --*

      The source of the document.

      - *(string) --*

        - *(string) --*
    """


_ClientGetResourcesResponseDocumentsTypeDef = TypedDict(
    "_ClientGetResourcesResponseDocumentsTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef,
        "ResourceState": str,
        "Labels": List[str],
    },
    total=False,
)


class ClientGetResourcesResponseDocumentsTypeDef(
    _ClientGetResourcesResponseDocumentsTypeDef
):
    """
    Type definition for `ClientGetResourcesResponse` `Documents`

    Describes the document.

    - **Id** *(string) --*

      The ID of the document.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the document was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the document was updated.

    - **LatestVersionMetadata** *(dict) --*

      The latest version of the document.

      - **Id** *(string) --*

        The ID of the version.

      - **Name** *(string) --*

        The name of the version.

      - **ContentType** *(string) --*

        The content type of the document.

      - **Size** *(integer) --*

        The size of the document, in bytes.

      - **Signature** *(string) --*

        The signature of the document.

      - **Status** *(string) --*

        The status of the document.

      - **CreatedTimestamp** *(datetime) --*

        The timestamp when the document was first uploaded.

      - **ModifiedTimestamp** *(datetime) --*

        The timestamp when the document was last uploaded.

      - **ContentCreatedTimestamp** *(datetime) --*

        The timestamp when the content of the document was originally created.

      - **ContentModifiedTimestamp** *(datetime) --*

        The timestamp when the content of the document was modified.

      - **CreatorId** *(string) --*

        The ID of the creator.

      - **Thumbnail** *(dict) --*

        The thumbnail of the document.

        - *(string) --*

          - *(string) --*

      - **Source** *(dict) --*

        The source of the document.

        - *(string) --*

          - *(string) --*

    - **ResourceState** *(string) --*

      The resource state.

    - **Labels** *(list) --*

      List of labels on the document.

      - *(string) --*
    """


_ClientGetResourcesResponseFoldersTypeDef = TypedDict(
    "_ClientGetResourcesResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": str,
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class ClientGetResourcesResponseFoldersTypeDef(
    _ClientGetResourcesResponseFoldersTypeDef
):
    """
    Type definition for `ClientGetResourcesResponse` `Folders`

    Describes a folder.

    - **Id** *(string) --*

      The ID of the folder.

    - **Name** *(string) --*

      The name of the folder.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the folder was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the folder was updated.

    - **ResourceState** *(string) --*

      The resource state of the folder.

    - **Signature** *(string) --*

      The unique identifier created from the subfolders and documents of the folder.

    - **Labels** *(list) --*

      List of labels on the folder.

      - *(string) --*

    - **Size** *(integer) --*

      The size of the folder metadata.

    - **LatestVersionSize** *(integer) --*

      The size of the latest version of the folder metadata.
    """


_ClientGetResourcesResponseTypeDef = TypedDict(
    "_ClientGetResourcesResponseTypeDef",
    {
        "Folders": List[ClientGetResourcesResponseFoldersTypeDef],
        "Documents": List[ClientGetResourcesResponseDocumentsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientGetResourcesResponseTypeDef(_ClientGetResourcesResponseTypeDef):
    """
    Type definition for `ClientGetResources` `Response`

    - **Folders** *(list) --*

      The folders in the specified folder.

      - *(dict) --*

        Describes a folder.

        - **Id** *(string) --*

          The ID of the folder.

        - **Name** *(string) --*

          The name of the folder.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **ParentFolderId** *(string) --*

          The ID of the parent folder.

        - **CreatedTimestamp** *(datetime) --*

          The time when the folder was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the folder was updated.

        - **ResourceState** *(string) --*

          The resource state of the folder.

        - **Signature** *(string) --*

          The unique identifier created from the subfolders and documents of the folder.

        - **Labels** *(list) --*

          List of labels on the folder.

          - *(string) --*

        - **Size** *(integer) --*

          The size of the folder metadata.

        - **LatestVersionSize** *(integer) --*

          The size of the latest version of the folder metadata.

    - **Documents** *(list) --*

      The documents in the specified collection.

      - *(dict) --*

        Describes the document.

        - **Id** *(string) --*

          The ID of the document.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **ParentFolderId** *(string) --*

          The ID of the parent folder.

        - **CreatedTimestamp** *(datetime) --*

          The time when the document was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the document was updated.

        - **LatestVersionMetadata** *(dict) --*

          The latest version of the document.

          - **Id** *(string) --*

            The ID of the version.

          - **Name** *(string) --*

            The name of the version.

          - **ContentType** *(string) --*

            The content type of the document.

          - **Size** *(integer) --*

            The size of the document, in bytes.

          - **Signature** *(string) --*

            The signature of the document.

          - **Status** *(string) --*

            The status of the document.

          - **CreatedTimestamp** *(datetime) --*

            The timestamp when the document was first uploaded.

          - **ModifiedTimestamp** *(datetime) --*

            The timestamp when the document was last uploaded.

          - **ContentCreatedTimestamp** *(datetime) --*

            The timestamp when the content of the document was originally created.

          - **ContentModifiedTimestamp** *(datetime) --*

            The timestamp when the content of the document was modified.

          - **CreatorId** *(string) --*

            The ID of the creator.

          - **Thumbnail** *(dict) --*

            The thumbnail of the document.

            - *(string) --*

              - *(string) --*

          - **Source** *(dict) --*

            The source of the document.

            - *(string) --*

              - *(string) --*

        - **ResourceState** *(string) --*

          The resource state.

        - **Labels** *(list) --*

          List of labels on the document.

          - *(string) --*

    - **Marker** *(string) --*

      The marker to use when requesting the next set of results. If there are no additional
      results, the string is empty.
    """


_ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef = TypedDict(
    "_ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef(
    _ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef
):
    """
    Type definition for `ClientInitiateDocumentVersionUploadResponseMetadata` `LatestVersionMetadata`

    The latest version of the document.

    - **Id** *(string) --*

      The ID of the version.

    - **Name** *(string) --*

      The name of the version.

    - **ContentType** *(string) --*

      The content type of the document.

    - **Size** *(integer) --*

      The size of the document, in bytes.

    - **Signature** *(string) --*

      The signature of the document.

    - **Status** *(string) --*

      The status of the document.

    - **CreatedTimestamp** *(datetime) --*

      The timestamp when the document was first uploaded.

    - **ModifiedTimestamp** *(datetime) --*

      The timestamp when the document was last uploaded.

    - **ContentCreatedTimestamp** *(datetime) --*

      The timestamp when the content of the document was originally created.

    - **ContentModifiedTimestamp** *(datetime) --*

      The timestamp when the content of the document was modified.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **Thumbnail** *(dict) --*

      The thumbnail of the document.

      - *(string) --*

        - *(string) --*

    - **Source** *(dict) --*

      The source of the document.

      - *(string) --*

        - *(string) --*
    """


_ClientInitiateDocumentVersionUploadResponseMetadataTypeDef = TypedDict(
    "_ClientInitiateDocumentVersionUploadResponseMetadataTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef,
        "ResourceState": str,
        "Labels": List[str],
    },
    total=False,
)


class ClientInitiateDocumentVersionUploadResponseMetadataTypeDef(
    _ClientInitiateDocumentVersionUploadResponseMetadataTypeDef
):
    """
    Type definition for `ClientInitiateDocumentVersionUploadResponse` `Metadata`

    The document metadata.

    - **Id** *(string) --*

      The ID of the document.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the document was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the document was updated.

    - **LatestVersionMetadata** *(dict) --*

      The latest version of the document.

      - **Id** *(string) --*

        The ID of the version.

      - **Name** *(string) --*

        The name of the version.

      - **ContentType** *(string) --*

        The content type of the document.

      - **Size** *(integer) --*

        The size of the document, in bytes.

      - **Signature** *(string) --*

        The signature of the document.

      - **Status** *(string) --*

        The status of the document.

      - **CreatedTimestamp** *(datetime) --*

        The timestamp when the document was first uploaded.

      - **ModifiedTimestamp** *(datetime) --*

        The timestamp when the document was last uploaded.

      - **ContentCreatedTimestamp** *(datetime) --*

        The timestamp when the content of the document was originally created.

      - **ContentModifiedTimestamp** *(datetime) --*

        The timestamp when the content of the document was modified.

      - **CreatorId** *(string) --*

        The ID of the creator.

      - **Thumbnail** *(dict) --*

        The thumbnail of the document.

        - *(string) --*

          - *(string) --*

      - **Source** *(dict) --*

        The source of the document.

        - *(string) --*

          - *(string) --*

    - **ResourceState** *(string) --*

      The resource state.

    - **Labels** *(list) --*

      List of labels on the document.

      - *(string) --*
    """


_ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef = TypedDict(
    "_ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef",
    {"UploadUrl": str, "SignedHeaders": Dict[str, str]},
    total=False,
)


class ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef(
    _ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef
):
    """
    Type definition for `ClientInitiateDocumentVersionUploadResponse` `UploadMetadata`

    The upload metadata.

    - **UploadUrl** *(string) --*

      The URL of the upload.

    - **SignedHeaders** *(dict) --*

      The signed headers.

      - *(string) --*

        - *(string) --*
    """


_ClientInitiateDocumentVersionUploadResponseTypeDef = TypedDict(
    "_ClientInitiateDocumentVersionUploadResponseTypeDef",
    {
        "Metadata": ClientInitiateDocumentVersionUploadResponseMetadataTypeDef,
        "UploadMetadata": ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef,
    },
    total=False,
)


class ClientInitiateDocumentVersionUploadResponseTypeDef(
    _ClientInitiateDocumentVersionUploadResponseTypeDef
):
    """
    Type definition for `ClientInitiateDocumentVersionUpload` `Response`

    - **Metadata** *(dict) --*

      The document metadata.

      - **Id** *(string) --*

        The ID of the document.

      - **CreatorId** *(string) --*

        The ID of the creator.

      - **ParentFolderId** *(string) --*

        The ID of the parent folder.

      - **CreatedTimestamp** *(datetime) --*

        The time when the document was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the document was updated.

      - **LatestVersionMetadata** *(dict) --*

        The latest version of the document.

        - **Id** *(string) --*

          The ID of the version.

        - **Name** *(string) --*

          The name of the version.

        - **ContentType** *(string) --*

          The content type of the document.

        - **Size** *(integer) --*

          The size of the document, in bytes.

        - **Signature** *(string) --*

          The signature of the document.

        - **Status** *(string) --*

          The status of the document.

        - **CreatedTimestamp** *(datetime) --*

          The timestamp when the document was first uploaded.

        - **ModifiedTimestamp** *(datetime) --*

          The timestamp when the document was last uploaded.

        - **ContentCreatedTimestamp** *(datetime) --*

          The timestamp when the content of the document was originally created.

        - **ContentModifiedTimestamp** *(datetime) --*

          The timestamp when the content of the document was modified.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **Thumbnail** *(dict) --*

          The thumbnail of the document.

          - *(string) --*

            - *(string) --*

        - **Source** *(dict) --*

          The source of the document.

          - *(string) --*

            - *(string) --*

      - **ResourceState** *(string) --*

        The resource state.

      - **Labels** *(list) --*

        List of labels on the document.

        - *(string) --*

    - **UploadMetadata** *(dict) --*

      The upload metadata.

      - **UploadUrl** *(string) --*

        The URL of the upload.

      - **SignedHeaders** *(dict) --*

        The signed headers.

        - *(string) --*

          - *(string) --*
    """


_ClientUpdateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "_ClientUpdateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class ClientUpdateUserResponseUserStorageStorageRuleTypeDef(
    _ClientUpdateUserResponseUserStorageStorageRuleTypeDef
):
    """
    Type definition for `ClientUpdateUserResponseUserStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_ClientUpdateUserResponseUserStorageTypeDef = TypedDict(
    "_ClientUpdateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientUpdateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientUpdateUserResponseUserStorageTypeDef(
    _ClientUpdateUserResponseUserStorageTypeDef
):
    """
    Type definition for `ClientUpdateUserResponseUser` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_ClientUpdateUserResponseUserTypeDef = TypedDict(
    "_ClientUpdateUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": ClientUpdateUserResponseUserStorageTypeDef,
    },
    total=False,
)


class ClientUpdateUserResponseUserTypeDef(_ClientUpdateUserResponseUserTypeDef):
    """
    Type definition for `ClientUpdateUserResponse` `User`

    The user information.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_ClientUpdateUserResponseTypeDef = TypedDict(
    "_ClientUpdateUserResponseTypeDef",
    {"User": ClientUpdateUserResponseUserTypeDef},
    total=False,
)


class ClientUpdateUserResponseTypeDef(_ClientUpdateUserResponseTypeDef):
    """
    Type definition for `ClientUpdateUser` `Response`

    - **User** *(dict) --*

      The user information.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The login name of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

      - **GivenName** *(string) --*

        The given name of the user.

      - **Surname** *(string) --*

        The surname of the user.

      - **OrganizationId** *(string) --*

        The ID of the organization.

      - **RootFolderId** *(string) --*

        The ID of the root folder.

      - **RecycleBinFolderId** *(string) --*

        The ID of the recycle bin folder.

      - **Status** *(string) --*

        The status of the user.

      - **Type** *(string) --*

        The type of user.

      - **CreatedTimestamp** *(datetime) --*

        The time when the user was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the user was modified.

      - **TimeZoneId** *(string) --*

        The time zone ID of the user.

      - **Locale** *(string) --*

        The locale of the user.

      - **Storage** *(dict) --*

        The storage for the user.

        - **StorageUtilizedInBytes** *(integer) --*

          The amount of storage used, in bytes.

        - **StorageRule** *(dict) --*

          The storage for a user.

          - **StorageAllocatedInBytes** *(integer) --*

            The amount of storage allocated, in bytes.

          - **StorageType** *(string) --*

            The type of storage.
    """


_ClientUpdateUserStorageRuleTypeDef = TypedDict(
    "_ClientUpdateUserStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class ClientUpdateUserStorageRuleTypeDef(_ClientUpdateUserStorageRuleTypeDef):
    """
    Type definition for `ClientUpdateUser` `StorageRule`

    The amount of storage for the user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_DescribeActivitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeActivitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeActivitiesPaginatePaginationConfigTypeDef(
    _DescribeActivitiesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributor` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivitiesCommentMetadata` `Contributor`

    The user who made the comment.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef",
    {
        "CommentId": str,
        "Contributor": DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef,
        "CreatedTimestamp": datetime,
        "CommentStatus": str,
        "RecipientId": str,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivities` `CommentMetadata`

    Metadata of the commenting activity. This is an optional field and is filled for
    commenting activities.

    - **CommentId** *(string) --*

      The ID of the comment.

    - **Contributor** *(dict) --*

      The user who made the comment.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The login name of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

      - **GivenName** *(string) --*

        The given name of the user.

      - **Surname** *(string) --*

        The surname of the user.

      - **OrganizationId** *(string) --*

        The ID of the organization.

      - **RootFolderId** *(string) --*

        The ID of the root folder.

      - **RecycleBinFolderId** *(string) --*

        The ID of the recycle bin folder.

      - **Status** *(string) --*

        The status of the user.

      - **Type** *(string) --*

        The type of user.

      - **CreatedTimestamp** *(datetime) --*

        The time when the user was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the user was modified.

      - **TimeZoneId** *(string) --*

        The time zone ID of the user.

      - **Locale** *(string) --*

        The locale of the user.

      - **Storage** *(dict) --*

        The storage for the user.

        - **StorageUtilizedInBytes** *(integer) --*

          The amount of storage used, in bytes.

        - **StorageRule** *(dict) --*

          The storage for a user.

          - **StorageAllocatedInBytes** *(integer) --*

            The amount of storage allocated, in bytes.

          - **StorageType** *(string) --*

            The type of storage.

    - **CreatedTimestamp** *(datetime) --*

      The timestamp that the comment was created.

    - **CommentStatus** *(string) --*

      The status of the comment.

    - **RecipientId** *(string) --*

      The ID of the user being replied to.
    """


_DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivities` `Initiator`

    The user who performed the action.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The name of the user.

    - **GivenName** *(string) --*

      The given name of the user before a rename operation.

    - **Surname** *(string) --*

      The surname of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.
    """


_DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivitiesOriginalParent` `Owner`

    The owner of the resource.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The name of the user.

    - **GivenName** *(string) --*

      The given name of the user before a rename operation.

    - **Surname** *(string) --*

      The surname of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.
    """


_DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef",
    {
        "Type": str,
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef,
        "ParentId": str,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivities` `OriginalParent`

    The original parent of the resource. This is an optional field and is filled for move
    activities.

    - **Type** *(string) --*

      The type of resource.

    - **Name** *(string) --*

      The name of the resource.

    - **OriginalName** *(string) --*

      The original name of the resource before a rename operation.

    - **Id** *(string) --*

      The ID of the resource.

    - **VersionId** *(string) --*

      The version ID of the resource. This is an optional field and is filled for action on
      document version.

    - **Owner** *(dict) --*

      The owner of the resource.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The name of the user.

      - **GivenName** *(string) --*

        The given name of the user before a rename operation.

      - **Surname** *(string) --*

        The surname of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

    - **ParentId** *(string) --*

      The parent ID of the resource before a rename operation.
    """


_DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef",
    {"Id": str, "Name": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivitiesParticipants` `Groups`

    Describes the metadata of a user group.

    - **Id** *(string) --*

      The ID of the user group.

    - **Name** *(string) --*

      The name of the group.
    """


_DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivitiesParticipants` `Users`

    Describes the metadata of the user.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The name of the user.

    - **GivenName** *(string) --*

      The given name of the user before a rename operation.

    - **Surname** *(string) --*

      The surname of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.
    """


_DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef",
    {
        "Users": List[
            DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef
        ],
        "Groups": List[
            DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef
        ],
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivities` `Participants`

    The list of users or groups impacted by this action. This is an optional field and is
    filled for the following sharing activities: DOCUMENT_SHARED, DOCUMENT_SHARED,
    DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.

    - **Users** *(list) --*

      The list of users.

      - *(dict) --*

        Describes the metadata of the user.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The name of the user.

        - **GivenName** *(string) --*

          The given name of the user before a rename operation.

        - **Surname** *(string) --*

          The surname of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

    - **Groups** *(list) --*

      The list of user groups.

      - *(dict) --*

        Describes the metadata of a user group.

        - **Id** *(string) --*

          The ID of the user group.

        - **Name** *(string) --*

          The name of the group.
    """


_DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivitiesResourceMetadata` `Owner`

    The owner of the resource.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The name of the user.

    - **GivenName** *(string) --*

      The given name of the user before a rename operation.

    - **Surname** *(string) --*

      The surname of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.
    """


_DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef",
    {
        "Type": str,
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef,
        "ParentId": str,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponseUserActivities` `ResourceMetadata`

    The metadata of the resource involved in the user action.

    - **Type** *(string) --*

      The type of resource.

    - **Name** *(string) --*

      The name of the resource.

    - **OriginalName** *(string) --*

      The original name of the resource before a rename operation.

    - **Id** *(string) --*

      The ID of the resource.

    - **VersionId** *(string) --*

      The version ID of the resource. This is an optional field and is filled for action on
      document version.

    - **Owner** *(dict) --*

      The owner of the resource.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The name of the user.

      - **GivenName** *(string) --*

        The given name of the user before a rename operation.

      - **Surname** *(string) --*

        The surname of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

    - **ParentId** *(string) --*

      The parent ID of the resource before a rename operation.
    """


_DescribeActivitiesPaginateResponseUserActivitiesTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesTypeDef",
    {
        "Type": str,
        "TimeStamp": datetime,
        "IsIndirectActivity": bool,
        "OrganizationId": str,
        "Initiator": DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef,
        "Participants": DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef,
        "ResourceMetadata": DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef,
        "OriginalParent": DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef,
        "CommentMetadata": DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginateResponse` `UserActivities`

    Describes the activity information.

    - **Type** *(string) --*

      The activity type.

    - **TimeStamp** *(datetime) --*

      The timestamp when the action was performed.

    - **IsIndirectActivity** *(boolean) --*

      Indicates whether an activity is indirect or direct. An indirect activity results from a
      direct activity performed on a parent resource. For example, sharing a parent folder (the
      direct activity) shares all of the subfolders and documents within the parent folder (the
      indirect activity).

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **Initiator** *(dict) --*

      The user who performed the action.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The name of the user.

      - **GivenName** *(string) --*

        The given name of the user before a rename operation.

      - **Surname** *(string) --*

        The surname of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

    - **Participants** *(dict) --*

      The list of users or groups impacted by this action. This is an optional field and is
      filled for the following sharing activities: DOCUMENT_SHARED, DOCUMENT_SHARED,
      DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.

      - **Users** *(list) --*

        The list of users.

        - *(dict) --*

          Describes the metadata of the user.

          - **Id** *(string) --*

            The ID of the user.

          - **Username** *(string) --*

            The name of the user.

          - **GivenName** *(string) --*

            The given name of the user before a rename operation.

          - **Surname** *(string) --*

            The surname of the user.

          - **EmailAddress** *(string) --*

            The email address of the user.

      - **Groups** *(list) --*

        The list of user groups.

        - *(dict) --*

          Describes the metadata of a user group.

          - **Id** *(string) --*

            The ID of the user group.

          - **Name** *(string) --*

            The name of the group.

    - **ResourceMetadata** *(dict) --*

      The metadata of the resource involved in the user action.

      - **Type** *(string) --*

        The type of resource.

      - **Name** *(string) --*

        The name of the resource.

      - **OriginalName** *(string) --*

        The original name of the resource before a rename operation.

      - **Id** *(string) --*

        The ID of the resource.

      - **VersionId** *(string) --*

        The version ID of the resource. This is an optional field and is filled for action on
        document version.

      - **Owner** *(dict) --*

        The owner of the resource.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The name of the user.

        - **GivenName** *(string) --*

          The given name of the user before a rename operation.

        - **Surname** *(string) --*

          The surname of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

      - **ParentId** *(string) --*

        The parent ID of the resource before a rename operation.

    - **OriginalParent** *(dict) --*

      The original parent of the resource. This is an optional field and is filled for move
      activities.

      - **Type** *(string) --*

        The type of resource.

      - **Name** *(string) --*

        The name of the resource.

      - **OriginalName** *(string) --*

        The original name of the resource before a rename operation.

      - **Id** *(string) --*

        The ID of the resource.

      - **VersionId** *(string) --*

        The version ID of the resource. This is an optional field and is filled for action on
        document version.

      - **Owner** *(dict) --*

        The owner of the resource.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The name of the user.

        - **GivenName** *(string) --*

          The given name of the user before a rename operation.

        - **Surname** *(string) --*

          The surname of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

      - **ParentId** *(string) --*

        The parent ID of the resource before a rename operation.

    - **CommentMetadata** *(dict) --*

      Metadata of the commenting activity. This is an optional field and is filled for
      commenting activities.

      - **CommentId** *(string) --*

        The ID of the comment.

      - **Contributor** *(dict) --*

        The user who made the comment.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The login name of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

        - **GivenName** *(string) --*

          The given name of the user.

        - **Surname** *(string) --*

          The surname of the user.

        - **OrganizationId** *(string) --*

          The ID of the organization.

        - **RootFolderId** *(string) --*

          The ID of the root folder.

        - **RecycleBinFolderId** *(string) --*

          The ID of the recycle bin folder.

        - **Status** *(string) --*

          The status of the user.

        - **Type** *(string) --*

          The type of user.

        - **CreatedTimestamp** *(datetime) --*

          The time when the user was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the user was modified.

        - **TimeZoneId** *(string) --*

          The time zone ID of the user.

        - **Locale** *(string) --*

          The locale of the user.

        - **Storage** *(dict) --*

          The storage for the user.

          - **StorageUtilizedInBytes** *(integer) --*

            The amount of storage used, in bytes.

          - **StorageRule** *(dict) --*

            The storage for a user.

            - **StorageAllocatedInBytes** *(integer) --*

              The amount of storage allocated, in bytes.

            - **StorageType** *(string) --*

              The type of storage.

      - **CreatedTimestamp** *(datetime) --*

        The timestamp that the comment was created.

      - **CommentStatus** *(string) --*

        The status of the comment.

      - **RecipientId** *(string) --*

        The ID of the user being replied to.
    """


_DescribeActivitiesPaginateResponseTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseTypeDef",
    {
        "UserActivities": List[DescribeActivitiesPaginateResponseUserActivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseTypeDef(
    _DescribeActivitiesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeActivitiesPaginate` `Response`

    - **UserActivities** *(list) --*

      The list of activities for the specified user and time period.

      - *(dict) --*

        Describes the activity information.

        - **Type** *(string) --*

          The activity type.

        - **TimeStamp** *(datetime) --*

          The timestamp when the action was performed.

        - **IsIndirectActivity** *(boolean) --*

          Indicates whether an activity is indirect or direct. An indirect activity results from a
          direct activity performed on a parent resource. For example, sharing a parent folder (the
          direct activity) shares all of the subfolders and documents within the parent folder (the
          indirect activity).

        - **OrganizationId** *(string) --*

          The ID of the organization.

        - **Initiator** *(dict) --*

          The user who performed the action.

          - **Id** *(string) --*

            The ID of the user.

          - **Username** *(string) --*

            The name of the user.

          - **GivenName** *(string) --*

            The given name of the user before a rename operation.

          - **Surname** *(string) --*

            The surname of the user.

          - **EmailAddress** *(string) --*

            The email address of the user.

        - **Participants** *(dict) --*

          The list of users or groups impacted by this action. This is an optional field and is
          filled for the following sharing activities: DOCUMENT_SHARED, DOCUMENT_SHARED,
          DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.

          - **Users** *(list) --*

            The list of users.

            - *(dict) --*

              Describes the metadata of the user.

              - **Id** *(string) --*

                The ID of the user.

              - **Username** *(string) --*

                The name of the user.

              - **GivenName** *(string) --*

                The given name of the user before a rename operation.

              - **Surname** *(string) --*

                The surname of the user.

              - **EmailAddress** *(string) --*

                The email address of the user.

          - **Groups** *(list) --*

            The list of user groups.

            - *(dict) --*

              Describes the metadata of a user group.

              - **Id** *(string) --*

                The ID of the user group.

              - **Name** *(string) --*

                The name of the group.

        - **ResourceMetadata** *(dict) --*

          The metadata of the resource involved in the user action.

          - **Type** *(string) --*

            The type of resource.

          - **Name** *(string) --*

            The name of the resource.

          - **OriginalName** *(string) --*

            The original name of the resource before a rename operation.

          - **Id** *(string) --*

            The ID of the resource.

          - **VersionId** *(string) --*

            The version ID of the resource. This is an optional field and is filled for action on
            document version.

          - **Owner** *(dict) --*

            The owner of the resource.

            - **Id** *(string) --*

              The ID of the user.

            - **Username** *(string) --*

              The name of the user.

            - **GivenName** *(string) --*

              The given name of the user before a rename operation.

            - **Surname** *(string) --*

              The surname of the user.

            - **EmailAddress** *(string) --*

              The email address of the user.

          - **ParentId** *(string) --*

            The parent ID of the resource before a rename operation.

        - **OriginalParent** *(dict) --*

          The original parent of the resource. This is an optional field and is filled for move
          activities.

          - **Type** *(string) --*

            The type of resource.

          - **Name** *(string) --*

            The name of the resource.

          - **OriginalName** *(string) --*

            The original name of the resource before a rename operation.

          - **Id** *(string) --*

            The ID of the resource.

          - **VersionId** *(string) --*

            The version ID of the resource. This is an optional field and is filled for action on
            document version.

          - **Owner** *(dict) --*

            The owner of the resource.

            - **Id** *(string) --*

              The ID of the user.

            - **Username** *(string) --*

              The name of the user.

            - **GivenName** *(string) --*

              The given name of the user before a rename operation.

            - **Surname** *(string) --*

              The surname of the user.

            - **EmailAddress** *(string) --*

              The email address of the user.

          - **ParentId** *(string) --*

            The parent ID of the resource before a rename operation.

        - **CommentMetadata** *(dict) --*

          Metadata of the commenting activity. This is an optional field and is filled for
          commenting activities.

          - **CommentId** *(string) --*

            The ID of the comment.

          - **Contributor** *(dict) --*

            The user who made the comment.

            - **Id** *(string) --*

              The ID of the user.

            - **Username** *(string) --*

              The login name of the user.

            - **EmailAddress** *(string) --*

              The email address of the user.

            - **GivenName** *(string) --*

              The given name of the user.

            - **Surname** *(string) --*

              The surname of the user.

            - **OrganizationId** *(string) --*

              The ID of the organization.

            - **RootFolderId** *(string) --*

              The ID of the root folder.

            - **RecycleBinFolderId** *(string) --*

              The ID of the recycle bin folder.

            - **Status** *(string) --*

              The status of the user.

            - **Type** *(string) --*

              The type of user.

            - **CreatedTimestamp** *(datetime) --*

              The time when the user was created.

            - **ModifiedTimestamp** *(datetime) --*

              The time when the user was modified.

            - **TimeZoneId** *(string) --*

              The time zone ID of the user.

            - **Locale** *(string) --*

              The locale of the user.

            - **Storage** *(dict) --*

              The storage for the user.

              - **StorageUtilizedInBytes** *(integer) --*

                The amount of storage used, in bytes.

              - **StorageRule** *(dict) --*

                The storage for a user.

                - **StorageAllocatedInBytes** *(integer) --*

                  The amount of storage allocated, in bytes.

                - **StorageType** *(string) --*

                  The type of storage.

          - **CreatedTimestamp** *(datetime) --*

            The timestamp that the comment was created.

          - **CommentStatus** *(string) --*

            The status of the comment.

          - **RecipientId** *(string) --*

            The ID of the user being replied to.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeCommentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCommentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCommentsPaginatePaginationConfigTypeDef(
    _DescribeCommentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeCommentsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef = TypedDict(
    "_DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef(
    _DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef
):
    """
    Type definition for `DescribeCommentsPaginateResponseCommentsContributorStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef = TypedDict(
    "_DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef,
    },
    total=False,
)


class DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef(
    _DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef
):
    """
    Type definition for `DescribeCommentsPaginateResponseCommentsContributor` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_DescribeCommentsPaginateResponseCommentsContributorTypeDef = TypedDict(
    "_DescribeCommentsPaginateResponseCommentsContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef,
    },
    total=False,
)


class DescribeCommentsPaginateResponseCommentsContributorTypeDef(
    _DescribeCommentsPaginateResponseCommentsContributorTypeDef
):
    """
    Type definition for `DescribeCommentsPaginateResponseComments` `Contributor`

    The details of the user who made the comment.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_DescribeCommentsPaginateResponseCommentsTypeDef = TypedDict(
    "_DescribeCommentsPaginateResponseCommentsTypeDef",
    {
        "CommentId": str,
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": DescribeCommentsPaginateResponseCommentsContributorTypeDef,
        "CreatedTimestamp": datetime,
        "Status": str,
        "Visibility": str,
        "RecipientId": str,
    },
    total=False,
)


class DescribeCommentsPaginateResponseCommentsTypeDef(
    _DescribeCommentsPaginateResponseCommentsTypeDef
):
    """
    Type definition for `DescribeCommentsPaginateResponse` `Comments`

    Describes a comment.

    - **CommentId** *(string) --*

      The ID of the comment.

    - **ParentId** *(string) --*

      The ID of the parent comment.

    - **ThreadId** *(string) --*

      The ID of the root comment in the thread.

    - **Text** *(string) --*

      The text of the comment.

    - **Contributor** *(dict) --*

      The details of the user who made the comment.

      - **Id** *(string) --*

        The ID of the user.

      - **Username** *(string) --*

        The login name of the user.

      - **EmailAddress** *(string) --*

        The email address of the user.

      - **GivenName** *(string) --*

        The given name of the user.

      - **Surname** *(string) --*

        The surname of the user.

      - **OrganizationId** *(string) --*

        The ID of the organization.

      - **RootFolderId** *(string) --*

        The ID of the root folder.

      - **RecycleBinFolderId** *(string) --*

        The ID of the recycle bin folder.

      - **Status** *(string) --*

        The status of the user.

      - **Type** *(string) --*

        The type of user.

      - **CreatedTimestamp** *(datetime) --*

        The time when the user was created.

      - **ModifiedTimestamp** *(datetime) --*

        The time when the user was modified.

      - **TimeZoneId** *(string) --*

        The time zone ID of the user.

      - **Locale** *(string) --*

        The locale of the user.

      - **Storage** *(dict) --*

        The storage for the user.

        - **StorageUtilizedInBytes** *(integer) --*

          The amount of storage used, in bytes.

        - **StorageRule** *(dict) --*

          The storage for a user.

          - **StorageAllocatedInBytes** *(integer) --*

            The amount of storage allocated, in bytes.

          - **StorageType** *(string) --*

            The type of storage.

    - **CreatedTimestamp** *(datetime) --*

      The time that the comment was created.

    - **Status** *(string) --*

      The status of the comment.

    - **Visibility** *(string) --*

      The visibility of the comment. Options are either PRIVATE, where the comment is visible
      only to the comment author and document owner and co-owners, or PUBLIC, where the comment
      is visible to document owners, co-owners, and contributors.

    - **RecipientId** *(string) --*

      If the comment is a reply to another user's comment, this field contains the user ID of
      the user being replied to.
    """


_DescribeCommentsPaginateResponseTypeDef = TypedDict(
    "_DescribeCommentsPaginateResponseTypeDef",
    {
        "Comments": List[DescribeCommentsPaginateResponseCommentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeCommentsPaginateResponseTypeDef(_DescribeCommentsPaginateResponseTypeDef):
    """
    Type definition for `DescribeCommentsPaginate` `Response`

    - **Comments** *(list) --*

      The list of comments for the specified document version.

      - *(dict) --*

        Describes a comment.

        - **CommentId** *(string) --*

          The ID of the comment.

        - **ParentId** *(string) --*

          The ID of the parent comment.

        - **ThreadId** *(string) --*

          The ID of the root comment in the thread.

        - **Text** *(string) --*

          The text of the comment.

        - **Contributor** *(dict) --*

          The details of the user who made the comment.

          - **Id** *(string) --*

            The ID of the user.

          - **Username** *(string) --*

            The login name of the user.

          - **EmailAddress** *(string) --*

            The email address of the user.

          - **GivenName** *(string) --*

            The given name of the user.

          - **Surname** *(string) --*

            The surname of the user.

          - **OrganizationId** *(string) --*

            The ID of the organization.

          - **RootFolderId** *(string) --*

            The ID of the root folder.

          - **RecycleBinFolderId** *(string) --*

            The ID of the recycle bin folder.

          - **Status** *(string) --*

            The status of the user.

          - **Type** *(string) --*

            The type of user.

          - **CreatedTimestamp** *(datetime) --*

            The time when the user was created.

          - **ModifiedTimestamp** *(datetime) --*

            The time when the user was modified.

          - **TimeZoneId** *(string) --*

            The time zone ID of the user.

          - **Locale** *(string) --*

            The locale of the user.

          - **Storage** *(dict) --*

            The storage for the user.

            - **StorageUtilizedInBytes** *(integer) --*

              The amount of storage used, in bytes.

            - **StorageRule** *(dict) --*

              The storage for a user.

              - **StorageAllocatedInBytes** *(integer) --*

                The amount of storage allocated, in bytes.

              - **StorageType** *(string) --*

                The type of storage.

        - **CreatedTimestamp** *(datetime) --*

          The time that the comment was created.

        - **Status** *(string) --*

          The status of the comment.

        - **Visibility** *(string) --*

          The visibility of the comment. Options are either PRIVATE, where the comment is visible
          only to the comment author and document owner and co-owners, or PUBLIC, where the comment
          is visible to document owners, co-owners, and contributors.

        - **RecipientId** *(string) --*

          If the comment is a reply to another user's comment, this field contains the user ID of
          the user being replied to.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDocumentVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDocumentVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDocumentVersionsPaginatePaginationConfigTypeDef(
    _DescribeDocumentVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDocumentVersionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef = TypedDict(
    "_DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef(
    _DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef
):
    """
    Type definition for `DescribeDocumentVersionsPaginateResponse` `DocumentVersions`

    Describes a version of a document.

    - **Id** *(string) --*

      The ID of the version.

    - **Name** *(string) --*

      The name of the version.

    - **ContentType** *(string) --*

      The content type of the document.

    - **Size** *(integer) --*

      The size of the document, in bytes.

    - **Signature** *(string) --*

      The signature of the document.

    - **Status** *(string) --*

      The status of the document.

    - **CreatedTimestamp** *(datetime) --*

      The timestamp when the document was first uploaded.

    - **ModifiedTimestamp** *(datetime) --*

      The timestamp when the document was last uploaded.

    - **ContentCreatedTimestamp** *(datetime) --*

      The timestamp when the content of the document was originally created.

    - **ContentModifiedTimestamp** *(datetime) --*

      The timestamp when the content of the document was modified.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **Thumbnail** *(dict) --*

      The thumbnail of the document.

      - *(string) --*

        - *(string) --*

    - **Source** *(dict) --*

      The source of the document.

      - *(string) --*

        - *(string) --*
    """


_DescribeDocumentVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeDocumentVersionsPaginateResponseTypeDef",
    {
        "DocumentVersions": List[
            DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDocumentVersionsPaginateResponseTypeDef(
    _DescribeDocumentVersionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDocumentVersionsPaginate` `Response`

    - **DocumentVersions** *(list) --*

      The document versions.

      - *(dict) --*

        Describes a version of a document.

        - **Id** *(string) --*

          The ID of the version.

        - **Name** *(string) --*

          The name of the version.

        - **ContentType** *(string) --*

          The content type of the document.

        - **Size** *(integer) --*

          The size of the document, in bytes.

        - **Signature** *(string) --*

          The signature of the document.

        - **Status** *(string) --*

          The status of the document.

        - **CreatedTimestamp** *(datetime) --*

          The timestamp when the document was first uploaded.

        - **ModifiedTimestamp** *(datetime) --*

          The timestamp when the document was last uploaded.

        - **ContentCreatedTimestamp** *(datetime) --*

          The timestamp when the content of the document was originally created.

        - **ContentModifiedTimestamp** *(datetime) --*

          The timestamp when the content of the document was modified.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **Thumbnail** *(dict) --*

          The thumbnail of the document.

          - *(string) --*

            - *(string) --*

        - **Source** *(dict) --*

          The source of the document.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeFolderContentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFolderContentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFolderContentsPaginatePaginationConfigTypeDef(
    _DescribeFolderContentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeFolderContentsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "_DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef(
    _DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef
):
    """
    Type definition for `DescribeFolderContentsPaginateResponseDocuments` `LatestVersionMetadata`

    The latest version of the document.

    - **Id** *(string) --*

      The ID of the version.

    - **Name** *(string) --*

      The name of the version.

    - **ContentType** *(string) --*

      The content type of the document.

    - **Size** *(integer) --*

      The size of the document, in bytes.

    - **Signature** *(string) --*

      The signature of the document.

    - **Status** *(string) --*

      The status of the document.

    - **CreatedTimestamp** *(datetime) --*

      The timestamp when the document was first uploaded.

    - **ModifiedTimestamp** *(datetime) --*

      The timestamp when the document was last uploaded.

    - **ContentCreatedTimestamp** *(datetime) --*

      The timestamp when the content of the document was originally created.

    - **ContentModifiedTimestamp** *(datetime) --*

      The timestamp when the content of the document was modified.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **Thumbnail** *(dict) --*

      The thumbnail of the document.

      - *(string) --*

        - *(string) --*

    - **Source** *(dict) --*

      The source of the document.

      - *(string) --*

        - *(string) --*
    """


_DescribeFolderContentsPaginateResponseDocumentsTypeDef = TypedDict(
    "_DescribeFolderContentsPaginateResponseDocumentsTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef,
        "ResourceState": str,
        "Labels": List[str],
    },
    total=False,
)


class DescribeFolderContentsPaginateResponseDocumentsTypeDef(
    _DescribeFolderContentsPaginateResponseDocumentsTypeDef
):
    """
    Type definition for `DescribeFolderContentsPaginateResponse` `Documents`

    Describes the document.

    - **Id** *(string) --*

      The ID of the document.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the document was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the document was updated.

    - **LatestVersionMetadata** *(dict) --*

      The latest version of the document.

      - **Id** *(string) --*

        The ID of the version.

      - **Name** *(string) --*

        The name of the version.

      - **ContentType** *(string) --*

        The content type of the document.

      - **Size** *(integer) --*

        The size of the document, in bytes.

      - **Signature** *(string) --*

        The signature of the document.

      - **Status** *(string) --*

        The status of the document.

      - **CreatedTimestamp** *(datetime) --*

        The timestamp when the document was first uploaded.

      - **ModifiedTimestamp** *(datetime) --*

        The timestamp when the document was last uploaded.

      - **ContentCreatedTimestamp** *(datetime) --*

        The timestamp when the content of the document was originally created.

      - **ContentModifiedTimestamp** *(datetime) --*

        The timestamp when the content of the document was modified.

      - **CreatorId** *(string) --*

        The ID of the creator.

      - **Thumbnail** *(dict) --*

        The thumbnail of the document.

        - *(string) --*

          - *(string) --*

      - **Source** *(dict) --*

        The source of the document.

        - *(string) --*

          - *(string) --*

    - **ResourceState** *(string) --*

      The resource state.

    - **Labels** *(list) --*

      List of labels on the document.

      - *(string) --*
    """


_DescribeFolderContentsPaginateResponseFoldersTypeDef = TypedDict(
    "_DescribeFolderContentsPaginateResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": str,
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class DescribeFolderContentsPaginateResponseFoldersTypeDef(
    _DescribeFolderContentsPaginateResponseFoldersTypeDef
):
    """
    Type definition for `DescribeFolderContentsPaginateResponse` `Folders`

    Describes a folder.

    - **Id** *(string) --*

      The ID of the folder.

    - **Name** *(string) --*

      The name of the folder.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the folder was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the folder was updated.

    - **ResourceState** *(string) --*

      The resource state of the folder.

    - **Signature** *(string) --*

      The unique identifier created from the subfolders and documents of the folder.

    - **Labels** *(list) --*

      List of labels on the folder.

      - *(string) --*

    - **Size** *(integer) --*

      The size of the folder metadata.

    - **LatestVersionSize** *(integer) --*

      The size of the latest version of the folder metadata.
    """


_DescribeFolderContentsPaginateResponseTypeDef = TypedDict(
    "_DescribeFolderContentsPaginateResponseTypeDef",
    {
        "Folders": List[DescribeFolderContentsPaginateResponseFoldersTypeDef],
        "Documents": List[DescribeFolderContentsPaginateResponseDocumentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeFolderContentsPaginateResponseTypeDef(
    _DescribeFolderContentsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeFolderContentsPaginate` `Response`

    - **Folders** *(list) --*

      The subfolders in the specified folder.

      - *(dict) --*

        Describes a folder.

        - **Id** *(string) --*

          The ID of the folder.

        - **Name** *(string) --*

          The name of the folder.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **ParentFolderId** *(string) --*

          The ID of the parent folder.

        - **CreatedTimestamp** *(datetime) --*

          The time when the folder was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the folder was updated.

        - **ResourceState** *(string) --*

          The resource state of the folder.

        - **Signature** *(string) --*

          The unique identifier created from the subfolders and documents of the folder.

        - **Labels** *(list) --*

          List of labels on the folder.

          - *(string) --*

        - **Size** *(integer) --*

          The size of the folder metadata.

        - **LatestVersionSize** *(integer) --*

          The size of the latest version of the folder metadata.

    - **Documents** *(list) --*

      The documents in the specified folder.

      - *(dict) --*

        Describes the document.

        - **Id** *(string) --*

          The ID of the document.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **ParentFolderId** *(string) --*

          The ID of the parent folder.

        - **CreatedTimestamp** *(datetime) --*

          The time when the document was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the document was updated.

        - **LatestVersionMetadata** *(dict) --*

          The latest version of the document.

          - **Id** *(string) --*

            The ID of the version.

          - **Name** *(string) --*

            The name of the version.

          - **ContentType** *(string) --*

            The content type of the document.

          - **Size** *(integer) --*

            The size of the document, in bytes.

          - **Signature** *(string) --*

            The signature of the document.

          - **Status** *(string) --*

            The status of the document.

          - **CreatedTimestamp** *(datetime) --*

            The timestamp when the document was first uploaded.

          - **ModifiedTimestamp** *(datetime) --*

            The timestamp when the document was last uploaded.

          - **ContentCreatedTimestamp** *(datetime) --*

            The timestamp when the content of the document was originally created.

          - **ContentModifiedTimestamp** *(datetime) --*

            The timestamp when the content of the document was modified.

          - **CreatorId** *(string) --*

            The ID of the creator.

          - **Thumbnail** *(dict) --*

            The thumbnail of the document.

            - *(string) --*

              - *(string) --*

          - **Source** *(dict) --*

            The source of the document.

            - *(string) --*

              - *(string) --*

        - **ResourceState** *(string) --*

          The resource state.

        - **Labels** *(list) --*

          List of labels on the document.

          - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeGroupsPaginatePaginationConfigTypeDef(
    _DescribeGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeGroupsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_DescribeGroupsPaginateResponseGroupsTypeDef",
    {"Id": str, "Name": str},
    total=False,
)


class DescribeGroupsPaginateResponseGroupsTypeDef(
    _DescribeGroupsPaginateResponseGroupsTypeDef
):
    """
    Type definition for `DescribeGroupsPaginateResponse` `Groups`

    Describes the metadata of a user group.

    - **Id** *(string) --*

      The ID of the user group.

    - **Name** *(string) --*

      The name of the group.
    """


_DescribeGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeGroupsPaginateResponseTypeDef",
    {"Groups": List[DescribeGroupsPaginateResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class DescribeGroupsPaginateResponseTypeDef(_DescribeGroupsPaginateResponseTypeDef):
    """
    Type definition for `DescribeGroupsPaginate` `Response`

    - **Groups** *(list) --*

      The list of groups.

      - *(dict) --*

        Describes the metadata of a user group.

        - **Id** *(string) --*

          The ID of the user group.

        - **Name** *(string) --*

          The name of the group.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef(
    _DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeNotificationSubscriptionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef = TypedDict(
    "_DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)


class DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef(
    _DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef
):
    """
    Type definition for `DescribeNotificationSubscriptionsPaginateResponse` `Subscriptions`

    Describes a subscription.

    - **SubscriptionId** *(string) --*

      The ID of the subscription.

    - **EndPoint** *(string) --*

      The endpoint of the subscription.

    - **Protocol** *(string) --*

      The protocol of the subscription.
    """


_DescribeNotificationSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeNotificationSubscriptionsPaginateResponseTypeDef",
    {
        "Subscriptions": List[
            DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeNotificationSubscriptionsPaginateResponseTypeDef(
    _DescribeNotificationSubscriptionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeNotificationSubscriptionsPaginate` `Response`

    - **Subscriptions** *(list) --*

      The subscriptions.

      - *(dict) --*

        Describes a subscription.

        - **SubscriptionId** *(string) --*

          The ID of the subscription.

        - **EndPoint** *(string) --*

          The endpoint of the subscription.

        - **Protocol** *(string) --*

          The protocol of the subscription.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeResourcePermissionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeResourcePermissionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeResourcePermissionsPaginatePaginationConfigTypeDef(
    _DescribeResourcePermissionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeResourcePermissionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef = TypedDict(
    "_DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef",
    {"Role": str, "Type": str},
    total=False,
)


class DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef(
    _DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef
):
    """
    Type definition for `DescribeResourcePermissionsPaginateResponsePrincipals` `Roles`

    Describes the permissions.

    - **Role** *(string) --*

      The role of the user.

    - **Type** *(string) --*

      The type of permissions.
    """


_DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef = TypedDict(
    "_DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef",
    {
        "Id": str,
        "Type": str,
        "Roles": List[
            DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef
        ],
    },
    total=False,
)


class DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef(
    _DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef
):
    """
    Type definition for `DescribeResourcePermissionsPaginateResponse` `Principals`

    Describes a resource.

    - **Id** *(string) --*

      The ID of the resource.

    - **Type** *(string) --*

      The type of resource.

    - **Roles** *(list) --*

      The permission information for the resource.

      - *(dict) --*

        Describes the permissions.

        - **Role** *(string) --*

          The role of the user.

        - **Type** *(string) --*

          The type of permissions.
    """


_DescribeResourcePermissionsPaginateResponseTypeDef = TypedDict(
    "_DescribeResourcePermissionsPaginateResponseTypeDef",
    {
        "Principals": List[
            DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeResourcePermissionsPaginateResponseTypeDef(
    _DescribeResourcePermissionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeResourcePermissionsPaginate` `Response`

    - **Principals** *(list) --*

      The principals.

      - *(dict) --*

        Describes a resource.

        - **Id** *(string) --*

          The ID of the resource.

        - **Type** *(string) --*

          The type of resource.

        - **Roles** *(list) --*

          The permission information for the resource.

          - *(dict) --*

            Describes the permissions.

            - **Role** *(string) --*

              The role of the user.

            - **Type** *(string) --*

              The type of permissions.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeRootFoldersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeRootFoldersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeRootFoldersPaginatePaginationConfigTypeDef(
    _DescribeRootFoldersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeRootFoldersPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeRootFoldersPaginateResponseFoldersTypeDef = TypedDict(
    "_DescribeRootFoldersPaginateResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": str,
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class DescribeRootFoldersPaginateResponseFoldersTypeDef(
    _DescribeRootFoldersPaginateResponseFoldersTypeDef
):
    """
    Type definition for `DescribeRootFoldersPaginateResponse` `Folders`

    Describes a folder.

    - **Id** *(string) --*

      The ID of the folder.

    - **Name** *(string) --*

      The name of the folder.

    - **CreatorId** *(string) --*

      The ID of the creator.

    - **ParentFolderId** *(string) --*

      The ID of the parent folder.

    - **CreatedTimestamp** *(datetime) --*

      The time when the folder was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the folder was updated.

    - **ResourceState** *(string) --*

      The resource state of the folder.

    - **Signature** *(string) --*

      The unique identifier created from the subfolders and documents of the folder.

    - **Labels** *(list) --*

      List of labels on the folder.

      - *(string) --*

    - **Size** *(integer) --*

      The size of the folder metadata.

    - **LatestVersionSize** *(integer) --*

      The size of the latest version of the folder metadata.
    """


_DescribeRootFoldersPaginateResponseTypeDef = TypedDict(
    "_DescribeRootFoldersPaginateResponseTypeDef",
    {
        "Folders": List[DescribeRootFoldersPaginateResponseFoldersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeRootFoldersPaginateResponseTypeDef(
    _DescribeRootFoldersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeRootFoldersPaginate` `Response`

    - **Folders** *(list) --*

      The user's special folders.

      - *(dict) --*

        Describes a folder.

        - **Id** *(string) --*

          The ID of the folder.

        - **Name** *(string) --*

          The name of the folder.

        - **CreatorId** *(string) --*

          The ID of the creator.

        - **ParentFolderId** *(string) --*

          The ID of the parent folder.

        - **CreatedTimestamp** *(datetime) --*

          The time when the folder was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the folder was updated.

        - **ResourceState** *(string) --*

          The resource state of the folder.

        - **Signature** *(string) --*

          The unique identifier created from the subfolders and documents of the folder.

        - **Labels** *(list) --*

          List of labels on the folder.

          - *(string) --*

        - **Size** *(integer) --*

          The size of the folder metadata.

        - **LatestVersionSize** *(integer) --*

          The size of the latest version of the folder metadata.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeUsersPaginatePaginationConfigTypeDef(
    _DescribeUsersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeUsersPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": str},
    total=False,
)


class DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef(
    _DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef
):
    """
    Type definition for `DescribeUsersPaginateResponseUsersStorage` `StorageRule`

    The storage for a user.

    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.

    - **StorageType** *(string) --*

      The type of storage.
    """


_DescribeUsersPaginateResponseUsersStorageTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseUsersStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef,
    },
    total=False,
)


class DescribeUsersPaginateResponseUsersStorageTypeDef(
    _DescribeUsersPaginateResponseUsersStorageTypeDef
):
    """
    Type definition for `DescribeUsersPaginateResponseUsers` `Storage`

    The storage for the user.

    - **StorageUtilizedInBytes** *(integer) --*

      The amount of storage used, in bytes.

    - **StorageRule** *(dict) --*

      The storage for a user.

      - **StorageAllocatedInBytes** *(integer) --*

        The amount of storage allocated, in bytes.

      - **StorageType** *(string) --*

        The type of storage.
    """


_DescribeUsersPaginateResponseUsersTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseUsersTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": str,
        "Type": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": str,
        "Storage": DescribeUsersPaginateResponseUsersStorageTypeDef,
    },
    total=False,
)


class DescribeUsersPaginateResponseUsersTypeDef(
    _DescribeUsersPaginateResponseUsersTypeDef
):
    """
    Type definition for `DescribeUsersPaginateResponse` `Users`

    Describes a user.

    - **Id** *(string) --*

      The ID of the user.

    - **Username** *(string) --*

      The login name of the user.

    - **EmailAddress** *(string) --*

      The email address of the user.

    - **GivenName** *(string) --*

      The given name of the user.

    - **Surname** *(string) --*

      The surname of the user.

    - **OrganizationId** *(string) --*

      The ID of the organization.

    - **RootFolderId** *(string) --*

      The ID of the root folder.

    - **RecycleBinFolderId** *(string) --*

      The ID of the recycle bin folder.

    - **Status** *(string) --*

      The status of the user.

    - **Type** *(string) --*

      The type of user.

    - **CreatedTimestamp** *(datetime) --*

      The time when the user was created.

    - **ModifiedTimestamp** *(datetime) --*

      The time when the user was modified.

    - **TimeZoneId** *(string) --*

      The time zone ID of the user.

    - **Locale** *(string) --*

      The locale of the user.

    - **Storage** *(dict) --*

      The storage for the user.

      - **StorageUtilizedInBytes** *(integer) --*

        The amount of storage used, in bytes.

      - **StorageRule** *(dict) --*

        The storage for a user.

        - **StorageAllocatedInBytes** *(integer) --*

          The amount of storage allocated, in bytes.

        - **StorageType** *(string) --*

          The type of storage.
    """


_DescribeUsersPaginateResponseTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseTypeDef",
    {
        "Users": List[DescribeUsersPaginateResponseUsersTypeDef],
        "TotalNumberOfUsers": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeUsersPaginateResponseTypeDef(_DescribeUsersPaginateResponseTypeDef):
    """
    Type definition for `DescribeUsersPaginate` `Response`

    - **Users** *(list) --*

      The users.

      - *(dict) --*

        Describes a user.

        - **Id** *(string) --*

          The ID of the user.

        - **Username** *(string) --*

          The login name of the user.

        - **EmailAddress** *(string) --*

          The email address of the user.

        - **GivenName** *(string) --*

          The given name of the user.

        - **Surname** *(string) --*

          The surname of the user.

        - **OrganizationId** *(string) --*

          The ID of the organization.

        - **RootFolderId** *(string) --*

          The ID of the root folder.

        - **RecycleBinFolderId** *(string) --*

          The ID of the recycle bin folder.

        - **Status** *(string) --*

          The status of the user.

        - **Type** *(string) --*

          The type of user.

        - **CreatedTimestamp** *(datetime) --*

          The time when the user was created.

        - **ModifiedTimestamp** *(datetime) --*

          The time when the user was modified.

        - **TimeZoneId** *(string) --*

          The time zone ID of the user.

        - **Locale** *(string) --*

          The locale of the user.

        - **Storage** *(dict) --*

          The storage for the user.

          - **StorageUtilizedInBytes** *(integer) --*

            The amount of storage used, in bytes.

          - **StorageRule** *(dict) --*

            The storage for a user.

            - **StorageAllocatedInBytes** *(integer) --*

              The amount of storage allocated, in bytes.

            - **StorageType** *(string) --*

              The type of storage.

    - **TotalNumberOfUsers** *(integer) --*

      The total number of users included in the results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
