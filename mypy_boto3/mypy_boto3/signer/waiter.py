from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class SuccessfulSigningJob(Waiter):
    def wait(
        self,
        jobId: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

