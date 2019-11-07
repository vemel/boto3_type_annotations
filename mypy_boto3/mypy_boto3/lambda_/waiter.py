from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class FunctionExists(Waiter):
    def wait(
        self,
        FunctionName: str,
        Qualifier: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

