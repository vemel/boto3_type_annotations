from __future__ import annotations

from datetime import datetime
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
    def create_app(
        self,
        name: str,
        description: str = None,
        repository: str = None,
        platform: str = None,
        iamServiceRoleArn: str = None,
        oauthToken: str = None,
        accessToken: str = None,
        environmentVariables: Dict[str, Any] = None,
        enableBranchAutoBuild: bool = None,
        enableBasicAuth: bool = None,
        basicAuthCredentials: str = None,
        customRules: List[Any] = None,
        tags: Dict[str, Any] = None,
        buildSpec: str = None,
        enableAutoBranchCreation: bool = None,
        autoBranchCreationPatterns: List[Any] = None,
        autoBranchCreationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_branch(
        self,
        appId: str,
        branchName: str,
        description: str = None,
        stage: str = None,
        framework: str = None,
        enableNotification: bool = None,
        enableAutoBuild: bool = None,
        environmentVariables: Dict[str, Any] = None,
        basicAuthCredentials: str = None,
        enableBasicAuth: bool = None,
        tags: Dict[str, Any] = None,
        buildSpec: str = None,
        ttl: str = None,
        displayName: str = None,
        enablePullRequestPreview: bool = None,
        pullRequestEnvironmentName: str = None,
        backendEnvironmentArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_deployment(
        self, appId: str, branchName: str, fileMap: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_domain_association(
        self,
        appId: str,
        domainName: str,
        subDomainSettings: List[Any],
        enableAutoSubDomain: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_webhook(
        self, appId: str, branchName: str, description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_app(self, appId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_branch(self, appId: str, branchName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_domain_association(self, appId: str, domainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_job(self, appId: str, branchName: str, jobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_webhook(self, webhookId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_access_logs(
        self,
        domainName: str,
        appId: str,
        startTime: datetime = None,
        endTime: datetime = None,
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
    def get_app(self, appId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_artifact_url(self, artifactId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_branch(self, appId: str, branchName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_domain_association(self, appId: str, domainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_job(self, appId: str, branchName: str, jobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def get_webhook(self, webhookId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_apps(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_artifacts(
        self,
        appId: str,
        branchName: str,
        jobId: str,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_branches(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_domain_associations(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_jobs(
        self, appId: str, branchName: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, resourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_webhooks(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_deployment(
        self, appId: str, branchName: str, jobId: str = None, sourceUrl: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_job(
        self,
        appId: str,
        branchName: str,
        jobType: str,
        jobId: str = None,
        jobReason: str = None,
        commitId: str = None,
        commitMessage: str = None,
        commitTime: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_job(self, appId: str, branchName: str, jobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_app(
        self,
        appId: str,
        name: str = None,
        description: str = None,
        platform: str = None,
        iamServiceRoleArn: str = None,
        environmentVariables: Dict[str, Any] = None,
        enableBranchAutoBuild: bool = None,
        enableBasicAuth: bool = None,
        basicAuthCredentials: str = None,
        customRules: List[Any] = None,
        buildSpec: str = None,
        enableAutoBranchCreation: bool = None,
        autoBranchCreationPatterns: List[Any] = None,
        autoBranchCreationConfig: Dict[str, Any] = None,
        repository: str = None,
        oauthToken: str = None,
        accessToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_branch(
        self,
        appId: str,
        branchName: str,
        description: str = None,
        framework: str = None,
        stage: str = None,
        enableNotification: bool = None,
        enableAutoBuild: bool = None,
        environmentVariables: Dict[str, Any] = None,
        basicAuthCredentials: str = None,
        enableBasicAuth: bool = None,
        buildSpec: str = None,
        ttl: str = None,
        displayName: str = None,
        enablePullRequestPreview: bool = None,
        pullRequestEnvironmentName: str = None,
        backendEnvironmentArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_domain_association(
        self,
        appId: str,
        domainName: str,
        subDomainSettings: List[Any],
        enableAutoSubDomain: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_webhook(
        self, webhookId: str, branchName: str = None, description: str = None
    ) -> Dict[str, Any]:
        pass
