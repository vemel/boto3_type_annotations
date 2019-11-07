from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeEcsClusters(Paginator):
    def paginate(
        self,
        EcsClusterArns: Optional[List] = None,
        StackId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

