from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_member_account(self, memberAccountId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def associate_s3_resources(
        self, s3Resources: List[Any], memberAccountId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def disassociate_member_account(self, memberAccountId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def disassociate_s3_resources(
        self, associatedS3Resources: List[Any], memberAccountId: str = None
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
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_member_accounts(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_s3_resources(
        self, memberAccountId: str = None, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_s3_resources(
        self, s3ResourcesUpdate: List[Any], memberAccountId: str = None
    ) -> Dict[str, Any]:
        pass
