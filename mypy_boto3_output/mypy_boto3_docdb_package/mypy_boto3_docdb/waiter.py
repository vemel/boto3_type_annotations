"Main interface for docdb Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_docdb.type_defs import (
    DbInstanceAvailableWaitFiltersTypeDef,
    DbInstanceAvailableWaitWaiterConfigTypeDef,
    DbInstanceDeletedWaitFiltersTypeDef,
    DbInstanceDeletedWaitWaiterConfigTypeDef,
)


__all__ = ("DBInstanceAvailableWaiter", "DBInstanceDeletedWaiter")


class DBInstanceAvailableWaiter(Boto3Waiter):
    """
    Waiter for `db_instance_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[DbInstanceAvailableWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: DbInstanceAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`DocDB.Client.describe_db_instances` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBInstances>`_

        **Request Syntax**
        ::

          waiter.wait(
              DBInstanceIdentifier='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier:

          The user-provided instance identifier. If this parameter is specified, information from only the
          specific DB instance is returned. This parameter isn't case sensitive.

          Constraints:

          * If provided, must match the identifier of an existing ``DBInstance`` .

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB instances to describe.

          Supported filters:

          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs).
          The results list includes only the information about the DB instances that are associated with
          the DB clusters that are identified by these ARNs.

          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance ARNs. The results list
          includes only the information about the DB instances that are identified by these ARNs.

          - *(dict) --*

            A named set of filter values, used to return a more specific list of results. You can use a
            filter to match a set of resources by specific criteria, such as IDs.

            Wildcards are not supported in filters.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter. Filter names are case sensitive.

            - **Values** *(list) --* **[REQUIRED]**

              One or more filter values. Filter values are case sensitive.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that
          the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class DBInstanceDeletedWaiter(Boto3Waiter):
    """
    Waiter for `db_instance_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[DbInstanceDeletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: DbInstanceDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`DocDB.Client.describe_db_instances` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBInstances>`_

        **Request Syntax**
        ::

          waiter.wait(
              DBInstanceIdentifier='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier:

          The user-provided instance identifier. If this parameter is specified, information from only the
          specific DB instance is returned. This parameter isn't case sensitive.

          Constraints:

          * If provided, must match the identifier of an existing ``DBInstance`` .

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB instances to describe.

          Supported filters:

          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs).
          The results list includes only the information about the DB instances that are associated with
          the DB clusters that are identified by these ARNs.

          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance ARNs. The results list
          includes only the information about the DB instances that are identified by these ARNs.

          - *(dict) --*

            A named set of filter values, used to return a more specific list of results. You can use a
            filter to match a set of resources by specific criteria, such as IDs.

            Wildcards are not supported in filters.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter. Filter names are case sensitive.

            - **Values** *(list) --* **[REQUIRED]**

              One or more filter values. Filter values are case sensitive.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that
          the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """
