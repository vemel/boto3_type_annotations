from __future__ import annotations

# builtin imports
from typing import Dict
from typing import List
from typing import Any

# boto3 imports
from botocore.waiter import Waiter


class FleetStarted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Names: List[Any] = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class FleetStopped(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Names: List[Any] = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
