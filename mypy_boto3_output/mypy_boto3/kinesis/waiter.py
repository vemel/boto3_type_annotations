from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.waiter import Waiter


class StreamExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class StreamNotExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
