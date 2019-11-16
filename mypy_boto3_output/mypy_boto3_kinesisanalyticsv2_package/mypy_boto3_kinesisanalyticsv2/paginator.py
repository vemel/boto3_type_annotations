"Main interface for kinesisanalyticsv2 Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kinesisanalyticsv2.type_defs import (
    ListApplicationSnapshotsPaginatePaginationConfigTypeDef,
    ListApplicationSnapshotsPaginateResponseTypeDef,
    ListApplicationsPaginatePaginationConfigTypeDef,
    ListApplicationsPaginateResponseTypeDef,
)


__all__ = ("ListApplicationSnapshotsPaginator", "ListApplicationsPaginator")


class ListApplicationSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `list_application_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationName: str,
        PaginationConfig: ListApplicationSnapshotsPaginatePaginationConfigTypeDef = None,
    ) -> ListApplicationSnapshotsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`KinesisAnalyticsV2.Client.list_application_snapshots`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ApplicationName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**

          The name of an existing application.

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
                'SnapshotSummaries': [
                    {
                        'SnapshotName': 'string',
                        'SnapshotStatus': 'CREATING'|'READY'|'DELETING'|'FAILED',
                        'ApplicationVersionId': 123,
                        'SnapshotCreationTimestamp': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **SnapshotSummaries** *(list) --*

              A collection of objects containing information about the application snapshots.

              - *(dict) --*

                Provides details about a snapshot of application state.

                - **SnapshotName** *(string) --*

                  The identifier for the application snapshot.

                - **SnapshotStatus** *(string) --*

                  The status of the application snapshot.

                - **ApplicationVersionId** *(integer) --*

                  The current application version ID when the snapshot was created.

                - **SnapshotCreationTimestamp** *(datetime) --*

                  The timestamp of the application snapshot.

        """


class ListApplicationsPaginator(Boto3Paginator):
    """
    Paginator for `list_applications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListApplicationsPaginatePaginationConfigTypeDef = None
    ) -> ListApplicationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`KinesisAnalyticsV2.Client.list_applications`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/ListApplications>`_

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
                'ApplicationSummaries': [
                    {
                        'ApplicationName': 'string',
                        'ApplicationARN': 'string',
                        'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
                        'ApplicationVersionId': 123,
                        'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ApplicationSummaries** *(list) --*

              A list of ``ApplicationSummary`` objects.

              - *(dict) --*

                Provides application summary information, including the application Amazon Resource Name
                (ARN), name, and status.

                - **ApplicationName** *(string) --*

                  The name of the application.

                - **ApplicationARN** *(string) --*

                  The ARN of the application.

                - **ApplicationStatus** *(string) --*

                  The status of the application.

                - **ApplicationVersionId** *(integer) --*

                  Provides the current application version.

                - **RuntimeEnvironment** *(string) --*

                  The runtime environment for the application (``SQL-1.0`` or ``FLINK-1_6`` ).

        """
