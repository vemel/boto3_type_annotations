from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListAccelerators(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListEndpointGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ListenerArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListListeners(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AcceleratorArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
