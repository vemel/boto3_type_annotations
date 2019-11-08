from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeTapeArchives(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, TapeARNs: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeTapeRecoveryPoints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, GatewayARN: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeTapes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        GatewayARN: str,
        TapeARNs: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVTLDevices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListFileShares(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, GatewayARN: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListGateways(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListTagsForResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceARN: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTapes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, TapeARNs: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListVolumes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, GatewayARN: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
