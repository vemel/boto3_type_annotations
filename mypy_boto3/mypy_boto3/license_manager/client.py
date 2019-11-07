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


    def create_license_configuration(
        self,
        Name: str,
        LicenseCountingType: str,
        Description: Optional[str] = None,
        LicenseCount: Optional[int] = None,
        LicenseCountHardLimit: Optional[bool] = None,
        LicenseRules: Optional[List] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_license_configuration(
        self,
        LicenseConfigurationArn: str,
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


    def get_license_configuration(
        self,
        LicenseConfigurationArn: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_service_settings(
        self,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_associations_for_license_configuration(
        self,
        LicenseConfigurationArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_license_configurations(
        self,
        LicenseConfigurationArns: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_license_specifications_for_resource(
        self,
        ResourceArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_resource_inventory(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def list_usage_for_license_configuration(
        self,
        LicenseConfigurationArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_license_configuration(
        self,
        LicenseConfigurationArn: str,
        LicenseConfigurationStatus: Optional[str] = None,
        LicenseRules: Optional[List] = None,
        LicenseCount: Optional[int] = None,
        LicenseCountHardLimit: Optional[bool] = None,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_license_specifications_for_resource(
        self,
        ResourceArn: str,
        AddLicenseSpecifications: Optional[List] = None,
        RemoveLicenseSpecifications: Optional[List] = None,
    ) -> Dict:
        pass


    def update_service_settings(
        self,
        S3BucketArn: Optional[str] = None,
        SnsTopicArn: Optional[str] = None,
        OrganizationConfiguration: Optional[Dict] = None,
        EnableCrossAccountsDiscovery: Optional[bool] = None,
    ) -> Dict:
        pass

