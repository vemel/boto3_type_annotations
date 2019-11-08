from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListProjects(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, projectId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTeamMembers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, projectId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUserProfiles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
