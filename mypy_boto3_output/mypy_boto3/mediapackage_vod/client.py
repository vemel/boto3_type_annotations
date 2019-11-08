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
    def create_asset(
        self,
        Id: str,
        PackagingGroupId: str,
        SourceArn: str,
        SourceRoleArn: str,
        ResourceId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_packaging_configuration(
        self,
        Id: str,
        PackagingGroupId: str,
        CmafPackage: Dict[str, Any] = None,
        DashPackage: Dict[str, Any] = None,
        HlsPackage: Dict[str, Any] = None,
        MssPackage: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_packaging_group(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_asset(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_packaging_configuration(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_packaging_group(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_asset(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_packaging_configuration(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_packaging_group(self, Id: str) -> Dict[str, Any]:
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
    def list_assets(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        PackagingGroupId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_packaging_configurations(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        PackagingGroupId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_packaging_groups(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass
