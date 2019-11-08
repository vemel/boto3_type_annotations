from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListActionExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        pipelineName: str,
        filter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListActionTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, actionOwnerFilter: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPipelineExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, pipelineName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPipelines(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListTagsForResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, resourceArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListWebhooks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
