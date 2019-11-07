from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class ListJobsByPipeline(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        PipelineId: str,
        Ascending: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListJobsByStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Status: str,
        Ascending: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPipelines(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Ascending: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPresets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Ascending: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
