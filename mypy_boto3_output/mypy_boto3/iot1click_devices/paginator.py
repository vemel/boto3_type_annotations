from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListDeviceEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListDevices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DeviceType: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
