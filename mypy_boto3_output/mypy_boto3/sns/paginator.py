from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListEndpointsByPlatformApplication(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PlatformApplicationArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPhoneNumbersOptedOut(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListPlatformApplications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListSubscriptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListSubscriptionsByTopic(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, TopicArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTopics(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
