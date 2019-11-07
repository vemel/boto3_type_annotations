from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListAccelerators(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEndpointGroups(Paginator):
    def paginate(
        self,
        ListenerArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListListeners(Paginator):
    def paginate(
        self,
        AcceleratorArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

