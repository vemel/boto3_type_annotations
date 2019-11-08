from __future__ import annotations

from typing import Any
from typing import Dict

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
