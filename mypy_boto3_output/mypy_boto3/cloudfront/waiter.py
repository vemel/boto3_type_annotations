from __future__ import annotations

from typing import Any
from typing import Dict

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
