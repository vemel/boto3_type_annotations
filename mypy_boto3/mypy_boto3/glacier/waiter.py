from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class VaultExists(Waiter):
    def wait(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class VaultNotExists(Waiter):
    def wait(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

