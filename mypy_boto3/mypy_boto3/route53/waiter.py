from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class ResourceRecordSetsChanged(Waiter):
    def wait(
        self,
        Id: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

