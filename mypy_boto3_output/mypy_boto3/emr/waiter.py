from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class ClusterRunning(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, ClusterId: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class ClusterTerminated(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, ClusterId: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class StepComplete(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, ClusterId: str, StepId: str, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass
