from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class IdentityExists(Waiter):
    def wait(
        self,
        Identities: List,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

