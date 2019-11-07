from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.waiter import Waiter


class VaultExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, vaultName: str, accountId: str = None, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass


class VaultNotExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, vaultName: str, accountId: str = None, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass
