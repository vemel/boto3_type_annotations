from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListApplicationDependencies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ApplicationId: str,
        SemanticVersion: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListApplicationVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ApplicationId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListApplications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
