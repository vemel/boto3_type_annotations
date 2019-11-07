from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class StreamExists(Waiter):
    def wait(
        self,
        StreamName: str,
        Limit: Optional[int] = None,
        ExclusiveStartShardId: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class StreamNotExists(Waiter):
    def wait(
        self,
        StreamName: str,
        Limit: Optional[int] = None,
        ExclusiveStartShardId: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

