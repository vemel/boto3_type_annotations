from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class CacheClusterAvailable(Waiter):
    def wait(
        self,
        CacheClusterId: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        ShowCacheNodeInfo: Optional[bool] = None,
        ShowCacheClustersNotInReplicationGroups: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class CacheClusterDeleted(Waiter):
    def wait(
        self,
        CacheClusterId: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        ShowCacheNodeInfo: Optional[bool] = None,
        ShowCacheClustersNotInReplicationGroups: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ReplicationGroupAvailable(Waiter):
    def wait(
        self,
        ReplicationGroupId: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ReplicationGroupDeleted(Waiter):
    def wait(
        self,
        ReplicationGroupId: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

