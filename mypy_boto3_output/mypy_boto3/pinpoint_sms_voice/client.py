from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_configuration_set(
        self, ConfigurationSetName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: Dict[str, Any] = None,
        EventDestinationName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
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
    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def send_voice_message(
        self,
        CallerId: str = None,
        ConfigurationSetName: str = None,
        Content: Dict[str, Any] = None,
        DestinationPhoneNumber: str = None,
        OriginationPhoneNumber: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
