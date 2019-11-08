from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def batch_delete_builds(self, ids: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_builds(self, ids: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_projects(self, names: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_project(
        self,
        name: str,
        source: Dict[str, Any],
        artifacts: Dict[str, Any],
        environment: Dict[str, Any],
        serviceRole: str,
        description: str = None,
        secondarySources: List[Any] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List[Any] = None,
        secondaryArtifacts: List[Any] = None,
        cache: Dict[str, Any] = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List[Any] = None,
        vpcConfig: Dict[str, Any] = None,
        badgeEnabled: bool = None,
        logsConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_webhook(
        self, projectName: str, branchFilter: str = None, filterGroups: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_project(self, name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_source_credentials(self, arn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_webhook(self, projectName: str) -> Dict[str, Any]:
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
    def import_source_credentials(
        self,
        token: str,
        serverType: str,
        authType: str,
        username: str = None,
        shouldOverwrite: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def invalidate_project_cache(self, projectName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_builds(
        self, sortOrder: str = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_builds_for_project(
        self, projectName: str, sortOrder: str = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_curated_environment_images(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_projects(
        self, sortBy: str = None, sortOrder: str = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_source_credentials(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_build(
        self,
        projectName: str,
        secondarySourcesOverride: List[Any] = None,
        secondarySourcesVersionOverride: List[Any] = None,
        sourceVersion: str = None,
        artifactsOverride: Dict[str, Any] = None,
        secondaryArtifactsOverride: List[Any] = None,
        environmentVariablesOverride: List[Any] = None,
        sourceTypeOverride: str = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: Dict[str, Any] = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: Dict[str, Any] = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildStatusOverride: bool = None,
        environmentTypeOverride: str = None,
        imageOverride: str = None,
        computeTypeOverride: str = None,
        certificateOverride: str = None,
        cacheOverride: Dict[str, Any] = None,
        serviceRoleOverride: str = None,
        privilegedModeOverride: bool = None,
        timeoutInMinutesOverride: int = None,
        queuedTimeoutInMinutesOverride: int = None,
        idempotencyToken: str = None,
        logsConfigOverride: Dict[str, Any] = None,
        registryCredentialOverride: Dict[str, Any] = None,
        imagePullCredentialsTypeOverride: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_build(self, id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_project(
        self,
        name: str,
        description: str = None,
        source: Dict[str, Any] = None,
        secondarySources: List[Any] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List[Any] = None,
        artifacts: Dict[str, Any] = None,
        secondaryArtifacts: List[Any] = None,
        cache: Dict[str, Any] = None,
        environment: Dict[str, Any] = None,
        serviceRole: str = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List[Any] = None,
        vpcConfig: Dict[str, Any] = None,
        badgeEnabled: bool = None,
        logsConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        rotateSecret: bool = None,
        filterGroups: List[Any] = None,
    ) -> Dict[str, Any]:
        pass
