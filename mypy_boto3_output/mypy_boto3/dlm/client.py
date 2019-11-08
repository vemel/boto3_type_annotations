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
    def create_lifecycle_policy(
        self,
        ExecutionRoleArn: str,
        Description: str,
        State: str,
        PolicyDetails: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_lifecycle_policy(self, PolicyId: str) -> Dict[str, Any]:
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
    def get_lifecycle_policies(
        self,
        PolicyIds: List[Any] = None,
        State: str = None,
        ResourceTypes: List[Any] = None,
        TargetTags: List[Any] = None,
        TagsToAdd: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_lifecycle_policy(self, PolicyId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def update_lifecycle_policy(
        self,
        PolicyId: str,
        ExecutionRoleArn: str = None,
        State: str = None,
        Description: str = None,
        PolicyDetails: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
