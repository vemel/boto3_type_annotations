from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_drt_log_bucket(self, LogBucket: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_drt_role(self, RoleArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_protection(self, Name: str, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_subscription(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_protection(self, ProtectionId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_subscription(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_attack(self, AttackId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_drt_access(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_emergency_contact_settings(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_protection(
        self, ProtectionId: str = None, ResourceArn: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_subscription(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_drt_log_bucket(self, LogBucket: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_drt_role(self) -> Dict[str, Any]:
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
    def get_subscription_state(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_attacks(
        self,
        ResourceArns: List[Any] = None,
        StartTime: Dict[str, Any] = None,
        EndTime: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_protections(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_emergency_contact_settings(
        self, EmergencyContactList: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_subscription(self, AutoRenew: str = None) -> Dict[str, Any]:
        pass
