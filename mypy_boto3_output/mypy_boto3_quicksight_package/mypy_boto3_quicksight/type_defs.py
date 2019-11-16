"Main interface for quicksight type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateGroupMembershipResponseGroupMemberTypeDef",
    "ClientCreateGroupMembershipResponseTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientDeleteGroupMembershipResponseTypeDef",
    "ClientDeleteGroupResponseTypeDef",
    "ClientDeleteUserByPrincipalIdResponseTypeDef",
    "ClientDeleteUserResponseTypeDef",
    "ClientDescribeGroupResponseGroupTypeDef",
    "ClientDescribeGroupResponseTypeDef",
    "ClientDescribeUserResponseUserTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientGetDashboardEmbedUrlResponseTypeDef",
    "ClientListGroupMembershipsResponseGroupMemberListTypeDef",
    "ClientListGroupMembershipsResponseTypeDef",
    "ClientListGroupsResponseGroupListTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListUserGroupsResponseGroupListTypeDef",
    "ClientListUserGroupsResponseTypeDef",
    "ClientListUsersResponseUserListTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientRegisterUserResponseUserTypeDef",
    "ClientRegisterUserResponseTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ClientUpdateUserResponseUserTypeDef",
    "ClientUpdateUserResponseTypeDef",
)


_ClientCreateGroupMembershipResponseGroupMemberTypeDef = TypedDict(
    "_ClientCreateGroupMembershipResponseGroupMemberTypeDef",
    {"Arn": str, "MemberName": str},
    total=False,
)


class ClientCreateGroupMembershipResponseGroupMemberTypeDef(
    _ClientCreateGroupMembershipResponseGroupMemberTypeDef
):
    """
    Type definition for `ClientCreateGroupMembershipResponse` `GroupMember`

    The group member.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the group member (user).

    - **MemberName** *(string) --*

      The name of the group member (user).
    """


_ClientCreateGroupMembershipResponseTypeDef = TypedDict(
    "_ClientCreateGroupMembershipResponseTypeDef",
    {
        "GroupMember": ClientCreateGroupMembershipResponseGroupMemberTypeDef,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientCreateGroupMembershipResponseTypeDef(
    _ClientCreateGroupMembershipResponseTypeDef
):
    """
    Type definition for `ClientCreateGroupMembership` `Response`

    - **GroupMember** *(dict) --*

      The group member.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the group member (user).

      - **MemberName** *(string) --*

        The name of the group member (user).

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "_ClientCreateGroupResponseGroupTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)


class ClientCreateGroupResponseGroupTypeDef(_ClientCreateGroupResponseGroupTypeDef):
    """
    Type definition for `ClientCreateGroupResponse` `Group`

    The name of the group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the group.

    - **GroupName** *(string) --*

      The name of the group.

    - **Description** *(string) --*

      The group description.

    - **PrincipalId** *(string) --*

      The principal ID of the group.
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    Type definition for `ClientCreateGroup` `Response`

    The response object for this operation.

    - **Group** *(dict) --*

      The name of the group.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the group.

      - **GroupName** *(string) --*

        The name of the group.

      - **Description** *(string) --*

        The group description.

      - **PrincipalId** *(string) --*

        The principal ID of the group.

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientDeleteGroupMembershipResponseTypeDef = TypedDict(
    "_ClientDeleteGroupMembershipResponseTypeDef",
    {"RequestId": str, "Status": int},
    total=False,
)


class ClientDeleteGroupMembershipResponseTypeDef(
    _ClientDeleteGroupMembershipResponseTypeDef
):
    """
    Type definition for `ClientDeleteGroupMembership` `Response`

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientDeleteGroupResponseTypeDef = TypedDict(
    "_ClientDeleteGroupResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)


class ClientDeleteGroupResponseTypeDef(_ClientDeleteGroupResponseTypeDef):
    """
    Type definition for `ClientDeleteGroup` `Response`

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientDeleteUserByPrincipalIdResponseTypeDef = TypedDict(
    "_ClientDeleteUserByPrincipalIdResponseTypeDef",
    {"RequestId": str, "Status": int},
    total=False,
)


class ClientDeleteUserByPrincipalIdResponseTypeDef(
    _ClientDeleteUserByPrincipalIdResponseTypeDef
):
    """
    Type definition for `ClientDeleteUserByPrincipalId` `Response`

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientDeleteUserResponseTypeDef = TypedDict(
    "_ClientDeleteUserResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)


class ClientDeleteUserResponseTypeDef(_ClientDeleteUserResponseTypeDef):
    """
    Type definition for `ClientDeleteUser` `Response`

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientDescribeGroupResponseGroupTypeDef = TypedDict(
    "_ClientDescribeGroupResponseGroupTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)


class ClientDescribeGroupResponseGroupTypeDef(_ClientDescribeGroupResponseGroupTypeDef):
    """
    Type definition for `ClientDescribeGroupResponse` `Group`

    The name of the group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the group.

    - **GroupName** *(string) --*

      The name of the group.

    - **Description** *(string) --*

      The group description.

    - **PrincipalId** *(string) --*

      The principal ID of the group.
    """


_ClientDescribeGroupResponseTypeDef = TypedDict(
    "_ClientDescribeGroupResponseTypeDef",
    {"Group": ClientDescribeGroupResponseGroupTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientDescribeGroupResponseTypeDef(_ClientDescribeGroupResponseTypeDef):
    """
    Type definition for `ClientDescribeGroup` `Response`

    - **Group** *(dict) --*

      The name of the group.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the group.

      - **GroupName** *(string) --*

        The name of the group.

      - **Description** *(string) --*

        The group description.

      - **PrincipalId** *(string) --*

        The principal ID of the group.

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientDescribeUserResponseUserTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": str,
        "IdentityType": str,
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)


class ClientDescribeUserResponseUserTypeDef(_ClientDescribeUserResponseUserTypeDef):
    """
    Type definition for `ClientDescribeUserResponse` `User`

    The user name.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the user.

    - **UserName** *(string) --*

      The user's user name.

    - **Email** *(string) --*

      The user's email address.

    - **Role** *(string) --*

      The Amazon QuickSight role for the user.

    - **IdentityType** *(string) --*

      The type of identity authentication used by the user.

    - **Active** *(boolean) --*

      Active status of user. When you create an Amazon QuickSight user that’s not an IAM user or
      an AD user, that user is inactive until they sign in and provide a password

    - **PrincipalId** *(string) --*

      The principal ID of the user.
    """


_ClientDescribeUserResponseTypeDef = TypedDict(
    "_ClientDescribeUserResponseTypeDef",
    {"User": ClientDescribeUserResponseUserTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientDescribeUserResponseTypeDef(_ClientDescribeUserResponseTypeDef):
    """
    Type definition for `ClientDescribeUser` `Response`

    - **User** *(dict) --*

      The user name.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the user.

      - **UserName** *(string) --*

        The user's user name.

      - **Email** *(string) --*

        The user's email address.

      - **Role** *(string) --*

        The Amazon QuickSight role for the user.

      - **IdentityType** *(string) --*

        The type of identity authentication used by the user.

      - **Active** *(boolean) --*

        Active status of user. When you create an Amazon QuickSight user that’s not an IAM user or
        an AD user, that user is inactive until they sign in and provide a password

      - **PrincipalId** *(string) --*

        The principal ID of the user.

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientGetDashboardEmbedUrlResponseTypeDef = TypedDict(
    "_ClientGetDashboardEmbedUrlResponseTypeDef",
    {"EmbedUrl": str, "Status": int, "RequestId": str},
    total=False,
)


class ClientGetDashboardEmbedUrlResponseTypeDef(
    _ClientGetDashboardEmbedUrlResponseTypeDef
):
    """
    Type definition for `ClientGetDashboardEmbedUrl` `Response`

    - **EmbedUrl** *(string) --*

      URL that you can put into your server-side webpage to embed your dashboard. This URL is valid
      for 5 minutes, and the resulting session is valid for 10 hours. The API provides the URL with
      an auth_code that enables a single-signon session.

    - **Status** *(integer) --*

      The http status of the request.

    - **RequestId** *(string) --*

      The AWS request ID for this operation.
    """


_ClientListGroupMembershipsResponseGroupMemberListTypeDef = TypedDict(
    "_ClientListGroupMembershipsResponseGroupMemberListTypeDef",
    {"Arn": str, "MemberName": str},
    total=False,
)


class ClientListGroupMembershipsResponseGroupMemberListTypeDef(
    _ClientListGroupMembershipsResponseGroupMemberListTypeDef
):
    """
    Type definition for `ClientListGroupMembershipsResponse` `GroupMemberList`

    A member of an Amazon QuickSight group. Currently, group members must be users. Groups
    can't be members of another group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the group member (user).

    - **MemberName** *(string) --*

      The name of the group member (user).
    """


_ClientListGroupMembershipsResponseTypeDef = TypedDict(
    "_ClientListGroupMembershipsResponseTypeDef",
    {
        "GroupMemberList": List[
            ClientListGroupMembershipsResponseGroupMemberListTypeDef
        ],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListGroupMembershipsResponseTypeDef(
    _ClientListGroupMembershipsResponseTypeDef
):
    """
    Type definition for `ClientListGroupMemberships` `Response`

    - **GroupMemberList** *(list) --*

      The list of the members of the group.

      - *(dict) --*

        A member of an Amazon QuickSight group. Currently, group members must be users. Groups
        can't be members of another group.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) for the group member (user).

        - **MemberName** *(string) --*

          The name of the group member (user).

    - **NextToken** *(string) --*

      A pagination token that can be used in a subsequent request.

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientListGroupsResponseGroupListTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupListTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)


class ClientListGroupsResponseGroupListTypeDef(
    _ClientListGroupsResponseGroupListTypeDef
):
    """
    Type definition for `ClientListGroupsResponse` `GroupList`

    A *group* in Amazon QuickSight consists of a set of users. You can use groups to make it
    easier to manage access and security. Currently, an Amazon QuickSight subscription can't
    contain more than 500 Amazon QuickSight groups.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the group.

    - **GroupName** *(string) --*

      The name of the group.

    - **Description** *(string) --*

      The group description.

    - **PrincipalId** *(string) --*

      The principal ID of the group.
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {
        "GroupList": List[ClientListGroupsResponseGroupListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    Type definition for `ClientListGroups` `Response`

    - **GroupList** *(list) --*

      The list of the groups.

      - *(dict) --*

        A *group* in Amazon QuickSight consists of a set of users. You can use groups to make it
        easier to manage access and security. Currently, an Amazon QuickSight subscription can't
        contain more than 500 Amazon QuickSight groups.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) for the group.

        - **GroupName** *(string) --*

          The name of the group.

        - **Description** *(string) --*

          The group description.

        - **PrincipalId** *(string) --*

          The principal ID of the group.

    - **NextToken** *(string) --*

      A pagination token that can be used in a subsequent request.

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientListUserGroupsResponseGroupListTypeDef = TypedDict(
    "_ClientListUserGroupsResponseGroupListTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)


class ClientListUserGroupsResponseGroupListTypeDef(
    _ClientListUserGroupsResponseGroupListTypeDef
):
    """
    Type definition for `ClientListUserGroupsResponse` `GroupList`

    A *group* in Amazon QuickSight consists of a set of users. You can use groups to make it
    easier to manage access and security. Currently, an Amazon QuickSight subscription can't
    contain more than 500 Amazon QuickSight groups.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the group.

    - **GroupName** *(string) --*

      The name of the group.

    - **Description** *(string) --*

      The group description.

    - **PrincipalId** *(string) --*

      The principal ID of the group.
    """


_ClientListUserGroupsResponseTypeDef = TypedDict(
    "_ClientListUserGroupsResponseTypeDef",
    {
        "GroupList": List[ClientListUserGroupsResponseGroupListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListUserGroupsResponseTypeDef(_ClientListUserGroupsResponseTypeDef):
    """
    Type definition for `ClientListUserGroups` `Response`

    - **GroupList** *(list) --*

      The list of groups the user is a member of.

      - *(dict) --*

        A *group* in Amazon QuickSight consists of a set of users. You can use groups to make it
        easier to manage access and security. Currently, an Amazon QuickSight subscription can't
        contain more than 500 Amazon QuickSight groups.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) for the group.

        - **GroupName** *(string) --*

          The name of the group.

        - **Description** *(string) --*

          The group description.

        - **PrincipalId** *(string) --*

          The principal ID of the group.

    - **NextToken** *(string) --*

      A pagination token that can be used in a subsequent request.

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The HTTP status of the request.
    """


_ClientListUsersResponseUserListTypeDef = TypedDict(
    "_ClientListUsersResponseUserListTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": str,
        "IdentityType": str,
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)


class ClientListUsersResponseUserListTypeDef(_ClientListUsersResponseUserListTypeDef):
    """
    Type definition for `ClientListUsersResponse` `UserList`

    A registered user of Amazon QuickSight. Currently, an Amazon QuickSight subscription can't
    contain more than 20 million users.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the user.

    - **UserName** *(string) --*

      The user's user name.

    - **Email** *(string) --*

      The user's email address.

    - **Role** *(string) --*

      The Amazon QuickSight role for the user.

    - **IdentityType** *(string) --*

      The type of identity authentication used by the user.

    - **Active** *(boolean) --*

      Active status of user. When you create an Amazon QuickSight user that’s not an IAM user
      or an AD user, that user is inactive until they sign in and provide a password

    - **PrincipalId** *(string) --*

      The principal ID of the user.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {
        "UserList": List[ClientListUsersResponseUserListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    Type definition for `ClientListUsers` `Response`

    - **UserList** *(list) --*

      The list of users.

      - *(dict) --*

        A registered user of Amazon QuickSight. Currently, an Amazon QuickSight subscription can't
        contain more than 20 million users.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) for the user.

        - **UserName** *(string) --*

          The user's user name.

        - **Email** *(string) --*

          The user's email address.

        - **Role** *(string) --*

          The Amazon QuickSight role for the user.

        - **IdentityType** *(string) --*

          The type of identity authentication used by the user.

        - **Active** *(boolean) --*

          Active status of user. When you create an Amazon QuickSight user that’s not an IAM user
          or an AD user, that user is inactive until they sign in and provide a password

        - **PrincipalId** *(string) --*

          The principal ID of the user.

    - **NextToken** *(string) --*

      A pagination token that can be used in a subsequent request.

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientRegisterUserResponseUserTypeDef = TypedDict(
    "_ClientRegisterUserResponseUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": str,
        "IdentityType": str,
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)


class ClientRegisterUserResponseUserTypeDef(_ClientRegisterUserResponseUserTypeDef):
    """
    Type definition for `ClientRegisterUserResponse` `User`

    The user name.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the user.

    - **UserName** *(string) --*

      The user's user name.

    - **Email** *(string) --*

      The user's email address.

    - **Role** *(string) --*

      The Amazon QuickSight role for the user.

    - **IdentityType** *(string) --*

      The type of identity authentication used by the user.

    - **Active** *(boolean) --*

      Active status of user. When you create an Amazon QuickSight user that’s not an IAM user or
      an AD user, that user is inactive until they sign in and provide a password

    - **PrincipalId** *(string) --*

      The principal ID of the user.
    """


_ClientRegisterUserResponseTypeDef = TypedDict(
    "_ClientRegisterUserResponseTypeDef",
    {
        "User": ClientRegisterUserResponseUserTypeDef,
        "UserInvitationUrl": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientRegisterUserResponseTypeDef(_ClientRegisterUserResponseTypeDef):
    """
    Type definition for `ClientRegisterUser` `Response`

    - **User** *(dict) --*

      The user name.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the user.

      - **UserName** *(string) --*

        The user's user name.

      - **Email** *(string) --*

        The user's email address.

      - **Role** *(string) --*

        The Amazon QuickSight role for the user.

      - **IdentityType** *(string) --*

        The type of identity authentication used by the user.

      - **Active** *(boolean) --*

        Active status of user. When you create an Amazon QuickSight user that’s not an IAM user or
        an AD user, that user is inactive until they sign in and provide a password

      - **PrincipalId** *(string) --*

        The principal ID of the user.

    - **UserInvitationUrl** *(string) --*

      The URL the user visits to complete registration and provide a password. This is returned
      only for users with an identity type of ``QUICKSIGHT`` .

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "_ClientUpdateGroupResponseGroupTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)


class ClientUpdateGroupResponseGroupTypeDef(_ClientUpdateGroupResponseGroupTypeDef):
    """
    Type definition for `ClientUpdateGroupResponse` `Group`

    The name of the group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the group.

    - **GroupName** *(string) --*

      The name of the group.

    - **Description** *(string) --*

      The group description.

    - **PrincipalId** *(string) --*

      The principal ID of the group.
    """


_ClientUpdateGroupResponseTypeDef = TypedDict(
    "_ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientUpdateGroupResponseTypeDef(_ClientUpdateGroupResponseTypeDef):
    """
    Type definition for `ClientUpdateGroup` `Response`

    - **Group** *(dict) --*

      The name of the group.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the group.

      - **GroupName** *(string) --*

        The name of the group.

      - **Description** *(string) --*

        The group description.

      - **PrincipalId** *(string) --*

        The principal ID of the group.

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """


_ClientUpdateUserResponseUserTypeDef = TypedDict(
    "_ClientUpdateUserResponseUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": str,
        "IdentityType": str,
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)


class ClientUpdateUserResponseUserTypeDef(_ClientUpdateUserResponseUserTypeDef):
    """
    Type definition for `ClientUpdateUserResponse` `User`

    The Amazon QuickSight user.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the user.

    - **UserName** *(string) --*

      The user's user name.

    - **Email** *(string) --*

      The user's email address.

    - **Role** *(string) --*

      The Amazon QuickSight role for the user.

    - **IdentityType** *(string) --*

      The type of identity authentication used by the user.

    - **Active** *(boolean) --*

      Active status of user. When you create an Amazon QuickSight user that’s not an IAM user or
      an AD user, that user is inactive until they sign in and provide a password

    - **PrincipalId** *(string) --*

      The principal ID of the user.
    """


_ClientUpdateUserResponseTypeDef = TypedDict(
    "_ClientUpdateUserResponseTypeDef",
    {"User": ClientUpdateUserResponseUserTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientUpdateUserResponseTypeDef(_ClientUpdateUserResponseTypeDef):
    """
    Type definition for `ClientUpdateUser` `Response`

    - **User** *(dict) --*

      The Amazon QuickSight user.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the user.

      - **UserName** *(string) --*

        The user's user name.

      - **Email** *(string) --*

        The user's email address.

      - **Role** *(string) --*

        The Amazon QuickSight role for the user.

      - **IdentityType** *(string) --*

        The type of identity authentication used by the user.

      - **Active** *(boolean) --*

        Active status of user. When you create an Amazon QuickSight user that’s not an IAM user or
        an AD user, that user is inactive until they sign in and provide a password

      - **PrincipalId** *(string) --*

        The principal ID of the user.

    - **RequestId** *(string) --*

      The AWS request ID for this operation.

    - **Status** *(integer) --*

      The http status of the request.
    """
