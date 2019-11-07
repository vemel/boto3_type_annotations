from __future__ import annotations

# builtin imports
from typing import Dict
from typing import List
from typing import Any

# boto3 imports
from botocore.waiter import Waiter


class LoadBalancerAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        LoadBalancerArns: List[Any] = None,
        Names: List[Any] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class LoadBalancerExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        LoadBalancerArns: List[Any] = None,
        Names: List[Any] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class LoadBalancersDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        LoadBalancerArns: List[Any] = None,
        Names: List[Any] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class TargetDeregistered(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        TargetGroupArn: str,
        Targets: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class TargetInService(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        TargetGroupArn: str,
        Targets: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
