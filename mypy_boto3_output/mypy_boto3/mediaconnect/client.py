from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_flow_outputs(self, FlowArn: str, Outputs: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_flow(
        self,
        Name: str,
        Source: Dict[str, Any],
        AvailabilityZone: str = None,
        Entitlements: List[Any] = None,
        Outputs: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_flow(self, FlowArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_flow(self, FlowArn: str) -> Dict[str, Any]:
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
    def grant_flow_entitlements(
        self, Entitlements: List[Any], FlowArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_entitlements(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_flows(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_flow_output(self, FlowArn: str, OutputArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def revoke_flow_entitlement(
        self, EntitlementArn: str, FlowArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_flow(self, FlowArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_flow(self, FlowArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_flow_entitlement(
        self,
        EntitlementArn: str,
        FlowArn: str,
        Description: str = None,
        Encryption: Dict[str, Any] = None,
        Subscribers: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_flow_output(
        self,
        FlowArn: str,
        OutputArn: str,
        CidrAllowList: List[Any] = None,
        Description: str = None,
        Destination: str = None,
        Encryption: Dict[str, Any] = None,
        MaxLatency: int = None,
        Port: int = None,
        Protocol: str = None,
        RemoteId: str = None,
        SmoothingLatency: int = None,
        StreamId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_flow_source(
        self,
        FlowArn: str,
        SourceArn: str,
        Decryption: Dict[str, Any] = None,
        Description: str = None,
        EntitlementArn: str = None,
        IngestPort: int = None,
        MaxBitrate: int = None,
        MaxLatency: int = None,
        Protocol: str = None,
        StreamId: str = None,
        WhitelistCidr: str = None,
    ) -> Dict[str, Any]:
        pass
