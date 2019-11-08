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
    def create_license_configuration(
        self,
        Name: str,
        LicenseCountingType: str,
        Description: str = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        LicenseRules: List[Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_license_configuration(
        self, LicenseConfigurationArn: str
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
    def get_license_configuration(self, LicenseConfigurationArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_service_settings(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_associations_for_license_configuration(
        self,
        LicenseConfigurationArn: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_license_configurations(
        self,
        LicenseConfigurationArns: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_license_specifications_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resource_inventory(
        self, MaxResults: int = None, NextToken: str = None, Filters: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_usage_for_license_configuration(
        self,
        LicenseConfigurationArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_license_configuration(
        self,
        LicenseConfigurationArn: str,
        LicenseConfigurationStatus: str = None,
        LicenseRules: List[Any] = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        Name: str = None,
        Description: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_license_specifications_for_resource(
        self,
        ResourceArn: str,
        AddLicenseSpecifications: List[Any] = None,
        RemoveLicenseSpecifications: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_service_settings(
        self,
        S3BucketArn: str = None,
        SnsTopicArn: str = None,
        OrganizationConfiguration: Dict[str, Any] = None,
        EnableCrossAccountsDiscovery: bool = None,
    ) -> Dict[str, Any]:
        pass
