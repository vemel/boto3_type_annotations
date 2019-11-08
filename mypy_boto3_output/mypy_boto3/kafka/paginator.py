from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListClusterOperations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ClusterArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ClusterNameFilter: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListConfigurationRevisions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Arn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListNodes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ClusterArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
