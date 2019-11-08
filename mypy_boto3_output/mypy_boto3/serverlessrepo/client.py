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
    def create_application(
        self,
        Author: str,
        Description: str,
        Name: str,
        HomePageUrl: str = None,
        Labels: List[Any] = None,
        LicenseBody: str = None,
        LicenseUrl: str = None,
        ReadmeBody: str = None,
        ReadmeUrl: str = None,
        SemanticVersion: str = None,
        SourceCodeArchiveUrl: str = None,
        SourceCodeUrl: str = None,
        SpdxLicenseId: str = None,
        TemplateBody: str = None,
        TemplateUrl: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_application_version(
        self,
        ApplicationId: str,
        SemanticVersion: str,
        SourceCodeArchiveUrl: str = None,
        SourceCodeUrl: str = None,
        TemplateBody: str = None,
        TemplateUrl: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cloud_formation_change_set(
        self,
        ApplicationId: str,
        StackName: str,
        Capabilities: List[Any] = None,
        ChangeSetName: str = None,
        ClientToken: str = None,
        Description: str = None,
        NotificationArns: List[Any] = None,
        ParameterOverrides: List[Any] = None,
        ResourceTypes: List[Any] = None,
        RollbackConfiguration: Dict[str, Any] = None,
        SemanticVersion: str = None,
        Tags: List[Any] = None,
        TemplateId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cloud_formation_template(
        self, ApplicationId: str, SemanticVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_application(self, ApplicationId: str) -> None:
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
    def get_application(
        self, ApplicationId: str, SemanticVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_application_policy(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_cloud_formation_template(
        self, ApplicationId: str, TemplateId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_application_dependencies(
        self,
        ApplicationId: str,
        MaxItems: int = None,
        NextToken: str = None,
        SemanticVersion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_application_versions(
        self, ApplicationId: str, MaxItems: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_applications(
        self, MaxItems: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_application_policy(
        self, ApplicationId: str, Statements: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_application(
        self,
        ApplicationId: str,
        Author: str = None,
        Description: str = None,
        HomePageUrl: str = None,
        Labels: List[Any] = None,
        ReadmeBody: str = None,
        ReadmeUrl: str = None,
    ) -> Dict[str, Any]:
        pass
