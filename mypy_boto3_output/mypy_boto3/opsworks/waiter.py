from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.waiter import Waiter


class AppExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StackId: str = None,
        AppIds: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class DeploymentSuccessful(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StackId: str = None,
        AppId: str = None,
        DeploymentIds: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceOnline(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceRegistered(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceStopped(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceTerminated(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[Any] = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
