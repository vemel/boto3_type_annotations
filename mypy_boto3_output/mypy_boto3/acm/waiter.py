from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class CertificateValidated(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, CertificateArn: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass
