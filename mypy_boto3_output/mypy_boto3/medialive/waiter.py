from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.waiter import Waiter


class ChannelCreated(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, ChannelId: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class ChannelDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, ChannelId: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class ChannelRunning(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, ChannelId: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class ChannelStopped(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, ChannelId: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass
