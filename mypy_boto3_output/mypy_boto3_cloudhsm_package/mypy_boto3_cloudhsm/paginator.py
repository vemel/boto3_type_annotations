"Main interface for cloudhsm Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudhsm.type_defs import (
    ListHapgsPaginatePaginationConfigTypeDef,
    ListHapgsPaginateResponseTypeDef,
    ListHsmsPaginatePaginationConfigTypeDef,
    ListHsmsPaginateResponseTypeDef,
    ListLunaClientsPaginatePaginationConfigTypeDef,
    ListLunaClientsPaginateResponseTypeDef,
)


__all__ = ("ListHapgsPaginator", "ListHsmsPaginator", "ListLunaClientsPaginator")


class ListHapgsPaginator(Boto3Paginator):
    """
    Paginator for `list_hapgs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListHapgsPaginatePaginationConfigTypeDef = None
    ) -> ListHapgsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudHSM.Client.list_hapgs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ListHapgs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
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

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'HapgList': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **HapgList** *(list) --*

              The list of high-availability partition groups.

              - *(string) --*

        """


class ListHsmsPaginator(Boto3Paginator):
    """
    Paginator for `list_hsms`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListHsmsPaginatePaginationConfigTypeDef = None
    ) -> ListHsmsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudHSM.Client.list_hsms`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ListHsms>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
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

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'HsmList': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            Contains the output of the ``ListHsms`` operation.

            - **HsmList** *(list) --*

              The list of ARNs that identify the HSMs.

              - *(string) --*

                An ARN that identifies an HSM.

        """


class ListLunaClientsPaginator(Boto3Paginator):
    """
    Paginator for `list_luna_clients`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListLunaClientsPaginatePaginationConfigTypeDef = None
    ) -> ListLunaClientsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CloudHSM.Client.list_luna_clients`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ListLunaClients>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
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

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ClientList': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ClientList** *(list) --*

              The list of clients.

              - *(string) --*

        """
