"Main interface for cloud9 Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloud9.type_defs import (
    DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef,
    DescribeEnvironmentMembershipsPaginateResponseTypeDef,
    ListEnvironmentsPaginatePaginationConfigTypeDef,
    ListEnvironmentsPaginateResponseTypeDef,
)


__all__ = ("DescribeEnvironmentMembershipsPaginator", "ListEnvironmentsPaginator")


class DescribeEnvironmentMembershipsPaginator(Boto3Paginator):
    """
    Paginator for `describe_environment_memberships`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        userArn: str = None,
        environmentId: str = None,
        permissions: List[str] = None,
        PaginationConfig: DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEnvironmentMembershipsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Cloud9.Client.describe_environment_memberships`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/DescribeEnvironmentMemberships>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              userArn='string',
              environmentId='string',
              permissions=[
                  'owner'|'read-write'|'read-only',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type userArn: string
        :param userArn:

          The Amazon Resource Name (ARN) of an individual environment member to get information about. If
          no value is specified, information about all environment members are returned.

        :type environmentId: string
        :param environmentId:

          The ID of the environment to get environment member information about.

        :type permissions: list
        :param permissions:

          The type of environment member permissions to get information about. Available values include:

          * ``owner`` : Owns the environment.

          * ``read-only`` : Has read-only access to the environment.

          * ``read-write`` : Has read-write access to the environment.

          If no value is specified, information about all environment members are returned.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'memberships': [
                    {
                        'permissions': 'owner'|'read-write'|'read-only',
                        'userId': 'string',
                        'userArn': 'string',
                        'environmentId': 'string',
                        'lastAccess': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListEnvironmentsPaginator(Boto3Paginator):
    """
    Paginator for `list_environments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListEnvironmentsPaginatePaginationConfigTypeDef = None
    ) -> ListEnvironmentsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Cloud9.Client.list_environments`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/ListEnvironments>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'environmentIds': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **environmentIds** *(list) --*

              The list of environment identifiers.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """
