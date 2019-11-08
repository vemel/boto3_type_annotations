from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_notification_rule(
        self,
        Name: str,
        EventTypeIds: List[Any],
        Resource: str,
        Targets: List[Any],
        DetailType: str,
        ClientRequestToken: str = None,
        Tags: Dict[str, Any] = None,
        Status: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_notification_rule(self, Arn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_target(
        self, TargetAddress: str, ForceUnsubscribeAll: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_notification_rule(self, Arn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_event_types(
        self, Filters: List[Any] = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_notification_rules(
        self, Filters: List[Any] = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, Arn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_targets(
        self, Filters: List[Any] = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def subscribe(
        self, Arn: str, Target: Dict[str, Any], ClientRequestToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, Arn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def unsubscribe(self, Arn: str, TargetAddress: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, Arn: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_notification_rule(
        self,
        Arn: str,
        Name: str = None,
        Status: str = None,
        EventTypeIds: List[Any] = None,
        Targets: List[Any] = None,
        DetailType: str = None,
    ) -> Dict[str, Any]:
        pass
