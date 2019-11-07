from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListFragments(Paginator):
    def paginate(
        self,
        StreamName: str,
        FragmentSelector: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

