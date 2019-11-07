from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.waiter import Waiter


class FunctionExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        FunctionName: str,
        Qualifier: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
