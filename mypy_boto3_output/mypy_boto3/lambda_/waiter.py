from __future__ import annotations

from typing import Any
from typing import Dict

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
