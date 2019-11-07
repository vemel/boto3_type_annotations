from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class CertificateValidated(Waiter):
    def wait(
        self,
        CertificateArn: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

