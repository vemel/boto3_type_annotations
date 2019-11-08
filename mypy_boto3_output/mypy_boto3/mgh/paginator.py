from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListCreatedArtifacts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListDiscoveredResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListMigrationTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListProgressUpdateStreams(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
