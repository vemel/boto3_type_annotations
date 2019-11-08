from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class ClusterActive(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, name: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class ClusterDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, name: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass
