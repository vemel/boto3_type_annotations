from datetime import datetime
from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListDeviceEvents(Paginator):
    def paginate(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDevices(Paginator):
    def paginate(
        self,
        DeviceType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

