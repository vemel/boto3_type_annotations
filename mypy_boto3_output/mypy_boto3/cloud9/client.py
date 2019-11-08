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
    def create_environment_ec2(
        self,
        name: str,
        instanceType: str,
        description: str = None,
        clientRequestToken: str = None,
        subnetId: str = None,
        automaticStopTimeMinutes: int = None,
        ownerArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_environment_membership(
        self, environmentId: str, userArn: str, permissions: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_environment(self, environmentId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_environment_membership(
        self, environmentId: str, userArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_environment_memberships(
        self,
        userArn: str = None,
        environmentId: str = None,
        permissions: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_environment_status(self, environmentId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_environments(self, environmentIds: List[Any]) -> Dict[str, Any]:
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
    def list_environments(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_environment(
        self, environmentId: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_environment_membership(
        self, environmentId: str, userArn: str, permissions: str
    ) -> Dict[str, Any]:
        pass
