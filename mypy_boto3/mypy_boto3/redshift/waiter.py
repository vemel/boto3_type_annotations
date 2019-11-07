from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class ClusterAvailable(Waiter):
    def wait(
        self,
        ClusterIdentifier: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ClusterDeleted(Waiter):
    def wait(
        self,
        ClusterIdentifier: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ClusterRestored(Waiter):
    def wait(
        self,
        ClusterIdentifier: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class SnapshotAvailable(Waiter):
    def wait(
        self,
        ClusterIdentifier: Optional[str] = None,
        SnapshotIdentifier: Optional[str] = None,
        SnapshotType: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        OwnerAccount: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        ClusterExists: Optional[bool] = None,
        SortingEntities: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

