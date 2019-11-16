"Main interface for rds Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_rds.type_defs import (
    DbClusterSnapshotAvailableWaitFiltersTypeDef,
    DbClusterSnapshotAvailableWaitWaiterConfigTypeDef,
    DbClusterSnapshotDeletedWaitFiltersTypeDef,
    DbClusterSnapshotDeletedWaitWaiterConfigTypeDef,
    DbInstanceAvailableWaitFiltersTypeDef,
    DbInstanceAvailableWaitWaiterConfigTypeDef,
    DbInstanceDeletedWaitFiltersTypeDef,
    DbInstanceDeletedWaitWaiterConfigTypeDef,
    DbSnapshotAvailableWaitFiltersTypeDef,
    DbSnapshotAvailableWaitWaiterConfigTypeDef,
    DbSnapshotCompletedWaitFiltersTypeDef,
    DbSnapshotCompletedWaitWaiterConfigTypeDef,
    DbSnapshotDeletedWaitFiltersTypeDef,
    DbSnapshotDeletedWaitWaiterConfigTypeDef,
)


__all__ = (
    "DBClusterSnapshotAvailableWaiter",
    "DBClusterSnapshotDeletedWaiter",
    "DBInstanceAvailableWaiter",
    "DBInstanceDeletedWaiter",
    "DBSnapshotAvailableWaiter",
    "DBSnapshotCompletedWaiter",
    "DBSnapshotDeletedWaiter",
)


class DBClusterSnapshotAvailableWaiter(Boto3Waiter):
    """
    Waiter for `db_cluster_snapshot_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DbClusterSnapshotAvailableWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: DbClusterSnapshotAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`RDS.Client.describe_db_cluster_snapshots` every 30 seconds until a successful state
        is reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBClusterSnapshots>`_

        **Request Syntax**
        ::

          waiter.wait(
              DBClusterIdentifier='string',
              DBClusterSnapshotIdentifier='string',
              SnapshotType='string',
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
              IncludeShared=True|False,
              IncludePublic=True|False,
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier:

          The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can't
          be used in conjunction with the ``DBClusterSnapshotIdentifier`` parameter. This parameter isn't
          case-sensitive.

          Constraints:

          * If supplied, must match the identifier of an existing DBCluster.

        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier:

          A specific DB cluster snapshot identifier to describe. This parameter can't be used in
          conjunction with the ``DBClusterIdentifier`` parameter. This value is stored as a lowercase
          string.

          Constraints:

          * If supplied, must match the identifier of an existing DBClusterSnapshot.

          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be
          specified.

        :type SnapshotType: string
        :param SnapshotType:

          The type of DB cluster snapshots to be returned. You can specify one of the following values:

          * ``automated`` - Return all DB cluster snapshots that have been automatically taken by Amazon
          RDS for my AWS account.

          * ``manual`` - Return all DB cluster snapshots that have been taken by my AWS account.

          * ``shared`` - Return all manual DB cluster snapshots that have been shared to my AWS account.

          * ``public`` - Return all DB cluster snapshots that have been marked as public.

          If you don't specify a ``SnapshotType`` value, then both automated and manual DB cluster
          snapshots are returned. You can include shared DB cluster snapshots with these results by
          enabling the ``IncludeShared`` parameter. You can include public DB cluster snapshots with these
          results by enabling the ``IncludePublic`` parameter.

          The ``IncludeShared`` and ``IncludePublic`` parameters don't apply for ``SnapshotType`` values of
          ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn't apply when ``SnapshotType``
          is set to ``shared`` . The ``IncludeShared`` parameter doesn't apply when ``SnapshotType`` is set
          to ``public`` .

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB cluster snapshots to describe.

          Supported filters:

          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs).

          * ``db-cluster-snapshot-id`` - Accepts DB cluster snapshot identifiers.

          * ``snapshot-type`` - Accepts types of DB cluster snapshots.

          * ``engine`` - Accepts names of database engines.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results from a
            describe operation. Filters can be used to match a set of resources by specific criteria, such
            as IDs. The filters supported by a describe operation are documented with the describe
            operation.

            .. note::

              Currently, wildcards are not supported in filters.

            The following actions can be filtered:

            * ``DescribeDBClusterBacktracks``

            * ``DescribeDBClusterEndpoints``

            * ``DescribeDBClusters``

            * ``DescribeDBInstances``

            * ``DescribePendingMaintenanceActions``

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter. Filter names are case-sensitive.

            - **Values** *(list) --* **[REQUIRED]**

              One or more filter values. Filter values are case-sensitive.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          you can retrieve the remaining results.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous ``DescribeDBClusterSnapshots`` request. If
          this parameter is specified, the response includes only records beyond the marker, up to the
          value specified by ``MaxRecords`` .

        :type IncludeShared: boolean
        :param IncludeShared:

          A value that indicates whether to include shared manual DB cluster snapshots from other AWS
          accounts that this AWS account has been given permission to copy or restore. By default, these
          snapshots are not included.

          You can give an AWS account permission to restore a manual DB cluster snapshot from another AWS
          account by the ``ModifyDBClusterSnapshotAttribute`` API action.

        :type IncludePublic: boolean
        :param IncludePublic:

          A value that indicates whether to include manual DB cluster snapshots that are public and can be
          copied or restored by any AWS account. By default, the public snapshots are not included.

          You can share a manual DB cluster snapshot as public by using the
          ModifyDBClusterSnapshotAttribute API action.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class DBClusterSnapshotDeletedWaiter(Boto3Waiter):
    """
    Waiter for `db_cluster_snapshot_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DbClusterSnapshotDeletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: DbClusterSnapshotDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`RDS.Client.describe_db_cluster_snapshots` every 30 seconds until a successful state
        is reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBClusterSnapshots>`_

        **Request Syntax**
        ::

          waiter.wait(
              DBClusterIdentifier='string',
              DBClusterSnapshotIdentifier='string',
              SnapshotType='string',
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
              IncludeShared=True|False,
              IncludePublic=True|False,
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier:

          The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can't
          be used in conjunction with the ``DBClusterSnapshotIdentifier`` parameter. This parameter isn't
          case-sensitive.

          Constraints:

          * If supplied, must match the identifier of an existing DBCluster.

        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier:

          A specific DB cluster snapshot identifier to describe. This parameter can't be used in
          conjunction with the ``DBClusterIdentifier`` parameter. This value is stored as a lowercase
          string.

          Constraints:

          * If supplied, must match the identifier of an existing DBClusterSnapshot.

          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be
          specified.

        :type SnapshotType: string
        :param SnapshotType:

          The type of DB cluster snapshots to be returned. You can specify one of the following values:

          * ``automated`` - Return all DB cluster snapshots that have been automatically taken by Amazon
          RDS for my AWS account.

          * ``manual`` - Return all DB cluster snapshots that have been taken by my AWS account.

          * ``shared`` - Return all manual DB cluster snapshots that have been shared to my AWS account.

          * ``public`` - Return all DB cluster snapshots that have been marked as public.

          If you don't specify a ``SnapshotType`` value, then both automated and manual DB cluster
          snapshots are returned. You can include shared DB cluster snapshots with these results by
          enabling the ``IncludeShared`` parameter. You can include public DB cluster snapshots with these
          results by enabling the ``IncludePublic`` parameter.

          The ``IncludeShared`` and ``IncludePublic`` parameters don't apply for ``SnapshotType`` values of
          ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn't apply when ``SnapshotType``
          is set to ``shared`` . The ``IncludeShared`` parameter doesn't apply when ``SnapshotType`` is set
          to ``public`` .

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB cluster snapshots to describe.

          Supported filters:

          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs).

          * ``db-cluster-snapshot-id`` - Accepts DB cluster snapshot identifiers.

          * ``snapshot-type`` - Accepts types of DB cluster snapshots.

          * ``engine`` - Accepts names of database engines.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results from a
            describe operation. Filters can be used to match a set of resources by specific criteria, such
            as IDs. The filters supported by a describe operation are documented with the describe
            operation.

            .. note::

              Currently, wildcards are not supported in filters.

            The following actions can be filtered:

            * ``DescribeDBClusterBacktracks``

            * ``DescribeDBClusterEndpoints``

            * ``DescribeDBClusters``

            * ``DescribeDBInstances``

            * ``DescribePendingMaintenanceActions``

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter. Filter names are case-sensitive.

            - **Values** *(list) --* **[REQUIRED]**

              One or more filter values. Filter values are case-sensitive.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          you can retrieve the remaining results.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous ``DescribeDBClusterSnapshots`` request. If
          this parameter is specified, the response includes only records beyond the marker, up to the
          value specified by ``MaxRecords`` .

        :type IncludeShared: boolean
        :param IncludeShared:

          A value that indicates whether to include shared manual DB cluster snapshots from other AWS
          accounts that this AWS account has been given permission to copy or restore. By default, these
          snapshots are not included.

          You can give an AWS account permission to restore a manual DB cluster snapshot from another AWS
          account by the ``ModifyDBClusterSnapshotAttribute`` API action.

        :type IncludePublic: boolean
        :param IncludePublic:

          A value that indicates whether to include manual DB cluster snapshots that are public and can be
          copied or restored by any AWS account. By default, the public snapshots are not included.

          You can share a manual DB cluster snapshot as public by using the
          ModifyDBClusterSnapshotAttribute API action.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


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
        Polls :py:meth:`RDS.Client.describe_db_instances` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBInstances>`_

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

          The user-supplied instance identifier. If this parameter is specified, information from only the
          specific DB instance is returned. This parameter isn't case-sensitive.

          Constraints:

          * If supplied, must match the identifier of an existing DBInstance.

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB instances to describe.

          Supported filters:

          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs).
          The results list will only include information about the DB instances associated with the DB
          clusters identified by these ARNs.

          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance Amazon Resource Names
          (ARNs). The results list will only include information about the DB instances identified by these
          ARNs.

          * ``dbi-resource-id`` - Accepts DB instance resource identifiers. The results list will only
          include information about the DB instances identified by these DB instance resource identifiers.

          * ``domain`` - Accepts Active Directory directory IDs. The results list will only include
          information about the DB instances associated with these domains.

          * ``engine`` - Accepts engine names. The results list will only include information about the DB
          instances for these engines.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results from a
            describe operation. Filters can be used to match a set of resources by specific criteria, such
            as IDs. The filters supported by a describe operation are documented with the describe
            operation.

            .. note::

              Currently, wildcards are not supported in filters.

            The following actions can be filtered:

            * ``DescribeDBClusterBacktracks``

            * ``DescribeDBClusterEndpoints``

            * ``DescribeDBClusters``

            * ``DescribeDBInstances``

            * ``DescribePendingMaintenanceActions``

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter. Filter names are case-sensitive.

            - **Values** *(list) --* **[REQUIRED]**

              One or more filter values. Filter values are case-sensitive.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that you can retrieve the remaining results.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous ``DescribeDBInstances`` request. If this
          parameter is specified, the response includes only records beyond the marker, up to the value
          specified by ``MaxRecords`` .

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
        Polls :py:meth:`RDS.Client.describe_db_instances` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBInstances>`_

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

          The user-supplied instance identifier. If this parameter is specified, information from only the
          specific DB instance is returned. This parameter isn't case-sensitive.

          Constraints:

          * If supplied, must match the identifier of an existing DBInstance.

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB instances to describe.

          Supported filters:

          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs).
          The results list will only include information about the DB instances associated with the DB
          clusters identified by these ARNs.

          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance Amazon Resource Names
          (ARNs). The results list will only include information about the DB instances identified by these
          ARNs.

          * ``dbi-resource-id`` - Accepts DB instance resource identifiers. The results list will only
          include information about the DB instances identified by these DB instance resource identifiers.

          * ``domain`` - Accepts Active Directory directory IDs. The results list will only include
          information about the DB instances associated with these domains.

          * ``engine`` - Accepts engine names. The results list will only include information about the DB
          instances for these engines.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results from a
            describe operation. Filters can be used to match a set of resources by specific criteria, such
            as IDs. The filters supported by a describe operation are documented with the describe
            operation.

            .. note::

              Currently, wildcards are not supported in filters.

            The following actions can be filtered:

            * ``DescribeDBClusterBacktracks``

            * ``DescribeDBClusterEndpoints``

            * ``DescribeDBClusters``

            * ``DescribeDBInstances``

            * ``DescribePendingMaintenanceActions``

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter. Filter names are case-sensitive.

            - **Values** *(list) --* **[REQUIRED]**

              One or more filter values. Filter values are case-sensitive.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that you can retrieve the remaining results.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous ``DescribeDBInstances`` request. If this
          parameter is specified, the response includes only records beyond the marker, up to the value
          specified by ``MaxRecords`` .

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class DBSnapshotAvailableWaiter(Boto3Waiter):
    """
    Waiter for `db_snapshot_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DbSnapshotAvailableWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: DbSnapshotAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        .. _https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html:
        https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
        Polls :py:meth:`RDS.Client.describe_db_snapshots` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSnapshots>`_

        **Request Syntax**
        ::

          waiter.wait(
              DBInstanceIdentifier='string',
              DBSnapshotIdentifier='string',
              SnapshotType='string',
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
              IncludeShared=True|False,
              IncludePublic=True|False,
              DbiResourceId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier:

          The ID of the DB instance to retrieve the list of DB snapshots for. This parameter can't be used
          in conjunction with ``DBSnapshotIdentifier`` . This parameter isn't case-sensitive.

          Constraints:

          * If supplied, must match the identifier of an existing DBInstance.

        :type DBSnapshotIdentifier: string
        :param DBSnapshotIdentifier:

          A specific DB snapshot identifier to describe. This parameter can't be used in conjunction with
          ``DBInstanceIdentifier`` . This value is stored as a lowercase string.

          Constraints:

          * If supplied, must match the identifier of an existing DBSnapshot.

          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be
          specified.

        :type SnapshotType: string
        :param SnapshotType:

          The type of snapshots to be returned. You can specify one of the following values:

          * ``automated`` - Return all DB snapshots that have been automatically taken by Amazon RDS for my
          AWS account.

          * ``manual`` - Return all DB snapshots that have been taken by my AWS account.

          * ``shared`` - Return all manual DB snapshots that have been shared to my AWS account.

          * ``public`` - Return all DB snapshots that have been marked as public.

          * ``awsbackup`` - Return the DB snapshots managed by the AWS Backup service. For information
          about AWS Backup, see the ` *AWS Backup Developer Guide.*
          https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html`__   The ``awsbackup``
          type does not apply to Aurora.

          If you don't specify a ``SnapshotType`` value, then both automated and manual snapshots are
          returned. Shared and public DB snapshots are not included in the returned results by default. You
          can include shared snapshots with these results by enabling the ``IncludeShared`` parameter. You
          can include public snapshots with these results by enabling the ``IncludePublic`` parameter.

          The ``IncludeShared`` and ``IncludePublic`` parameters don't apply for ``SnapshotType`` values of
          ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn't apply when ``SnapshotType``
          is set to ``shared`` . The ``IncludeShared`` parameter doesn't apply when ``SnapshotType`` is set
          to ``public`` .

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB snapshots to describe.

          Supported filters:

          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance Amazon Resource Names
          (ARNs).

          * ``db-snapshot-id`` - Accepts DB snapshot identifiers.

          * ``dbi-resource-id`` - Accepts identifiers of source DB instances.

          * ``snapshot-type`` - Accepts types of DB snapshots.

          * ``engine`` - Accepts names of database engines.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results from a
            describe operation. Filters can be used to match a set of resources by specific criteria, such
            as IDs. The filters supported by a describe operation are documented with the describe
            operation.

            .. note::

              Currently, wildcards are not supported in filters.

            The following actions can be filtered:

            * ``DescribeDBClusterBacktracks``

            * ``DescribeDBClusterEndpoints``

            * ``DescribeDBClusters``

            * ``DescribeDBInstances``

            * ``DescribePendingMaintenanceActions``

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter. Filter names are case-sensitive.

            - **Values** *(list) --* **[REQUIRED]**

              One or more filter values. Filter values are case-sensitive.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that you can retrieve the remaining results.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous ``DescribeDBSnapshots`` request. If this
          parameter is specified, the response includes only records beyond the marker, up to the value
          specified by ``MaxRecords`` .

        :type IncludeShared: boolean
        :param IncludeShared:

          A value that indicates whether to include shared manual DB cluster snapshots from other AWS
          accounts that this AWS account has been given permission to copy or restore. By default, these
          snapshots are not included.

          You can give an AWS account permission to restore a manual DB snapshot from another AWS account
          by using the ``ModifyDBSnapshotAttribute`` API action.

        :type IncludePublic: boolean
        :param IncludePublic:

          A value that indicates whether to include manual DB cluster snapshots that are public and can be
          copied or restored by any AWS account. By default, the public snapshots are not included.

          You can share a manual DB snapshot as public by using the  ModifyDBSnapshotAttribute API.

        :type DbiResourceId: string
        :param DbiResourceId:

          A specific DB resource ID to describe.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class DBSnapshotCompletedWaiter(Boto3Waiter):
    """
    Waiter for `db_snapshot_completed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DbSnapshotCompletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: DbSnapshotCompletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        .. _https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html:
        https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
        Polls :py:meth:`RDS.Client.describe_db_snapshots` every 15 seconds until a successful state is
        reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSnapshots>`_

        **Request Syntax**
        ::

          waiter.wait(
              DBInstanceIdentifier='string',
              DBSnapshotIdentifier='string',
              SnapshotType='string',
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
              IncludeShared=True|False,
              IncludePublic=True|False,
              DbiResourceId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier:

          The ID of the DB instance to retrieve the list of DB snapshots for. This parameter can't be used
          in conjunction with ``DBSnapshotIdentifier`` . This parameter isn't case-sensitive.

          Constraints:

          * If supplied, must match the identifier of an existing DBInstance.

        :type DBSnapshotIdentifier: string
        :param DBSnapshotIdentifier:

          A specific DB snapshot identifier to describe. This parameter can't be used in conjunction with
          ``DBInstanceIdentifier`` . This value is stored as a lowercase string.

          Constraints:

          * If supplied, must match the identifier of an existing DBSnapshot.

          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be
          specified.

        :type SnapshotType: string
        :param SnapshotType:

          The type of snapshots to be returned. You can specify one of the following values:

          * ``automated`` - Return all DB snapshots that have been automatically taken by Amazon RDS for my
          AWS account.

          * ``manual`` - Return all DB snapshots that have been taken by my AWS account.

          * ``shared`` - Return all manual DB snapshots that have been shared to my AWS account.

          * ``public`` - Return all DB snapshots that have been marked as public.

          * ``awsbackup`` - Return the DB snapshots managed by the AWS Backup service. For information
          about AWS Backup, see the ` *AWS Backup Developer Guide.*
          https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html`__   The ``awsbackup``
          type does not apply to Aurora.

          If you don't specify a ``SnapshotType`` value, then both automated and manual snapshots are
          returned. Shared and public DB snapshots are not included in the returned results by default. You
          can include shared snapshots with these results by enabling the ``IncludeShared`` parameter. You
          can include public snapshots with these results by enabling the ``IncludePublic`` parameter.

          The ``IncludeShared`` and ``IncludePublic`` parameters don't apply for ``SnapshotType`` values of
          ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn't apply when ``SnapshotType``
          is set to ``shared`` . The ``IncludeShared`` parameter doesn't apply when ``SnapshotType`` is set
          to ``public`` .

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB snapshots to describe.

          Supported filters:

          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance Amazon Resource Names
          (ARNs).

          * ``db-snapshot-id`` - Accepts DB snapshot identifiers.

          * ``dbi-resource-id`` - Accepts identifiers of source DB instances.

          * ``snapshot-type`` - Accepts types of DB snapshots.

          * ``engine`` - Accepts names of database engines.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results from a
            describe operation. Filters can be used to match a set of resources by specific criteria, such
            as IDs. The filters supported by a describe operation are documented with the describe
            operation.

            .. note::

              Currently, wildcards are not supported in filters.

            The following actions can be filtered:

            * ``DescribeDBClusterBacktracks``

            * ``DescribeDBClusterEndpoints``

            * ``DescribeDBClusters``

            * ``DescribeDBInstances``

            * ``DescribePendingMaintenanceActions``

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter. Filter names are case-sensitive.

            - **Values** *(list) --* **[REQUIRED]**

              One or more filter values. Filter values are case-sensitive.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that you can retrieve the remaining results.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous ``DescribeDBSnapshots`` request. If this
          parameter is specified, the response includes only records beyond the marker, up to the value
          specified by ``MaxRecords`` .

        :type IncludeShared: boolean
        :param IncludeShared:

          A value that indicates whether to include shared manual DB cluster snapshots from other AWS
          accounts that this AWS account has been given permission to copy or restore. By default, these
          snapshots are not included.

          You can give an AWS account permission to restore a manual DB snapshot from another AWS account
          by using the ``ModifyDBSnapshotAttribute`` API action.

        :type IncludePublic: boolean
        :param IncludePublic:

          A value that indicates whether to include manual DB cluster snapshots that are public and can be
          copied or restored by any AWS account. By default, the public snapshots are not included.

          You can share a manual DB snapshot as public by using the  ModifyDBSnapshotAttribute API.

        :type DbiResourceId: string
        :param DbiResourceId:

          A specific DB resource ID to describe.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class DBSnapshotDeletedWaiter(Boto3Waiter):
    """
    Waiter for `db_snapshot_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DbSnapshotDeletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: DbSnapshotDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        .. _https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html:
        https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
        Polls :py:meth:`RDS.Client.describe_db_snapshots` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSnapshots>`_

        **Request Syntax**
        ::

          waiter.wait(
              DBInstanceIdentifier='string',
              DBSnapshotIdentifier='string',
              SnapshotType='string',
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
              IncludeShared=True|False,
              IncludePublic=True|False,
              DbiResourceId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier:

          The ID of the DB instance to retrieve the list of DB snapshots for. This parameter can't be used
          in conjunction with ``DBSnapshotIdentifier`` . This parameter isn't case-sensitive.

          Constraints:

          * If supplied, must match the identifier of an existing DBInstance.

        :type DBSnapshotIdentifier: string
        :param DBSnapshotIdentifier:

          A specific DB snapshot identifier to describe. This parameter can't be used in conjunction with
          ``DBInstanceIdentifier`` . This value is stored as a lowercase string.

          Constraints:

          * If supplied, must match the identifier of an existing DBSnapshot.

          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be
          specified.

        :type SnapshotType: string
        :param SnapshotType:

          The type of snapshots to be returned. You can specify one of the following values:

          * ``automated`` - Return all DB snapshots that have been automatically taken by Amazon RDS for my
          AWS account.

          * ``manual`` - Return all DB snapshots that have been taken by my AWS account.

          * ``shared`` - Return all manual DB snapshots that have been shared to my AWS account.

          * ``public`` - Return all DB snapshots that have been marked as public.

          * ``awsbackup`` - Return the DB snapshots managed by the AWS Backup service. For information
          about AWS Backup, see the ` *AWS Backup Developer Guide.*
          https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html`__   The ``awsbackup``
          type does not apply to Aurora.

          If you don't specify a ``SnapshotType`` value, then both automated and manual snapshots are
          returned. Shared and public DB snapshots are not included in the returned results by default. You
          can include shared snapshots with these results by enabling the ``IncludeShared`` parameter. You
          can include public snapshots with these results by enabling the ``IncludePublic`` parameter.

          The ``IncludeShared`` and ``IncludePublic`` parameters don't apply for ``SnapshotType`` values of
          ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn't apply when ``SnapshotType``
          is set to ``shared`` . The ``IncludeShared`` parameter doesn't apply when ``SnapshotType`` is set
          to ``public`` .

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB snapshots to describe.

          Supported filters:

          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance Amazon Resource Names
          (ARNs).

          * ``db-snapshot-id`` - Accepts DB snapshot identifiers.

          * ``dbi-resource-id`` - Accepts identifiers of source DB instances.

          * ``snapshot-type`` - Accepts types of DB snapshots.

          * ``engine`` - Accepts names of database engines.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results from a
            describe operation. Filters can be used to match a set of resources by specific criteria, such
            as IDs. The filters supported by a describe operation are documented with the describe
            operation.

            .. note::

              Currently, wildcards are not supported in filters.

            The following actions can be filtered:

            * ``DescribeDBClusterBacktracks``

            * ``DescribeDBClusterEndpoints``

            * ``DescribeDBClusters``

            * ``DescribeDBInstances``

            * ``DescribePendingMaintenanceActions``

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter. Filter names are case-sensitive.

            - **Values** *(list) --* **[REQUIRED]**

              One or more filter values. Filter values are case-sensitive.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that you can retrieve the remaining results.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous ``DescribeDBSnapshots`` request. If this
          parameter is specified, the response includes only records beyond the marker, up to the value
          specified by ``MaxRecords`` .

        :type IncludeShared: boolean
        :param IncludeShared:

          A value that indicates whether to include shared manual DB cluster snapshots from other AWS
          accounts that this AWS account has been given permission to copy or restore. By default, these
          snapshots are not included.

          You can give an AWS account permission to restore a manual DB snapshot from another AWS account
          by using the ``ModifyDBSnapshotAttribute`` API action.

        :type IncludePublic: boolean
        :param IncludePublic:

          A value that indicates whether to include manual DB cluster snapshots that are public and can be
          copied or restored by any AWS account. By default, the public snapshots are not included.

          You can share a manual DB snapshot as public by using the  ModifyDBSnapshotAttribute API.

        :type DbiResourceId: string
        :param DbiResourceId:

          A specific DB resource ID to describe.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """
