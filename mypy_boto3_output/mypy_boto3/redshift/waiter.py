from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.waiter import Waiter


class ClusterAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ClusterDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ClusterRestored(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class SnapshotAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        Marker: str = None,
        OwnerAccount: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        ClusterExists: bool = None,
        SortingEntities: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
