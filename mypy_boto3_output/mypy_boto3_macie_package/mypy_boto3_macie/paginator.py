"Main interface for macie Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_macie.type_defs import (
    ListMemberAccountsPaginatePaginationConfigTypeDef,
    ListMemberAccountsPaginateResponseTypeDef,
    ListS3ResourcesPaginatePaginationConfigTypeDef,
    ListS3ResourcesPaginateResponseTypeDef,
)


__all__ = ("ListMemberAccountsPaginator", "ListS3ResourcesPaginator")


class ListMemberAccountsPaginator(Boto3Paginator):
    """
    Paginator for `list_member_accounts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListMemberAccountsPaginatePaginationConfigTypeDef = None
    ) -> ListMemberAccountsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Macie.Client.list_member_accounts`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/macie-2017-12-19/ListMemberAccounts>`_

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
                'memberAccounts': [
                    {
                        'accountId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **memberAccounts** *(list) --*

              A list of the Amazon Macie member accounts returned by the action. The current master account
              is also included in this list.

              - *(dict) --*

                Contains information about the Amazon Macie member account.

                - **accountId** *(string) --*

                  The AWS account ID of the Amazon Macie member account.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListS3ResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_s3_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        memberAccountId: str = None,
        PaginationConfig: ListS3ResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListS3ResourcesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Macie.Client.list_s3_resources`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/macie-2017-12-19/ListS3Resources>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              memberAccountId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type memberAccountId: string
        :param memberAccountId:

          The Amazon Macie member account ID whose associated S3 resources you want to list.

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
                's3Resources': [
                    {
                        'bucketName': 'string',
                        'prefix': 'string',
                        'classificationType': {
                            'oneTime': 'FULL'|'NONE',
                            'continuous': 'FULL'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **s3Resources** *(list) --*

              A list of the associated S3 resources returned by the action.

              - *(dict) --*

                The S3 resources that you want to associate with Amazon Macie for monitoring and data
                classification. This data type is used as a request parameter in the AssociateS3Resources
                action and a response parameter in the ListS3Resources action.

                - **bucketName** *(string) --*

                  The name of the S3 bucket that you want to associate with Amazon Macie.

                - **prefix** *(string) --*

                  The prefix of the S3 bucket that you want to associate with Amazon Macie.

                - **classificationType** *(dict) --*

                  The classification type that you want to specify for the resource associated with Amazon
                  Macie.

                  - **oneTime** *(string) --*

                    A one-time classification of all of the existing objects in a specified S3 bucket.

                  - **continuous** *(string) --*

                    A continuous classification of the objects that are added to a specified S3 bucket.
                    Amazon Macie begins performing continuous classification after a bucket is successfully
                    associated with Amazon Macie.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """
