"Main interface for worklink Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_worklink.client as client_scope
from mypy_boto3_worklink.type_defs import (
    ClientAssociateWebsiteAuthorizationProviderResponseTypeDef,
    ClientAssociateWebsiteCertificateAuthorityResponseTypeDef,
    ClientCreateFleetResponseTypeDef,
    ClientDescribeAuditStreamConfigurationResponseTypeDef,
    ClientDescribeCompanyNetworkConfigurationResponseTypeDef,
    ClientDescribeDevicePolicyConfigurationResponseTypeDef,
    ClientDescribeDeviceResponseTypeDef,
    ClientDescribeDomainResponseTypeDef,
    ClientDescribeFleetMetadataResponseTypeDef,
    ClientDescribeIdentityProviderConfigurationResponseTypeDef,
    ClientDescribeWebsiteCertificateAuthorityResponseTypeDef,
    ClientListDevicesResponseTypeDef,
    ClientListDomainsResponseTypeDef,
    ClientListFleetsResponseTypeDef,
    ClientListWebsiteAuthorizationProvidersResponseTypeDef,
    ClientListWebsiteCertificateAuthoritiesResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_domain(
        self,
        FleetArn: str,
        DomainName: str,
        AcmCertificateArn: str,
        DisplayName: str = None,
    ) -> Dict[str, Any]:
        """
        Specifies a domain to be associated to Amazon WorkLink.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/AssociateDomain>`_

        **Request Syntax**
        ::

          response = client.associate_domain(
              FleetArn='string',
              DomainName='string',
              DisplayName='string',
              AcmCertificateArn='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the fleet.

        :type DomainName: string
        :param DomainName: **[REQUIRED]**

          The fully qualified domain name (FQDN).

        :type DisplayName: string
        :param DisplayName:

          The name to display.

        :type AcmCertificateArn: string
        :param AcmCertificateArn: **[REQUIRED]**

          The ARN of an issued ACM certificate that is valid for the domain being associated.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_website_authorization_provider(
        self, FleetArn: str, AuthorizationProviderType: str, DomainName: str = None
    ) -> ClientAssociateWebsiteAuthorizationProviderResponseTypeDef:
        """
        Associates a website authorization provider with a specified fleet. This is used to authorize users
        against associated websites in the company network.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/AssociateWebsiteAuthorizationProvider>`_
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/AssociateWebsiteAuthorizationProvider>`_

        **Request Syntax**
        ::

          response = client.associate_website_authorization_provider(
              FleetArn='string',
              AuthorizationProviderType='SAML',
              DomainName='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type AuthorizationProviderType: string
        :param AuthorizationProviderType: **[REQUIRED]**

          The authorization provider type.

        :type DomainName: string
        :param DomainName:

          The domain name of the authorization provider. This applies only to SAML-based authorization
          providers.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AuthorizationProviderId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **AuthorizationProviderId** *(string) --*

              A unique identifier for the authorization provider.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_website_certificate_authority(
        self, FleetArn: str, Certificate: str, DisplayName: str = None
    ) -> ClientAssociateWebsiteCertificateAuthorityResponseTypeDef:
        """
        Imports the root certificate of a certificate authority (CA) used to obtain TLS certificates used
        by associated websites within the company network.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/AssociateWebsiteCertificateAuthority>`_

        **Request Syntax**
        ::

          response = client.associate_website_certificate_authority(
              FleetArn='string',
              Certificate='string',
              DisplayName='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type Certificate: string
        :param Certificate: **[REQUIRED]**

          The root certificate of the CA.

        :type DisplayName: string
        :param DisplayName:

          The certificate name to display.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'WebsiteCaId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **WebsiteCaId** *(string) --*

              A unique identifier for the CA.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_fleet(
        self,
        FleetName: str,
        DisplayName: str = None,
        OptimizeForEndUserLocation: bool = None,
    ) -> ClientCreateFleetResponseTypeDef:
        """
        Creates a fleet. A fleet consists of resources and the configuration that delivers associated
        websites to authorized users who download and set up the Amazon WorkLink app.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/CreateFleet>`_

        **Request Syntax**
        ::

          response = client.create_fleet(
              FleetName='string',
              DisplayName='string',
              OptimizeForEndUserLocation=True|False
          )
        :type FleetName: string
        :param FleetName: **[REQUIRED]**

          A unique name for the fleet.

        :type DisplayName: string
        :param DisplayName:

          The fleet name to display.

        :type OptimizeForEndUserLocation: boolean
        :param OptimizeForEndUserLocation:

          The option to optimize for better performance by routing traffic through the closest AWS Region
          to users, which may be outside of your home Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FleetArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **FleetArn** *(string) --*

              The ARN of the fleet.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_fleet(self, FleetArn: str) -> Dict[str, Any]:
        """
        Deletes a fleet. Prevents users from accessing previously associated websites.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DeleteFleet>`_

        **Request Syntax**
        ::

          response = client.delete_fleet(
              FleetArn='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_audit_stream_configuration(
        self, FleetArn: str
    ) -> ClientDescribeAuditStreamConfigurationResponseTypeDef:
        """
        Describes the configuration for delivering audit streams to the customer account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeAuditStreamConfiguration>`_

        **Request Syntax**
        ::

          response = client.describe_audit_stream_configuration(
              FleetArn='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AuditStreamArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **AuditStreamArn** *(string) --*

              The ARN of the Amazon Kinesis data stream that will receive the audit events.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_company_network_configuration(
        self, FleetArn: str
    ) -> ClientDescribeCompanyNetworkConfigurationResponseTypeDef:
        """
        Describes the networking configuration to access the internal websites associated with the
        specified fleet.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeCompanyNetworkConfiguration>`_

        **Request Syntax**
        ::

          response = client.describe_company_network_configuration(
              FleetArn='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VpcId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **VpcId** *(string) --*

              The VPC with connectivity to associated websites.

            - **SubnetIds** *(list) --*

              The subnets used for X-ENI connections from Amazon WorkLink rendering containers.

              - *(string) --*

            - **SecurityGroupIds** *(list) --*

              The security groups associated with access to the provided subnets.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_device(
        self, FleetArn: str, DeviceId: str
    ) -> ClientDescribeDeviceResponseTypeDef:
        """
        Provides information about a user's device.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeDevice>`_

        **Request Syntax**
        ::

          response = client.describe_device(
              FleetArn='string',
              DeviceId='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type DeviceId: string
        :param DeviceId: **[REQUIRED]**

          A unique identifier for a registered user's device.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Status': 'ACTIVE'|'SIGNED_OUT',
                'Model': 'string',
                'Manufacturer': 'string',
                'OperatingSystem': 'string',
                'OperatingSystemVersion': 'string',
                'PatchLevel': 'string',
                'FirstAccessedTime': datetime(2015, 1, 1),
                'LastAccessedTime': datetime(2015, 1, 1),
                'Username': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_device_policy_configuration(
        self, FleetArn: str
    ) -> ClientDescribeDevicePolicyConfigurationResponseTypeDef:
        """
        Describes the device policy configuration for the specified fleet.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeDevicePolicyConfiguration>`_

        **Request Syntax**
        ::

          response = client.describe_device_policy_configuration(
              FleetArn='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DeviceCaCertificate': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DeviceCaCertificate** *(string) --*

              The certificate chain, including intermediate certificates and the root certificate authority
              certificate used to issue device certificates.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_domain(
        self, FleetArn: str, DomainName: str
    ) -> ClientDescribeDomainResponseTypeDef:
        """
        Provides information about the domain.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeDomain>`_

        **Request Syntax**
        ::

          response = client.describe_domain(
              FleetArn='string',
              DomainName='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type DomainName: string
        :param DomainName: **[REQUIRED]**

          The name of the domain.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DomainName': 'string',
                'DisplayName': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'DomainStatus':
                'PENDING_VALIDATION'|'ASSOCIATING'|'ACTIVE'|'INACTIVE'|'DISASSOCIATING'|'DISASSOCIATED'
                |'FAILED_TO_ASSOCIATE'|'FAILED_TO_DISASSOCIATE',
                'AcmCertificateArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleet_metadata(
        self, FleetArn: str
    ) -> ClientDescribeFleetMetadataResponseTypeDef:
        """
        Provides basic information for the specified fleet, excluding identity provider, networking, and
        device configuration details.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeFleetMetadata>`_

        **Request Syntax**
        ::

          response = client.describe_fleet_metadata(
              FleetArn='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CreatedTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'FleetName': 'string',
                'DisplayName': 'string',
                'OptimizeForEndUserLocation': True|False,
                'CompanyCode': 'string',
                'FleetStatus':
                'CREATING'|'ACTIVE'|'DELETING'|'DELETED'|'FAILED_TO_CREATE'|'FAILED_TO_DELETE'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_identity_provider_configuration(
        self, FleetArn: str
    ) -> ClientDescribeIdentityProviderConfigurationResponseTypeDef:
        """
        Describes the identity provider configuration of the specified fleet.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeIdentityProviderConfiguration>`_
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeIdentityProviderConfiguration>`_

        **Request Syntax**
        ::

          response = client.describe_identity_provider_configuration(
              FleetArn='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IdentityProviderType': 'SAML',
                'ServiceProviderSamlMetadata': 'string',
                'IdentityProviderSamlMetadata': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **IdentityProviderType** *(string) --*

              The type of identity provider.

            - **ServiceProviderSamlMetadata** *(string) --*

              The SAML metadata document uploaded to the user’s identity provider.

            - **IdentityProviderSamlMetadata** *(string) --*

              The SAML metadata document provided by the user’s identity provider.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_website_certificate_authority(
        self, FleetArn: str, WebsiteCaId: str
    ) -> ClientDescribeWebsiteCertificateAuthorityResponseTypeDef:
        """
        Provides information about the certificate authority.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeWebsiteCertificateAuthority>`_

        **Request Syntax**
        ::

          response = client.describe_website_certificate_authority(
              FleetArn='string',
              WebsiteCaId='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type WebsiteCaId: string
        :param WebsiteCaId: **[REQUIRED]**

          A unique identifier for the certificate authority.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Certificate': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'DisplayName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Certificate** *(string) --*

              The root certificate of the certificate authority.

            - **CreatedTime** *(datetime) --*

              The time that the certificate authority was added.

            - **DisplayName** *(string) --*

              The certificate name to display.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_domain(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        Disassociates a domain from Amazon WorkLink. End users lose the ability to access the domain with
        Amazon WorkLink.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DisassociateDomain>`_

        **Request Syntax**
        ::

          response = client.disassociate_domain(
              FleetArn='string',
              DomainName='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type DomainName: string
        :param DomainName: **[REQUIRED]**

          The name of the domain.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_website_authorization_provider(
        self, FleetArn: str, AuthorizationProviderId: str
    ) -> Dict[str, Any]:
        """
        Disassociates a website authorization provider from a specified fleet. After the disassociation,
        users can't load any associated websites that require this authorization provider.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DisassociateWebsiteAuthorizationProvider>`_
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DisassociateWebsiteAuthorizationProvider>`_

        **Request Syntax**
        ::

          response = client.disassociate_website_authorization_provider(
              FleetArn='string',
              AuthorizationProviderId='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type AuthorizationProviderId: string
        :param AuthorizationProviderId: **[REQUIRED]**

          A unique identifier for the authorization provider.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_website_certificate_authority(
        self, FleetArn: str, WebsiteCaId: str
    ) -> Dict[str, Any]:
        """
        Removes a certificate authority (CA).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DisassociateWebsiteCertificateAuthority>`_
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DisassociateWebsiteCertificateAuthority>`_

        **Request Syntax**
        ::

          response = client.disassociate_website_certificate_authority(
              FleetArn='string',
              WebsiteCaId='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type WebsiteCaId: string
        :param WebsiteCaId: **[REQUIRED]**

          A unique identifier for the CA.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_devices(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDevicesResponseTypeDef:
        """
        Retrieves a list of devices registered with the specified fleet.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/ListDevices>`_

        **Request Syntax**
        ::

          response = client.list_devices(
              FleetArn='string',
              NextToken='string',
              MaxResults=123
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type NextToken: string
        :param NextToken:

          The pagination token used to retrieve the next page of results for this operation. If this value
          is null, it retrieves the first page.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to be included in the next page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Devices': [
                    {
                        'DeviceId': 'string',
                        'DeviceStatus': 'ACTIVE'|'SIGNED_OUT'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_domains(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDomainsResponseTypeDef:
        """
        Retrieves a list of domains associated to a specified fleet.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/ListDomains>`_

        **Request Syntax**
        ::

          response = client.list_domains(
              FleetArn='string',
              NextToken='string',
              MaxResults=123
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type NextToken: string
        :param NextToken:

          The pagination token used to retrieve the next page of results for this operation. If this value
          is null, it retrieves the first page.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to be included in the next page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Domains': [
                    {
                        'DomainName': 'string',
                        'DisplayName': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'DomainStatus':
                        'PENDING_VALIDATION'|'ASSOCIATING'|'ACTIVE'|'INACTIVE'|'DISASSOCIATING'
                        |'DISASSOCIATED'|'FAILED_TO_ASSOCIATE'|'FAILED_TO_DISASSOCIATE'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_fleets(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListFleetsResponseTypeDef:
        """
        Retrieves a list of fleets for the current account and Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/ListFleets>`_

        **Request Syntax**
        ::

          response = client.list_fleets(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          The pagination token used to retrieve the next page of results for this operation. If this value
          is null, it retrieves the first page.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to be included in the next page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FleetSummaryList': [
                    {
                        'FleetArn': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1),
                        'FleetName': 'string',
                        'DisplayName': 'string',
                        'CompanyCode': 'string',
                        'FleetStatus':
                        'CREATING'|'ACTIVE'|'DELETING'|'DELETED'|'FAILED_TO_CREATE'|'FAILED_TO_DELETE'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_website_authorization_providers(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListWebsiteAuthorizationProvidersResponseTypeDef:
        """
        Retrieves a list of website authorization providers associated with a specified fleet.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/ListWebsiteAuthorizationProviders>`_

        **Request Syntax**
        ::

          response = client.list_website_authorization_providers(
              FleetArn='string',
              NextToken='string',
              MaxResults=123
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type NextToken: string
        :param NextToken:

          The pagination token to use to retrieve the next page of results for this operation. If this
          value is null, it retrieves the first page.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to be included in the next page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'WebsiteAuthorizationProviders': [
                    {
                        'AuthorizationProviderId': 'string',
                        'AuthorizationProviderType': 'SAML',
                        'DomainName': 'string',
                        'CreatedTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_website_certificate_authorities(
        self, FleetArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListWebsiteCertificateAuthoritiesResponseTypeDef:
        """
        Retrieves a list of certificate authorities added for the current account and Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/ListWebsiteCertificateAuthorities>`_

        **Request Syntax**
        ::

          response = client.list_website_certificate_authorities(
              FleetArn='string',
              MaxResults=123,
              NextToken='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to be included in the next page.

        :type NextToken: string
        :param NextToken:

          The pagination token used to retrieve the next page of results for this operation. If this value
          is null, it retrieves the first page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'WebsiteCertificateAuthorities': [
                    {
                        'WebsiteCaId': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'DisplayName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_domain_access(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        Moves a domain to ACTIVE status if it was in the INACTIVE status.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/RestoreDomainAccess>`_

        **Request Syntax**
        ::

          response = client.restore_domain_access(
              FleetArn='string',
              DomainName='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type DomainName: string
        :param DomainName: **[REQUIRED]**

          The name of the domain.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_domain_access(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        Moves a domain to INACTIVE status if it was in the ACTIVE status.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/RevokeDomainAccess>`_

        **Request Syntax**
        ::

          response = client.revoke_domain_access(
              FleetArn='string',
              DomainName='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type DomainName: string
        :param DomainName: **[REQUIRED]**

          The name of the domain.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def sign_out_user(self, FleetArn: str, Username: str) -> Dict[str, Any]:
        """
        Signs the user out from all of their devices. The user can sign in again if they have valid
        credentials.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/SignOutUser>`_

        **Request Syntax**
        ::

          response = client.sign_out_user(
              FleetArn='string',
              Username='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type Username: string
        :param Username: **[REQUIRED]**

          The name of the user.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_audit_stream_configuration(
        self, FleetArn: str, AuditStreamArn: str = None
    ) -> Dict[str, Any]:
        """
        Updates the audit stream configuration for the fleet.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateAuditStreamConfiguration>`_

        **Request Syntax**
        ::

          response = client.update_audit_stream_configuration(
              FleetArn='string',
              AuditStreamArn='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type AuditStreamArn: string
        :param AuditStreamArn:

          The ARN of the Amazon Kinesis data stream that receives the audit events.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_company_network_configuration(
        self,
        FleetArn: str,
        VpcId: str,
        SubnetIds: List[str],
        SecurityGroupIds: List[str],
    ) -> Dict[str, Any]:
        """
        Updates the company network configuration for the fleet.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateCompanyNetworkConfiguration>`_

        **Request Syntax**
        ::

          response = client.update_company_network_configuration(
              FleetArn='string',
              VpcId='string',
              SubnetIds=[
                  'string',
              ],
              SecurityGroupIds=[
                  'string',
              ]
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type VpcId: string
        :param VpcId: **[REQUIRED]**

          The VPC with connectivity to associated websites.

        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]**

          The subnets used for X-ENI connections from Amazon WorkLink rendering containers.

          - *(string) --*

        :type SecurityGroupIds: list
        :param SecurityGroupIds: **[REQUIRED]**

          The security groups associated with access to the provided subnets.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_device_policy_configuration(
        self, FleetArn: str, DeviceCaCertificate: str = None
    ) -> Dict[str, Any]:
        """
        Updates the device policy configuration for the fleet.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateDevicePolicyConfiguration>`_

        **Request Syntax**
        ::

          response = client.update_device_policy_configuration(
              FleetArn='string',
              DeviceCaCertificate='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type DeviceCaCertificate: string
        :param DeviceCaCertificate:

          The certificate chain, including intermediate certificates and the root certificate authority
          certificate used to issue device certificates.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_domain_metadata(
        self, FleetArn: str, DomainName: str, DisplayName: str = None
    ) -> Dict[str, Any]:
        """
        Updates domain metadata, such as DisplayName.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateDomainMetadata>`_

        **Request Syntax**
        ::

          response = client.update_domain_metadata(
              FleetArn='string',
              DomainName='string',
              DisplayName='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type DomainName: string
        :param DomainName: **[REQUIRED]**

          The name of the domain.

        :type DisplayName: string
        :param DisplayName:

          The name to display.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_fleet_metadata(
        self,
        FleetArn: str,
        DisplayName: str = None,
        OptimizeForEndUserLocation: bool = None,
    ) -> Dict[str, Any]:
        """
        Updates fleet metadata, such as DisplayName.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateFleetMetadata>`_

        **Request Syntax**
        ::

          response = client.update_fleet_metadata(
              FleetArn='string',
              DisplayName='string',
              OptimizeForEndUserLocation=True|False
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type DisplayName: string
        :param DisplayName:

          The fleet name to display. The existing DisplayName is unset if null is passed.

        :type OptimizeForEndUserLocation: boolean
        :param OptimizeForEndUserLocation:

          The option to optimize for better performance by routing traffic through the closest AWS Region
          to users, which may be outside of your home Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_identity_provider_configuration(
        self,
        FleetArn: str,
        IdentityProviderType: str,
        IdentityProviderSamlMetadata: str = None,
    ) -> Dict[str, Any]:
        """
        Updates the identity provider configuration for the fleet.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateIdentityProviderConfiguration>`_

        **Request Syntax**
        ::

          response = client.update_identity_provider_configuration(
              FleetArn='string',
              IdentityProviderType='SAML',
              IdentityProviderSamlMetadata='string'
          )
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**

          The ARN of the fleet.

        :type IdentityProviderType: string
        :param IdentityProviderType: **[REQUIRED]**

          The type of identity provider.

        :type IdentityProviderSamlMetadata: string
        :param IdentityProviderSamlMetadata:

          The SAML metadata document provided by the customer’s identity provider. The existing
          IdentityProviderSamlMetadata is unset if null is passed.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
