from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class AlarmExists(Waiter):
    def wait(
        self,
        AlarmNames: Optional[List] = None,
        AlarmNamePrefix: Optional[str] = None,
        StateValue: Optional[str] = None,
        ActionPrefix: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

