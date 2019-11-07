from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
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
