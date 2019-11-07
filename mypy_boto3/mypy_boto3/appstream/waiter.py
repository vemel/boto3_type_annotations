from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class FleetStarted(Waiter):
    def wait(
        self,
        Names: Optional[List] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class FleetStopped(Waiter):
    def wait(
        self,
        Names: Optional[List] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

