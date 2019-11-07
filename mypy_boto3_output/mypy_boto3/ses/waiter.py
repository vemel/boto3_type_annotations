from __future__ import annotations

# builtin imports
from typing import Dict
from typing import List
from typing import Any

# boto3 imports
from botocore.waiter import Waiter


class IdentityExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, Identities: List[Any], WaiterConfig: Dict[str, Any] = None) -> None:
        pass
