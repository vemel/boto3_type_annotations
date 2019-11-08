from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class GetFlowTemplateRevisions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, id: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetSystemTemplateRevisions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, id: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListFlowExecutionMessages(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, flowExecutionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTagsForResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, resourceArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class SearchEntities(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        entityTypes: List[Any],
        filters: List[Any] = None,
        namespaceVersion: int = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class SearchFlowExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class SearchFlowTemplates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class SearchSystemInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class SearchSystemTemplates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class SearchThings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        entityId: str,
        namespaceVersion: int = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
