from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class DescribeSchedule(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ChannelId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListChannels(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListInputSecurityGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListInputs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListOfferings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ChannelClass: str = None,
        ChannelConfiguration: str = None,
        Codec: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListReservations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ChannelClass: str = None,
        Codec: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
