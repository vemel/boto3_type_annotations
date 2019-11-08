from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_team_member(
        self,
        projectId: str,
        userArn: str,
        projectRole: str,
        clientRequestToken: str = None,
        remoteAccessAllowed: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_project(
        self,
        name: str,
        id: str,
        description: str = None,
        clientRequestToken: str = None,
        sourceCode: List[Any] = None,
        toolchain: Dict[str, Any] = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_user_profile(
        self,
        userArn: str,
        displayName: str,
        emailAddress: str,
        sshPublicKey: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_project(
        self, id: str, clientRequestToken: str = None, deleteStack: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_user_profile(self, userArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_project(self, id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_user_profile(self, userArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_team_member(self, projectId: str, userArn: str) -> Dict[str, Any]:
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
    def list_projects(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resources(
        self, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_project(
        self, id: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_team_members(
        self, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_user_profiles(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_project(self, id: str, tags: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_project(self, id: str, tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_project(
        self, id: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_team_member(
        self,
        projectId: str,
        userArn: str,
        projectRole: str = None,
        remoteAccessAllowed: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_user_profile(
        self,
        userArn: str,
        displayName: str = None,
        emailAddress: str = None,
        sshPublicKey: str = None,
    ) -> Dict[str, Any]:
        pass
