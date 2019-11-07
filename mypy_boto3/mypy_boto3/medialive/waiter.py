from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class ChannelCreated(Waiter):
    def wait(
        self,
        ChannelId: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ChannelDeleted(Waiter):
    def wait(
        self,
        ChannelId: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ChannelRunning(Waiter):
    def wait(
        self,
        ChannelId: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ChannelStopped(Waiter):
    def wait(
        self,
        ChannelId: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

