from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListCloudFrontOriginAccessIdentities(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListDistributions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListInvalidations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DistributionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListStreamingDistributions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
