from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.waiter import Waiter


class DistributionDeployed(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, Id: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class InvalidationCompleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, DistributionId: str, Id: str, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass


class StreamingDistributionDeployed(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, Id: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass
