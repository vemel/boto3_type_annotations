from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class CacheClusterAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class CacheClusterDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ReplicationGroupAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ReplicationGroupDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
