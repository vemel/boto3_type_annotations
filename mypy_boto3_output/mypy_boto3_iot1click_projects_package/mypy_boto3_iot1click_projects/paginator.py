"Main interface for iot1click-projects Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iot1click_projects.type_defs import (
    ListPlacementsPaginatePaginationConfigTypeDef,
    ListPlacementsPaginateResponseTypeDef,
    ListProjectsPaginatePaginationConfigTypeDef,
    ListProjectsPaginateResponseTypeDef,
)


__all__ = ("ListPlacementsPaginator", "ListProjectsPaginator")


class ListPlacementsPaginator(Boto3Paginator):
    """
    Paginator for `list_placements`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        projectName: str,
        PaginationConfig: ListPlacementsPaginatePaginationConfigTypeDef = None,
    ) -> ListPlacementsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoT1ClickProjects.Client.list_placements`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/ListPlacements>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              projectName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type projectName: string
        :param projectName: **[REQUIRED]**

          The project containing the placements to be listed.

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
                'placements': [
                    {
                        'projectName': 'string',
                        'placementName': 'string',
                        'createdDate': datetime(2015, 1, 1),
                        'updatedDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **placements** *(list) --*

              An object listing the requested placements.

              - *(dict) --*

                An object providing summary information for a particular placement.

                - **projectName** *(string) --*

                  The name of the project containing the placement.

                - **placementName** *(string) --*

                  The name of the placement being summarized.

                - **createdDate** *(datetime) --*

                  The date when the placement was originally created, in UNIX epoch time format.

                - **updatedDate** *(datetime) --*

                  The date when the placement was last updated, in UNIX epoch time format. If the placement
                  was not updated, then ``createdDate`` and ``updatedDate`` are the same.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListProjectsPaginator(Boto3Paginator):
    """
    Paginator for `list_projects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListProjectsPaginatePaginationConfigTypeDef = None
    ) -> ListProjectsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoT1ClickProjects.Client.list_projects`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/ListProjects>`_

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
                'projects': [
                    {
                        'arn': 'string',
                        'projectName': 'string',
                        'createdDate': datetime(2015, 1, 1),
                        'updatedDate': datetime(2015, 1, 1),
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **projects** *(list) --*

              An object containing the list of projects.

              - *(dict) --*

                An object providing summary information for a particular project for an associated AWS
                account and region.

                - **arn** *(string) --*

                  The ARN of the project.

                - **projectName** *(string) --*

                  The name of the project being summarized.

                - **createdDate** *(datetime) --*

                  The date when the project was originally created, in UNIX epoch time format.

                - **updatedDate** *(datetime) --*

                  The date when the project was last updated, in UNIX epoch time format. If the project was
                  not updated, then ``createdDate`` and ``updatedDate`` are the same.

                - **tags** *(dict) --*

                  The tags (metadata key/value pairs) associated with the project.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """
