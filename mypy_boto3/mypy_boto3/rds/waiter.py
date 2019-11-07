from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class DBClusterSnapshotAvailable(Waiter):
    def wait(
        self,
        DBClusterIdentifier: Optional[str] = None,
        DBClusterSnapshotIdentifier: Optional[str] = None,
        SnapshotType: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        IncludeShared: Optional[bool] = None,
        IncludePublic: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class DBClusterSnapshotDeleted(Waiter):
    def wait(
        self,
        DBClusterIdentifier: Optional[str] = None,
        DBClusterSnapshotIdentifier: Optional[str] = None,
        SnapshotType: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        IncludeShared: Optional[bool] = None,
        IncludePublic: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class DBInstanceAvailable(Waiter):
    def wait(
        self,
        DBInstanceIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class DBInstanceDeleted(Waiter):
    def wait(
        self,
        DBInstanceIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class DBSnapshotAvailable(Waiter):
    def wait(
        self,
        DBInstanceIdentifier: Optional[str] = None,
        DBSnapshotIdentifier: Optional[str] = None,
        SnapshotType: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        IncludeShared: Optional[bool] = None,
        IncludePublic: Optional[bool] = None,
        DbiResourceId: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class DBSnapshotCompleted(Waiter):
    def wait(
        self,
        DBInstanceIdentifier: Optional[str] = None,
        DBSnapshotIdentifier: Optional[str] = None,
        SnapshotType: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        IncludeShared: Optional[bool] = None,
        IncludePublic: Optional[bool] = None,
        DbiResourceId: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class DBSnapshotDeleted(Waiter):
    def wait(
        self,
        DBInstanceIdentifier: Optional[str] = None,
        DBSnapshotIdentifier: Optional[str] = None,
        SnapshotType: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        IncludeShared: Optional[bool] = None,
        IncludePublic: Optional[bool] = None,
        DbiResourceId: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

