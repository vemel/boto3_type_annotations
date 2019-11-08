from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def batch_grant_permissions(
        self, Entries: List[Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_revoke_permissions(
        self, Entries: List[Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def deregister_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_resource(self, ResourceArn: str) -> Dict[str, Any]:
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
    def get_data_lake_settings(self, CatalogId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_effective_permissions_for_path(
        self,
        ResourceArn: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def grant_permissions(
        self,
        Principal: Dict[str, Any],
        Resource: Dict[str, Any],
        Permissions: List[Any],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_permissions(
        self,
        CatalogId: str = None,
        Principal: Dict[str, Any] = None,
        ResourceType: str = None,
        Resource: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resources(
        self,
        FilterConditionList: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_data_lake_settings(
        self, DataLakeSettings: Dict[str, Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_resource(
        self, ResourceArn: str, UseServiceLinkedRole: bool = None, RoleArn: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def revoke_permissions(
        self,
        Principal: Dict[str, Any],
        Resource: Dict[str, Any],
        Permissions: List[Any],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_resource(self, RoleArn: str, ResourceArn: str) -> Dict[str, Any]:
        pass
