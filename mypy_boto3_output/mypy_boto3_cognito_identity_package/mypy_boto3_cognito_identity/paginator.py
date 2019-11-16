"Main interface for cognito-identity Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cognito_identity.type_defs import (
    ListIdentityPoolsPaginatePaginationConfigTypeDef,
    ListIdentityPoolsPaginateResponseTypeDef,
)


__all__ = ("ListIdentityPoolsPaginator",)


class ListIdentityPoolsPaginator(Boto3Paginator):
    """
    Paginator for `list_identity_pools`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListIdentityPoolsPaginatePaginationConfigTypeDef = None
    ) -> ListIdentityPoolsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CognitoIdentity.Client.list_identity_pools`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/ListIdentityPools>`_

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
                'IdentityPools': [
                    {
                        'IdentityPoolId': 'string',
                        'IdentityPoolName': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            The result of a successful ListIdentityPools action.

            - **IdentityPools** *(list) --*

              The identity pools returned by the ListIdentityPools action.

              - *(dict) --*

                A description of the identity pool.

                - **IdentityPoolId** *(string) --*

                  An identity pool ID in the format REGION:GUID.

                - **IdentityPoolName** *(string) --*

                  A string that you provide.

        """
