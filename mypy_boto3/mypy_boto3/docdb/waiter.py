from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class DBInstanceAvailable(Waiter):
    def wait(
        self,
        DBInstanceIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class DBInstanceDeleted(Waiter):
    def wait(
        self,
        DBInstanceIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

