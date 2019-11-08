from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.waiter import Waiter


class AlarmExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        AlarmNames: List[Any] = None,
        AlarmNamePrefix: str = None,
        StateValue: str = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
