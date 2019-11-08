from __future__ import annotations

from typing import Any
from typing import Dict
from typing import IO
from typing import Union

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_project(
        self,
        name: str = None,
        region: str = None,
        contents: Union[bytes, IO] = None,
        snapshotId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_project(self, projectId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_bundle(self, bundleId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_project(
        self, projectId: str, syncFromResources: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def export_bundle(
        self, bundleId: str, projectId: str = None, platform: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def export_project(self, projectId: str) -> Dict[str, Any]:
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
    def list_bundles(
        self, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_projects(
        self, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_project(
        self, projectId: str, contents: Union[bytes, IO] = None
    ) -> Dict[str, Any]:
        pass
