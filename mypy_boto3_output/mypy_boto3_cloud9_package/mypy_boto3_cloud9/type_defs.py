"Main interface for cloud9 type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateEnvironmentEc2ResponseTypeDef",
    "ClientCreateEnvironmentMembershipResponsemembershipTypeDef",
    "ClientCreateEnvironmentMembershipResponseTypeDef",
    "ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef",
    "ClientDescribeEnvironmentMembershipsResponseTypeDef",
    "ClientDescribeEnvironmentStatusResponseTypeDef",
    "ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef",
    "ClientDescribeEnvironmentsResponseenvironmentsTypeDef",
    "ClientDescribeEnvironmentsResponseTypeDef",
    "ClientListEnvironmentsResponseTypeDef",
    "ClientUpdateEnvironmentMembershipResponsemembershipTypeDef",
    "ClientUpdateEnvironmentMembershipResponseTypeDef",
    "DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef",
    "DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef",
    "DescribeEnvironmentMembershipsPaginateResponseTypeDef",
    "ListEnvironmentsPaginatePaginationConfigTypeDef",
    "ListEnvironmentsPaginateResponseTypeDef",
)


_ClientCreateEnvironmentEc2ResponseTypeDef = TypedDict(
    "_ClientCreateEnvironmentEc2ResponseTypeDef", {"environmentId": str}, total=False
)


class ClientCreateEnvironmentEc2ResponseTypeDef(
    _ClientCreateEnvironmentEc2ResponseTypeDef
):
    """
    Type definition for `ClientCreateEnvironmentEc2` `Response`

    - **environmentId** *(string) --*

      The ID of the environment that was created.
    """


_ClientCreateEnvironmentMembershipResponsemembershipTypeDef = TypedDict(
    "_ClientCreateEnvironmentMembershipResponsemembershipTypeDef",
    {
        "permissions": str,
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)


class ClientCreateEnvironmentMembershipResponsemembershipTypeDef(
    _ClientCreateEnvironmentMembershipResponsemembershipTypeDef
):
    """
    Type definition for `ClientCreateEnvironmentMembershipResponse` `membership`

    Information about the environment member that was added.

    - **permissions** *(string) --*

      The type of environment member permissions associated with this environment member.
      Available values include:

      * ``owner`` : Owns the environment.

      * ``read-only`` : Has read-only access to the environment.

      * ``read-write`` : Has read-write access to the environment.

    - **userId** *(string) --*

      The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the environment member.

    - **environmentId** *(string) --*

      The ID of the environment for the environment member.

    - **lastAccess** *(datetime) --*

      The time, expressed in epoch time format, when the environment member last opened the
      environment.
    """


_ClientCreateEnvironmentMembershipResponseTypeDef = TypedDict(
    "_ClientCreateEnvironmentMembershipResponseTypeDef",
    {"membership": ClientCreateEnvironmentMembershipResponsemembershipTypeDef},
    total=False,
)


class ClientCreateEnvironmentMembershipResponseTypeDef(
    _ClientCreateEnvironmentMembershipResponseTypeDef
):
    """
    Type definition for `ClientCreateEnvironmentMembership` `Response`

    - **membership** *(dict) --*

      Information about the environment member that was added.

      - **permissions** *(string) --*

        The type of environment member permissions associated with this environment member.
        Available values include:

        * ``owner`` : Owns the environment.

        * ``read-only`` : Has read-only access to the environment.

        * ``read-write`` : Has read-write access to the environment.

      - **userId** *(string) --*

        The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the environment member.

      - **environmentId** *(string) --*

        The ID of the environment for the environment member.

      - **lastAccess** *(datetime) --*

        The time, expressed in epoch time format, when the environment member last opened the
        environment.
    """


_ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef",
    {
        "permissions": str,
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)


class ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef(
    _ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentMembershipsResponse` `memberships`

    Information about an environment member for an AWS Cloud9 development environment.

    - **permissions** *(string) --*

      The type of environment member permissions associated with this environment member.
      Available values include:

      * ``owner`` : Owns the environment.

      * ``read-only`` : Has read-only access to the environment.

      * ``read-write`` : Has read-write access to the environment.

    - **userId** *(string) --*

      The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the environment member.

    - **environmentId** *(string) --*

      The ID of the environment for the environment member.

    - **lastAccess** *(datetime) --*

      The time, expressed in epoch time format, when the environment member last opened the
      environment.
    """


_ClientDescribeEnvironmentMembershipsResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentMembershipsResponseTypeDef",
    {
        "memberships": List[
            ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeEnvironmentMembershipsResponseTypeDef(
    _ClientDescribeEnvironmentMembershipsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentMemberships` `Response`

    - **memberships** *(list) --*

      Information about the environment members for the environment.

      - *(dict) --*

        Information about an environment member for an AWS Cloud9 development environment.

        - **permissions** *(string) --*

          The type of environment member permissions associated with this environment member.
          Available values include:

          * ``owner`` : Owns the environment.

          * ``read-only`` : Has read-only access to the environment.

          * ``read-write`` : Has read-write access to the environment.

        - **userId** *(string) --*

          The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

        - **userArn** *(string) --*

          The Amazon Resource Name (ARN) of the environment member.

        - **environmentId** *(string) --*

          The ID of the environment for the environment member.

        - **lastAccess** *(datetime) --*

          The time, expressed in epoch time format, when the environment member last opened the
          environment.

    - **nextToken** *(string) --*

      If there are more than 25 items in the list, only the first 25 items are returned, along with
      a unique string called a *next token* . To get the next batch of items in the list, call this
      operation again, adding the next token to the call.
    """


_ClientDescribeEnvironmentStatusResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentStatusResponseTypeDef",
    {"status": str, "message": str},
    total=False,
)


class ClientDescribeEnvironmentStatusResponseTypeDef(
    _ClientDescribeEnvironmentStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentStatus` `Response`

    - **status** *(string) --*

      The status of the environment. Available values include:

      * ``connecting`` : The environment is connecting.

      * ``creating`` : The environment is being created.

      * ``deleting`` : The environment is being deleted.

      * ``error`` : The environment is in an error state.

      * ``ready`` : The environment is ready.

      * ``stopped`` : The environment is stopped.

      * ``stopping`` : The environment is stopping.

    - **message** *(string) --*

      Any informational message about the status of the environment.
    """


_ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef",
    {"status": str, "reason": str, "failureResource": str},
    total=False,
)


class ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef(
    _ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentsResponseenvironments` `lifecycle`

    The state of the environment in its creation or deletion lifecycle.

    - **status** *(string) --*

      The current creation or deletion lifecycle state of the environment.

      * ``CREATING`` : The environment is in the process of being created.

      * ``CREATED`` : The environment was successfully created.

      * ``CREATE_FAILED`` : The environment failed to be created.

      * ``DELETING`` : The environment is in the process of being deleted.

      * ``DELETE_FAILED`` : The environment failed to delete.

    - **reason** *(string) --*

      Any informational message about the lifecycle state of the environment.

    - **failureResource** *(string) --*

      If the environment failed to delete, the Amazon Resource Name (ARN) of the related AWS
      resource.
    """


_ClientDescribeEnvironmentsResponseenvironmentsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseenvironmentsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "type": str,
        "arn": str,
        "ownerArn": str,
        "lifecycle": ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef,
    },
    total=False,
)


class ClientDescribeEnvironmentsResponseenvironmentsTypeDef(
    _ClientDescribeEnvironmentsResponseenvironmentsTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentsResponse` `environments`

    Information about an AWS Cloud9 development environment.

    - **id** *(string) --*

      The ID of the environment.

    - **name** *(string) --*

      The name of the environment.

    - **description** *(string) --*

      The description for the environment.

    - **type** *(string) --*

      The type of environment. Valid values include the following:

      * ``ec2`` : An Amazon Elastic Compute Cloud (Amazon EC2) instance connects to the
      environment.

      * ``ssh`` : Your own server connects to the environment.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the environment.

    - **ownerArn** *(string) --*

      The Amazon Resource Name (ARN) of the environment owner.

    - **lifecycle** *(dict) --*

      The state of the environment in its creation or deletion lifecycle.

      - **status** *(string) --*

        The current creation or deletion lifecycle state of the environment.

        * ``CREATING`` : The environment is in the process of being created.

        * ``CREATED`` : The environment was successfully created.

        * ``CREATE_FAILED`` : The environment failed to be created.

        * ``DELETING`` : The environment is in the process of being deleted.

        * ``DELETE_FAILED`` : The environment failed to delete.

      - **reason** *(string) --*

        Any informational message about the lifecycle state of the environment.

      - **failureResource** *(string) --*

        If the environment failed to delete, the Amazon Resource Name (ARN) of the related AWS
        resource.
    """


_ClientDescribeEnvironmentsResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseTypeDef",
    {"environments": List[ClientDescribeEnvironmentsResponseenvironmentsTypeDef]},
    total=False,
)


class ClientDescribeEnvironmentsResponseTypeDef(
    _ClientDescribeEnvironmentsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEnvironments` `Response`

    - **environments** *(list) --*

      Information about the environments that are returned.

      - *(dict) --*

        Information about an AWS Cloud9 development environment.

        - **id** *(string) --*

          The ID of the environment.

        - **name** *(string) --*

          The name of the environment.

        - **description** *(string) --*

          The description for the environment.

        - **type** *(string) --*

          The type of environment. Valid values include the following:

          * ``ec2`` : An Amazon Elastic Compute Cloud (Amazon EC2) instance connects to the
          environment.

          * ``ssh`` : Your own server connects to the environment.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the environment.

        - **ownerArn** *(string) --*

          The Amazon Resource Name (ARN) of the environment owner.

        - **lifecycle** *(dict) --*

          The state of the environment in its creation or deletion lifecycle.

          - **status** *(string) --*

            The current creation or deletion lifecycle state of the environment.

            * ``CREATING`` : The environment is in the process of being created.

            * ``CREATED`` : The environment was successfully created.

            * ``CREATE_FAILED`` : The environment failed to be created.

            * ``DELETING`` : The environment is in the process of being deleted.

            * ``DELETE_FAILED`` : The environment failed to delete.

          - **reason** *(string) --*

            Any informational message about the lifecycle state of the environment.

          - **failureResource** *(string) --*

            If the environment failed to delete, the Amazon Resource Name (ARN) of the related AWS
            resource.
    """


_ClientListEnvironmentsResponseTypeDef = TypedDict(
    "_ClientListEnvironmentsResponseTypeDef",
    {"nextToken": str, "environmentIds": List[str]},
    total=False,
)


class ClientListEnvironmentsResponseTypeDef(_ClientListEnvironmentsResponseTypeDef):
    """
    Type definition for `ClientListEnvironments` `Response`

    - **nextToken** *(string) --*

      If there are more than 25 items in the list, only the first 25 items are returned, along with
      a unique string called a *next token* . To get the next batch of items in the list, call this
      operation again, adding the next token to the call.

    - **environmentIds** *(list) --*

      The list of environment identifiers.

      - *(string) --*
    """


_ClientUpdateEnvironmentMembershipResponsemembershipTypeDef = TypedDict(
    "_ClientUpdateEnvironmentMembershipResponsemembershipTypeDef",
    {
        "permissions": str,
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)


class ClientUpdateEnvironmentMembershipResponsemembershipTypeDef(
    _ClientUpdateEnvironmentMembershipResponsemembershipTypeDef
):
    """
    Type definition for `ClientUpdateEnvironmentMembershipResponse` `membership`

    Information about the environment member whose settings were changed.

    - **permissions** *(string) --*

      The type of environment member permissions associated with this environment member.
      Available values include:

      * ``owner`` : Owns the environment.

      * ``read-only`` : Has read-only access to the environment.

      * ``read-write`` : Has read-write access to the environment.

    - **userId** *(string) --*

      The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the environment member.

    - **environmentId** *(string) --*

      The ID of the environment for the environment member.

    - **lastAccess** *(datetime) --*

      The time, expressed in epoch time format, when the environment member last opened the
      environment.
    """


_ClientUpdateEnvironmentMembershipResponseTypeDef = TypedDict(
    "_ClientUpdateEnvironmentMembershipResponseTypeDef",
    {"membership": ClientUpdateEnvironmentMembershipResponsemembershipTypeDef},
    total=False,
)


class ClientUpdateEnvironmentMembershipResponseTypeDef(
    _ClientUpdateEnvironmentMembershipResponseTypeDef
):
    """
    Type definition for `ClientUpdateEnvironmentMembership` `Response`

    - **membership** *(dict) --*

      Information about the environment member whose settings were changed.

      - **permissions** *(string) --*

        The type of environment member permissions associated with this environment member.
        Available values include:

        * ``owner`` : Owns the environment.

        * ``read-only`` : Has read-only access to the environment.

        * ``read-write`` : Has read-write access to the environment.

      - **userId** *(string) --*

        The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the environment member.

      - **environmentId** *(string) --*

        The ID of the environment for the environment member.

      - **lastAccess** *(datetime) --*

        The time, expressed in epoch time format, when the environment member last opened the
        environment.
    """


_DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef(
    _DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEnvironmentMembershipsPaginate` `PaginationConfig`

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


_DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef = TypedDict(
    "_DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef",
    {
        "permissions": str,
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)


class DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef(
    _DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef
):
    """
    Type definition for `DescribeEnvironmentMembershipsPaginateResponse` `memberships`

    Information about an environment member for an AWS Cloud9 development environment.

    - **permissions** *(string) --*

      The type of environment member permissions associated with this environment member.
      Available values include:

      * ``owner`` : Owns the environment.

      * ``read-only`` : Has read-only access to the environment.

      * ``read-write`` : Has read-write access to the environment.

    - **userId** *(string) --*

      The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the environment member.

    - **environmentId** *(string) --*

      The ID of the environment for the environment member.

    - **lastAccess** *(datetime) --*

      The time, expressed in epoch time format, when the environment member last opened the
      environment.
    """


_DescribeEnvironmentMembershipsPaginateResponseTypeDef = TypedDict(
    "_DescribeEnvironmentMembershipsPaginateResponseTypeDef",
    {
        "memberships": List[
            DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeEnvironmentMembershipsPaginateResponseTypeDef(
    _DescribeEnvironmentMembershipsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEnvironmentMembershipsPaginate` `Response`

    - **memberships** *(list) --*

      Information about the environment members for the environment.

      - *(dict) --*

        Information about an environment member for an AWS Cloud9 development environment.

        - **permissions** *(string) --*

          The type of environment member permissions associated with this environment member.
          Available values include:

          * ``owner`` : Owns the environment.

          * ``read-only`` : Has read-only access to the environment.

          * ``read-write`` : Has read-write access to the environment.

        - **userId** *(string) --*

          The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

        - **userArn** *(string) --*

          The Amazon Resource Name (ARN) of the environment member.

        - **environmentId** *(string) --*

          The ID of the environment for the environment member.

        - **lastAccess** *(datetime) --*

          The time, expressed in epoch time format, when the environment member last opened the
          environment.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListEnvironmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEnvironmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEnvironmentsPaginatePaginationConfigTypeDef(
    _ListEnvironmentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEnvironmentsPaginate` `PaginationConfig`

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


_ListEnvironmentsPaginateResponseTypeDef = TypedDict(
    "_ListEnvironmentsPaginateResponseTypeDef",
    {"environmentIds": List[str], "NextToken": str},
    total=False,
)


class ListEnvironmentsPaginateResponseTypeDef(_ListEnvironmentsPaginateResponseTypeDef):
    """
    Type definition for `ListEnvironmentsPaginate` `Response`

    - **environmentIds** *(list) --*

      The list of environment identifiers.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
