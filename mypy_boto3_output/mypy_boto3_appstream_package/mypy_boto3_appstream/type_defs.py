"Main interface for appstream type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef",
    "ClientBatchAssociateUserStackResponseerrorsTypeDef",
    "ClientBatchAssociateUserStackResponseTypeDef",
    "ClientBatchAssociateUserStackUserStackAssociationsTypeDef",
    "ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef",
    "ClientBatchDisassociateUserStackResponseerrorsTypeDef",
    "ClientBatchDisassociateUserStackResponseTypeDef",
    "ClientBatchDisassociateUserStackUserStackAssociationsTypeDef",
    "ClientCopyImageResponseTypeDef",
    "ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef",
    "ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef",
    "ClientCreateDirectoryConfigResponseTypeDef",
    "ClientCreateDirectoryConfigServiceAccountCredentialsTypeDef",
    "ClientCreateFleetComputeCapacityTypeDef",
    "ClientCreateFleetDomainJoinInfoTypeDef",
    "ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef",
    "ClientCreateFleetResponseFleetDomainJoinInfoTypeDef",
    "ClientCreateFleetResponseFleetFleetErrorsTypeDef",
    "ClientCreateFleetResponseFleetVpcConfigTypeDef",
    "ClientCreateFleetResponseFleetTypeDef",
    "ClientCreateFleetResponseTypeDef",
    "ClientCreateFleetVpcConfigTypeDef",
    "ClientCreateImageBuilderAccessEndpointsTypeDef",
    "ClientCreateImageBuilderDomainJoinInfoTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderTypeDef",
    "ClientCreateImageBuilderResponseTypeDef",
    "ClientCreateImageBuilderStreamingUrlResponseTypeDef",
    "ClientCreateImageBuilderVpcConfigTypeDef",
    "ClientCreateStackAccessEndpointsTypeDef",
    "ClientCreateStackApplicationSettingsTypeDef",
    "ClientCreateStackResponseStackAccessEndpointsTypeDef",
    "ClientCreateStackResponseStackApplicationSettingsTypeDef",
    "ClientCreateStackResponseStackStackErrorsTypeDef",
    "ClientCreateStackResponseStackStorageConnectorsTypeDef",
    "ClientCreateStackResponseStackUserSettingsTypeDef",
    "ClientCreateStackResponseStackTypeDef",
    "ClientCreateStackResponseTypeDef",
    "ClientCreateStackStorageConnectorsTypeDef",
    "ClientCreateStackUserSettingsTypeDef",
    "ClientCreateStreamingUrlResponseTypeDef",
    "ClientCreateUsageReportSubscriptionResponseTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderTypeDef",
    "ClientDeleteImageBuilderResponseTypeDef",
    "ClientDeleteImageResponseImageApplicationsTypeDef",
    "ClientDeleteImageResponseImageImagePermissionsTypeDef",
    "ClientDeleteImageResponseImageStateChangeReasonTypeDef",
    "ClientDeleteImageResponseImageTypeDef",
    "ClientDeleteImageResponseTypeDef",
    "ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef",
    "ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef",
    "ClientDescribeDirectoryConfigsResponseTypeDef",
    "ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef",
    "ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef",
    "ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef",
    "ClientDescribeFleetsResponseFleetsVpcConfigTypeDef",
    "ClientDescribeFleetsResponseFleetsTypeDef",
    "ClientDescribeFleetsResponseTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersTypeDef",
    "ClientDescribeImageBuildersResponseTypeDef",
    "ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef",
    "ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef",
    "ClientDescribeImagePermissionsResponseTypeDef",
    "ClientDescribeImagesResponseImagesApplicationsTypeDef",
    "ClientDescribeImagesResponseImagesImagePermissionsTypeDef",
    "ClientDescribeImagesResponseImagesStateChangeReasonTypeDef",
    "ClientDescribeImagesResponseImagesTypeDef",
    "ClientDescribeImagesResponseTypeDef",
    "ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef",
    "ClientDescribeSessionsResponseSessionsTypeDef",
    "ClientDescribeSessionsResponseTypeDef",
    "ClientDescribeStacksResponseStacksAccessEndpointsTypeDef",
    "ClientDescribeStacksResponseStacksApplicationSettingsTypeDef",
    "ClientDescribeStacksResponseStacksStackErrorsTypeDef",
    "ClientDescribeStacksResponseStacksStorageConnectorsTypeDef",
    "ClientDescribeStacksResponseStacksUserSettingsTypeDef",
    "ClientDescribeStacksResponseStacksTypeDef",
    "ClientDescribeStacksResponseTypeDef",
    "ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef",
    "ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef",
    "ClientDescribeUsageReportSubscriptionsResponseTypeDef",
    "ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef",
    "ClientDescribeUserStackAssociationsResponseTypeDef",
    "ClientDescribeUsersResponseUsersTypeDef",
    "ClientDescribeUsersResponseTypeDef",
    "ClientListAssociatedFleetsResponseTypeDef",
    "ClientListAssociatedStacksResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    "ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    "ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    "ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    "ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    "ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef",
    "ClientStartImageBuilderResponseImageBuilderTypeDef",
    "ClientStartImageBuilderResponseTypeDef",
    "ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    "ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    "ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    "ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    "ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    "ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef",
    "ClientStopImageBuilderResponseImageBuilderTypeDef",
    "ClientStopImageBuilderResponseTypeDef",
    "ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef",
    "ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef",
    "ClientUpdateDirectoryConfigResponseTypeDef",
    "ClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef",
    "ClientUpdateFleetComputeCapacityTypeDef",
    "ClientUpdateFleetDomainJoinInfoTypeDef",
    "ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef",
    "ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef",
    "ClientUpdateFleetResponseFleetFleetErrorsTypeDef",
    "ClientUpdateFleetResponseFleetVpcConfigTypeDef",
    "ClientUpdateFleetResponseFleetTypeDef",
    "ClientUpdateFleetResponseTypeDef",
    "ClientUpdateFleetVpcConfigTypeDef",
    "ClientUpdateImagePermissionsImagePermissionsTypeDef",
    "ClientUpdateStackAccessEndpointsTypeDef",
    "ClientUpdateStackApplicationSettingsTypeDef",
    "ClientUpdateStackResponseStackAccessEndpointsTypeDef",
    "ClientUpdateStackResponseStackApplicationSettingsTypeDef",
    "ClientUpdateStackResponseStackStackErrorsTypeDef",
    "ClientUpdateStackResponseStackStorageConnectorsTypeDef",
    "ClientUpdateStackResponseStackUserSettingsTypeDef",
    "ClientUpdateStackResponseStackTypeDef",
    "ClientUpdateStackResponseTypeDef",
    "ClientUpdateStackStorageConnectorsTypeDef",
    "ClientUpdateStackUserSettingsTypeDef",
    "DescribeDirectoryConfigsPaginatePaginationConfigTypeDef",
    "DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef",
    "DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef",
    "DescribeDirectoryConfigsPaginateResponseTypeDef",
    "DescribeFleetsPaginatePaginationConfigTypeDef",
    "DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef",
    "DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef",
    "DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef",
    "DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef",
    "DescribeFleetsPaginateResponseFleetsTypeDef",
    "DescribeFleetsPaginateResponseTypeDef",
    "DescribeImageBuildersPaginatePaginationConfigTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersTypeDef",
    "DescribeImageBuildersPaginateResponseTypeDef",
    "DescribeImagesPaginatePaginationConfigTypeDef",
    "DescribeImagesPaginateResponseImagesApplicationsTypeDef",
    "DescribeImagesPaginateResponseImagesImagePermissionsTypeDef",
    "DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef",
    "DescribeImagesPaginateResponseImagesTypeDef",
    "DescribeImagesPaginateResponseTypeDef",
    "DescribeSessionsPaginatePaginationConfigTypeDef",
    "DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef",
    "DescribeSessionsPaginateResponseSessionsTypeDef",
    "DescribeSessionsPaginateResponseTypeDef",
    "DescribeStacksPaginatePaginationConfigTypeDef",
    "DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef",
    "DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef",
    "DescribeStacksPaginateResponseStacksStackErrorsTypeDef",
    "DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef",
    "DescribeStacksPaginateResponseStacksUserSettingsTypeDef",
    "DescribeStacksPaginateResponseStacksTypeDef",
    "DescribeStacksPaginateResponseTypeDef",
    "DescribeUserStackAssociationsPaginatePaginationConfigTypeDef",
    "DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef",
    "DescribeUserStackAssociationsPaginateResponseTypeDef",
    "DescribeUsersPaginatePaginationConfigTypeDef",
    "DescribeUsersPaginateResponseUsersTypeDef",
    "DescribeUsersPaginateResponseTypeDef",
    "FleetStartedWaitWaiterConfigTypeDef",
    "FleetStoppedWaitWaiterConfigTypeDef",
    "ListAssociatedFleetsPaginatePaginationConfigTypeDef",
    "ListAssociatedFleetsPaginateResponseTypeDef",
    "ListAssociatedStacksPaginatePaginationConfigTypeDef",
    "ListAssociatedStacksPaginateResponseTypeDef",
)


_ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef = TypedDict(
    "_ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": str,
        "SendEmailNotification": bool,
    },
    total=False,
)


class ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef(
    _ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef
):
    """
    Type definition for `ClientBatchAssociateUserStackResponseerrors` `UserStackAssociation`

    Information about the user and associated stack.

    - **StackName** *(string) --*

      The name of the stack that is associated with the user.

    - **UserName** *(string) --*

      The email address of the user who is associated with the stack.

      .. note::

        Users' email addresses are case-sensitive.

    - **AuthenticationType** *(string) --*

      The authentication type for the user.

    - **SendEmailNotification** *(boolean) --*

      Specifies whether a welcome email is sent to a user after the user is created in the
      user pool.
    """


_ClientBatchAssociateUserStackResponseerrorsTypeDef = TypedDict(
    "_ClientBatchAssociateUserStackResponseerrorsTypeDef",
    {
        "UserStackAssociation": ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchAssociateUserStackResponseerrorsTypeDef(
    _ClientBatchAssociateUserStackResponseerrorsTypeDef
):
    """
    Type definition for `ClientBatchAssociateUserStackResponse` `errors`

    Describes the error that is returned when a user can’t be associated with or disassociated
    from a stack.

    - **UserStackAssociation** *(dict) --*

      Information about the user and associated stack.

      - **StackName** *(string) --*

        The name of the stack that is associated with the user.

      - **UserName** *(string) --*

        The email address of the user who is associated with the stack.

        .. note::

          Users' email addresses are case-sensitive.

      - **AuthenticationType** *(string) --*

        The authentication type for the user.

      - **SendEmailNotification** *(boolean) --*

        Specifies whether a welcome email is sent to a user after the user is created in the
        user pool.

    - **ErrorCode** *(string) --*

      The error code for the error that is returned when a user can’t be associated with or
      disassociated from a stack.

    - **ErrorMessage** *(string) --*

      The error message for the error that is returned when a user can’t be associated with or
      disassociated from a stack.
    """


_ClientBatchAssociateUserStackResponseTypeDef = TypedDict(
    "_ClientBatchAssociateUserStackResponseTypeDef",
    {"errors": List[ClientBatchAssociateUserStackResponseerrorsTypeDef]},
    total=False,
)


class ClientBatchAssociateUserStackResponseTypeDef(
    _ClientBatchAssociateUserStackResponseTypeDef
):
    """
    Type definition for `ClientBatchAssociateUserStack` `Response`

    - **errors** *(list) --*

      The list of UserStackAssociationError objects.

      - *(dict) --*

        Describes the error that is returned when a user can’t be associated with or disassociated
        from a stack.

        - **UserStackAssociation** *(dict) --*

          Information about the user and associated stack.

          - **StackName** *(string) --*

            The name of the stack that is associated with the user.

          - **UserName** *(string) --*

            The email address of the user who is associated with the stack.

            .. note::

              Users' email addresses are case-sensitive.

          - **AuthenticationType** *(string) --*

            The authentication type for the user.

          - **SendEmailNotification** *(boolean) --*

            Specifies whether a welcome email is sent to a user after the user is created in the
            user pool.

        - **ErrorCode** *(string) --*

          The error code for the error that is returned when a user can’t be associated with or
          disassociated from a stack.

        - **ErrorMessage** *(string) --*

          The error message for the error that is returned when a user can’t be associated with or
          disassociated from a stack.
    """


_RequiredClientBatchAssociateUserStackUserStackAssociationsTypeDef = TypedDict(
    "_RequiredClientBatchAssociateUserStackUserStackAssociationsTypeDef",
    {"StackName": str, "UserName": str, "AuthenticationType": str},
)
_OptionalClientBatchAssociateUserStackUserStackAssociationsTypeDef = TypedDict(
    "_OptionalClientBatchAssociateUserStackUserStackAssociationsTypeDef",
    {"SendEmailNotification": bool},
    total=False,
)


class ClientBatchAssociateUserStackUserStackAssociationsTypeDef(
    _RequiredClientBatchAssociateUserStackUserStackAssociationsTypeDef,
    _OptionalClientBatchAssociateUserStackUserStackAssociationsTypeDef,
):
    """
    Type definition for `ClientBatchAssociateUserStack` `UserStackAssociations`

    Describes a user in the user pool and the associated stack.

    - **StackName** *(string) --* **[REQUIRED]**

      The name of the stack that is associated with the user.

    - **UserName** *(string) --* **[REQUIRED]**

      The email address of the user who is associated with the stack.

      .. note::

        Users' email addresses are case-sensitive.

    - **AuthenticationType** *(string) --* **[REQUIRED]**

      The authentication type for the user.

    - **SendEmailNotification** *(boolean) --*

      Specifies whether a welcome email is sent to a user after the user is created in the user
      pool.
    """


_ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef = TypedDict(
    "_ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": str,
        "SendEmailNotification": bool,
    },
    total=False,
)


class ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef(
    _ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef
):
    """
    Type definition for `ClientBatchDisassociateUserStackResponseerrors` `UserStackAssociation`

    Information about the user and associated stack.

    - **StackName** *(string) --*

      The name of the stack that is associated with the user.

    - **UserName** *(string) --*

      The email address of the user who is associated with the stack.

      .. note::

        Users' email addresses are case-sensitive.

    - **AuthenticationType** *(string) --*

      The authentication type for the user.

    - **SendEmailNotification** *(boolean) --*

      Specifies whether a welcome email is sent to a user after the user is created in the
      user pool.
    """


_ClientBatchDisassociateUserStackResponseerrorsTypeDef = TypedDict(
    "_ClientBatchDisassociateUserStackResponseerrorsTypeDef",
    {
        "UserStackAssociation": ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchDisassociateUserStackResponseerrorsTypeDef(
    _ClientBatchDisassociateUserStackResponseerrorsTypeDef
):
    """
    Type definition for `ClientBatchDisassociateUserStackResponse` `errors`

    Describes the error that is returned when a user can’t be associated with or disassociated
    from a stack.

    - **UserStackAssociation** *(dict) --*

      Information about the user and associated stack.

      - **StackName** *(string) --*

        The name of the stack that is associated with the user.

      - **UserName** *(string) --*

        The email address of the user who is associated with the stack.

        .. note::

          Users' email addresses are case-sensitive.

      - **AuthenticationType** *(string) --*

        The authentication type for the user.

      - **SendEmailNotification** *(boolean) --*

        Specifies whether a welcome email is sent to a user after the user is created in the
        user pool.

    - **ErrorCode** *(string) --*

      The error code for the error that is returned when a user can’t be associated with or
      disassociated from a stack.

    - **ErrorMessage** *(string) --*

      The error message for the error that is returned when a user can’t be associated with or
      disassociated from a stack.
    """


_ClientBatchDisassociateUserStackResponseTypeDef = TypedDict(
    "_ClientBatchDisassociateUserStackResponseTypeDef",
    {"errors": List[ClientBatchDisassociateUserStackResponseerrorsTypeDef]},
    total=False,
)


class ClientBatchDisassociateUserStackResponseTypeDef(
    _ClientBatchDisassociateUserStackResponseTypeDef
):
    """
    Type definition for `ClientBatchDisassociateUserStack` `Response`

    - **errors** *(list) --*

      The list of UserStackAssociationError objects.

      - *(dict) --*

        Describes the error that is returned when a user can’t be associated with or disassociated
        from a stack.

        - **UserStackAssociation** *(dict) --*

          Information about the user and associated stack.

          - **StackName** *(string) --*

            The name of the stack that is associated with the user.

          - **UserName** *(string) --*

            The email address of the user who is associated with the stack.

            .. note::

              Users' email addresses are case-sensitive.

          - **AuthenticationType** *(string) --*

            The authentication type for the user.

          - **SendEmailNotification** *(boolean) --*

            Specifies whether a welcome email is sent to a user after the user is created in the
            user pool.

        - **ErrorCode** *(string) --*

          The error code for the error that is returned when a user can’t be associated with or
          disassociated from a stack.

        - **ErrorMessage** *(string) --*

          The error message for the error that is returned when a user can’t be associated with or
          disassociated from a stack.
    """


_RequiredClientBatchDisassociateUserStackUserStackAssociationsTypeDef = TypedDict(
    "_RequiredClientBatchDisassociateUserStackUserStackAssociationsTypeDef",
    {"StackName": str, "UserName": str, "AuthenticationType": str},
)
_OptionalClientBatchDisassociateUserStackUserStackAssociationsTypeDef = TypedDict(
    "_OptionalClientBatchDisassociateUserStackUserStackAssociationsTypeDef",
    {"SendEmailNotification": bool},
    total=False,
)


class ClientBatchDisassociateUserStackUserStackAssociationsTypeDef(
    _RequiredClientBatchDisassociateUserStackUserStackAssociationsTypeDef,
    _OptionalClientBatchDisassociateUserStackUserStackAssociationsTypeDef,
):
    """
    Type definition for `ClientBatchDisassociateUserStack` `UserStackAssociations`

    Describes a user in the user pool and the associated stack.

    - **StackName** *(string) --* **[REQUIRED]**

      The name of the stack that is associated with the user.

    - **UserName** *(string) --* **[REQUIRED]**

      The email address of the user who is associated with the stack.

      .. note::

        Users' email addresses are case-sensitive.

    - **AuthenticationType** *(string) --* **[REQUIRED]**

      The authentication type for the user.

    - **SendEmailNotification** *(boolean) --*

      Specifies whether a welcome email is sent to a user after the user is created in the user
      pool.
    """


_ClientCopyImageResponseTypeDef = TypedDict(
    "_ClientCopyImageResponseTypeDef", {"DestinationImageName": str}, total=False
)


class ClientCopyImageResponseTypeDef(_ClientCopyImageResponseTypeDef):
    """
    Type definition for `ClientCopyImage` `Response`

    - **DestinationImageName** *(string) --*

      The name of the destination image.
    """


_ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "_ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)


class ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef(
    _ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef
):
    """
    Type definition for `ClientCreateDirectoryConfigResponseDirectoryConfig` `ServiceAccountCredentials`

    The credentials for the service account used by the fleet or image builder to connect to
    the directory.

    - **AccountName** *(string) --*

      The user name of the account. This account must have the following privileges: create
      computer objects, join computers to the domain, and change/reset the password on
      descendant computer objects for the organizational units specified.

    - **AccountPassword** *(string) --*

      The password for the account.
    """


_ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef = TypedDict(
    "_ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef(
    _ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef
):
    """
    Type definition for `ClientCreateDirectoryConfigResponse` `DirectoryConfig`

    Information about the directory configuration.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedNames** *(list) --*

      The distinguished names of the organizational units for computer accounts.

      - *(string) --*

    - **ServiceAccountCredentials** *(dict) --*

      The credentials for the service account used by the fleet or image builder to connect to
      the directory.

      - **AccountName** *(string) --*

        The user name of the account. This account must have the following privileges: create
        computer objects, join computers to the domain, and change/reset the password on
        descendant computer objects for the organizational units specified.

      - **AccountPassword** *(string) --*

        The password for the account.

    - **CreatedTime** *(datetime) --*

      The time the directory configuration was created.
    """


_ClientCreateDirectoryConfigResponseTypeDef = TypedDict(
    "_ClientCreateDirectoryConfigResponseTypeDef",
    {"DirectoryConfig": ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef},
    total=False,
)


class ClientCreateDirectoryConfigResponseTypeDef(
    _ClientCreateDirectoryConfigResponseTypeDef
):
    """
    Type definition for `ClientCreateDirectoryConfig` `Response`

    - **DirectoryConfig** *(dict) --*

      Information about the directory configuration.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedNames** *(list) --*

        The distinguished names of the organizational units for computer accounts.

        - *(string) --*

      - **ServiceAccountCredentials** *(dict) --*

        The credentials for the service account used by the fleet or image builder to connect to
        the directory.

        - **AccountName** *(string) --*

          The user name of the account. This account must have the following privileges: create
          computer objects, join computers to the domain, and change/reset the password on
          descendant computer objects for the organizational units specified.

        - **AccountPassword** *(string) --*

          The password for the account.

      - **CreatedTime** *(datetime) --*

        The time the directory configuration was created.
    """


_ClientCreateDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "_ClientCreateDirectoryConfigServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
)


class ClientCreateDirectoryConfigServiceAccountCredentialsTypeDef(
    _ClientCreateDirectoryConfigServiceAccountCredentialsTypeDef
):
    """
    Type definition for `ClientCreateDirectoryConfig` `ServiceAccountCredentials`

    The credentials for the service account used by the fleet or image builder to connect to the
    directory.

    - **AccountName** *(string) --* **[REQUIRED]**

      The user name of the account. This account must have the following privileges: create computer
      objects, join computers to the domain, and change/reset the password on descendant computer
      objects for the organizational units specified.

    - **AccountPassword** *(string) --* **[REQUIRED]**

      The password for the account.
    """


_ClientCreateFleetComputeCapacityTypeDef = TypedDict(
    "_ClientCreateFleetComputeCapacityTypeDef", {"DesiredInstances": int}
)


class ClientCreateFleetComputeCapacityTypeDef(_ClientCreateFleetComputeCapacityTypeDef):
    """
    Type definition for `ClientCreateFleet` `ComputeCapacity`

    The desired capacity for the fleet.

    - **DesiredInstances** *(integer) --* **[REQUIRED]**

      The desired number of streaming instances.
    """


_ClientCreateFleetDomainJoinInfoTypeDef = TypedDict(
    "_ClientCreateFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientCreateFleetDomainJoinInfoTypeDef(_ClientCreateFleetDomainJoinInfoTypeDef):
    """
    Type definition for `ClientCreateFleet` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft
    Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)


class ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef(
    _ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef
):
    """
    Type definition for `ClientCreateFleetResponseFleet` `ComputeCapacityStatus`

    The capacity status for the fleet.

    - **Desired** *(integer) --*

      The desired number of streaming instances.

    - **Running** *(integer) --*

      The total number of simultaneous streaming instances that are running.

    - **InUse** *(integer) --*

      The number of instances in use for streaming.

    - **Available** *(integer) --*

      The number of currently available instances that can be used to stream sessions.
    """


_ClientCreateFleetResponseFleetDomainJoinInfoTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientCreateFleetResponseFleetDomainJoinInfoTypeDef(
    _ClientCreateFleetResponseFleetDomainJoinInfoTypeDef
):
    """
    Type definition for `ClientCreateFleetResponseFleet` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the fleet to a
    Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientCreateFleetResponseFleetFleetErrorsTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetFleetErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientCreateFleetResponseFleetFleetErrorsTypeDef(
    _ClientCreateFleetResponseFleetFleetErrorsTypeDef
):
    """
    Type definition for `ClientCreateFleetResponseFleet` `FleetErrors`

    Describes a fleet error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientCreateFleetResponseFleetVpcConfigTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateFleetResponseFleetVpcConfigTypeDef(
    _ClientCreateFleetResponseFleetVpcConfigTypeDef
):
    """
    Type definition for `ClientCreateFleetResponseFleet` `VpcConfig`

    The VPC configuration for the fleet.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image
      builder instances use one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_ClientCreateFleetResponseFleetTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "InstanceType": str,
        "FleetType": str,
        "ComputeCapacityStatus": ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef,
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "State": str,
        "VpcConfig": ClientCreateFleetResponseFleetVpcConfigTypeDef,
        "CreatedTime": datetime,
        "FleetErrors": List[ClientCreateFleetResponseFleetFleetErrorsTypeDef],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientCreateFleetResponseFleetDomainJoinInfoTypeDef,
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
    },
    total=False,
)


class ClientCreateFleetResponseFleetTypeDef(_ClientCreateFleetResponseFleetTypeDef):
    """
    Type definition for `ClientCreateFleetResponse` `Fleet`

    Information about the fleet.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the fleet.

    - **Name** *(string) --*

      The name of the fleet.

    - **DisplayName** *(string) --*

      The fleet name to display.

    - **Description** *(string) --*

      The description to display.

    - **ImageName** *(string) --*

      The name of the image used to create the fleet.

    - **ImageArn** *(string) --*

      The ARN for the public, private, or shared image.

    - **InstanceType** *(string) --*

      The instance type to use when launching fleet instances. The following instance types are
      available:

      * stream.standard.medium

      * stream.standard.large

      * stream.compute.large

      * stream.compute.xlarge

      * stream.compute.2xlarge

      * stream.compute.4xlarge

      * stream.compute.8xlarge

      * stream.memory.large

      * stream.memory.xlarge

      * stream.memory.2xlarge

      * stream.memory.4xlarge

      * stream.memory.8xlarge

      * stream.graphics-design.large

      * stream.graphics-design.xlarge

      * stream.graphics-design.2xlarge

      * stream.graphics-design.4xlarge

      * stream.graphics-desktop.2xlarge

      * stream.graphics-pro.4xlarge

      * stream.graphics-pro.8xlarge

      * stream.graphics-pro.16xlarge

    - **FleetType** *(string) --*

      The fleet type.

        ALWAYS_ON

      Provides users with instant-on access to their apps. You are charged for all running
      instances in your fleet, even if no users are streaming apps.

        ON_DEMAND

      Provide users with access to applications after they connect, which takes one to two
      minutes. You are charged for instance streaming when users are connected and a small hourly
      fee for instances that are not streaming apps.

    - **ComputeCapacityStatus** *(dict) --*

      The capacity status for the fleet.

      - **Desired** *(integer) --*

        The desired number of streaming instances.

      - **Running** *(integer) --*

        The total number of simultaneous streaming instances that are running.

      - **InUse** *(integer) --*

        The number of instances in use for streaming.

      - **Available** *(integer) --*

        The number of currently available instances that can be used to stream sessions.

    - **MaxUserDurationInSeconds** *(integer) --*

      The maximum amount of time that a streaming session can remain active, in seconds. If users
      are still connected to a streaming instance five minutes before this limit is reached, they
      are prompted to save any open documents before being disconnected. After this time elapses,
      the instance is terminated and replaced by a new instance.

      Specify a value between 600 and 360000.

    - **DisconnectTimeoutInSeconds** *(integer) --*

      The amount of time that a streaming session remains active after users disconnect. If they
      try to reconnect to the streaming session after a disconnection or network interruption
      within this time interval, they are connected to their previous session. Otherwise, they
      are connected to a new session with a new streaming instance.

      Specify a value between 60 and 360000.

    - **State** *(string) --*

      The current state for the fleet.

    - **VpcConfig** *(dict) --*

      The VPC configuration for the fleet.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets to which a network interface is attached from the fleet
        instance or image builder instance. Fleet instances use one or more subnets. Image
        builder instances use one subnet.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        The identifiers of the security groups for the fleet or image builder.

        - *(string) --*

    - **CreatedTime** *(datetime) --*

      The time the fleet was created.

    - **FleetErrors** *(list) --*

      The fleet errors.

      - *(dict) --*

        Describes a fleet error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

    - **EnableDefaultInternetAccess** *(boolean) --*

      Indicates whether default internet access is enabled for the fleet.

    - **DomainJoinInfo** *(dict) --*

      The name of the directory and organizational unit (OU) to use to join the fleet to a
      Microsoft Active Directory domain.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedName** *(string) --*

        The distinguished name of the organizational unit for computer accounts.

    - **IdleDisconnectTimeoutInSeconds** *(integer) --*

      The amount of time that users can be idle (inactive) before they are disconnected from
      their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins. Users
      are notified before they are disconnected due to inactivity. If users try to reconnect to
      the streaming session before the time interval specified in ``DisconnectTimeoutInSeconds``
      elapses, they are connected to their previous session. Users are considered idle when they
      stop providing keyboard or mouse input during their streaming session. File uploads and
      downloads, audio in, audio out, and pixels changing do not qualify as user activity. If
      users continue to be idle after the time interval in ``IdleDisconnectTimeoutInSeconds``
      elapses, they are disconnected.

      To prevent users from being disconnected due to inactivity, specify a value of 0.
      Otherwise, specify a value between 60 and 3600. The default value is 0.

      .. note::

        If you enable this feature, we recommend that you specify a value that corresponds
        exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do
        this, the value is rounded to the nearest minute. For example, if you specify a value of
        70, users are disconnected after 1 minute of inactivity. If you specify a value that is
        at the midpoint between two different minutes, the value is rounded up. For example, if
        you specify a value of 90, users are disconnected after 2 minutes of inactivity.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance
      calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes the ARN
      of the role to use. The operation creates a new session with temporary credentials.
      AppStream 2.0 retrieves the temporary credentials and creates the
      **AppStream_Machine_Role** credential profile on the instance.

      For more information, see `Using an IAM Role to Grant Permissions to Applications and
      Scripts Running on AppStream 2.0 Streaming Instances
      <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
      in the *Amazon AppStream 2.0 Administration Guide* .
    """


_ClientCreateFleetResponseTypeDef = TypedDict(
    "_ClientCreateFleetResponseTypeDef",
    {"Fleet": ClientCreateFleetResponseFleetTypeDef},
    total=False,
)


class ClientCreateFleetResponseTypeDef(_ClientCreateFleetResponseTypeDef):
    """
    Type definition for `ClientCreateFleet` `Response`

    - **Fleet** *(dict) --*

      Information about the fleet.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the fleet.

      - **Name** *(string) --*

        The name of the fleet.

      - **DisplayName** *(string) --*

        The fleet name to display.

      - **Description** *(string) --*

        The description to display.

      - **ImageName** *(string) --*

        The name of the image used to create the fleet.

      - **ImageArn** *(string) --*

        The ARN for the public, private, or shared image.

      - **InstanceType** *(string) --*

        The instance type to use when launching fleet instances. The following instance types are
        available:

        * stream.standard.medium

        * stream.standard.large

        * stream.compute.large

        * stream.compute.xlarge

        * stream.compute.2xlarge

        * stream.compute.4xlarge

        * stream.compute.8xlarge

        * stream.memory.large

        * stream.memory.xlarge

        * stream.memory.2xlarge

        * stream.memory.4xlarge

        * stream.memory.8xlarge

        * stream.graphics-design.large

        * stream.graphics-design.xlarge

        * stream.graphics-design.2xlarge

        * stream.graphics-design.4xlarge

        * stream.graphics-desktop.2xlarge

        * stream.graphics-pro.4xlarge

        * stream.graphics-pro.8xlarge

        * stream.graphics-pro.16xlarge

      - **FleetType** *(string) --*

        The fleet type.

          ALWAYS_ON

        Provides users with instant-on access to their apps. You are charged for all running
        instances in your fleet, even if no users are streaming apps.

          ON_DEMAND

        Provide users with access to applications after they connect, which takes one to two
        minutes. You are charged for instance streaming when users are connected and a small hourly
        fee for instances that are not streaming apps.

      - **ComputeCapacityStatus** *(dict) --*

        The capacity status for the fleet.

        - **Desired** *(integer) --*

          The desired number of streaming instances.

        - **Running** *(integer) --*

          The total number of simultaneous streaming instances that are running.

        - **InUse** *(integer) --*

          The number of instances in use for streaming.

        - **Available** *(integer) --*

          The number of currently available instances that can be used to stream sessions.

      - **MaxUserDurationInSeconds** *(integer) --*

        The maximum amount of time that a streaming session can remain active, in seconds. If users
        are still connected to a streaming instance five minutes before this limit is reached, they
        are prompted to save any open documents before being disconnected. After this time elapses,
        the instance is terminated and replaced by a new instance.

        Specify a value between 600 and 360000.

      - **DisconnectTimeoutInSeconds** *(integer) --*

        The amount of time that a streaming session remains active after users disconnect. If they
        try to reconnect to the streaming session after a disconnection or network interruption
        within this time interval, they are connected to their previous session. Otherwise, they
        are connected to a new session with a new streaming instance.

        Specify a value between 60 and 360000.

      - **State** *(string) --*

        The current state for the fleet.

      - **VpcConfig** *(dict) --*

        The VPC configuration for the fleet.

        - **SubnetIds** *(list) --*

          The identifiers of the subnets to which a network interface is attached from the fleet
          instance or image builder instance. Fleet instances use one or more subnets. Image
          builder instances use one subnet.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          The identifiers of the security groups for the fleet or image builder.

          - *(string) --*

      - **CreatedTime** *(datetime) --*

        The time the fleet was created.

      - **FleetErrors** *(list) --*

        The fleet errors.

        - *(dict) --*

          Describes a fleet error.

          - **ErrorCode** *(string) --*

            The error code.

          - **ErrorMessage** *(string) --*

            The error message.

      - **EnableDefaultInternetAccess** *(boolean) --*

        Indicates whether default internet access is enabled for the fleet.

      - **DomainJoinInfo** *(dict) --*

        The name of the directory and organizational unit (OU) to use to join the fleet to a
        Microsoft Active Directory domain.

        - **DirectoryName** *(string) --*

          The fully qualified name of the directory (for example, corp.example.com).

        - **OrganizationalUnitDistinguishedName** *(string) --*

          The distinguished name of the organizational unit for computer accounts.

      - **IdleDisconnectTimeoutInSeconds** *(integer) --*

        The amount of time that users can be idle (inactive) before they are disconnected from
        their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins. Users
        are notified before they are disconnected due to inactivity. If users try to reconnect to
        the streaming session before the time interval specified in ``DisconnectTimeoutInSeconds``
        elapses, they are connected to their previous session. Users are considered idle when they
        stop providing keyboard or mouse input during their streaming session. File uploads and
        downloads, audio in, audio out, and pixels changing do not qualify as user activity. If
        users continue to be idle after the time interval in ``IdleDisconnectTimeoutInSeconds``
        elapses, they are disconnected.

        To prevent users from being disconnected due to inactivity, specify a value of 0.
        Otherwise, specify a value between 60 and 3600. The default value is 0.

        .. note::

          If you enable this feature, we recommend that you specify a value that corresponds
          exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do
          this, the value is rounded to the nearest minute. For example, if you specify a value of
          70, users are disconnected after 1 minute of inactivity. If you specify a value that is
          at the midpoint between two different minutes, the value is rounded up. For example, if
          you specify a value of 90, users are disconnected after 2 minutes of inactivity.

      - **IamRoleArn** *(string) --*

        The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance
        calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes the ARN
        of the role to use. The operation creates a new session with temporary credentials.
        AppStream 2.0 retrieves the temporary credentials and creates the
        **AppStream_Machine_Role** credential profile on the instance.

        For more information, see `Using an IAM Role to Grant Permissions to Applications and
        Scripts Running on AppStream 2.0 Streaming Instances
        <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
        in the *Amazon AppStream 2.0 Administration Guide* .
    """


_ClientCreateFleetVpcConfigTypeDef = TypedDict(
    "_ClientCreateFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateFleetVpcConfigTypeDef(_ClientCreateFleetVpcConfigTypeDef):
    """
    Type definition for `ClientCreateFleet` `VpcConfig`

    The VPC configuration for the fleet.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet instance
      or image builder instance. Fleet instances use one or more subnets. Image builder instances use
      one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_RequiredClientCreateImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_RequiredClientCreateImageBuilderAccessEndpointsTypeDef", {"EndpointType": str}
)
_OptionalClientCreateImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_OptionalClientCreateImageBuilderAccessEndpointsTypeDef",
    {"VpceId": str},
    total=False,
)


class ClientCreateImageBuilderAccessEndpointsTypeDef(
    _RequiredClientCreateImageBuilderAccessEndpointsTypeDef,
    _OptionalClientCreateImageBuilderAccessEndpointsTypeDef,
):
    """
    Type definition for `ClientCreateImageBuilder` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you
    specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only
    through that endpoint. When you specify an interface endpoint for an image builder,
    administrators can connect to the image builder only through that endpoint.

    - **EndpointType** *(string) --* **[REQUIRED]**

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientCreateImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "_ClientCreateImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientCreateImageBuilderDomainJoinInfoTypeDef(
    _ClientCreateImageBuilderDomainJoinInfoTypeDef
):
    """
    Type definition for `ClientCreateImageBuilder` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the image builder to a
    Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef
):
    """
    Type definition for `ClientCreateImageBuilderResponseImageBuilder` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
    When you specify an interface endpoint for a stack, users of the stack can connect to
    AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
    image builder, administrators can connect to the image builder only through that endpoint.

    - **EndpointType** *(string) --*

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef
):
    """
    Type definition for `ClientCreateImageBuilderResponseImageBuilder` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the image builder to
    a Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "ErrorTimestamp": datetime},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
):
    """
    Type definition for `ClientCreateImageBuilderResponseImageBuilder` `ImageBuilderErrors`

    Describes a resource error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.

    - **ErrorTimestamp** *(datetime) --*

      The time the error occurred.
    """


_ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef
):
    """
    Type definition for `ClientCreateImageBuilderResponseImageBuilder` `NetworkAccessConfiguration`

    Describes the network details of the fleet or image builder instance.

    - **EniPrivateIpAddress** *(string) --*

      The private IP address of the elastic network interface that is attached to instances in
      your VPC.

    - **EniId** *(string) --*

      The resource identifier of the elastic network interface that is attached to instances in
      your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef
):
    """
    Type definition for `ClientCreateImageBuilderResponseImageBuilder` `StateChangeReason`

    The reason why the last state change occurred.

    - **Code** *(string) --*

      The state change reason code.

    - **Message** *(string) --*

      The state change reason message.
    """


_ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef
):
    """
    Type definition for `ClientCreateImageBuilderResponseImageBuilder` `VpcConfig`

    The VPC configuration of the image builder.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image
      builder instances use one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_ClientCreateImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": str,
        "IamRoleArn": str,
        "State": str,
        "StateChangeReason": ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[
            ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef
        ],
    },
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderTypeDef
):
    """
    Type definition for `ClientCreateImageBuilderResponse` `ImageBuilder`

    Information about the image builder.

    - **Name** *(string) --*

      The name of the image builder.

    - **Arn** *(string) --*

      The ARN for the image builder.

    - **ImageArn** *(string) --*

      The ARN of the image from which this builder was created.

    - **Description** *(string) --*

      The description to display.

    - **DisplayName** *(string) --*

      The image builder name to display.

    - **VpcConfig** *(dict) --*

      The VPC configuration of the image builder.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets to which a network interface is attached from the fleet
        instance or image builder instance. Fleet instances use one or more subnets. Image
        builder instances use one subnet.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        The identifiers of the security groups for the fleet or image builder.

        - *(string) --*

    - **InstanceType** *(string) --*

      The instance type for the image builder. The following instance types are available:

      * stream.standard.medium

      * stream.standard.large

      * stream.compute.large

      * stream.compute.xlarge

      * stream.compute.2xlarge

      * stream.compute.4xlarge

      * stream.compute.8xlarge

      * stream.memory.large

      * stream.memory.xlarge

      * stream.memory.2xlarge

      * stream.memory.4xlarge

      * stream.memory.8xlarge

      * stream.graphics-design.large

      * stream.graphics-design.xlarge

      * stream.graphics-design.2xlarge

      * stream.graphics-design.4xlarge

      * stream.graphics-desktop.2xlarge

      * stream.graphics-pro.4xlarge

      * stream.graphics-pro.8xlarge

      * stream.graphics-pro.16xlarge

    - **Platform** *(string) --*

      The operating system platform of the image builder.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that is applied to the image builder. To assume a role, the image
      builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes
      the ARN of the role to use. The operation creates a new session with temporary credentials.
      AppStream 2.0 retrieves the temporary credentials and creates the
      **AppStream_Machine_Role** credential profile on the instance.

      For more information, see `Using an IAM Role to Grant Permissions to Applications and
      Scripts Running on AppStream 2.0 Streaming Instances
      <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
      in the *Amazon AppStream 2.0 Administration Guide* .

    - **State** *(string) --*

      The state of the image builder.

    - **StateChangeReason** *(dict) --*

      The reason why the last state change occurred.

      - **Code** *(string) --*

        The state change reason code.

      - **Message** *(string) --*

        The state change reason message.

    - **CreatedTime** *(datetime) --*

      The time stamp when the image builder was created.

    - **EnableDefaultInternetAccess** *(boolean) --*

      Enables or disables default internet access for the image builder.

    - **DomainJoinInfo** *(dict) --*

      The name of the directory and organizational unit (OU) to use to join the image builder to
      a Microsoft Active Directory domain.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedName** *(string) --*

        The distinguished name of the organizational unit for computer accounts.

    - **NetworkAccessConfiguration** *(dict) --*

      Describes the network details of the fleet or image builder instance.

      - **EniPrivateIpAddress** *(string) --*

        The private IP address of the elastic network interface that is attached to instances in
        your VPC.

      - **EniId** *(string) --*

        The resource identifier of the elastic network interface that is attached to instances in
        your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

    - **ImageBuilderErrors** *(list) --*

      The image builder errors.

      - *(dict) --*

        Describes a resource error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

        - **ErrorTimestamp** *(datetime) --*

          The time the error occurred.

    - **AppstreamAgentVersion** *(string) --*

      The version of the AppStream 2.0 agent that is currently being used by the image builder.

    - **AccessEndpoints** *(list) --*

      The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
      connect to the image builder only through the specified endpoints.

      - *(dict) --*

        Describes an interface VPC endpoint (interface endpoint) that lets you create a private
        connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
        When you specify an interface endpoint for a stack, users of the stack can connect to
        AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
        image builder, administrators can connect to the image builder only through that endpoint.

        - **EndpointType** *(string) --*

          The type of interface endpoint.

        - **VpceId** *(string) --*

          The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientCreateImageBuilderResponseTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientCreateImageBuilderResponseImageBuilderTypeDef},
    total=False,
)


class ClientCreateImageBuilderResponseTypeDef(_ClientCreateImageBuilderResponseTypeDef):
    """
    Type definition for `ClientCreateImageBuilder` `Response`

    - **ImageBuilder** *(dict) --*

      Information about the image builder.

      - **Name** *(string) --*

        The name of the image builder.

      - **Arn** *(string) --*

        The ARN for the image builder.

      - **ImageArn** *(string) --*

        The ARN of the image from which this builder was created.

      - **Description** *(string) --*

        The description to display.

      - **DisplayName** *(string) --*

        The image builder name to display.

      - **VpcConfig** *(dict) --*

        The VPC configuration of the image builder.

        - **SubnetIds** *(list) --*

          The identifiers of the subnets to which a network interface is attached from the fleet
          instance or image builder instance. Fleet instances use one or more subnets. Image
          builder instances use one subnet.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          The identifiers of the security groups for the fleet or image builder.

          - *(string) --*

      - **InstanceType** *(string) --*

        The instance type for the image builder. The following instance types are available:

        * stream.standard.medium

        * stream.standard.large

        * stream.compute.large

        * stream.compute.xlarge

        * stream.compute.2xlarge

        * stream.compute.4xlarge

        * stream.compute.8xlarge

        * stream.memory.large

        * stream.memory.xlarge

        * stream.memory.2xlarge

        * stream.memory.4xlarge

        * stream.memory.8xlarge

        * stream.graphics-design.large

        * stream.graphics-design.xlarge

        * stream.graphics-design.2xlarge

        * stream.graphics-design.4xlarge

        * stream.graphics-desktop.2xlarge

        * stream.graphics-pro.4xlarge

        * stream.graphics-pro.8xlarge

        * stream.graphics-pro.16xlarge

      - **Platform** *(string) --*

        The operating system platform of the image builder.

      - **IamRoleArn** *(string) --*

        The ARN of the IAM role that is applied to the image builder. To assume a role, the image
        builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes
        the ARN of the role to use. The operation creates a new session with temporary credentials.
        AppStream 2.0 retrieves the temporary credentials and creates the
        **AppStream_Machine_Role** credential profile on the instance.

        For more information, see `Using an IAM Role to Grant Permissions to Applications and
        Scripts Running on AppStream 2.0 Streaming Instances
        <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
        in the *Amazon AppStream 2.0 Administration Guide* .

      - **State** *(string) --*

        The state of the image builder.

      - **StateChangeReason** *(dict) --*

        The reason why the last state change occurred.

        - **Code** *(string) --*

          The state change reason code.

        - **Message** *(string) --*

          The state change reason message.

      - **CreatedTime** *(datetime) --*

        The time stamp when the image builder was created.

      - **EnableDefaultInternetAccess** *(boolean) --*

        Enables or disables default internet access for the image builder.

      - **DomainJoinInfo** *(dict) --*

        The name of the directory and organizational unit (OU) to use to join the image builder to
        a Microsoft Active Directory domain.

        - **DirectoryName** *(string) --*

          The fully qualified name of the directory (for example, corp.example.com).

        - **OrganizationalUnitDistinguishedName** *(string) --*

          The distinguished name of the organizational unit for computer accounts.

      - **NetworkAccessConfiguration** *(dict) --*

        Describes the network details of the fleet or image builder instance.

        - **EniPrivateIpAddress** *(string) --*

          The private IP address of the elastic network interface that is attached to instances in
          your VPC.

        - **EniId** *(string) --*

          The resource identifier of the elastic network interface that is attached to instances in
          your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

      - **ImageBuilderErrors** *(list) --*

        The image builder errors.

        - *(dict) --*

          Describes a resource error.

          - **ErrorCode** *(string) --*

            The error code.

          - **ErrorMessage** *(string) --*

            The error message.

          - **ErrorTimestamp** *(datetime) --*

            The time the error occurred.

      - **AppstreamAgentVersion** *(string) --*

        The version of the AppStream 2.0 agent that is currently being used by the image builder.

      - **AccessEndpoints** *(list) --*

        The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
        connect to the image builder only through the specified endpoints.

        - *(dict) --*

          Describes an interface VPC endpoint (interface endpoint) that lets you create a private
          connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
          When you specify an interface endpoint for a stack, users of the stack can connect to
          AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
          image builder, administrators can connect to the image builder only through that endpoint.

          - **EndpointType** *(string) --*

            The type of interface endpoint.

          - **VpceId** *(string) --*

            The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientCreateImageBuilderStreamingUrlResponseTypeDef = TypedDict(
    "_ClientCreateImageBuilderStreamingUrlResponseTypeDef",
    {"StreamingURL": str, "Expires": datetime},
    total=False,
)


class ClientCreateImageBuilderStreamingUrlResponseTypeDef(
    _ClientCreateImageBuilderStreamingUrlResponseTypeDef
):
    """
    Type definition for `ClientCreateImageBuilderStreamingUrl` `Response`

    - **StreamingURL** *(string) --*

      The URL to start the AppStream 2.0 streaming session.

    - **Expires** *(datetime) --*

      The elapsed time, in seconds after the Unix epoch, when this URL expires.
    """


_ClientCreateImageBuilderVpcConfigTypeDef = TypedDict(
    "_ClientCreateImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateImageBuilderVpcConfigTypeDef(
    _ClientCreateImageBuilderVpcConfigTypeDef
):
    """
    Type definition for `ClientCreateImageBuilder` `VpcConfig`

    The VPC configuration for the image builder. You can specify only one subnet.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet instance
      or image builder instance. Fleet instances use one or more subnets. Image builder instances use
      one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_RequiredClientCreateStackAccessEndpointsTypeDef = TypedDict(
    "_RequiredClientCreateStackAccessEndpointsTypeDef", {"EndpointType": str}
)
_OptionalClientCreateStackAccessEndpointsTypeDef = TypedDict(
    "_OptionalClientCreateStackAccessEndpointsTypeDef", {"VpceId": str}, total=False
)


class ClientCreateStackAccessEndpointsTypeDef(
    _RequiredClientCreateStackAccessEndpointsTypeDef,
    _OptionalClientCreateStackAccessEndpointsTypeDef,
):
    """
    Type definition for `ClientCreateStack` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you
    specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only
    through that endpoint. When you specify an interface endpoint for an image builder,
    administrators can connect to the image builder only through that endpoint.

    - **EndpointType** *(string) --* **[REQUIRED]**

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_RequiredClientCreateStackApplicationSettingsTypeDef = TypedDict(
    "_RequiredClientCreateStackApplicationSettingsTypeDef", {"Enabled": bool}
)
_OptionalClientCreateStackApplicationSettingsTypeDef = TypedDict(
    "_OptionalClientCreateStackApplicationSettingsTypeDef",
    {"SettingsGroup": str},
    total=False,
)


class ClientCreateStackApplicationSettingsTypeDef(
    _RequiredClientCreateStackApplicationSettingsTypeDef,
    _OptionalClientCreateStackApplicationSettingsTypeDef,
):
    """
    Type definition for `ClientCreateStack` `ApplicationSettings`

    The persistent application settings for users of a stack. When these settings are enabled,
    changes that users make to applications and Windows settings are automatically saved after each
    session and applied to the next session.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Enables or disables persistent application settings for users during their streaming sessions.

    - **SettingsGroup** *(string) --*

      The path prefix for the S3 bucket where users’ persistent application settings are stored. You
      can allow the same persistent application settings to be used across multiple stacks by
      specifying the same settings group for each stack.
    """


_ClientCreateStackResponseStackAccessEndpointsTypeDef = TypedDict(
    "_ClientCreateStackResponseStackAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientCreateStackResponseStackAccessEndpointsTypeDef(
    _ClientCreateStackResponseStackAccessEndpointsTypeDef
):
    """
    Type definition for `ClientCreateStackResponseStack` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
    When you specify an interface endpoint for a stack, users of the stack can connect to
    AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
    image builder, administrators can connect to the image builder only through that endpoint.

    - **EndpointType** *(string) --*

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientCreateStackResponseStackApplicationSettingsTypeDef = TypedDict(
    "_ClientCreateStackResponseStackApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)


class ClientCreateStackResponseStackApplicationSettingsTypeDef(
    _ClientCreateStackResponseStackApplicationSettingsTypeDef
):
    """
    Type definition for `ClientCreateStackResponseStack` `ApplicationSettings`

    The persistent application settings for users of the stack.

    - **Enabled** *(boolean) --*

      Specifies whether persistent application settings are enabled for users during their
      streaming sessions.

    - **SettingsGroup** *(string) --*

      The path prefix for the S3 bucket where users’ persistent application settings are stored.

    - **S3BucketName** *(string) --*

      The S3 bucket where users’ persistent application settings are stored. When persistent
      application settings are enabled for the first time for an account in an AWS Region, an
      S3 bucket is created. The bucket is unique to the AWS account and the Region.
    """


_ClientCreateStackResponseStackStackErrorsTypeDef = TypedDict(
    "_ClientCreateStackResponseStackStackErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientCreateStackResponseStackStackErrorsTypeDef(
    _ClientCreateStackResponseStackStackErrorsTypeDef
):
    """
    Type definition for `ClientCreateStackResponseStack` `StackErrors`

    Describes a stack error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientCreateStackResponseStackStorageConnectorsTypeDef = TypedDict(
    "_ClientCreateStackResponseStackStorageConnectorsTypeDef",
    {"ConnectorType": str, "ResourceIdentifier": str, "Domains": List[str]},
    total=False,
)


class ClientCreateStackResponseStackStorageConnectorsTypeDef(
    _ClientCreateStackResponseStackStorageConnectorsTypeDef
):
    """
    Type definition for `ClientCreateStackResponseStack` `StorageConnectors`

    Describes a connector that enables persistent storage for users.

    - **ConnectorType** *(string) --*

      The type of storage connector.

    - **ResourceIdentifier** *(string) --*

      The ARN of the storage connector.

    - **Domains** *(list) --*

      The names of the domains for the account.

      - *(string) --* GSuite domain for GDrive integration.
    """


_ClientCreateStackResponseStackUserSettingsTypeDef = TypedDict(
    "_ClientCreateStackResponseStackUserSettingsTypeDef",
    {"Action": str, "Permission": str},
    total=False,
)


class ClientCreateStackResponseStackUserSettingsTypeDef(
    _ClientCreateStackResponseStackUserSettingsTypeDef
):
    """
    Type definition for `ClientCreateStackResponseStack` `UserSettings`

    Describes an action and whether the action is enabled or disabled for users during their
    streaming sessions.

    - **Action** *(string) --*

      The action that is enabled or disabled.

    - **Permission** *(string) --*

      Indicates whether the action is enabled or disabled.
    """


_ClientCreateStackResponseStackTypeDef = TypedDict(
    "_ClientCreateStackResponseStackTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "StorageConnectors": List[
            ClientCreateStackResponseStackStorageConnectorsTypeDef
        ],
        "RedirectURL": str,
        "FeedbackURL": str,
        "StackErrors": List[ClientCreateStackResponseStackStackErrorsTypeDef],
        "UserSettings": List[ClientCreateStackResponseStackUserSettingsTypeDef],
        "ApplicationSettings": ClientCreateStackResponseStackApplicationSettingsTypeDef,
        "AccessEndpoints": List[ClientCreateStackResponseStackAccessEndpointsTypeDef],
        "EmbedHostDomains": List[str],
    },
    total=False,
)


class ClientCreateStackResponseStackTypeDef(_ClientCreateStackResponseStackTypeDef):
    """
    Type definition for `ClientCreateStackResponse` `Stack`

    Information about the stack.

    - **Arn** *(string) --*

      The ARN of the stack.

    - **Name** *(string) --*

      The name of the stack.

    - **Description** *(string) --*

      The description to display.

    - **DisplayName** *(string) --*

      The stack name to display.

    - **CreatedTime** *(datetime) --*

      The time the stack was created.

    - **StorageConnectors** *(list) --*

      The storage connectors to enable.

      - *(dict) --*

        Describes a connector that enables persistent storage for users.

        - **ConnectorType** *(string) --*

          The type of storage connector.

        - **ResourceIdentifier** *(string) --*

          The ARN of the storage connector.

        - **Domains** *(list) --*

          The names of the domains for the account.

          - *(string) --* GSuite domain for GDrive integration.

    - **RedirectURL** *(string) --*

      The URL that users are redirected to after their streaming session ends.

    - **FeedbackURL** *(string) --*

      The URL that users are redirected to after they click the Send Feedback link. If no URL is
      specified, no Send Feedback link is displayed.

    - **StackErrors** *(list) --*

      The errors for the stack.

      - *(dict) --*

        Describes a stack error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

    - **UserSettings** *(list) --*

      The actions that are enabled or disabled for users during their streaming sessions. By
      default these actions are enabled.

      - *(dict) --*

        Describes an action and whether the action is enabled or disabled for users during their
        streaming sessions.

        - **Action** *(string) --*

          The action that is enabled or disabled.

        - **Permission** *(string) --*

          Indicates whether the action is enabled or disabled.

    - **ApplicationSettings** *(dict) --*

      The persistent application settings for users of the stack.

      - **Enabled** *(boolean) --*

        Specifies whether persistent application settings are enabled for users during their
        streaming sessions.

      - **SettingsGroup** *(string) --*

        The path prefix for the S3 bucket where users’ persistent application settings are stored.

      - **S3BucketName** *(string) --*

        The S3 bucket where users’ persistent application settings are stored. When persistent
        application settings are enabled for the first time for an account in an AWS Region, an
        S3 bucket is created. The bucket is unique to the AWS account and the Region.

    - **AccessEndpoints** *(list) --*

      The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can
      connect to AppStream 2.0 only through the specified endpoints.

      - *(dict) --*

        Describes an interface VPC endpoint (interface endpoint) that lets you create a private
        connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
        When you specify an interface endpoint for a stack, users of the stack can connect to
        AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
        image builder, administrators can connect to the image builder only through that endpoint.

        - **EndpointType** *(string) --*

          The type of interface endpoint.

        - **VpceId** *(string) --*

          The identifier (ID) of the VPC in which the interface endpoint is used.

    - **EmbedHostDomains** *(list) --*

      The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must
      approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

      - *(string) --* Specifies a valid domain that can embed AppStream. Valid examples include:
      ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples include:
      ["test,com", ".com", "h*llo.com". ""]
    """


_ClientCreateStackResponseTypeDef = TypedDict(
    "_ClientCreateStackResponseTypeDef",
    {"Stack": ClientCreateStackResponseStackTypeDef},
    total=False,
)


class ClientCreateStackResponseTypeDef(_ClientCreateStackResponseTypeDef):
    """
    Type definition for `ClientCreateStack` `Response`

    - **Stack** *(dict) --*

      Information about the stack.

      - **Arn** *(string) --*

        The ARN of the stack.

      - **Name** *(string) --*

        The name of the stack.

      - **Description** *(string) --*

        The description to display.

      - **DisplayName** *(string) --*

        The stack name to display.

      - **CreatedTime** *(datetime) --*

        The time the stack was created.

      - **StorageConnectors** *(list) --*

        The storage connectors to enable.

        - *(dict) --*

          Describes a connector that enables persistent storage for users.

          - **ConnectorType** *(string) --*

            The type of storage connector.

          - **ResourceIdentifier** *(string) --*

            The ARN of the storage connector.

          - **Domains** *(list) --*

            The names of the domains for the account.

            - *(string) --* GSuite domain for GDrive integration.

      - **RedirectURL** *(string) --*

        The URL that users are redirected to after their streaming session ends.

      - **FeedbackURL** *(string) --*

        The URL that users are redirected to after they click the Send Feedback link. If no URL is
        specified, no Send Feedback link is displayed.

      - **StackErrors** *(list) --*

        The errors for the stack.

        - *(dict) --*

          Describes a stack error.

          - **ErrorCode** *(string) --*

            The error code.

          - **ErrorMessage** *(string) --*

            The error message.

      - **UserSettings** *(list) --*

        The actions that are enabled or disabled for users during their streaming sessions. By
        default these actions are enabled.

        - *(dict) --*

          Describes an action and whether the action is enabled or disabled for users during their
          streaming sessions.

          - **Action** *(string) --*

            The action that is enabled or disabled.

          - **Permission** *(string) --*

            Indicates whether the action is enabled or disabled.

      - **ApplicationSettings** *(dict) --*

        The persistent application settings for users of the stack.

        - **Enabled** *(boolean) --*

          Specifies whether persistent application settings are enabled for users during their
          streaming sessions.

        - **SettingsGroup** *(string) --*

          The path prefix for the S3 bucket where users’ persistent application settings are stored.

        - **S3BucketName** *(string) --*

          The S3 bucket where users’ persistent application settings are stored. When persistent
          application settings are enabled for the first time for an account in an AWS Region, an
          S3 bucket is created. The bucket is unique to the AWS account and the Region.

      - **AccessEndpoints** *(list) --*

        The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can
        connect to AppStream 2.0 only through the specified endpoints.

        - *(dict) --*

          Describes an interface VPC endpoint (interface endpoint) that lets you create a private
          connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
          When you specify an interface endpoint for a stack, users of the stack can connect to
          AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
          image builder, administrators can connect to the image builder only through that endpoint.

          - **EndpointType** *(string) --*

            The type of interface endpoint.

          - **VpceId** *(string) --*

            The identifier (ID) of the VPC in which the interface endpoint is used.

      - **EmbedHostDomains** *(list) --*

        The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must
        approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

        - *(string) --* Specifies a valid domain that can embed AppStream. Valid examples include:
        ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples include:
        ["test,com", ".com", "h*llo.com". ""]
    """


_RequiredClientCreateStackStorageConnectorsTypeDef = TypedDict(
    "_RequiredClientCreateStackStorageConnectorsTypeDef", {"ConnectorType": str}
)
_OptionalClientCreateStackStorageConnectorsTypeDef = TypedDict(
    "_OptionalClientCreateStackStorageConnectorsTypeDef",
    {"ResourceIdentifier": str, "Domains": List[str]},
    total=False,
)


class ClientCreateStackStorageConnectorsTypeDef(
    _RequiredClientCreateStackStorageConnectorsTypeDef,
    _OptionalClientCreateStackStorageConnectorsTypeDef,
):
    """
    Type definition for `ClientCreateStack` `StorageConnectors`

    Describes a connector that enables persistent storage for users.

    - **ConnectorType** *(string) --* **[REQUIRED]**

      The type of storage connector.

    - **ResourceIdentifier** *(string) --*

      The ARN of the storage connector.

    - **Domains** *(list) --*

      The names of the domains for the account.

      - *(string) --* GSuite domain for GDrive integration.
    """


_ClientCreateStackUserSettingsTypeDef = TypedDict(
    "_ClientCreateStackUserSettingsTypeDef", {"Action": str, "Permission": str}
)


class ClientCreateStackUserSettingsTypeDef(_ClientCreateStackUserSettingsTypeDef):
    """
    Type definition for `ClientCreateStack` `UserSettings`

    Describes an action and whether the action is enabled or disabled for users during their
    streaming sessions.

    - **Action** *(string) --* **[REQUIRED]**

      The action that is enabled or disabled.

    - **Permission** *(string) --* **[REQUIRED]**

      Indicates whether the action is enabled or disabled.
    """


_ClientCreateStreamingUrlResponseTypeDef = TypedDict(
    "_ClientCreateStreamingUrlResponseTypeDef",
    {"StreamingURL": str, "Expires": datetime},
    total=False,
)


class ClientCreateStreamingUrlResponseTypeDef(_ClientCreateStreamingUrlResponseTypeDef):
    """
    Type definition for `ClientCreateStreamingUrl` `Response`

    - **StreamingURL** *(string) --*

      The URL to start the AppStream 2.0 streaming session.

    - **Expires** *(datetime) --*

      The elapsed time, in seconds after the Unix epoch, when this URL expires.
    """


_ClientCreateUsageReportSubscriptionResponseTypeDef = TypedDict(
    "_ClientCreateUsageReportSubscriptionResponseTypeDef",
    {"S3BucketName": str, "Schedule": str},
    total=False,
)


class ClientCreateUsageReportSubscriptionResponseTypeDef(
    _ClientCreateUsageReportSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientCreateUsageReportSubscription` `Response`

    - **S3BucketName** *(string) --*

      The Amazon S3 bucket where generated reports are stored.

      If you enabled on-instance session scripts and Amazon S3 logging for your session script
      configuration, AppStream 2.0 created an S3 bucket to store the script output. The bucket is
      unique to your account and Region. When you enable usage reporting in this case, AppStream
      2.0 uses the same bucket to store your usage reports. If you haven't already enabled
      on-instance session scripts, when you enable usage reports, AppStream 2.0 creates a new S3
      bucket.

    - **Schedule** *(string) --*

      The schedule for generating usage reports.
    """


_ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef
):
    """
    Type definition for `ClientDeleteImageBuilderResponseImageBuilder` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
    When you specify an interface endpoint for a stack, users of the stack can connect to
    AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
    image builder, administrators can connect to the image builder only through that endpoint.

    - **EndpointType** *(string) --*

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef
):
    """
    Type definition for `ClientDeleteImageBuilderResponseImageBuilder` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the image builder to
    a Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "ErrorTimestamp": datetime},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
):
    """
    Type definition for `ClientDeleteImageBuilderResponseImageBuilder` `ImageBuilderErrors`

    Describes a resource error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.

    - **ErrorTimestamp** *(datetime) --*

      The time the error occurred.
    """


_ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef
):
    """
    Type definition for `ClientDeleteImageBuilderResponseImageBuilder` `NetworkAccessConfiguration`

    Describes the network details of the fleet or image builder instance.

    - **EniPrivateIpAddress** *(string) --*

      The private IP address of the elastic network interface that is attached to instances in
      your VPC.

    - **EniId** *(string) --*

      The resource identifier of the elastic network interface that is attached to instances in
      your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef
):
    """
    Type definition for `ClientDeleteImageBuilderResponseImageBuilder` `StateChangeReason`

    The reason why the last state change occurred.

    - **Code** *(string) --*

      The state change reason code.

    - **Message** *(string) --*

      The state change reason message.
    """


_ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef
):
    """
    Type definition for `ClientDeleteImageBuilderResponseImageBuilder` `VpcConfig`

    The VPC configuration of the image builder.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image
      builder instances use one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_ClientDeleteImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": str,
        "IamRoleArn": str,
        "State": str,
        "StateChangeReason": ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[
            ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef
        ],
    },
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderTypeDef
):
    """
    Type definition for `ClientDeleteImageBuilderResponse` `ImageBuilder`

    Information about the image builder.

    - **Name** *(string) --*

      The name of the image builder.

    - **Arn** *(string) --*

      The ARN for the image builder.

    - **ImageArn** *(string) --*

      The ARN of the image from which this builder was created.

    - **Description** *(string) --*

      The description to display.

    - **DisplayName** *(string) --*

      The image builder name to display.

    - **VpcConfig** *(dict) --*

      The VPC configuration of the image builder.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets to which a network interface is attached from the fleet
        instance or image builder instance. Fleet instances use one or more subnets. Image
        builder instances use one subnet.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        The identifiers of the security groups for the fleet or image builder.

        - *(string) --*

    - **InstanceType** *(string) --*

      The instance type for the image builder. The following instance types are available:

      * stream.standard.medium

      * stream.standard.large

      * stream.compute.large

      * stream.compute.xlarge

      * stream.compute.2xlarge

      * stream.compute.4xlarge

      * stream.compute.8xlarge

      * stream.memory.large

      * stream.memory.xlarge

      * stream.memory.2xlarge

      * stream.memory.4xlarge

      * stream.memory.8xlarge

      * stream.graphics-design.large

      * stream.graphics-design.xlarge

      * stream.graphics-design.2xlarge

      * stream.graphics-design.4xlarge

      * stream.graphics-desktop.2xlarge

      * stream.graphics-pro.4xlarge

      * stream.graphics-pro.8xlarge

      * stream.graphics-pro.16xlarge

    - **Platform** *(string) --*

      The operating system platform of the image builder.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that is applied to the image builder. To assume a role, the image
      builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes
      the ARN of the role to use. The operation creates a new session with temporary credentials.
      AppStream 2.0 retrieves the temporary credentials and creates the
      **AppStream_Machine_Role** credential profile on the instance.

      For more information, see `Using an IAM Role to Grant Permissions to Applications and
      Scripts Running on AppStream 2.0 Streaming Instances
      <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
      in the *Amazon AppStream 2.0 Administration Guide* .

    - **State** *(string) --*

      The state of the image builder.

    - **StateChangeReason** *(dict) --*

      The reason why the last state change occurred.

      - **Code** *(string) --*

        The state change reason code.

      - **Message** *(string) --*

        The state change reason message.

    - **CreatedTime** *(datetime) --*

      The time stamp when the image builder was created.

    - **EnableDefaultInternetAccess** *(boolean) --*

      Enables or disables default internet access for the image builder.

    - **DomainJoinInfo** *(dict) --*

      The name of the directory and organizational unit (OU) to use to join the image builder to
      a Microsoft Active Directory domain.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedName** *(string) --*

        The distinguished name of the organizational unit for computer accounts.

    - **NetworkAccessConfiguration** *(dict) --*

      Describes the network details of the fleet or image builder instance.

      - **EniPrivateIpAddress** *(string) --*

        The private IP address of the elastic network interface that is attached to instances in
        your VPC.

      - **EniId** *(string) --*

        The resource identifier of the elastic network interface that is attached to instances in
        your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

    - **ImageBuilderErrors** *(list) --*

      The image builder errors.

      - *(dict) --*

        Describes a resource error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

        - **ErrorTimestamp** *(datetime) --*

          The time the error occurred.

    - **AppstreamAgentVersion** *(string) --*

      The version of the AppStream 2.0 agent that is currently being used by the image builder.

    - **AccessEndpoints** *(list) --*

      The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
      connect to the image builder only through the specified endpoints.

      - *(dict) --*

        Describes an interface VPC endpoint (interface endpoint) that lets you create a private
        connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
        When you specify an interface endpoint for a stack, users of the stack can connect to
        AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
        image builder, administrators can connect to the image builder only through that endpoint.

        - **EndpointType** *(string) --*

          The type of interface endpoint.

        - **VpceId** *(string) --*

          The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientDeleteImageBuilderResponseTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientDeleteImageBuilderResponseImageBuilderTypeDef},
    total=False,
)


class ClientDeleteImageBuilderResponseTypeDef(_ClientDeleteImageBuilderResponseTypeDef):
    """
    Type definition for `ClientDeleteImageBuilder` `Response`

    - **ImageBuilder** *(dict) --*

      Information about the image builder.

      - **Name** *(string) --*

        The name of the image builder.

      - **Arn** *(string) --*

        The ARN for the image builder.

      - **ImageArn** *(string) --*

        The ARN of the image from which this builder was created.

      - **Description** *(string) --*

        The description to display.

      - **DisplayName** *(string) --*

        The image builder name to display.

      - **VpcConfig** *(dict) --*

        The VPC configuration of the image builder.

        - **SubnetIds** *(list) --*

          The identifiers of the subnets to which a network interface is attached from the fleet
          instance or image builder instance. Fleet instances use one or more subnets. Image
          builder instances use one subnet.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          The identifiers of the security groups for the fleet or image builder.

          - *(string) --*

      - **InstanceType** *(string) --*

        The instance type for the image builder. The following instance types are available:

        * stream.standard.medium

        * stream.standard.large

        * stream.compute.large

        * stream.compute.xlarge

        * stream.compute.2xlarge

        * stream.compute.4xlarge

        * stream.compute.8xlarge

        * stream.memory.large

        * stream.memory.xlarge

        * stream.memory.2xlarge

        * stream.memory.4xlarge

        * stream.memory.8xlarge

        * stream.graphics-design.large

        * stream.graphics-design.xlarge

        * stream.graphics-design.2xlarge

        * stream.graphics-design.4xlarge

        * stream.graphics-desktop.2xlarge

        * stream.graphics-pro.4xlarge

        * stream.graphics-pro.8xlarge

        * stream.graphics-pro.16xlarge

      - **Platform** *(string) --*

        The operating system platform of the image builder.

      - **IamRoleArn** *(string) --*

        The ARN of the IAM role that is applied to the image builder. To assume a role, the image
        builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes
        the ARN of the role to use. The operation creates a new session with temporary credentials.
        AppStream 2.0 retrieves the temporary credentials and creates the
        **AppStream_Machine_Role** credential profile on the instance.

        For more information, see `Using an IAM Role to Grant Permissions to Applications and
        Scripts Running on AppStream 2.0 Streaming Instances
        <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
        in the *Amazon AppStream 2.0 Administration Guide* .

      - **State** *(string) --*

        The state of the image builder.

      - **StateChangeReason** *(dict) --*

        The reason why the last state change occurred.

        - **Code** *(string) --*

          The state change reason code.

        - **Message** *(string) --*

          The state change reason message.

      - **CreatedTime** *(datetime) --*

        The time stamp when the image builder was created.

      - **EnableDefaultInternetAccess** *(boolean) --*

        Enables or disables default internet access for the image builder.

      - **DomainJoinInfo** *(dict) --*

        The name of the directory and organizational unit (OU) to use to join the image builder to
        a Microsoft Active Directory domain.

        - **DirectoryName** *(string) --*

          The fully qualified name of the directory (for example, corp.example.com).

        - **OrganizationalUnitDistinguishedName** *(string) --*

          The distinguished name of the organizational unit for computer accounts.

      - **NetworkAccessConfiguration** *(dict) --*

        Describes the network details of the fleet or image builder instance.

        - **EniPrivateIpAddress** *(string) --*

          The private IP address of the elastic network interface that is attached to instances in
          your VPC.

        - **EniId** *(string) --*

          The resource identifier of the elastic network interface that is attached to instances in
          your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

      - **ImageBuilderErrors** *(list) --*

        The image builder errors.

        - *(dict) --*

          Describes a resource error.

          - **ErrorCode** *(string) --*

            The error code.

          - **ErrorMessage** *(string) --*

            The error message.

          - **ErrorTimestamp** *(datetime) --*

            The time the error occurred.

      - **AppstreamAgentVersion** *(string) --*

        The version of the AppStream 2.0 agent that is currently being used by the image builder.

      - **AccessEndpoints** *(list) --*

        The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
        connect to the image builder only through the specified endpoints.

        - *(dict) --*

          Describes an interface VPC endpoint (interface endpoint) that lets you create a private
          connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
          When you specify an interface endpoint for a stack, users of the stack can connect to
          AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
          image builder, administrators can connect to the image builder only through that endpoint.

          - **EndpointType** *(string) --*

            The type of interface endpoint.

          - **VpceId** *(string) --*

            The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientDeleteImageResponseImageApplicationsTypeDef = TypedDict(
    "_ClientDeleteImageResponseImageApplicationsTypeDef",
    {
        "Name": str,
        "DisplayName": str,
        "IconURL": str,
        "LaunchPath": str,
        "LaunchParameters": str,
        "Enabled": bool,
        "Metadata": Dict[str, str],
    },
    total=False,
)


class ClientDeleteImageResponseImageApplicationsTypeDef(
    _ClientDeleteImageResponseImageApplicationsTypeDef
):
    """
    Type definition for `ClientDeleteImageResponseImage` `Applications`

    Describes an application in the application catalog.

    - **Name** *(string) --*

      The name of the application.

    - **DisplayName** *(string) --*

      The application name to display.

    - **IconURL** *(string) --*

      The URL for the application icon. This URL might be time-limited.

    - **LaunchPath** *(string) --*

      The path to the application executable in the instance.

    - **LaunchParameters** *(string) --*

      The arguments that are passed to the application at launch.

    - **Enabled** *(boolean) --*

      If there is a problem, the application can be disabled after image creation.

    - **Metadata** *(dict) --*

      Additional attributes that describe the application.

      - *(string) --*

        - *(string) --*
    """


_ClientDeleteImageResponseImageImagePermissionsTypeDef = TypedDict(
    "_ClientDeleteImageResponseImageImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)


class ClientDeleteImageResponseImageImagePermissionsTypeDef(
    _ClientDeleteImageResponseImageImagePermissionsTypeDef
):
    """
    Type definition for `ClientDeleteImageResponseImage` `ImagePermissions`

    The permissions to provide to the destination AWS account for the specified image.

    - **allowFleet** *(boolean) --*

      Indicates whether the image can be used for a fleet.

    - **allowImageBuilder** *(boolean) --*

      Indicates whether the image can be used for an image builder.
    """


_ClientDeleteImageResponseImageStateChangeReasonTypeDef = TypedDict(
    "_ClientDeleteImageResponseImageStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientDeleteImageResponseImageStateChangeReasonTypeDef(
    _ClientDeleteImageResponseImageStateChangeReasonTypeDef
):
    """
    Type definition for `ClientDeleteImageResponseImage` `StateChangeReason`

    The reason why the last state change occurred.

    - **Code** *(string) --*

      The state change reason code.

    - **Message** *(string) --*

      The state change reason message.
    """


_ClientDeleteImageResponseImageTypeDef = TypedDict(
    "_ClientDeleteImageResponseImageTypeDef",
    {
        "Name": str,
        "Arn": str,
        "BaseImageArn": str,
        "DisplayName": str,
        "State": str,
        "Visibility": str,
        "ImageBuilderSupported": bool,
        "ImageBuilderName": str,
        "Platform": str,
        "Description": str,
        "StateChangeReason": ClientDeleteImageResponseImageStateChangeReasonTypeDef,
        "Applications": List[ClientDeleteImageResponseImageApplicationsTypeDef],
        "CreatedTime": datetime,
        "PublicBaseImageReleasedDate": datetime,
        "AppstreamAgentVersion": str,
        "ImagePermissions": ClientDeleteImageResponseImageImagePermissionsTypeDef,
    },
    total=False,
)


class ClientDeleteImageResponseImageTypeDef(_ClientDeleteImageResponseImageTypeDef):
    """
    Type definition for `ClientDeleteImageResponse` `Image`

    Information about the image.

    - **Name** *(string) --*

      The name of the image.

    - **Arn** *(string) --*

      The ARN of the image.

    - **BaseImageArn** *(string) --*

      The ARN of the image from which this image was created.

    - **DisplayName** *(string) --*

      The image name to display.

    - **State** *(string) --*

      The image starts in the ``PENDING`` state. If image creation succeeds, the state is
      ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .

    - **Visibility** *(string) --*

      Indicates whether the image is public or private.

    - **ImageBuilderSupported** *(boolean) --*

      Indicates whether an image builder can be launched from this image.

    - **ImageBuilderName** *(string) --*

      The name of the image builder that was used to create the private image. If the image is
      shared, this value is null.

    - **Platform** *(string) --*

      The operating system platform of the image.

    - **Description** *(string) --*

      The description to display.

    - **StateChangeReason** *(dict) --*

      The reason why the last state change occurred.

      - **Code** *(string) --*

        The state change reason code.

      - **Message** *(string) --*

        The state change reason message.

    - **Applications** *(list) --*

      The applications associated with the image.

      - *(dict) --*

        Describes an application in the application catalog.

        - **Name** *(string) --*

          The name of the application.

        - **DisplayName** *(string) --*

          The application name to display.

        - **IconURL** *(string) --*

          The URL for the application icon. This URL might be time-limited.

        - **LaunchPath** *(string) --*

          The path to the application executable in the instance.

        - **LaunchParameters** *(string) --*

          The arguments that are passed to the application at launch.

        - **Enabled** *(boolean) --*

          If there is a problem, the application can be disabled after image creation.

        - **Metadata** *(dict) --*

          Additional attributes that describe the application.

          - *(string) --*

            - *(string) --*

    - **CreatedTime** *(datetime) --*

      The time the image was created.

    - **PublicBaseImageReleasedDate** *(datetime) --*

      The release date of the public base image. For private images, this date is the release
      date of the base image from which the image was created.

    - **AppstreamAgentVersion** *(string) --*

      The version of the AppStream 2.0 agent to use for instances that are launched from this
      image.

    - **ImagePermissions** *(dict) --*

      The permissions to provide to the destination AWS account for the specified image.

      - **allowFleet** *(boolean) --*

        Indicates whether the image can be used for a fleet.

      - **allowImageBuilder** *(boolean) --*

        Indicates whether the image can be used for an image builder.
    """


_ClientDeleteImageResponseTypeDef = TypedDict(
    "_ClientDeleteImageResponseTypeDef",
    {"Image": ClientDeleteImageResponseImageTypeDef},
    total=False,
)


class ClientDeleteImageResponseTypeDef(_ClientDeleteImageResponseTypeDef):
    """
    Type definition for `ClientDeleteImage` `Response`

    - **Image** *(dict) --*

      Information about the image.

      - **Name** *(string) --*

        The name of the image.

      - **Arn** *(string) --*

        The ARN of the image.

      - **BaseImageArn** *(string) --*

        The ARN of the image from which this image was created.

      - **DisplayName** *(string) --*

        The image name to display.

      - **State** *(string) --*

        The image starts in the ``PENDING`` state. If image creation succeeds, the state is
        ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .

      - **Visibility** *(string) --*

        Indicates whether the image is public or private.

      - **ImageBuilderSupported** *(boolean) --*

        Indicates whether an image builder can be launched from this image.

      - **ImageBuilderName** *(string) --*

        The name of the image builder that was used to create the private image. If the image is
        shared, this value is null.

      - **Platform** *(string) --*

        The operating system platform of the image.

      - **Description** *(string) --*

        The description to display.

      - **StateChangeReason** *(dict) --*

        The reason why the last state change occurred.

        - **Code** *(string) --*

          The state change reason code.

        - **Message** *(string) --*

          The state change reason message.

      - **Applications** *(list) --*

        The applications associated with the image.

        - *(dict) --*

          Describes an application in the application catalog.

          - **Name** *(string) --*

            The name of the application.

          - **DisplayName** *(string) --*

            The application name to display.

          - **IconURL** *(string) --*

            The URL for the application icon. This URL might be time-limited.

          - **LaunchPath** *(string) --*

            The path to the application executable in the instance.

          - **LaunchParameters** *(string) --*

            The arguments that are passed to the application at launch.

          - **Enabled** *(boolean) --*

            If there is a problem, the application can be disabled after image creation.

          - **Metadata** *(dict) --*

            Additional attributes that describe the application.

            - *(string) --*

              - *(string) --*

      - **CreatedTime** *(datetime) --*

        The time the image was created.

      - **PublicBaseImageReleasedDate** *(datetime) --*

        The release date of the public base image. For private images, this date is the release
        date of the base image from which the image was created.

      - **AppstreamAgentVersion** *(string) --*

        The version of the AppStream 2.0 agent to use for instances that are launched from this
        image.

      - **ImagePermissions** *(dict) --*

        The permissions to provide to the destination AWS account for the specified image.

        - **allowFleet** *(boolean) --*

          Indicates whether the image can be used for a fleet.

        - **allowImageBuilder** *(boolean) --*

          Indicates whether the image can be used for an image builder.
    """


_ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef = TypedDict(
    "_ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)


class ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef(
    _ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef
):
    """
    Type definition for `ClientDescribeDirectoryConfigsResponseDirectoryConfigs` `ServiceAccountCredentials`

    The credentials for the service account used by the fleet or image builder to connect to
    the directory.

    - **AccountName** *(string) --*

      The user name of the account. This account must have the following privileges: create
      computer objects, join computers to the domain, and change/reset the password on
      descendant computer objects for the organizational units specified.

    - **AccountPassword** *(string) --*

      The password for the account.
    """


_ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef = TypedDict(
    "_ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef(
    _ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef
):
    """
    Type definition for `ClientDescribeDirectoryConfigsResponse` `DirectoryConfigs`

    Describes the configuration information required to join fleets and image builders to
    Microsoft Active Directory domains.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedNames** *(list) --*

      The distinguished names of the organizational units for computer accounts.

      - *(string) --*

    - **ServiceAccountCredentials** *(dict) --*

      The credentials for the service account used by the fleet or image builder to connect to
      the directory.

      - **AccountName** *(string) --*

        The user name of the account. This account must have the following privileges: create
        computer objects, join computers to the domain, and change/reset the password on
        descendant computer objects for the organizational units specified.

      - **AccountPassword** *(string) --*

        The password for the account.

    - **CreatedTime** *(datetime) --*

      The time the directory configuration was created.
    """


_ClientDescribeDirectoryConfigsResponseTypeDef = TypedDict(
    "_ClientDescribeDirectoryConfigsResponseTypeDef",
    {
        "DirectoryConfigs": List[
            ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeDirectoryConfigsResponseTypeDef(
    _ClientDescribeDirectoryConfigsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDirectoryConfigs` `Response`

    - **DirectoryConfigs** *(list) --*

      Information about the directory configurations. Note that although the response syntax in
      this topic includes the account password, this password is not returned in the actual
      response.

      - *(dict) --*

        Describes the configuration information required to join fleets and image builders to
        Microsoft Active Directory domains.

        - **DirectoryName** *(string) --*

          The fully qualified name of the directory (for example, corp.example.com).

        - **OrganizationalUnitDistinguishedNames** *(list) --*

          The distinguished names of the organizational units for computer accounts.

          - *(string) --*

        - **ServiceAccountCredentials** *(dict) --*

          The credentials for the service account used by the fleet or image builder to connect to
          the directory.

          - **AccountName** *(string) --*

            The user name of the account. This account must have the following privileges: create
            computer objects, join computers to the domain, and change/reset the password on
            descendant computer objects for the organizational units specified.

          - **AccountPassword** *(string) --*

            The password for the account.

        - **CreatedTime** *(datetime) --*

          The time the directory configuration was created.

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)


class ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef(
    _ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef
):
    """
    Type definition for `ClientDescribeFleetsResponseFleets` `ComputeCapacityStatus`

    The capacity status for the fleet.

    - **Desired** *(integer) --*

      The desired number of streaming instances.

    - **Running** *(integer) --*

      The total number of simultaneous streaming instances that are running.

    - **InUse** *(integer) --*

      The number of instances in use for streaming.

    - **Available** *(integer) --*

      The number of currently available instances that can be used to stream sessions.
    """


_ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef(
    _ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef
):
    """
    Type definition for `ClientDescribeFleetsResponseFleets` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the fleet to a
    Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef(
    _ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef
):
    """
    Type definition for `ClientDescribeFleetsResponseFleets` `FleetErrors`

    Describes a fleet error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientDescribeFleetsResponseFleetsVpcConfigTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseFleetsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientDescribeFleetsResponseFleetsVpcConfigTypeDef(
    _ClientDescribeFleetsResponseFleetsVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeFleetsResponseFleets` `VpcConfig`

    The VPC configuration for the fleet.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image
      builder instances use one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_ClientDescribeFleetsResponseFleetsTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseFleetsTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "InstanceType": str,
        "FleetType": str,
        "ComputeCapacityStatus": ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef,
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "State": str,
        "VpcConfig": ClientDescribeFleetsResponseFleetsVpcConfigTypeDef,
        "CreatedTime": datetime,
        "FleetErrors": List[ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef,
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
    },
    total=False,
)


class ClientDescribeFleetsResponseFleetsTypeDef(
    _ClientDescribeFleetsResponseFleetsTypeDef
):
    """
    Type definition for `ClientDescribeFleetsResponse` `Fleets`

    Describes a fleet.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the fleet.

    - **Name** *(string) --*

      The name of the fleet.

    - **DisplayName** *(string) --*

      The fleet name to display.

    - **Description** *(string) --*

      The description to display.

    - **ImageName** *(string) --*

      The name of the image used to create the fleet.

    - **ImageArn** *(string) --*

      The ARN for the public, private, or shared image.

    - **InstanceType** *(string) --*

      The instance type to use when launching fleet instances. The following instance types are
      available:

      * stream.standard.medium

      * stream.standard.large

      * stream.compute.large

      * stream.compute.xlarge

      * stream.compute.2xlarge

      * stream.compute.4xlarge

      * stream.compute.8xlarge

      * stream.memory.large

      * stream.memory.xlarge

      * stream.memory.2xlarge

      * stream.memory.4xlarge

      * stream.memory.8xlarge

      * stream.graphics-design.large

      * stream.graphics-design.xlarge

      * stream.graphics-design.2xlarge

      * stream.graphics-design.4xlarge

      * stream.graphics-desktop.2xlarge

      * stream.graphics-pro.4xlarge

      * stream.graphics-pro.8xlarge

      * stream.graphics-pro.16xlarge

    - **FleetType** *(string) --*

      The fleet type.

        ALWAYS_ON

      Provides users with instant-on access to their apps. You are charged for all running
      instances in your fleet, even if no users are streaming apps.

        ON_DEMAND

      Provide users with access to applications after they connect, which takes one to two
      minutes. You are charged for instance streaming when users are connected and a small
      hourly fee for instances that are not streaming apps.

    - **ComputeCapacityStatus** *(dict) --*

      The capacity status for the fleet.

      - **Desired** *(integer) --*

        The desired number of streaming instances.

      - **Running** *(integer) --*

        The total number of simultaneous streaming instances that are running.

      - **InUse** *(integer) --*

        The number of instances in use for streaming.

      - **Available** *(integer) --*

        The number of currently available instances that can be used to stream sessions.

    - **MaxUserDurationInSeconds** *(integer) --*

      The maximum amount of time that a streaming session can remain active, in seconds. If
      users are still connected to a streaming instance five minutes before this limit is
      reached, they are prompted to save any open documents before being disconnected. After
      this time elapses, the instance is terminated and replaced by a new instance.

      Specify a value between 600 and 360000.

    - **DisconnectTimeoutInSeconds** *(integer) --*

      The amount of time that a streaming session remains active after users disconnect. If
      they try to reconnect to the streaming session after a disconnection or network
      interruption within this time interval, they are connected to their previous session.
      Otherwise, they are connected to a new session with a new streaming instance.

      Specify a value between 60 and 360000.

    - **State** *(string) --*

      The current state for the fleet.

    - **VpcConfig** *(dict) --*

      The VPC configuration for the fleet.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets to which a network interface is attached from the fleet
        instance or image builder instance. Fleet instances use one or more subnets. Image
        builder instances use one subnet.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        The identifiers of the security groups for the fleet or image builder.

        - *(string) --*

    - **CreatedTime** *(datetime) --*

      The time the fleet was created.

    - **FleetErrors** *(list) --*

      The fleet errors.

      - *(dict) --*

        Describes a fleet error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

    - **EnableDefaultInternetAccess** *(boolean) --*

      Indicates whether default internet access is enabled for the fleet.

    - **DomainJoinInfo** *(dict) --*

      The name of the directory and organizational unit (OU) to use to join the fleet to a
      Microsoft Active Directory domain.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedName** *(string) --*

        The distinguished name of the organizational unit for computer accounts.

    - **IdleDisconnectTimeoutInSeconds** *(integer) --*

      The amount of time that users can be idle (inactive) before they are disconnected from
      their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins.
      Users are notified before they are disconnected due to inactivity. If users try to
      reconnect to the streaming session before the time interval specified in
      ``DisconnectTimeoutInSeconds`` elapses, they are connected to their previous session.
      Users are considered idle when they stop providing keyboard or mouse input during their
      streaming session. File uploads and downloads, audio in, audio out, and pixels changing
      do not qualify as user activity. If users continue to be idle after the time interval in
      ``IdleDisconnectTimeoutInSeconds`` elapses, they are disconnected.

      To prevent users from being disconnected due to inactivity, specify a value of 0.
      Otherwise, specify a value between 60 and 3600. The default value is 0.

      .. note::

        If you enable this feature, we recommend that you specify a value that corresponds
        exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do
        this, the value is rounded to the nearest minute. For example, if you specify a value
        of 70, users are disconnected after 1 minute of inactivity. If you specify a value that
        is at the midpoint between two different minutes, the value is rounded up. For example,
        if you specify a value of 90, users are disconnected after 2 minutes of inactivity.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet
      instance calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and
      passes the ARN of the role to use. The operation creates a new session with temporary
      credentials. AppStream 2.0 retrieves the temporary credentials and creates the
      **AppStream_Machine_Role** credential profile on the instance.

      For more information, see `Using an IAM Role to Grant Permissions to Applications and
      Scripts Running on AppStream 2.0 Streaming Instances
      <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
      in the *Amazon AppStream 2.0 Administration Guide* .
    """


_ClientDescribeFleetsResponseTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseTypeDef",
    {"Fleets": List[ClientDescribeFleetsResponseFleetsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeFleetsResponseTypeDef(_ClientDescribeFleetsResponseTypeDef):
    """
    Type definition for `ClientDescribeFleets` `Response`

    - **Fleets** *(list) --*

      Information about the fleets.

      - *(dict) --*

        Describes a fleet.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) for the fleet.

        - **Name** *(string) --*

          The name of the fleet.

        - **DisplayName** *(string) --*

          The fleet name to display.

        - **Description** *(string) --*

          The description to display.

        - **ImageName** *(string) --*

          The name of the image used to create the fleet.

        - **ImageArn** *(string) --*

          The ARN for the public, private, or shared image.

        - **InstanceType** *(string) --*

          The instance type to use when launching fleet instances. The following instance types are
          available:

          * stream.standard.medium

          * stream.standard.large

          * stream.compute.large

          * stream.compute.xlarge

          * stream.compute.2xlarge

          * stream.compute.4xlarge

          * stream.compute.8xlarge

          * stream.memory.large

          * stream.memory.xlarge

          * stream.memory.2xlarge

          * stream.memory.4xlarge

          * stream.memory.8xlarge

          * stream.graphics-design.large

          * stream.graphics-design.xlarge

          * stream.graphics-design.2xlarge

          * stream.graphics-design.4xlarge

          * stream.graphics-desktop.2xlarge

          * stream.graphics-pro.4xlarge

          * stream.graphics-pro.8xlarge

          * stream.graphics-pro.16xlarge

        - **FleetType** *(string) --*

          The fleet type.

            ALWAYS_ON

          Provides users with instant-on access to their apps. You are charged for all running
          instances in your fleet, even if no users are streaming apps.

            ON_DEMAND

          Provide users with access to applications after they connect, which takes one to two
          minutes. You are charged for instance streaming when users are connected and a small
          hourly fee for instances that are not streaming apps.

        - **ComputeCapacityStatus** *(dict) --*

          The capacity status for the fleet.

          - **Desired** *(integer) --*

            The desired number of streaming instances.

          - **Running** *(integer) --*

            The total number of simultaneous streaming instances that are running.

          - **InUse** *(integer) --*

            The number of instances in use for streaming.

          - **Available** *(integer) --*

            The number of currently available instances that can be used to stream sessions.

        - **MaxUserDurationInSeconds** *(integer) --*

          The maximum amount of time that a streaming session can remain active, in seconds. If
          users are still connected to a streaming instance five minutes before this limit is
          reached, they are prompted to save any open documents before being disconnected. After
          this time elapses, the instance is terminated and replaced by a new instance.

          Specify a value between 600 and 360000.

        - **DisconnectTimeoutInSeconds** *(integer) --*

          The amount of time that a streaming session remains active after users disconnect. If
          they try to reconnect to the streaming session after a disconnection or network
          interruption within this time interval, they are connected to their previous session.
          Otherwise, they are connected to a new session with a new streaming instance.

          Specify a value between 60 and 360000.

        - **State** *(string) --*

          The current state for the fleet.

        - **VpcConfig** *(dict) --*

          The VPC configuration for the fleet.

          - **SubnetIds** *(list) --*

            The identifiers of the subnets to which a network interface is attached from the fleet
            instance or image builder instance. Fleet instances use one or more subnets. Image
            builder instances use one subnet.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            The identifiers of the security groups for the fleet or image builder.

            - *(string) --*

        - **CreatedTime** *(datetime) --*

          The time the fleet was created.

        - **FleetErrors** *(list) --*

          The fleet errors.

          - *(dict) --*

            Describes a fleet error.

            - **ErrorCode** *(string) --*

              The error code.

            - **ErrorMessage** *(string) --*

              The error message.

        - **EnableDefaultInternetAccess** *(boolean) --*

          Indicates whether default internet access is enabled for the fleet.

        - **DomainJoinInfo** *(dict) --*

          The name of the directory and organizational unit (OU) to use to join the fleet to a
          Microsoft Active Directory domain.

          - **DirectoryName** *(string) --*

            The fully qualified name of the directory (for example, corp.example.com).

          - **OrganizationalUnitDistinguishedName** *(string) --*

            The distinguished name of the organizational unit for computer accounts.

        - **IdleDisconnectTimeoutInSeconds** *(integer) --*

          The amount of time that users can be idle (inactive) before they are disconnected from
          their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins.
          Users are notified before they are disconnected due to inactivity. If users try to
          reconnect to the streaming session before the time interval specified in
          ``DisconnectTimeoutInSeconds`` elapses, they are connected to their previous session.
          Users are considered idle when they stop providing keyboard or mouse input during their
          streaming session. File uploads and downloads, audio in, audio out, and pixels changing
          do not qualify as user activity. If users continue to be idle after the time interval in
          ``IdleDisconnectTimeoutInSeconds`` elapses, they are disconnected.

          To prevent users from being disconnected due to inactivity, specify a value of 0.
          Otherwise, specify a value between 60 and 3600. The default value is 0.

          .. note::

            If you enable this feature, we recommend that you specify a value that corresponds
            exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do
            this, the value is rounded to the nearest minute. For example, if you specify a value
            of 70, users are disconnected after 1 minute of inactivity. If you specify a value that
            is at the midpoint between two different minutes, the value is rounded up. For example,
            if you specify a value of 90, users are disconnected after 2 minutes of inactivity.

        - **IamRoleArn** *(string) --*

          The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet
          instance calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and
          passes the ARN of the role to use. The operation creates a new session with temporary
          credentials. AppStream 2.0 retrieves the temporary credentials and creates the
          **AppStream_Machine_Role** credential profile on the instance.

          For more information, see `Using an IAM Role to Grant Permissions to Applications and
          Scripts Running on AppStream 2.0 Streaming Instances
          <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
          in the *Amazon AppStream 2.0 Administration Guide* .

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef
):
    """
    Type definition for `ClientDescribeImageBuildersResponseImageBuilders` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
    When you specify an interface endpoint for a stack, users of the stack can connect to
    AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
    image builder, administrators can connect to the image builder only through that
    endpoint.

    - **EndpointType** *(string) --*

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef
):
    """
    Type definition for `ClientDescribeImageBuildersResponseImageBuilders` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the image builder
    to a Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "ErrorTimestamp": datetime},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef
):
    """
    Type definition for `ClientDescribeImageBuildersResponseImageBuilders` `ImageBuilderErrors`

    Describes a resource error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.

    - **ErrorTimestamp** *(datetime) --*

      The time the error occurred.
    """


_ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeImageBuildersResponseImageBuilders` `NetworkAccessConfiguration`

    Describes the network details of the fleet or image builder instance.

    - **EniPrivateIpAddress** *(string) --*

      The private IP address of the elastic network interface that is attached to instances
      in your VPC.

    - **EniId** *(string) --*

      The resource identifier of the elastic network interface that is attached to instances
      in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef
):
    """
    Type definition for `ClientDescribeImageBuildersResponseImageBuilders` `StateChangeReason`

    The reason why the last state change occurred.

    - **Code** *(string) --*

      The state change reason code.

    - **Message** *(string) --*

      The state change reason message.
    """


_ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeImageBuildersResponseImageBuilders` `VpcConfig`

    The VPC configuration of the image builder.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image
      builder instances use one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_ClientDescribeImageBuildersResponseImageBuildersTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": str,
        "IamRoleArn": str,
        "State": str,
        "StateChangeReason": ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[
            ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersTypeDef
):
    """
    Type definition for `ClientDescribeImageBuildersResponse` `ImageBuilders`

    Describes a virtual machine that is used to create an image.

    - **Name** *(string) --*

      The name of the image builder.

    - **Arn** *(string) --*

      The ARN for the image builder.

    - **ImageArn** *(string) --*

      The ARN of the image from which this builder was created.

    - **Description** *(string) --*

      The description to display.

    - **DisplayName** *(string) --*

      The image builder name to display.

    - **VpcConfig** *(dict) --*

      The VPC configuration of the image builder.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets to which a network interface is attached from the fleet
        instance or image builder instance. Fleet instances use one or more subnets. Image
        builder instances use one subnet.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        The identifiers of the security groups for the fleet or image builder.

        - *(string) --*

    - **InstanceType** *(string) --*

      The instance type for the image builder. The following instance types are available:

      * stream.standard.medium

      * stream.standard.large

      * stream.compute.large

      * stream.compute.xlarge

      * stream.compute.2xlarge

      * stream.compute.4xlarge

      * stream.compute.8xlarge

      * stream.memory.large

      * stream.memory.xlarge

      * stream.memory.2xlarge

      * stream.memory.4xlarge

      * stream.memory.8xlarge

      * stream.graphics-design.large

      * stream.graphics-design.xlarge

      * stream.graphics-design.2xlarge

      * stream.graphics-design.4xlarge

      * stream.graphics-desktop.2xlarge

      * stream.graphics-pro.4xlarge

      * stream.graphics-pro.8xlarge

      * stream.graphics-pro.16xlarge

    - **Platform** *(string) --*

      The operating system platform of the image builder.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that is applied to the image builder. To assume a role, the image
      builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and
      passes the ARN of the role to use. The operation creates a new session with temporary
      credentials. AppStream 2.0 retrieves the temporary credentials and creates the
      **AppStream_Machine_Role** credential profile on the instance.

      For more information, see `Using an IAM Role to Grant Permissions to Applications and
      Scripts Running on AppStream 2.0 Streaming Instances
      <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
      in the *Amazon AppStream 2.0 Administration Guide* .

    - **State** *(string) --*

      The state of the image builder.

    - **StateChangeReason** *(dict) --*

      The reason why the last state change occurred.

      - **Code** *(string) --*

        The state change reason code.

      - **Message** *(string) --*

        The state change reason message.

    - **CreatedTime** *(datetime) --*

      The time stamp when the image builder was created.

    - **EnableDefaultInternetAccess** *(boolean) --*

      Enables or disables default internet access for the image builder.

    - **DomainJoinInfo** *(dict) --*

      The name of the directory and organizational unit (OU) to use to join the image builder
      to a Microsoft Active Directory domain.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedName** *(string) --*

        The distinguished name of the organizational unit for computer accounts.

    - **NetworkAccessConfiguration** *(dict) --*

      Describes the network details of the fleet or image builder instance.

      - **EniPrivateIpAddress** *(string) --*

        The private IP address of the elastic network interface that is attached to instances
        in your VPC.

      - **EniId** *(string) --*

        The resource identifier of the elastic network interface that is attached to instances
        in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

    - **ImageBuilderErrors** *(list) --*

      The image builder errors.

      - *(dict) --*

        Describes a resource error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

        - **ErrorTimestamp** *(datetime) --*

          The time the error occurred.

    - **AppstreamAgentVersion** *(string) --*

      The version of the AppStream 2.0 agent that is currently being used by the image builder.

    - **AccessEndpoints** *(list) --*

      The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
      connect to the image builder only through the specified endpoints.

      - *(dict) --*

        Describes an interface VPC endpoint (interface endpoint) that lets you create a private
        connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
        When you specify an interface endpoint for a stack, users of the stack can connect to
        AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
        image builder, administrators can connect to the image builder only through that
        endpoint.

        - **EndpointType** *(string) --*

          The type of interface endpoint.

        - **VpceId** *(string) --*

          The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientDescribeImageBuildersResponseTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseTypeDef",
    {
        "ImageBuilders": List[ClientDescribeImageBuildersResponseImageBuildersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeImageBuildersResponseTypeDef(
    _ClientDescribeImageBuildersResponseTypeDef
):
    """
    Type definition for `ClientDescribeImageBuilders` `Response`

    - **ImageBuilders** *(list) --*

      Information about the image builders.

      - *(dict) --*

        Describes a virtual machine that is used to create an image.

        - **Name** *(string) --*

          The name of the image builder.

        - **Arn** *(string) --*

          The ARN for the image builder.

        - **ImageArn** *(string) --*

          The ARN of the image from which this builder was created.

        - **Description** *(string) --*

          The description to display.

        - **DisplayName** *(string) --*

          The image builder name to display.

        - **VpcConfig** *(dict) --*

          The VPC configuration of the image builder.

          - **SubnetIds** *(list) --*

            The identifiers of the subnets to which a network interface is attached from the fleet
            instance or image builder instance. Fleet instances use one or more subnets. Image
            builder instances use one subnet.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            The identifiers of the security groups for the fleet or image builder.

            - *(string) --*

        - **InstanceType** *(string) --*

          The instance type for the image builder. The following instance types are available:

          * stream.standard.medium

          * stream.standard.large

          * stream.compute.large

          * stream.compute.xlarge

          * stream.compute.2xlarge

          * stream.compute.4xlarge

          * stream.compute.8xlarge

          * stream.memory.large

          * stream.memory.xlarge

          * stream.memory.2xlarge

          * stream.memory.4xlarge

          * stream.memory.8xlarge

          * stream.graphics-design.large

          * stream.graphics-design.xlarge

          * stream.graphics-design.2xlarge

          * stream.graphics-design.4xlarge

          * stream.graphics-desktop.2xlarge

          * stream.graphics-pro.4xlarge

          * stream.graphics-pro.8xlarge

          * stream.graphics-pro.16xlarge

        - **Platform** *(string) --*

          The operating system platform of the image builder.

        - **IamRoleArn** *(string) --*

          The ARN of the IAM role that is applied to the image builder. To assume a role, the image
          builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and
          passes the ARN of the role to use. The operation creates a new session with temporary
          credentials. AppStream 2.0 retrieves the temporary credentials and creates the
          **AppStream_Machine_Role** credential profile on the instance.

          For more information, see `Using an IAM Role to Grant Permissions to Applications and
          Scripts Running on AppStream 2.0 Streaming Instances
          <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
          in the *Amazon AppStream 2.0 Administration Guide* .

        - **State** *(string) --*

          The state of the image builder.

        - **StateChangeReason** *(dict) --*

          The reason why the last state change occurred.

          - **Code** *(string) --*

            The state change reason code.

          - **Message** *(string) --*

            The state change reason message.

        - **CreatedTime** *(datetime) --*

          The time stamp when the image builder was created.

        - **EnableDefaultInternetAccess** *(boolean) --*

          Enables or disables default internet access for the image builder.

        - **DomainJoinInfo** *(dict) --*

          The name of the directory and organizational unit (OU) to use to join the image builder
          to a Microsoft Active Directory domain.

          - **DirectoryName** *(string) --*

            The fully qualified name of the directory (for example, corp.example.com).

          - **OrganizationalUnitDistinguishedName** *(string) --*

            The distinguished name of the organizational unit for computer accounts.

        - **NetworkAccessConfiguration** *(dict) --*

          Describes the network details of the fleet or image builder instance.

          - **EniPrivateIpAddress** *(string) --*

            The private IP address of the elastic network interface that is attached to instances
            in your VPC.

          - **EniId** *(string) --*

            The resource identifier of the elastic network interface that is attached to instances
            in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

        - **ImageBuilderErrors** *(list) --*

          The image builder errors.

          - *(dict) --*

            Describes a resource error.

            - **ErrorCode** *(string) --*

              The error code.

            - **ErrorMessage** *(string) --*

              The error message.

            - **ErrorTimestamp** *(datetime) --*

              The time the error occurred.

        - **AppstreamAgentVersion** *(string) --*

          The version of the AppStream 2.0 agent that is currently being used by the image builder.

        - **AccessEndpoints** *(list) --*

          The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
          connect to the image builder only through the specified endpoints.

          - *(dict) --*

            Describes an interface VPC endpoint (interface endpoint) that lets you create a private
            connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
            When you specify an interface endpoint for a stack, users of the stack can connect to
            AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
            image builder, administrators can connect to the image builder only through that
            endpoint.

            - **EndpointType** *(string) --*

              The type of interface endpoint.

            - **VpceId** *(string) --*

              The identifier (ID) of the VPC in which the interface endpoint is used.

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef = TypedDict(
    "_ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)


class ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef(
    _ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef
):
    """
    Type definition for `ClientDescribeImagePermissionsResponseSharedImagePermissionsList` `imagePermissions`

    Describes the permissions for a shared image.

    - **allowFleet** *(boolean) --*

      Indicates whether the image can be used for a fleet.

    - **allowImageBuilder** *(boolean) --*

      Indicates whether the image can be used for an image builder.
    """


_ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef = TypedDict(
    "_ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef",
    {
        "sharedAccountId": str,
        "imagePermissions": ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef,
    },
    total=False,
)


class ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef(
    _ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef
):
    """
    Type definition for `ClientDescribeImagePermissionsResponse` `SharedImagePermissionsList`

    Describes the permissions that are available to the specified AWS account for a shared
    image.

    - **sharedAccountId** *(string) --*

      The 12-digit identifier of the AWS account with which the image is shared.

    - **imagePermissions** *(dict) --*

      Describes the permissions for a shared image.

      - **allowFleet** *(boolean) --*

        Indicates whether the image can be used for a fleet.

      - **allowImageBuilder** *(boolean) --*

        Indicates whether the image can be used for an image builder.
    """


_ClientDescribeImagePermissionsResponseTypeDef = TypedDict(
    "_ClientDescribeImagePermissionsResponseTypeDef",
    {
        "Name": str,
        "SharedImagePermissionsList": List[
            ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeImagePermissionsResponseTypeDef(
    _ClientDescribeImagePermissionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeImagePermissions` `Response`

    - **Name** *(string) --*

      The name of the private image.

    - **SharedImagePermissionsList** *(list) --*

      The permissions for a private image that you own.

      - *(dict) --*

        Describes the permissions that are available to the specified AWS account for a shared
        image.

        - **sharedAccountId** *(string) --*

          The 12-digit identifier of the AWS account with which the image is shared.

        - **imagePermissions** *(dict) --*

          Describes the permissions for a shared image.

          - **allowFleet** *(boolean) --*

            Indicates whether the image can be used for a fleet.

          - **allowImageBuilder** *(boolean) --*

            Indicates whether the image can be used for an image builder.

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientDescribeImagesResponseImagesApplicationsTypeDef = TypedDict(
    "_ClientDescribeImagesResponseImagesApplicationsTypeDef",
    {
        "Name": str,
        "DisplayName": str,
        "IconURL": str,
        "LaunchPath": str,
        "LaunchParameters": str,
        "Enabled": bool,
        "Metadata": Dict[str, str],
    },
    total=False,
)


class ClientDescribeImagesResponseImagesApplicationsTypeDef(
    _ClientDescribeImagesResponseImagesApplicationsTypeDef
):
    """
    Type definition for `ClientDescribeImagesResponseImages` `Applications`

    Describes an application in the application catalog.

    - **Name** *(string) --*

      The name of the application.

    - **DisplayName** *(string) --*

      The application name to display.

    - **IconURL** *(string) --*

      The URL for the application icon. This URL might be time-limited.

    - **LaunchPath** *(string) --*

      The path to the application executable in the instance.

    - **LaunchParameters** *(string) --*

      The arguments that are passed to the application at launch.

    - **Enabled** *(boolean) --*

      If there is a problem, the application can be disabled after image creation.

    - **Metadata** *(dict) --*

      Additional attributes that describe the application.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeImagesResponseImagesImagePermissionsTypeDef = TypedDict(
    "_ClientDescribeImagesResponseImagesImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)


class ClientDescribeImagesResponseImagesImagePermissionsTypeDef(
    _ClientDescribeImagesResponseImagesImagePermissionsTypeDef
):
    """
    Type definition for `ClientDescribeImagesResponseImages` `ImagePermissions`

    The permissions to provide to the destination AWS account for the specified image.

    - **allowFleet** *(boolean) --*

      Indicates whether the image can be used for a fleet.

    - **allowImageBuilder** *(boolean) --*

      Indicates whether the image can be used for an image builder.
    """


_ClientDescribeImagesResponseImagesStateChangeReasonTypeDef = TypedDict(
    "_ClientDescribeImagesResponseImagesStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientDescribeImagesResponseImagesStateChangeReasonTypeDef(
    _ClientDescribeImagesResponseImagesStateChangeReasonTypeDef
):
    """
    Type definition for `ClientDescribeImagesResponseImages` `StateChangeReason`

    The reason why the last state change occurred.

    - **Code** *(string) --*

      The state change reason code.

    - **Message** *(string) --*

      The state change reason message.
    """


_ClientDescribeImagesResponseImagesTypeDef = TypedDict(
    "_ClientDescribeImagesResponseImagesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "BaseImageArn": str,
        "DisplayName": str,
        "State": str,
        "Visibility": str,
        "ImageBuilderSupported": bool,
        "ImageBuilderName": str,
        "Platform": str,
        "Description": str,
        "StateChangeReason": ClientDescribeImagesResponseImagesStateChangeReasonTypeDef,
        "Applications": List[ClientDescribeImagesResponseImagesApplicationsTypeDef],
        "CreatedTime": datetime,
        "PublicBaseImageReleasedDate": datetime,
        "AppstreamAgentVersion": str,
        "ImagePermissions": ClientDescribeImagesResponseImagesImagePermissionsTypeDef,
    },
    total=False,
)


class ClientDescribeImagesResponseImagesTypeDef(
    _ClientDescribeImagesResponseImagesTypeDef
):
    """
    Type definition for `ClientDescribeImagesResponse` `Images`

    Describes an image.

    - **Name** *(string) --*

      The name of the image.

    - **Arn** *(string) --*

      The ARN of the image.

    - **BaseImageArn** *(string) --*

      The ARN of the image from which this image was created.

    - **DisplayName** *(string) --*

      The image name to display.

    - **State** *(string) --*

      The image starts in the ``PENDING`` state. If image creation succeeds, the state is
      ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .

    - **Visibility** *(string) --*

      Indicates whether the image is public or private.

    - **ImageBuilderSupported** *(boolean) --*

      Indicates whether an image builder can be launched from this image.

    - **ImageBuilderName** *(string) --*

      The name of the image builder that was used to create the private image. If the image is
      shared, this value is null.

    - **Platform** *(string) --*

      The operating system platform of the image.

    - **Description** *(string) --*

      The description to display.

    - **StateChangeReason** *(dict) --*

      The reason why the last state change occurred.

      - **Code** *(string) --*

        The state change reason code.

      - **Message** *(string) --*

        The state change reason message.

    - **Applications** *(list) --*

      The applications associated with the image.

      - *(dict) --*

        Describes an application in the application catalog.

        - **Name** *(string) --*

          The name of the application.

        - **DisplayName** *(string) --*

          The application name to display.

        - **IconURL** *(string) --*

          The URL for the application icon. This URL might be time-limited.

        - **LaunchPath** *(string) --*

          The path to the application executable in the instance.

        - **LaunchParameters** *(string) --*

          The arguments that are passed to the application at launch.

        - **Enabled** *(boolean) --*

          If there is a problem, the application can be disabled after image creation.

        - **Metadata** *(dict) --*

          Additional attributes that describe the application.

          - *(string) --*

            - *(string) --*

    - **CreatedTime** *(datetime) --*

      The time the image was created.

    - **PublicBaseImageReleasedDate** *(datetime) --*

      The release date of the public base image. For private images, this date is the release
      date of the base image from which the image was created.

    - **AppstreamAgentVersion** *(string) --*

      The version of the AppStream 2.0 agent to use for instances that are launched from this
      image.

    - **ImagePermissions** *(dict) --*

      The permissions to provide to the destination AWS account for the specified image.

      - **allowFleet** *(boolean) --*

        Indicates whether the image can be used for a fleet.

      - **allowImageBuilder** *(boolean) --*

        Indicates whether the image can be used for an image builder.
    """


_ClientDescribeImagesResponseTypeDef = TypedDict(
    "_ClientDescribeImagesResponseTypeDef",
    {"Images": List[ClientDescribeImagesResponseImagesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeImagesResponseTypeDef(_ClientDescribeImagesResponseTypeDef):
    """
    Type definition for `ClientDescribeImages` `Response`

    - **Images** *(list) --*

      Information about the images.

      - *(dict) --*

        Describes an image.

        - **Name** *(string) --*

          The name of the image.

        - **Arn** *(string) --*

          The ARN of the image.

        - **BaseImageArn** *(string) --*

          The ARN of the image from which this image was created.

        - **DisplayName** *(string) --*

          The image name to display.

        - **State** *(string) --*

          The image starts in the ``PENDING`` state. If image creation succeeds, the state is
          ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .

        - **Visibility** *(string) --*

          Indicates whether the image is public or private.

        - **ImageBuilderSupported** *(boolean) --*

          Indicates whether an image builder can be launched from this image.

        - **ImageBuilderName** *(string) --*

          The name of the image builder that was used to create the private image. If the image is
          shared, this value is null.

        - **Platform** *(string) --*

          The operating system platform of the image.

        - **Description** *(string) --*

          The description to display.

        - **StateChangeReason** *(dict) --*

          The reason why the last state change occurred.

          - **Code** *(string) --*

            The state change reason code.

          - **Message** *(string) --*

            The state change reason message.

        - **Applications** *(list) --*

          The applications associated with the image.

          - *(dict) --*

            Describes an application in the application catalog.

            - **Name** *(string) --*

              The name of the application.

            - **DisplayName** *(string) --*

              The application name to display.

            - **IconURL** *(string) --*

              The URL for the application icon. This URL might be time-limited.

            - **LaunchPath** *(string) --*

              The path to the application executable in the instance.

            - **LaunchParameters** *(string) --*

              The arguments that are passed to the application at launch.

            - **Enabled** *(boolean) --*

              If there is a problem, the application can be disabled after image creation.

            - **Metadata** *(dict) --*

              Additional attributes that describe the application.

              - *(string) --*

                - *(string) --*

        - **CreatedTime** *(datetime) --*

          The time the image was created.

        - **PublicBaseImageReleasedDate** *(datetime) --*

          The release date of the public base image. For private images, this date is the release
          date of the base image from which the image was created.

        - **AppstreamAgentVersion** *(string) --*

          The version of the AppStream 2.0 agent to use for instances that are launched from this
          image.

        - **ImagePermissions** *(dict) --*

          The permissions to provide to the destination AWS account for the specified image.

          - **allowFleet** *(boolean) --*

            Indicates whether the image can be used for a fleet.

          - **allowImageBuilder** *(boolean) --*

            Indicates whether the image can be used for an image builder.

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef(
    _ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeSessionsResponseSessions` `NetworkAccessConfiguration`

    The network details for the streaming session.

    - **EniPrivateIpAddress** *(string) --*

      The private IP address of the elastic network interface that is attached to instances
      in your VPC.

    - **EniId** *(string) --*

      The resource identifier of the elastic network interface that is attached to instances
      in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_ClientDescribeSessionsResponseSessionsTypeDef = TypedDict(
    "_ClientDescribeSessionsResponseSessionsTypeDef",
    {
        "Id": str,
        "UserId": str,
        "StackName": str,
        "FleetName": str,
        "State": str,
        "ConnectionState": str,
        "StartTime": datetime,
        "MaxExpirationTime": datetime,
        "AuthenticationType": str,
        "NetworkAccessConfiguration": ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeSessionsResponseSessionsTypeDef(
    _ClientDescribeSessionsResponseSessionsTypeDef
):
    """
    Type definition for `ClientDescribeSessionsResponse` `Sessions`

    Describes a streaming session.

    - **Id** *(string) --*

      The identifier of the streaming session.

    - **UserId** *(string) --*

      The identifier of the user for whom the session was created.

    - **StackName** *(string) --*

      The name of the stack for the streaming session.

    - **FleetName** *(string) --*

      The name of the fleet for the streaming session.

    - **State** *(string) --*

      The current state of the streaming session.

    - **ConnectionState** *(string) --*

      Specifies whether a user is connected to the streaming session.

    - **StartTime** *(datetime) --*

      The time when a streaming instance is dedicated for the user.

    - **MaxExpirationTime** *(datetime) --*

      The time when the streaming session is set to expire. This time is based on the
      ``MaxUserDurationinSeconds`` value, which determines the maximum length of time that a
      streaming session can run. A streaming session might end earlier than the time specified
      in ``SessionMaxExpirationTime`` , when the ``DisconnectTimeOutInSeconds`` elapses or the
      user chooses to end his or her session. If the ``DisconnectTimeOutInSeconds`` elapses, or
      the user chooses to end his or her session, the streaming instance is terminated and the
      streaming session ends.

    - **AuthenticationType** *(string) --*

      The authentication method. The user is authenticated using a streaming URL (``API`` ) or
      SAML 2.0 federation (``SAML`` ).

    - **NetworkAccessConfiguration** *(dict) --*

      The network details for the streaming session.

      - **EniPrivateIpAddress** *(string) --*

        The private IP address of the elastic network interface that is attached to instances
        in your VPC.

      - **EniId** *(string) --*

        The resource identifier of the elastic network interface that is attached to instances
        in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_ClientDescribeSessionsResponseTypeDef = TypedDict(
    "_ClientDescribeSessionsResponseTypeDef",
    {"Sessions": List[ClientDescribeSessionsResponseSessionsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeSessionsResponseTypeDef(_ClientDescribeSessionsResponseTypeDef):
    """
    Type definition for `ClientDescribeSessions` `Response`

    - **Sessions** *(list) --*

      Information about the streaming sessions.

      - *(dict) --*

        Describes a streaming session.

        - **Id** *(string) --*

          The identifier of the streaming session.

        - **UserId** *(string) --*

          The identifier of the user for whom the session was created.

        - **StackName** *(string) --*

          The name of the stack for the streaming session.

        - **FleetName** *(string) --*

          The name of the fleet for the streaming session.

        - **State** *(string) --*

          The current state of the streaming session.

        - **ConnectionState** *(string) --*

          Specifies whether a user is connected to the streaming session.

        - **StartTime** *(datetime) --*

          The time when a streaming instance is dedicated for the user.

        - **MaxExpirationTime** *(datetime) --*

          The time when the streaming session is set to expire. This time is based on the
          ``MaxUserDurationinSeconds`` value, which determines the maximum length of time that a
          streaming session can run. A streaming session might end earlier than the time specified
          in ``SessionMaxExpirationTime`` , when the ``DisconnectTimeOutInSeconds`` elapses or the
          user chooses to end his or her session. If the ``DisconnectTimeOutInSeconds`` elapses, or
          the user chooses to end his or her session, the streaming instance is terminated and the
          streaming session ends.

        - **AuthenticationType** *(string) --*

          The authentication method. The user is authenticated using a streaming URL (``API`` ) or
          SAML 2.0 federation (``SAML`` ).

        - **NetworkAccessConfiguration** *(dict) --*

          The network details for the streaming session.

          - **EniPrivateIpAddress** *(string) --*

            The private IP address of the elastic network interface that is attached to instances
            in your VPC.

          - **EniId** *(string) --*

            The resource identifier of the elastic network interface that is attached to instances
            in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientDescribeStacksResponseStacksAccessEndpointsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientDescribeStacksResponseStacksAccessEndpointsTypeDef(
    _ClientDescribeStacksResponseStacksAccessEndpointsTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
    When you specify an interface endpoint for a stack, users of the stack can connect to
    AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
    image builder, administrators can connect to the image builder only through that
    endpoint.

    - **EndpointType** *(string) --*

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientDescribeStacksResponseStacksApplicationSettingsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)


class ClientDescribeStacksResponseStacksApplicationSettingsTypeDef(
    _ClientDescribeStacksResponseStacksApplicationSettingsTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `ApplicationSettings`

    The persistent application settings for users of the stack.

    - **Enabled** *(boolean) --*

      Specifies whether persistent application settings are enabled for users during their
      streaming sessions.

    - **SettingsGroup** *(string) --*

      The path prefix for the S3 bucket where users’ persistent application settings are
      stored.

    - **S3BucketName** *(string) --*

      The S3 bucket where users’ persistent application settings are stored. When persistent
      application settings are enabled for the first time for an account in an AWS Region, an
      S3 bucket is created. The bucket is unique to the AWS account and the Region.
    """


_ClientDescribeStacksResponseStacksStackErrorsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksStackErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientDescribeStacksResponseStacksStackErrorsTypeDef(
    _ClientDescribeStacksResponseStacksStackErrorsTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `StackErrors`

    Describes a stack error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientDescribeStacksResponseStacksStorageConnectorsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksStorageConnectorsTypeDef",
    {"ConnectorType": str, "ResourceIdentifier": str, "Domains": List[str]},
    total=False,
)


class ClientDescribeStacksResponseStacksStorageConnectorsTypeDef(
    _ClientDescribeStacksResponseStacksStorageConnectorsTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `StorageConnectors`

    Describes a connector that enables persistent storage for users.

    - **ConnectorType** *(string) --*

      The type of storage connector.

    - **ResourceIdentifier** *(string) --*

      The ARN of the storage connector.

    - **Domains** *(list) --*

      The names of the domains for the account.

      - *(string) --* GSuite domain for GDrive integration.
    """


_ClientDescribeStacksResponseStacksUserSettingsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksUserSettingsTypeDef",
    {"Action": str, "Permission": str},
    total=False,
)


class ClientDescribeStacksResponseStacksUserSettingsTypeDef(
    _ClientDescribeStacksResponseStacksUserSettingsTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `UserSettings`

    Describes an action and whether the action is enabled or disabled for users during
    their streaming sessions.

    - **Action** *(string) --*

      The action that is enabled or disabled.

    - **Permission** *(string) --*

      Indicates whether the action is enabled or disabled.
    """


_ClientDescribeStacksResponseStacksTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "StorageConnectors": List[
            ClientDescribeStacksResponseStacksStorageConnectorsTypeDef
        ],
        "RedirectURL": str,
        "FeedbackURL": str,
        "StackErrors": List[ClientDescribeStacksResponseStacksStackErrorsTypeDef],
        "UserSettings": List[ClientDescribeStacksResponseStacksUserSettingsTypeDef],
        "ApplicationSettings": ClientDescribeStacksResponseStacksApplicationSettingsTypeDef,
        "AccessEndpoints": List[
            ClientDescribeStacksResponseStacksAccessEndpointsTypeDef
        ],
        "EmbedHostDomains": List[str],
    },
    total=False,
)


class ClientDescribeStacksResponseStacksTypeDef(
    _ClientDescribeStacksResponseStacksTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponse` `Stacks`

    Describes a stack.

    - **Arn** *(string) --*

      The ARN of the stack.

    - **Name** *(string) --*

      The name of the stack.

    - **Description** *(string) --*

      The description to display.

    - **DisplayName** *(string) --*

      The stack name to display.

    - **CreatedTime** *(datetime) --*

      The time the stack was created.

    - **StorageConnectors** *(list) --*

      The storage connectors to enable.

      - *(dict) --*

        Describes a connector that enables persistent storage for users.

        - **ConnectorType** *(string) --*

          The type of storage connector.

        - **ResourceIdentifier** *(string) --*

          The ARN of the storage connector.

        - **Domains** *(list) --*

          The names of the domains for the account.

          - *(string) --* GSuite domain for GDrive integration.

    - **RedirectURL** *(string) --*

      The URL that users are redirected to after their streaming session ends.

    - **FeedbackURL** *(string) --*

      The URL that users are redirected to after they click the Send Feedback link. If no URL
      is specified, no Send Feedback link is displayed.

    - **StackErrors** *(list) --*

      The errors for the stack.

      - *(dict) --*

        Describes a stack error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

    - **UserSettings** *(list) --*

      The actions that are enabled or disabled for users during their streaming sessions. By
      default these actions are enabled.

      - *(dict) --*

        Describes an action and whether the action is enabled or disabled for users during
        their streaming sessions.

        - **Action** *(string) --*

          The action that is enabled or disabled.

        - **Permission** *(string) --*

          Indicates whether the action is enabled or disabled.

    - **ApplicationSettings** *(dict) --*

      The persistent application settings for users of the stack.

      - **Enabled** *(boolean) --*

        Specifies whether persistent application settings are enabled for users during their
        streaming sessions.

      - **SettingsGroup** *(string) --*

        The path prefix for the S3 bucket where users’ persistent application settings are
        stored.

      - **S3BucketName** *(string) --*

        The S3 bucket where users’ persistent application settings are stored. When persistent
        application settings are enabled for the first time for an account in an AWS Region, an
        S3 bucket is created. The bucket is unique to the AWS account and the Region.

    - **AccessEndpoints** *(list) --*

      The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack
      can connect to AppStream 2.0 only through the specified endpoints.

      - *(dict) --*

        Describes an interface VPC endpoint (interface endpoint) that lets you create a private
        connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
        When you specify an interface endpoint for a stack, users of the stack can connect to
        AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
        image builder, administrators can connect to the image builder only through that
        endpoint.

        - **EndpointType** *(string) --*

          The type of interface endpoint.

        - **VpceId** *(string) --*

          The identifier (ID) of the VPC in which the interface endpoint is used.

    - **EmbedHostDomains** *(list) --*

      The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must
      approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

      - *(string) --* Specifies a valid domain that can embed AppStream. Valid examples
      include: ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples
      include: ["test,com", ".com", "h*llo.com". ""]
    """


_ClientDescribeStacksResponseTypeDef = TypedDict(
    "_ClientDescribeStacksResponseTypeDef",
    {"Stacks": List[ClientDescribeStacksResponseStacksTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeStacksResponseTypeDef(_ClientDescribeStacksResponseTypeDef):
    """
    Type definition for `ClientDescribeStacks` `Response`

    - **Stacks** *(list) --*

      Information about the stacks.

      - *(dict) --*

        Describes a stack.

        - **Arn** *(string) --*

          The ARN of the stack.

        - **Name** *(string) --*

          The name of the stack.

        - **Description** *(string) --*

          The description to display.

        - **DisplayName** *(string) --*

          The stack name to display.

        - **CreatedTime** *(datetime) --*

          The time the stack was created.

        - **StorageConnectors** *(list) --*

          The storage connectors to enable.

          - *(dict) --*

            Describes a connector that enables persistent storage for users.

            - **ConnectorType** *(string) --*

              The type of storage connector.

            - **ResourceIdentifier** *(string) --*

              The ARN of the storage connector.

            - **Domains** *(list) --*

              The names of the domains for the account.

              - *(string) --* GSuite domain for GDrive integration.

        - **RedirectURL** *(string) --*

          The URL that users are redirected to after their streaming session ends.

        - **FeedbackURL** *(string) --*

          The URL that users are redirected to after they click the Send Feedback link. If no URL
          is specified, no Send Feedback link is displayed.

        - **StackErrors** *(list) --*

          The errors for the stack.

          - *(dict) --*

            Describes a stack error.

            - **ErrorCode** *(string) --*

              The error code.

            - **ErrorMessage** *(string) --*

              The error message.

        - **UserSettings** *(list) --*

          The actions that are enabled or disabled for users during their streaming sessions. By
          default these actions are enabled.

          - *(dict) --*

            Describes an action and whether the action is enabled or disabled for users during
            their streaming sessions.

            - **Action** *(string) --*

              The action that is enabled or disabled.

            - **Permission** *(string) --*

              Indicates whether the action is enabled or disabled.

        - **ApplicationSettings** *(dict) --*

          The persistent application settings for users of the stack.

          - **Enabled** *(boolean) --*

            Specifies whether persistent application settings are enabled for users during their
            streaming sessions.

          - **SettingsGroup** *(string) --*

            The path prefix for the S3 bucket where users’ persistent application settings are
            stored.

          - **S3BucketName** *(string) --*

            The S3 bucket where users’ persistent application settings are stored. When persistent
            application settings are enabled for the first time for an account in an AWS Region, an
            S3 bucket is created. The bucket is unique to the AWS account and the Region.

        - **AccessEndpoints** *(list) --*

          The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack
          can connect to AppStream 2.0 only through the specified endpoints.

          - *(dict) --*

            Describes an interface VPC endpoint (interface endpoint) that lets you create a private
            connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
            When you specify an interface endpoint for a stack, users of the stack can connect to
            AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
            image builder, administrators can connect to the image builder only through that
            endpoint.

            - **EndpointType** *(string) --*

              The type of interface endpoint.

            - **VpceId** *(string) --*

              The identifier (ID) of the VPC in which the interface endpoint is used.

        - **EmbedHostDomains** *(list) --*

          The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must
          approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

          - *(string) --* Specifies a valid domain that can embed AppStream. Valid examples
          include: ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples
          include: ["test,com", ".com", "h*llo.com". ""]

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef = TypedDict(
    "_ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef(
    _ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef
):
    """
    Type definition for `ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptions` `SubscriptionErrors`

    Describes the error that is returned when a usage report can't be generated.

    - **ErrorCode** *(string) --*

      The error code for the error that is returned when a usage report can't be generated.

    - **ErrorMessage** *(string) --*

      The error message for the error that is returned when a usage report can't be
      generated.
    """


_ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef = TypedDict(
    "_ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef",
    {
        "S3BucketName": str,
        "Schedule": str,
        "LastGeneratedReportDate": datetime,
        "SubscriptionErrors": List[
            ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef(
    _ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef
):
    """
    Type definition for `ClientDescribeUsageReportSubscriptionsResponse` `UsageReportSubscriptions`

    Describes information about the usage report subscription.

    - **S3BucketName** *(string) --*

      The Amazon S3 bucket where generated reports are stored.

      If you enabled on-instance session scripts and Amazon S3 logging for your session script
      configuration, AppStream 2.0 created an S3 bucket to store the script output. The bucket
      is unique to your account and Region. When you enable usage reporting in this case,
      AppStream 2.0 uses the same bucket to store your usage reports. If you haven't already
      enabled on-instance session scripts, when you enable usage reports, AppStream 2.0 creates
      a new S3 bucket.

    - **Schedule** *(string) --*

      The schedule for generating usage reports.

    - **LastGeneratedReportDate** *(datetime) --*

      The time when the last usage report was generated.

    - **SubscriptionErrors** *(list) --*

      The errors that were returned if usage reports couldn't be generated.

      - *(dict) --*

        Describes the error that is returned when a usage report can't be generated.

        - **ErrorCode** *(string) --*

          The error code for the error that is returned when a usage report can't be generated.

        - **ErrorMessage** *(string) --*

          The error message for the error that is returned when a usage report can't be
          generated.
    """


_ClientDescribeUsageReportSubscriptionsResponseTypeDef = TypedDict(
    "_ClientDescribeUsageReportSubscriptionsResponseTypeDef",
    {
        "UsageReportSubscriptions": List[
            ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeUsageReportSubscriptionsResponseTypeDef(
    _ClientDescribeUsageReportSubscriptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeUsageReportSubscriptions` `Response`

    - **UsageReportSubscriptions** *(list) --*

      Information about the usage report subscription.

      - *(dict) --*

        Describes information about the usage report subscription.

        - **S3BucketName** *(string) --*

          The Amazon S3 bucket where generated reports are stored.

          If you enabled on-instance session scripts and Amazon S3 logging for your session script
          configuration, AppStream 2.0 created an S3 bucket to store the script output. The bucket
          is unique to your account and Region. When you enable usage reporting in this case,
          AppStream 2.0 uses the same bucket to store your usage reports. If you haven't already
          enabled on-instance session scripts, when you enable usage reports, AppStream 2.0 creates
          a new S3 bucket.

        - **Schedule** *(string) --*

          The schedule for generating usage reports.

        - **LastGeneratedReportDate** *(datetime) --*

          The time when the last usage report was generated.

        - **SubscriptionErrors** *(list) --*

          The errors that were returned if usage reports couldn't be generated.

          - *(dict) --*

            Describes the error that is returned when a usage report can't be generated.

            - **ErrorCode** *(string) --*

              The error code for the error that is returned when a usage report can't be generated.

            - **ErrorMessage** *(string) --*

              The error message for the error that is returned when a usage report can't be
              generated.

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef = TypedDict(
    "_ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": str,
        "SendEmailNotification": bool,
    },
    total=False,
)


class ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef(
    _ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef
):
    """
    Type definition for `ClientDescribeUserStackAssociationsResponse` `UserStackAssociations`

    Describes a user in the user pool and the associated stack.

    - **StackName** *(string) --*

      The name of the stack that is associated with the user.

    - **UserName** *(string) --*

      The email address of the user who is associated with the stack.

      .. note::

        Users' email addresses are case-sensitive.

    - **AuthenticationType** *(string) --*

      The authentication type for the user.

    - **SendEmailNotification** *(boolean) --*

      Specifies whether a welcome email is sent to a user after the user is created in the user
      pool.
    """


_ClientDescribeUserStackAssociationsResponseTypeDef = TypedDict(
    "_ClientDescribeUserStackAssociationsResponseTypeDef",
    {
        "UserStackAssociations": List[
            ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeUserStackAssociationsResponseTypeDef(
    _ClientDescribeUserStackAssociationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeUserStackAssociations` `Response`

    - **UserStackAssociations** *(list) --*

      The UserStackAssociation objects.

      - *(dict) --*

        Describes a user in the user pool and the associated stack.

        - **StackName** *(string) --*

          The name of the stack that is associated with the user.

        - **UserName** *(string) --*

          The email address of the user who is associated with the stack.

          .. note::

            Users' email addresses are case-sensitive.

        - **AuthenticationType** *(string) --*

          The authentication type for the user.

        - **SendEmailNotification** *(boolean) --*

          Specifies whether a welcome email is sent to a user after the user is created in the user
          pool.

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientDescribeUsersResponseUsersTypeDef = TypedDict(
    "_ClientDescribeUsersResponseUsersTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Enabled": bool,
        "Status": str,
        "FirstName": str,
        "LastName": str,
        "CreatedTime": datetime,
        "AuthenticationType": str,
    },
    total=False,
)


class ClientDescribeUsersResponseUsersTypeDef(_ClientDescribeUsersResponseUsersTypeDef):
    """
    Type definition for `ClientDescribeUsersResponse` `Users`

    Describes a user in the user pool.

    - **Arn** *(string) --*

      The ARN of the user.

    - **UserName** *(string) --*

      The email address of the user.

      .. note::

        Users' email addresses are case-sensitive.

    - **Enabled** *(boolean) --*

      Specifies whether the user in the user pool is enabled.

    - **Status** *(string) --*

      The status of the user in the user pool. The status can be one of the following:

      * UNCONFIRMED – The user is created but not confirmed.

      * CONFIRMED – The user is confirmed.

      * ARCHIVED – The user is no longer active.

      * COMPROMISED – The user is disabled because of a potential security threat.

      * UNKNOWN – The user status is not known.

    - **FirstName** *(string) --*

      The first name, or given name, of the user.

    - **LastName** *(string) --*

      The last name, or surname, of the user.

    - **CreatedTime** *(datetime) --*

      The date and time the user was created in the user pool.

    - **AuthenticationType** *(string) --*

      The authentication type for the user.
    """


_ClientDescribeUsersResponseTypeDef = TypedDict(
    "_ClientDescribeUsersResponseTypeDef",
    {"Users": List[ClientDescribeUsersResponseUsersTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeUsersResponseTypeDef(_ClientDescribeUsersResponseTypeDef):
    """
    Type definition for `ClientDescribeUsers` `Response`

    - **Users** *(list) --*

      Information about users in the user pool.

      - *(dict) --*

        Describes a user in the user pool.

        - **Arn** *(string) --*

          The ARN of the user.

        - **UserName** *(string) --*

          The email address of the user.

          .. note::

            Users' email addresses are case-sensitive.

        - **Enabled** *(boolean) --*

          Specifies whether the user in the user pool is enabled.

        - **Status** *(string) --*

          The status of the user in the user pool. The status can be one of the following:

          * UNCONFIRMED – The user is created but not confirmed.

          * CONFIRMED – The user is confirmed.

          * ARCHIVED – The user is no longer active.

          * COMPROMISED – The user is disabled because of a potential security threat.

          * UNKNOWN – The user status is not known.

        - **FirstName** *(string) --*

          The first name, or given name, of the user.

        - **LastName** *(string) --*

          The last name, or surname, of the user.

        - **CreatedTime** *(datetime) --*

          The date and time the user was created in the user pool.

        - **AuthenticationType** *(string) --*

          The authentication type for the user.

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientListAssociatedFleetsResponseTypeDef = TypedDict(
    "_ClientListAssociatedFleetsResponseTypeDef",
    {"Names": List[str], "NextToken": str},
    total=False,
)


class ClientListAssociatedFleetsResponseTypeDef(
    _ClientListAssociatedFleetsResponseTypeDef
):
    """
    Type definition for `ClientListAssociatedFleets` `Response`

    - **Names** *(list) --*

      The name of the fleet.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientListAssociatedStacksResponseTypeDef = TypedDict(
    "_ClientListAssociatedStacksResponseTypeDef",
    {"Names": List[str], "NextToken": str},
    total=False,
)


class ClientListAssociatedStacksResponseTypeDef(
    _ClientListAssociatedStacksResponseTypeDef
):
    """
    Type definition for `ClientListAssociatedStacks` `Response`

    - **Names** *(list) --*

      The name of the stack.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(dict) --*

      The information about the tags.

      - *(string) --*

        - *(string) --*
    """


_ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef(
    _ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef
):
    """
    Type definition for `ClientStartImageBuilderResponseImageBuilder` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
    When you specify an interface endpoint for a stack, users of the stack can connect to
    AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
    image builder, administrators can connect to the image builder only through that endpoint.

    - **EndpointType** *(string) --*

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef(
    _ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef
):
    """
    Type definition for `ClientStartImageBuilderResponseImageBuilder` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the image builder to
    a Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "ErrorTimestamp": datetime},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef(
    _ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
):
    """
    Type definition for `ClientStartImageBuilderResponseImageBuilder` `ImageBuilderErrors`

    Describes a resource error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.

    - **ErrorTimestamp** *(datetime) --*

      The time the error occurred.
    """


_ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef(
    _ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef
):
    """
    Type definition for `ClientStartImageBuilderResponseImageBuilder` `NetworkAccessConfiguration`

    Describes the network details of the fleet or image builder instance.

    - **EniPrivateIpAddress** *(string) --*

      The private IP address of the elastic network interface that is attached to instances in
      your VPC.

    - **EniId** *(string) --*

      The resource identifier of the elastic network interface that is attached to instances in
      your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef(
    _ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef
):
    """
    Type definition for `ClientStartImageBuilderResponseImageBuilder` `StateChangeReason`

    The reason why the last state change occurred.

    - **Code** *(string) --*

      The state change reason code.

    - **Message** *(string) --*

      The state change reason message.
    """


_ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef(
    _ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef
):
    """
    Type definition for `ClientStartImageBuilderResponseImageBuilder` `VpcConfig`

    The VPC configuration of the image builder.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image
      builder instances use one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_ClientStartImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": str,
        "IamRoleArn": str,
        "State": str,
        "StateChangeReason": ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[
            ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef
        ],
    },
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderTypeDef(
    _ClientStartImageBuilderResponseImageBuilderTypeDef
):
    """
    Type definition for `ClientStartImageBuilderResponse` `ImageBuilder`

    Information about the image builder.

    - **Name** *(string) --*

      The name of the image builder.

    - **Arn** *(string) --*

      The ARN for the image builder.

    - **ImageArn** *(string) --*

      The ARN of the image from which this builder was created.

    - **Description** *(string) --*

      The description to display.

    - **DisplayName** *(string) --*

      The image builder name to display.

    - **VpcConfig** *(dict) --*

      The VPC configuration of the image builder.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets to which a network interface is attached from the fleet
        instance or image builder instance. Fleet instances use one or more subnets. Image
        builder instances use one subnet.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        The identifiers of the security groups for the fleet or image builder.

        - *(string) --*

    - **InstanceType** *(string) --*

      The instance type for the image builder. The following instance types are available:

      * stream.standard.medium

      * stream.standard.large

      * stream.compute.large

      * stream.compute.xlarge

      * stream.compute.2xlarge

      * stream.compute.4xlarge

      * stream.compute.8xlarge

      * stream.memory.large

      * stream.memory.xlarge

      * stream.memory.2xlarge

      * stream.memory.4xlarge

      * stream.memory.8xlarge

      * stream.graphics-design.large

      * stream.graphics-design.xlarge

      * stream.graphics-design.2xlarge

      * stream.graphics-design.4xlarge

      * stream.graphics-desktop.2xlarge

      * stream.graphics-pro.4xlarge

      * stream.graphics-pro.8xlarge

      * stream.graphics-pro.16xlarge

    - **Platform** *(string) --*

      The operating system platform of the image builder.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that is applied to the image builder. To assume a role, the image
      builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes
      the ARN of the role to use. The operation creates a new session with temporary credentials.
      AppStream 2.0 retrieves the temporary credentials and creates the
      **AppStream_Machine_Role** credential profile on the instance.

      For more information, see `Using an IAM Role to Grant Permissions to Applications and
      Scripts Running on AppStream 2.0 Streaming Instances
      <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
      in the *Amazon AppStream 2.0 Administration Guide* .

    - **State** *(string) --*

      The state of the image builder.

    - **StateChangeReason** *(dict) --*

      The reason why the last state change occurred.

      - **Code** *(string) --*

        The state change reason code.

      - **Message** *(string) --*

        The state change reason message.

    - **CreatedTime** *(datetime) --*

      The time stamp when the image builder was created.

    - **EnableDefaultInternetAccess** *(boolean) --*

      Enables or disables default internet access for the image builder.

    - **DomainJoinInfo** *(dict) --*

      The name of the directory and organizational unit (OU) to use to join the image builder to
      a Microsoft Active Directory domain.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedName** *(string) --*

        The distinguished name of the organizational unit for computer accounts.

    - **NetworkAccessConfiguration** *(dict) --*

      Describes the network details of the fleet or image builder instance.

      - **EniPrivateIpAddress** *(string) --*

        The private IP address of the elastic network interface that is attached to instances in
        your VPC.

      - **EniId** *(string) --*

        The resource identifier of the elastic network interface that is attached to instances in
        your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

    - **ImageBuilderErrors** *(list) --*

      The image builder errors.

      - *(dict) --*

        Describes a resource error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

        - **ErrorTimestamp** *(datetime) --*

          The time the error occurred.

    - **AppstreamAgentVersion** *(string) --*

      The version of the AppStream 2.0 agent that is currently being used by the image builder.

    - **AccessEndpoints** *(list) --*

      The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
      connect to the image builder only through the specified endpoints.

      - *(dict) --*

        Describes an interface VPC endpoint (interface endpoint) that lets you create a private
        connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
        When you specify an interface endpoint for a stack, users of the stack can connect to
        AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
        image builder, administrators can connect to the image builder only through that endpoint.

        - **EndpointType** *(string) --*

          The type of interface endpoint.

        - **VpceId** *(string) --*

          The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientStartImageBuilderResponseTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientStartImageBuilderResponseImageBuilderTypeDef},
    total=False,
)


class ClientStartImageBuilderResponseTypeDef(_ClientStartImageBuilderResponseTypeDef):
    """
    Type definition for `ClientStartImageBuilder` `Response`

    - **ImageBuilder** *(dict) --*

      Information about the image builder.

      - **Name** *(string) --*

        The name of the image builder.

      - **Arn** *(string) --*

        The ARN for the image builder.

      - **ImageArn** *(string) --*

        The ARN of the image from which this builder was created.

      - **Description** *(string) --*

        The description to display.

      - **DisplayName** *(string) --*

        The image builder name to display.

      - **VpcConfig** *(dict) --*

        The VPC configuration of the image builder.

        - **SubnetIds** *(list) --*

          The identifiers of the subnets to which a network interface is attached from the fleet
          instance or image builder instance. Fleet instances use one or more subnets. Image
          builder instances use one subnet.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          The identifiers of the security groups for the fleet or image builder.

          - *(string) --*

      - **InstanceType** *(string) --*

        The instance type for the image builder. The following instance types are available:

        * stream.standard.medium

        * stream.standard.large

        * stream.compute.large

        * stream.compute.xlarge

        * stream.compute.2xlarge

        * stream.compute.4xlarge

        * stream.compute.8xlarge

        * stream.memory.large

        * stream.memory.xlarge

        * stream.memory.2xlarge

        * stream.memory.4xlarge

        * stream.memory.8xlarge

        * stream.graphics-design.large

        * stream.graphics-design.xlarge

        * stream.graphics-design.2xlarge

        * stream.graphics-design.4xlarge

        * stream.graphics-desktop.2xlarge

        * stream.graphics-pro.4xlarge

        * stream.graphics-pro.8xlarge

        * stream.graphics-pro.16xlarge

      - **Platform** *(string) --*

        The operating system platform of the image builder.

      - **IamRoleArn** *(string) --*

        The ARN of the IAM role that is applied to the image builder. To assume a role, the image
        builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes
        the ARN of the role to use. The operation creates a new session with temporary credentials.
        AppStream 2.0 retrieves the temporary credentials and creates the
        **AppStream_Machine_Role** credential profile on the instance.

        For more information, see `Using an IAM Role to Grant Permissions to Applications and
        Scripts Running on AppStream 2.0 Streaming Instances
        <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
        in the *Amazon AppStream 2.0 Administration Guide* .

      - **State** *(string) --*

        The state of the image builder.

      - **StateChangeReason** *(dict) --*

        The reason why the last state change occurred.

        - **Code** *(string) --*

          The state change reason code.

        - **Message** *(string) --*

          The state change reason message.

      - **CreatedTime** *(datetime) --*

        The time stamp when the image builder was created.

      - **EnableDefaultInternetAccess** *(boolean) --*

        Enables or disables default internet access for the image builder.

      - **DomainJoinInfo** *(dict) --*

        The name of the directory and organizational unit (OU) to use to join the image builder to
        a Microsoft Active Directory domain.

        - **DirectoryName** *(string) --*

          The fully qualified name of the directory (for example, corp.example.com).

        - **OrganizationalUnitDistinguishedName** *(string) --*

          The distinguished name of the organizational unit for computer accounts.

      - **NetworkAccessConfiguration** *(dict) --*

        Describes the network details of the fleet or image builder instance.

        - **EniPrivateIpAddress** *(string) --*

          The private IP address of the elastic network interface that is attached to instances in
          your VPC.

        - **EniId** *(string) --*

          The resource identifier of the elastic network interface that is attached to instances in
          your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

      - **ImageBuilderErrors** *(list) --*

        The image builder errors.

        - *(dict) --*

          Describes a resource error.

          - **ErrorCode** *(string) --*

            The error code.

          - **ErrorMessage** *(string) --*

            The error message.

          - **ErrorTimestamp** *(datetime) --*

            The time the error occurred.

      - **AppstreamAgentVersion** *(string) --*

        The version of the AppStream 2.0 agent that is currently being used by the image builder.

      - **AccessEndpoints** *(list) --*

        The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
        connect to the image builder only through the specified endpoints.

        - *(dict) --*

          Describes an interface VPC endpoint (interface endpoint) that lets you create a private
          connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
          When you specify an interface endpoint for a stack, users of the stack can connect to
          AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
          image builder, administrators can connect to the image builder only through that endpoint.

          - **EndpointType** *(string) --*

            The type of interface endpoint.

          - **VpceId** *(string) --*

            The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef(
    _ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef
):
    """
    Type definition for `ClientStopImageBuilderResponseImageBuilder` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
    When you specify an interface endpoint for a stack, users of the stack can connect to
    AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
    image builder, administrators can connect to the image builder only through that endpoint.

    - **EndpointType** *(string) --*

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef(
    _ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef
):
    """
    Type definition for `ClientStopImageBuilderResponseImageBuilder` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the image builder to
    a Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "ErrorTimestamp": datetime},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef(
    _ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
):
    """
    Type definition for `ClientStopImageBuilderResponseImageBuilder` `ImageBuilderErrors`

    Describes a resource error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.

    - **ErrorTimestamp** *(datetime) --*

      The time the error occurred.
    """


_ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef(
    _ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef
):
    """
    Type definition for `ClientStopImageBuilderResponseImageBuilder` `NetworkAccessConfiguration`

    Describes the network details of the fleet or image builder instance.

    - **EniPrivateIpAddress** *(string) --*

      The private IP address of the elastic network interface that is attached to instances in
      your VPC.

    - **EniId** *(string) --*

      The resource identifier of the elastic network interface that is attached to instances in
      your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef(
    _ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef
):
    """
    Type definition for `ClientStopImageBuilderResponseImageBuilder` `StateChangeReason`

    The reason why the last state change occurred.

    - **Code** *(string) --*

      The state change reason code.

    - **Message** *(string) --*

      The state change reason message.
    """


_ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef(
    _ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef
):
    """
    Type definition for `ClientStopImageBuilderResponseImageBuilder` `VpcConfig`

    The VPC configuration of the image builder.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image
      builder instances use one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_ClientStopImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": str,
        "IamRoleArn": str,
        "State": str,
        "StateChangeReason": ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[
            ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef
        ],
    },
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderTypeDef(
    _ClientStopImageBuilderResponseImageBuilderTypeDef
):
    """
    Type definition for `ClientStopImageBuilderResponse` `ImageBuilder`

    Information about the image builder.

    - **Name** *(string) --*

      The name of the image builder.

    - **Arn** *(string) --*

      The ARN for the image builder.

    - **ImageArn** *(string) --*

      The ARN of the image from which this builder was created.

    - **Description** *(string) --*

      The description to display.

    - **DisplayName** *(string) --*

      The image builder name to display.

    - **VpcConfig** *(dict) --*

      The VPC configuration of the image builder.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets to which a network interface is attached from the fleet
        instance or image builder instance. Fleet instances use one or more subnets. Image
        builder instances use one subnet.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        The identifiers of the security groups for the fleet or image builder.

        - *(string) --*

    - **InstanceType** *(string) --*

      The instance type for the image builder. The following instance types are available:

      * stream.standard.medium

      * stream.standard.large

      * stream.compute.large

      * stream.compute.xlarge

      * stream.compute.2xlarge

      * stream.compute.4xlarge

      * stream.compute.8xlarge

      * stream.memory.large

      * stream.memory.xlarge

      * stream.memory.2xlarge

      * stream.memory.4xlarge

      * stream.memory.8xlarge

      * stream.graphics-design.large

      * stream.graphics-design.xlarge

      * stream.graphics-design.2xlarge

      * stream.graphics-design.4xlarge

      * stream.graphics-desktop.2xlarge

      * stream.graphics-pro.4xlarge

      * stream.graphics-pro.8xlarge

      * stream.graphics-pro.16xlarge

    - **Platform** *(string) --*

      The operating system platform of the image builder.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that is applied to the image builder. To assume a role, the image
      builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes
      the ARN of the role to use. The operation creates a new session with temporary credentials.
      AppStream 2.0 retrieves the temporary credentials and creates the
      **AppStream_Machine_Role** credential profile on the instance.

      For more information, see `Using an IAM Role to Grant Permissions to Applications and
      Scripts Running on AppStream 2.0 Streaming Instances
      <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
      in the *Amazon AppStream 2.0 Administration Guide* .

    - **State** *(string) --*

      The state of the image builder.

    - **StateChangeReason** *(dict) --*

      The reason why the last state change occurred.

      - **Code** *(string) --*

        The state change reason code.

      - **Message** *(string) --*

        The state change reason message.

    - **CreatedTime** *(datetime) --*

      The time stamp when the image builder was created.

    - **EnableDefaultInternetAccess** *(boolean) --*

      Enables or disables default internet access for the image builder.

    - **DomainJoinInfo** *(dict) --*

      The name of the directory and organizational unit (OU) to use to join the image builder to
      a Microsoft Active Directory domain.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedName** *(string) --*

        The distinguished name of the organizational unit for computer accounts.

    - **NetworkAccessConfiguration** *(dict) --*

      Describes the network details of the fleet or image builder instance.

      - **EniPrivateIpAddress** *(string) --*

        The private IP address of the elastic network interface that is attached to instances in
        your VPC.

      - **EniId** *(string) --*

        The resource identifier of the elastic network interface that is attached to instances in
        your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

    - **ImageBuilderErrors** *(list) --*

      The image builder errors.

      - *(dict) --*

        Describes a resource error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

        - **ErrorTimestamp** *(datetime) --*

          The time the error occurred.

    - **AppstreamAgentVersion** *(string) --*

      The version of the AppStream 2.0 agent that is currently being used by the image builder.

    - **AccessEndpoints** *(list) --*

      The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
      connect to the image builder only through the specified endpoints.

      - *(dict) --*

        Describes an interface VPC endpoint (interface endpoint) that lets you create a private
        connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
        When you specify an interface endpoint for a stack, users of the stack can connect to
        AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
        image builder, administrators can connect to the image builder only through that endpoint.

        - **EndpointType** *(string) --*

          The type of interface endpoint.

        - **VpceId** *(string) --*

          The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientStopImageBuilderResponseTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientStopImageBuilderResponseImageBuilderTypeDef},
    total=False,
)


class ClientStopImageBuilderResponseTypeDef(_ClientStopImageBuilderResponseTypeDef):
    """
    Type definition for `ClientStopImageBuilder` `Response`

    - **ImageBuilder** *(dict) --*

      Information about the image builder.

      - **Name** *(string) --*

        The name of the image builder.

      - **Arn** *(string) --*

        The ARN for the image builder.

      - **ImageArn** *(string) --*

        The ARN of the image from which this builder was created.

      - **Description** *(string) --*

        The description to display.

      - **DisplayName** *(string) --*

        The image builder name to display.

      - **VpcConfig** *(dict) --*

        The VPC configuration of the image builder.

        - **SubnetIds** *(list) --*

          The identifiers of the subnets to which a network interface is attached from the fleet
          instance or image builder instance. Fleet instances use one or more subnets. Image
          builder instances use one subnet.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          The identifiers of the security groups for the fleet or image builder.

          - *(string) --*

      - **InstanceType** *(string) --*

        The instance type for the image builder. The following instance types are available:

        * stream.standard.medium

        * stream.standard.large

        * stream.compute.large

        * stream.compute.xlarge

        * stream.compute.2xlarge

        * stream.compute.4xlarge

        * stream.compute.8xlarge

        * stream.memory.large

        * stream.memory.xlarge

        * stream.memory.2xlarge

        * stream.memory.4xlarge

        * stream.memory.8xlarge

        * stream.graphics-design.large

        * stream.graphics-design.xlarge

        * stream.graphics-design.2xlarge

        * stream.graphics-design.4xlarge

        * stream.graphics-desktop.2xlarge

        * stream.graphics-pro.4xlarge

        * stream.graphics-pro.8xlarge

        * stream.graphics-pro.16xlarge

      - **Platform** *(string) --*

        The operating system platform of the image builder.

      - **IamRoleArn** *(string) --*

        The ARN of the IAM role that is applied to the image builder. To assume a role, the image
        builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes
        the ARN of the role to use. The operation creates a new session with temporary credentials.
        AppStream 2.0 retrieves the temporary credentials and creates the
        **AppStream_Machine_Role** credential profile on the instance.

        For more information, see `Using an IAM Role to Grant Permissions to Applications and
        Scripts Running on AppStream 2.0 Streaming Instances
        <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
        in the *Amazon AppStream 2.0 Administration Guide* .

      - **State** *(string) --*

        The state of the image builder.

      - **StateChangeReason** *(dict) --*

        The reason why the last state change occurred.

        - **Code** *(string) --*

          The state change reason code.

        - **Message** *(string) --*

          The state change reason message.

      - **CreatedTime** *(datetime) --*

        The time stamp when the image builder was created.

      - **EnableDefaultInternetAccess** *(boolean) --*

        Enables or disables default internet access for the image builder.

      - **DomainJoinInfo** *(dict) --*

        The name of the directory and organizational unit (OU) to use to join the image builder to
        a Microsoft Active Directory domain.

        - **DirectoryName** *(string) --*

          The fully qualified name of the directory (for example, corp.example.com).

        - **OrganizationalUnitDistinguishedName** *(string) --*

          The distinguished name of the organizational unit for computer accounts.

      - **NetworkAccessConfiguration** *(dict) --*

        Describes the network details of the fleet or image builder instance.

        - **EniPrivateIpAddress** *(string) --*

          The private IP address of the elastic network interface that is attached to instances in
          your VPC.

        - **EniId** *(string) --*

          The resource identifier of the elastic network interface that is attached to instances in
          your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

      - **ImageBuilderErrors** *(list) --*

        The image builder errors.

        - *(dict) --*

          Describes a resource error.

          - **ErrorCode** *(string) --*

            The error code.

          - **ErrorMessage** *(string) --*

            The error message.

          - **ErrorTimestamp** *(datetime) --*

            The time the error occurred.

      - **AppstreamAgentVersion** *(string) --*

        The version of the AppStream 2.0 agent that is currently being used by the image builder.

      - **AccessEndpoints** *(list) --*

        The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
        connect to the image builder only through the specified endpoints.

        - *(dict) --*

          Describes an interface VPC endpoint (interface endpoint) that lets you create a private
          connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
          When you specify an interface endpoint for a stack, users of the stack can connect to
          AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
          image builder, administrators can connect to the image builder only through that endpoint.

          - **EndpointType** *(string) --*

            The type of interface endpoint.

          - **VpceId** *(string) --*

            The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "_ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)


class ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef(
    _ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef
):
    """
    Type definition for `ClientUpdateDirectoryConfigResponseDirectoryConfig` `ServiceAccountCredentials`

    The credentials for the service account used by the fleet or image builder to connect to
    the directory.

    - **AccountName** *(string) --*

      The user name of the account. This account must have the following privileges: create
      computer objects, join computers to the domain, and change/reset the password on
      descendant computer objects for the organizational units specified.

    - **AccountPassword** *(string) --*

      The password for the account.
    """


_ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef = TypedDict(
    "_ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef(
    _ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef
):
    """
    Type definition for `ClientUpdateDirectoryConfigResponse` `DirectoryConfig`

    Information about the Directory Config object.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedNames** *(list) --*

      The distinguished names of the organizational units for computer accounts.

      - *(string) --*

    - **ServiceAccountCredentials** *(dict) --*

      The credentials for the service account used by the fleet or image builder to connect to
      the directory.

      - **AccountName** *(string) --*

        The user name of the account. This account must have the following privileges: create
        computer objects, join computers to the domain, and change/reset the password on
        descendant computer objects for the organizational units specified.

      - **AccountPassword** *(string) --*

        The password for the account.

    - **CreatedTime** *(datetime) --*

      The time the directory configuration was created.
    """


_ClientUpdateDirectoryConfigResponseTypeDef = TypedDict(
    "_ClientUpdateDirectoryConfigResponseTypeDef",
    {"DirectoryConfig": ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef},
    total=False,
)


class ClientUpdateDirectoryConfigResponseTypeDef(
    _ClientUpdateDirectoryConfigResponseTypeDef
):
    """
    Type definition for `ClientUpdateDirectoryConfig` `Response`

    - **DirectoryConfig** *(dict) --*

      Information about the Directory Config object.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedNames** *(list) --*

        The distinguished names of the organizational units for computer accounts.

        - *(string) --*

      - **ServiceAccountCredentials** *(dict) --*

        The credentials for the service account used by the fleet or image builder to connect to
        the directory.

        - **AccountName** *(string) --*

          The user name of the account. This account must have the following privileges: create
          computer objects, join computers to the domain, and change/reset the password on
          descendant computer objects for the organizational units specified.

        - **AccountPassword** *(string) --*

          The password for the account.

      - **CreatedTime** *(datetime) --*

        The time the directory configuration was created.
    """


_ClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "_ClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
)


class ClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef(
    _ClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef
):
    """
    Type definition for `ClientUpdateDirectoryConfig` `ServiceAccountCredentials`

    The credentials for the service account used by the fleet or image builder to connect to the
    directory.

    - **AccountName** *(string) --* **[REQUIRED]**

      The user name of the account. This account must have the following privileges: create computer
      objects, join computers to the domain, and change/reset the password on descendant computer
      objects for the organizational units specified.

    - **AccountPassword** *(string) --* **[REQUIRED]**

      The password for the account.
    """


_ClientUpdateFleetComputeCapacityTypeDef = TypedDict(
    "_ClientUpdateFleetComputeCapacityTypeDef", {"DesiredInstances": int}
)


class ClientUpdateFleetComputeCapacityTypeDef(_ClientUpdateFleetComputeCapacityTypeDef):
    """
    Type definition for `ClientUpdateFleet` `ComputeCapacity`

    The desired capacity for the fleet.

    - **DesiredInstances** *(integer) --* **[REQUIRED]**

      The desired number of streaming instances.
    """


_ClientUpdateFleetDomainJoinInfoTypeDef = TypedDict(
    "_ClientUpdateFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientUpdateFleetDomainJoinInfoTypeDef(_ClientUpdateFleetDomainJoinInfoTypeDef):
    """
    Type definition for `ClientUpdateFleet` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft
    Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef = TypedDict(
    "_ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)


class ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef(
    _ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef
):
    """
    Type definition for `ClientUpdateFleetResponseFleet` `ComputeCapacityStatus`

    The capacity status for the fleet.

    - **Desired** *(integer) --*

      The desired number of streaming instances.

    - **Running** *(integer) --*

      The total number of simultaneous streaming instances that are running.

    - **InUse** *(integer) --*

      The number of instances in use for streaming.

    - **Available** *(integer) --*

      The number of currently available instances that can be used to stream sessions.
    """


_ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef = TypedDict(
    "_ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef(
    _ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef
):
    """
    Type definition for `ClientUpdateFleetResponseFleet` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the fleet to a
    Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_ClientUpdateFleetResponseFleetFleetErrorsTypeDef = TypedDict(
    "_ClientUpdateFleetResponseFleetFleetErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientUpdateFleetResponseFleetFleetErrorsTypeDef(
    _ClientUpdateFleetResponseFleetFleetErrorsTypeDef
):
    """
    Type definition for `ClientUpdateFleetResponseFleet` `FleetErrors`

    Describes a fleet error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientUpdateFleetResponseFleetVpcConfigTypeDef = TypedDict(
    "_ClientUpdateFleetResponseFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientUpdateFleetResponseFleetVpcConfigTypeDef(
    _ClientUpdateFleetResponseFleetVpcConfigTypeDef
):
    """
    Type definition for `ClientUpdateFleetResponseFleet` `VpcConfig`

    The VPC configuration for the fleet.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image
      builder instances use one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_ClientUpdateFleetResponseFleetTypeDef = TypedDict(
    "_ClientUpdateFleetResponseFleetTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "InstanceType": str,
        "FleetType": str,
        "ComputeCapacityStatus": ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef,
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "State": str,
        "VpcConfig": ClientUpdateFleetResponseFleetVpcConfigTypeDef,
        "CreatedTime": datetime,
        "FleetErrors": List[ClientUpdateFleetResponseFleetFleetErrorsTypeDef],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef,
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
    },
    total=False,
)


class ClientUpdateFleetResponseFleetTypeDef(_ClientUpdateFleetResponseFleetTypeDef):
    """
    Type definition for `ClientUpdateFleetResponse` `Fleet`

    Information about the fleet.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the fleet.

    - **Name** *(string) --*

      The name of the fleet.

    - **DisplayName** *(string) --*

      The fleet name to display.

    - **Description** *(string) --*

      The description to display.

    - **ImageName** *(string) --*

      The name of the image used to create the fleet.

    - **ImageArn** *(string) --*

      The ARN for the public, private, or shared image.

    - **InstanceType** *(string) --*

      The instance type to use when launching fleet instances. The following instance types are
      available:

      * stream.standard.medium

      * stream.standard.large

      * stream.compute.large

      * stream.compute.xlarge

      * stream.compute.2xlarge

      * stream.compute.4xlarge

      * stream.compute.8xlarge

      * stream.memory.large

      * stream.memory.xlarge

      * stream.memory.2xlarge

      * stream.memory.4xlarge

      * stream.memory.8xlarge

      * stream.graphics-design.large

      * stream.graphics-design.xlarge

      * stream.graphics-design.2xlarge

      * stream.graphics-design.4xlarge

      * stream.graphics-desktop.2xlarge

      * stream.graphics-pro.4xlarge

      * stream.graphics-pro.8xlarge

      * stream.graphics-pro.16xlarge

    - **FleetType** *(string) --*

      The fleet type.

        ALWAYS_ON

      Provides users with instant-on access to their apps. You are charged for all running
      instances in your fleet, even if no users are streaming apps.

        ON_DEMAND

      Provide users with access to applications after they connect, which takes one to two
      minutes. You are charged for instance streaming when users are connected and a small hourly
      fee for instances that are not streaming apps.

    - **ComputeCapacityStatus** *(dict) --*

      The capacity status for the fleet.

      - **Desired** *(integer) --*

        The desired number of streaming instances.

      - **Running** *(integer) --*

        The total number of simultaneous streaming instances that are running.

      - **InUse** *(integer) --*

        The number of instances in use for streaming.

      - **Available** *(integer) --*

        The number of currently available instances that can be used to stream sessions.

    - **MaxUserDurationInSeconds** *(integer) --*

      The maximum amount of time that a streaming session can remain active, in seconds. If users
      are still connected to a streaming instance five minutes before this limit is reached, they
      are prompted to save any open documents before being disconnected. After this time elapses,
      the instance is terminated and replaced by a new instance.

      Specify a value between 600 and 360000.

    - **DisconnectTimeoutInSeconds** *(integer) --*

      The amount of time that a streaming session remains active after users disconnect. If they
      try to reconnect to the streaming session after a disconnection or network interruption
      within this time interval, they are connected to their previous session. Otherwise, they
      are connected to a new session with a new streaming instance.

      Specify a value between 60 and 360000.

    - **State** *(string) --*

      The current state for the fleet.

    - **VpcConfig** *(dict) --*

      The VPC configuration for the fleet.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets to which a network interface is attached from the fleet
        instance or image builder instance. Fleet instances use one or more subnets. Image
        builder instances use one subnet.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        The identifiers of the security groups for the fleet or image builder.

        - *(string) --*

    - **CreatedTime** *(datetime) --*

      The time the fleet was created.

    - **FleetErrors** *(list) --*

      The fleet errors.

      - *(dict) --*

        Describes a fleet error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

    - **EnableDefaultInternetAccess** *(boolean) --*

      Indicates whether default internet access is enabled for the fleet.

    - **DomainJoinInfo** *(dict) --*

      The name of the directory and organizational unit (OU) to use to join the fleet to a
      Microsoft Active Directory domain.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedName** *(string) --*

        The distinguished name of the organizational unit for computer accounts.

    - **IdleDisconnectTimeoutInSeconds** *(integer) --*

      The amount of time that users can be idle (inactive) before they are disconnected from
      their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins. Users
      are notified before they are disconnected due to inactivity. If users try to reconnect to
      the streaming session before the time interval specified in ``DisconnectTimeoutInSeconds``
      elapses, they are connected to their previous session. Users are considered idle when they
      stop providing keyboard or mouse input during their streaming session. File uploads and
      downloads, audio in, audio out, and pixels changing do not qualify as user activity. If
      users continue to be idle after the time interval in ``IdleDisconnectTimeoutInSeconds``
      elapses, they are disconnected.

      To prevent users from being disconnected due to inactivity, specify a value of 0.
      Otherwise, specify a value between 60 and 3600. The default value is 0.

      .. note::

        If you enable this feature, we recommend that you specify a value that corresponds
        exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do
        this, the value is rounded to the nearest minute. For example, if you specify a value of
        70, users are disconnected after 1 minute of inactivity. If you specify a value that is
        at the midpoint between two different minutes, the value is rounded up. For example, if
        you specify a value of 90, users are disconnected after 2 minutes of inactivity.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance
      calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes the ARN
      of the role to use. The operation creates a new session with temporary credentials.
      AppStream 2.0 retrieves the temporary credentials and creates the
      **AppStream_Machine_Role** credential profile on the instance.

      For more information, see `Using an IAM Role to Grant Permissions to Applications and
      Scripts Running on AppStream 2.0 Streaming Instances
      <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
      in the *Amazon AppStream 2.0 Administration Guide* .
    """


_ClientUpdateFleetResponseTypeDef = TypedDict(
    "_ClientUpdateFleetResponseTypeDef",
    {"Fleet": ClientUpdateFleetResponseFleetTypeDef},
    total=False,
)


class ClientUpdateFleetResponseTypeDef(_ClientUpdateFleetResponseTypeDef):
    """
    Type definition for `ClientUpdateFleet` `Response`

    - **Fleet** *(dict) --*

      Information about the fleet.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the fleet.

      - **Name** *(string) --*

        The name of the fleet.

      - **DisplayName** *(string) --*

        The fleet name to display.

      - **Description** *(string) --*

        The description to display.

      - **ImageName** *(string) --*

        The name of the image used to create the fleet.

      - **ImageArn** *(string) --*

        The ARN for the public, private, or shared image.

      - **InstanceType** *(string) --*

        The instance type to use when launching fleet instances. The following instance types are
        available:

        * stream.standard.medium

        * stream.standard.large

        * stream.compute.large

        * stream.compute.xlarge

        * stream.compute.2xlarge

        * stream.compute.4xlarge

        * stream.compute.8xlarge

        * stream.memory.large

        * stream.memory.xlarge

        * stream.memory.2xlarge

        * stream.memory.4xlarge

        * stream.memory.8xlarge

        * stream.graphics-design.large

        * stream.graphics-design.xlarge

        * stream.graphics-design.2xlarge

        * stream.graphics-design.4xlarge

        * stream.graphics-desktop.2xlarge

        * stream.graphics-pro.4xlarge

        * stream.graphics-pro.8xlarge

        * stream.graphics-pro.16xlarge

      - **FleetType** *(string) --*

        The fleet type.

          ALWAYS_ON

        Provides users with instant-on access to their apps. You are charged for all running
        instances in your fleet, even if no users are streaming apps.

          ON_DEMAND

        Provide users with access to applications after they connect, which takes one to two
        minutes. You are charged for instance streaming when users are connected and a small hourly
        fee for instances that are not streaming apps.

      - **ComputeCapacityStatus** *(dict) --*

        The capacity status for the fleet.

        - **Desired** *(integer) --*

          The desired number of streaming instances.

        - **Running** *(integer) --*

          The total number of simultaneous streaming instances that are running.

        - **InUse** *(integer) --*

          The number of instances in use for streaming.

        - **Available** *(integer) --*

          The number of currently available instances that can be used to stream sessions.

      - **MaxUserDurationInSeconds** *(integer) --*

        The maximum amount of time that a streaming session can remain active, in seconds. If users
        are still connected to a streaming instance five minutes before this limit is reached, they
        are prompted to save any open documents before being disconnected. After this time elapses,
        the instance is terminated and replaced by a new instance.

        Specify a value between 600 and 360000.

      - **DisconnectTimeoutInSeconds** *(integer) --*

        The amount of time that a streaming session remains active after users disconnect. If they
        try to reconnect to the streaming session after a disconnection or network interruption
        within this time interval, they are connected to their previous session. Otherwise, they
        are connected to a new session with a new streaming instance.

        Specify a value between 60 and 360000.

      - **State** *(string) --*

        The current state for the fleet.

      - **VpcConfig** *(dict) --*

        The VPC configuration for the fleet.

        - **SubnetIds** *(list) --*

          The identifiers of the subnets to which a network interface is attached from the fleet
          instance or image builder instance. Fleet instances use one or more subnets. Image
          builder instances use one subnet.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          The identifiers of the security groups for the fleet or image builder.

          - *(string) --*

      - **CreatedTime** *(datetime) --*

        The time the fleet was created.

      - **FleetErrors** *(list) --*

        The fleet errors.

        - *(dict) --*

          Describes a fleet error.

          - **ErrorCode** *(string) --*

            The error code.

          - **ErrorMessage** *(string) --*

            The error message.

      - **EnableDefaultInternetAccess** *(boolean) --*

        Indicates whether default internet access is enabled for the fleet.

      - **DomainJoinInfo** *(dict) --*

        The name of the directory and organizational unit (OU) to use to join the fleet to a
        Microsoft Active Directory domain.

        - **DirectoryName** *(string) --*

          The fully qualified name of the directory (for example, corp.example.com).

        - **OrganizationalUnitDistinguishedName** *(string) --*

          The distinguished name of the organizational unit for computer accounts.

      - **IdleDisconnectTimeoutInSeconds** *(integer) --*

        The amount of time that users can be idle (inactive) before they are disconnected from
        their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins. Users
        are notified before they are disconnected due to inactivity. If users try to reconnect to
        the streaming session before the time interval specified in ``DisconnectTimeoutInSeconds``
        elapses, they are connected to their previous session. Users are considered idle when they
        stop providing keyboard or mouse input during their streaming session. File uploads and
        downloads, audio in, audio out, and pixels changing do not qualify as user activity. If
        users continue to be idle after the time interval in ``IdleDisconnectTimeoutInSeconds``
        elapses, they are disconnected.

        To prevent users from being disconnected due to inactivity, specify a value of 0.
        Otherwise, specify a value between 60 and 3600. The default value is 0.

        .. note::

          If you enable this feature, we recommend that you specify a value that corresponds
          exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do
          this, the value is rounded to the nearest minute. For example, if you specify a value of
          70, users are disconnected after 1 minute of inactivity. If you specify a value that is
          at the midpoint between two different minutes, the value is rounded up. For example, if
          you specify a value of 90, users are disconnected after 2 minutes of inactivity.

      - **IamRoleArn** *(string) --*

        The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance
        calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and passes the ARN
        of the role to use. The operation creates a new session with temporary credentials.
        AppStream 2.0 retrieves the temporary credentials and creates the
        **AppStream_Machine_Role** credential profile on the instance.

        For more information, see `Using an IAM Role to Grant Permissions to Applications and
        Scripts Running on AppStream 2.0 Streaming Instances
        <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
        in the *Amazon AppStream 2.0 Administration Guide* .
    """


_ClientUpdateFleetVpcConfigTypeDef = TypedDict(
    "_ClientUpdateFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientUpdateFleetVpcConfigTypeDef(_ClientUpdateFleetVpcConfigTypeDef):
    """
    Type definition for `ClientUpdateFleet` `VpcConfig`

    The VPC configuration for the fleet.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet instance
      or image builder instance. Fleet instances use one or more subnets. Image builder instances use
      one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_ClientUpdateImagePermissionsImagePermissionsTypeDef = TypedDict(
    "_ClientUpdateImagePermissionsImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)


class ClientUpdateImagePermissionsImagePermissionsTypeDef(
    _ClientUpdateImagePermissionsImagePermissionsTypeDef
):
    """
    Type definition for `ClientUpdateImagePermissions` `ImagePermissions`

    The permissions for the image.

    - **allowFleet** *(boolean) --*

      Indicates whether the image can be used for a fleet.

    - **allowImageBuilder** *(boolean) --*

      Indicates whether the image can be used for an image builder.
    """


_RequiredClientUpdateStackAccessEndpointsTypeDef = TypedDict(
    "_RequiredClientUpdateStackAccessEndpointsTypeDef", {"EndpointType": str}
)
_OptionalClientUpdateStackAccessEndpointsTypeDef = TypedDict(
    "_OptionalClientUpdateStackAccessEndpointsTypeDef", {"VpceId": str}, total=False
)


class ClientUpdateStackAccessEndpointsTypeDef(
    _RequiredClientUpdateStackAccessEndpointsTypeDef,
    _OptionalClientUpdateStackAccessEndpointsTypeDef,
):
    """
    Type definition for `ClientUpdateStack` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you
    specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only
    through that endpoint. When you specify an interface endpoint for an image builder,
    administrators can connect to the image builder only through that endpoint.

    - **EndpointType** *(string) --* **[REQUIRED]**

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_RequiredClientUpdateStackApplicationSettingsTypeDef = TypedDict(
    "_RequiredClientUpdateStackApplicationSettingsTypeDef", {"Enabled": bool}
)
_OptionalClientUpdateStackApplicationSettingsTypeDef = TypedDict(
    "_OptionalClientUpdateStackApplicationSettingsTypeDef",
    {"SettingsGroup": str},
    total=False,
)


class ClientUpdateStackApplicationSettingsTypeDef(
    _RequiredClientUpdateStackApplicationSettingsTypeDef,
    _OptionalClientUpdateStackApplicationSettingsTypeDef,
):
    """
    Type definition for `ClientUpdateStack` `ApplicationSettings`

    The persistent application settings for users of a stack. When these settings are enabled,
    changes that users make to applications and Windows settings are automatically saved after each
    session and applied to the next session.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Enables or disables persistent application settings for users during their streaming sessions.

    - **SettingsGroup** *(string) --*

      The path prefix for the S3 bucket where users’ persistent application settings are stored. You
      can allow the same persistent application settings to be used across multiple stacks by
      specifying the same settings group for each stack.
    """


_ClientUpdateStackResponseStackAccessEndpointsTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientUpdateStackResponseStackAccessEndpointsTypeDef(
    _ClientUpdateStackResponseStackAccessEndpointsTypeDef
):
    """
    Type definition for `ClientUpdateStackResponseStack` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
    When you specify an interface endpoint for a stack, users of the stack can connect to
    AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
    image builder, administrators can connect to the image builder only through that endpoint.

    - **EndpointType** *(string) --*

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_ClientUpdateStackResponseStackApplicationSettingsTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)


class ClientUpdateStackResponseStackApplicationSettingsTypeDef(
    _ClientUpdateStackResponseStackApplicationSettingsTypeDef
):
    """
    Type definition for `ClientUpdateStackResponseStack` `ApplicationSettings`

    The persistent application settings for users of the stack.

    - **Enabled** *(boolean) --*

      Specifies whether persistent application settings are enabled for users during their
      streaming sessions.

    - **SettingsGroup** *(string) --*

      The path prefix for the S3 bucket where users’ persistent application settings are stored.

    - **S3BucketName** *(string) --*

      The S3 bucket where users’ persistent application settings are stored. When persistent
      application settings are enabled for the first time for an account in an AWS Region, an
      S3 bucket is created. The bucket is unique to the AWS account and the Region.
    """


_ClientUpdateStackResponseStackStackErrorsTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackStackErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientUpdateStackResponseStackStackErrorsTypeDef(
    _ClientUpdateStackResponseStackStackErrorsTypeDef
):
    """
    Type definition for `ClientUpdateStackResponseStack` `StackErrors`

    Describes a stack error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientUpdateStackResponseStackStorageConnectorsTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackStorageConnectorsTypeDef",
    {"ConnectorType": str, "ResourceIdentifier": str, "Domains": List[str]},
    total=False,
)


class ClientUpdateStackResponseStackStorageConnectorsTypeDef(
    _ClientUpdateStackResponseStackStorageConnectorsTypeDef
):
    """
    Type definition for `ClientUpdateStackResponseStack` `StorageConnectors`

    Describes a connector that enables persistent storage for users.

    - **ConnectorType** *(string) --*

      The type of storage connector.

    - **ResourceIdentifier** *(string) --*

      The ARN of the storage connector.

    - **Domains** *(list) --*

      The names of the domains for the account.

      - *(string) --* GSuite domain for GDrive integration.
    """


_ClientUpdateStackResponseStackUserSettingsTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackUserSettingsTypeDef",
    {"Action": str, "Permission": str},
    total=False,
)


class ClientUpdateStackResponseStackUserSettingsTypeDef(
    _ClientUpdateStackResponseStackUserSettingsTypeDef
):
    """
    Type definition for `ClientUpdateStackResponseStack` `UserSettings`

    Describes an action and whether the action is enabled or disabled for users during their
    streaming sessions.

    - **Action** *(string) --*

      The action that is enabled or disabled.

    - **Permission** *(string) --*

      Indicates whether the action is enabled or disabled.
    """


_ClientUpdateStackResponseStackTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "StorageConnectors": List[
            ClientUpdateStackResponseStackStorageConnectorsTypeDef
        ],
        "RedirectURL": str,
        "FeedbackURL": str,
        "StackErrors": List[ClientUpdateStackResponseStackStackErrorsTypeDef],
        "UserSettings": List[ClientUpdateStackResponseStackUserSettingsTypeDef],
        "ApplicationSettings": ClientUpdateStackResponseStackApplicationSettingsTypeDef,
        "AccessEndpoints": List[ClientUpdateStackResponseStackAccessEndpointsTypeDef],
        "EmbedHostDomains": List[str],
    },
    total=False,
)


class ClientUpdateStackResponseStackTypeDef(_ClientUpdateStackResponseStackTypeDef):
    """
    Type definition for `ClientUpdateStackResponse` `Stack`

    Information about the stack.

    - **Arn** *(string) --*

      The ARN of the stack.

    - **Name** *(string) --*

      The name of the stack.

    - **Description** *(string) --*

      The description to display.

    - **DisplayName** *(string) --*

      The stack name to display.

    - **CreatedTime** *(datetime) --*

      The time the stack was created.

    - **StorageConnectors** *(list) --*

      The storage connectors to enable.

      - *(dict) --*

        Describes a connector that enables persistent storage for users.

        - **ConnectorType** *(string) --*

          The type of storage connector.

        - **ResourceIdentifier** *(string) --*

          The ARN of the storage connector.

        - **Domains** *(list) --*

          The names of the domains for the account.

          - *(string) --* GSuite domain for GDrive integration.

    - **RedirectURL** *(string) --*

      The URL that users are redirected to after their streaming session ends.

    - **FeedbackURL** *(string) --*

      The URL that users are redirected to after they click the Send Feedback link. If no URL is
      specified, no Send Feedback link is displayed.

    - **StackErrors** *(list) --*

      The errors for the stack.

      - *(dict) --*

        Describes a stack error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

    - **UserSettings** *(list) --*

      The actions that are enabled or disabled for users during their streaming sessions. By
      default these actions are enabled.

      - *(dict) --*

        Describes an action and whether the action is enabled or disabled for users during their
        streaming sessions.

        - **Action** *(string) --*

          The action that is enabled or disabled.

        - **Permission** *(string) --*

          Indicates whether the action is enabled or disabled.

    - **ApplicationSettings** *(dict) --*

      The persistent application settings for users of the stack.

      - **Enabled** *(boolean) --*

        Specifies whether persistent application settings are enabled for users during their
        streaming sessions.

      - **SettingsGroup** *(string) --*

        The path prefix for the S3 bucket where users’ persistent application settings are stored.

      - **S3BucketName** *(string) --*

        The S3 bucket where users’ persistent application settings are stored. When persistent
        application settings are enabled for the first time for an account in an AWS Region, an
        S3 bucket is created. The bucket is unique to the AWS account and the Region.

    - **AccessEndpoints** *(list) --*

      The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can
      connect to AppStream 2.0 only through the specified endpoints.

      - *(dict) --*

        Describes an interface VPC endpoint (interface endpoint) that lets you create a private
        connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
        When you specify an interface endpoint for a stack, users of the stack can connect to
        AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
        image builder, administrators can connect to the image builder only through that endpoint.

        - **EndpointType** *(string) --*

          The type of interface endpoint.

        - **VpceId** *(string) --*

          The identifier (ID) of the VPC in which the interface endpoint is used.

    - **EmbedHostDomains** *(list) --*

      The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must
      approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

      - *(string) --* Specifies a valid domain that can embed AppStream. Valid examples include:
      ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples include:
      ["test,com", ".com", "h*llo.com". ""]
    """


_ClientUpdateStackResponseTypeDef = TypedDict(
    "_ClientUpdateStackResponseTypeDef",
    {"Stack": ClientUpdateStackResponseStackTypeDef},
    total=False,
)


class ClientUpdateStackResponseTypeDef(_ClientUpdateStackResponseTypeDef):
    """
    Type definition for `ClientUpdateStack` `Response`

    - **Stack** *(dict) --*

      Information about the stack.

      - **Arn** *(string) --*

        The ARN of the stack.

      - **Name** *(string) --*

        The name of the stack.

      - **Description** *(string) --*

        The description to display.

      - **DisplayName** *(string) --*

        The stack name to display.

      - **CreatedTime** *(datetime) --*

        The time the stack was created.

      - **StorageConnectors** *(list) --*

        The storage connectors to enable.

        - *(dict) --*

          Describes a connector that enables persistent storage for users.

          - **ConnectorType** *(string) --*

            The type of storage connector.

          - **ResourceIdentifier** *(string) --*

            The ARN of the storage connector.

          - **Domains** *(list) --*

            The names of the domains for the account.

            - *(string) --* GSuite domain for GDrive integration.

      - **RedirectURL** *(string) --*

        The URL that users are redirected to after their streaming session ends.

      - **FeedbackURL** *(string) --*

        The URL that users are redirected to after they click the Send Feedback link. If no URL is
        specified, no Send Feedback link is displayed.

      - **StackErrors** *(list) --*

        The errors for the stack.

        - *(dict) --*

          Describes a stack error.

          - **ErrorCode** *(string) --*

            The error code.

          - **ErrorMessage** *(string) --*

            The error message.

      - **UserSettings** *(list) --*

        The actions that are enabled or disabled for users during their streaming sessions. By
        default these actions are enabled.

        - *(dict) --*

          Describes an action and whether the action is enabled or disabled for users during their
          streaming sessions.

          - **Action** *(string) --*

            The action that is enabled or disabled.

          - **Permission** *(string) --*

            Indicates whether the action is enabled or disabled.

      - **ApplicationSettings** *(dict) --*

        The persistent application settings for users of the stack.

        - **Enabled** *(boolean) --*

          Specifies whether persistent application settings are enabled for users during their
          streaming sessions.

        - **SettingsGroup** *(string) --*

          The path prefix for the S3 bucket where users’ persistent application settings are stored.

        - **S3BucketName** *(string) --*

          The S3 bucket where users’ persistent application settings are stored. When persistent
          application settings are enabled for the first time for an account in an AWS Region, an
          S3 bucket is created. The bucket is unique to the AWS account and the Region.

      - **AccessEndpoints** *(list) --*

        The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can
        connect to AppStream 2.0 only through the specified endpoints.

        - *(dict) --*

          Describes an interface VPC endpoint (interface endpoint) that lets you create a private
          connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
          When you specify an interface endpoint for a stack, users of the stack can connect to
          AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
          image builder, administrators can connect to the image builder only through that endpoint.

          - **EndpointType** *(string) --*

            The type of interface endpoint.

          - **VpceId** *(string) --*

            The identifier (ID) of the VPC in which the interface endpoint is used.

      - **EmbedHostDomains** *(list) --*

        The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must
        approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

        - *(string) --* Specifies a valid domain that can embed AppStream. Valid examples include:
        ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples include:
        ["test,com", ".com", "h*llo.com". ""]
    """


_RequiredClientUpdateStackStorageConnectorsTypeDef = TypedDict(
    "_RequiredClientUpdateStackStorageConnectorsTypeDef", {"ConnectorType": str}
)
_OptionalClientUpdateStackStorageConnectorsTypeDef = TypedDict(
    "_OptionalClientUpdateStackStorageConnectorsTypeDef",
    {"ResourceIdentifier": str, "Domains": List[str]},
    total=False,
)


class ClientUpdateStackStorageConnectorsTypeDef(
    _RequiredClientUpdateStackStorageConnectorsTypeDef,
    _OptionalClientUpdateStackStorageConnectorsTypeDef,
):
    """
    Type definition for `ClientUpdateStack` `StorageConnectors`

    Describes a connector that enables persistent storage for users.

    - **ConnectorType** *(string) --* **[REQUIRED]**

      The type of storage connector.

    - **ResourceIdentifier** *(string) --*

      The ARN of the storage connector.

    - **Domains** *(list) --*

      The names of the domains for the account.

      - *(string) --* GSuite domain for GDrive integration.
    """


_ClientUpdateStackUserSettingsTypeDef = TypedDict(
    "_ClientUpdateStackUserSettingsTypeDef", {"Action": str, "Permission": str}
)


class ClientUpdateStackUserSettingsTypeDef(_ClientUpdateStackUserSettingsTypeDef):
    """
    Type definition for `ClientUpdateStack` `UserSettings`

    Describes an action and whether the action is enabled or disabled for users during their
    streaming sessions.

    - **Action** *(string) --* **[REQUIRED]**

      The action that is enabled or disabled.

    - **Permission** *(string) --* **[REQUIRED]**

      Indicates whether the action is enabled or disabled.
    """


_DescribeDirectoryConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDirectoryConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDirectoryConfigsPaginatePaginationConfigTypeDef(
    _DescribeDirectoryConfigsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDirectoryConfigsPaginate` `PaginationConfig`

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


_DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef = TypedDict(
    "_DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)


class DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef(
    _DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef
):
    """
    Type definition for `DescribeDirectoryConfigsPaginateResponseDirectoryConfigs` `ServiceAccountCredentials`

    The credentials for the service account used by the fleet or image builder to connect to
    the directory.

    - **AccountName** *(string) --*

      The user name of the account. This account must have the following privileges: create
      computer objects, join computers to the domain, and change/reset the password on
      descendant computer objects for the organizational units specified.

    - **AccountPassword** *(string) --*

      The password for the account.
    """


_DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef = TypedDict(
    "_DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)


class DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef(
    _DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef
):
    """
    Type definition for `DescribeDirectoryConfigsPaginateResponse` `DirectoryConfigs`

    Describes the configuration information required to join fleets and image builders to
    Microsoft Active Directory domains.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedNames** *(list) --*

      The distinguished names of the organizational units for computer accounts.

      - *(string) --*

    - **ServiceAccountCredentials** *(dict) --*

      The credentials for the service account used by the fleet or image builder to connect to
      the directory.

      - **AccountName** *(string) --*

        The user name of the account. This account must have the following privileges: create
        computer objects, join computers to the domain, and change/reset the password on
        descendant computer objects for the organizational units specified.

      - **AccountPassword** *(string) --*

        The password for the account.

    - **CreatedTime** *(datetime) --*

      The time the directory configuration was created.
    """


_DescribeDirectoryConfigsPaginateResponseTypeDef = TypedDict(
    "_DescribeDirectoryConfigsPaginateResponseTypeDef",
    {
        "DirectoryConfigs": List[
            DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef
        ]
    },
    total=False,
)


class DescribeDirectoryConfigsPaginateResponseTypeDef(
    _DescribeDirectoryConfigsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDirectoryConfigsPaginate` `Response`

    - **DirectoryConfigs** *(list) --*

      Information about the directory configurations. Note that although the response syntax in
      this topic includes the account password, this password is not returned in the actual
      response.

      - *(dict) --*

        Describes the configuration information required to join fleets and image builders to
        Microsoft Active Directory domains.

        - **DirectoryName** *(string) --*

          The fully qualified name of the directory (for example, corp.example.com).

        - **OrganizationalUnitDistinguishedNames** *(list) --*

          The distinguished names of the organizational units for computer accounts.

          - *(string) --*

        - **ServiceAccountCredentials** *(dict) --*

          The credentials for the service account used by the fleet or image builder to connect to
          the directory.

          - **AccountName** *(string) --*

            The user name of the account. This account must have the following privileges: create
            computer objects, join computers to the domain, and change/reset the password on
            descendant computer objects for the organizational units specified.

          - **AccountPassword** *(string) --*

            The password for the account.

        - **CreatedTime** *(datetime) --*

          The time the directory configuration was created.
    """


_DescribeFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeFleetsPaginatePaginationConfigTypeDef(
    _DescribeFleetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeFleetsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)


class DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef(
    _DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef
):
    """
    Type definition for `DescribeFleetsPaginateResponseFleets` `ComputeCapacityStatus`

    The capacity status for the fleet.

    - **Desired** *(integer) --*

      The desired number of streaming instances.

    - **Running** *(integer) --*

      The total number of simultaneous streaming instances that are running.

    - **InUse** *(integer) --*

      The number of instances in use for streaming.

    - **Available** *(integer) --*

      The number of currently available instances that can be used to stream sessions.
    """


_DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef(
    _DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef
):
    """
    Type definition for `DescribeFleetsPaginateResponseFleets` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the fleet to a
    Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef(
    _DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef
):
    """
    Type definition for `DescribeFleetsPaginateResponseFleets` `FleetErrors`

    Describes a fleet error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef(
    _DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef
):
    """
    Type definition for `DescribeFleetsPaginateResponseFleets` `VpcConfig`

    The VPC configuration for the fleet.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image
      builder instances use one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_DescribeFleetsPaginateResponseFleetsTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseFleetsTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "InstanceType": str,
        "FleetType": str,
        "ComputeCapacityStatus": DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef,
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "State": str,
        "VpcConfig": DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef,
        "CreatedTime": datetime,
        "FleetErrors": List[DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef,
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
    },
    total=False,
)


class DescribeFleetsPaginateResponseFleetsTypeDef(
    _DescribeFleetsPaginateResponseFleetsTypeDef
):
    """
    Type definition for `DescribeFleetsPaginateResponse` `Fleets`

    Describes a fleet.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the fleet.

    - **Name** *(string) --*

      The name of the fleet.

    - **DisplayName** *(string) --*

      The fleet name to display.

    - **Description** *(string) --*

      The description to display.

    - **ImageName** *(string) --*

      The name of the image used to create the fleet.

    - **ImageArn** *(string) --*

      The ARN for the public, private, or shared image.

    - **InstanceType** *(string) --*

      The instance type to use when launching fleet instances. The following instance types are
      available:

      * stream.standard.medium

      * stream.standard.large

      * stream.compute.large

      * stream.compute.xlarge

      * stream.compute.2xlarge

      * stream.compute.4xlarge

      * stream.compute.8xlarge

      * stream.memory.large

      * stream.memory.xlarge

      * stream.memory.2xlarge

      * stream.memory.4xlarge

      * stream.memory.8xlarge

      * stream.graphics-design.large

      * stream.graphics-design.xlarge

      * stream.graphics-design.2xlarge

      * stream.graphics-design.4xlarge

      * stream.graphics-desktop.2xlarge

      * stream.graphics-pro.4xlarge

      * stream.graphics-pro.8xlarge

      * stream.graphics-pro.16xlarge

    - **FleetType** *(string) --*

      The fleet type.

        ALWAYS_ON

      Provides users with instant-on access to their apps. You are charged for all running
      instances in your fleet, even if no users are streaming apps.

        ON_DEMAND

      Provide users with access to applications after they connect, which takes one to two
      minutes. You are charged for instance streaming when users are connected and a small
      hourly fee for instances that are not streaming apps.

    - **ComputeCapacityStatus** *(dict) --*

      The capacity status for the fleet.

      - **Desired** *(integer) --*

        The desired number of streaming instances.

      - **Running** *(integer) --*

        The total number of simultaneous streaming instances that are running.

      - **InUse** *(integer) --*

        The number of instances in use for streaming.

      - **Available** *(integer) --*

        The number of currently available instances that can be used to stream sessions.

    - **MaxUserDurationInSeconds** *(integer) --*

      The maximum amount of time that a streaming session can remain active, in seconds. If
      users are still connected to a streaming instance five minutes before this limit is
      reached, they are prompted to save any open documents before being disconnected. After
      this time elapses, the instance is terminated and replaced by a new instance.

      Specify a value between 600 and 360000.

    - **DisconnectTimeoutInSeconds** *(integer) --*

      The amount of time that a streaming session remains active after users disconnect. If
      they try to reconnect to the streaming session after a disconnection or network
      interruption within this time interval, they are connected to their previous session.
      Otherwise, they are connected to a new session with a new streaming instance.

      Specify a value between 60 and 360000.

    - **State** *(string) --*

      The current state for the fleet.

    - **VpcConfig** *(dict) --*

      The VPC configuration for the fleet.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets to which a network interface is attached from the fleet
        instance or image builder instance. Fleet instances use one or more subnets. Image
        builder instances use one subnet.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        The identifiers of the security groups for the fleet or image builder.

        - *(string) --*

    - **CreatedTime** *(datetime) --*

      The time the fleet was created.

    - **FleetErrors** *(list) --*

      The fleet errors.

      - *(dict) --*

        Describes a fleet error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

    - **EnableDefaultInternetAccess** *(boolean) --*

      Indicates whether default internet access is enabled for the fleet.

    - **DomainJoinInfo** *(dict) --*

      The name of the directory and organizational unit (OU) to use to join the fleet to a
      Microsoft Active Directory domain.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedName** *(string) --*

        The distinguished name of the organizational unit for computer accounts.

    - **IdleDisconnectTimeoutInSeconds** *(integer) --*

      The amount of time that users can be idle (inactive) before they are disconnected from
      their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins.
      Users are notified before they are disconnected due to inactivity. If users try to
      reconnect to the streaming session before the time interval specified in
      ``DisconnectTimeoutInSeconds`` elapses, they are connected to their previous session.
      Users are considered idle when they stop providing keyboard or mouse input during their
      streaming session. File uploads and downloads, audio in, audio out, and pixels changing
      do not qualify as user activity. If users continue to be idle after the time interval in
      ``IdleDisconnectTimeoutInSeconds`` elapses, they are disconnected.

      To prevent users from being disconnected due to inactivity, specify a value of 0.
      Otherwise, specify a value between 60 and 3600. The default value is 0.

      .. note::

        If you enable this feature, we recommend that you specify a value that corresponds
        exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do
        this, the value is rounded to the nearest minute. For example, if you specify a value
        of 70, users are disconnected after 1 minute of inactivity. If you specify a value that
        is at the midpoint between two different minutes, the value is rounded up. For example,
        if you specify a value of 90, users are disconnected after 2 minutes of inactivity.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet
      instance calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and
      passes the ARN of the role to use. The operation creates a new session with temporary
      credentials. AppStream 2.0 retrieves the temporary credentials and creates the
      **AppStream_Machine_Role** credential profile on the instance.

      For more information, see `Using an IAM Role to Grant Permissions to Applications and
      Scripts Running on AppStream 2.0 Streaming Instances
      <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
      in the *Amazon AppStream 2.0 Administration Guide* .
    """


_DescribeFleetsPaginateResponseTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseTypeDef",
    {"Fleets": List[DescribeFleetsPaginateResponseFleetsTypeDef]},
    total=False,
)


class DescribeFleetsPaginateResponseTypeDef(_DescribeFleetsPaginateResponseTypeDef):
    """
    Type definition for `DescribeFleetsPaginate` `Response`

    - **Fleets** *(list) --*

      Information about the fleets.

      - *(dict) --*

        Describes a fleet.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) for the fleet.

        - **Name** *(string) --*

          The name of the fleet.

        - **DisplayName** *(string) --*

          The fleet name to display.

        - **Description** *(string) --*

          The description to display.

        - **ImageName** *(string) --*

          The name of the image used to create the fleet.

        - **ImageArn** *(string) --*

          The ARN for the public, private, or shared image.

        - **InstanceType** *(string) --*

          The instance type to use when launching fleet instances. The following instance types are
          available:

          * stream.standard.medium

          * stream.standard.large

          * stream.compute.large

          * stream.compute.xlarge

          * stream.compute.2xlarge

          * stream.compute.4xlarge

          * stream.compute.8xlarge

          * stream.memory.large

          * stream.memory.xlarge

          * stream.memory.2xlarge

          * stream.memory.4xlarge

          * stream.memory.8xlarge

          * stream.graphics-design.large

          * stream.graphics-design.xlarge

          * stream.graphics-design.2xlarge

          * stream.graphics-design.4xlarge

          * stream.graphics-desktop.2xlarge

          * stream.graphics-pro.4xlarge

          * stream.graphics-pro.8xlarge

          * stream.graphics-pro.16xlarge

        - **FleetType** *(string) --*

          The fleet type.

            ALWAYS_ON

          Provides users with instant-on access to their apps. You are charged for all running
          instances in your fleet, even if no users are streaming apps.

            ON_DEMAND

          Provide users with access to applications after they connect, which takes one to two
          minutes. You are charged for instance streaming when users are connected and a small
          hourly fee for instances that are not streaming apps.

        - **ComputeCapacityStatus** *(dict) --*

          The capacity status for the fleet.

          - **Desired** *(integer) --*

            The desired number of streaming instances.

          - **Running** *(integer) --*

            The total number of simultaneous streaming instances that are running.

          - **InUse** *(integer) --*

            The number of instances in use for streaming.

          - **Available** *(integer) --*

            The number of currently available instances that can be used to stream sessions.

        - **MaxUserDurationInSeconds** *(integer) --*

          The maximum amount of time that a streaming session can remain active, in seconds. If
          users are still connected to a streaming instance five minutes before this limit is
          reached, they are prompted to save any open documents before being disconnected. After
          this time elapses, the instance is terminated and replaced by a new instance.

          Specify a value between 600 and 360000.

        - **DisconnectTimeoutInSeconds** *(integer) --*

          The amount of time that a streaming session remains active after users disconnect. If
          they try to reconnect to the streaming session after a disconnection or network
          interruption within this time interval, they are connected to their previous session.
          Otherwise, they are connected to a new session with a new streaming instance.

          Specify a value between 60 and 360000.

        - **State** *(string) --*

          The current state for the fleet.

        - **VpcConfig** *(dict) --*

          The VPC configuration for the fleet.

          - **SubnetIds** *(list) --*

            The identifiers of the subnets to which a network interface is attached from the fleet
            instance or image builder instance. Fleet instances use one or more subnets. Image
            builder instances use one subnet.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            The identifiers of the security groups for the fleet or image builder.

            - *(string) --*

        - **CreatedTime** *(datetime) --*

          The time the fleet was created.

        - **FleetErrors** *(list) --*

          The fleet errors.

          - *(dict) --*

            Describes a fleet error.

            - **ErrorCode** *(string) --*

              The error code.

            - **ErrorMessage** *(string) --*

              The error message.

        - **EnableDefaultInternetAccess** *(boolean) --*

          Indicates whether default internet access is enabled for the fleet.

        - **DomainJoinInfo** *(dict) --*

          The name of the directory and organizational unit (OU) to use to join the fleet to a
          Microsoft Active Directory domain.

          - **DirectoryName** *(string) --*

            The fully qualified name of the directory (for example, corp.example.com).

          - **OrganizationalUnitDistinguishedName** *(string) --*

            The distinguished name of the organizational unit for computer accounts.

        - **IdleDisconnectTimeoutInSeconds** *(integer) --*

          The amount of time that users can be idle (inactive) before they are disconnected from
          their streaming session and the ``DisconnectTimeoutInSeconds`` time interval begins.
          Users are notified before they are disconnected due to inactivity. If users try to
          reconnect to the streaming session before the time interval specified in
          ``DisconnectTimeoutInSeconds`` elapses, they are connected to their previous session.
          Users are considered idle when they stop providing keyboard or mouse input during their
          streaming session. File uploads and downloads, audio in, audio out, and pixels changing
          do not qualify as user activity. If users continue to be idle after the time interval in
          ``IdleDisconnectTimeoutInSeconds`` elapses, they are disconnected.

          To prevent users from being disconnected due to inactivity, specify a value of 0.
          Otherwise, specify a value between 60 and 3600. The default value is 0.

          .. note::

            If you enable this feature, we recommend that you specify a value that corresponds
            exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do
            this, the value is rounded to the nearest minute. For example, if you specify a value
            of 70, users are disconnected after 1 minute of inactivity. If you specify a value that
            is at the midpoint between two different minutes, the value is rounded up. For example,
            if you specify a value of 90, users are disconnected after 2 minutes of inactivity.

        - **IamRoleArn** *(string) --*

          The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet
          instance calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and
          passes the ARN of the role to use. The operation creates a new session with temporary
          credentials. AppStream 2.0 retrieves the temporary credentials and creates the
          **AppStream_Machine_Role** credential profile on the instance.

          For more information, see `Using an IAM Role to Grant Permissions to Applications and
          Scripts Running on AppStream 2.0 Streaming Instances
          <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
          in the *Amazon AppStream 2.0 Administration Guide* .
    """


_DescribeImageBuildersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeImageBuildersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeImageBuildersPaginatePaginationConfigTypeDef(
    _DescribeImageBuildersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeImageBuildersPaginate` `PaginationConfig`

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


_DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef
):
    """
    Type definition for `DescribeImageBuildersPaginateResponseImageBuilders` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
    When you specify an interface endpoint for a stack, users of the stack can connect to
    AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
    image builder, administrators can connect to the image builder only through that
    endpoint.

    - **EndpointType** *(string) --*

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef
):
    """
    Type definition for `DescribeImageBuildersPaginateResponseImageBuilders` `DomainJoinInfo`

    The name of the directory and organizational unit (OU) to use to join the image builder
    to a Microsoft Active Directory domain.

    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).

    - **OrganizationalUnitDistinguishedName** *(string) --*

      The distinguished name of the organizational unit for computer accounts.
    """


_DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "ErrorTimestamp": datetime},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef
):
    """
    Type definition for `DescribeImageBuildersPaginateResponseImageBuilders` `ImageBuilderErrors`

    Describes a resource error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.

    - **ErrorTimestamp** *(datetime) --*

      The time the error occurred.
    """


_DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef
):
    """
    Type definition for `DescribeImageBuildersPaginateResponseImageBuilders` `NetworkAccessConfiguration`

    Describes the network details of the fleet or image builder instance.

    - **EniPrivateIpAddress** *(string) --*

      The private IP address of the elastic network interface that is attached to instances
      in your VPC.

    - **EniId** *(string) --*

      The resource identifier of the elastic network interface that is attached to instances
      in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef
):
    """
    Type definition for `DescribeImageBuildersPaginateResponseImageBuilders` `StateChangeReason`

    The reason why the last state change occurred.

    - **Code** *(string) --*

      The state change reason code.

    - **Message** *(string) --*

      The state change reason message.
    """


_DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef
):
    """
    Type definition for `DescribeImageBuildersPaginateResponseImageBuilders` `VpcConfig`

    The VPC configuration of the image builder.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image
      builder instances use one subnet.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The identifiers of the security groups for the fleet or image builder.

      - *(string) --*
    """


_DescribeImageBuildersPaginateResponseImageBuildersTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": str,
        "IamRoleArn": str,
        "State": str,
        "StateChangeReason": DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[
            DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef
        ],
    },
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersTypeDef
):
    """
    Type definition for `DescribeImageBuildersPaginateResponse` `ImageBuilders`

    Describes a virtual machine that is used to create an image.

    - **Name** *(string) --*

      The name of the image builder.

    - **Arn** *(string) --*

      The ARN for the image builder.

    - **ImageArn** *(string) --*

      The ARN of the image from which this builder was created.

    - **Description** *(string) --*

      The description to display.

    - **DisplayName** *(string) --*

      The image builder name to display.

    - **VpcConfig** *(dict) --*

      The VPC configuration of the image builder.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets to which a network interface is attached from the fleet
        instance or image builder instance. Fleet instances use one or more subnets. Image
        builder instances use one subnet.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        The identifiers of the security groups for the fleet or image builder.

        - *(string) --*

    - **InstanceType** *(string) --*

      The instance type for the image builder. The following instance types are available:

      * stream.standard.medium

      * stream.standard.large

      * stream.compute.large

      * stream.compute.xlarge

      * stream.compute.2xlarge

      * stream.compute.4xlarge

      * stream.compute.8xlarge

      * stream.memory.large

      * stream.memory.xlarge

      * stream.memory.2xlarge

      * stream.memory.4xlarge

      * stream.memory.8xlarge

      * stream.graphics-design.large

      * stream.graphics-design.xlarge

      * stream.graphics-design.2xlarge

      * stream.graphics-design.4xlarge

      * stream.graphics-desktop.2xlarge

      * stream.graphics-pro.4xlarge

      * stream.graphics-pro.8xlarge

      * stream.graphics-pro.16xlarge

    - **Platform** *(string) --*

      The operating system platform of the image builder.

    - **IamRoleArn** *(string) --*

      The ARN of the IAM role that is applied to the image builder. To assume a role, the image
      builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and
      passes the ARN of the role to use. The operation creates a new session with temporary
      credentials. AppStream 2.0 retrieves the temporary credentials and creates the
      **AppStream_Machine_Role** credential profile on the instance.

      For more information, see `Using an IAM Role to Grant Permissions to Applications and
      Scripts Running on AppStream 2.0 Streaming Instances
      <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
      in the *Amazon AppStream 2.0 Administration Guide* .

    - **State** *(string) --*

      The state of the image builder.

    - **StateChangeReason** *(dict) --*

      The reason why the last state change occurred.

      - **Code** *(string) --*

        The state change reason code.

      - **Message** *(string) --*

        The state change reason message.

    - **CreatedTime** *(datetime) --*

      The time stamp when the image builder was created.

    - **EnableDefaultInternetAccess** *(boolean) --*

      Enables or disables default internet access for the image builder.

    - **DomainJoinInfo** *(dict) --*

      The name of the directory and organizational unit (OU) to use to join the image builder
      to a Microsoft Active Directory domain.

      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).

      - **OrganizationalUnitDistinguishedName** *(string) --*

        The distinguished name of the organizational unit for computer accounts.

    - **NetworkAccessConfiguration** *(dict) --*

      Describes the network details of the fleet or image builder instance.

      - **EniPrivateIpAddress** *(string) --*

        The private IP address of the elastic network interface that is attached to instances
        in your VPC.

      - **EniId** *(string) --*

        The resource identifier of the elastic network interface that is attached to instances
        in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

    - **ImageBuilderErrors** *(list) --*

      The image builder errors.

      - *(dict) --*

        Describes a resource error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

        - **ErrorTimestamp** *(datetime) --*

          The time the error occurred.

    - **AppstreamAgentVersion** *(string) --*

      The version of the AppStream 2.0 agent that is currently being used by the image builder.

    - **AccessEndpoints** *(list) --*

      The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
      connect to the image builder only through the specified endpoints.

      - *(dict) --*

        Describes an interface VPC endpoint (interface endpoint) that lets you create a private
        connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
        When you specify an interface endpoint for a stack, users of the stack can connect to
        AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
        image builder, administrators can connect to the image builder only through that
        endpoint.

        - **EndpointType** *(string) --*

          The type of interface endpoint.

        - **VpceId** *(string) --*

          The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_DescribeImageBuildersPaginateResponseTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseTypeDef",
    {"ImageBuilders": List[DescribeImageBuildersPaginateResponseImageBuildersTypeDef]},
    total=False,
)


class DescribeImageBuildersPaginateResponseTypeDef(
    _DescribeImageBuildersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeImageBuildersPaginate` `Response`

    - **ImageBuilders** *(list) --*

      Information about the image builders.

      - *(dict) --*

        Describes a virtual machine that is used to create an image.

        - **Name** *(string) --*

          The name of the image builder.

        - **Arn** *(string) --*

          The ARN for the image builder.

        - **ImageArn** *(string) --*

          The ARN of the image from which this builder was created.

        - **Description** *(string) --*

          The description to display.

        - **DisplayName** *(string) --*

          The image builder name to display.

        - **VpcConfig** *(dict) --*

          The VPC configuration of the image builder.

          - **SubnetIds** *(list) --*

            The identifiers of the subnets to which a network interface is attached from the fleet
            instance or image builder instance. Fleet instances use one or more subnets. Image
            builder instances use one subnet.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            The identifiers of the security groups for the fleet or image builder.

            - *(string) --*

        - **InstanceType** *(string) --*

          The instance type for the image builder. The following instance types are available:

          * stream.standard.medium

          * stream.standard.large

          * stream.compute.large

          * stream.compute.xlarge

          * stream.compute.2xlarge

          * stream.compute.4xlarge

          * stream.compute.8xlarge

          * stream.memory.large

          * stream.memory.xlarge

          * stream.memory.2xlarge

          * stream.memory.4xlarge

          * stream.memory.8xlarge

          * stream.graphics-design.large

          * stream.graphics-design.xlarge

          * stream.graphics-design.2xlarge

          * stream.graphics-design.4xlarge

          * stream.graphics-desktop.2xlarge

          * stream.graphics-pro.4xlarge

          * stream.graphics-pro.8xlarge

          * stream.graphics-pro.16xlarge

        - **Platform** *(string) --*

          The operating system platform of the image builder.

        - **IamRoleArn** *(string) --*

          The ARN of the IAM role that is applied to the image builder. To assume a role, the image
          builder calls the AWS Security Token Service (STS) ``AssumeRole`` API operation and
          passes the ARN of the role to use. The operation creates a new session with temporary
          credentials. AppStream 2.0 retrieves the temporary credentials and creates the
          **AppStream_Machine_Role** credential profile on the instance.

          For more information, see `Using an IAM Role to Grant Permissions to Applications and
          Scripts Running on AppStream 2.0 Streaming Instances
          <https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html>`__
          in the *Amazon AppStream 2.0 Administration Guide* .

        - **State** *(string) --*

          The state of the image builder.

        - **StateChangeReason** *(dict) --*

          The reason why the last state change occurred.

          - **Code** *(string) --*

            The state change reason code.

          - **Message** *(string) --*

            The state change reason message.

        - **CreatedTime** *(datetime) --*

          The time stamp when the image builder was created.

        - **EnableDefaultInternetAccess** *(boolean) --*

          Enables or disables default internet access for the image builder.

        - **DomainJoinInfo** *(dict) --*

          The name of the directory and organizational unit (OU) to use to join the image builder
          to a Microsoft Active Directory domain.

          - **DirectoryName** *(string) --*

            The fully qualified name of the directory (for example, corp.example.com).

          - **OrganizationalUnitDistinguishedName** *(string) --*

            The distinguished name of the organizational unit for computer accounts.

        - **NetworkAccessConfiguration** *(dict) --*

          Describes the network details of the fleet or image builder instance.

          - **EniPrivateIpAddress** *(string) --*

            The private IP address of the elastic network interface that is attached to instances
            in your VPC.

          - **EniId** *(string) --*

            The resource identifier of the elastic network interface that is attached to instances
            in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.

        - **ImageBuilderErrors** *(list) --*

          The image builder errors.

          - *(dict) --*

            Describes a resource error.

            - **ErrorCode** *(string) --*

              The error code.

            - **ErrorMessage** *(string) --*

              The error message.

            - **ErrorTimestamp** *(datetime) --*

              The time the error occurred.

        - **AppstreamAgentVersion** *(string) --*

          The version of the AppStream 2.0 agent that is currently being used by the image builder.

        - **AccessEndpoints** *(list) --*

          The list of virtual private cloud (VPC) interface endpoint objects. Administrators can
          connect to the image builder only through the specified endpoints.

          - *(dict) --*

            Describes an interface VPC endpoint (interface endpoint) that lets you create a private
            connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
            When you specify an interface endpoint for a stack, users of the stack can connect to
            AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
            image builder, administrators can connect to the image builder only through that
            endpoint.

            - **EndpointType** *(string) --*

              The type of interface endpoint.

            - **VpceId** *(string) --*

              The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_DescribeImagesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeImagesPaginatePaginationConfigTypeDef(
    _DescribeImagesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeImagesPaginate` `PaginationConfig`

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


_DescribeImagesPaginateResponseImagesApplicationsTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseImagesApplicationsTypeDef",
    {
        "Name": str,
        "DisplayName": str,
        "IconURL": str,
        "LaunchPath": str,
        "LaunchParameters": str,
        "Enabled": bool,
        "Metadata": Dict[str, str],
    },
    total=False,
)


class DescribeImagesPaginateResponseImagesApplicationsTypeDef(
    _DescribeImagesPaginateResponseImagesApplicationsTypeDef
):
    """
    Type definition for `DescribeImagesPaginateResponseImages` `Applications`

    Describes an application in the application catalog.

    - **Name** *(string) --*

      The name of the application.

    - **DisplayName** *(string) --*

      The application name to display.

    - **IconURL** *(string) --*

      The URL for the application icon. This URL might be time-limited.

    - **LaunchPath** *(string) --*

      The path to the application executable in the instance.

    - **LaunchParameters** *(string) --*

      The arguments that are passed to the application at launch.

    - **Enabled** *(boolean) --*

      If there is a problem, the application can be disabled after image creation.

    - **Metadata** *(dict) --*

      Additional attributes that describe the application.

      - *(string) --*

        - *(string) --*
    """


_DescribeImagesPaginateResponseImagesImagePermissionsTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseImagesImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)


class DescribeImagesPaginateResponseImagesImagePermissionsTypeDef(
    _DescribeImagesPaginateResponseImagesImagePermissionsTypeDef
):
    """
    Type definition for `DescribeImagesPaginateResponseImages` `ImagePermissions`

    The permissions to provide to the destination AWS account for the specified image.

    - **allowFleet** *(boolean) --*

      Indicates whether the image can be used for a fleet.

    - **allowImageBuilder** *(boolean) --*

      Indicates whether the image can be used for an image builder.
    """


_DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef(
    _DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef
):
    """
    Type definition for `DescribeImagesPaginateResponseImages` `StateChangeReason`

    The reason why the last state change occurred.

    - **Code** *(string) --*

      The state change reason code.

    - **Message** *(string) --*

      The state change reason message.
    """


_DescribeImagesPaginateResponseImagesTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseImagesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "BaseImageArn": str,
        "DisplayName": str,
        "State": str,
        "Visibility": str,
        "ImageBuilderSupported": bool,
        "ImageBuilderName": str,
        "Platform": str,
        "Description": str,
        "StateChangeReason": DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef,
        "Applications": List[DescribeImagesPaginateResponseImagesApplicationsTypeDef],
        "CreatedTime": datetime,
        "PublicBaseImageReleasedDate": datetime,
        "AppstreamAgentVersion": str,
        "ImagePermissions": DescribeImagesPaginateResponseImagesImagePermissionsTypeDef,
    },
    total=False,
)


class DescribeImagesPaginateResponseImagesTypeDef(
    _DescribeImagesPaginateResponseImagesTypeDef
):
    """
    Type definition for `DescribeImagesPaginateResponse` `Images`

    Describes an image.

    - **Name** *(string) --*

      The name of the image.

    - **Arn** *(string) --*

      The ARN of the image.

    - **BaseImageArn** *(string) --*

      The ARN of the image from which this image was created.

    - **DisplayName** *(string) --*

      The image name to display.

    - **State** *(string) --*

      The image starts in the ``PENDING`` state. If image creation succeeds, the state is
      ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .

    - **Visibility** *(string) --*

      Indicates whether the image is public or private.

    - **ImageBuilderSupported** *(boolean) --*

      Indicates whether an image builder can be launched from this image.

    - **ImageBuilderName** *(string) --*

      The name of the image builder that was used to create the private image. If the image is
      shared, this value is null.

    - **Platform** *(string) --*

      The operating system platform of the image.

    - **Description** *(string) --*

      The description to display.

    - **StateChangeReason** *(dict) --*

      The reason why the last state change occurred.

      - **Code** *(string) --*

        The state change reason code.

      - **Message** *(string) --*

        The state change reason message.

    - **Applications** *(list) --*

      The applications associated with the image.

      - *(dict) --*

        Describes an application in the application catalog.

        - **Name** *(string) --*

          The name of the application.

        - **DisplayName** *(string) --*

          The application name to display.

        - **IconURL** *(string) --*

          The URL for the application icon. This URL might be time-limited.

        - **LaunchPath** *(string) --*

          The path to the application executable in the instance.

        - **LaunchParameters** *(string) --*

          The arguments that are passed to the application at launch.

        - **Enabled** *(boolean) --*

          If there is a problem, the application can be disabled after image creation.

        - **Metadata** *(dict) --*

          Additional attributes that describe the application.

          - *(string) --*

            - *(string) --*

    - **CreatedTime** *(datetime) --*

      The time the image was created.

    - **PublicBaseImageReleasedDate** *(datetime) --*

      The release date of the public base image. For private images, this date is the release
      date of the base image from which the image was created.

    - **AppstreamAgentVersion** *(string) --*

      The version of the AppStream 2.0 agent to use for instances that are launched from this
      image.

    - **ImagePermissions** *(dict) --*

      The permissions to provide to the destination AWS account for the specified image.

      - **allowFleet** *(boolean) --*

        Indicates whether the image can be used for a fleet.

      - **allowImageBuilder** *(boolean) --*

        Indicates whether the image can be used for an image builder.
    """


_DescribeImagesPaginateResponseTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseTypeDef",
    {"Images": List[DescribeImagesPaginateResponseImagesTypeDef]},
    total=False,
)


class DescribeImagesPaginateResponseTypeDef(_DescribeImagesPaginateResponseTypeDef):
    """
    Type definition for `DescribeImagesPaginate` `Response`

    - **Images** *(list) --*

      Information about the images.

      - *(dict) --*

        Describes an image.

        - **Name** *(string) --*

          The name of the image.

        - **Arn** *(string) --*

          The ARN of the image.

        - **BaseImageArn** *(string) --*

          The ARN of the image from which this image was created.

        - **DisplayName** *(string) --*

          The image name to display.

        - **State** *(string) --*

          The image starts in the ``PENDING`` state. If image creation succeeds, the state is
          ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .

        - **Visibility** *(string) --*

          Indicates whether the image is public or private.

        - **ImageBuilderSupported** *(boolean) --*

          Indicates whether an image builder can be launched from this image.

        - **ImageBuilderName** *(string) --*

          The name of the image builder that was used to create the private image. If the image is
          shared, this value is null.

        - **Platform** *(string) --*

          The operating system platform of the image.

        - **Description** *(string) --*

          The description to display.

        - **StateChangeReason** *(dict) --*

          The reason why the last state change occurred.

          - **Code** *(string) --*

            The state change reason code.

          - **Message** *(string) --*

            The state change reason message.

        - **Applications** *(list) --*

          The applications associated with the image.

          - *(dict) --*

            Describes an application in the application catalog.

            - **Name** *(string) --*

              The name of the application.

            - **DisplayName** *(string) --*

              The application name to display.

            - **IconURL** *(string) --*

              The URL for the application icon. This URL might be time-limited.

            - **LaunchPath** *(string) --*

              The path to the application executable in the instance.

            - **LaunchParameters** *(string) --*

              The arguments that are passed to the application at launch.

            - **Enabled** *(boolean) --*

              If there is a problem, the application can be disabled after image creation.

            - **Metadata** *(dict) --*

              Additional attributes that describe the application.

              - *(string) --*

                - *(string) --*

        - **CreatedTime** *(datetime) --*

          The time the image was created.

        - **PublicBaseImageReleasedDate** *(datetime) --*

          The release date of the public base image. For private images, this date is the release
          date of the base image from which the image was created.

        - **AppstreamAgentVersion** *(string) --*

          The version of the AppStream 2.0 agent to use for instances that are launched from this
          image.

        - **ImagePermissions** *(dict) --*

          The permissions to provide to the destination AWS account for the specified image.

          - **allowFleet** *(boolean) --*

            Indicates whether the image can be used for a fleet.

          - **allowImageBuilder** *(boolean) --*

            Indicates whether the image can be used for an image builder.
    """


_DescribeSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSessionsPaginatePaginationConfigTypeDef(
    _DescribeSessionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeSessionsPaginate` `PaginationConfig`

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


_DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef = TypedDict(
    "_DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef(
    _DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef
):
    """
    Type definition for `DescribeSessionsPaginateResponseSessions` `NetworkAccessConfiguration`

    The network details for the streaming session.

    - **EniPrivateIpAddress** *(string) --*

      The private IP address of the elastic network interface that is attached to instances
      in your VPC.

    - **EniId** *(string) --*

      The resource identifier of the elastic network interface that is attached to instances
      in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_DescribeSessionsPaginateResponseSessionsTypeDef = TypedDict(
    "_DescribeSessionsPaginateResponseSessionsTypeDef",
    {
        "Id": str,
        "UserId": str,
        "StackName": str,
        "FleetName": str,
        "State": str,
        "ConnectionState": str,
        "StartTime": datetime,
        "MaxExpirationTime": datetime,
        "AuthenticationType": str,
        "NetworkAccessConfiguration": DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef,
    },
    total=False,
)


class DescribeSessionsPaginateResponseSessionsTypeDef(
    _DescribeSessionsPaginateResponseSessionsTypeDef
):
    """
    Type definition for `DescribeSessionsPaginateResponse` `Sessions`

    Describes a streaming session.

    - **Id** *(string) --*

      The identifier of the streaming session.

    - **UserId** *(string) --*

      The identifier of the user for whom the session was created.

    - **StackName** *(string) --*

      The name of the stack for the streaming session.

    - **FleetName** *(string) --*

      The name of the fleet for the streaming session.

    - **State** *(string) --*

      The current state of the streaming session.

    - **ConnectionState** *(string) --*

      Specifies whether a user is connected to the streaming session.

    - **StartTime** *(datetime) --*

      The time when a streaming instance is dedicated for the user.

    - **MaxExpirationTime** *(datetime) --*

      The time when the streaming session is set to expire. This time is based on the
      ``MaxUserDurationinSeconds`` value, which determines the maximum length of time that a
      streaming session can run. A streaming session might end earlier than the time specified
      in ``SessionMaxExpirationTime`` , when the ``DisconnectTimeOutInSeconds`` elapses or the
      user chooses to end his or her session. If the ``DisconnectTimeOutInSeconds`` elapses, or
      the user chooses to end his or her session, the streaming instance is terminated and the
      streaming session ends.

    - **AuthenticationType** *(string) --*

      The authentication method. The user is authenticated using a streaming URL (``API`` ) or
      SAML 2.0 federation (``SAML`` ).

    - **NetworkAccessConfiguration** *(dict) --*

      The network details for the streaming session.

      - **EniPrivateIpAddress** *(string) --*

        The private IP address of the elastic network interface that is attached to instances
        in your VPC.

      - **EniId** *(string) --*

        The resource identifier of the elastic network interface that is attached to instances
        in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_DescribeSessionsPaginateResponseTypeDef = TypedDict(
    "_DescribeSessionsPaginateResponseTypeDef",
    {"Sessions": List[DescribeSessionsPaginateResponseSessionsTypeDef]},
    total=False,
)


class DescribeSessionsPaginateResponseTypeDef(_DescribeSessionsPaginateResponseTypeDef):
    """
    Type definition for `DescribeSessionsPaginate` `Response`

    - **Sessions** *(list) --*

      Information about the streaming sessions.

      - *(dict) --*

        Describes a streaming session.

        - **Id** *(string) --*

          The identifier of the streaming session.

        - **UserId** *(string) --*

          The identifier of the user for whom the session was created.

        - **StackName** *(string) --*

          The name of the stack for the streaming session.

        - **FleetName** *(string) --*

          The name of the fleet for the streaming session.

        - **State** *(string) --*

          The current state of the streaming session.

        - **ConnectionState** *(string) --*

          Specifies whether a user is connected to the streaming session.

        - **StartTime** *(datetime) --*

          The time when a streaming instance is dedicated for the user.

        - **MaxExpirationTime** *(datetime) --*

          The time when the streaming session is set to expire. This time is based on the
          ``MaxUserDurationinSeconds`` value, which determines the maximum length of time that a
          streaming session can run. A streaming session might end earlier than the time specified
          in ``SessionMaxExpirationTime`` , when the ``DisconnectTimeOutInSeconds`` elapses or the
          user chooses to end his or her session. If the ``DisconnectTimeOutInSeconds`` elapses, or
          the user chooses to end his or her session, the streaming instance is terminated and the
          streaming session ends.

        - **AuthenticationType** *(string) --*

          The authentication method. The user is authenticated using a streaming URL (``API`` ) or
          SAML 2.0 federation (``SAML`` ).

        - **NetworkAccessConfiguration** *(dict) --*

          The network details for the streaming session.

          - **EniPrivateIpAddress** *(string) --*

            The private IP address of the elastic network interface that is attached to instances
            in your VPC.

          - **EniId** *(string) --*

            The resource identifier of the elastic network interface that is attached to instances
            in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
    """


_DescribeStacksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeStacksPaginatePaginationConfigTypeDef(
    _DescribeStacksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeStacksPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef(
    _DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacks` `AccessEndpoints`

    Describes an interface VPC endpoint (interface endpoint) that lets you create a private
    connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
    When you specify an interface endpoint for a stack, users of the stack can connect to
    AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
    image builder, administrators can connect to the image builder only through that
    endpoint.

    - **EndpointType** *(string) --*

      The type of interface endpoint.

    - **VpceId** *(string) --*

      The identifier (ID) of the VPC in which the interface endpoint is used.
    """


_DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef(
    _DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacks` `ApplicationSettings`

    The persistent application settings for users of the stack.

    - **Enabled** *(boolean) --*

      Specifies whether persistent application settings are enabled for users during their
      streaming sessions.

    - **SettingsGroup** *(string) --*

      The path prefix for the S3 bucket where users’ persistent application settings are
      stored.

    - **S3BucketName** *(string) --*

      The S3 bucket where users’ persistent application settings are stored. When persistent
      application settings are enabled for the first time for an account in an AWS Region, an
      S3 bucket is created. The bucket is unique to the AWS account and the Region.
    """


_DescribeStacksPaginateResponseStacksStackErrorsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksStackErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksStackErrorsTypeDef(
    _DescribeStacksPaginateResponseStacksStackErrorsTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacks` `StackErrors`

    Describes a stack error.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef",
    {"ConnectorType": str, "ResourceIdentifier": str, "Domains": List[str]},
    total=False,
)


class DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef(
    _DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacks` `StorageConnectors`

    Describes a connector that enables persistent storage for users.

    - **ConnectorType** *(string) --*

      The type of storage connector.

    - **ResourceIdentifier** *(string) --*

      The ARN of the storage connector.

    - **Domains** *(list) --*

      The names of the domains for the account.

      - *(string) --* GSuite domain for GDrive integration.
    """


_DescribeStacksPaginateResponseStacksUserSettingsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksUserSettingsTypeDef",
    {"Action": str, "Permission": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksUserSettingsTypeDef(
    _DescribeStacksPaginateResponseStacksUserSettingsTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponseStacks` `UserSettings`

    Describes an action and whether the action is enabled or disabled for users during
    their streaming sessions.

    - **Action** *(string) --*

      The action that is enabled or disabled.

    - **Permission** *(string) --*

      Indicates whether the action is enabled or disabled.
    """


_DescribeStacksPaginateResponseStacksTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "StorageConnectors": List[
            DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef
        ],
        "RedirectURL": str,
        "FeedbackURL": str,
        "StackErrors": List[DescribeStacksPaginateResponseStacksStackErrorsTypeDef],
        "UserSettings": List[DescribeStacksPaginateResponseStacksUserSettingsTypeDef],
        "ApplicationSettings": DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef,
        "AccessEndpoints": List[
            DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef
        ],
        "EmbedHostDomains": List[str],
    },
    total=False,
)


class DescribeStacksPaginateResponseStacksTypeDef(
    _DescribeStacksPaginateResponseStacksTypeDef
):
    """
    Type definition for `DescribeStacksPaginateResponse` `Stacks`

    Describes a stack.

    - **Arn** *(string) --*

      The ARN of the stack.

    - **Name** *(string) --*

      The name of the stack.

    - **Description** *(string) --*

      The description to display.

    - **DisplayName** *(string) --*

      The stack name to display.

    - **CreatedTime** *(datetime) --*

      The time the stack was created.

    - **StorageConnectors** *(list) --*

      The storage connectors to enable.

      - *(dict) --*

        Describes a connector that enables persistent storage for users.

        - **ConnectorType** *(string) --*

          The type of storage connector.

        - **ResourceIdentifier** *(string) --*

          The ARN of the storage connector.

        - **Domains** *(list) --*

          The names of the domains for the account.

          - *(string) --* GSuite domain for GDrive integration.

    - **RedirectURL** *(string) --*

      The URL that users are redirected to after their streaming session ends.

    - **FeedbackURL** *(string) --*

      The URL that users are redirected to after they click the Send Feedback link. If no URL
      is specified, no Send Feedback link is displayed.

    - **StackErrors** *(list) --*

      The errors for the stack.

      - *(dict) --*

        Describes a stack error.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.

    - **UserSettings** *(list) --*

      The actions that are enabled or disabled for users during their streaming sessions. By
      default these actions are enabled.

      - *(dict) --*

        Describes an action and whether the action is enabled or disabled for users during
        their streaming sessions.

        - **Action** *(string) --*

          The action that is enabled or disabled.

        - **Permission** *(string) --*

          Indicates whether the action is enabled or disabled.

    - **ApplicationSettings** *(dict) --*

      The persistent application settings for users of the stack.

      - **Enabled** *(boolean) --*

        Specifies whether persistent application settings are enabled for users during their
        streaming sessions.

      - **SettingsGroup** *(string) --*

        The path prefix for the S3 bucket where users’ persistent application settings are
        stored.

      - **S3BucketName** *(string) --*

        The S3 bucket where users’ persistent application settings are stored. When persistent
        application settings are enabled for the first time for an account in an AWS Region, an
        S3 bucket is created. The bucket is unique to the AWS account and the Region.

    - **AccessEndpoints** *(list) --*

      The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack
      can connect to AppStream 2.0 only through the specified endpoints.

      - *(dict) --*

        Describes an interface VPC endpoint (interface endpoint) that lets you create a private
        connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
        When you specify an interface endpoint for a stack, users of the stack can connect to
        AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
        image builder, administrators can connect to the image builder only through that
        endpoint.

        - **EndpointType** *(string) --*

          The type of interface endpoint.

        - **VpceId** *(string) --*

          The identifier (ID) of the VPC in which the interface endpoint is used.

    - **EmbedHostDomains** *(list) --*

      The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must
      approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

      - *(string) --* Specifies a valid domain that can embed AppStream. Valid examples
      include: ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples
      include: ["test,com", ".com", "h*llo.com". ""]
    """


_DescribeStacksPaginateResponseTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseTypeDef",
    {"Stacks": List[DescribeStacksPaginateResponseStacksTypeDef]},
    total=False,
)


class DescribeStacksPaginateResponseTypeDef(_DescribeStacksPaginateResponseTypeDef):
    """
    Type definition for `DescribeStacksPaginate` `Response`

    - **Stacks** *(list) --*

      Information about the stacks.

      - *(dict) --*

        Describes a stack.

        - **Arn** *(string) --*

          The ARN of the stack.

        - **Name** *(string) --*

          The name of the stack.

        - **Description** *(string) --*

          The description to display.

        - **DisplayName** *(string) --*

          The stack name to display.

        - **CreatedTime** *(datetime) --*

          The time the stack was created.

        - **StorageConnectors** *(list) --*

          The storage connectors to enable.

          - *(dict) --*

            Describes a connector that enables persistent storage for users.

            - **ConnectorType** *(string) --*

              The type of storage connector.

            - **ResourceIdentifier** *(string) --*

              The ARN of the storage connector.

            - **Domains** *(list) --*

              The names of the domains for the account.

              - *(string) --* GSuite domain for GDrive integration.

        - **RedirectURL** *(string) --*

          The URL that users are redirected to after their streaming session ends.

        - **FeedbackURL** *(string) --*

          The URL that users are redirected to after they click the Send Feedback link. If no URL
          is specified, no Send Feedback link is displayed.

        - **StackErrors** *(list) --*

          The errors for the stack.

          - *(dict) --*

            Describes a stack error.

            - **ErrorCode** *(string) --*

              The error code.

            - **ErrorMessage** *(string) --*

              The error message.

        - **UserSettings** *(list) --*

          The actions that are enabled or disabled for users during their streaming sessions. By
          default these actions are enabled.

          - *(dict) --*

            Describes an action and whether the action is enabled or disabled for users during
            their streaming sessions.

            - **Action** *(string) --*

              The action that is enabled or disabled.

            - **Permission** *(string) --*

              Indicates whether the action is enabled or disabled.

        - **ApplicationSettings** *(dict) --*

          The persistent application settings for users of the stack.

          - **Enabled** *(boolean) --*

            Specifies whether persistent application settings are enabled for users during their
            streaming sessions.

          - **SettingsGroup** *(string) --*

            The path prefix for the S3 bucket where users’ persistent application settings are
            stored.

          - **S3BucketName** *(string) --*

            The S3 bucket where users’ persistent application settings are stored. When persistent
            application settings are enabled for the first time for an account in an AWS Region, an
            S3 bucket is created. The bucket is unique to the AWS account and the Region.

        - **AccessEndpoints** *(list) --*

          The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack
          can connect to AppStream 2.0 only through the specified endpoints.

          - *(dict) --*

            Describes an interface VPC endpoint (interface endpoint) that lets you create a private
            connection between the virtual private cloud (VPC) that you specify and AppStream 2.0.
            When you specify an interface endpoint for a stack, users of the stack can connect to
            AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an
            image builder, administrators can connect to the image builder only through that
            endpoint.

            - **EndpointType** *(string) --*

              The type of interface endpoint.

            - **VpceId** *(string) --*

              The identifier (ID) of the VPC in which the interface endpoint is used.

        - **EmbedHostDomains** *(list) --*

          The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must
          approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

          - *(string) --* Specifies a valid domain that can embed AppStream. Valid examples
          include: ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples
          include: ["test,com", ".com", "h*llo.com". ""]
    """


_DescribeUserStackAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeUserStackAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeUserStackAssociationsPaginatePaginationConfigTypeDef(
    _DescribeUserStackAssociationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeUserStackAssociationsPaginate` `PaginationConfig`

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


_DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef = TypedDict(
    "_DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": str,
        "SendEmailNotification": bool,
    },
    total=False,
)


class DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef(
    _DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef
):
    """
    Type definition for `DescribeUserStackAssociationsPaginateResponse` `UserStackAssociations`

    Describes a user in the user pool and the associated stack.

    - **StackName** *(string) --*

      The name of the stack that is associated with the user.

    - **UserName** *(string) --*

      The email address of the user who is associated with the stack.

      .. note::

        Users' email addresses are case-sensitive.

    - **AuthenticationType** *(string) --*

      The authentication type for the user.

    - **SendEmailNotification** *(boolean) --*

      Specifies whether a welcome email is sent to a user after the user is created in the user
      pool.
    """


_DescribeUserStackAssociationsPaginateResponseTypeDef = TypedDict(
    "_DescribeUserStackAssociationsPaginateResponseTypeDef",
    {
        "UserStackAssociations": List[
            DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef
        ]
    },
    total=False,
)


class DescribeUserStackAssociationsPaginateResponseTypeDef(
    _DescribeUserStackAssociationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeUserStackAssociationsPaginate` `Response`

    - **UserStackAssociations** *(list) --*

      The UserStackAssociation objects.

      - *(dict) --*

        Describes a user in the user pool and the associated stack.

        - **StackName** *(string) --*

          The name of the stack that is associated with the user.

        - **UserName** *(string) --*

          The email address of the user who is associated with the stack.

          .. note::

            Users' email addresses are case-sensitive.

        - **AuthenticationType** *(string) --*

          The authentication type for the user.

        - **SendEmailNotification** *(boolean) --*

          Specifies whether a welcome email is sent to a user after the user is created in the user
          pool.
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


_DescribeUsersPaginateResponseUsersTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseUsersTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Enabled": bool,
        "Status": str,
        "FirstName": str,
        "LastName": str,
        "CreatedTime": datetime,
        "AuthenticationType": str,
    },
    total=False,
)


class DescribeUsersPaginateResponseUsersTypeDef(
    _DescribeUsersPaginateResponseUsersTypeDef
):
    """
    Type definition for `DescribeUsersPaginateResponse` `Users`

    Describes a user in the user pool.

    - **Arn** *(string) --*

      The ARN of the user.

    - **UserName** *(string) --*

      The email address of the user.

      .. note::

        Users' email addresses are case-sensitive.

    - **Enabled** *(boolean) --*

      Specifies whether the user in the user pool is enabled.

    - **Status** *(string) --*

      The status of the user in the user pool. The status can be one of the following:

      * UNCONFIRMED – The user is created but not confirmed.

      * CONFIRMED – The user is confirmed.

      * ARCHIVED – The user is no longer active.

      * COMPROMISED – The user is disabled because of a potential security threat.

      * UNKNOWN – The user status is not known.

    - **FirstName** *(string) --*

      The first name, or given name, of the user.

    - **LastName** *(string) --*

      The last name, or surname, of the user.

    - **CreatedTime** *(datetime) --*

      The date and time the user was created in the user pool.

    - **AuthenticationType** *(string) --*

      The authentication type for the user.
    """


_DescribeUsersPaginateResponseTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseTypeDef",
    {"Users": List[DescribeUsersPaginateResponseUsersTypeDef]},
    total=False,
)


class DescribeUsersPaginateResponseTypeDef(_DescribeUsersPaginateResponseTypeDef):
    """
    Type definition for `DescribeUsersPaginate` `Response`

    - **Users** *(list) --*

      Information about users in the user pool.

      - *(dict) --*

        Describes a user in the user pool.

        - **Arn** *(string) --*

          The ARN of the user.

        - **UserName** *(string) --*

          The email address of the user.

          .. note::

            Users' email addresses are case-sensitive.

        - **Enabled** *(boolean) --*

          Specifies whether the user in the user pool is enabled.

        - **Status** *(string) --*

          The status of the user in the user pool. The status can be one of the following:

          * UNCONFIRMED – The user is created but not confirmed.

          * CONFIRMED – The user is confirmed.

          * ARCHIVED – The user is no longer active.

          * COMPROMISED – The user is disabled because of a potential security threat.

          * UNKNOWN – The user status is not known.

        - **FirstName** *(string) --*

          The first name, or given name, of the user.

        - **LastName** *(string) --*

          The last name, or surname, of the user.

        - **CreatedTime** *(datetime) --*

          The date and time the user was created in the user pool.

        - **AuthenticationType** *(string) --*

          The authentication type for the user.
    """


_FleetStartedWaitWaiterConfigTypeDef = TypedDict(
    "_FleetStartedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class FleetStartedWaitWaiterConfigTypeDef(_FleetStartedWaitWaiterConfigTypeDef):
    """
    Type definition for `FleetStartedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_FleetStoppedWaitWaiterConfigTypeDef = TypedDict(
    "_FleetStoppedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class FleetStoppedWaitWaiterConfigTypeDef(_FleetStoppedWaitWaiterConfigTypeDef):
    """
    Type definition for `FleetStoppedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_ListAssociatedFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssociatedFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListAssociatedFleetsPaginatePaginationConfigTypeDef(
    _ListAssociatedFleetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAssociatedFleetsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListAssociatedFleetsPaginateResponseTypeDef = TypedDict(
    "_ListAssociatedFleetsPaginateResponseTypeDef", {"Names": List[str]}, total=False
)


class ListAssociatedFleetsPaginateResponseTypeDef(
    _ListAssociatedFleetsPaginateResponseTypeDef
):
    """
    Type definition for `ListAssociatedFleetsPaginate` `Response`

    - **Names** *(list) --*

      The name of the fleet.

      - *(string) --*
    """


_ListAssociatedStacksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssociatedStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListAssociatedStacksPaginatePaginationConfigTypeDef(
    _ListAssociatedStacksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAssociatedStacksPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListAssociatedStacksPaginateResponseTypeDef = TypedDict(
    "_ListAssociatedStacksPaginateResponseTypeDef", {"Names": List[str]}, total=False
)


class ListAssociatedStacksPaginateResponseTypeDef(
    _ListAssociatedStacksPaginateResponseTypeDef
):
    """
    Type definition for `ListAssociatedStacksPaginate` `Response`

    - **Names** *(list) --*

      The name of the stack.

      - *(string) --*
    """
