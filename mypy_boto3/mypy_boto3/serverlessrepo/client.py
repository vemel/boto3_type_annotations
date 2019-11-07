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


    def create_application(
        self,
        Author: str,
        Description: str,
        Name: str,
        HomePageUrl: Optional[str] = None,
        Labels: Optional[List] = None,
        LicenseBody: Optional[str] = None,
        LicenseUrl: Optional[str] = None,
        ReadmeBody: Optional[str] = None,
        ReadmeUrl: Optional[str] = None,
        SemanticVersion: Optional[str] = None,
        SourceCodeArchiveUrl: Optional[str] = None,
        SourceCodeUrl: Optional[str] = None,
        SpdxLicenseId: Optional[str] = None,
        TemplateBody: Optional[str] = None,
        TemplateUrl: Optional[str] = None,
    ) -> Dict:
        pass


    def create_application_version(
        self,
        ApplicationId: str,
        SemanticVersion: str,
        SourceCodeArchiveUrl: Optional[str] = None,
        SourceCodeUrl: Optional[str] = None,
        TemplateBody: Optional[str] = None,
        TemplateUrl: Optional[str] = None,
    ) -> Dict:
        pass


    def create_cloud_formation_change_set(
        self,
        ApplicationId: str,
        StackName: str,
        Capabilities: Optional[List] = None,
        ChangeSetName: Optional[str] = None,
        ClientToken: Optional[str] = None,
        Description: Optional[str] = None,
        NotificationArns: Optional[List] = None,
        ParameterOverrides: Optional[List] = None,
        ResourceTypes: Optional[List] = None,
        RollbackConfiguration: Optional[Dict] = None,
        SemanticVersion: Optional[str] = None,
        Tags: Optional[List] = None,
        TemplateId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_cloud_formation_template(
        self,
        ApplicationId: str,
        SemanticVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_application(
        self,
        ApplicationId: str,
    ):
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_application(
        self,
        ApplicationId: str,
        SemanticVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def get_application_policy(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_cloud_formation_template(
        self,
        ApplicationId: str,
        TemplateId: str,
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


    def list_application_dependencies(
        self,
        ApplicationId: str,
        MaxItems: Optional[int] = None,
        NextToken: Optional[str] = None,
        SemanticVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def list_application_versions(
        self,
        ApplicationId: str,
        MaxItems: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_applications(
        self,
        MaxItems: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_application_policy(
        self,
        ApplicationId: str,
        Statements: List,
    ) -> Dict:
        pass


    def update_application(
        self,
        ApplicationId: str,
        Author: Optional[str] = None,
        Description: Optional[str] = None,
        HomePageUrl: Optional[str] = None,
        Labels: Optional[List] = None,
        ReadmeBody: Optional[str] = None,
        ReadmeUrl: Optional[str] = None,
    ) -> Dict:
        pass

