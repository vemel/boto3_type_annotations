from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListStreams(Paginator):
    def paginate(
        self,
        StreamNameCondition: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

