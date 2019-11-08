from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListBuilds(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, sortOrder: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListBuildsForProject(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        projectName: str,
        sortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListProjects(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        sortBy: str = None,
        sortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
