from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class InstanceProfileExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, InstanceProfileName: str, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass


class PolicyExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, PolicyArn: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class RoleExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, RoleName: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class UserExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, UserName: str = None, WaiterConfig: Dict[str, Any] = None) -> None:
        pass
