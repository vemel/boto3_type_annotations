from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.waiter import Waiter


class IdentityExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, Identities: List[Any], WaiterConfig: Dict[str, Any] = None) -> None:
        pass
