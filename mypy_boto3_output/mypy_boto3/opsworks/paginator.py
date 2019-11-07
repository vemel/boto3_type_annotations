from __future__ import annotations

# builtin imports
from typing import Dict
from typing import List
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class DescribeEcsClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        EcsClusterArns: List[Any] = None,
        StackId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
