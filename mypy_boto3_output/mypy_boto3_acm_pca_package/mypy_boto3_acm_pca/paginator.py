"Main interface for acm-pca Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_acm_pca.type_defs import (
    ListCertificateAuthoritiesPaginatePaginationConfigTypeDef,
    ListCertificateAuthoritiesPaginateResponseTypeDef,
    ListPermissionsPaginatePaginationConfigTypeDef,
    ListPermissionsPaginateResponseTypeDef,
    ListTagsPaginatePaginationConfigTypeDef,
    ListTagsPaginateResponseTypeDef,
)


__all__ = (
    "ListCertificateAuthoritiesPaginator",
    "ListPermissionsPaginator",
    "ListTagsPaginator",
)


class ListCertificateAuthoritiesPaginator(Boto3Paginator):
    """
    Paginator for `list_certificate_authorities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListCertificateAuthoritiesPaginatePaginationConfigTypeDef = None,
    ) -> ListCertificateAuthoritiesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ACMPCA.Client.list_certificate_authorities`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/ListCertificateAuthorities>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CertificateAuthorities': [
                    {
                        'Arn': 'string',
                        'CreatedAt': datetime(2015, 1, 1),
                        'LastStateChangeAt': datetime(2015, 1, 1),
                        'Type': 'ROOT'|'SUBORDINATE',
                        'Serial': 'string',
                        'Status':
                        'CREATING'|'PENDING_CERTIFICATE'|'ACTIVE'|'DELETED'|'DISABLED'|'EXPIRED'|'FAILED',
                        'NotBefore': datetime(2015, 1, 1),
                        'NotAfter': datetime(2015, 1, 1),
                        'FailureReason': 'REQUEST_TIMED_OUT'|'UNSUPPORTED_ALGORITHM'|'OTHER',
                        'CertificateAuthorityConfiguration': {
                            'KeyAlgorithm': 'RSA_2048'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1',
                            'SigningAlgorithm':
                            'SHA256WITHECDSA'|'SHA384WITHECDSA'|'SHA512WITHECDSA'|'SHA256WITHRSA'
                            |'SHA384WITHRSA'|'SHA512WITHRSA',
                            'Subject': {
                                'Country': 'string',
                                'Organization': 'string',
                                'OrganizationalUnit': 'string',
                                'DistinguishedNameQualifier': 'string',
                                'State': 'string',
                                'CommonName': 'string',
                                'SerialNumber': 'string',
                                'Locality': 'string',
                                'Title': 'string',
                                'Surname': 'string',
                                'GivenName': 'string',
                                'Initials': 'string',
                                'Pseudonym': 'string',
                                'GenerationQualifier': 'string'
                            }
                        },
                        'RevocationConfiguration': {
                            'CrlConfiguration': {
                                'Enabled': True|False,
                                'ExpirationInDays': 123,
                                'CustomCname': 'string',
                                'S3BucketName': 'string'
                            }
                        },
                        'RestorableUntil': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **CertificateAuthorities** *(list) --*

              Summary information about each certificate authority you have created.

              - *(dict) --*

                Contains information about your private certificate authority (CA). Your private CA can
                issue and revoke X.509 digital certificates. Digital certificates verify that the entity
                named in the certificate **Subject** field owns or controls the public key contained in the
                **Subject Public Key Info** field. Call the  CreateCertificateAuthority action to create
                your private CA. You must then call the  GetCertificateAuthorityCertificate action to
                retrieve a private CA certificate signing request (CSR). Sign the CSR with your ACM Private
                CA-hosted or on-premises root or subordinate CA certificate. Call the
                ImportCertificateAuthorityCertificate action to import the signed certificate into AWS
                Certificate Manager (ACM).

                - **Arn** *(string) --*

                  Amazon Resource Name (ARN) for your private certificate authority (CA). The format is ``
                  *12345678-1234-1234-1234-123456789012* `` .

                - **CreatedAt** *(datetime) --*

                  Date and time at which your private CA was created.

                - **LastStateChangeAt** *(datetime) --*

                  Date and time at which your private CA was last updated.

                - **Type** *(string) --*

                  Type of your private CA.

                - **Serial** *(string) --*

                  Serial number of your private CA.

                - **Status** *(string) --*

                  Status of your private CA.

                - **NotBefore** *(datetime) --*

                  Date and time before which your private CA certificate is not valid.

                - **NotAfter** *(datetime) --*

                  Date and time after which your private CA certificate is not valid.

                - **FailureReason** *(string) --*

                  Reason the request to create your private CA failed.

                - **CertificateAuthorityConfiguration** *(dict) --*

                  Your private CA configuration.

                  - **KeyAlgorithm** *(string) --*

                    Type of the public key algorithm and size, in bits, of the key pair that your CA
                    creates when it issues a certificate. When you create a subordinate CA, you must use a
                    key algorithm supported by the parent CA.

                  - **SigningAlgorithm** *(string) --*

                    Name of the algorithm your private CA uses to sign certificate requests.

                  - **Subject** *(dict) --*

                    Structure that contains X.500 distinguished name information for your private CA.

                    - **Country** *(string) --*

                      Two-digit code that specifies the country in which the certificate subject located.

                    - **Organization** *(string) --*

                      Legal name of the organization with which the certificate subject is affiliated.

                    - **OrganizationalUnit** *(string) --*

                      A subdivision or unit of the organization (such as sales or finance) with which the
                      certificate subject is affiliated.

                    - **DistinguishedNameQualifier** *(string) --*

                      Disambiguating information for the certificate subject.

                    - **State** *(string) --*

                      State in which the subject of the certificate is located.

                    - **CommonName** *(string) --*

                      Fully qualified domain name (FQDN) associated with the certificate subject.

                    - **SerialNumber** *(string) --*

                      The certificate serial number.

                    - **Locality** *(string) --*

                      The locality (such as a city or town) in which the certificate subject is located.

                    - **Title** *(string) --*

                      A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the
                      certificate subject.

                    - **Surname** *(string) --*

                      Family name. In the US and the UK, for example, the surname of an individual is
                      ordered last. In Asian cultures the surname is typically ordered first.

                    - **GivenName** *(string) --*

                      First name.

                    - **Initials** *(string) --*

                      Concatenation that typically contains the first letter of the **GivenName** , the
                      first letter of the middle name if one exists, and the first letter of the
                      **SurName** .

                    - **Pseudonym** *(string) --*

                      Typically a shortened version of a longer **GivenName** . For example, Jonathan is
                      often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

                    - **GenerationQualifier** *(string) --*

                      Typically a qualifier appended to the name of an individual. Examples include Jr. for
                      junior, Sr. for senior, and III for third.

                - **RevocationConfiguration** *(dict) --*

                  Information about the certificate revocation list (CRL) created and maintained by your
                  private CA.

                  - **CrlConfiguration** *(dict) --*

                    Configuration of the certificate revocation list (CRL), if any, maintained by your
                    private CA.

                    - **Enabled** *(boolean) --*

                      Boolean value that specifies whether certificate revocation lists (CRLs) are enabled.
                      You can use this value to enable certificate revocation for a new CA when you call
                      the  CreateCertificateAuthority action or for an existing CA when you call the
                      UpdateCertificateAuthority action.

                    - **ExpirationInDays** *(integer) --*

                      Number of days until a certificate expires.

                    - **CustomCname** *(string) --*

                      Name inserted into the certificate **CRL Distribution Points** extension that enables
                      the use of an alias for the CRL distribution point. Use this value if you don't want
                      the name of your S3 bucket to be public.

                    - **S3BucketName** *(string) --*

                      Name of the S3 bucket that contains the CRL. If you do not provide a value for the
                      **CustomCname** argument, the name of your S3 bucket is placed into the **CRL
                      Distribution Points** extension of the issued certificate. You can change the name of
                      your bucket by calling the  UpdateCertificateAuthority action. You must specify a
                      bucket policy that allows ACM Private CA to write the CRL to your bucket.

                - **RestorableUntil** *(datetime) --*

                  The period during which a deleted CA can be restored. For more information, see the
                  ``PermanentDeletionTimeInDays`` parameter of the  DeleteCertificateAuthorityRequest
                  action.

        """


class ListPermissionsPaginator(Boto3Paginator):
    """
    Paginator for `list_permissions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CertificateAuthorityArn: str,
        PaginationConfig: ListPermissionsPaginatePaginationConfigTypeDef = None,
    ) -> ListPermissionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ACMPCA.Client.list_permissions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/ListPermissions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CertificateAuthorityArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]**

          The Amazon Resource Number (ARN) of the private CA to inspect. You can find the ARN by calling
          the  ListCertificateAuthorities action. This must be of the form:
          ``arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012`` You
          can get a private CA's ARN by running the  ListCertificateAuthorities action.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Permissions': [
                    {
                        'CertificateAuthorityArn': 'string',
                        'CreatedAt': datetime(2015, 1, 1),
                        'Principal': 'string',
                        'SourceAccount': 'string',
                        'Actions': [
                            'IssueCertificate'|'GetCertificate'|'ListPermissions',
                        ],
                        'Policy': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Permissions** *(list) --*

              Summary information about each permission assigned by the specified private CA, including the
              action enabled, the policy provided, and the time of creation.

              - *(dict) --*

                Permissions designate which private CA actions can be performed by an AWS service or
                entity. In order for ACM to automatically renew private certificates, you must give the ACM
                service principal all available permissions (``IssueCertificate`` , ``GetCertificate`` ,
                and ``ListPermissions`` ). Permissions can be assigned with the  CreatePermission action,
                removed with the  DeletePermission action, and listed with the  ListPermissions action.

                - **CertificateAuthorityArn** *(string) --*

                  The Amazon Resource Number (ARN) of the private CA from which the permission was issued.

                - **CreatedAt** *(datetime) --*

                  The time at which the permission was created.

                - **Principal** *(string) --*

                  The AWS service or entity that holds the permission. At this time, the only valid
                  principal is ``acm.amazonaws.com`` .

                - **SourceAccount** *(string) --*

                  The ID of the account that assigned the permission.

                - **Actions** *(list) --*

                  The private CA actions that can be performed by the designated AWS service.

                  - *(string) --*

                - **Policy** *(string) --*

                  The name of the policy that is associated with the permission.

        """


class ListTagsPaginator(Boto3Paginator):
    """
    Paginator for `list_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CertificateAuthorityArn: str,
        PaginationConfig: ListTagsPaginatePaginationConfigTypeDef = None,
    ) -> ListTagsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ACMPCA.Client.list_tags`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/ListTags>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CertificateAuthorityArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that was returned when you called the  CreateCertificateAuthority
          action. This must be of the form:

           ``arn:aws:acm-pca:*region* :*account*
           :certificate-authority/*12345678-1234-1234-1234-123456789012* ``

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(list) --*

              The tags associated with your private CA.

              - *(dict) --*

                Tags are labels that you can use to identify and organize your private CAs. Each tag
                consists of a key and an optional value. You can associate up to 50 tags with a private CA.
                To add one or more tags to a private CA, call the  TagCertificateAuthority action. To
                remove a tag, call the  UntagCertificateAuthority action.

                - **Key** *(string) --*

                  Key (name) of the tag.

                - **Value** *(string) --*

                  Value of the tag.

        """
