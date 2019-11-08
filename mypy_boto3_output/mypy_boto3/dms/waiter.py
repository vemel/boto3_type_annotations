from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.waiter import Waiter


class EndpointDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ReplicationInstanceAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ReplicationInstanceDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ReplicationTaskDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ReplicationTaskReady(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ReplicationTaskRunning(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ReplicationTaskStopped(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class TestConnectionSucceeds(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
