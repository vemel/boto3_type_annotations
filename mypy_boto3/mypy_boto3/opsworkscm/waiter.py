from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class NodeAssociated(Waiter):
    def wait(
        self,
        NodeAssociationStatusToken: str,
        ServerName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

