from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.waiter import Waiter


class DBClusterSnapshotAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class DBClusterSnapshotDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class DBInstanceAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class DBInstanceDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class DBSnapshotAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class DBSnapshotCompleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class DBSnapshotDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
