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
    def create_backup(
        self, FileSystemId: str, ClientRequestToken: str = None, Tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_file_system(
        self,
        FileSystemType: str,
        StorageCapacity: int,
        SubnetIds: List[Any],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[Any] = None,
        Tags: List[Any] = None,
        KmsKeyId: str = None,
        WindowsConfiguration: Dict[str, Any] = None,
        LustreConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_file_system_from_backup(
        self,
        BackupId: str,
        SubnetIds: List[Any],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[Any] = None,
        Tags: List[Any] = None,
        WindowsConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_backup(
        self, BackupId: str, ClientRequestToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_backups(
        self,
        BackupIds: List[Any] = None,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_file_systems(
        self,
        FileSystemIds: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
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
    def list_tags_for_resource(
        self, ResourceARN: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: Dict[str, Any] = None,
        LustreConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
