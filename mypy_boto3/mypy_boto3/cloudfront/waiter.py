from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class DistributionDeployed(Waiter):
    def wait(
        self,
        Id: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class InvalidationCompleted(Waiter):
    def wait(
        self,
        DistributionId: str,
        Id: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class StreamingDistributionDeployed(Waiter):
    def wait(
        self,
        Id: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

