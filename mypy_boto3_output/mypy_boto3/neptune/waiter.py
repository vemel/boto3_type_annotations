from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.waiter import Waiter


class DBInstanceAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class DBInstanceDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
