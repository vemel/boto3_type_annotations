from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_delete_builds(
        self,
        ids: List,
    ) -> Dict:
        pass


    def batch_get_builds(
        self,
        ids: List,
    ) -> Dict:
        pass


    def batch_get_projects(
        self,
        names: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_project(
        self,
        name: str,
        source: Dict,
        artifacts: Dict,
        environment: Dict,
        serviceRole: str,
        description: Optional[str] = None,
        secondarySources: Optional[List] = None,
        sourceVersion: Optional[str] = None,
        secondarySourceVersions: Optional[List] = None,
        secondaryArtifacts: Optional[List] = None,
        cache: Optional[Dict] = None,
        timeoutInMinutes: Optional[int] = None,
        queuedTimeoutInMinutes: Optional[int] = None,
        encryptionKey: Optional[str] = None,
        tags: Optional[List] = None,
        vpcConfig: Optional[Dict] = None,
        badgeEnabled: Optional[bool] = None,
        logsConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_webhook(
        self,
        projectName: str,
        branchFilter: Optional[str] = None,
        filterGroups: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_project(
        self,
        name: str,
    ) -> Dict:
        pass


    def delete_source_credentials(
        self,
        arn: str,
    ) -> Dict:
        pass


    def delete_webhook(
        self,
        projectName: str,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def import_source_credentials(
        self,
        token: str,
        serverType: str,
        authType: str,
        username: Optional[str] = None,
        shouldOverwrite: Optional[bool] = None,
    ) -> Dict:
        pass


    def invalidate_project_cache(
        self,
        projectName: str,
    ) -> Dict:
        pass


    def list_builds(
        self,
        sortOrder: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_builds_for_project(
        self,
        projectName: str,
        sortOrder: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_curated_environment_images(
        self,
    ) -> Dict:
        pass


    def list_projects(
        self,
        sortBy: Optional[str] = None,
        sortOrder: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_source_credentials(
        self,
    ) -> Dict:
        pass


    def start_build(
        self,
        projectName: str,
        secondarySourcesOverride: Optional[List] = None,
        secondarySourcesVersionOverride: Optional[List] = None,
        sourceVersion: Optional[str] = None,
        artifactsOverride: Optional[Dict] = None,
        secondaryArtifactsOverride: Optional[List] = None,
        environmentVariablesOverride: Optional[List] = None,
        sourceTypeOverride: Optional[str] = None,
        sourceLocationOverride: Optional[str] = None,
        sourceAuthOverride: Optional[Dict] = None,
        gitCloneDepthOverride: Optional[int] = None,
        gitSubmodulesConfigOverride: Optional[Dict] = None,
        buildspecOverride: Optional[str] = None,
        insecureSslOverride: Optional[bool] = None,
        reportBuildStatusOverride: Optional[bool] = None,
        environmentTypeOverride: Optional[str] = None,
        imageOverride: Optional[str] = None,
        computeTypeOverride: Optional[str] = None,
        certificateOverride: Optional[str] = None,
        cacheOverride: Optional[Dict] = None,
        serviceRoleOverride: Optional[str] = None,
        privilegedModeOverride: Optional[bool] = None,
        timeoutInMinutesOverride: Optional[int] = None,
        queuedTimeoutInMinutesOverride: Optional[int] = None,
        idempotencyToken: Optional[str] = None,
        logsConfigOverride: Optional[Dict] = None,
        registryCredentialOverride: Optional[Dict] = None,
        imagePullCredentialsTypeOverride: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_build(
        self,
        id: str,
    ) -> Dict:
        pass


    def update_project(
        self,
        name: str,
        description: Optional[str] = None,
        source: Optional[Dict] = None,
        secondarySources: Optional[List] = None,
        sourceVersion: Optional[str] = None,
        secondarySourceVersions: Optional[List] = None,
        artifacts: Optional[Dict] = None,
        secondaryArtifacts: Optional[List] = None,
        cache: Optional[Dict] = None,
        environment: Optional[Dict] = None,
        serviceRole: Optional[str] = None,
        timeoutInMinutes: Optional[int] = None,
        queuedTimeoutInMinutes: Optional[int] = None,
        encryptionKey: Optional[str] = None,
        tags: Optional[List] = None,
        vpcConfig: Optional[Dict] = None,
        badgeEnabled: Optional[bool] = None,
        logsConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_webhook(
        self,
        projectName: str,
        branchFilter: Optional[str] = None,
        rotateSecret: Optional[bool] = None,
        filterGroups: Optional[List] = None,
    ) -> Dict:
        pass

