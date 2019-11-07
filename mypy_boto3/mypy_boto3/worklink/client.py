from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_domain(
        self,
        FleetArn: str,
        DomainName: str,
        AcmCertificateArn: str,
        DisplayName: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_website_authorization_provider(
        self,
        FleetArn: str,
        AuthorizationProviderType: str,
        DomainName: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_website_certificate_authority(
        self,
        FleetArn: str,
        Certificate: str,
        DisplayName: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_fleet(
        self,
        FleetName: str,
        DisplayName: Optional[str] = None,
        OptimizeForEndUserLocation: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_fleet(
        self,
        FleetArn: str,
    ) -> Dict:
        pass


    def describe_audit_stream_configuration(
        self,
        FleetArn: str,
    ) -> Dict:
        pass


    def describe_company_network_configuration(
        self,
        FleetArn: str,
    ) -> Dict:
        pass


    def describe_device(
        self,
        FleetArn: str,
        DeviceId: str,
    ) -> Dict:
        pass


    def describe_device_policy_configuration(
        self,
        FleetArn: str,
    ) -> Dict:
        pass


    def describe_domain(
        self,
        FleetArn: str,
        DomainName: str,
    ) -> Dict:
        pass


    def describe_fleet_metadata(
        self,
        FleetArn: str,
    ) -> Dict:
        pass


    def describe_identity_provider_configuration(
        self,
        FleetArn: str,
    ) -> Dict:
        pass


    def describe_website_certificate_authority(
        self,
        FleetArn: str,
        WebsiteCaId: str,
    ) -> Dict:
        pass


    def disassociate_domain(
        self,
        FleetArn: str,
        DomainName: str,
    ) -> Dict:
        pass


    def disassociate_website_authorization_provider(
        self,
        FleetArn: str,
        AuthorizationProviderId: str,
    ) -> Dict:
        pass


    def disassociate_website_certificate_authority(
        self,
        FleetArn: str,
        WebsiteCaId: str,
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


    def list_devices(
        self,
        FleetArn: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_domains(
        self,
        FleetArn: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_fleets(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_website_authorization_providers(
        self,
        FleetArn: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_website_certificate_authorities(
        self,
        FleetArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def restore_domain_access(
        self,
        FleetArn: str,
        DomainName: str,
    ) -> Dict:
        pass


    def revoke_domain_access(
        self,
        FleetArn: str,
        DomainName: str,
    ) -> Dict:
        pass


    def sign_out_user(
        self,
        FleetArn: str,
        Username: str,
    ) -> Dict:
        pass


    def update_audit_stream_configuration(
        self,
        FleetArn: str,
        AuditStreamArn: Optional[str] = None,
    ) -> Dict:
        pass


    def update_company_network_configuration(
        self,
        FleetArn: str,
        VpcId: str,
        SubnetIds: List,
        SecurityGroupIds: List,
    ) -> Dict:
        pass


    def update_device_policy_configuration(
        self,
        FleetArn: str,
        DeviceCaCertificate: Optional[str] = None,
    ) -> Dict:
        pass


    def update_domain_metadata(
        self,
        FleetArn: str,
        DomainName: str,
        DisplayName: Optional[str] = None,
    ) -> Dict:
        pass


    def update_fleet_metadata(
        self,
        FleetArn: str,
        DisplayName: Optional[str] = None,
        OptimizeForEndUserLocation: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_identity_provider_configuration(
        self,
        FleetArn: str,
        IdentityProviderType: str,
        IdentityProviderSamlMetadata: Optional[str] = None,
    ) -> Dict:
        pass

