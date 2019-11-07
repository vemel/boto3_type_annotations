from __future__ import annotations

# builtin imports
from typing import Dict
from typing import List
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class DescribeObjects(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        pipelineId: str,
        objectIds: List[Any],
        evaluateExpressions: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPipelines(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class QueryObjects(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        pipelineId: str,
        sphere: str,
        query: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
