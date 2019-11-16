"Main interface for acm type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "CertificateValidatedWaitWaiterConfigTypeDef",
    "ClientAddTagsToCertificateTagsTypeDef",
    "ClientExportCertificateResponseTypeDef",
    "ClientGetCertificateResponseTypeDef",
    "ClientImportCertificateResponseTypeDef",
    "ClientListCertificatesIncludesTypeDef",
    "ClientListCertificatesResponseCertificateSummaryListTypeDef",
    "ClientListCertificatesResponseTypeDef",
    "ClientListTagsForCertificateResponseTagsTypeDef",
    "ClientListTagsForCertificateResponseTypeDef",
    "ClientRemoveTagsFromCertificateTagsTypeDef",
    "ClientRequestCertificateDomainValidationOptionsTypeDef",
    "ClientRequestCertificateOptionsTypeDef",
    "ClientRequestCertificateResponseTypeDef",
    "ClientUpdateCertificateOptionsOptionsTypeDef",
    "ListCertificatesPaginateIncludesTypeDef",
    "ListCertificatesPaginatePaginationConfigTypeDef",
    "ListCertificatesPaginateResponseCertificateSummaryListTypeDef",
    "ListCertificatesPaginateResponseTypeDef",
)


_CertificateValidatedWaitWaiterConfigTypeDef = TypedDict(
    "_CertificateValidatedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class CertificateValidatedWaitWaiterConfigTypeDef(
    _CertificateValidatedWaitWaiterConfigTypeDef
):
    """
    Type definition for `CertificateValidatedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 60

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_RequiredClientAddTagsToCertificateTagsTypeDef = TypedDict(
    "_RequiredClientAddTagsToCertificateTagsTypeDef", {"Key": str}
)
_OptionalClientAddTagsToCertificateTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsToCertificateTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsToCertificateTagsTypeDef(
    _RequiredClientAddTagsToCertificateTagsTypeDef,
    _OptionalClientAddTagsToCertificateTagsTypeDef,
):
    """
    Type definition for `ClientAddTagsToCertificate` `Tags`

    A key-value pair that identifies or specifies metadata about an ACM resource.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientExportCertificateResponseTypeDef = TypedDict(
    "_ClientExportCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str, "PrivateKey": str},
    total=False,
)


class ClientExportCertificateResponseTypeDef(_ClientExportCertificateResponseTypeDef):
    """
    Type definition for `ClientExportCertificate` `Response`

    - **Certificate** *(string) --*

      The base64 PEM-encoded certificate.

    - **CertificateChain** *(string) --*

      The base64 PEM-encoded certificate chain. This does not include the certificate that you are
      exporting.

    - **PrivateKey** *(string) --*

      The encrypted private key associated with the public key in the certificate. The key is
      output in PKCS #8 format and is base64 PEM-encoded.
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

      String that contains the ACM certificate represented by the ARN specified at input.

    - **CertificateChain** *(string) --*

      The certificate chain that contains the root certificate issued by the certificate authority
      (CA).
    """


_ClientImportCertificateResponseTypeDef = TypedDict(
    "_ClientImportCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)


class ClientImportCertificateResponseTypeDef(_ClientImportCertificateResponseTypeDef):
    """
    Type definition for `ClientImportCertificate` `Response`

    - **CertificateArn** *(string) --*

      The `Amazon Resource Name (ARN)
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of the
      imported certificate.
    """


_ClientListCertificatesIncludesTypeDef = TypedDict(
    "_ClientListCertificatesIncludesTypeDef",
    {"extendedKeyUsage": List[str], "keyUsage": List[str], "keyTypes": List[str]},
    total=False,
)


class ClientListCertificatesIncludesTypeDef(_ClientListCertificatesIncludesTypeDef):
    """
    Type definition for `ClientListCertificates` `Includes`

    Filter the certificate list. For more information, see the  Filters structure.

    - **extendedKeyUsage** *(list) --*

      Specify one or more  ExtendedKeyUsage extension values.

      - *(string) --*

    - **keyUsage** *(list) --*

      Specify one or more  KeyUsage extension values.

      - *(string) --*

    - **keyTypes** *(list) --*

      Specify one or more algorithms that can be used to generate key pairs.

      - *(string) --*
    """


_ClientListCertificatesResponseCertificateSummaryListTypeDef = TypedDict(
    "_ClientListCertificatesResponseCertificateSummaryListTypeDef",
    {"CertificateArn": str, "DomainName": str},
    total=False,
)


class ClientListCertificatesResponseCertificateSummaryListTypeDef(
    _ClientListCertificatesResponseCertificateSummaryListTypeDef
):
    """
    Type definition for `ClientListCertificatesResponse` `CertificateSummaryList`

    This structure is returned in the response object of  ListCertificates action.

    - **CertificateArn** *(string) --*

      Amazon Resource Name (ARN) of the certificate. This is of the form:

       ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **DomainName** *(string) --*

      Fully qualified domain name (FQDN), such as www.example.com or example.com, for the
      certificate.
    """


_ClientListCertificatesResponseTypeDef = TypedDict(
    "_ClientListCertificatesResponseTypeDef",
    {
        "NextToken": str,
        "CertificateSummaryList": List[
            ClientListCertificatesResponseCertificateSummaryListTypeDef
        ],
    },
    total=False,
)


class ClientListCertificatesResponseTypeDef(_ClientListCertificatesResponseTypeDef):
    """
    Type definition for `ClientListCertificates` `Response`

    - **NextToken** *(string) --*

      When the list is truncated, this value is present and contains the value to use for the
      ``NextToken`` parameter in a subsequent pagination request.

    - **CertificateSummaryList** *(list) --*

      A list of ACM certificates.

      - *(dict) --*

        This structure is returned in the response object of  ListCertificates action.

        - **CertificateArn** *(string) --*

          Amazon Resource Name (ARN) of the certificate. This is of the form:

           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **DomainName** *(string) --*

          Fully qualified domain name (FQDN), such as www.example.com or example.com, for the
          certificate.
    """


_ClientListTagsForCertificateResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForCertificateResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForCertificateResponseTagsTypeDef(
    _ClientListTagsForCertificateResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForCertificateResponse` `Tags`

    A key-value pair that identifies or specifies metadata about an ACM resource.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientListTagsForCertificateResponseTypeDef = TypedDict(
    "_ClientListTagsForCertificateResponseTypeDef",
    {"Tags": List[ClientListTagsForCertificateResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForCertificateResponseTypeDef(
    _ClientListTagsForCertificateResponseTypeDef
):
    """
    Type definition for `ClientListTagsForCertificate` `Response`

    - **Tags** *(list) --*

      The key-value pairs that define the applied tags.

      - *(dict) --*

        A key-value pair that identifies or specifies metadata about an ACM resource.

        - **Key** *(string) --*

          The key of the tag.

        - **Value** *(string) --*

          The value of the tag.
    """


_RequiredClientRemoveTagsFromCertificateTagsTypeDef = TypedDict(
    "_RequiredClientRemoveTagsFromCertificateTagsTypeDef", {"Key": str}
)
_OptionalClientRemoveTagsFromCertificateTagsTypeDef = TypedDict(
    "_OptionalClientRemoveTagsFromCertificateTagsTypeDef", {"Value": str}, total=False
)


class ClientRemoveTagsFromCertificateTagsTypeDef(
    _RequiredClientRemoveTagsFromCertificateTagsTypeDef,
    _OptionalClientRemoveTagsFromCertificateTagsTypeDef,
):
    """
    Type definition for `ClientRemoveTagsFromCertificate` `Tags`

    A key-value pair that identifies or specifies metadata about an ACM resource.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientRequestCertificateDomainValidationOptionsTypeDef = TypedDict(
    "_ClientRequestCertificateDomainValidationOptionsTypeDef",
    {"DomainName": str, "ValidationDomain": str},
)


class ClientRequestCertificateDomainValidationOptionsTypeDef(
    _ClientRequestCertificateDomainValidationOptionsTypeDef
):
    """
    Type definition for `ClientRequestCertificate` `DomainValidationOptions`

    Contains information about the domain names that you want ACM to use to send you emails that
    enable you to validate domain ownership.

    - **DomainName** *(string) --* **[REQUIRED]**

      A fully qualified domain name (FQDN) in the certificate request.

    - **ValidationDomain** *(string) --* **[REQUIRED]**

      The domain name that you want ACM to use to send you validation emails. This domain name is
      the suffix of the email addresses that you want ACM to use. This must be the same as the
      ``DomainName`` value or a superdomain of the ``DomainName`` value. For example, if you
      request a certificate for ``testing.example.com`` , you can specify ``example.com`` for this
      value. In that case, ACM sends domain validation emails to the following five addresses:

      * admin@example.com

      * administrator@example.com

      * hostmaster@example.com

      * postmaster@example.com

      * webmaster@example.com
    """


_ClientRequestCertificateOptionsTypeDef = TypedDict(
    "_ClientRequestCertificateOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": str},
    total=False,
)


class ClientRequestCertificateOptionsTypeDef(_ClientRequestCertificateOptionsTypeDef):
    """
    Type definition for `ClientRequestCertificate` `Options`

    Currently, you can use this parameter to specify whether to add the certificate to a certificate
    transparency log. Certificate transparency makes it possible to detect SSL/TLS certificates that
    have been mistakenly or maliciously issued. Certificates that have not been logged typically
    produce an error message in a browser. For more information, see `Opting Out of Certificate
    Transparency Logging
    <https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency>`__
    .

    - **CertificateTransparencyLoggingPreference** *(string) --*

      You can opt out of certificate transparency logging by specifying the ``DISABLED`` option. Opt
      in by specifying ``ENABLED`` .
    """


_ClientRequestCertificateResponseTypeDef = TypedDict(
    "_ClientRequestCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)


class ClientRequestCertificateResponseTypeDef(_ClientRequestCertificateResponseTypeDef):
    """
    Type definition for `ClientRequestCertificate` `Response`

    - **CertificateArn** *(string) --*

      String that contains the ARN of the issued certificate. This must be of the form:

       ``arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012``
    """


_ClientUpdateCertificateOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateCertificateOptionsOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": str},
    total=False,
)


class ClientUpdateCertificateOptionsOptionsTypeDef(
    _ClientUpdateCertificateOptionsOptionsTypeDef
):
    """
    Type definition for `ClientUpdateCertificateOptions` `Options`

    Use to update the options for your certificate. Currently, you can specify whether to add your
    certificate to a transparency log. Certificate transparency makes it possible to detect SSL/TLS
    certificates that have been mistakenly or maliciously issued. Certificates that have not been
    logged typically produce an error message in a browser.

    - **CertificateTransparencyLoggingPreference** *(string) --*

      You can opt out of certificate transparency logging by specifying the ``DISABLED`` option. Opt
      in by specifying ``ENABLED`` .
    """


_ListCertificatesPaginateIncludesTypeDef = TypedDict(
    "_ListCertificatesPaginateIncludesTypeDef",
    {"extendedKeyUsage": List[str], "keyUsage": List[str], "keyTypes": List[str]},
    total=False,
)


class ListCertificatesPaginateIncludesTypeDef(_ListCertificatesPaginateIncludesTypeDef):
    """
    Type definition for `ListCertificatesPaginate` `Includes`

    Filter the certificate list. For more information, see the  Filters structure.

    - **extendedKeyUsage** *(list) --*

      Specify one or more  ExtendedKeyUsage extension values.

      - *(string) --*

    - **keyUsage** *(list) --*

      Specify one or more  KeyUsage extension values.

      - *(string) --*

    - **keyTypes** *(list) --*

      Specify one or more algorithms that can be used to generate key pairs.

      - *(string) --*
    """


_ListCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCertificatesPaginatePaginationConfigTypeDef(
    _ListCertificatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCertificatesPaginate` `PaginationConfig`

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


_ListCertificatesPaginateResponseCertificateSummaryListTypeDef = TypedDict(
    "_ListCertificatesPaginateResponseCertificateSummaryListTypeDef",
    {"CertificateArn": str, "DomainName": str},
    total=False,
)


class ListCertificatesPaginateResponseCertificateSummaryListTypeDef(
    _ListCertificatesPaginateResponseCertificateSummaryListTypeDef
):
    """
    Type definition for `ListCertificatesPaginateResponse` `CertificateSummaryList`

    This structure is returned in the response object of  ListCertificates action.

    - **CertificateArn** *(string) --*

      Amazon Resource Name (ARN) of the certificate. This is of the form:

       ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

    - **DomainName** *(string) --*

      Fully qualified domain name (FQDN), such as www.example.com or example.com, for the
      certificate.
    """


_ListCertificatesPaginateResponseTypeDef = TypedDict(
    "_ListCertificatesPaginateResponseTypeDef",
    {
        "CertificateSummaryList": List[
            ListCertificatesPaginateResponseCertificateSummaryListTypeDef
        ]
    },
    total=False,
)


class ListCertificatesPaginateResponseTypeDef(_ListCertificatesPaginateResponseTypeDef):
    """
    Type definition for `ListCertificatesPaginate` `Response`

    - **CertificateSummaryList** *(list) --*

      A list of ACM certificates.

      - *(dict) --*

        This structure is returned in the response object of  ListCertificates action.

        - **CertificateArn** *(string) --*

          Amazon Resource Name (ARN) of the certificate. This is of the form:

           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

        - **DomainName** *(string) --*

          Fully qualified domain name (FQDN), such as www.example.com or example.com, for the
          certificate.
    """
