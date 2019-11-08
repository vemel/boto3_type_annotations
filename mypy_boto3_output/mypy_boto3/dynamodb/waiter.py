from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class TableExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, TableName: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class TableNotExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, TableName: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass
