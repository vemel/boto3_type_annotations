from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class TableExists(Waiter):
    def wait(
        self,
        TableName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class TableNotExists(Waiter):
    def wait(
        self,
        TableName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

