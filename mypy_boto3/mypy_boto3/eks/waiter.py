from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class ClusterActive(Waiter):
    def wait(
        self,
        name: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ClusterDeleted(Waiter):
    def wait(
        self,
        name: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

