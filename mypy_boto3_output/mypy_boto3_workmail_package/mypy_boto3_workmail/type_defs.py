"Main interface for workmail type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateResourceResponseTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientDescribeGroupResponseTypeDef",
    "ClientDescribeOrganizationResponseTypeDef",
    "ClientDescribeResourceResponseBookingOptionsTypeDef",
    "ClientDescribeResourceResponseTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientGetMailboxDetailsResponseTypeDef",
    "ClientListAliasesResponseTypeDef",
    "ClientListGroupMembersResponseMembersTypeDef",
    "ClientListGroupMembersResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListMailboxPermissionsResponsePermissionsTypeDef",
    "ClientListMailboxPermissionsResponseTypeDef",
    "ClientListOrganizationsResponseOrganizationSummariesTypeDef",
    "ClientListOrganizationsResponseTypeDef",
    "ClientListResourceDelegatesResponseDelegatesTypeDef",
    "ClientListResourceDelegatesResponseTypeDef",
    "ClientListResourcesResponseResourcesTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientUpdateResourceBookingOptionsTypeDef",
    "ListAliasesPaginatePaginationConfigTypeDef",
    "ListAliasesPaginateResponseTypeDef",
    "ListGroupMembersPaginatePaginationConfigTypeDef",
    "ListGroupMembersPaginateResponseMembersTypeDef",
    "ListGroupMembersPaginateResponseTypeDef",
    "ListGroupsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginateResponseGroupsTypeDef",
    "ListGroupsPaginateResponseTypeDef",
    "ListMailboxPermissionsPaginatePaginationConfigTypeDef",
    "ListMailboxPermissionsPaginateResponsePermissionsTypeDef",
    "ListMailboxPermissionsPaginateResponseTypeDef",
    "ListOrganizationsPaginatePaginationConfigTypeDef",
    "ListOrganizationsPaginateResponseOrganizationSummariesTypeDef",
    "ListOrganizationsPaginateResponseTypeDef",
    "ListResourceDelegatesPaginatePaginationConfigTypeDef",
    "ListResourceDelegatesPaginateResponseDelegatesTypeDef",
    "ListResourceDelegatesPaginateResponseTypeDef",
    "ListResourcesPaginatePaginationConfigTypeDef",
    "ListResourcesPaginateResponseResourcesTypeDef",
    "ListResourcesPaginateResponseTypeDef",
    "ListUsersPaginatePaginationConfigTypeDef",
    "ListUsersPaginateResponseUsersTypeDef",
    "ListUsersPaginateResponseTypeDef",
)


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef", {"GroupId": str}, total=False
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    Type definition for `ClientCreateGroup` `Response`

    - **GroupId** *(string) --*

      The identifier of the group.
    """


_ClientCreateResourceResponseTypeDef = TypedDict(
    "_ClientCreateResourceResponseTypeDef", {"ResourceId": str}, total=False
)


class ClientCreateResourceResponseTypeDef(_ClientCreateResourceResponseTypeDef):
    """
    Type definition for `ClientCreateResource` `Response`

    - **ResourceId** *(string) --*

      The identifier of the new resource.
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef", {"UserId": str}, total=False
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    Type definition for `ClientCreateUser` `Response`

    - **UserId** *(string) --*

      The identifier for the new user.
    """


_ClientDescribeGroupResponseTypeDef = TypedDict(
    "_ClientDescribeGroupResponseTypeDef",
    {
        "GroupId": str,
        "Name": str,
        "Email": str,
        "State": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientDescribeGroupResponseTypeDef(_ClientDescribeGroupResponseTypeDef):
    """
    Type definition for `ClientDescribeGroup` `Response`

    - **GroupId** *(string) --*

      The identifier of the described group.

    - **Name** *(string) --*

      The name of the described group.

    - **Email** *(string) --*

      The email of the described group.

    - **State** *(string) --*

      The state of the user: enabled (registered to Amazon WorkMail) or disabled (deregistered or
      never registered to WorkMail).

    - **EnabledDate** *(datetime) --*

      The date and time when a user was registered to WorkMail, in UNIX epoch time format.

    - **DisabledDate** *(datetime) --*

      The date and time when a user was deregistered from WorkMail, in UNIX epoch time format.
    """


_ClientDescribeOrganizationResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
        "Alias": str,
        "State": str,
        "DirectoryId": str,
        "DirectoryType": str,
        "DefaultMailDomain": str,
        "CompletedDate": datetime,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientDescribeOrganizationResponseTypeDef(
    _ClientDescribeOrganizationResponseTypeDef
):
    """
    Type definition for `ClientDescribeOrganization` `Response`

    - **OrganizationId** *(string) --*

      The identifier of an organization.

    - **Alias** *(string) --*

      The alias for an organization.

    - **State** *(string) --*

      The state of an organization.

    - **DirectoryId** *(string) --*

      The identifier for the directory associated with an Amazon WorkMail organization.

    - **DirectoryType** *(string) --*

      The type of directory associated with the WorkMail organization.

    - **DefaultMailDomain** *(string) --*

      The default mail domain associated with the organization.

    - **CompletedDate** *(datetime) --*

      The date at which the organization became usable in the WorkMail context, in UNIX epoch time
      format.

    - **ErrorMessage** *(string) --*

      (Optional) The error message indicating if unexpected behavior was encountered with regards
      to the organization.
    """


_ClientDescribeResourceResponseBookingOptionsTypeDef = TypedDict(
    "_ClientDescribeResourceResponseBookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)


class ClientDescribeResourceResponseBookingOptionsTypeDef(
    _ClientDescribeResourceResponseBookingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeResourceResponse` `BookingOptions`

    The booking options for the described resource.

    - **AutoAcceptRequests** *(boolean) --*

      The resource's ability to automatically reply to requests. If disabled, delegates must be
      associated to the resource.

    - **AutoDeclineRecurringRequests** *(boolean) --*

      The resource's ability to automatically decline any recurring requests.

    - **AutoDeclineConflictingRequests** *(boolean) --*

      The resource's ability to automatically decline any conflicting requests.
    """


_ClientDescribeResourceResponseTypeDef = TypedDict(
    "_ClientDescribeResourceResponseTypeDef",
    {
        "ResourceId": str,
        "Email": str,
        "Name": str,
        "Type": str,
        "BookingOptions": ClientDescribeResourceResponseBookingOptionsTypeDef,
        "State": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientDescribeResourceResponseTypeDef(_ClientDescribeResourceResponseTypeDef):
    """
    Type definition for `ClientDescribeResource` `Response`

    - **ResourceId** *(string) --*

      The identifier of the described resource.

    - **Email** *(string) --*

      The email of the described resource.

    - **Name** *(string) --*

      The name of the described resource.

    - **Type** *(string) --*

      The type of the described resource.

    - **BookingOptions** *(dict) --*

      The booking options for the described resource.

      - **AutoAcceptRequests** *(boolean) --*

        The resource's ability to automatically reply to requests. If disabled, delegates must be
        associated to the resource.

      - **AutoDeclineRecurringRequests** *(boolean) --*

        The resource's ability to automatically decline any recurring requests.

      - **AutoDeclineConflictingRequests** *(boolean) --*

        The resource's ability to automatically decline any conflicting requests.

    - **State** *(string) --*

      The state of the resource: enabled (registered to Amazon WorkMail) or disabled (deregistered
      or never registered to WorkMail).

    - **EnabledDate** *(datetime) --*

      The date and time when a resource was enabled for WorkMail, in UNIX epoch time format.

    - **DisabledDate** *(datetime) --*

      The date and time when a resource was disabled from WorkMail, in UNIX epoch time format.
    """


_ClientDescribeUserResponseTypeDef = TypedDict(
    "_ClientDescribeUserResponseTypeDef",
    {
        "UserId": str,
        "Name": str,
        "Email": str,
        "DisplayName": str,
        "State": str,
        "UserRole": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientDescribeUserResponseTypeDef(_ClientDescribeUserResponseTypeDef):
    """
    Type definition for `ClientDescribeUser` `Response`

    - **UserId** *(string) --*

      The identifier for the described user.

    - **Name** *(string) --*

      The name for the user.

    - **Email** *(string) --*

      The email of the user.

    - **DisplayName** *(string) --*

      The display name of the user.

    - **State** *(string) --*

      The state of a user: enabled (registered to Amazon WorkMail) or disabled (deregistered or
      never registered to WorkMail).

    - **UserRole** *(string) --*

      In certain cases, other entities are modeled as users. If interoperability is enabled,
      resources are imported into Amazon WorkMail as users. Because different WorkMail
      organizations rely on different directory types, administrators can distinguish between an
      unregistered user (account is disabled and has a user role) and the directory administrators.
      The values are USER, RESOURCE, and SYSTEM_USER.

    - **EnabledDate** *(datetime) --*

      The date and time at which the user was enabled for Amazon WorkMail usage, in UNIX epoch time
      format.

    - **DisabledDate** *(datetime) --*

      The date and time at which the user was disabled for Amazon WorkMail usage, in UNIX epoch
      time format.
    """


_ClientGetMailboxDetailsResponseTypeDef = TypedDict(
    "_ClientGetMailboxDetailsResponseTypeDef",
    {"MailboxQuota": int, "MailboxSize": float},
    total=False,
)


class ClientGetMailboxDetailsResponseTypeDef(_ClientGetMailboxDetailsResponseTypeDef):
    """
    Type definition for `ClientGetMailboxDetails` `Response`

    - **MailboxQuota** *(integer) --*

      The maximum allowed mailbox size, in MB, for the specified user.

    - **MailboxSize** *(float) --*

      The current mailbox size, in MB, for the specified user.
    """


_ClientListAliasesResponseTypeDef = TypedDict(
    "_ClientListAliasesResponseTypeDef",
    {"Aliases": List[str], "NextToken": str},
    total=False,
)


class ClientListAliasesResponseTypeDef(_ClientListAliasesResponseTypeDef):
    """
    Type definition for `ClientListAliases` `Response`

    - **Aliases** *(list) --*

      The entity's paginated aliases.

      - *(string) --*

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results. The value is "null" when there are no
      more results to return.
    """


_ClientListGroupMembersResponseMembersTypeDef = TypedDict(
    "_ClientListGroupMembersResponseMembersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": str,
        "State": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientListGroupMembersResponseMembersTypeDef(
    _ClientListGroupMembersResponseMembersTypeDef
):
    """
    Type definition for `ClientListGroupMembersResponse` `Members`

    The representation of a user or group.

    - **Id** *(string) --*

      The identifier of the member.

    - **Name** *(string) --*

      The name of the member.

    - **Type** *(string) --*

      A member can be a user or group.

    - **State** *(string) --*

      The state of the member, which can be ENABLED, DISABLED, or DELETED.

    - **EnabledDate** *(datetime) --*

      The date indicating when the member was enabled for Amazon WorkMail use.

    - **DisabledDate** *(datetime) --*

      The date indicating when the member was disabled from Amazon WorkMail use.
    """


_ClientListGroupMembersResponseTypeDef = TypedDict(
    "_ClientListGroupMembersResponseTypeDef",
    {"Members": List[ClientListGroupMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)


class ClientListGroupMembersResponseTypeDef(_ClientListGroupMembersResponseTypeDef):
    """
    Type definition for `ClientListGroupMembers` `Response`

    - **Members** *(list) --*

      The members associated to the group.

      - *(dict) --*

        The representation of a user or group.

        - **Id** *(string) --*

          The identifier of the member.

        - **Name** *(string) --*

          The name of the member.

        - **Type** *(string) --*

          A member can be a user or group.

        - **State** *(string) --*

          The state of the member, which can be ENABLED, DISABLED, or DELETED.

        - **EnabledDate** *(datetime) --*

          The date indicating when the member was enabled for Amazon WorkMail use.

        - **DisabledDate** *(datetime) --*

          The date indicating when the member was disabled from Amazon WorkMail use.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results. The first call does not contain any
      tokens.
    """


_ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupsTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "State": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientListGroupsResponseGroupsTypeDef(_ClientListGroupsResponseGroupsTypeDef):
    """
    Type definition for `ClientListGroupsResponse` `Groups`

    The representation of an Amazon WorkMail group.

    - **Id** *(string) --*

      The identifier of the group.

    - **Email** *(string) --*

      The email of the group.

    - **Name** *(string) --*

      The name of the group.

    - **State** *(string) --*

      The state of the group, which can be ENABLED, DISABLED, or DELETED.

    - **EnabledDate** *(datetime) --*

      The date indicating when the group was enabled for Amazon WorkMail use.

    - **DisabledDate** *(datetime) --*

      The date indicating when the group was disabled from Amazon WorkMail use.
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    Type definition for `ClientListGroups` `Response`

    - **Groups** *(list) --*

      The overview of groups for an organization.

      - *(dict) --*

        The representation of an Amazon WorkMail group.

        - **Id** *(string) --*

          The identifier of the group.

        - **Email** *(string) --*

          The email of the group.

        - **Name** *(string) --*

          The name of the group.

        - **State** *(string) --*

          The state of the group, which can be ENABLED, DISABLED, or DELETED.

        - **EnabledDate** *(datetime) --*

          The date indicating when the group was enabled for Amazon WorkMail use.

        - **DisabledDate** *(datetime) --*

          The date indicating when the group was disabled from Amazon WorkMail use.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results. The value is "null" when there are no
      more results to return.
    """


_ClientListMailboxPermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientListMailboxPermissionsResponsePermissionsTypeDef",
    {"GranteeId": str, "GranteeType": str, "PermissionValues": List[str]},
    total=False,
)


class ClientListMailboxPermissionsResponsePermissionsTypeDef(
    _ClientListMailboxPermissionsResponsePermissionsTypeDef
):
    """
    Type definition for `ClientListMailboxPermissionsResponse` `Permissions`

    Permission granted to a user, group, or resource to access a certain aspect of another
    user, group, or resource mailbox.

    - **GranteeId** *(string) --*

      The identifier of the user, group, or resource to which the permissions are granted.

    - **GranteeType** *(string) --*

      The type of user, group, or resource referred to in GranteeId.

    - **PermissionValues** *(list) --*

      The permissions granted to the grantee. SEND_AS allows the grantee to send email as the
      owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF
      allows the grantee to send email on behalf of the owner of the mailbox (the grantee is
      not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee
      full access to the mailbox, irrespective of other folder-level permissions set on the
      mailbox.

      - *(string) --*
    """


_ClientListMailboxPermissionsResponseTypeDef = TypedDict(
    "_ClientListMailboxPermissionsResponseTypeDef",
    {
        "Permissions": List[ClientListMailboxPermissionsResponsePermissionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListMailboxPermissionsResponseTypeDef(
    _ClientListMailboxPermissionsResponseTypeDef
):
    """
    Type definition for `ClientListMailboxPermissions` `Response`

    - **Permissions** *(list) --*

      One page of the user, group, or resource mailbox permissions.

      - *(dict) --*

        Permission granted to a user, group, or resource to access a certain aspect of another
        user, group, or resource mailbox.

        - **GranteeId** *(string) --*

          The identifier of the user, group, or resource to which the permissions are granted.

        - **GranteeType** *(string) --*

          The type of user, group, or resource referred to in GranteeId.

        - **PermissionValues** *(list) --*

          The permissions granted to the grantee. SEND_AS allows the grantee to send email as the
          owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF
          allows the grantee to send email on behalf of the owner of the mailbox (the grantee is
          not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee
          full access to the mailbox, irrespective of other folder-level permissions set on the
          mailbox.

          - *(string) --*

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results. The value is "null" when there are no
      more results to return.
    """


_ClientListOrganizationsResponseOrganizationSummariesTypeDef = TypedDict(
    "_ClientListOrganizationsResponseOrganizationSummariesTypeDef",
    {"OrganizationId": str, "Alias": str, "ErrorMessage": str, "State": str},
    total=False,
)


class ClientListOrganizationsResponseOrganizationSummariesTypeDef(
    _ClientListOrganizationsResponseOrganizationSummariesTypeDef
):
    """
    Type definition for `ClientListOrganizationsResponse` `OrganizationSummaries`

    The representation of an organization.

    - **OrganizationId** *(string) --*

      The identifier associated with the organization.

    - **Alias** *(string) --*

      The alias associated with the organization.

    - **ErrorMessage** *(string) --*

      The error message associated with the organization. It is only present if unexpected
      behavior has occurred with regards to the organization. It provides insight or solutions
      regarding unexpected behavior.

    - **State** *(string) --*

      The state associated with the organization.
    """


_ClientListOrganizationsResponseTypeDef = TypedDict(
    "_ClientListOrganizationsResponseTypeDef",
    {
        "OrganizationSummaries": List[
            ClientListOrganizationsResponseOrganizationSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListOrganizationsResponseTypeDef(_ClientListOrganizationsResponseTypeDef):
    """
    Type definition for `ClientListOrganizations` `Response`

    - **OrganizationSummaries** *(list) --*

      The overview of owned organizations presented as a list of organization summaries.

      - *(dict) --*

        The representation of an organization.

        - **OrganizationId** *(string) --*

          The identifier associated with the organization.

        - **Alias** *(string) --*

          The alias associated with the organization.

        - **ErrorMessage** *(string) --*

          The error message associated with the organization. It is only present if unexpected
          behavior has occurred with regards to the organization. It provides insight or solutions
          regarding unexpected behavior.

        - **State** *(string) --*

          The state associated with the organization.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results. The value is "null" when there are no
      more results to return.
    """


_ClientListResourceDelegatesResponseDelegatesTypeDef = TypedDict(
    "_ClientListResourceDelegatesResponseDelegatesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ClientListResourceDelegatesResponseDelegatesTypeDef(
    _ClientListResourceDelegatesResponseDelegatesTypeDef
):
    """
    Type definition for `ClientListResourceDelegatesResponse` `Delegates`

    The name of the attribute, which is one of the values defined in the UserAttribute
    enumeration.

    - **Id** *(string) --*

      The identifier for the user or group associated as the resource's delegate.

    - **Type** *(string) --*

      The type of the delegate: user or group.
    """


_ClientListResourceDelegatesResponseTypeDef = TypedDict(
    "_ClientListResourceDelegatesResponseTypeDef",
    {
        "Delegates": List[ClientListResourceDelegatesResponseDelegatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourceDelegatesResponseTypeDef(
    _ClientListResourceDelegatesResponseTypeDef
):
    """
    Type definition for `ClientListResourceDelegates` `Response`

    - **Delegates** *(list) --*

      One page of the resource's delegates.

      - *(dict) --*

        The name of the attribute, which is one of the values defined in the UserAttribute
        enumeration.

        - **Id** *(string) --*

          The identifier for the user or group associated as the resource's delegate.

        - **Type** *(string) --*

          The type of the delegate: user or group.

    - **NextToken** *(string) --*

      The token used to paginate through the delegates associated with a resource. While results
      are still available, it has an associated value. When the last page is reached, the token is
      empty.
    """


_ClientListResourcesResponseResourcesTypeDef = TypedDict(
    "_ClientListResourcesResponseResourcesTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "Type": str,
        "State": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientListResourcesResponseResourcesTypeDef(
    _ClientListResourcesResponseResourcesTypeDef
):
    """
    Type definition for `ClientListResourcesResponse` `Resources`

    The representation of a resource.

    - **Id** *(string) --*

      The identifier of the resource.

    - **Email** *(string) --*

      The email of the resource.

    - **Name** *(string) --*

      The name of the resource.

    - **Type** *(string) --*

      The type of the resource: equipment or room.

    - **State** *(string) --*

      The state of the resource, which can be ENABLED, DISABLED, or DELETED.

    - **EnabledDate** *(datetime) --*

      The date indicating when the resource was enabled for Amazon WorkMail use.

    - **DisabledDate** *(datetime) --*

      The date indicating when the resource was disabled from Amazon WorkMail use.
    """


_ClientListResourcesResponseTypeDef = TypedDict(
    "_ClientListResourcesResponseTypeDef",
    {"Resources": List[ClientListResourcesResponseResourcesTypeDef], "NextToken": str},
    total=False,
)


class ClientListResourcesResponseTypeDef(_ClientListResourcesResponseTypeDef):
    """
    Type definition for `ClientListResources` `Response`

    - **Resources** *(list) --*

      One page of the organization's resource representation.

      - *(dict) --*

        The representation of a resource.

        - **Id** *(string) --*

          The identifier of the resource.

        - **Email** *(string) --*

          The email of the resource.

        - **Name** *(string) --*

          The name of the resource.

        - **Type** *(string) --*

          The type of the resource: equipment or room.

        - **State** *(string) --*

          The state of the resource, which can be ENABLED, DISABLED, or DELETED.

        - **EnabledDate** *(datetime) --*

          The date indicating when the resource was enabled for Amazon WorkMail use.

        - **DisabledDate** *(datetime) --*

          The date indicating when the resource was disabled from Amazon WorkMail use.

    - **NextToken** *(string) --*

      The token used to paginate through all the organization's resources. While results are still
      available, it has an associated value. When the last page is reached, the token is empty.
    """


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "DisplayName": str,
        "State": str,
        "UserRole": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    Type definition for `ClientListUsersResponse` `Users`

    The representation of an Amazon WorkMail user.

    - **Id** *(string) --*

      The identifier of the user.

    - **Email** *(string) --*

      The email of the user.

    - **Name** *(string) --*

      The name of the user.

    - **DisplayName** *(string) --*

      The display name of the user.

    - **State** *(string) --*

      The state of the user, which can be ENABLED, DISABLED, or DELETED.

    - **UserRole** *(string) --*

      The role of the user.

    - **EnabledDate** *(datetime) --*

      The date indicating when the user was enabled for Amazon WorkMail use.

    - **DisabledDate** *(datetime) --*

      The date indicating when the user was disabled from Amazon WorkMail use.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "NextToken": str},
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    Type definition for `ClientListUsers` `Response`

    - **Users** *(list) --*

      The overview of users for an organization.

      - *(dict) --*

        The representation of an Amazon WorkMail user.

        - **Id** *(string) --*

          The identifier of the user.

        - **Email** *(string) --*

          The email of the user.

        - **Name** *(string) --*

          The name of the user.

        - **DisplayName** *(string) --*

          The display name of the user.

        - **State** *(string) --*

          The state of the user, which can be ENABLED, DISABLED, or DELETED.

        - **UserRole** *(string) --*

          The role of the user.

        - **EnabledDate** *(datetime) --*

          The date indicating when the user was enabled for Amazon WorkMail use.

        - **DisabledDate** *(datetime) --*

          The date indicating when the user was disabled from Amazon WorkMail use.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results. This value is `null` when there are no
      more results to return.
    """


_ClientUpdateResourceBookingOptionsTypeDef = TypedDict(
    "_ClientUpdateResourceBookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)


class ClientUpdateResourceBookingOptionsTypeDef(
    _ClientUpdateResourceBookingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateResource` `BookingOptions`

    The resource's booking options to be updated.

    - **AutoAcceptRequests** *(boolean) --*

      The resource's ability to automatically reply to requests. If disabled, delegates must be
      associated to the resource.

    - **AutoDeclineRecurringRequests** *(boolean) --*

      The resource's ability to automatically decline any recurring requests.

    - **AutoDeclineConflictingRequests** *(boolean) --*

      The resource's ability to automatically decline any conflicting requests.
    """


_ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAliasesPaginatePaginationConfigTypeDef(
    _ListAliasesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAliasesPaginate` `PaginationConfig`

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


_ListAliasesPaginateResponseTypeDef = TypedDict(
    "_ListAliasesPaginateResponseTypeDef", {"Aliases": List[str]}, total=False
)


class ListAliasesPaginateResponseTypeDef(_ListAliasesPaginateResponseTypeDef):
    """
    Type definition for `ListAliasesPaginate` `Response`

    - **Aliases** *(list) --*

      The entity's paginated aliases.

      - *(string) --*
    """


_ListGroupMembersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupMembersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupMembersPaginatePaginationConfigTypeDef(
    _ListGroupMembersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGroupMembersPaginate` `PaginationConfig`

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


_ListGroupMembersPaginateResponseMembersTypeDef = TypedDict(
    "_ListGroupMembersPaginateResponseMembersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": str,
        "State": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ListGroupMembersPaginateResponseMembersTypeDef(
    _ListGroupMembersPaginateResponseMembersTypeDef
):
    """
    Type definition for `ListGroupMembersPaginateResponse` `Members`

    The representation of a user or group.

    - **Id** *(string) --*

      The identifier of the member.

    - **Name** *(string) --*

      The name of the member.

    - **Type** *(string) --*

      A member can be a user or group.

    - **State** *(string) --*

      The state of the member, which can be ENABLED, DISABLED, or DELETED.

    - **EnabledDate** *(datetime) --*

      The date indicating when the member was enabled for Amazon WorkMail use.

    - **DisabledDate** *(datetime) --*

      The date indicating when the member was disabled from Amazon WorkMail use.
    """


_ListGroupMembersPaginateResponseTypeDef = TypedDict(
    "_ListGroupMembersPaginateResponseTypeDef",
    {"Members": List[ListGroupMembersPaginateResponseMembersTypeDef]},
    total=False,
)


class ListGroupMembersPaginateResponseTypeDef(_ListGroupMembersPaginateResponseTypeDef):
    """
    Type definition for `ListGroupMembersPaginate` `Response`

    - **Members** *(list) --*

      The members associated to the group.

      - *(dict) --*

        The representation of a user or group.

        - **Id** *(string) --*

          The identifier of the member.

        - **Name** *(string) --*

          The name of the member.

        - **Type** *(string) --*

          A member can be a user or group.

        - **State** *(string) --*

          The state of the member, which can be ENABLED, DISABLED, or DELETED.

        - **EnabledDate** *(datetime) --*

          The date indicating when the member was enabled for Amazon WorkMail use.

        - **DisabledDate** *(datetime) --*

          The date indicating when the member was disabled from Amazon WorkMail use.
    """


_ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsPaginatePaginationConfigTypeDef(
    _ListGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGroupsPaginate` `PaginationConfig`

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


_ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupsTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "State": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ListGroupsPaginateResponseGroupsTypeDef(_ListGroupsPaginateResponseGroupsTypeDef):
    """
    Type definition for `ListGroupsPaginateResponse` `Groups`

    The representation of an Amazon WorkMail group.

    - **Id** *(string) --*

      The identifier of the group.

    - **Email** *(string) --*

      The email of the group.

    - **Name** *(string) --*

      The name of the group.

    - **State** *(string) --*

      The state of the group, which can be ENABLED, DISABLED, or DELETED.

    - **EnabledDate** *(datetime) --*

      The date indicating when the group was enabled for Amazon WorkMail use.

    - **DisabledDate** *(datetime) --*

      The date indicating when the group was disabled from Amazon WorkMail use.
    """


_ListGroupsPaginateResponseTypeDef = TypedDict(
    "_ListGroupsPaginateResponseTypeDef",
    {"Groups": List[ListGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)


class ListGroupsPaginateResponseTypeDef(_ListGroupsPaginateResponseTypeDef):
    """
    Type definition for `ListGroupsPaginate` `Response`

    - **Groups** *(list) --*

      The overview of groups for an organization.

      - *(dict) --*

        The representation of an Amazon WorkMail group.

        - **Id** *(string) --*

          The identifier of the group.

        - **Email** *(string) --*

          The email of the group.

        - **Name** *(string) --*

          The name of the group.

        - **State** *(string) --*

          The state of the group, which can be ENABLED, DISABLED, or DELETED.

        - **EnabledDate** *(datetime) --*

          The date indicating when the group was enabled for Amazon WorkMail use.

        - **DisabledDate** *(datetime) --*

          The date indicating when the group was disabled from Amazon WorkMail use.
    """


_ListMailboxPermissionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMailboxPermissionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMailboxPermissionsPaginatePaginationConfigTypeDef(
    _ListMailboxPermissionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListMailboxPermissionsPaginate` `PaginationConfig`

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


_ListMailboxPermissionsPaginateResponsePermissionsTypeDef = TypedDict(
    "_ListMailboxPermissionsPaginateResponsePermissionsTypeDef",
    {"GranteeId": str, "GranteeType": str, "PermissionValues": List[str]},
    total=False,
)


class ListMailboxPermissionsPaginateResponsePermissionsTypeDef(
    _ListMailboxPermissionsPaginateResponsePermissionsTypeDef
):
    """
    Type definition for `ListMailboxPermissionsPaginateResponse` `Permissions`

    Permission granted to a user, group, or resource to access a certain aspect of another
    user, group, or resource mailbox.

    - **GranteeId** *(string) --*

      The identifier of the user, group, or resource to which the permissions are granted.

    - **GranteeType** *(string) --*

      The type of user, group, or resource referred to in GranteeId.

    - **PermissionValues** *(list) --*

      The permissions granted to the grantee. SEND_AS allows the grantee to send email as the
      owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF
      allows the grantee to send email on behalf of the owner of the mailbox (the grantee is
      not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee
      full access to the mailbox, irrespective of other folder-level permissions set on the
      mailbox.

      - *(string) --*
    """


_ListMailboxPermissionsPaginateResponseTypeDef = TypedDict(
    "_ListMailboxPermissionsPaginateResponseTypeDef",
    {"Permissions": List[ListMailboxPermissionsPaginateResponsePermissionsTypeDef]},
    total=False,
)


class ListMailboxPermissionsPaginateResponseTypeDef(
    _ListMailboxPermissionsPaginateResponseTypeDef
):
    """
    Type definition for `ListMailboxPermissionsPaginate` `Response`

    - **Permissions** *(list) --*

      One page of the user, group, or resource mailbox permissions.

      - *(dict) --*

        Permission granted to a user, group, or resource to access a certain aspect of another
        user, group, or resource mailbox.

        - **GranteeId** *(string) --*

          The identifier of the user, group, or resource to which the permissions are granted.

        - **GranteeType** *(string) --*

          The type of user, group, or resource referred to in GranteeId.

        - **PermissionValues** *(list) --*

          The permissions granted to the grantee. SEND_AS allows the grantee to send email as the
          owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF
          allows the grantee to send email on behalf of the owner of the mailbox (the grantee is
          not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee
          full access to the mailbox, irrespective of other folder-level permissions set on the
          mailbox.

          - *(string) --*
    """


_ListOrganizationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOrganizationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOrganizationsPaginatePaginationConfigTypeDef(
    _ListOrganizationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListOrganizationsPaginate` `PaginationConfig`

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


_ListOrganizationsPaginateResponseOrganizationSummariesTypeDef = TypedDict(
    "_ListOrganizationsPaginateResponseOrganizationSummariesTypeDef",
    {"OrganizationId": str, "Alias": str, "ErrorMessage": str, "State": str},
    total=False,
)


class ListOrganizationsPaginateResponseOrganizationSummariesTypeDef(
    _ListOrganizationsPaginateResponseOrganizationSummariesTypeDef
):
    """
    Type definition for `ListOrganizationsPaginateResponse` `OrganizationSummaries`

    The representation of an organization.

    - **OrganizationId** *(string) --*

      The identifier associated with the organization.

    - **Alias** *(string) --*

      The alias associated with the organization.

    - **ErrorMessage** *(string) --*

      The error message associated with the organization. It is only present if unexpected
      behavior has occurred with regards to the organization. It provides insight or solutions
      regarding unexpected behavior.

    - **State** *(string) --*

      The state associated with the organization.
    """


_ListOrganizationsPaginateResponseTypeDef = TypedDict(
    "_ListOrganizationsPaginateResponseTypeDef",
    {
        "OrganizationSummaries": List[
            ListOrganizationsPaginateResponseOrganizationSummariesTypeDef
        ]
    },
    total=False,
)


class ListOrganizationsPaginateResponseTypeDef(
    _ListOrganizationsPaginateResponseTypeDef
):
    """
    Type definition for `ListOrganizationsPaginate` `Response`

    - **OrganizationSummaries** *(list) --*

      The overview of owned organizations presented as a list of organization summaries.

      - *(dict) --*

        The representation of an organization.

        - **OrganizationId** *(string) --*

          The identifier associated with the organization.

        - **Alias** *(string) --*

          The alias associated with the organization.

        - **ErrorMessage** *(string) --*

          The error message associated with the organization. It is only present if unexpected
          behavior has occurred with regards to the organization. It provides insight or solutions
          regarding unexpected behavior.

        - **State** *(string) --*

          The state associated with the organization.
    """


_ListResourceDelegatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceDelegatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceDelegatesPaginatePaginationConfigTypeDef(
    _ListResourceDelegatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListResourceDelegatesPaginate` `PaginationConfig`

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


_ListResourceDelegatesPaginateResponseDelegatesTypeDef = TypedDict(
    "_ListResourceDelegatesPaginateResponseDelegatesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ListResourceDelegatesPaginateResponseDelegatesTypeDef(
    _ListResourceDelegatesPaginateResponseDelegatesTypeDef
):
    """
    Type definition for `ListResourceDelegatesPaginateResponse` `Delegates`

    The name of the attribute, which is one of the values defined in the UserAttribute
    enumeration.

    - **Id** *(string) --*

      The identifier for the user or group associated as the resource's delegate.

    - **Type** *(string) --*

      The type of the delegate: user or group.
    """


_ListResourceDelegatesPaginateResponseTypeDef = TypedDict(
    "_ListResourceDelegatesPaginateResponseTypeDef",
    {"Delegates": List[ListResourceDelegatesPaginateResponseDelegatesTypeDef]},
    total=False,
)


class ListResourceDelegatesPaginateResponseTypeDef(
    _ListResourceDelegatesPaginateResponseTypeDef
):
    """
    Type definition for `ListResourceDelegatesPaginate` `Response`

    - **Delegates** *(list) --*

      One page of the resource's delegates.

      - *(dict) --*

        The name of the attribute, which is one of the values defined in the UserAttribute
        enumeration.

        - **Id** *(string) --*

          The identifier for the user or group associated as the resource's delegate.

        - **Type** *(string) --*

          The type of the delegate: user or group.
    """


_ListResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourcesPaginatePaginationConfigTypeDef(
    _ListResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListResourcesPaginate` `PaginationConfig`

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


_ListResourcesPaginateResponseResourcesTypeDef = TypedDict(
    "_ListResourcesPaginateResponseResourcesTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "Type": str,
        "State": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ListResourcesPaginateResponseResourcesTypeDef(
    _ListResourcesPaginateResponseResourcesTypeDef
):
    """
    Type definition for `ListResourcesPaginateResponse` `Resources`

    The representation of a resource.

    - **Id** *(string) --*

      The identifier of the resource.

    - **Email** *(string) --*

      The email of the resource.

    - **Name** *(string) --*

      The name of the resource.

    - **Type** *(string) --*

      The type of the resource: equipment or room.

    - **State** *(string) --*

      The state of the resource, which can be ENABLED, DISABLED, or DELETED.

    - **EnabledDate** *(datetime) --*

      The date indicating when the resource was enabled for Amazon WorkMail use.

    - **DisabledDate** *(datetime) --*

      The date indicating when the resource was disabled from Amazon WorkMail use.
    """


_ListResourcesPaginateResponseTypeDef = TypedDict(
    "_ListResourcesPaginateResponseTypeDef",
    {"Resources": List[ListResourcesPaginateResponseResourcesTypeDef]},
    total=False,
)


class ListResourcesPaginateResponseTypeDef(_ListResourcesPaginateResponseTypeDef):
    """
    Type definition for `ListResourcesPaginate` `Response`

    - **Resources** *(list) --*

      One page of the organization's resource representation.

      - *(dict) --*

        The representation of a resource.

        - **Id** *(string) --*

          The identifier of the resource.

        - **Email** *(string) --*

          The email of the resource.

        - **Name** *(string) --*

          The name of the resource.

        - **Type** *(string) --*

          The type of the resource: equipment or room.

        - **State** *(string) --*

          The state of the resource, which can be ENABLED, DISABLED, or DELETED.

        - **EnabledDate** *(datetime) --*

          The date indicating when the resource was enabled for Amazon WorkMail use.

        - **DisabledDate** *(datetime) --*

          The date indicating when the resource was disabled from Amazon WorkMail use.
    """


_ListUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsersPaginatePaginationConfigTypeDef(
    _ListUsersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUsersPaginate` `PaginationConfig`

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


_ListUsersPaginateResponseUsersTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "DisplayName": str,
        "State": str,
        "UserRole": str,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ListUsersPaginateResponseUsersTypeDef(_ListUsersPaginateResponseUsersTypeDef):
    """
    Type definition for `ListUsersPaginateResponse` `Users`

    The representation of an Amazon WorkMail user.

    - **Id** *(string) --*

      The identifier of the user.

    - **Email** *(string) --*

      The email of the user.

    - **Name** *(string) --*

      The name of the user.

    - **DisplayName** *(string) --*

      The display name of the user.

    - **State** *(string) --*

      The state of the user, which can be ENABLED, DISABLED, or DELETED.

    - **UserRole** *(string) --*

      The role of the user.

    - **EnabledDate** *(datetime) --*

      The date indicating when the user was enabled for Amazon WorkMail use.

    - **DisabledDate** *(datetime) --*

      The date indicating when the user was disabled from Amazon WorkMail use.
    """


_ListUsersPaginateResponseTypeDef = TypedDict(
    "_ListUsersPaginateResponseTypeDef",
    {"Users": List[ListUsersPaginateResponseUsersTypeDef]},
    total=False,
)


class ListUsersPaginateResponseTypeDef(_ListUsersPaginateResponseTypeDef):
    """
    Type definition for `ListUsersPaginate` `Response`

    - **Users** *(list) --*

      The overview of users for an organization.

      - *(dict) --*

        The representation of an Amazon WorkMail user.

        - **Id** *(string) --*

          The identifier of the user.

        - **Email** *(string) --*

          The email of the user.

        - **Name** *(string) --*

          The name of the user.

        - **DisplayName** *(string) --*

          The display name of the user.

        - **State** *(string) --*

          The state of the user, which can be ENABLED, DISABLED, or DELETED.

        - **UserRole** *(string) --*

          The role of the user.

        - **EnabledDate** *(datetime) --*

          The date indicating when the user was enabled for Amazon WorkMail use.

        - **DisabledDate** *(datetime) --*

          The date indicating when the user was disabled from Amazon WorkMail use.
    """
