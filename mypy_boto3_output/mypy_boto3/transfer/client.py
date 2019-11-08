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
    def create_server(
        self,
        EndpointDetails: Dict[str, Any] = None,
        EndpointType: str = None,
        HostKey: str = None,
        IdentityProviderDetails: Dict[str, Any] = None,
        IdentityProviderType: str = None,
        LoggingRole: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_user(
        self,
        Role: str,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: str = None,
        HomeDirectoryMappings: List[Any] = None,
        Policy: str = None,
        SshPublicKeyBody: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_server(self, ServerId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_ssh_public_key(
        self, ServerId: str, SshPublicKeyId: str, UserName: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_user(self, ServerId: str, UserName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_server(self, ServerId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_user(self, ServerId: str, UserName: str) -> Dict[str, Any]:
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
    def import_ssh_public_key(
        self, ServerId: str, SshPublicKeyBody: str, UserName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_servers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, Arn: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_users(
        self, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_server(self, ServerId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_server(self, ServerId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, Arn: str, Tags: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def test_identity_provider(
        self, ServerId: str, UserName: str, UserPassword: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, Arn: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_server(
        self,
        ServerId: str,
        EndpointDetails: Dict[str, Any] = None,
        EndpointType: str = None,
        HostKey: str = None,
        IdentityProviderDetails: Dict[str, Any] = None,
        LoggingRole: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_user(
        self,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: str = None,
        HomeDirectoryMappings: List[Any] = None,
        Policy: str = None,
        Role: str = None,
    ) -> Dict[str, Any]:
        pass
