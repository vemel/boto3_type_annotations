"Main interface for acm-pca type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "AuditReportCreatedWaitWaiterConfigTypeDef",
    "CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef",
    "CertificateIssuedWaitWaiterConfigTypeDef",
    "ClientCreateCertificateAuthorityAuditReportResponseTypeDef",
    "ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef",
    "ClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef",
    "ClientCreateCertificateAuthorityResponseTypeDef",
    "ClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    "ClientCreateCertificateAuthorityRevocationConfigurationTypeDef",
    "ClientCreateCertificateAuthorityTagsTypeDef",
    "ClientDescribeCertificateAuthorityAuditReportResponseTypeDef",
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef",
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef",
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef",
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef",
    "ClientDescribeCertificateAuthorityResponseTypeDef",
    "ClientGetCertificateAuthorityCertificateResponseTypeDef",
    "ClientGetCertificateAuthorityCsrResponseTypeDef",
    "ClientGetCertificateResponseTypeDef",
    "ClientIssueCertificateResponseTypeDef",
    "ClientIssueCertificateValidityTypeDef",
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef",
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef",
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef",
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef",
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef",
    "ClientListCertificateAuthoritiesResponseTypeDef",
    "ClientListPermissionsResponsePermissionsTypeDef",
    "ClientListPermissionsResponseTypeDef",
    "ClientListTagsResponseTagsTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientTagCertificateAuthorityTagsTypeDef",
    "ClientUntagCertificateAuthorityTagsTypeDef",
    "ClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    "ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef",
    "ListCertificateAuthoritiesPaginatePaginationConfigTypeDef",
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef",
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef",
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef",
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef",
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef",
    "ListCertificateAuthoritiesPaginateResponseTypeDef",
    "ListPermissionsPaginatePaginationConfigTypeDef",
    "ListPermissionsPaginateResponsePermissionsTypeDef",
    "ListPermissionsPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseTagsTypeDef",
    "ListTagsPaginateResponseTypeDef",
)


_AuditReportCreatedWaitWaiterConfigTypeDef = TypedDict(
    "_AuditReportCreatedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class AuditReportCreatedWaitWaiterConfigTypeDef(
    _AuditReportCreatedWaitWaiterConfigTypeDef
):
    """
    Type definition for `AuditReportCreatedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef = TypedDict(
    "_CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef(
    _CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef
):
    """
    Type definition for `CertificateAuthorityCsrCreatedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_CertificateIssuedWaitWaiterConfigTypeDef = TypedDict(
    "_CertificateIssuedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class CertificateIssuedWaitWaiterConfigTypeDef(
    _CertificateIssuedWaitWaiterConfigTypeDef
):
    """
    Type definition for `CertificateIssuedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_ClientCreateCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "_ClientCreateCertificateAuthorityAuditReportResponseTypeDef",
    {"AuditReportId": str, "S3Key": str},
    total=False,
)


class ClientCreateCertificateAuthorityAuditReportResponseTypeDef(
    _ClientCreateCertificateAuthorityAuditReportResponseTypeDef
):
    """
    Type definition for `ClientCreateCertificateAuthorityAuditReport` `Response`

    - **AuditReportId** *(string) --*

      An alphanumeric string that contains a report identifier.

    - **S3Key** *(string) --*

      The **key** that uniquely identifies the report file in your S3 bucket.
    """


_ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "_ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
    },
    total=False,
)


class ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef(
    _ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef
):
    """
    Type definition for `ClientCreateCertificateAuthorityCertificateAuthorityConfiguration` `Subject`

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

      Family name. In the US and the UK, for example, the surname of an individual is ordered last.
      In Asian cultures the surname is typically ordered first.

    - **GivenName** *(string) --*

      First name.

    - **Initials** *(string) --*

      Concatenation that typically contains the first letter of the **GivenName** , the first
      letter of the middle name if one exists, and the first letter of the **SurName** .

    - **Pseudonym** *(string) --*

      Typically a shortened version of a longer **GivenName** . For example, Jonathan is often
      shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

    - **GenerationQualifier** *(string) --*

      Typically a qualifier appended to the name of an individual. Examples include Jr. for junior,
      Sr. for senior, and III for third.
    """


_ClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_ClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": str,
        "SigningAlgorithm": str,
        "Subject": ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef,
    },
)


class ClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef(
    _ClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef
):
    """
    Type definition for `ClientCreateCertificateAuthority` `CertificateAuthorityConfiguration`

    Name and bit size of the private key algorithm, the name of the signing algorithm, and X.500
    certificate subject information.

    - **KeyAlgorithm** *(string) --* **[REQUIRED]**

      Type of the public key algorithm and size, in bits, of the key pair that your CA creates when
      it issues a certificate. When you create a subordinate CA, you must use a key algorithm
      supported by the parent CA.

    - **SigningAlgorithm** *(string) --* **[REQUIRED]**

      Name of the algorithm your private CA uses to sign certificate requests.

    - **Subject** *(dict) --* **[REQUIRED]**

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

        Family name. In the US and the UK, for example, the surname of an individual is ordered last.
        In Asian cultures the surname is typically ordered first.

      - **GivenName** *(string) --*

        First name.

      - **Initials** *(string) --*

        Concatenation that typically contains the first letter of the **GivenName** , the first
        letter of the middle name if one exists, and the first letter of the **SurName** .

      - **Pseudonym** *(string) --*

        Typically a shortened version of a longer **GivenName** . For example, Jonathan is often
        shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

      - **GenerationQualifier** *(string) --*

        Typically a qualifier appended to the name of an individual. Examples include Jr. for junior,
        Sr. for senior, and III for third.
    """


_ClientCreateCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientCreateCertificateAuthorityResponseTypeDef",
    {"CertificateAuthorityArn": str},
    total=False,
)


class ClientCreateCertificateAuthorityResponseTypeDef(
    _ClientCreateCertificateAuthorityResponseTypeDef
):
    """
    Type definition for `ClientCreateCertificateAuthority` `Response`

    - **CertificateAuthorityArn** *(string) --*

      If successful, the Amazon Resource Name (ARN) of the certificate authority (CA). This is of
      the form:

       ``arn:aws:acm-pca:*region* :*account*
       :certificate-authority/*12345678-1234-1234-1234-123456789012* `` .
    """


_RequiredClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool},
)
_OptionalClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class ClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef(
    _RequiredClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef,
    _OptionalClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateCertificateAuthorityRevocationConfiguration` `CrlConfiguration`

    Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can
      use this value to enable certificate revocation for a new CA when you call the
      CreateCertificateAuthority action or for an existing CA when you call the
      UpdateCertificateAuthority action.

    - **ExpirationInDays** *(integer) --*

      Number of days until a certificate expires.

    - **CustomCname** *(string) --*

      Name inserted into the certificate **CRL Distribution Points** extension that enables the use
      of an alias for the CRL distribution point. Use this value if you don't want the name of your
      S3 bucket to be public.

    - **S3BucketName** *(string) --*

      Name of the S3 bucket that contains the CRL. If you do not provide a value for the
      **CustomCname** argument, the name of your S3 bucket is placed into the **CRL Distribution
      Points** extension of the issued certificate. You can change the name of your bucket by
      calling the  UpdateCertificateAuthority action. You must specify a bucket policy that allows
      ACM Private CA to write the CRL to your bucket.
    """


_ClientCreateCertificateAuthorityRevocationConfigurationTypeDef = TypedDict(
    "_ClientCreateCertificateAuthorityRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)


class ClientCreateCertificateAuthorityRevocationConfigurationTypeDef(
    _ClientCreateCertificateAuthorityRevocationConfigurationTypeDef
):
    """
    Type definition for `ClientCreateCertificateAuthority` `RevocationConfiguration`

    Contains a Boolean value that you can use to enable a certification revocation list (CRL) for the
    CA, the name of the S3 bucket to which ACM Private CA will write the CRL, and an optional CNAME
    alias that you can use to hide the name of your bucket in the **CRL Distribution Points**
    extension of your CA certificate. For more information, see the  CrlConfiguration structure.

    - **CrlConfiguration** *(dict) --*

      Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can
        use this value to enable certificate revocation for a new CA when you call the
        CreateCertificateAuthority action or for an existing CA when you call the
        UpdateCertificateAuthority action.

      - **ExpirationInDays** *(integer) --*

        Number of days until a certificate expires.

      - **CustomCname** *(string) --*

        Name inserted into the certificate **CRL Distribution Points** extension that enables the use
        of an alias for the CRL distribution point. Use this value if you don't want the name of your
        S3 bucket to be public.

      - **S3BucketName** *(string) --*

        Name of the S3 bucket that contains the CRL. If you do not provide a value for the
        **CustomCname** argument, the name of your S3 bucket is placed into the **CRL Distribution
        Points** extension of the issued certificate. You can change the name of your bucket by
        calling the  UpdateCertificateAuthority action. You must specify a bucket policy that allows
        ACM Private CA to write the CRL to your bucket.
    """


_RequiredClientCreateCertificateAuthorityTagsTypeDef = TypedDict(
    "_RequiredClientCreateCertificateAuthorityTagsTypeDef", {"Key": str}
)
_OptionalClientCreateCertificateAuthorityTagsTypeDef = TypedDict(
    "_OptionalClientCreateCertificateAuthorityTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateCertificateAuthorityTagsTypeDef(
    _RequiredClientCreateCertificateAuthorityTagsTypeDef,
    _OptionalClientCreateCertificateAuthorityTagsTypeDef,
):
    """
    Type definition for `ClientCreateCertificateAuthority` `Tags`

    Tags are labels that you can use to identify and organize your private CAs. Each tag consists
    of a key and an optional value. You can associate up to 50 tags with a private CA. To add one
    or more tags to a private CA, call the  TagCertificateAuthority action. To remove a tag, call
    the  UntagCertificateAuthority action.

    - **Key** *(string) --* **[REQUIRED]**

      Key (name) of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientDescribeCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportStatus": str,
        "S3BucketName": str,
        "S3Key": str,
        "CreatedAt": datetime,
    },
    total=False,
)


class ClientDescribeCertificateAuthorityAuditReportResponseTypeDef(
    _ClientDescribeCertificateAuthorityAuditReportResponseTypeDef
):
    """
    Type definition for `ClientDescribeCertificateAuthorityAuditReport` `Response`

    - **AuditReportStatus** *(string) --*

      Specifies whether report creation is in progress, has succeeded, or has failed.

    - **S3BucketName** *(string) --*

      Name of the S3 bucket that contains the report.

    - **S3Key** *(string) --*

      S3 **key** that uniquely identifies the report file in your S3 bucket.

    - **CreatedAt** *(datetime) --*

      The date and time at which the report was created.
    """


_ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
    },
    total=False,
)


class ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef(
    _ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef
):
    """
    Type definition for `ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfiguration` `Subject`

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

      Family name. In the US and the UK, for example, the surname of an individual is ordered
      last. In Asian cultures the surname is typically ordered first.

    - **GivenName** *(string) --*

      First name.

    - **Initials** *(string) --*

      Concatenation that typically contains the first letter of the **GivenName** , the first
      letter of the middle name if one exists, and the first letter of the **SurName** .

    - **Pseudonym** *(string) --*

      Typically a shortened version of a longer **GivenName** . For example, Jonathan is
      often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

    - **GenerationQualifier** *(string) --*

      Typically a qualifier appended to the name of an individual. Examples include Jr. for
      junior, Sr. for senior, and III for third.
    """


_ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": str,
        "SigningAlgorithm": str,
        "Subject": ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef,
    },
    total=False,
)


class ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef(
    _ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeCertificateAuthorityResponseCertificateAuthority` `CertificateAuthorityConfiguration`

    Your private CA configuration.

    - **KeyAlgorithm** *(string) --*

      Type of the public key algorithm and size, in bits, of the key pair that your CA creates
      when it issues a certificate. When you create a subordinate CA, you must use a key
      algorithm supported by the parent CA.

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

        Family name. In the US and the UK, for example, the surname of an individual is ordered
        last. In Asian cultures the surname is typically ordered first.

      - **GivenName** *(string) --*

        First name.

      - **Initials** *(string) --*

        Concatenation that typically contains the first letter of the **GivenName** , the first
        letter of the middle name if one exists, and the first letter of the **SurName** .

      - **Pseudonym** *(string) --*

        Typically a shortened version of a longer **GivenName** . For example, Jonathan is
        often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

      - **GenerationQualifier** *(string) --*

        Typically a qualifier appended to the name of an individual. Examples include Jr. for
        junior, Sr. for senior, and III for third.
    """


_ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool, "ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef(
    _ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfiguration` `CrlConfiguration`

    Configuration of the certificate revocation list (CRL), if any, maintained by your
    private CA.

    - **Enabled** *(boolean) --*

      Boolean value that specifies whether certificate revocation lists (CRLs) are enabled.
      You can use this value to enable certificate revocation for a new CA when you call the
      CreateCertificateAuthority action or for an existing CA when you call the
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
    """


_ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)


class ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef(
    _ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeCertificateAuthorityResponseCertificateAuthority` `RevocationConfiguration`

    Information about the certificate revocation list (CRL) created and maintained by your
    private CA.

    - **CrlConfiguration** *(dict) --*

      Configuration of the certificate revocation list (CRL), if any, maintained by your
      private CA.

      - **Enabled** *(boolean) --*

        Boolean value that specifies whether certificate revocation lists (CRLs) are enabled.
        You can use this value to enable certificate revocation for a new CA when you call the
        CreateCertificateAuthority action or for an existing CA when you call the
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
    """


_ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "LastStateChangeAt": datetime,
        "Type": str,
        "Serial": str,
        "Status": str,
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": str,
        "CertificateAuthorityConfiguration": ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef,
        "RevocationConfiguration": ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef,
        "RestorableUntil": datetime,
    },
    total=False,
)


class ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef(
    _ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef
):
    """
    Type definition for `ClientDescribeCertificateAuthorityResponse` `CertificateAuthority`

    A  CertificateAuthority structure that contains information about your private CA.

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

        Type of the public key algorithm and size, in bits, of the key pair that your CA creates
        when it issues a certificate. When you create a subordinate CA, you must use a key
        algorithm supported by the parent CA.

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

          Family name. In the US and the UK, for example, the surname of an individual is ordered
          last. In Asian cultures the surname is typically ordered first.

        - **GivenName** *(string) --*

          First name.

        - **Initials** *(string) --*

          Concatenation that typically contains the first letter of the **GivenName** , the first
          letter of the middle name if one exists, and the first letter of the **SurName** .

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
          You can use this value to enable certificate revocation for a new CA when you call the
          CreateCertificateAuthority action or for an existing CA when you call the
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
      ``PermanentDeletionTimeInDays`` parameter of the  DeleteCertificateAuthorityRequest action.
    """


_ClientDescribeCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseTypeDef",
    {
        "CertificateAuthority": ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef
    },
    total=False,
)


class ClientDescribeCertificateAuthorityResponseTypeDef(
    _ClientDescribeCertificateAuthorityResponseTypeDef
):
    """
    Type definition for `ClientDescribeCertificateAuthority` `Response`

    - **CertificateAuthority** *(dict) --*

      A  CertificateAuthority structure that contains information about your private CA.

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

          Type of the public key algorithm and size, in bits, of the key pair that your CA creates
          when it issues a certificate. When you create a subordinate CA, you must use a key
          algorithm supported by the parent CA.

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

            Family name. In the US and the UK, for example, the surname of an individual is ordered
            last. In Asian cultures the surname is typically ordered first.

          - **GivenName** *(string) --*

            First name.

          - **Initials** *(string) --*

            Concatenation that typically contains the first letter of the **GivenName** , the first
            letter of the middle name if one exists, and the first letter of the **SurName** .

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
            You can use this value to enable certificate revocation for a new CA when you call the
            CreateCertificateAuthority action or for an existing CA when you call the
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
        ``PermanentDeletionTimeInDays`` parameter of the  DeleteCertificateAuthorityRequest action.
    """


_ClientGetCertificateAuthorityCertificateResponseTypeDef = TypedDict(
    "_ClientGetCertificateAuthorityCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str},
    total=False,
)


class ClientGetCertificateAuthorityCertificateResponseTypeDef(
    _ClientGetCertificateAuthorityCertificateResponseTypeDef
):
    """
    Type definition for `ClientGetCertificateAuthorityCertificate` `Response`

    - **Certificate** *(string) --*

      Base64-encoded certificate authority (CA) certificate.

    - **CertificateChain** *(string) --*

      Base64-encoded certificate chain that includes any intermediate certificates and chains up to
      root on-premises certificate that you used to sign your private CA certificate. The chain
      does not include your private CA certificate. If this is a root CA, the value will be null.
    """


_ClientGetCertificateAuthorityCsrResponseTypeDef = TypedDict(
    "_ClientGetCertificateAuthorityCsrResponseTypeDef", {"Csr": str}, total=False
)


class ClientGetCertificateAuthorityCsrResponseTypeDef(
    _ClientGetCertificateAuthorityCsrResponseTypeDef
):
    """
    Type definition for `ClientGetCertificateAuthorityCsr` `Response`

    - **Csr** *(string) --*

      The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.
    """


_ClientGetCertificateResponseTypeDef = TypedDict(
    "_ClientGetCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str},
    total=False,
)


class ClientGetCertificateResponseTypeDef(_ClientGetCertificateResponseTypeDef):
    """
    Type definition for `ClientGetCertificate` `Response`

    - **Certificate** *(string) --*

      The base64 PEM-encoded certificate specified by the ``CertificateArn`` parameter.

    - **CertificateChain** *(string) --*

      The base64 PEM-encoded certificate chain that chains up to the on-premises root CA
      certificate that you used to sign your private CA certificate.
    """


_ClientIssueCertificateResponseTypeDef = TypedDict(
    "_ClientIssueCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)


class ClientIssueCertificateResponseTypeDef(_ClientIssueCertificateResponseTypeDef):
    """
    Type definition for `ClientIssueCertificate` `Response`

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the issued certificate and the certificate serial number.
      This is of the form:

       ``arn:aws:acm-pca:*region* :*account*
       :certificate-authority/*12345678-1234-1234-1234-123456789012*
       /certificate/*286535153982981100925020015808220737245* ``
    """


_ClientIssueCertificateValidityTypeDef = TypedDict(
    "_ClientIssueCertificateValidityTypeDef", {"Value": int, "Type": str}
)


class ClientIssueCertificateValidityTypeDef(_ClientIssueCertificateValidityTypeDef):
    """
    Type definition for `ClientIssueCertificate` `Validity`

    The type of the validity period.

    - **Value** *(integer) --* **[REQUIRED]**

      Time period.

    - **Type** *(string) --* **[REQUIRED]**

      Specifies whether the ``Value`` parameter represents days, months, or years.
    """


_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
    },
    total=False,
)


class ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef(
    _ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef
):
    """
    Type definition for `ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfiguration` `Subject`

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
    """


_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": str,
        "SigningAlgorithm": str,
        "Subject": ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef,
    },
    total=False,
)


class ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef(
    _ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef
):
    """
    Type definition for `ClientListCertificateAuthoritiesResponseCertificateAuthorities` `CertificateAuthorityConfiguration`

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
    """


_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool, "ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef(
    _ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef
):
    """
    Type definition for `ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfiguration` `CrlConfiguration`

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
    """


_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)


class ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef(
    _ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef
):
    """
    Type definition for `ClientListCertificateAuthoritiesResponseCertificateAuthorities` `RevocationConfiguration`

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
    """


_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "LastStateChangeAt": datetime,
        "Type": str,
        "Serial": str,
        "Status": str,
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": str,
        "CertificateAuthorityConfiguration": ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef,
        "RevocationConfiguration": ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef,
        "RestorableUntil": datetime,
    },
    total=False,
)


class ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef(
    _ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef
):
    """
    Type definition for `ClientListCertificateAuthoritiesResponse` `CertificateAuthorities`

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


_ClientListCertificateAuthoritiesResponseTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseTypeDef",
    {
        "CertificateAuthorities": List[
            ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListCertificateAuthoritiesResponseTypeDef(
    _ClientListCertificateAuthoritiesResponseTypeDef
):
    """
    Type definition for `ClientListCertificateAuthorities` `Response`

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

    - **NextToken** *(string) --*

      When the list is truncated, this value is present and should be used for the ``NextToken``
      parameter in a subsequent pagination request.
    """


_ClientListPermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientListPermissionsResponsePermissionsTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CreatedAt": datetime,
        "Principal": str,
        "SourceAccount": str,
        "Actions": List[str],
        "Policy": str,
    },
    total=False,
)


class ClientListPermissionsResponsePermissionsTypeDef(
    _ClientListPermissionsResponsePermissionsTypeDef
):
    """
    Type definition for `ClientListPermissionsResponse` `Permissions`

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


_ClientListPermissionsResponseTypeDef = TypedDict(
    "_ClientListPermissionsResponseTypeDef",
    {
        "Permissions": List[ClientListPermissionsResponsePermissionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListPermissionsResponseTypeDef(_ClientListPermissionsResponseTypeDef):
    """
    Type definition for `ClientListPermissions` `Response`

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

    - **NextToken** *(string) --*

      When the list is truncated, this value is present and should be used for the **NextToken**
      parameter in a subsequent pagination request.
    """


_ClientListTagsResponseTagsTypeDef = TypedDict(
    "_ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagsTypeDef(_ClientListTagsResponseTagsTypeDef):
    """
    Type definition for `ClientListTagsResponse` `Tags`

    Tags are labels that you can use to identify and organize your private CAs. Each tag
    consists of a key and an optional value. You can associate up to 50 tags with a private CA.
    To add one or more tags to a private CA, call the  TagCertificateAuthority action. To
    remove a tag, call the  UntagCertificateAuthority action.

    - **Key** *(string) --*

      Key (name) of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    Type definition for `ClientListTags` `Response`

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

    - **NextToken** *(string) --*

      When the list is truncated, this value is present and should be used for the **NextToken**
      parameter in a subsequent pagination request.
    """


_RequiredClientTagCertificateAuthorityTagsTypeDef = TypedDict(
    "_RequiredClientTagCertificateAuthorityTagsTypeDef", {"Key": str}
)
_OptionalClientTagCertificateAuthorityTagsTypeDef = TypedDict(
    "_OptionalClientTagCertificateAuthorityTagsTypeDef", {"Value": str}, total=False
)


class ClientTagCertificateAuthorityTagsTypeDef(
    _RequiredClientTagCertificateAuthorityTagsTypeDef,
    _OptionalClientTagCertificateAuthorityTagsTypeDef,
):
    """
    Type definition for `ClientTagCertificateAuthority` `Tags`

    Tags are labels that you can use to identify and organize your private CAs. Each tag consists
    of a key and an optional value. You can associate up to 50 tags with a private CA. To add one
    or more tags to a private CA, call the  TagCertificateAuthority action. To remove a tag, call
    the  UntagCertificateAuthority action.

    - **Key** *(string) --* **[REQUIRED]**

      Key (name) of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_RequiredClientUntagCertificateAuthorityTagsTypeDef = TypedDict(
    "_RequiredClientUntagCertificateAuthorityTagsTypeDef", {"Key": str}
)
_OptionalClientUntagCertificateAuthorityTagsTypeDef = TypedDict(
    "_OptionalClientUntagCertificateAuthorityTagsTypeDef", {"Value": str}, total=False
)


class ClientUntagCertificateAuthorityTagsTypeDef(
    _RequiredClientUntagCertificateAuthorityTagsTypeDef,
    _OptionalClientUntagCertificateAuthorityTagsTypeDef,
):
    """
    Type definition for `ClientUntagCertificateAuthority` `Tags`

    Tags are labels that you can use to identify and organize your private CAs. Each tag consists
    of a key and an optional value. You can associate up to 50 tags with a private CA. To add one
    or more tags to a private CA, call the  TagCertificateAuthority action. To remove a tag, call
    the  UntagCertificateAuthority action.

    - **Key** *(string) --* **[REQUIRED]**

      Key (name) of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_RequiredClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool},
)
_OptionalClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class ClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef(
    _RequiredClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef,
    _OptionalClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef,
):
    """
    Type definition for `ClientUpdateCertificateAuthorityRevocationConfiguration` `CrlConfiguration`

    Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can
      use this value to enable certificate revocation for a new CA when you call the
      CreateCertificateAuthority action or for an existing CA when you call the
      UpdateCertificateAuthority action.

    - **ExpirationInDays** *(integer) --*

      Number of days until a certificate expires.

    - **CustomCname** *(string) --*

      Name inserted into the certificate **CRL Distribution Points** extension that enables the use
      of an alias for the CRL distribution point. Use this value if you don't want the name of your
      S3 bucket to be public.

    - **S3BucketName** *(string) --*

      Name of the S3 bucket that contains the CRL. If you do not provide a value for the
      **CustomCname** argument, the name of your S3 bucket is placed into the **CRL Distribution
      Points** extension of the issued certificate. You can change the name of your bucket by
      calling the  UpdateCertificateAuthority action. You must specify a bucket policy that allows
      ACM Private CA to write the CRL to your bucket.
    """


_ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef = TypedDict(
    "_ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef(
    _ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateCertificateAuthority` `RevocationConfiguration`

    Revocation information for your private CA.

    - **CrlConfiguration** *(dict) --*

      Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can
        use this value to enable certificate revocation for a new CA when you call the
        CreateCertificateAuthority action or for an existing CA when you call the
        UpdateCertificateAuthority action.

      - **ExpirationInDays** *(integer) --*

        Number of days until a certificate expires.

      - **CustomCname** *(string) --*

        Name inserted into the certificate **CRL Distribution Points** extension that enables the use
        of an alias for the CRL distribution point. Use this value if you don't want the name of your
        S3 bucket to be public.

      - **S3BucketName** *(string) --*

        Name of the S3 bucket that contains the CRL. If you do not provide a value for the
        **CustomCname** argument, the name of your S3 bucket is placed into the **CRL Distribution
        Points** extension of the issued certificate. You can change the name of your bucket by
        calling the  UpdateCertificateAuthority action. You must specify a bucket policy that allows
        ACM Private CA to write the CRL to your bucket.
    """


_ListCertificateAuthoritiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCertificateAuthoritiesPaginatePaginationConfigTypeDef(
    _ListCertificateAuthoritiesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCertificateAuthoritiesPaginate` `PaginationConfig`

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
    """


_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
    },
    total=False,
)


class ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef(
    _ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef
):
    """
    Type definition for `ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfiguration` `Subject`

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
    """


_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": str,
        "SigningAlgorithm": str,
        "Subject": ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef,
    },
    total=False,
)


class ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef(
    _ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef
):
    """
    Type definition for `ListCertificateAuthoritiesPaginateResponseCertificateAuthorities` `CertificateAuthorityConfiguration`

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
    """


_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool, "ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef(
    _ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef
):
    """
    Type definition for `ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfiguration` `CrlConfiguration`

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
    """


_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)


class ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef(
    _ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef
):
    """
    Type definition for `ListCertificateAuthoritiesPaginateResponseCertificateAuthorities` `RevocationConfiguration`

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
    """


_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "LastStateChangeAt": datetime,
        "Type": str,
        "Serial": str,
        "Status": str,
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": str,
        "CertificateAuthorityConfiguration": ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef,
        "RevocationConfiguration": ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef,
        "RestorableUntil": datetime,
    },
    total=False,
)


class ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef(
    _ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef
):
    """
    Type definition for `ListCertificateAuthoritiesPaginateResponse` `CertificateAuthorities`

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


_ListCertificateAuthoritiesPaginateResponseTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseTypeDef",
    {
        "CertificateAuthorities": List[
            ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef
        ]
    },
    total=False,
)


class ListCertificateAuthoritiesPaginateResponseTypeDef(
    _ListCertificateAuthoritiesPaginateResponseTypeDef
):
    """
    Type definition for `ListCertificateAuthoritiesPaginate` `Response`

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


_ListPermissionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPermissionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPermissionsPaginatePaginationConfigTypeDef(
    _ListPermissionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPermissionsPaginate` `PaginationConfig`

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
    """


_ListPermissionsPaginateResponsePermissionsTypeDef = TypedDict(
    "_ListPermissionsPaginateResponsePermissionsTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CreatedAt": datetime,
        "Principal": str,
        "SourceAccount": str,
        "Actions": List[str],
        "Policy": str,
    },
    total=False,
)


class ListPermissionsPaginateResponsePermissionsTypeDef(
    _ListPermissionsPaginateResponsePermissionsTypeDef
):
    """
    Type definition for `ListPermissionsPaginateResponse` `Permissions`

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


_ListPermissionsPaginateResponseTypeDef = TypedDict(
    "_ListPermissionsPaginateResponseTypeDef",
    {"Permissions": List[ListPermissionsPaginateResponsePermissionsTypeDef]},
    total=False,
)


class ListPermissionsPaginateResponseTypeDef(_ListPermissionsPaginateResponseTypeDef):
    """
    Type definition for `ListPermissionsPaginate` `Response`

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


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsPaginatePaginationConfigTypeDef(_ListTagsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListTagsPaginate` `PaginationConfig`

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
    """


_ListTagsPaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsPaginateResponseTagsTypeDef(_ListTagsPaginateResponseTagsTypeDef):
    """
    Type definition for `ListTagsPaginateResponse` `Tags`

    Tags are labels that you can use to identify and organize your private CAs. Each tag
    consists of a key and an optional value. You can associate up to 50 tags with a private CA.
    To add one or more tags to a private CA, call the  TagCertificateAuthority action. To
    remove a tag, call the  UntagCertificateAuthority action.

    - **Key** *(string) --*

      Key (name) of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"Tags": List[ListTagsPaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    Type definition for `ListTagsPaginate` `Response`

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
