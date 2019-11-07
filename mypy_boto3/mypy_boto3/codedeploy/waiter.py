from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class DeploymentSuccessful(Waiter):
    def wait(
        self,
        deploymentId: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

