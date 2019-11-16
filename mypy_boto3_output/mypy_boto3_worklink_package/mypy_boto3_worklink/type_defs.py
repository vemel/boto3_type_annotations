"Main interface for worklink type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAssociateWebsiteAuthorizationProviderResponseTypeDef",
    "ClientAssociateWebsiteCertificateAuthorityResponseTypeDef",
    "ClientCreateFleetResponseTypeDef",
    "ClientDescribeAuditStreamConfigurationResponseTypeDef",
    "ClientDescribeCompanyNetworkConfigurationResponseTypeDef",
    "ClientDescribeDevicePolicyConfigurationResponseTypeDef",
    "ClientDescribeDeviceResponseTypeDef",
    "ClientDescribeDomainResponseTypeDef",
    "ClientDescribeFleetMetadataResponseTypeDef",
    "ClientDescribeIdentityProviderConfigurationResponseTypeDef",
    "ClientDescribeWebsiteCertificateAuthorityResponseTypeDef",
    "ClientListDevicesResponseDevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListDomainsResponseDomainsTypeDef",
    "ClientListDomainsResponseTypeDef",
    "ClientListFleetsResponseFleetSummaryListTypeDef",
    "ClientListFleetsResponseTypeDef",
    "ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef",
    "ClientListWebsiteAuthorizationProvidersResponseTypeDef",
    "ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef",
    "ClientListWebsiteCertificateAuthoritiesResponseTypeDef",
)


_ClientAssociateWebsiteAuthorizationProviderResponseTypeDef = TypedDict(
    "_ClientAssociateWebsiteAuthorizationProviderResponseTypeDef",
    {"AuthorizationProviderId": str},
    total=False,
)


class ClientAssociateWebsiteAuthorizationProviderResponseTypeDef(
    _ClientAssociateWebsiteAuthorizationProviderResponseTypeDef
):
    """
    Type definition for `ClientAssociateWebsiteAuthorizationProvider` `Response`

    - **AuthorizationProviderId** *(string) --*

      A unique identifier for the authorization provider.
    """


_ClientAssociateWebsiteCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientAssociateWebsiteCertificateAuthorityResponseTypeDef",
    {"WebsiteCaId": str},
    total=False,
)


class ClientAssociateWebsiteCertificateAuthorityResponseTypeDef(
    _ClientAssociateWebsiteCertificateAuthorityResponseTypeDef
):
    """
    Type definition for `ClientAssociateWebsiteCertificateAuthority` `Response`

    - **WebsiteCaId** *(string) --*

      A unique identifier for the CA.
    """


_ClientCreateFleetResponseTypeDef = TypedDict(
    "_ClientCreateFleetResponseTypeDef", {"FleetArn": str}, total=False
)


class ClientCreateFleetResponseTypeDef(_ClientCreateFleetResponseTypeDef):
    """
    Type definition for `ClientCreateFleet` `Response`

    - **FleetArn** *(string) --*

      The ARN of the fleet.
    """


_ClientDescribeAuditStreamConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeAuditStreamConfigurationResponseTypeDef",
    {"AuditStreamArn": str},
    total=False,
)


class ClientDescribeAuditStreamConfigurationResponseTypeDef(
    _ClientDescribeAuditStreamConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeAuditStreamConfiguration` `Response`

    - **AuditStreamArn** *(string) --*

      The ARN of the Amazon Kinesis data stream that will receive the audit events.
    """


_ClientDescribeCompanyNetworkConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeCompanyNetworkConfigurationResponseTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientDescribeCompanyNetworkConfigurationResponseTypeDef(
    _ClientDescribeCompanyNetworkConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeCompanyNetworkConfiguration` `Response`

    - **VpcId** *(string) --*

      The VPC with connectivity to associated websites.

    - **SubnetIds** *(list) --*

      The subnets used for X-ENI connections from Amazon WorkLink rendering containers.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      The security groups associated with access to the provided subnets.

      - *(string) --*
    """


_ClientDescribeDevicePolicyConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeDevicePolicyConfigurationResponseTypeDef",
    {"DeviceCaCertificate": str},
    total=False,
)


class ClientDescribeDevicePolicyConfigurationResponseTypeDef(
    _ClientDescribeDevicePolicyConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeDevicePolicyConfiguration` `Response`

    - **DeviceCaCertificate** *(string) --*

      The certificate chain, including intermediate certificates and the root certificate authority
      certificate used to issue device certificates.
    """


_ClientDescribeDeviceResponseTypeDef = TypedDict(
    "_ClientDescribeDeviceResponseTypeDef",
    {
        "Status": str,
        "Model": str,
        "Manufacturer": str,
        "OperatingSystem": str,
        "OperatingSystemVersion": str,
        "PatchLevel": str,
        "FirstAccessedTime": datetime,
        "LastAccessedTime": datetime,
        "Username": str,
    },
    total=False,
)


class ClientDescribeDeviceResponseTypeDef(_ClientDescribeDeviceResponseTypeDef):
    """
    Type definition for `ClientDescribeDevice` `Response`

    - **Status** *(string) --*

      The current state of the device.

    - **Model** *(string) --*

      The model of the device.

    - **Manufacturer** *(string) --*

      The manufacturer of the device.

    - **OperatingSystem** *(string) --*

      The operating system of the device.

    - **OperatingSystemVersion** *(string) --*

      The operating system version of the device.

    - **PatchLevel** *(string) --*

      The operating system patch level of the device.

    - **FirstAccessedTime** *(datetime) --*

      The date that the device first signed in to Amazon WorkLink.

    - **LastAccessedTime** *(datetime) --*

      The date that the device last accessed Amazon WorkLink.

    - **Username** *(string) --*

      The user name associated with the device.
    """


_ClientDescribeDomainResponseTypeDef = TypedDict(
    "_ClientDescribeDomainResponseTypeDef",
    {
        "DomainName": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "DomainStatus": str,
        "AcmCertificateArn": str,
    },
    total=False,
)


class ClientDescribeDomainResponseTypeDef(_ClientDescribeDomainResponseTypeDef):
    """
    Type definition for `ClientDescribeDomain` `Response`

    - **DomainName** *(string) --*

      The name of the domain.

    - **DisplayName** *(string) --*

      The name to display.

    - **CreatedTime** *(datetime) --*

      The time that the domain was added.

    - **DomainStatus** *(string) --*

      The current state for the domain.

    - **AcmCertificateArn** *(string) --*

      The ARN of an issued ACM certificate that is valid for the domain being associated.
    """


_ClientDescribeFleetMetadataResponseTypeDef = TypedDict(
    "_ClientDescribeFleetMetadataResponseTypeDef",
    {
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "OptimizeForEndUserLocation": bool,
        "CompanyCode": str,
        "FleetStatus": str,
    },
    total=False,
)


class ClientDescribeFleetMetadataResponseTypeDef(
    _ClientDescribeFleetMetadataResponseTypeDef
):
    """
    Type definition for `ClientDescribeFleetMetadata` `Response`

    - **CreatedTime** *(datetime) --*

      The time that the fleet was created.

    - **LastUpdatedTime** *(datetime) --*

      The time that the fleet was last updated.

    - **FleetName** *(string) --*

      The name of the fleet.

    - **DisplayName** *(string) --*

      The name to display.

    - **OptimizeForEndUserLocation** *(boolean) --*

      The option to optimize for better performance by routing traffic through the closest AWS
      Region to users, which may be outside of your home Region.

    - **CompanyCode** *(string) --*

      The identifier used by users to sign in to the Amazon WorkLink app.

    - **FleetStatus** *(string) --*

      The current state of the fleet.
    """


_ClientDescribeIdentityProviderConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeIdentityProviderConfigurationResponseTypeDef",
    {
        "IdentityProviderType": str,
        "ServiceProviderSamlMetadata": str,
        "IdentityProviderSamlMetadata": str,
    },
    total=False,
)


class ClientDescribeIdentityProviderConfigurationResponseTypeDef(
    _ClientDescribeIdentityProviderConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeIdentityProviderConfiguration` `Response`

    - **IdentityProviderType** *(string) --*

      The type of identity provider.

    - **ServiceProviderSamlMetadata** *(string) --*

      The SAML metadata document uploaded to the user’s identity provider.

    - **IdentityProviderSamlMetadata** *(string) --*

      The SAML metadata document provided by the user’s identity provider.
    """


_ClientDescribeWebsiteCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientDescribeWebsiteCertificateAuthorityResponseTypeDef",
    {"Certificate": str, "CreatedTime": datetime, "DisplayName": str},
    total=False,
)


class ClientDescribeWebsiteCertificateAuthorityResponseTypeDef(
    _ClientDescribeWebsiteCertificateAuthorityResponseTypeDef
):
    """
    Type definition for `ClientDescribeWebsiteCertificateAuthority` `Response`

    - **Certificate** *(string) --*

      The root certificate of the certificate authority.

    - **CreatedTime** *(datetime) --*

      The time that the certificate authority was added.

    - **DisplayName** *(string) --*

      The certificate name to display.
    """


_ClientListDevicesResponseDevicesTypeDef = TypedDict(
    "_ClientListDevicesResponseDevicesTypeDef",
    {"DeviceId": str, "DeviceStatus": str},
    total=False,
)


class ClientListDevicesResponseDevicesTypeDef(_ClientListDevicesResponseDevicesTypeDef):
    """
    Type definition for `ClientListDevicesResponse` `Devices`

    The summary of devices.

    - **DeviceId** *(string) --*

      The ID of the device.

    - **DeviceStatus** *(string) --*

      The status of the device.
    """


_ClientListDevicesResponseTypeDef = TypedDict(
    "_ClientListDevicesResponseTypeDef",
    {"Devices": List[ClientListDevicesResponseDevicesTypeDef], "NextToken": str},
    total=False,
)


class ClientListDevicesResponseTypeDef(_ClientListDevicesResponseTypeDef):
    """
    Type definition for `ClientListDevices` `Response`

    - **Devices** *(list) --*

      Information about the devices.

      - *(dict) --*

        The summary of devices.

        - **DeviceId** *(string) --*

          The ID of the device.

        - **DeviceStatus** *(string) --*

          The status of the device.

    - **NextToken** *(string) --*

      The pagination token used to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientListDomainsResponseDomainsTypeDef = TypedDict(
    "_ClientListDomainsResponseDomainsTypeDef",
    {
        "DomainName": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "DomainStatus": str,
    },
    total=False,
)


class ClientListDomainsResponseDomainsTypeDef(_ClientListDomainsResponseDomainsTypeDef):
    """
    Type definition for `ClientListDomainsResponse` `Domains`

    The summary of the domain.

    - **DomainName** *(string) --*

      The name of the domain.

    - **DisplayName** *(string) --*

      The name to display.

    - **CreatedTime** *(datetime) --*

      The time that the domain was created.

    - **DomainStatus** *(string) --*

      The status of the domain.
    """


_ClientListDomainsResponseTypeDef = TypedDict(
    "_ClientListDomainsResponseTypeDef",
    {"Domains": List[ClientListDomainsResponseDomainsTypeDef], "NextToken": str},
    total=False,
)


class ClientListDomainsResponseTypeDef(_ClientListDomainsResponseTypeDef):
    """
    Type definition for `ClientListDomains` `Response`

    - **Domains** *(list) --*

      Information about the domains.

      - *(dict) --*

        The summary of the domain.

        - **DomainName** *(string) --*

          The name of the domain.

        - **DisplayName** *(string) --*

          The name to display.

        - **CreatedTime** *(datetime) --*

          The time that the domain was created.

        - **DomainStatus** *(string) --*

          The status of the domain.

    - **NextToken** *(string) --*

      The pagination token used to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientListFleetsResponseFleetSummaryListTypeDef = TypedDict(
    "_ClientListFleetsResponseFleetSummaryListTypeDef",
    {
        "FleetArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "CompanyCode": str,
        "FleetStatus": str,
    },
    total=False,
)


class ClientListFleetsResponseFleetSummaryListTypeDef(
    _ClientListFleetsResponseFleetSummaryListTypeDef
):
    """
    Type definition for `ClientListFleetsResponse` `FleetSummaryList`

    The summary of the fleet.

    - **FleetArn** *(string) --*

      The ARN of the fleet.

    - **CreatedTime** *(datetime) --*

      The time when the fleet was created.

    - **LastUpdatedTime** *(datetime) --*

      The time when the fleet was last updated.

    - **FleetName** *(string) --*

      The name of the fleet.

    - **DisplayName** *(string) --*

      The name to display.

    - **CompanyCode** *(string) --*

      The identifier used by users to sign into the Amazon WorkLink app.

    - **FleetStatus** *(string) --*

      The status of the fleet.
    """


_ClientListFleetsResponseTypeDef = TypedDict(
    "_ClientListFleetsResponseTypeDef",
    {
        "FleetSummaryList": List[ClientListFleetsResponseFleetSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListFleetsResponseTypeDef(_ClientListFleetsResponseTypeDef):
    """
    Type definition for `ClientListFleets` `Response`

    - **FleetSummaryList** *(list) --*

      The summary list of the fleets.

      - *(dict) --*

        The summary of the fleet.

        - **FleetArn** *(string) --*

          The ARN of the fleet.

        - **CreatedTime** *(datetime) --*

          The time when the fleet was created.

        - **LastUpdatedTime** *(datetime) --*

          The time when the fleet was last updated.

        - **FleetName** *(string) --*

          The name of the fleet.

        - **DisplayName** *(string) --*

          The name to display.

        - **CompanyCode** *(string) --*

          The identifier used by users to sign into the Amazon WorkLink app.

        - **FleetStatus** *(string) --*

          The status of the fleet.

    - **NextToken** *(string) --*

      The pagination token used to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """


_ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef = TypedDict(
    "_ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef",
    {
        "AuthorizationProviderId": str,
        "AuthorizationProviderType": str,
        "DomainName": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef(
    _ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef
):
    """
    Type definition for `ClientListWebsiteAuthorizationProvidersResponse` `WebsiteAuthorizationProviders`

    The summary of the website authorization provider.

    - **AuthorizationProviderId** *(string) --*

      A unique identifier for the authorization provider.

    - **AuthorizationProviderType** *(string) --*

      The authorization provider type.

    - **DomainName** *(string) --*

      The domain name of the authorization provider. This applies only to SAML-based
      authorization providers.

    - **CreatedTime** *(datetime) --*

      The time of creation.
    """


_ClientListWebsiteAuthorizationProvidersResponseTypeDef = TypedDict(
    "_ClientListWebsiteAuthorizationProvidersResponseTypeDef",
    {
        "WebsiteAuthorizationProviders": List[
            ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListWebsiteAuthorizationProvidersResponseTypeDef(
    _ClientListWebsiteAuthorizationProvidersResponseTypeDef
):
    """
    Type definition for `ClientListWebsiteAuthorizationProviders` `Response`

    - **WebsiteAuthorizationProviders** *(list) --*

      The website authorization providers.

      - *(dict) --*

        The summary of the website authorization provider.

        - **AuthorizationProviderId** *(string) --*

          A unique identifier for the authorization provider.

        - **AuthorizationProviderType** *(string) --*

          The authorization provider type.

        - **DomainName** *(string) --*

          The domain name of the authorization provider. This applies only to SAML-based
          authorization providers.

        - **CreatedTime** *(datetime) --*

          The time of creation.

    - **NextToken** *(string) --*

      The pagination token to use to retrieve the next page of results for this operation. If this
      value is null, it retrieves the first page.
    """


_ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef = TypedDict(
    "_ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef",
    {"WebsiteCaId": str, "CreatedTime": datetime, "DisplayName": str},
    total=False,
)


class ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef(
    _ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef
):
    """
    Type definition for `ClientListWebsiteCertificateAuthoritiesResponse` `WebsiteCertificateAuthorities`

    The summary of the certificate authority (CA).

    - **WebsiteCaId** *(string) --*

      A unique identifier for the CA.

    - **CreatedTime** *(datetime) --*

      The time when the CA was added.

    - **DisplayName** *(string) --*

      The name to display.
    """


_ClientListWebsiteCertificateAuthoritiesResponseTypeDef = TypedDict(
    "_ClientListWebsiteCertificateAuthoritiesResponseTypeDef",
    {
        "WebsiteCertificateAuthorities": List[
            ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListWebsiteCertificateAuthoritiesResponseTypeDef(
    _ClientListWebsiteCertificateAuthoritiesResponseTypeDef
):
    """
    Type definition for `ClientListWebsiteCertificateAuthorities` `Response`

    - **WebsiteCertificateAuthorities** *(list) --*

      Information about the certificates.

      - *(dict) --*

        The summary of the certificate authority (CA).

        - **WebsiteCaId** *(string) --*

          A unique identifier for the CA.

        - **CreatedTime** *(datetime) --*

          The time when the CA was added.

        - **DisplayName** *(string) --*

          The name to display.

    - **NextToken** *(string) --*

      The pagination token used to retrieve the next page of results for this operation. If there
      are no more pages, this value is null.
    """
