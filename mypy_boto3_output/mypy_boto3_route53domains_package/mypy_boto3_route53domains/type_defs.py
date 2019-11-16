"Main interface for route53domains type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCheckDomainAvailabilityResponseTypeDef",
    "ClientCheckDomainTransferabilityResponseTransferabilityTypeDef",
    "ClientCheckDomainTransferabilityResponseTypeDef",
    "ClientDisableDomainTransferLockResponseTypeDef",
    "ClientEnableDomainTransferLockResponseTypeDef",
    "ClientGetContactReachabilityStatusResponseTypeDef",
    "ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef",
    "ClientGetDomainDetailResponseAdminContactTypeDef",
    "ClientGetDomainDetailResponseNameserversTypeDef",
    "ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef",
    "ClientGetDomainDetailResponseRegistrantContactTypeDef",
    "ClientGetDomainDetailResponseTechContactExtraParamsTypeDef",
    "ClientGetDomainDetailResponseTechContactTypeDef",
    "ClientGetDomainDetailResponseTypeDef",
    "ClientGetDomainSuggestionsResponseSuggestionsListTypeDef",
    "ClientGetDomainSuggestionsResponseTypeDef",
    "ClientGetOperationDetailResponseTypeDef",
    "ClientListDomainsResponseDomainsTypeDef",
    "ClientListDomainsResponseTypeDef",
    "ClientListOperationsResponseOperationsTypeDef",
    "ClientListOperationsResponseTypeDef",
    "ClientListTagsForDomainResponseTagListTypeDef",
    "ClientListTagsForDomainResponseTypeDef",
    "ClientRegisterDomainAdminContactExtraParamsTypeDef",
    "ClientRegisterDomainAdminContactTypeDef",
    "ClientRegisterDomainRegistrantContactExtraParamsTypeDef",
    "ClientRegisterDomainRegistrantContactTypeDef",
    "ClientRegisterDomainResponseTypeDef",
    "ClientRegisterDomainTechContactExtraParamsTypeDef",
    "ClientRegisterDomainTechContactTypeDef",
    "ClientRenewDomainResponseTypeDef",
    "ClientResendContactReachabilityEmailResponseTypeDef",
    "ClientRetrieveDomainAuthCodeResponseTypeDef",
    "ClientTransferDomainAdminContactExtraParamsTypeDef",
    "ClientTransferDomainAdminContactTypeDef",
    "ClientTransferDomainNameserversTypeDef",
    "ClientTransferDomainRegistrantContactExtraParamsTypeDef",
    "ClientTransferDomainRegistrantContactTypeDef",
    "ClientTransferDomainResponseTypeDef",
    "ClientTransferDomainTechContactExtraParamsTypeDef",
    "ClientTransferDomainTechContactTypeDef",
    "ClientUpdateDomainContactAdminContactExtraParamsTypeDef",
    "ClientUpdateDomainContactAdminContactTypeDef",
    "ClientUpdateDomainContactPrivacyResponseTypeDef",
    "ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef",
    "ClientUpdateDomainContactRegistrantContactTypeDef",
    "ClientUpdateDomainContactResponseTypeDef",
    "ClientUpdateDomainContactTechContactExtraParamsTypeDef",
    "ClientUpdateDomainContactTechContactTypeDef",
    "ClientUpdateDomainNameserversNameserversTypeDef",
    "ClientUpdateDomainNameserversResponseTypeDef",
    "ClientUpdateTagsForDomainTagsToUpdateTypeDef",
    "ClientViewBillingResponseBillingRecordsTypeDef",
    "ClientViewBillingResponseTypeDef",
    "ListDomainsPaginatePaginationConfigTypeDef",
    "ListDomainsPaginateResponseDomainsTypeDef",
    "ListDomainsPaginateResponseTypeDef",
    "ListOperationsPaginatePaginationConfigTypeDef",
    "ListOperationsPaginateResponseOperationsTypeDef",
    "ListOperationsPaginateResponseTypeDef",
    "ViewBillingPaginatePaginationConfigTypeDef",
    "ViewBillingPaginateResponseBillingRecordsTypeDef",
    "ViewBillingPaginateResponseTypeDef",
)


_ClientCheckDomainAvailabilityResponseTypeDef = TypedDict(
    "_ClientCheckDomainAvailabilityResponseTypeDef", {"Availability": str}, total=False
)


class ClientCheckDomainAvailabilityResponseTypeDef(
    _ClientCheckDomainAvailabilityResponseTypeDef
):
    """
    Type definition for `ClientCheckDomainAvailability` `Response`

    The CheckDomainAvailability response includes the following elements.

    - **Availability** *(string) --*

      Whether the domain name is available for registering.

      .. note::

        You can register only domains designated as ``AVAILABLE`` .

      Valid values:

        AVAILABLE

      The domain name is available.

        AVAILABLE_RESERVED

      The domain name is reserved under specific conditions.

        AVAILABLE_PREORDER

      The domain name is available and can be preordered.

        DONT_KNOW

      The TLD registry didn't reply with a definitive answer about whether the domain name is
      available. Amazon Route 53 can return this response for a variety of reasons, for example,
      the registry is performing maintenance. Try again later.

        PENDING

      The TLD registry didn't return a response in the expected amount of time. When the response
      is delayed, it usually takes just a few extra seconds. You can resubmit the request
      immediately.

        RESERVED

      The domain name has been reserved for another person or organization.

        UNAVAILABLE

      The domain name is not available.

        UNAVAILABLE_PREMIUM

      The domain name is not available.

        UNAVAILABLE_RESTRICTED

      The domain name is forbidden.
    """


_ClientCheckDomainTransferabilityResponseTransferabilityTypeDef = TypedDict(
    "_ClientCheckDomainTransferabilityResponseTransferabilityTypeDef",
    {"Transferable": str},
    total=False,
)


class ClientCheckDomainTransferabilityResponseTransferabilityTypeDef(
    _ClientCheckDomainTransferabilityResponseTransferabilityTypeDef
):
    """
    Type definition for `ClientCheckDomainTransferabilityResponse` `Transferability`

    A complex type that contains information about whether the specified domain can be
    transferred to Amazon Route 53.

    - **Transferable** *(string) --*

      Whether the domain name can be transferred to Amazon Route 53.

      .. note::

        You can transfer only domains that have a value of ``TRANSFERABLE`` for ``Transferable`` .

      Valid values:

        TRANSFERABLE

      The domain name can be transferred to Amazon Route 53.

        UNTRANSFERRABLE

      The domain name can't be transferred to Amazon Route 53.

        DONT_KNOW

      Reserved for future use.
    """


_ClientCheckDomainTransferabilityResponseTypeDef = TypedDict(
    "_ClientCheckDomainTransferabilityResponseTypeDef",
    {"Transferability": ClientCheckDomainTransferabilityResponseTransferabilityTypeDef},
    total=False,
)


class ClientCheckDomainTransferabilityResponseTypeDef(
    _ClientCheckDomainTransferabilityResponseTypeDef
):
    """
    Type definition for `ClientCheckDomainTransferability` `Response`

    The CheckDomainTransferability response includes the following elements.

    - **Transferability** *(dict) --*

      A complex type that contains information about whether the specified domain can be
      transferred to Amazon Route 53.

      - **Transferable** *(string) --*

        Whether the domain name can be transferred to Amazon Route 53.

        .. note::

          You can transfer only domains that have a value of ``TRANSFERABLE`` for ``Transferable`` .

        Valid values:

          TRANSFERABLE

        The domain name can be transferred to Amazon Route 53.

          UNTRANSFERRABLE

        The domain name can't be transferred to Amazon Route 53.

          DONT_KNOW

        Reserved for future use.
    """


_ClientDisableDomainTransferLockResponseTypeDef = TypedDict(
    "_ClientDisableDomainTransferLockResponseTypeDef", {"OperationId": str}, total=False
)


class ClientDisableDomainTransferLockResponseTypeDef(
    _ClientDisableDomainTransferLockResponseTypeDef
):
    """
    Type definition for `ClientDisableDomainTransferLock` `Response`

    The DisableDomainTransferLock response includes the following element.

    - **OperationId** *(string) --*

      Identifier for tracking the progress of the request. To use this ID to query the operation
      status, use  GetOperationDetail .
    """


_ClientEnableDomainTransferLockResponseTypeDef = TypedDict(
    "_ClientEnableDomainTransferLockResponseTypeDef", {"OperationId": str}, total=False
)


class ClientEnableDomainTransferLockResponseTypeDef(
    _ClientEnableDomainTransferLockResponseTypeDef
):
    """
    Type definition for `ClientEnableDomainTransferLock` `Response`

    The EnableDomainTransferLock response includes the following elements.

    - **OperationId** *(string) --*

      Identifier for tracking the progress of the request. To use this ID to query the operation
      status, use GetOperationDetail.
    """


_ClientGetContactReachabilityStatusResponseTypeDef = TypedDict(
    "_ClientGetContactReachabilityStatusResponseTypeDef",
    {"domainName": str, "status": str},
    total=False,
)


class ClientGetContactReachabilityStatusResponseTypeDef(
    _ClientGetContactReachabilityStatusResponseTypeDef
):
    """
    Type definition for `ClientGetContactReachabilityStatus` `Response`

    - **domainName** *(string) --*

      The domain name for which you requested the reachability status.

    - **status** *(string) --*

      Whether the registrant contact has responded. Values include the following:

        PENDING

      We sent the confirmation email and haven't received a response yet.

        DONE

      We sent the email and got confirmation from the registrant contact.

        EXPIRED

      The time limit expired before the registrant contact responded.
    """


_ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef(
    _ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef
):
    """
    Type definition for `ClientGetDomainDetailResponseAdminContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --*

      Name of the additional parameter required by the top-level domain. Here are the
      top-level domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --*

      Values corresponding to the additional parameter names required by some top-level
      domains.
    """


_ClientGetDomainDetailResponseAdminContactTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseAdminContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[
            ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef
        ],
    },
    total=False,
)


class ClientGetDomainDetailResponseAdminContactTypeDef(
    _ClientGetDomainDetailResponseAdminContactTypeDef
):
    """
    Type definition for `ClientGetDomainDetailResponse` `AdminContact`

    Provides details about the domain administrative contact.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If
      you choose an option other than ``PERSON`` , you must enter an organization name, and you
      can't enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as
      ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as
      ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --*

          Name of the additional parameter required by the top-level domain. Here are the
          top-level domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --*

          Values corresponding to the additional parameter names required by some top-level
          domains.
    """


_ClientGetDomainDetailResponseNameserversTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseNameserversTypeDef",
    {"Name": str, "GlueIps": List[str]},
    total=False,
)


class ClientGetDomainDetailResponseNameserversTypeDef(
    _ClientGetDomainDetailResponseNameserversTypeDef
):
    """
    Type definition for `ClientGetDomainDetailResponse` `Nameservers`

    Nameserver includes the following elements.

    - **Name** *(string) --*

      The fully qualified host name of the name server.

      Constraint: Maximum 255 characters

    - **GlueIps** *(list) --*

      Glue IP address of a name server entry. Glue IP addresses are required only when the name
      of the name server is a subdomain of the domain. For example, if your domain is
      example.com and the name server for the domain is ns.example.com, you need to specify the
      IP address for ns.example.com.

      Constraints: The list can contain only one IPv4 and one IPv6 address.

      - *(string) --*
    """


_ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef(
    _ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef
):
    """
    Type definition for `ClientGetDomainDetailResponseRegistrantContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --*

      Name of the additional parameter required by the top-level domain. Here are the
      top-level domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --*

      Values corresponding to the additional parameter names required by some top-level
      domains.
    """


_ClientGetDomainDetailResponseRegistrantContactTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseRegistrantContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[
            ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef
        ],
    },
    total=False,
)


class ClientGetDomainDetailResponseRegistrantContactTypeDef(
    _ClientGetDomainDetailResponseRegistrantContactTypeDef
):
    """
    Type definition for `ClientGetDomainDetailResponse` `RegistrantContact`

    Provides details about the domain registrant.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If
      you choose an option other than ``PERSON`` , you must enter an organization name, and you
      can't enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as
      ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as
      ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --*

          Name of the additional parameter required by the top-level domain. Here are the
          top-level domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --*

          Values corresponding to the additional parameter names required by some top-level
          domains.
    """


_ClientGetDomainDetailResponseTechContactExtraParamsTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseTechContactExtraParamsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetDomainDetailResponseTechContactExtraParamsTypeDef(
    _ClientGetDomainDetailResponseTechContactExtraParamsTypeDef
):
    """
    Type definition for `ClientGetDomainDetailResponseTechContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --*

      Name of the additional parameter required by the top-level domain. Here are the
      top-level domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --*

      Values corresponding to the additional parameter names required by some top-level
      domains.
    """


_ClientGetDomainDetailResponseTechContactTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseTechContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientGetDomainDetailResponseTechContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientGetDomainDetailResponseTechContactTypeDef(
    _ClientGetDomainDetailResponseTechContactTypeDef
):
    """
    Type definition for `ClientGetDomainDetailResponse` `TechContact`

    Provides details about the domain technical contact.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If
      you choose an option other than ``PERSON`` , you must enter an organization name, and you
      can't enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as
      ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as
      ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --*

          Name of the additional parameter required by the top-level domain. Here are the
          top-level domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --*

          Values corresponding to the additional parameter names required by some top-level
          domains.
    """


_ClientGetDomainDetailResponseTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseTypeDef",
    {
        "DomainName": str,
        "Nameservers": List[ClientGetDomainDetailResponseNameserversTypeDef],
        "AutoRenew": bool,
        "AdminContact": ClientGetDomainDetailResponseAdminContactTypeDef,
        "RegistrantContact": ClientGetDomainDetailResponseRegistrantContactTypeDef,
        "TechContact": ClientGetDomainDetailResponseTechContactTypeDef,
        "AdminPrivacy": bool,
        "RegistrantPrivacy": bool,
        "TechPrivacy": bool,
        "RegistrarName": str,
        "WhoIsServer": str,
        "RegistrarUrl": str,
        "AbuseContactEmail": str,
        "AbuseContactPhone": str,
        "RegistryDomainId": str,
        "CreationDate": datetime,
        "UpdatedDate": datetime,
        "ExpirationDate": datetime,
        "Reseller": str,
        "DnsSec": str,
        "StatusList": List[str],
    },
    total=False,
)


class ClientGetDomainDetailResponseTypeDef(_ClientGetDomainDetailResponseTypeDef):
    """
    Type definition for `ClientGetDomainDetail` `Response`

    The GetDomainDetail response includes the following elements.

    - **DomainName** *(string) --*

      The name of a domain.

    - **Nameservers** *(list) --*

      The name of the domain.

      - *(dict) --*

        Nameserver includes the following elements.

        - **Name** *(string) --*

          The fully qualified host name of the name server.

          Constraint: Maximum 255 characters

        - **GlueIps** *(list) --*

          Glue IP address of a name server entry. Glue IP addresses are required only when the name
          of the name server is a subdomain of the domain. For example, if your domain is
          example.com and the name server for the domain is ns.example.com, you need to specify the
          IP address for ns.example.com.

          Constraints: The list can contain only one IPv4 and one IPv6 address.

          - *(string) --*

    - **AutoRenew** *(boolean) --*

      Specifies whether the domain registration is set to renew automatically.

    - **AdminContact** *(dict) --*

      Provides details about the domain administrative contact.

      - **FirstName** *(string) --*

        First name of contact.

      - **LastName** *(string) --*

        Last name of contact.

      - **ContactType** *(string) --*

        Indicates whether the contact is a person, company, association, or public organization. If
        you choose an option other than ``PERSON`` , you must enter an organization name, and you
        can't enable privacy protection for the contact.

      - **OrganizationName** *(string) --*

        Name of the organization for contact types other than ``PERSON`` .

      - **AddressLine1** *(string) --*

        First line of the contact's address.

      - **AddressLine2** *(string) --*

        Second line of contact's address, if any.

      - **City** *(string) --*

        The city of the contact's address.

      - **State** *(string) --*

        The state or province of the contact's city.

      - **CountryCode** *(string) --*

        Code for the country of the contact's address.

      - **ZipCode** *(string) --*

        The zip or postal code of the contact's address.

      - **PhoneNumber** *(string) --*

        The phone number of the contact.

        Constraints: Phone number must be specified in the format "+[country dialing code].[number
        including any area code>]". For example, a US phone number might appear as
        ``"+1.1234567890"`` .

      - **Email** *(string) --*

        Email address of the contact.

      - **Fax** *(string) --*

        Fax number of the contact.

        Constraints: Phone number must be specified in the format "+[country dialing code].[number
        including any area code]". For example, a US phone number might appear as
        ``"+1.1234567890"`` .

      - **ExtraParams** *(list) --*

        A list of name-value pairs for parameters required by certain top-level domains.

        - *(dict) --*

          ExtraParam includes the following elements.

          - **Name** *(string) --*

            Name of the additional parameter required by the top-level domain. Here are the
            top-level domains that require additional parameters and which parameters they require:

            * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

            * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

            * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

            * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
            ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

            * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
            ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

            * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

            * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

            * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

            * **.sg:**  ``SG_ID_NUMBER``

            * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

            In addition, many TLDs require ``VAT_NUMBER`` .

          - **Value** *(string) --*

            Values corresponding to the additional parameter names required by some top-level
            domains.

    - **RegistrantContact** *(dict) --*

      Provides details about the domain registrant.

      - **FirstName** *(string) --*

        First name of contact.

      - **LastName** *(string) --*

        Last name of contact.

      - **ContactType** *(string) --*

        Indicates whether the contact is a person, company, association, or public organization. If
        you choose an option other than ``PERSON`` , you must enter an organization name, and you
        can't enable privacy protection for the contact.

      - **OrganizationName** *(string) --*

        Name of the organization for contact types other than ``PERSON`` .

      - **AddressLine1** *(string) --*

        First line of the contact's address.

      - **AddressLine2** *(string) --*

        Second line of contact's address, if any.

      - **City** *(string) --*

        The city of the contact's address.

      - **State** *(string) --*

        The state or province of the contact's city.

      - **CountryCode** *(string) --*

        Code for the country of the contact's address.

      - **ZipCode** *(string) --*

        The zip or postal code of the contact's address.

      - **PhoneNumber** *(string) --*

        The phone number of the contact.

        Constraints: Phone number must be specified in the format "+[country dialing code].[number
        including any area code>]". For example, a US phone number might appear as
        ``"+1.1234567890"`` .

      - **Email** *(string) --*

        Email address of the contact.

      - **Fax** *(string) --*

        Fax number of the contact.

        Constraints: Phone number must be specified in the format "+[country dialing code].[number
        including any area code]". For example, a US phone number might appear as
        ``"+1.1234567890"`` .

      - **ExtraParams** *(list) --*

        A list of name-value pairs for parameters required by certain top-level domains.

        - *(dict) --*

          ExtraParam includes the following elements.

          - **Name** *(string) --*

            Name of the additional parameter required by the top-level domain. Here are the
            top-level domains that require additional parameters and which parameters they require:

            * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

            * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

            * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

            * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
            ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

            * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
            ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

            * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

            * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

            * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

            * **.sg:**  ``SG_ID_NUMBER``

            * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

            In addition, many TLDs require ``VAT_NUMBER`` .

          - **Value** *(string) --*

            Values corresponding to the additional parameter names required by some top-level
            domains.

    - **TechContact** *(dict) --*

      Provides details about the domain technical contact.

      - **FirstName** *(string) --*

        First name of contact.

      - **LastName** *(string) --*

        Last name of contact.

      - **ContactType** *(string) --*

        Indicates whether the contact is a person, company, association, or public organization. If
        you choose an option other than ``PERSON`` , you must enter an organization name, and you
        can't enable privacy protection for the contact.

      - **OrganizationName** *(string) --*

        Name of the organization for contact types other than ``PERSON`` .

      - **AddressLine1** *(string) --*

        First line of the contact's address.

      - **AddressLine2** *(string) --*

        Second line of contact's address, if any.

      - **City** *(string) --*

        The city of the contact's address.

      - **State** *(string) --*

        The state or province of the contact's city.

      - **CountryCode** *(string) --*

        Code for the country of the contact's address.

      - **ZipCode** *(string) --*

        The zip or postal code of the contact's address.

      - **PhoneNumber** *(string) --*

        The phone number of the contact.

        Constraints: Phone number must be specified in the format "+[country dialing code].[number
        including any area code>]". For example, a US phone number might appear as
        ``"+1.1234567890"`` .

      - **Email** *(string) --*

        Email address of the contact.

      - **Fax** *(string) --*

        Fax number of the contact.

        Constraints: Phone number must be specified in the format "+[country dialing code].[number
        including any area code]". For example, a US phone number might appear as
        ``"+1.1234567890"`` .

      - **ExtraParams** *(list) --*

        A list of name-value pairs for parameters required by certain top-level domains.

        - *(dict) --*

          ExtraParam includes the following elements.

          - **Name** *(string) --*

            Name of the additional parameter required by the top-level domain. Here are the
            top-level domains that require additional parameters and which parameters they require:

            * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

            * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

            * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

            * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
            ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

            * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
            ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

            * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

            * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

            * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

            * **.sg:**  ``SG_ID_NUMBER``

            * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

            In addition, many TLDs require ``VAT_NUMBER`` .

          - **Value** *(string) --*

            Values corresponding to the additional parameter names required by some top-level
            domains.

    - **AdminPrivacy** *(boolean) --*

      Specifies whether contact information is concealed from WHOIS queries. If the value is
      ``true`` , WHOIS ("who is") queries return contact information either for Amazon Registrar
      (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other
      TLDs). If the value is ``false`` , WHOIS queries return the information that you entered for
      the admin contact.

    - **RegistrantPrivacy** *(boolean) --*

      Specifies whether contact information is concealed from WHOIS queries. If the value is
      ``true`` , WHOIS ("who is") queries return contact information either for Amazon Registrar
      (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other
      TLDs). If the value is ``false`` , WHOIS queries return the information that you entered for
      the registrant contact (domain owner).

    - **TechPrivacy** *(boolean) --*

      Specifies whether contact information is concealed from WHOIS queries. If the value is
      ``true`` , WHOIS ("who is") queries return contact information either for Amazon Registrar
      (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other
      TLDs). If the value is ``false`` , WHOIS queries return the information that you entered for
      the technical contact.

    - **RegistrarName** *(string) --*

      Name of the registrar of the domain as identified in the registry. Domains with a .com, .net,
      or .org TLD are registered by Amazon Registrar. All other domains are registered by our
      registrar associate, Gandi. The value for domains that are registered by Gandi is ``"GANDI
      SAS"`` .

    - **WhoIsServer** *(string) --*

      The fully qualified name of the WHOIS server that can answer the WHOIS query for the domain.

    - **RegistrarUrl** *(string) --*

      Web address of the registrar.

    - **AbuseContactEmail** *(string) --*

      Email address to contact to report incorrect contact information for a domain, to report that
      the domain is being used to send spam, to report that someone is cybersquatting on a domain
      name, or report some other type of abuse.

    - **AbuseContactPhone** *(string) --*

      Phone number for reporting abuse.

    - **RegistryDomainId** *(string) --*

      Reserved for future use.

    - **CreationDate** *(datetime) --*

      The date when the domain was created as found in the response to a WHOIS query. The date and
      time is in Coordinated Universal time (UTC).

    - **UpdatedDate** *(datetime) --*

      The last updated date of the domain as found in the response to a WHOIS query. The date and
      time is in Coordinated Universal time (UTC).

    - **ExpirationDate** *(datetime) --*

      The date when the registration for the domain is set to expire. The date and time is in
      Coordinated Universal time (UTC).

    - **Reseller** *(string) --*

      Reseller of the domain. Domains registered or transferred using Amazon Route 53 domains will
      have ``"Amazon"`` as the reseller.

    - **DnsSec** *(string) --*

      Reserved for future use.

    - **StatusList** *(list) --*

      An array of domain name status codes, also known as Extensible Provisioning Protocol (EPP)
      status codes.

      ICANN, the organization that maintains a central database of domain names, has developed a
      set of domain name status codes that tell you the status of a variety of operations on a
      domain name, for example, registering a domain name, transferring a domain name to another
      registrar, renewing the registration for a domain name, and so on. All registrars use this
      same set of status codes.

      For a current list of domain name status codes and an explanation of what each code means, go
      to the `ICANN website <https://www.icann.org/>`__ and search for ``epp status codes`` .
      (Search on the ICANN website; web searches sometimes return an old version of the document.)

      - *(string) --*
    """


_ClientGetDomainSuggestionsResponseSuggestionsListTypeDef = TypedDict(
    "_ClientGetDomainSuggestionsResponseSuggestionsListTypeDef",
    {"DomainName": str, "Availability": str},
    total=False,
)


class ClientGetDomainSuggestionsResponseSuggestionsListTypeDef(
    _ClientGetDomainSuggestionsResponseSuggestionsListTypeDef
):
    """
    Type definition for `ClientGetDomainSuggestionsResponse` `SuggestionsList`

    Information about one suggested domain name.

    - **DomainName** *(string) --*

      A suggested domain name.

    - **Availability** *(string) --*

      Whether the domain name is available for registering.

      .. note::

        You can register only the domains that are designated as ``AVAILABLE`` .

      Valid values:

        AVAILABLE

      The domain name is available.

        AVAILABLE_RESERVED

      The domain name is reserved under specific conditions.

        AVAILABLE_PREORDER

      The domain name is available and can be preordered.

        DONT_KNOW

      The TLD registry didn't reply with a definitive answer about whether the domain name is
      available. Amazon Route 53 can return this response for a variety of reasons, for
      example, the registry is performing maintenance. Try again later.

        PENDING

      The TLD registry didn't return a response in the expected amount of time. When the
      response is delayed, it usually takes just a few extra seconds. You can resubmit the
      request immediately.

        RESERVED

      The domain name has been reserved for another person or organization.

        UNAVAILABLE

      The domain name is not available.

        UNAVAILABLE_PREMIUM

      The domain name is not available.

        UNAVAILABLE_RESTRICTED

      The domain name is forbidden.
    """


_ClientGetDomainSuggestionsResponseTypeDef = TypedDict(
    "_ClientGetDomainSuggestionsResponseTypeDef",
    {"SuggestionsList": List[ClientGetDomainSuggestionsResponseSuggestionsListTypeDef]},
    total=False,
)


class ClientGetDomainSuggestionsResponseTypeDef(
    _ClientGetDomainSuggestionsResponseTypeDef
):
    """
    Type definition for `ClientGetDomainSuggestions` `Response`

    - **SuggestionsList** *(list) --*

      A list of possible domain names. If you specified ``true`` for ``OnlyAvailable`` in the
      request, the list contains only domains that are available for registration.

      - *(dict) --*

        Information about one suggested domain name.

        - **DomainName** *(string) --*

          A suggested domain name.

        - **Availability** *(string) --*

          Whether the domain name is available for registering.

          .. note::

            You can register only the domains that are designated as ``AVAILABLE`` .

          Valid values:

            AVAILABLE

          The domain name is available.

            AVAILABLE_RESERVED

          The domain name is reserved under specific conditions.

            AVAILABLE_PREORDER

          The domain name is available and can be preordered.

            DONT_KNOW

          The TLD registry didn't reply with a definitive answer about whether the domain name is
          available. Amazon Route 53 can return this response for a variety of reasons, for
          example, the registry is performing maintenance. Try again later.

            PENDING

          The TLD registry didn't return a response in the expected amount of time. When the
          response is delayed, it usually takes just a few extra seconds. You can resubmit the
          request immediately.

            RESERVED

          The domain name has been reserved for another person or organization.

            UNAVAILABLE

          The domain name is not available.

            UNAVAILABLE_PREMIUM

          The domain name is not available.

            UNAVAILABLE_RESTRICTED

          The domain name is forbidden.
    """


_ClientGetOperationDetailResponseTypeDef = TypedDict(
    "_ClientGetOperationDetailResponseTypeDef",
    {
        "OperationId": str,
        "Status": str,
        "Message": str,
        "DomainName": str,
        "Type": str,
        "SubmittedDate": datetime,
    },
    total=False,
)


class ClientGetOperationDetailResponseTypeDef(_ClientGetOperationDetailResponseTypeDef):
    """
    Type definition for `ClientGetOperationDetail` `Response`

    The GetOperationDetail response includes the following elements.

    - **OperationId** *(string) --*

      The identifier for the operation.

    - **Status** *(string) --*

      The current status of the requested operation in the system.

    - **Message** *(string) --*

      Detailed information on the status including possible errors.

    - **DomainName** *(string) --*

      The name of a domain.

    - **Type** *(string) --*

      The type of operation that was requested.

    - **SubmittedDate** *(datetime) --*

      The date when the request was submitted.
    """


_ClientListDomainsResponseDomainsTypeDef = TypedDict(
    "_ClientListDomainsResponseDomainsTypeDef",
    {"DomainName": str, "AutoRenew": bool, "TransferLock": bool, "Expiry": datetime},
    total=False,
)


class ClientListDomainsResponseDomainsTypeDef(_ClientListDomainsResponseDomainsTypeDef):
    """
    Type definition for `ClientListDomainsResponse` `Domains`

    Summary information about one domain.

    - **DomainName** *(string) --*

      The name of the domain that the summary information applies to.

    - **AutoRenew** *(boolean) --*

      Indicates whether the domain is automatically renewed upon expiration.

    - **TransferLock** *(boolean) --*

      Indicates whether a domain is locked from unauthorized transfer to another party.

    - **Expiry** *(datetime) --*

      Expiration date of the domain in Coordinated Universal Time (UTC).
    """


_ClientListDomainsResponseTypeDef = TypedDict(
    "_ClientListDomainsResponseTypeDef",
    {"Domains": List[ClientListDomainsResponseDomainsTypeDef], "NextPageMarker": str},
    total=False,
)


class ClientListDomainsResponseTypeDef(_ClientListDomainsResponseTypeDef):
    """
    Type definition for `ClientListDomains` `Response`

    The ListDomains response includes the following elements.

    - **Domains** *(list) --*

      A summary of domains.

      - *(dict) --*

        Summary information about one domain.

        - **DomainName** *(string) --*

          The name of the domain that the summary information applies to.

        - **AutoRenew** *(boolean) --*

          Indicates whether the domain is automatically renewed upon expiration.

        - **TransferLock** *(boolean) --*

          Indicates whether a domain is locked from unauthorized transfer to another party.

        - **Expiry** *(datetime) --*

          Expiration date of the domain in Coordinated Universal Time (UTC).

    - **NextPageMarker** *(string) --*

      If there are more domains than you specified for ``MaxItems`` in the request, submit another
      request and include the value of ``NextPageMarker`` in the value of ``Marker`` .
    """


_ClientListOperationsResponseOperationsTypeDef = TypedDict(
    "_ClientListOperationsResponseOperationsTypeDef",
    {"OperationId": str, "Status": str, "Type": str, "SubmittedDate": datetime},
    total=False,
)


class ClientListOperationsResponseOperationsTypeDef(
    _ClientListOperationsResponseOperationsTypeDef
):
    """
    Type definition for `ClientListOperationsResponse` `Operations`

    OperationSummary includes the following elements.

    - **OperationId** *(string) --*

      Identifier returned to track the requested action.

    - **Status** *(string) --*

      The current status of the requested operation in the system.

    - **Type** *(string) --*

      Type of the action requested.

    - **SubmittedDate** *(datetime) --*

      The date when the request was submitted.
    """


_ClientListOperationsResponseTypeDef = TypedDict(
    "_ClientListOperationsResponseTypeDef",
    {
        "Operations": List[ClientListOperationsResponseOperationsTypeDef],
        "NextPageMarker": str,
    },
    total=False,
)


class ClientListOperationsResponseTypeDef(_ClientListOperationsResponseTypeDef):
    """
    Type definition for `ClientListOperations` `Response`

    The ListOperations response includes the following elements.

    - **Operations** *(list) --*

      Lists summaries of the operations.

      - *(dict) --*

        OperationSummary includes the following elements.

        - **OperationId** *(string) --*

          Identifier returned to track the requested action.

        - **Status** *(string) --*

          The current status of the requested operation in the system.

        - **Type** *(string) --*

          Type of the action requested.

        - **SubmittedDate** *(datetime) --*

          The date when the request was submitted.

    - **NextPageMarker** *(string) --*

      If there are more operations than you specified for ``MaxItems`` in the request, submit
      another request and include the value of ``NextPageMarker`` in the value of ``Marker`` .
    """


_ClientListTagsForDomainResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForDomainResponseTagListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForDomainResponseTagListTypeDef(
    _ClientListTagsForDomainResponseTagListTypeDef
):
    """
    Type definition for `ClientListTagsForDomainResponse` `TagList`

    Each tag includes the following elements.

    - **Key** *(string) --*

      The key (name) of a tag.

      Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"

      Constraints: Each key can be 1-128 characters long.

    - **Value** *(string) --*

      The value of a tag.

      Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"

      Constraints: Each value can be 0-256 characters long.
    """


_ClientListTagsForDomainResponseTypeDef = TypedDict(
    "_ClientListTagsForDomainResponseTypeDef",
    {"TagList": List[ClientListTagsForDomainResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForDomainResponseTypeDef(_ClientListTagsForDomainResponseTypeDef):
    """
    Type definition for `ClientListTagsForDomain` `Response`

    The ListTagsForDomain response includes the following elements.

    - **TagList** *(list) --*

      A list of the tags that are associated with the specified domain.

      - *(dict) --*

        Each tag includes the following elements.

        - **Key** *(string) --*

          The key (name) of a tag.

          Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"

          Constraints: Each key can be 1-128 characters long.

        - **Value** *(string) --*

          The value of a tag.

          Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"

          Constraints: Each value can be 0-256 characters long.
    """


_ClientRegisterDomainAdminContactExtraParamsTypeDef = TypedDict(
    "_ClientRegisterDomainAdminContactExtraParamsTypeDef", {"Name": str, "Value": str}
)


class ClientRegisterDomainAdminContactExtraParamsTypeDef(
    _ClientRegisterDomainAdminContactExtraParamsTypeDef
):
    """
    Type definition for `ClientRegisterDomainAdminContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the additional parameter required by the top-level domain. Here are the top-level
      domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --* **[REQUIRED]**

      Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientRegisterDomainAdminContactTypeDef = TypedDict(
    "_ClientRegisterDomainAdminContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientRegisterDomainAdminContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientRegisterDomainAdminContactTypeDef(_ClientRegisterDomainAdminContactTypeDef):
    """
    Type definition for `ClientRegisterDomain` `AdminContact`

    Provides detailed contact information.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If you
      choose an option other than ``PERSON`` , you must enter an organization name, and you can't
      enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the additional parameter required by the top-level domain. Here are the top-level
          domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --* **[REQUIRED]**

          Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientRegisterDomainRegistrantContactExtraParamsTypeDef = TypedDict(
    "_ClientRegisterDomainRegistrantContactExtraParamsTypeDef",
    {"Name": str, "Value": str},
)


class ClientRegisterDomainRegistrantContactExtraParamsTypeDef(
    _ClientRegisterDomainRegistrantContactExtraParamsTypeDef
):
    """
    Type definition for `ClientRegisterDomainRegistrantContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the additional parameter required by the top-level domain. Here are the top-level
      domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --* **[REQUIRED]**

      Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientRegisterDomainRegistrantContactTypeDef = TypedDict(
    "_ClientRegisterDomainRegistrantContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientRegisterDomainRegistrantContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientRegisterDomainRegistrantContactTypeDef(
    _ClientRegisterDomainRegistrantContactTypeDef
):
    """
    Type definition for `ClientRegisterDomain` `RegistrantContact`

    Provides detailed contact information.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If you
      choose an option other than ``PERSON`` , you must enter an organization name, and you can't
      enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the additional parameter required by the top-level domain. Here are the top-level
          domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --* **[REQUIRED]**

          Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientRegisterDomainResponseTypeDef = TypedDict(
    "_ClientRegisterDomainResponseTypeDef", {"OperationId": str}, total=False
)


class ClientRegisterDomainResponseTypeDef(_ClientRegisterDomainResponseTypeDef):
    """
    Type definition for `ClientRegisterDomain` `Response`

    The RegisterDomain response includes the following element.

    - **OperationId** *(string) --*

      Identifier for tracking the progress of the request. To use this ID to query the operation
      status, use  GetOperationDetail .
    """


_ClientRegisterDomainTechContactExtraParamsTypeDef = TypedDict(
    "_ClientRegisterDomainTechContactExtraParamsTypeDef", {"Name": str, "Value": str}
)


class ClientRegisterDomainTechContactExtraParamsTypeDef(
    _ClientRegisterDomainTechContactExtraParamsTypeDef
):
    """
    Type definition for `ClientRegisterDomainTechContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the additional parameter required by the top-level domain. Here are the top-level
      domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --* **[REQUIRED]**

      Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientRegisterDomainTechContactTypeDef = TypedDict(
    "_ClientRegisterDomainTechContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientRegisterDomainTechContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientRegisterDomainTechContactTypeDef(_ClientRegisterDomainTechContactTypeDef):
    """
    Type definition for `ClientRegisterDomain` `TechContact`

    Provides detailed contact information.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If you
      choose an option other than ``PERSON`` , you must enter an organization name, and you can't
      enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the additional parameter required by the top-level domain. Here are the top-level
          domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --* **[REQUIRED]**

          Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientRenewDomainResponseTypeDef = TypedDict(
    "_ClientRenewDomainResponseTypeDef", {"OperationId": str}, total=False
)


class ClientRenewDomainResponseTypeDef(_ClientRenewDomainResponseTypeDef):
    """
    Type definition for `ClientRenewDomain` `Response`

    - **OperationId** *(string) --*

      The identifier for tracking the progress of the request. To use this ID to query the
      operation status, use  GetOperationDetail .
    """


_ClientResendContactReachabilityEmailResponseTypeDef = TypedDict(
    "_ClientResendContactReachabilityEmailResponseTypeDef",
    {"domainName": str, "emailAddress": str, "isAlreadyVerified": bool},
    total=False,
)


class ClientResendContactReachabilityEmailResponseTypeDef(
    _ClientResendContactReachabilityEmailResponseTypeDef
):
    """
    Type definition for `ClientResendContactReachabilityEmail` `Response`

    - **domainName** *(string) --*

      The domain name for which you requested a confirmation email.

    - **emailAddress** *(string) --*

      The email address for the registrant contact at the time that we sent the verification email.

    - **isAlreadyVerified** *(boolean) --*

       ``True`` if the email address for the registrant contact has already been verified, and
       ``false`` otherwise. If the email address has already been verified, we don't send another
       confirmation email.
    """


_ClientRetrieveDomainAuthCodeResponseTypeDef = TypedDict(
    "_ClientRetrieveDomainAuthCodeResponseTypeDef", {"AuthCode": str}, total=False
)


class ClientRetrieveDomainAuthCodeResponseTypeDef(
    _ClientRetrieveDomainAuthCodeResponseTypeDef
):
    """
    Type definition for `ClientRetrieveDomainAuthCode` `Response`

    The RetrieveDomainAuthCode response includes the following element.

    - **AuthCode** *(string) --*

      The authorization code for the domain.
    """


_ClientTransferDomainAdminContactExtraParamsTypeDef = TypedDict(
    "_ClientTransferDomainAdminContactExtraParamsTypeDef", {"Name": str, "Value": str}
)


class ClientTransferDomainAdminContactExtraParamsTypeDef(
    _ClientTransferDomainAdminContactExtraParamsTypeDef
):
    """
    Type definition for `ClientTransferDomainAdminContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the additional parameter required by the top-level domain. Here are the top-level
      domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --* **[REQUIRED]**

      Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientTransferDomainAdminContactTypeDef = TypedDict(
    "_ClientTransferDomainAdminContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientTransferDomainAdminContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientTransferDomainAdminContactTypeDef(_ClientTransferDomainAdminContactTypeDef):
    """
    Type definition for `ClientTransferDomain` `AdminContact`

    Provides detailed contact information.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If you
      choose an option other than ``PERSON`` , you must enter an organization name, and you can't
      enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the additional parameter required by the top-level domain. Here are the top-level
          domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --* **[REQUIRED]**

          Values corresponding to the additional parameter names required by some top-level domains.
    """


_RequiredClientTransferDomainNameserversTypeDef = TypedDict(
    "_RequiredClientTransferDomainNameserversTypeDef", {"Name": str}
)
_OptionalClientTransferDomainNameserversTypeDef = TypedDict(
    "_OptionalClientTransferDomainNameserversTypeDef",
    {"GlueIps": List[str]},
    total=False,
)


class ClientTransferDomainNameserversTypeDef(
    _RequiredClientTransferDomainNameserversTypeDef,
    _OptionalClientTransferDomainNameserversTypeDef,
):
    """
    Type definition for `ClientTransferDomain` `Nameservers`

    Nameserver includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      The fully qualified host name of the name server.

      Constraint: Maximum 255 characters

    - **GlueIps** *(list) --*

      Glue IP address of a name server entry. Glue IP addresses are required only when the name of
      the name server is a subdomain of the domain. For example, if your domain is example.com and
      the name server for the domain is ns.example.com, you need to specify the IP address for
      ns.example.com.

      Constraints: The list can contain only one IPv4 and one IPv6 address.

      - *(string) --*
    """


_ClientTransferDomainRegistrantContactExtraParamsTypeDef = TypedDict(
    "_ClientTransferDomainRegistrantContactExtraParamsTypeDef",
    {"Name": str, "Value": str},
)


class ClientTransferDomainRegistrantContactExtraParamsTypeDef(
    _ClientTransferDomainRegistrantContactExtraParamsTypeDef
):
    """
    Type definition for `ClientTransferDomainRegistrantContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the additional parameter required by the top-level domain. Here are the top-level
      domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --* **[REQUIRED]**

      Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientTransferDomainRegistrantContactTypeDef = TypedDict(
    "_ClientTransferDomainRegistrantContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientTransferDomainRegistrantContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientTransferDomainRegistrantContactTypeDef(
    _ClientTransferDomainRegistrantContactTypeDef
):
    """
    Type definition for `ClientTransferDomain` `RegistrantContact`

    Provides detailed contact information.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If you
      choose an option other than ``PERSON`` , you must enter an organization name, and you can't
      enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the additional parameter required by the top-level domain. Here are the top-level
          domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --* **[REQUIRED]**

          Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientTransferDomainResponseTypeDef = TypedDict(
    "_ClientTransferDomainResponseTypeDef", {"OperationId": str}, total=False
)


class ClientTransferDomainResponseTypeDef(_ClientTransferDomainResponseTypeDef):
    """
    Type definition for `ClientTransferDomain` `Response`

    The TranserDomain response includes the following element.

    - **OperationId** *(string) --*

      Identifier for tracking the progress of the request. To use this ID to query the operation
      status, use  GetOperationDetail .
    """


_ClientTransferDomainTechContactExtraParamsTypeDef = TypedDict(
    "_ClientTransferDomainTechContactExtraParamsTypeDef", {"Name": str, "Value": str}
)


class ClientTransferDomainTechContactExtraParamsTypeDef(
    _ClientTransferDomainTechContactExtraParamsTypeDef
):
    """
    Type definition for `ClientTransferDomainTechContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the additional parameter required by the top-level domain. Here are the top-level
      domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --* **[REQUIRED]**

      Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientTransferDomainTechContactTypeDef = TypedDict(
    "_ClientTransferDomainTechContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientTransferDomainTechContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientTransferDomainTechContactTypeDef(_ClientTransferDomainTechContactTypeDef):
    """
    Type definition for `ClientTransferDomain` `TechContact`

    Provides detailed contact information.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If you
      choose an option other than ``PERSON`` , you must enter an organization name, and you can't
      enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the additional parameter required by the top-level domain. Here are the top-level
          domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --* **[REQUIRED]**

          Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientUpdateDomainContactAdminContactExtraParamsTypeDef = TypedDict(
    "_ClientUpdateDomainContactAdminContactExtraParamsTypeDef",
    {"Name": str, "Value": str},
)


class ClientUpdateDomainContactAdminContactExtraParamsTypeDef(
    _ClientUpdateDomainContactAdminContactExtraParamsTypeDef
):
    """
    Type definition for `ClientUpdateDomainContactAdminContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the additional parameter required by the top-level domain. Here are the top-level
      domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --* **[REQUIRED]**

      Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientUpdateDomainContactAdminContactTypeDef = TypedDict(
    "_ClientUpdateDomainContactAdminContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientUpdateDomainContactAdminContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientUpdateDomainContactAdminContactTypeDef(
    _ClientUpdateDomainContactAdminContactTypeDef
):
    """
    Type definition for `ClientUpdateDomainContact` `AdminContact`

    Provides detailed contact information.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If you
      choose an option other than ``PERSON`` , you must enter an organization name, and you can't
      enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the additional parameter required by the top-level domain. Here are the top-level
          domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --* **[REQUIRED]**

          Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientUpdateDomainContactPrivacyResponseTypeDef = TypedDict(
    "_ClientUpdateDomainContactPrivacyResponseTypeDef",
    {"OperationId": str},
    total=False,
)


class ClientUpdateDomainContactPrivacyResponseTypeDef(
    _ClientUpdateDomainContactPrivacyResponseTypeDef
):
    """
    Type definition for `ClientUpdateDomainContactPrivacy` `Response`

    The UpdateDomainContactPrivacy response includes the following element.

    - **OperationId** *(string) --*

      Identifier for tracking the progress of the request. To use this ID to query the operation
      status, use GetOperationDetail.
    """


_ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef = TypedDict(
    "_ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef",
    {"Name": str, "Value": str},
)


class ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef(
    _ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef
):
    """
    Type definition for `ClientUpdateDomainContactRegistrantContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the additional parameter required by the top-level domain. Here are the top-level
      domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --* **[REQUIRED]**

      Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientUpdateDomainContactRegistrantContactTypeDef = TypedDict(
    "_ClientUpdateDomainContactRegistrantContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[
            ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDomainContactRegistrantContactTypeDef(
    _ClientUpdateDomainContactRegistrantContactTypeDef
):
    """
    Type definition for `ClientUpdateDomainContact` `RegistrantContact`

    Provides detailed contact information.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If you
      choose an option other than ``PERSON`` , you must enter an organization name, and you can't
      enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the additional parameter required by the top-level domain. Here are the top-level
          domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --* **[REQUIRED]**

          Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientUpdateDomainContactResponseTypeDef = TypedDict(
    "_ClientUpdateDomainContactResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateDomainContactResponseTypeDef(
    _ClientUpdateDomainContactResponseTypeDef
):
    """
    Type definition for `ClientUpdateDomainContact` `Response`

    The UpdateDomainContact response includes the following element.

    - **OperationId** *(string) --*

      Identifier for tracking the progress of the request. To use this ID to query the operation
      status, use  GetOperationDetail .
    """


_ClientUpdateDomainContactTechContactExtraParamsTypeDef = TypedDict(
    "_ClientUpdateDomainContactTechContactExtraParamsTypeDef",
    {"Name": str, "Value": str},
)


class ClientUpdateDomainContactTechContactExtraParamsTypeDef(
    _ClientUpdateDomainContactTechContactExtraParamsTypeDef
):
    """
    Type definition for `ClientUpdateDomainContactTechContact` `ExtraParams`

    ExtraParam includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      Name of the additional parameter required by the top-level domain. Here are the top-level
      domains that require additional parameters and which parameters they require:

      * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

      * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

      * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

      * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
      ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

      * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
      ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

      * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

      * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

      * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

      * **.sg:**  ``SG_ID_NUMBER``

      * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

      In addition, many TLDs require ``VAT_NUMBER`` .

    - **Value** *(string) --* **[REQUIRED]**

      Values corresponding to the additional parameter names required by some top-level domains.
    """


_ClientUpdateDomainContactTechContactTypeDef = TypedDict(
    "_ClientUpdateDomainContactTechContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": str,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": str,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientUpdateDomainContactTechContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientUpdateDomainContactTechContactTypeDef(
    _ClientUpdateDomainContactTechContactTypeDef
):
    """
    Type definition for `ClientUpdateDomainContact` `TechContact`

    Provides detailed contact information.

    - **FirstName** *(string) --*

      First name of contact.

    - **LastName** *(string) --*

      Last name of contact.

    - **ContactType** *(string) --*

      Indicates whether the contact is a person, company, association, or public organization. If you
      choose an option other than ``PERSON`` , you must enter an organization name, and you can't
      enable privacy protection for the contact.

    - **OrganizationName** *(string) --*

      Name of the organization for contact types other than ``PERSON`` .

    - **AddressLine1** *(string) --*

      First line of the contact's address.

    - **AddressLine2** *(string) --*

      Second line of contact's address, if any.

    - **City** *(string) --*

      The city of the contact's address.

    - **State** *(string) --*

      The state or province of the contact's city.

    - **CountryCode** *(string) --*

      Code for the country of the contact's address.

    - **ZipCode** *(string) --*

      The zip or postal code of the contact's address.

    - **PhoneNumber** *(string) --*

      The phone number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code>]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **Email** *(string) --*

      Email address of the contact.

    - **Fax** *(string) --*

      Fax number of the contact.

      Constraints: Phone number must be specified in the format "+[country dialing code].[number
      including any area code]". For example, a US phone number might appear as ``"+1.1234567890"`` .

    - **ExtraParams** *(list) --*

      A list of name-value pairs for parameters required by certain top-level domains.

      - *(dict) --*

        ExtraParam includes the following elements.

        - **Name** *(string) --* **[REQUIRED]**

          Name of the additional parameter required by the top-level domain. Here are the top-level
          domains that require additional parameters and which parameters they require:

          * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``

          * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``

          * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``

          * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` ,
          ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``

          * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` ,
          ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``

          * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``

          * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``

          * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``

          * **.sg:**  ``SG_ID_NUMBER``

          * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``

          In addition, many TLDs require ``VAT_NUMBER`` .

        - **Value** *(string) --* **[REQUIRED]**

          Values corresponding to the additional parameter names required by some top-level domains.
    """


_RequiredClientUpdateDomainNameserversNameserversTypeDef = TypedDict(
    "_RequiredClientUpdateDomainNameserversNameserversTypeDef", {"Name": str}
)
_OptionalClientUpdateDomainNameserversNameserversTypeDef = TypedDict(
    "_OptionalClientUpdateDomainNameserversNameserversTypeDef",
    {"GlueIps": List[str]},
    total=False,
)


class ClientUpdateDomainNameserversNameserversTypeDef(
    _RequiredClientUpdateDomainNameserversNameserversTypeDef,
    _OptionalClientUpdateDomainNameserversNameserversTypeDef,
):
    """
    Type definition for `ClientUpdateDomainNameservers` `Nameservers`

    Nameserver includes the following elements.

    - **Name** *(string) --* **[REQUIRED]**

      The fully qualified host name of the name server.

      Constraint: Maximum 255 characters

    - **GlueIps** *(list) --*

      Glue IP address of a name server entry. Glue IP addresses are required only when the name of
      the name server is a subdomain of the domain. For example, if your domain is example.com and
      the name server for the domain is ns.example.com, you need to specify the IP address for
      ns.example.com.

      Constraints: The list can contain only one IPv4 and one IPv6 address.

      - *(string) --*
    """


_ClientUpdateDomainNameserversResponseTypeDef = TypedDict(
    "_ClientUpdateDomainNameserversResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateDomainNameserversResponseTypeDef(
    _ClientUpdateDomainNameserversResponseTypeDef
):
    """
    Type definition for `ClientUpdateDomainNameservers` `Response`

    The UpdateDomainNameservers response includes the following element.

    - **OperationId** *(string) --*

      Identifier for tracking the progress of the request. To use this ID to query the operation
      status, use  GetOperationDetail .
    """


_ClientUpdateTagsForDomainTagsToUpdateTypeDef = TypedDict(
    "_ClientUpdateTagsForDomainTagsToUpdateTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateTagsForDomainTagsToUpdateTypeDef(
    _ClientUpdateTagsForDomainTagsToUpdateTypeDef
):
    """
    Type definition for `ClientUpdateTagsForDomain` `TagsToUpdate`

    Each tag includes the following elements.

    - **Key** *(string) --*

      The key (name) of a tag.

      Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"

      Constraints: Each key can be 1-128 characters long.

    - **Value** *(string) --*

      The value of a tag.

      Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"

      Constraints: Each value can be 0-256 characters long.
    """


_ClientViewBillingResponseBillingRecordsTypeDef = TypedDict(
    "_ClientViewBillingResponseBillingRecordsTypeDef",
    {
        "DomainName": str,
        "Operation": str,
        "InvoiceId": str,
        "BillDate": datetime,
        "Price": float,
    },
    total=False,
)


class ClientViewBillingResponseBillingRecordsTypeDef(
    _ClientViewBillingResponseBillingRecordsTypeDef
):
    """
    Type definition for `ClientViewBillingResponse` `BillingRecords`

    Information for one billing record.

    - **DomainName** *(string) --*

      The name of the domain that the billing record applies to. If the domain name contains
      characters other than a-z, 0-9, and - (hyphen), such as an internationalized domain name,
      then this value is in Punycode. For more information, see `DNS Domain Name Format
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in
      the *Amazon Route 53 Developer Guidezzz* .

    - **Operation** *(string) --*

      The operation that you were charged for.

    - **InvoiceId** *(string) --*

      The ID of the invoice that is associated with the billing record.

    - **BillDate** *(datetime) --*

      The date that the operation was billed, in Unix format.

    - **Price** *(float) --*

      The price that you were charged for the operation, in US dollars.

      Example value: 12.0
    """


_ClientViewBillingResponseTypeDef = TypedDict(
    "_ClientViewBillingResponseTypeDef",
    {
        "NextPageMarker": str,
        "BillingRecords": List[ClientViewBillingResponseBillingRecordsTypeDef],
    },
    total=False,
)


class ClientViewBillingResponseTypeDef(_ClientViewBillingResponseTypeDef):
    """
    Type definition for `ClientViewBilling` `Response`

    The ViewBilling response includes the following elements.

    - **NextPageMarker** *(string) --*

      If there are more billing records than you specified for ``MaxItems`` in the request, submit
      another request and include the value of ``NextPageMarker`` in the value of ``Marker`` .

    - **BillingRecords** *(list) --*

      A summary of billing records.

      - *(dict) --*

        Information for one billing record.

        - **DomainName** *(string) --*

          The name of the domain that the billing record applies to. If the domain name contains
          characters other than a-z, 0-9, and - (hyphen), such as an internationalized domain name,
          then this value is in Punycode. For more information, see `DNS Domain Name Format
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in
          the *Amazon Route 53 Developer Guidezzz* .

        - **Operation** *(string) --*

          The operation that you were charged for.

        - **InvoiceId** *(string) --*

          The ID of the invoice that is associated with the billing record.

        - **BillDate** *(datetime) --*

          The date that the operation was billed, in Unix format.

        - **Price** *(float) --*

          The price that you were charged for the operation, in US dollars.

          Example value: 12.0
    """


_ListDomainsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDomainsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDomainsPaginatePaginationConfigTypeDef(
    _ListDomainsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDomainsPaginate` `PaginationConfig`

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


_ListDomainsPaginateResponseDomainsTypeDef = TypedDict(
    "_ListDomainsPaginateResponseDomainsTypeDef",
    {"DomainName": str, "AutoRenew": bool, "TransferLock": bool, "Expiry": datetime},
    total=False,
)


class ListDomainsPaginateResponseDomainsTypeDef(
    _ListDomainsPaginateResponseDomainsTypeDef
):
    """
    Type definition for `ListDomainsPaginateResponse` `Domains`

    Summary information about one domain.

    - **DomainName** *(string) --*

      The name of the domain that the summary information applies to.

    - **AutoRenew** *(boolean) --*

      Indicates whether the domain is automatically renewed upon expiration.

    - **TransferLock** *(boolean) --*

      Indicates whether a domain is locked from unauthorized transfer to another party.

    - **Expiry** *(datetime) --*

      Expiration date of the domain in Coordinated Universal Time (UTC).
    """


_ListDomainsPaginateResponseTypeDef = TypedDict(
    "_ListDomainsPaginateResponseTypeDef",
    {"Domains": List[ListDomainsPaginateResponseDomainsTypeDef], "NextToken": str},
    total=False,
)


class ListDomainsPaginateResponseTypeDef(_ListDomainsPaginateResponseTypeDef):
    """
    Type definition for `ListDomainsPaginate` `Response`

    The ListDomains response includes the following elements.

    - **Domains** *(list) --*

      A summary of domains.

      - *(dict) --*

        Summary information about one domain.

        - **DomainName** *(string) --*

          The name of the domain that the summary information applies to.

        - **AutoRenew** *(boolean) --*

          Indicates whether the domain is automatically renewed upon expiration.

        - **TransferLock** *(boolean) --*

          Indicates whether a domain is locked from unauthorized transfer to another party.

        - **Expiry** *(datetime) --*

          Expiration date of the domain in Coordinated Universal Time (UTC).

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOperationsPaginatePaginationConfigTypeDef(
    _ListOperationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListOperationsPaginate` `PaginationConfig`

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


_ListOperationsPaginateResponseOperationsTypeDef = TypedDict(
    "_ListOperationsPaginateResponseOperationsTypeDef",
    {"OperationId": str, "Status": str, "Type": str, "SubmittedDate": datetime},
    total=False,
)


class ListOperationsPaginateResponseOperationsTypeDef(
    _ListOperationsPaginateResponseOperationsTypeDef
):
    """
    Type definition for `ListOperationsPaginateResponse` `Operations`

    OperationSummary includes the following elements.

    - **OperationId** *(string) --*

      Identifier returned to track the requested action.

    - **Status** *(string) --*

      The current status of the requested operation in the system.

    - **Type** *(string) --*

      Type of the action requested.

    - **SubmittedDate** *(datetime) --*

      The date when the request was submitted.
    """


_ListOperationsPaginateResponseTypeDef = TypedDict(
    "_ListOperationsPaginateResponseTypeDef",
    {
        "Operations": List[ListOperationsPaginateResponseOperationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListOperationsPaginateResponseTypeDef(_ListOperationsPaginateResponseTypeDef):
    """
    Type definition for `ListOperationsPaginate` `Response`

    The ListOperations response includes the following elements.

    - **Operations** *(list) --*

      Lists summaries of the operations.

      - *(dict) --*

        OperationSummary includes the following elements.

        - **OperationId** *(string) --*

          Identifier returned to track the requested action.

        - **Status** *(string) --*

          The current status of the requested operation in the system.

        - **Type** *(string) --*

          Type of the action requested.

        - **SubmittedDate** *(datetime) --*

          The date when the request was submitted.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ViewBillingPaginatePaginationConfigTypeDef = TypedDict(
    "_ViewBillingPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ViewBillingPaginatePaginationConfigTypeDef(
    _ViewBillingPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ViewBillingPaginate` `PaginationConfig`

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


_ViewBillingPaginateResponseBillingRecordsTypeDef = TypedDict(
    "_ViewBillingPaginateResponseBillingRecordsTypeDef",
    {
        "DomainName": str,
        "Operation": str,
        "InvoiceId": str,
        "BillDate": datetime,
        "Price": float,
    },
    total=False,
)


class ViewBillingPaginateResponseBillingRecordsTypeDef(
    _ViewBillingPaginateResponseBillingRecordsTypeDef
):
    """
    Type definition for `ViewBillingPaginateResponse` `BillingRecords`

    Information for one billing record.

    - **DomainName** *(string) --*

      The name of the domain that the billing record applies to. If the domain name contains
      characters other than a-z, 0-9, and - (hyphen), such as an internationalized domain name,
      then this value is in Punycode. For more information, see `DNS Domain Name Format
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in
      the *Amazon Route 53 Developer Guidezzz* .

    - **Operation** *(string) --*

      The operation that you were charged for.

    - **InvoiceId** *(string) --*

      The ID of the invoice that is associated with the billing record.

    - **BillDate** *(datetime) --*

      The date that the operation was billed, in Unix format.

    - **Price** *(float) --*

      The price that you were charged for the operation, in US dollars.

      Example value: 12.0
    """


_ViewBillingPaginateResponseTypeDef = TypedDict(
    "_ViewBillingPaginateResponseTypeDef",
    {
        "BillingRecords": List[ViewBillingPaginateResponseBillingRecordsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ViewBillingPaginateResponseTypeDef(_ViewBillingPaginateResponseTypeDef):
    """
    Type definition for `ViewBillingPaginate` `Response`

    The ViewBilling response includes the following elements.

    - **BillingRecords** *(list) --*

      A summary of billing records.

      - *(dict) --*

        Information for one billing record.

        - **DomainName** *(string) --*

          The name of the domain that the billing record applies to. If the domain name contains
          characters other than a-z, 0-9, and - (hyphen), such as an internationalized domain name,
          then this value is in Punycode. For more information, see `DNS Domain Name Format
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in
          the *Amazon Route 53 Developer Guidezzz* .

        - **Operation** *(string) --*

          The operation that you were charged for.

        - **InvoiceId** *(string) --*

          The ID of the invoice that is associated with the billing record.

        - **BillDate** *(datetime) --*

          The date that the operation was billed, in Unix format.

        - **Price** *(float) --*

          The price that you were charged for the operation, in US dollars.

          Example value: 12.0

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
