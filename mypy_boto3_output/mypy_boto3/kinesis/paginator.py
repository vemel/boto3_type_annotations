from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class DescribeStream(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, StreamName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListShards(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StreamName: str = None,
        ExclusiveStartShardId: str = None,
        StreamCreationTimestamp: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListStreamConsumers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StreamARN: str,
        StreamCreationTimestamp: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListStreams(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
