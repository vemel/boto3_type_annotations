from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_domain(
        self,
        FleetArn: str,
        DomainName: str,
        AcmCertificateArn: str,
        DisplayName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_website_authorization_provider(
        self, FleetArn: str, AuthorizationProviderType: str, DomainName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_website_certificate_authority(
        self, FleetArn: str, Certificate: str, DisplayName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_fleet(
        self,
        FleetName: str,
        DisplayName: str = None,
        OptimizeForEndUserLocation: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_fleet(self, FleetArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_audit_stream_configuration(self, FleetArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_company_network_configuration(self, FleetArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_device(self, FleetArn: str, DeviceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_device_policy_configuration(self, FleetArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_domain(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_fleet_metadata(self, FleetArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_identity_provider_configuration(self, FleetArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_website_certificate_authority(
        self, FleetArn: str, WebsiteCaId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_domain(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_website_authorization_provider(
        self, FleetArn: str, AuthorizationProviderId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_website_certificate_authority(
        self, FleetArn: str, WebsiteCaId: str
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
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_devices(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_domains(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_fleets(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_website_authorization_providers(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_website_certificate_authorities(
        self, FleetArn: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_domain_access(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def revoke_domain_access(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def sign_out_user(self, FleetArn: str, Username: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_audit_stream_configuration(
        self, FleetArn: str, AuditStreamArn: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_company_network_configuration(
        self,
        FleetArn: str,
        VpcId: str,
        SubnetIds: List[Any],
        SecurityGroupIds: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_device_policy_configuration(
        self, FleetArn: str, DeviceCaCertificate: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_domain_metadata(
        self, FleetArn: str, DomainName: str, DisplayName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_fleet_metadata(
        self,
        FleetArn: str,
        DisplayName: str = None,
        OptimizeForEndUserLocation: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_identity_provider_configuration(
        self,
        FleetArn: str,
        IdentityProviderType: str,
        IdentityProviderSamlMetadata: str = None,
    ) -> Dict[str, Any]:
        pass
