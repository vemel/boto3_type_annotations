from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.waiter import Waiter


class ServicesInactive(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        services: List[Any],
        cluster: str = None,
        include: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ServicesStable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        services: List[Any],
        cluster: str = None,
        include: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class TasksRunning(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        tasks: List[Any],
        cluster: str = None,
        include: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class TasksStopped(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        tasks: List[Any],
        cluster: str = None,
        include: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
