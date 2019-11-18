"Main interface for eks Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_eks.type_defs import (
    ListClustersPaginatePaginationConfigTypeDef,
    ListClustersPaginateResponseTypeDef,
    ListNodegroupsPaginatePaginationConfigTypeDef,
    ListNodegroupsPaginateResponseTypeDef,
    ListUpdatesPaginatePaginationConfigTypeDef,
    ListUpdatesPaginateResponseTypeDef,
)


__all__ = ("ListClustersPaginator", "ListNodegroupsPaginator", "ListUpdatesPaginator")


class ListClustersPaginator(Boto3Paginator):
    """
    Paginator for `list_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListClustersPaginatePaginationConfigTypeDef = None
    ) -> ListClustersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EKS.Client.list_clusters`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListClusters>`_

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
                'clusters': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **clusters** *(list) --*

              A list of all of the clusters for your account in the specified Region.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListNodegroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_nodegroups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        clusterName: str,
        PaginationConfig: ListNodegroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListNodegroupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EKS.Client.list_nodegroups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListNodegroups>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              clusterName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type clusterName: string
        :param clusterName: **[REQUIRED]**

          The name of the Amazon EKS cluster that you would like to list node groups in.

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
                'nodegroups': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **nodegroups** *(list) --*

              A list of all of the node groups associated with the specified cluster.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListUpdatesPaginator(Boto3Paginator):
    """
    Paginator for `list_updates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        name: str,
        nodegroupName: str = None,
        PaginationConfig: ListUpdatesPaginatePaginationConfigTypeDef = None,
    ) -> ListUpdatesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EKS.Client.list_updates`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListUpdates>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              name='string',
              nodegroupName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the Amazon EKS cluster to list updates for.

        :type nodegroupName: string
        :param nodegroupName:

          The name of the Amazon EKS managed node group to list updates for.

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
                'updateIds': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **updateIds** *(list) --*

              A list of all the updates for the specified cluster and Region.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """
