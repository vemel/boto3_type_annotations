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
    def get_resources(
        self,
        PaginationToken: str = None,
        TagFilters: List[Any] = None,
        ResourcesPerPage: int = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_tag_keys(self, PaginationToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_tag_values(self, Key: str, PaginationToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def tag_resources(
        self, ResourceARNList: List[Any], Tags: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resources(
        self, ResourceARNList: List[Any], TagKeys: List[Any]
    ) -> Dict[str, Any]:
        pass
