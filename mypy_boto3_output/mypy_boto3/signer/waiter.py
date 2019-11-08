from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class SuccessfulSigningJob(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, jobId: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass
