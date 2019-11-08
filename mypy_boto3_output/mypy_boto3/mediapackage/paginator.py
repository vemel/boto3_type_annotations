from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListChannels(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListHarvestJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        IncludeChannelId: str = None,
        IncludeStatus: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListOriginEndpoints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ChannelId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
