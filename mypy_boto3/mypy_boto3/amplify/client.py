from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_app(
        self,
        name: str,
        description: Optional[str] = None,
        repository: Optional[str] = None,
        platform: Optional[str] = None,
        iamServiceRoleArn: Optional[str] = None,
        oauthToken: Optional[str] = None,
        accessToken: Optional[str] = None,
        environmentVariables: Optional[Dict] = None,
        enableBranchAutoBuild: Optional[bool] = None,
        enableBasicAuth: Optional[bool] = None,
        basicAuthCredentials: Optional[str] = None,
        customRules: Optional[List] = None,
        tags: Optional[Dict] = None,
        buildSpec: Optional[str] = None,
        enableAutoBranchCreation: Optional[bool] = None,
        autoBranchCreationPatterns: Optional[List] = None,
        autoBranchCreationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_branch(
        self,
        appId: str,
        branchName: str,
        description: Optional[str] = None,
        stage: Optional[str] = None,
        framework: Optional[str] = None,
        enableNotification: Optional[bool] = None,
        enableAutoBuild: Optional[bool] = None,
        environmentVariables: Optional[Dict] = None,
        basicAuthCredentials: Optional[str] = None,
        enableBasicAuth: Optional[bool] = None,
        tags: Optional[Dict] = None,
        buildSpec: Optional[str] = None,
        ttl: Optional[str] = None,
        displayName: Optional[str] = None,
        enablePullRequestPreview: Optional[bool] = None,
        pullRequestEnvironmentName: Optional[str] = None,
        backendEnvironmentArn: Optional[str] = None,
    ) -> Dict:
        pass


    def create_deployment(
        self,
        appId: str,
        branchName: str,
        fileMap: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_domain_association(
        self,
        appId: str,
        domainName: str,
        subDomainSettings: List,
        enableAutoSubDomain: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_webhook(
        self,
        appId: str,
        branchName: str,
        description: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_app(
        self,
        appId: str,
    ) -> Dict:
        pass


    def delete_branch(
        self,
        appId: str,
        branchName: str,
    ) -> Dict:
        pass


    def delete_domain_association(
        self,
        appId: str,
        domainName: str,
    ) -> Dict:
        pass


    def delete_job(
        self,
        appId: str,
        branchName: str,
        jobId: str,
    ) -> Dict:
        pass


    def delete_webhook(
        self,
        webhookId: str,
    ) -> Dict:
        pass


    def generate_access_logs(
        self,
        domainName: str,
        appId: str,
        startTime: Optional[datetime] = None,
        endTime: Optional[datetime] = None,
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


    def get_app(
        self,
        appId: str,
    ) -> Dict:
        pass


    def get_artifact_url(
        self,
        artifactId: str,
    ) -> Dict:
        pass


    def get_branch(
        self,
        appId: str,
        branchName: str,
    ) -> Dict:
        pass


    def get_domain_association(
        self,
        appId: str,
        domainName: str,
    ) -> Dict:
        pass


    def get_job(
        self,
        appId: str,
        branchName: str,
        jobId: str,
    ) -> Dict:
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


    def get_webhook(
        self,
        webhookId: str,
    ) -> Dict:
        pass


    def list_apps(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_artifacts(
        self,
        appId: str,
        branchName: str,
        jobId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_branches(
        self,
        appId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_domain_associations(
        self,
        appId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_jobs(
        self,
        appId: str,
        branchName: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def list_webhooks(
        self,
        appId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def start_deployment(
        self,
        appId: str,
        branchName: str,
        jobId: Optional[str] = None,
        sourceUrl: Optional[str] = None,
    ) -> Dict:
        pass


    def start_job(
        self,
        appId: str,
        branchName: str,
        jobType: str,
        jobId: Optional[str] = None,
        jobReason: Optional[str] = None,
        commitId: Optional[str] = None,
        commitMessage: Optional[str] = None,
        commitTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def stop_job(
        self,
        appId: str,
        branchName: str,
        jobId: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_app(
        self,
        appId: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        platform: Optional[str] = None,
        iamServiceRoleArn: Optional[str] = None,
        environmentVariables: Optional[Dict] = None,
        enableBranchAutoBuild: Optional[bool] = None,
        enableBasicAuth: Optional[bool] = None,
        basicAuthCredentials: Optional[str] = None,
        customRules: Optional[List] = None,
        buildSpec: Optional[str] = None,
        enableAutoBranchCreation: Optional[bool] = None,
        autoBranchCreationPatterns: Optional[List] = None,
        autoBranchCreationConfig: Optional[Dict] = None,
        repository: Optional[str] = None,
        oauthToken: Optional[str] = None,
        accessToken: Optional[str] = None,
    ) -> Dict:
        pass


    def update_branch(
        self,
        appId: str,
        branchName: str,
        description: Optional[str] = None,
        framework: Optional[str] = None,
        stage: Optional[str] = None,
        enableNotification: Optional[bool] = None,
        enableAutoBuild: Optional[bool] = None,
        environmentVariables: Optional[Dict] = None,
        basicAuthCredentials: Optional[str] = None,
        enableBasicAuth: Optional[bool] = None,
        buildSpec: Optional[str] = None,
        ttl: Optional[str] = None,
        displayName: Optional[str] = None,
        enablePullRequestPreview: Optional[bool] = None,
        pullRequestEnvironmentName: Optional[str] = None,
        backendEnvironmentArn: Optional[str] = None,
    ) -> Dict:
        pass


    def update_domain_association(
        self,
        appId: str,
        domainName: str,
        subDomainSettings: List,
        enableAutoSubDomain: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_webhook(
        self,
        webhookId: str,
        branchName: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict:
        pass

