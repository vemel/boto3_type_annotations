from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class ListSigningJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        status: str = None,
        platformId: str = None,
        requestedBy: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListSigningPlatforms(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        category: str = None,
        partner: str = None,
        target: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListSigningProfiles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, includeCanceled: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
