"Main interface for guardduty type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateDetectorResponseTypeDef",
    "ClientCreateFilterFindingCriteriaCriterionTypeDef",
    "ClientCreateFilterFindingCriteriaTypeDef",
    "ClientCreateFilterResponseTypeDef",
    "ClientCreateIpSetResponseTypeDef",
    "ClientCreateMembersAccountDetailsTypeDef",
    "ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    "ClientCreateMembersResponseTypeDef",
    "ClientCreatePublishingDestinationDestinationPropertiesTypeDef",
    "ClientCreatePublishingDestinationResponseTypeDef",
    "ClientCreateThreatIntelSetResponseTypeDef",
    "ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    "ClientDeclineInvitationsResponseTypeDef",
    "ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    "ClientDeleteInvitationsResponseTypeDef",
    "ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    "ClientDeleteMembersResponseTypeDef",
    "ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef",
    "ClientDescribePublishingDestinationResponseTypeDef",
    "ClientDisassociateMembersResponseUnprocessedAccountsTypeDef",
    "ClientDisassociateMembersResponseTypeDef",
    "ClientGetDetectorResponseTypeDef",
    "ClientGetFilterResponseFindingCriteriaCriterionTypeDef",
    "ClientGetFilterResponseFindingCriteriaTypeDef",
    "ClientGetFilterResponseTypeDef",
    "ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef",
    "ClientGetFindingsResponseFindingsResourceTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceEvidenceTypeDef",
    "ClientGetFindingsResponseFindingsServiceTypeDef",
    "ClientGetFindingsResponseFindingsTypeDef",
    "ClientGetFindingsResponseTypeDef",
    "ClientGetFindingsSortCriteriaTypeDef",
    "ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef",
    "ClientGetFindingsStatisticsFindingCriteriaTypeDef",
    "ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef",
    "ClientGetFindingsStatisticsResponseTypeDef",
    "ClientGetInvitationsCountResponseTypeDef",
    "ClientGetIpSetResponseTypeDef",
    "ClientGetMasterAccountResponseMasterTypeDef",
    "ClientGetMasterAccountResponseTypeDef",
    "ClientGetMembersResponseMembersTypeDef",
    "ClientGetMembersResponseUnprocessedAccountsTypeDef",
    "ClientGetMembersResponseTypeDef",
    "ClientGetThreatIntelSetResponseTypeDef",
    "ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    "ClientInviteMembersResponseTypeDef",
    "ClientListDetectorsResponseTypeDef",
    "ClientListFiltersResponseTypeDef",
    "ClientListFindingsFindingCriteriaCriterionTypeDef",
    "ClientListFindingsFindingCriteriaTypeDef",
    "ClientListFindingsResponseTypeDef",
    "ClientListFindingsSortCriteriaTypeDef",
    "ClientListInvitationsResponseInvitationsTypeDef",
    "ClientListInvitationsResponseTypeDef",
    "ClientListIpSetsResponseTypeDef",
    "ClientListMembersResponseMembersTypeDef",
    "ClientListMembersResponseTypeDef",
    "ClientListPublishingDestinationsResponseDestinationsTypeDef",
    "ClientListPublishingDestinationsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListThreatIntelSetsResponseTypeDef",
    "ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef",
    "ClientStartMonitoringMembersResponseTypeDef",
    "ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef",
    "ClientStopMonitoringMembersResponseTypeDef",
    "ClientUpdateFilterFindingCriteriaCriterionTypeDef",
    "ClientUpdateFilterFindingCriteriaTypeDef",
    "ClientUpdateFilterResponseTypeDef",
    "ClientUpdatePublishingDestinationDestinationPropertiesTypeDef",
    "ListDetectorsPaginatePaginationConfigTypeDef",
    "ListDetectorsPaginateResponseTypeDef",
    "ListFiltersPaginatePaginationConfigTypeDef",
    "ListFiltersPaginateResponseTypeDef",
    "ListFindingsPaginateFindingCriteriaCriterionTypeDef",
    "ListFindingsPaginateFindingCriteriaTypeDef",
    "ListFindingsPaginatePaginationConfigTypeDef",
    "ListFindingsPaginateResponseTypeDef",
    "ListFindingsPaginateSortCriteriaTypeDef",
    "ListIPSetsPaginatePaginationConfigTypeDef",
    "ListIPSetsPaginateResponseTypeDef",
    "ListInvitationsPaginatePaginationConfigTypeDef",
    "ListInvitationsPaginateResponseInvitationsTypeDef",
    "ListInvitationsPaginateResponseTypeDef",
    "ListMembersPaginatePaginationConfigTypeDef",
    "ListMembersPaginateResponseMembersTypeDef",
    "ListMembersPaginateResponseTypeDef",
    "ListThreatIntelSetsPaginatePaginationConfigTypeDef",
    "ListThreatIntelSetsPaginateResponseTypeDef",
)


_ClientCreateDetectorResponseTypeDef = TypedDict(
    "_ClientCreateDetectorResponseTypeDef", {"DetectorId": str}, total=False
)


class ClientCreateDetectorResponseTypeDef(_ClientCreateDetectorResponseTypeDef):
    """
    Type definition for `ClientCreateDetector` `Response`

    - **DetectorId** *(string) --*

      The unique ID of the created detector.
    """


_ClientCreateFilterFindingCriteriaCriterionTypeDef = TypedDict(
    "_ClientCreateFilterFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ClientCreateFilterFindingCriteriaCriterionTypeDef(
    _ClientCreateFilterFindingCriteriaCriterionTypeDef
):
    """
    Type definition for `ClientCreateFilterFindingCriteria` `Criterion`

    Contains information about the condition.

    - **Eq** *(list) --*

      Represents the equal condition to be applied to a single field when querying for findings.

      - *(string) --*

    - **Neq** *(list) --*

      Represents the not equal condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **Gt** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **Gte** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when querying
      for findings.

    - **Lt** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **Lte** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying for
      findings.

    - **Equals** *(list) --*

      Represents an **equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **NotEquals** *(list) --*

      Represents an **not equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **GreaterThan** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **GreaterThanOrEqual** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when querying
      for findings.

    - **LessThan** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **LessThanOrEqual** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying for
      findings.
    """


_ClientCreateFilterFindingCriteriaTypeDef = TypedDict(
    "_ClientCreateFilterFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientCreateFilterFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ClientCreateFilterFindingCriteriaTypeDef(
    _ClientCreateFilterFindingCriteriaTypeDef
):
    """
    Type definition for `ClientCreateFilter` `FindingCriteria`

    Represents the criteria to be used in the filter for querying findings.

    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when querying
      findings.

      - *(string) --*

        - *(dict) --*

          Contains information about the condition.

          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for findings.

            - *(string) --*

          - **Neq** *(list) --*

            Represents the not equal condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **Gt** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **Gte** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when querying
            for findings.

          - **Lt** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **Lte** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying for
            findings.

          - **Equals** *(list) --*

            Represents an **equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **NotEquals** *(list) --*

            Represents an **not equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **GreaterThan** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **GreaterThanOrEqual** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when querying
            for findings.

          - **LessThan** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **LessThanOrEqual** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying for
            findings.
    """


_ClientCreateFilterResponseTypeDef = TypedDict(
    "_ClientCreateFilterResponseTypeDef", {"Name": str}, total=False
)


class ClientCreateFilterResponseTypeDef(_ClientCreateFilterResponseTypeDef):
    """
    Type definition for `ClientCreateFilter` `Response`

    - **Name** *(string) --*

      The name of the successfully created filter.
    """


_ClientCreateIpSetResponseTypeDef = TypedDict(
    "_ClientCreateIpSetResponseTypeDef", {"IpSetId": str}, total=False
)


class ClientCreateIpSetResponseTypeDef(_ClientCreateIpSetResponseTypeDef):
    """
    Type definition for `ClientCreateIpSet` `Response`

    - **IpSetId** *(string) --*

      The ID of the IPSet resource.
    """


_ClientCreateMembersAccountDetailsTypeDef = TypedDict(
    "_ClientCreateMembersAccountDetailsTypeDef", {"AccountId": str, "Email": str}
)


class ClientCreateMembersAccountDetailsTypeDef(
    _ClientCreateMembersAccountDetailsTypeDef
):
    """
    Type definition for `ClientCreateMembers` `AccountDetails`

    Contains information about the account.

    - **AccountId** *(string) --* **[REQUIRED]**

      Member account ID.

    - **Email** *(string) --* **[REQUIRED]**

      Member account's email address.
    """


_ClientCreateMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientCreateMembersResponseUnprocessedAccountsTypeDef(
    _ClientCreateMembersResponseUnprocessedAccountsTypeDef
):
    """
    Type definition for `ClientCreateMembersResponse` `UnprocessedAccounts`

    Contains information about the accounts that were not processed.

    - **AccountId** *(string) --*

      AWS Account ID.

    - **Result** *(string) --*

      A reason why the account hasn't been processed.
    """


_ClientCreateMembersResponseTypeDef = TypedDict(
    "_ClientCreateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[
            ClientCreateMembersResponseUnprocessedAccountsTypeDef
        ]
    },
    total=False,
)


class ClientCreateMembersResponseTypeDef(_ClientCreateMembersResponseTypeDef):
    """
    Type definition for `ClientCreateMembers` `Response`

    - **UnprocessedAccounts** *(list) --*

      A list of objects containing the unprocessed account and a result string explaining why it
      was unprocessed.

      - *(dict) --*

        Contains information about the accounts that were not processed.

        - **AccountId** *(string) --*

          AWS Account ID.

        - **Result** *(string) --*

          A reason why the account hasn't been processed.
    """


_ClientCreatePublishingDestinationDestinationPropertiesTypeDef = TypedDict(
    "_ClientCreatePublishingDestinationDestinationPropertiesTypeDef",
    {"DestinationArn": str, "KmsKeyArn": str},
    total=False,
)


class ClientCreatePublishingDestinationDestinationPropertiesTypeDef(
    _ClientCreatePublishingDestinationDestinationPropertiesTypeDef
):
    """
    Type definition for `ClientCreatePublishingDestination` `DestinationProperties`

    Properties of the publishing destination, including the ARNs for the destination and the KMS key
    used for encryption.

    - **DestinationArn** *(string) --*

      The ARN of the resource to publish to.

    - **KmsKeyArn** *(string) --*

      The ARN of the KMS key to use for encryption.
    """


_ClientCreatePublishingDestinationResponseTypeDef = TypedDict(
    "_ClientCreatePublishingDestinationResponseTypeDef",
    {"DestinationId": str},
    total=False,
)


class ClientCreatePublishingDestinationResponseTypeDef(
    _ClientCreatePublishingDestinationResponseTypeDef
):
    """
    Type definition for `ClientCreatePublishingDestination` `Response`

    - **DestinationId** *(string) --*

      The ID of the publishing destination created.
    """


_ClientCreateThreatIntelSetResponseTypeDef = TypedDict(
    "_ClientCreateThreatIntelSetResponseTypeDef", {"ThreatIntelSetId": str}, total=False
)


class ClientCreateThreatIntelSetResponseTypeDef(
    _ClientCreateThreatIntelSetResponseTypeDef
):
    """
    Type definition for `ClientCreateThreatIntelSet` `Response`

    - **ThreatIntelSetId** *(string) --*

      The ID of the ThreatIntelSet resource.
    """


_ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef(
    _ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef
):
    """
    Type definition for `ClientDeclineInvitationsResponse` `UnprocessedAccounts`

    Contains information about the accounts that were not processed.

    - **AccountId** *(string) --*

      AWS Account ID.

    - **Result** *(string) --*

      A reason why the account hasn't been processed.
    """


_ClientDeclineInvitationsResponseTypeDef = TypedDict(
    "_ClientDeclineInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List[
            ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef
        ]
    },
    total=False,
)


class ClientDeclineInvitationsResponseTypeDef(_ClientDeclineInvitationsResponseTypeDef):
    """
    Type definition for `ClientDeclineInvitations` `Response`

    - **UnprocessedAccounts** *(list) --*

      A list of objects containing the unprocessed account and a result string explaining why it
      was unprocessed.

      - *(dict) --*

        Contains information about the accounts that were not processed.

        - **AccountId** *(string) --*

          AWS Account ID.

        - **Result** *(string) --*

          A reason why the account hasn't been processed.
    """


_ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef(
    _ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef
):
    """
    Type definition for `ClientDeleteInvitationsResponse` `UnprocessedAccounts`

    Contains information about the accounts that were not processed.

    - **AccountId** *(string) --*

      AWS Account ID.

    - **Result** *(string) --*

      A reason why the account hasn't been processed.
    """


_ClientDeleteInvitationsResponseTypeDef = TypedDict(
    "_ClientDeleteInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List[
            ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteInvitationsResponseTypeDef(_ClientDeleteInvitationsResponseTypeDef):
    """
    Type definition for `ClientDeleteInvitations` `Response`

    - **UnprocessedAccounts** *(list) --*

      A list of objects containing the unprocessed account and a result string explaining why it
      was unprocessed.

      - *(dict) --*

        Contains information about the accounts that were not processed.

        - **AccountId** *(string) --*

          AWS Account ID.

        - **Result** *(string) --*

          A reason why the account hasn't been processed.
    """


_ClientDeleteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientDeleteMembersResponseUnprocessedAccountsTypeDef(
    _ClientDeleteMembersResponseUnprocessedAccountsTypeDef
):
    """
    Type definition for `ClientDeleteMembersResponse` `UnprocessedAccounts`

    Contains information about the accounts that were not processed.

    - **AccountId** *(string) --*

      AWS Account ID.

    - **Result** *(string) --*

      A reason why the account hasn't been processed.
    """


_ClientDeleteMembersResponseTypeDef = TypedDict(
    "_ClientDeleteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[
            ClientDeleteMembersResponseUnprocessedAccountsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteMembersResponseTypeDef(_ClientDeleteMembersResponseTypeDef):
    """
    Type definition for `ClientDeleteMembers` `Response`

    - **UnprocessedAccounts** *(list) --*

      The accounts that could not be processed.

      - *(dict) --*

        Contains information about the accounts that were not processed.

        - **AccountId** *(string) --*

          AWS Account ID.

        - **Result** *(string) --*

          A reason why the account hasn't been processed.
    """


_ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef = TypedDict(
    "_ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef",
    {"DestinationArn": str, "KmsKeyArn": str},
    total=False,
)


class ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef(
    _ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef
):
    """
    Type definition for `ClientDescribePublishingDestinationResponse` `DestinationProperties`

    A ``DestinationProperties`` object that includes the ``DestinationArn`` and ``KmsKeyArn`` of
    the publishing destination.

    - **DestinationArn** *(string) --*

      The ARN of the resource to publish to.

    - **KmsKeyArn** *(string) --*

      The ARN of the KMS key to use for encryption.
    """


_ClientDescribePublishingDestinationResponseTypeDef = TypedDict(
    "_ClientDescribePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
        "DestinationType": str,
        "Status": str,
        "PublishingFailureStartTimestamp": int,
        "DestinationProperties": ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef,
    },
    total=False,
)


class ClientDescribePublishingDestinationResponseTypeDef(
    _ClientDescribePublishingDestinationResponseTypeDef
):
    """
    Type definition for `ClientDescribePublishingDestination` `Response`

    - **DestinationId** *(string) --*

      The ID of the publishing destination.

    - **DestinationType** *(string) --*

      The type of the publishing destination. Currently, only S3 is supported.

    - **Status** *(string) --*

      The status of the publishing destination.

    - **PublishingFailureStartTimestamp** *(integer) --*

      The time, in epoch millisecond format, at which GuardDuty was first unable to publish
      findings to the destination.

    - **DestinationProperties** *(dict) --*

      A ``DestinationProperties`` object that includes the ``DestinationArn`` and ``KmsKeyArn`` of
      the publishing destination.

      - **DestinationArn** *(string) --*

        The ARN of the resource to publish to.

      - **KmsKeyArn** *(string) --*

        The ARN of the KMS key to use for encryption.
    """


_ClientDisassociateMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDisassociateMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientDisassociateMembersResponseUnprocessedAccountsTypeDef(
    _ClientDisassociateMembersResponseUnprocessedAccountsTypeDef
):
    """
    Type definition for `ClientDisassociateMembersResponse` `UnprocessedAccounts`

    Contains information about the accounts that were not processed.

    - **AccountId** *(string) --*

      AWS Account ID.

    - **Result** *(string) --*

      A reason why the account hasn't been processed.
    """


_ClientDisassociateMembersResponseTypeDef = TypedDict(
    "_ClientDisassociateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[
            ClientDisassociateMembersResponseUnprocessedAccountsTypeDef
        ]
    },
    total=False,
)


class ClientDisassociateMembersResponseTypeDef(
    _ClientDisassociateMembersResponseTypeDef
):
    """
    Type definition for `ClientDisassociateMembers` `Response`

    - **UnprocessedAccounts** *(list) --*

      A list of objects containing the unprocessed account and a result string explaining why it
      was unprocessed.

      - *(dict) --*

        Contains information about the accounts that were not processed.

        - **AccountId** *(string) --*

          AWS Account ID.

        - **Result** *(string) --*

          A reason why the account hasn't been processed.
    """


_ClientGetDetectorResponseTypeDef = TypedDict(
    "_ClientGetDetectorResponseTypeDef",
    {
        "CreatedAt": str,
        "FindingPublishingFrequency": str,
        "ServiceRole": str,
        "Status": str,
        "UpdatedAt": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDetectorResponseTypeDef(_ClientGetDetectorResponseTypeDef):
    """
    Type definition for `ClientGetDetector` `Response`

    - **CreatedAt** *(string) --*

      Detector creation timestamp.

    - **FindingPublishingFrequency** *(string) --*

      Finding publishing frequency.

    - **ServiceRole** *(string) --*

      The GuardDuty service role.

    - **Status** *(string) --*

      The detector status.

    - **UpdatedAt** *(string) --*

      Detector last update timestamp.

    - **Tags** *(dict) --*

      The tags of the detector resource.

      - *(string) --*

        - *(string) --*
    """


_ClientGetFilterResponseFindingCriteriaCriterionTypeDef = TypedDict(
    "_ClientGetFilterResponseFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ClientGetFilterResponseFindingCriteriaCriterionTypeDef(
    _ClientGetFilterResponseFindingCriteriaCriterionTypeDef
):
    """
    Type definition for `ClientGetFilterResponseFindingCriteria` `Criterion`

    Contains information about the condition.

    - **Eq** *(list) --*

      Represents the equal condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **Neq** *(list) --*

      Represents the not equal condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **Gt** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **Gte** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when
      querying for findings.

    - **Lt** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **Lte** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying
      for findings.

    - **Equals** *(list) --*

      Represents an **equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **NotEquals** *(list) --*

      Represents an **not equal** condition to be applied to a single field when querying
      for findings.

      - *(string) --*

    - **GreaterThan** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **GreaterThanOrEqual** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when
      querying for findings.

    - **LessThan** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **LessThanOrEqual** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying
      for findings.
    """


_ClientGetFilterResponseFindingCriteriaTypeDef = TypedDict(
    "_ClientGetFilterResponseFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientGetFilterResponseFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ClientGetFilterResponseFindingCriteriaTypeDef(
    _ClientGetFilterResponseFindingCriteriaTypeDef
):
    """
    Type definition for `ClientGetFilterResponse` `FindingCriteria`

    Represents the criteria to be used in the filter for querying findings.

    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when
      querying findings.

      - *(string) --*

        - *(dict) --*

          Contains information about the condition.

          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **Neq** *(list) --*

            Represents the not equal condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **Gt** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **Gte** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when
            querying for findings.

          - **Lt** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **Lte** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying
            for findings.

          - **Equals** *(list) --*

            Represents an **equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **NotEquals** *(list) --*

            Represents an **not equal** condition to be applied to a single field when querying
            for findings.

            - *(string) --*

          - **GreaterThan** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **GreaterThanOrEqual** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when
            querying for findings.

          - **LessThan** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **LessThanOrEqual** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying
            for findings.
    """


_ClientGetFilterResponseTypeDef = TypedDict(
    "_ClientGetFilterResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": str,
        "Rank": int,
        "FindingCriteria": ClientGetFilterResponseFindingCriteriaTypeDef,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetFilterResponseTypeDef(_ClientGetFilterResponseTypeDef):
    """
    Type definition for `ClientGetFilter` `Response`

    - **Name** *(string) --*

      The name of the filter.

    - **Description** *(string) --*

      The description of the filter.

    - **Action** *(string) --*

      Specifies the action that is to be applied to the findings that match the filter.

    - **Rank** *(integer) --*

      Specifies the position of the filter in the list of current filters. Also specifies the order
      in which this filter is applied to the findings.

    - **FindingCriteria** *(dict) --*

      Represents the criteria to be used in the filter for querying findings.

      - **Criterion** *(dict) --*

        Represents a map of finding properties that match specified conditions and values when
        querying findings.

        - *(string) --*

          - *(dict) --*

            Contains information about the condition.

            - **Eq** *(list) --*

              Represents the equal condition to be applied to a single field when querying for
              findings.

              - *(string) --*

            - **Neq** *(list) --*

              Represents the not equal condition to be applied to a single field when querying for
              findings.

              - *(string) --*

            - **Gt** *(integer) --*

              Represents a greater than condition to be applied to a single field when querying for
              findings.

            - **Gte** *(integer) --*

              Represents a greater than equal condition to be applied to a single field when
              querying for findings.

            - **Lt** *(integer) --*

              Represents a less than condition to be applied to a single field when querying for
              findings.

            - **Lte** *(integer) --*

              Represents a less than equal condition to be applied to a single field when querying
              for findings.

            - **Equals** *(list) --*

              Represents an **equal** condition to be applied to a single field when querying for
              findings.

              - *(string) --*

            - **NotEquals** *(list) --*

              Represents an **not equal** condition to be applied to a single field when querying
              for findings.

              - *(string) --*

            - **GreaterThan** *(integer) --*

              Represents a greater than condition to be applied to a single field when querying for
              findings.

            - **GreaterThanOrEqual** *(integer) --*

              Represents a greater than equal condition to be applied to a single field when
              querying for findings.

            - **LessThan** *(integer) --*

              Represents a less than condition to be applied to a single field when querying for
              findings.

            - **LessThanOrEqual** *(integer) --*

              Represents a less than equal condition to be applied to a single field when querying
              for findings.

    - **Tags** *(dict) --*

      The tags of the filter resource.

      - *(string) --*

        - *(string) --*
    """


_ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef",
    {"AccessKeyId": str, "PrincipalId": str, "UserName": str, "UserType": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef(
    _ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsResource` `AccessKeyDetails`

    The IAM access key details (IAM user information) of a user that engaged in the
    activity that prompted GuardDuty to generate a finding.

    - **AccessKeyId** *(string) --*

      Access key ID of the user.

    - **PrincipalId** *(string) --*

      The principal ID of the user.

    - **UserName** *(string) --*

      The name of the user.

    - **UserType** *(string) --*

      The type of the user.
    """


_ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef",
    {"Arn": str, "Id": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsResourceInstanceDetails` `IamInstanceProfile`

    The profile information of the EC2 instance.

    - **Arn** *(string) --*

      AWS EC2 instance profile ARN.

    - **Id** *(string) --*

      AWS EC2 instance profile ID.
    """


_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef",
    {"PrivateDnsName": str, "PrivateIpAddress": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfaces` `PrivateIpAddresses`

    Contains other private IP address information of the EC2 instance.

    - **PrivateDnsName** *(string) --*

      Private DNS name of the EC2 instance.

    - **PrivateIpAddress** *(string) --*

      Private IP address of the EC2 instance.
    """


_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef",
    {"GroupId": str, "GroupName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfaces` `SecurityGroups`

    Contains information about the security groups associated with the EC2 instance.

    - **GroupId** *(string) --*

      EC2 instance's security group ID.

    - **GroupName** *(string) --*

      EC2 instance's security group name.
    """


_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef",
    {
        "Ipv6Addresses": List[str],
        "NetworkInterfaceId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef
        ],
        "PublicDnsName": str,
        "PublicIp": str,
        "SecurityGroups": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef
        ],
        "SubnetId": str,
        "VpcId": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsResourceInstanceDetails` `NetworkInterfaces`

    Contains information about the network interface of the Ec2 instance.

    - **Ipv6Addresses** *(list) --*

      A list of EC2 instance IPv6 address information.

      - *(string) --*

    - **NetworkInterfaceId** *(string) --*

      The ID of the network interface

    - **PrivateDnsName** *(string) --*

      Private DNS name of the EC2 instance.

    - **PrivateIpAddress** *(string) --*

      Private IP address of the EC2 instance.

    - **PrivateIpAddresses** *(list) --*

      Other private IP address information of the EC2 instance.

      - *(dict) --*

        Contains other private IP address information of the EC2 instance.

        - **PrivateDnsName** *(string) --*

          Private DNS name of the EC2 instance.

        - **PrivateIpAddress** *(string) --*

          Private IP address of the EC2 instance.

    - **PublicDnsName** *(string) --*

      Public DNS name of the EC2 instance.

    - **PublicIp** *(string) --*

      Public IP address of the EC2 instance.

    - **SecurityGroups** *(list) --*

      Security groups associated with the EC2 instance.

      - *(dict) --*

        Contains information about the security groups associated with the EC2 instance.

        - **GroupId** *(string) --*

          EC2 instance's security group ID.

        - **GroupName** *(string) --*

          EC2 instance's security group name.

    - **SubnetId** *(string) --*

      The subnet ID of the EC2 instance.

    - **VpcId** *(string) --*

      The VPC ID of the EC2 instance.
    """


_ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef",
    {"Code": str, "ProductType": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsResourceInstanceDetails` `ProductCodes`

    Contains information about the product code for the Ec2 instance.

    - **Code** *(string) --*

      Product code information.

    - **ProductType** *(string) --*

      Product code type.
    """


_ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsResourceInstanceDetails` `Tags`

    Contains information about a tag associated with the Ec2 instance.

    - **Key** *(string) --*

      EC2 instance tag key.

    - **Value** *(string) --*

      EC2 instance tag value.
    """


_ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef",
    {
        "AvailabilityZone": str,
        "IamInstanceProfile": ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef,
        "ImageDescription": str,
        "ImageId": str,
        "InstanceId": str,
        "InstanceState": str,
        "InstanceType": str,
        "LaunchTime": str,
        "NetworkInterfaces": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef
        ],
        "Platform": str,
        "ProductCodes": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef
        ],
        "Tags": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef
        ],
    },
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsResource` `InstanceDetails`

    The information about the EC2 instance associated with the activity that prompted
    GuardDuty to generate a finding.

    - **AvailabilityZone** *(string) --*

      The availability zone of the EC2 instance.

    - **IamInstanceProfile** *(dict) --*

      The profile information of the EC2 instance.

      - **Arn** *(string) --*

        AWS EC2 instance profile ARN.

      - **Id** *(string) --*

        AWS EC2 instance profile ID.

    - **ImageDescription** *(string) --*

      The image description of the EC2 instance.

    - **ImageId** *(string) --*

      The image ID of the EC2 instance.

    - **InstanceId** *(string) --*

      The ID of the EC2 instance.

    - **InstanceState** *(string) --*

      The state of the EC2 instance.

    - **InstanceType** *(string) --*

      The type of the EC2 instance.

    - **LaunchTime** *(string) --*

      The launch time of the EC2 instance.

    - **NetworkInterfaces** *(list) --*

      The network interface information of the EC2 instance.

      - *(dict) --*

        Contains information about the network interface of the Ec2 instance.

        - **Ipv6Addresses** *(list) --*

          A list of EC2 instance IPv6 address information.

          - *(string) --*

        - **NetworkInterfaceId** *(string) --*

          The ID of the network interface

        - **PrivateDnsName** *(string) --*

          Private DNS name of the EC2 instance.

        - **PrivateIpAddress** *(string) --*

          Private IP address of the EC2 instance.

        - **PrivateIpAddresses** *(list) --*

          Other private IP address information of the EC2 instance.

          - *(dict) --*

            Contains other private IP address information of the EC2 instance.

            - **PrivateDnsName** *(string) --*

              Private DNS name of the EC2 instance.

            - **PrivateIpAddress** *(string) --*

              Private IP address of the EC2 instance.

        - **PublicDnsName** *(string) --*

          Public DNS name of the EC2 instance.

        - **PublicIp** *(string) --*

          Public IP address of the EC2 instance.

        - **SecurityGroups** *(list) --*

          Security groups associated with the EC2 instance.

          - *(dict) --*

            Contains information about the security groups associated with the EC2 instance.

            - **GroupId** *(string) --*

              EC2 instance's security group ID.

            - **GroupName** *(string) --*

              EC2 instance's security group name.

        - **SubnetId** *(string) --*

          The subnet ID of the EC2 instance.

        - **VpcId** *(string) --*

          The VPC ID of the EC2 instance.

    - **Platform** *(string) --*

      The platform of the EC2 instance.

    - **ProductCodes** *(list) --*

      The product code of the EC2 instance.

      - *(dict) --*

        Contains information about the product code for the Ec2 instance.

        - **Code** *(string) --*

          Product code information.

        - **ProductType** *(string) --*

          Product code type.

    - **Tags** *(list) --*

      The tags of the EC2 instance.

      - *(dict) --*

        Contains information about a tag associated with the Ec2 instance.

        - **Key** *(string) --*

          EC2 instance tag key.

        - **Value** *(string) --*

          EC2 instance tag value.
    """


_ClientGetFindingsResponseFindingsResourceTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceTypeDef",
    {
        "AccessKeyDetails": ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef,
        "InstanceDetails": ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef,
        "ResourceType": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsResourceTypeDef(
    _ClientGetFindingsResponseFindingsResourceTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindings` `Resource`

    Contains information about the AWS resource associated with the activity that prompted
    GuardDuty to generate a finding.

    - **AccessKeyDetails** *(dict) --*

      The IAM access key details (IAM user information) of a user that engaged in the
      activity that prompted GuardDuty to generate a finding.

      - **AccessKeyId** *(string) --*

        Access key ID of the user.

      - **PrincipalId** *(string) --*

        The principal ID of the user.

      - **UserName** *(string) --*

        The name of the user.

      - **UserType** *(string) --*

        The type of the user.

    - **InstanceDetails** *(dict) --*

      The information about the EC2 instance associated with the activity that prompted
      GuardDuty to generate a finding.

      - **AvailabilityZone** *(string) --*

        The availability zone of the EC2 instance.

      - **IamInstanceProfile** *(dict) --*

        The profile information of the EC2 instance.

        - **Arn** *(string) --*

          AWS EC2 instance profile ARN.

        - **Id** *(string) --*

          AWS EC2 instance profile ID.

      - **ImageDescription** *(string) --*

        The image description of the EC2 instance.

      - **ImageId** *(string) --*

        The image ID of the EC2 instance.

      - **InstanceId** *(string) --*

        The ID of the EC2 instance.

      - **InstanceState** *(string) --*

        The state of the EC2 instance.

      - **InstanceType** *(string) --*

        The type of the EC2 instance.

      - **LaunchTime** *(string) --*

        The launch time of the EC2 instance.

      - **NetworkInterfaces** *(list) --*

        The network interface information of the EC2 instance.

        - *(dict) --*

          Contains information about the network interface of the Ec2 instance.

          - **Ipv6Addresses** *(list) --*

            A list of EC2 instance IPv6 address information.

            - *(string) --*

          - **NetworkInterfaceId** *(string) --*

            The ID of the network interface

          - **PrivateDnsName** *(string) --*

            Private DNS name of the EC2 instance.

          - **PrivateIpAddress** *(string) --*

            Private IP address of the EC2 instance.

          - **PrivateIpAddresses** *(list) --*

            Other private IP address information of the EC2 instance.

            - *(dict) --*

              Contains other private IP address information of the EC2 instance.

              - **PrivateDnsName** *(string) --*

                Private DNS name of the EC2 instance.

              - **PrivateIpAddress** *(string) --*

                Private IP address of the EC2 instance.

          - **PublicDnsName** *(string) --*

            Public DNS name of the EC2 instance.

          - **PublicIp** *(string) --*

            Public IP address of the EC2 instance.

          - **SecurityGroups** *(list) --*

            Security groups associated with the EC2 instance.

            - *(dict) --*

              Contains information about the security groups associated with the EC2 instance.

              - **GroupId** *(string) --*

                EC2 instance's security group ID.

              - **GroupName** *(string) --*

                EC2 instance's security group name.

          - **SubnetId** *(string) --*

            The subnet ID of the EC2 instance.

          - **VpcId** *(string) --*

            The VPC ID of the EC2 instance.

      - **Platform** *(string) --*

        The platform of the EC2 instance.

      - **ProductCodes** *(list) --*

        The product code of the EC2 instance.

        - *(dict) --*

          Contains information about the product code for the Ec2 instance.

          - **Code** *(string) --*

            Product code information.

          - **ProductType** *(string) --*

            Product code type.

      - **Tags** *(list) --*

        The tags of the EC2 instance.

        - *(dict) --*

          Contains information about a tag associated with the Ec2 instance.

          - **Key** *(string) --*

            EC2 instance tag key.

          - **Value** *(string) --*

            EC2 instance tag value.

    - **ResourceType** *(string) --*

      The type of the AWS resource.
    """


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef",
    {"Domain": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionAwsApiCallAction` `DomainDetails`

    Domain information for the AWS API call.

    - **Domain** *(string) --*

      Domain information for the AWS API call.
    """


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef",
    {"CityName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetails` `City`

    City information of the remote IP address.

    - **CityName** *(string) --*

      City name of the remote IP address.
    """


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef",
    {"CountryCode": str, "CountryName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetails` `Country`

    Country code of the remote IP address.

    - **CountryCode** *(string) --*

      Country code of the remote IP address.

    - **CountryName** *(string) --*

      Country name of the remote IP address.
    """


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef",
    {"Lat": float, "Lon": float},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetails` `GeoLocation`

    Location information of the remote IP address.

    - **Lat** *(float) --*

      Latitude information of remote IP address.

    - **Lon** *(float) --*

      Longitude information of remote IP address.
    """


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef",
    {"Asn": str, "AsnOrg": str, "Isp": str, "Org": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetails` `Organization`

    ISP Organization information of the remote IP address.

    - **Asn** *(string) --*

      Autonomous system number of the internet provider of the remote IP address.

    - **AsnOrg** *(string) --*

      Organization that registered this ASN.

    - **Isp** *(string) --*

      ISP information for the internet provider.

    - **Org** *(string) --*

      Name of the internet provider.
    """


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef",
    {
        "City": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef,
        "Country": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef,
        "GeoLocation": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef,
        "IpAddressV4": str,
        "Organization": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionAwsApiCallAction` `RemoteIpDetails`

    Remote IP information of the connection.

    - **City** *(dict) --*

      City information of the remote IP address.

      - **CityName** *(string) --*

        City name of the remote IP address.

    - **Country** *(dict) --*

      Country code of the remote IP address.

      - **CountryCode** *(string) --*

        Country code of the remote IP address.

      - **CountryName** *(string) --*

        Country name of the remote IP address.

    - **GeoLocation** *(dict) --*

      Location information of the remote IP address.

      - **Lat** *(float) --*

        Latitude information of remote IP address.

      - **Lon** *(float) --*

        Longitude information of remote IP address.

    - **IpAddressV4** *(string) --*

      IPV4 remote address of the connection.

    - **Organization** *(dict) --*

      ISP Organization information of the remote IP address.

      - **Asn** *(string) --*

        Autonomous system number of the internet provider of the remote IP address.

      - **AsnOrg** *(string) --*

        Organization that registered this ASN.

      - **Isp** *(string) --*

        ISP information for the internet provider.

      - **Org** *(string) --*

        Name of the internet provider.
    """


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef",
    {
        "Api": str,
        "CallerType": str,
        "DomainDetails": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef,
        "RemoteIpDetails": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef,
        "ServiceName": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceAction` `AwsApiCallAction`

    Information about the AWS_API_CALL action described in this finding.

    - **Api** *(string) --*

      AWS API name.

    - **CallerType** *(string) --*

      AWS API caller type.

    - **DomainDetails** *(dict) --*

      Domain information for the AWS API call.

      - **Domain** *(string) --*

        Domain information for the AWS API call.

    - **RemoteIpDetails** *(dict) --*

      Remote IP information of the connection.

      - **City** *(dict) --*

        City information of the remote IP address.

        - **CityName** *(string) --*

          City name of the remote IP address.

      - **Country** *(dict) --*

        Country code of the remote IP address.

        - **CountryCode** *(string) --*

          Country code of the remote IP address.

        - **CountryName** *(string) --*

          Country name of the remote IP address.

      - **GeoLocation** *(dict) --*

        Location information of the remote IP address.

        - **Lat** *(float) --*

          Latitude information of remote IP address.

        - **Lon** *(float) --*

          Longitude information of remote IP address.

      - **IpAddressV4** *(string) --*

        IPV4 remote address of the connection.

      - **Organization** *(dict) --*

        ISP Organization information of the remote IP address.

        - **Asn** *(string) --*

          Autonomous system number of the internet provider of the remote IP address.

        - **AsnOrg** *(string) --*

          Organization that registered this ASN.

        - **Isp** *(string) --*

          ISP information for the internet provider.

        - **Org** *(string) --*

          Name of the internet provider.

    - **ServiceName** *(string) --*

      AWS service name whose API was invoked.
    """


_ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef",
    {"Domain": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceAction` `DnsRequestAction`

    Information about the DNS_REQUEST action described in this finding.

    - **Domain** *(string) --*

      Domain information for the API request.
    """


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef",
    {"Port": int, "PortName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionNetworkConnectionAction` `LocalPortDetails`

    Local port information of the connection.

    - **Port** *(integer) --*

      Port number of the local connection.

    - **PortName** *(string) --*

      Port name of the local connection.
    """


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef",
    {"CityName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetails` `City`

    City information of the remote IP address.

    - **CityName** *(string) --*

      City name of the remote IP address.
    """


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef",
    {"CountryCode": str, "CountryName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetails` `Country`

    Country code of the remote IP address.

    - **CountryCode** *(string) --*

      Country code of the remote IP address.

    - **CountryName** *(string) --*

      Country name of the remote IP address.
    """


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef",
    {"Lat": float, "Lon": float},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetails` `GeoLocation`

    Location information of the remote IP address.

    - **Lat** *(float) --*

      Latitude information of remote IP address.

    - **Lon** *(float) --*

      Longitude information of remote IP address.
    """


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef",
    {"Asn": str, "AsnOrg": str, "Isp": str, "Org": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetails` `Organization`

    ISP Organization information of the remote IP address.

    - **Asn** *(string) --*

      Autonomous system number of the internet provider of the remote IP address.

    - **AsnOrg** *(string) --*

      Organization that registered this ASN.

    - **Isp** *(string) --*

      ISP information for the internet provider.

    - **Org** *(string) --*

      Name of the internet provider.
    """


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef",
    {
        "City": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef,
        "Country": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef,
        "GeoLocation": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef,
        "IpAddressV4": str,
        "Organization": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionNetworkConnectionAction` `RemoteIpDetails`

    Remote IP information of the connection.

    - **City** *(dict) --*

      City information of the remote IP address.

      - **CityName** *(string) --*

        City name of the remote IP address.

    - **Country** *(dict) --*

      Country code of the remote IP address.

      - **CountryCode** *(string) --*

        Country code of the remote IP address.

      - **CountryName** *(string) --*

        Country name of the remote IP address.

    - **GeoLocation** *(dict) --*

      Location information of the remote IP address.

      - **Lat** *(float) --*

        Latitude information of remote IP address.

      - **Lon** *(float) --*

        Longitude information of remote IP address.

    - **IpAddressV4** *(string) --*

      IPV4 remote address of the connection.

    - **Organization** *(dict) --*

      ISP Organization information of the remote IP address.

      - **Asn** *(string) --*

        Autonomous system number of the internet provider of the remote IP address.

      - **AsnOrg** *(string) --*

        Organization that registered this ASN.

      - **Isp** *(string) --*

        ISP information for the internet provider.

      - **Org** *(string) --*

        Name of the internet provider.
    """


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef",
    {"Port": int, "PortName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionNetworkConnectionAction` `RemotePortDetails`

    Remote port information of the connection.

    - **Port** *(integer) --*

      Port number of the remote connection.

    - **PortName** *(string) --*

      Port name of the remote connection.
    """


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef",
    {
        "Blocked": bool,
        "ConnectionDirection": str,
        "LocalPortDetails": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef,
        "Protocol": str,
        "RemoteIpDetails": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef,
        "RemotePortDetails": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceAction` `NetworkConnectionAction`

    Information about the NETWORK_CONNECTION action described in this finding.

    - **Blocked** *(boolean) --*

      Network connection blocked information.

    - **ConnectionDirection** *(string) --*

      Network connection direction.

    - **LocalPortDetails** *(dict) --*

      Local port information of the connection.

      - **Port** *(integer) --*

        Port number of the local connection.

      - **PortName** *(string) --*

        Port name of the local connection.

    - **Protocol** *(string) --*

      Network connection protocol.

    - **RemoteIpDetails** *(dict) --*

      Remote IP information of the connection.

      - **City** *(dict) --*

        City information of the remote IP address.

        - **CityName** *(string) --*

          City name of the remote IP address.

      - **Country** *(dict) --*

        Country code of the remote IP address.

        - **CountryCode** *(string) --*

          Country code of the remote IP address.

        - **CountryName** *(string) --*

          Country name of the remote IP address.

      - **GeoLocation** *(dict) --*

        Location information of the remote IP address.

        - **Lat** *(float) --*

          Latitude information of remote IP address.

        - **Lon** *(float) --*

          Longitude information of remote IP address.

      - **IpAddressV4** *(string) --*

        IPV4 remote address of the connection.

      - **Organization** *(dict) --*

        ISP Organization information of the remote IP address.

        - **Asn** *(string) --*

          Autonomous system number of the internet provider of the remote IP address.

        - **AsnOrg** *(string) --*

          Organization that registered this ASN.

        - **Isp** *(string) --*

          ISP information for the internet provider.

        - **Org** *(string) --*

          Name of the internet provider.

    - **RemotePortDetails** *(dict) --*

      Remote port information of the connection.

      - **Port** *(integer) --*

        Port number of the remote connection.

      - **PortName** *(string) --*

        Port name of the remote connection.
    """


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef",
    {"Port": int, "PortName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetails` `LocalPortDetails`

    Local port information of the connection.

    - **Port** *(integer) --*

      Port number of the local connection.

    - **PortName** *(string) --*

      Port name of the local connection.
    """


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef",
    {"CityName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetails` `City`

    City information of the remote IP address.

    - **CityName** *(string) --*

      City name of the remote IP address.
    """


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef",
    {"CountryCode": str, "CountryName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetails` `Country`

    Country code of the remote IP address.

    - **CountryCode** *(string) --*

      Country code of the remote IP address.

    - **CountryName** *(string) --*

      Country name of the remote IP address.
    """


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef",
    {"Lat": float, "Lon": float},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetails` `GeoLocation`

    Location information of the remote IP address.

    - **Lat** *(float) --*

      Latitude information of remote IP address.

    - **Lon** *(float) --*

      Longitude information of remote IP address.
    """


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef",
    {"Asn": str, "AsnOrg": str, "Isp": str, "Org": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetails` `Organization`

    ISP Organization information of the remote IP address.

    - **Asn** *(string) --*

      Autonomous system number of the internet provider of the remote IP address.

    - **AsnOrg** *(string) --*

      Organization that registered this ASN.

    - **Isp** *(string) --*

      ISP information for the internet provider.

    - **Org** *(string) --*

      Name of the internet provider.
    """


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef",
    {
        "City": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef,
        "Country": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef,
        "GeoLocation": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef,
        "IpAddressV4": str,
        "Organization": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetails` `RemoteIpDetails`

    Remote IP information of the connection.

    - **City** *(dict) --*

      City information of the remote IP address.

      - **CityName** *(string) --*

        City name of the remote IP address.

    - **Country** *(dict) --*

      Country code of the remote IP address.

      - **CountryCode** *(string) --*

        Country code of the remote IP address.

      - **CountryName** *(string) --*

        Country name of the remote IP address.

    - **GeoLocation** *(dict) --*

      Location information of the remote IP address.

      - **Lat** *(float) --*

        Latitude information of remote IP address.

      - **Lon** *(float) --*

        Longitude information of remote IP address.

    - **IpAddressV4** *(string) --*

      IPV4 remote address of the connection.

    - **Organization** *(dict) --*

      ISP Organization information of the remote IP address.

      - **Asn** *(string) --*

        Autonomous system number of the internet provider of the remote IP address.

      - **AsnOrg** *(string) --*

        Organization that registered this ASN.

      - **Isp** *(string) --*

        ISP information for the internet provider.

      - **Org** *(string) --*

        Name of the internet provider.
    """


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef",
    {
        "LocalPortDetails": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef,
        "RemoteIpDetails": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceActionPortProbeAction` `PortProbeDetails`

    Contains information about the port probe details.

    - **LocalPortDetails** *(dict) --*

      Local port information of the connection.

      - **Port** *(integer) --*

        Port number of the local connection.

      - **PortName** *(string) --*

        Port name of the local connection.

    - **RemoteIpDetails** *(dict) --*

      Remote IP information of the connection.

      - **City** *(dict) --*

        City information of the remote IP address.

        - **CityName** *(string) --*

          City name of the remote IP address.

      - **Country** *(dict) --*

        Country code of the remote IP address.

        - **CountryCode** *(string) --*

          Country code of the remote IP address.

        - **CountryName** *(string) --*

          Country name of the remote IP address.

      - **GeoLocation** *(dict) --*

        Location information of the remote IP address.

        - **Lat** *(float) --*

          Latitude information of remote IP address.

        - **Lon** *(float) --*

          Longitude information of remote IP address.

      - **IpAddressV4** *(string) --*

        IPV4 remote address of the connection.

      - **Organization** *(dict) --*

        ISP Organization information of the remote IP address.

        - **Asn** *(string) --*

          Autonomous system number of the internet provider of the remote IP address.

        - **AsnOrg** *(string) --*

          Organization that registered this ASN.

        - **Isp** *(string) --*

          ISP information for the internet provider.

        - **Org** *(string) --*

          Name of the internet provider.
    """


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef",
    {
        "Blocked": bool,
        "PortProbeDetails": List[
            ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef
        ],
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceAction` `PortProbeAction`

    Information about the PORT_PROBE action described in this finding.

    - **Blocked** *(boolean) --*

      Port probe blocked information.

    - **PortProbeDetails** *(list) --*

      A list of port probe details objects.

      - *(dict) --*

        Contains information about the port probe details.

        - **LocalPortDetails** *(dict) --*

          Local port information of the connection.

          - **Port** *(integer) --*

            Port number of the local connection.

          - **PortName** *(string) --*

            Port name of the local connection.

        - **RemoteIpDetails** *(dict) --*

          Remote IP information of the connection.

          - **City** *(dict) --*

            City information of the remote IP address.

            - **CityName** *(string) --*

              City name of the remote IP address.

          - **Country** *(dict) --*

            Country code of the remote IP address.

            - **CountryCode** *(string) --*

              Country code of the remote IP address.

            - **CountryName** *(string) --*

              Country name of the remote IP address.

          - **GeoLocation** *(dict) --*

            Location information of the remote IP address.

            - **Lat** *(float) --*

              Latitude information of remote IP address.

            - **Lon** *(float) --*

              Longitude information of remote IP address.

          - **IpAddressV4** *(string) --*

            IPV4 remote address of the connection.

          - **Organization** *(dict) --*

            ISP Organization information of the remote IP address.

            - **Asn** *(string) --*

              Autonomous system number of the internet provider of the remote IP address.

            - **AsnOrg** *(string) --*

              Organization that registered this ASN.

            - **Isp** *(string) --*

              ISP information for the internet provider.

            - **Org** *(string) --*

              Name of the internet provider.
    """


_ClientGetFindingsResponseFindingsServiceActionTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionTypeDef",
    {
        "ActionType": str,
        "AwsApiCallAction": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef,
        "DnsRequestAction": ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef,
        "NetworkConnectionAction": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef,
        "PortProbeAction": ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsService` `Action`

    Information about the activity described in a finding.

    - **ActionType** *(string) --*

      GuardDuty Finding activity type.

    - **AwsApiCallAction** *(dict) --*

      Information about the AWS_API_CALL action described in this finding.

      - **Api** *(string) --*

        AWS API name.

      - **CallerType** *(string) --*

        AWS API caller type.

      - **DomainDetails** *(dict) --*

        Domain information for the AWS API call.

        - **Domain** *(string) --*

          Domain information for the AWS API call.

      - **RemoteIpDetails** *(dict) --*

        Remote IP information of the connection.

        - **City** *(dict) --*

          City information of the remote IP address.

          - **CityName** *(string) --*

            City name of the remote IP address.

        - **Country** *(dict) --*

          Country code of the remote IP address.

          - **CountryCode** *(string) --*

            Country code of the remote IP address.

          - **CountryName** *(string) --*

            Country name of the remote IP address.

        - **GeoLocation** *(dict) --*

          Location information of the remote IP address.

          - **Lat** *(float) --*

            Latitude information of remote IP address.

          - **Lon** *(float) --*

            Longitude information of remote IP address.

        - **IpAddressV4** *(string) --*

          IPV4 remote address of the connection.

        - **Organization** *(dict) --*

          ISP Organization information of the remote IP address.

          - **Asn** *(string) --*

            Autonomous system number of the internet provider of the remote IP address.

          - **AsnOrg** *(string) --*

            Organization that registered this ASN.

          - **Isp** *(string) --*

            ISP information for the internet provider.

          - **Org** *(string) --*

            Name of the internet provider.

      - **ServiceName** *(string) --*

        AWS service name whose API was invoked.

    - **DnsRequestAction** *(dict) --*

      Information about the DNS_REQUEST action described in this finding.

      - **Domain** *(string) --*

        Domain information for the API request.

    - **NetworkConnectionAction** *(dict) --*

      Information about the NETWORK_CONNECTION action described in this finding.

      - **Blocked** *(boolean) --*

        Network connection blocked information.

      - **ConnectionDirection** *(string) --*

        Network connection direction.

      - **LocalPortDetails** *(dict) --*

        Local port information of the connection.

        - **Port** *(integer) --*

          Port number of the local connection.

        - **PortName** *(string) --*

          Port name of the local connection.

      - **Protocol** *(string) --*

        Network connection protocol.

      - **RemoteIpDetails** *(dict) --*

        Remote IP information of the connection.

        - **City** *(dict) --*

          City information of the remote IP address.

          - **CityName** *(string) --*

            City name of the remote IP address.

        - **Country** *(dict) --*

          Country code of the remote IP address.

          - **CountryCode** *(string) --*

            Country code of the remote IP address.

          - **CountryName** *(string) --*

            Country name of the remote IP address.

        - **GeoLocation** *(dict) --*

          Location information of the remote IP address.

          - **Lat** *(float) --*

            Latitude information of remote IP address.

          - **Lon** *(float) --*

            Longitude information of remote IP address.

        - **IpAddressV4** *(string) --*

          IPV4 remote address of the connection.

        - **Organization** *(dict) --*

          ISP Organization information of the remote IP address.

          - **Asn** *(string) --*

            Autonomous system number of the internet provider of the remote IP address.

          - **AsnOrg** *(string) --*

            Organization that registered this ASN.

          - **Isp** *(string) --*

            ISP information for the internet provider.

          - **Org** *(string) --*

            Name of the internet provider.

      - **RemotePortDetails** *(dict) --*

        Remote port information of the connection.

        - **Port** *(integer) --*

          Port number of the remote connection.

        - **PortName** *(string) --*

          Port name of the remote connection.

    - **PortProbeAction** *(dict) --*

      Information about the PORT_PROBE action described in this finding.

      - **Blocked** *(boolean) --*

        Port probe blocked information.

      - **PortProbeDetails** *(list) --*

        A list of port probe details objects.

        - *(dict) --*

          Contains information about the port probe details.

          - **LocalPortDetails** *(dict) --*

            Local port information of the connection.

            - **Port** *(integer) --*

              Port number of the local connection.

            - **PortName** *(string) --*

              Port name of the local connection.

          - **RemoteIpDetails** *(dict) --*

            Remote IP information of the connection.

            - **City** *(dict) --*

              City information of the remote IP address.

              - **CityName** *(string) --*

                City name of the remote IP address.

            - **Country** *(dict) --*

              Country code of the remote IP address.

              - **CountryCode** *(string) --*

                Country code of the remote IP address.

              - **CountryName** *(string) --*

                Country name of the remote IP address.

            - **GeoLocation** *(dict) --*

              Location information of the remote IP address.

              - **Lat** *(float) --*

                Latitude information of remote IP address.

              - **Lon** *(float) --*

                Longitude information of remote IP address.

            - **IpAddressV4** *(string) --*

              IPV4 remote address of the connection.

            - **Organization** *(dict) --*

              ISP Organization information of the remote IP address.

              - **Asn** *(string) --*

                Autonomous system number of the internet provider of the remote IP address.

              - **AsnOrg** *(string) --*

                Organization that registered this ASN.

              - **Isp** *(string) --*

                ISP information for the internet provider.

              - **Org** *(string) --*

                Name of the internet provider.
    """


_ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef",
    {"ThreatListName": str, "ThreatNames": List[str]},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsServiceEvidence` `ThreatIntelligenceDetails`

    An instance of a threat intelligence detail that constitutes evidence for the
    finding.

    - **ThreatListName** *(string) --*

      The name of the threat intelligence list that triggered the finding.

    - **ThreatNames** *(list) --*

      A list of names of the threats in the threat intelligence list that triggered the
      finding.

      - *(string) --*
    """


_ClientGetFindingsResponseFindingsServiceEvidenceTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceEvidenceTypeDef",
    {
        "ThreatIntelligenceDetails": List[
            ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef
        ]
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceEvidenceTypeDef(
    _ClientGetFindingsResponseFindingsServiceEvidenceTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindingsService` `Evidence`

    An evidence object associated with the service.

    - **ThreatIntelligenceDetails** *(list) --*

      A list of threat intelligence details related to the evidence.

      - *(dict) --*

        An instance of a threat intelligence detail that constitutes evidence for the
        finding.

        - **ThreatListName** *(string) --*

          The name of the threat intelligence list that triggered the finding.

        - **ThreatNames** *(list) --*

          A list of names of the threats in the threat intelligence list that triggered the
          finding.

          - *(string) --*
    """


_ClientGetFindingsResponseFindingsServiceTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceTypeDef",
    {
        "Action": ClientGetFindingsResponseFindingsServiceActionTypeDef,
        "Evidence": ClientGetFindingsResponseFindingsServiceEvidenceTypeDef,
        "Archived": bool,
        "Count": int,
        "DetectorId": str,
        "EventFirstSeen": str,
        "EventLastSeen": str,
        "ResourceRole": str,
        "ServiceName": str,
        "UserFeedback": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceTypeDef(
    _ClientGetFindingsResponseFindingsServiceTypeDef
):
    """
    Type definition for `ClientGetFindingsResponseFindings` `Service`

    Contains additional information about the generated finding.

    - **Action** *(dict) --*

      Information about the activity described in a finding.

      - **ActionType** *(string) --*

        GuardDuty Finding activity type.

      - **AwsApiCallAction** *(dict) --*

        Information about the AWS_API_CALL action described in this finding.

        - **Api** *(string) --*

          AWS API name.

        - **CallerType** *(string) --*

          AWS API caller type.

        - **DomainDetails** *(dict) --*

          Domain information for the AWS API call.

          - **Domain** *(string) --*

            Domain information for the AWS API call.

        - **RemoteIpDetails** *(dict) --*

          Remote IP information of the connection.

          - **City** *(dict) --*

            City information of the remote IP address.

            - **CityName** *(string) --*

              City name of the remote IP address.

          - **Country** *(dict) --*

            Country code of the remote IP address.

            - **CountryCode** *(string) --*

              Country code of the remote IP address.

            - **CountryName** *(string) --*

              Country name of the remote IP address.

          - **GeoLocation** *(dict) --*

            Location information of the remote IP address.

            - **Lat** *(float) --*

              Latitude information of remote IP address.

            - **Lon** *(float) --*

              Longitude information of remote IP address.

          - **IpAddressV4** *(string) --*

            IPV4 remote address of the connection.

          - **Organization** *(dict) --*

            ISP Organization information of the remote IP address.

            - **Asn** *(string) --*

              Autonomous system number of the internet provider of the remote IP address.

            - **AsnOrg** *(string) --*

              Organization that registered this ASN.

            - **Isp** *(string) --*

              ISP information for the internet provider.

            - **Org** *(string) --*

              Name of the internet provider.

        - **ServiceName** *(string) --*

          AWS service name whose API was invoked.

      - **DnsRequestAction** *(dict) --*

        Information about the DNS_REQUEST action described in this finding.

        - **Domain** *(string) --*

          Domain information for the API request.

      - **NetworkConnectionAction** *(dict) --*

        Information about the NETWORK_CONNECTION action described in this finding.

        - **Blocked** *(boolean) --*

          Network connection blocked information.

        - **ConnectionDirection** *(string) --*

          Network connection direction.

        - **LocalPortDetails** *(dict) --*

          Local port information of the connection.

          - **Port** *(integer) --*

            Port number of the local connection.

          - **PortName** *(string) --*

            Port name of the local connection.

        - **Protocol** *(string) --*

          Network connection protocol.

        - **RemoteIpDetails** *(dict) --*

          Remote IP information of the connection.

          - **City** *(dict) --*

            City information of the remote IP address.

            - **CityName** *(string) --*

              City name of the remote IP address.

          - **Country** *(dict) --*

            Country code of the remote IP address.

            - **CountryCode** *(string) --*

              Country code of the remote IP address.

            - **CountryName** *(string) --*

              Country name of the remote IP address.

          - **GeoLocation** *(dict) --*

            Location information of the remote IP address.

            - **Lat** *(float) --*

              Latitude information of remote IP address.

            - **Lon** *(float) --*

              Longitude information of remote IP address.

          - **IpAddressV4** *(string) --*

            IPV4 remote address of the connection.

          - **Organization** *(dict) --*

            ISP Organization information of the remote IP address.

            - **Asn** *(string) --*

              Autonomous system number of the internet provider of the remote IP address.

            - **AsnOrg** *(string) --*

              Organization that registered this ASN.

            - **Isp** *(string) --*

              ISP information for the internet provider.

            - **Org** *(string) --*

              Name of the internet provider.

        - **RemotePortDetails** *(dict) --*

          Remote port information of the connection.

          - **Port** *(integer) --*

            Port number of the remote connection.

          - **PortName** *(string) --*

            Port name of the remote connection.

      - **PortProbeAction** *(dict) --*

        Information about the PORT_PROBE action described in this finding.

        - **Blocked** *(boolean) --*

          Port probe blocked information.

        - **PortProbeDetails** *(list) --*

          A list of port probe details objects.

          - *(dict) --*

            Contains information about the port probe details.

            - **LocalPortDetails** *(dict) --*

              Local port information of the connection.

              - **Port** *(integer) --*

                Port number of the local connection.

              - **PortName** *(string) --*

                Port name of the local connection.

            - **RemoteIpDetails** *(dict) --*

              Remote IP information of the connection.

              - **City** *(dict) --*

                City information of the remote IP address.

                - **CityName** *(string) --*

                  City name of the remote IP address.

              - **Country** *(dict) --*

                Country code of the remote IP address.

                - **CountryCode** *(string) --*

                  Country code of the remote IP address.

                - **CountryName** *(string) --*

                  Country name of the remote IP address.

              - **GeoLocation** *(dict) --*

                Location information of the remote IP address.

                - **Lat** *(float) --*

                  Latitude information of remote IP address.

                - **Lon** *(float) --*

                  Longitude information of remote IP address.

              - **IpAddressV4** *(string) --*

                IPV4 remote address of the connection.

              - **Organization** *(dict) --*

                ISP Organization information of the remote IP address.

                - **Asn** *(string) --*

                  Autonomous system number of the internet provider of the remote IP address.

                - **AsnOrg** *(string) --*

                  Organization that registered this ASN.

                - **Isp** *(string) --*

                  ISP information for the internet provider.

                - **Org** *(string) --*

                  Name of the internet provider.

    - **Evidence** *(dict) --*

      An evidence object associated with the service.

      - **ThreatIntelligenceDetails** *(list) --*

        A list of threat intelligence details related to the evidence.

        - *(dict) --*

          An instance of a threat intelligence detail that constitutes evidence for the
          finding.

          - **ThreatListName** *(string) --*

            The name of the threat intelligence list that triggered the finding.

          - **ThreatNames** *(list) --*

            A list of names of the threats in the threat intelligence list that triggered the
            finding.

            - *(string) --*

    - **Archived** *(boolean) --*

      Indicates whether this finding is archived.

    - **Count** *(integer) --*

      Total count of the occurrences of this finding type.

    - **DetectorId** *(string) --*

      Detector ID for the GuardDuty service.

    - **EventFirstSeen** *(string) --*

      First seen timestamp of the activity that prompted GuardDuty to generate this finding.

    - **EventLastSeen** *(string) --*

      Last seen timestamp of the activity that prompted GuardDuty to generate this finding.

    - **ResourceRole** *(string) --*

      Resource role information for this finding.

    - **ServiceName** *(string) --*

      The name of the AWS service (GuardDuty) that generated a finding.

    - **UserFeedback** *(string) --*

      Feedback left about the finding.
    """


_ClientGetFindingsResponseFindingsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsTypeDef",
    {
        "AccountId": str,
        "Arn": str,
        "Confidence": float,
        "CreatedAt": str,
        "Description": str,
        "Id": str,
        "Partition": str,
        "Region": str,
        "Resource": ClientGetFindingsResponseFindingsResourceTypeDef,
        "SchemaVersion": str,
        "Service": ClientGetFindingsResponseFindingsServiceTypeDef,
        "Severity": float,
        "Title": str,
        "Type": str,
        "UpdatedAt": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsTypeDef(
    _ClientGetFindingsResponseFindingsTypeDef
):
    """
    Type definition for `ClientGetFindingsResponse` `Findings`

    Contains information about the finding, which is generated when abnormal or suspicious
    activity is detected.

    - **AccountId** *(string) --*

      The ID of the account in which the finding was generated.

    - **Arn** *(string) --*

      The ARN for the finding.

    - **Confidence** *(float) --*

      The confidence score for the finding.

    - **CreatedAt** *(string) --*

      The time and date at which the finding was created.

    - **Description** *(string) --*

      The description of the finding.

    - **Id** *(string) --*

      The ID of the finding.

    - **Partition** *(string) --*

      The partition associated with the finding.

    - **Region** *(string) --*

      The Region in which the finding was generated.

    - **Resource** *(dict) --*

      Contains information about the AWS resource associated with the activity that prompted
      GuardDuty to generate a finding.

      - **AccessKeyDetails** *(dict) --*

        The IAM access key details (IAM user information) of a user that engaged in the
        activity that prompted GuardDuty to generate a finding.

        - **AccessKeyId** *(string) --*

          Access key ID of the user.

        - **PrincipalId** *(string) --*

          The principal ID of the user.

        - **UserName** *(string) --*

          The name of the user.

        - **UserType** *(string) --*

          The type of the user.

      - **InstanceDetails** *(dict) --*

        The information about the EC2 instance associated with the activity that prompted
        GuardDuty to generate a finding.

        - **AvailabilityZone** *(string) --*

          The availability zone of the EC2 instance.

        - **IamInstanceProfile** *(dict) --*

          The profile information of the EC2 instance.

          - **Arn** *(string) --*

            AWS EC2 instance profile ARN.

          - **Id** *(string) --*

            AWS EC2 instance profile ID.

        - **ImageDescription** *(string) --*

          The image description of the EC2 instance.

        - **ImageId** *(string) --*

          The image ID of the EC2 instance.

        - **InstanceId** *(string) --*

          The ID of the EC2 instance.

        - **InstanceState** *(string) --*

          The state of the EC2 instance.

        - **InstanceType** *(string) --*

          The type of the EC2 instance.

        - **LaunchTime** *(string) --*

          The launch time of the EC2 instance.

        - **NetworkInterfaces** *(list) --*

          The network interface information of the EC2 instance.

          - *(dict) --*

            Contains information about the network interface of the Ec2 instance.

            - **Ipv6Addresses** *(list) --*

              A list of EC2 instance IPv6 address information.

              - *(string) --*

            - **NetworkInterfaceId** *(string) --*

              The ID of the network interface

            - **PrivateDnsName** *(string) --*

              Private DNS name of the EC2 instance.

            - **PrivateIpAddress** *(string) --*

              Private IP address of the EC2 instance.

            - **PrivateIpAddresses** *(list) --*

              Other private IP address information of the EC2 instance.

              - *(dict) --*

                Contains other private IP address information of the EC2 instance.

                - **PrivateDnsName** *(string) --*

                  Private DNS name of the EC2 instance.

                - **PrivateIpAddress** *(string) --*

                  Private IP address of the EC2 instance.

            - **PublicDnsName** *(string) --*

              Public DNS name of the EC2 instance.

            - **PublicIp** *(string) --*

              Public IP address of the EC2 instance.

            - **SecurityGroups** *(list) --*

              Security groups associated with the EC2 instance.

              - *(dict) --*

                Contains information about the security groups associated with the EC2 instance.

                - **GroupId** *(string) --*

                  EC2 instance's security group ID.

                - **GroupName** *(string) --*

                  EC2 instance's security group name.

            - **SubnetId** *(string) --*

              The subnet ID of the EC2 instance.

            - **VpcId** *(string) --*

              The VPC ID of the EC2 instance.

        - **Platform** *(string) --*

          The platform of the EC2 instance.

        - **ProductCodes** *(list) --*

          The product code of the EC2 instance.

          - *(dict) --*

            Contains information about the product code for the Ec2 instance.

            - **Code** *(string) --*

              Product code information.

            - **ProductType** *(string) --*

              Product code type.

        - **Tags** *(list) --*

          The tags of the EC2 instance.

          - *(dict) --*

            Contains information about a tag associated with the Ec2 instance.

            - **Key** *(string) --*

              EC2 instance tag key.

            - **Value** *(string) --*

              EC2 instance tag value.

      - **ResourceType** *(string) --*

        The type of the AWS resource.

    - **SchemaVersion** *(string) --*

      The version of the schema used for the finding.

    - **Service** *(dict) --*

      Contains additional information about the generated finding.

      - **Action** *(dict) --*

        Information about the activity described in a finding.

        - **ActionType** *(string) --*

          GuardDuty Finding activity type.

        - **AwsApiCallAction** *(dict) --*

          Information about the AWS_API_CALL action described in this finding.

          - **Api** *(string) --*

            AWS API name.

          - **CallerType** *(string) --*

            AWS API caller type.

          - **DomainDetails** *(dict) --*

            Domain information for the AWS API call.

            - **Domain** *(string) --*

              Domain information for the AWS API call.

          - **RemoteIpDetails** *(dict) --*

            Remote IP information of the connection.

            - **City** *(dict) --*

              City information of the remote IP address.

              - **CityName** *(string) --*

                City name of the remote IP address.

            - **Country** *(dict) --*

              Country code of the remote IP address.

              - **CountryCode** *(string) --*

                Country code of the remote IP address.

              - **CountryName** *(string) --*

                Country name of the remote IP address.

            - **GeoLocation** *(dict) --*

              Location information of the remote IP address.

              - **Lat** *(float) --*

                Latitude information of remote IP address.

              - **Lon** *(float) --*

                Longitude information of remote IP address.

            - **IpAddressV4** *(string) --*

              IPV4 remote address of the connection.

            - **Organization** *(dict) --*

              ISP Organization information of the remote IP address.

              - **Asn** *(string) --*

                Autonomous system number of the internet provider of the remote IP address.

              - **AsnOrg** *(string) --*

                Organization that registered this ASN.

              - **Isp** *(string) --*

                ISP information for the internet provider.

              - **Org** *(string) --*

                Name of the internet provider.

          - **ServiceName** *(string) --*

            AWS service name whose API was invoked.

        - **DnsRequestAction** *(dict) --*

          Information about the DNS_REQUEST action described in this finding.

          - **Domain** *(string) --*

            Domain information for the API request.

        - **NetworkConnectionAction** *(dict) --*

          Information about the NETWORK_CONNECTION action described in this finding.

          - **Blocked** *(boolean) --*

            Network connection blocked information.

          - **ConnectionDirection** *(string) --*

            Network connection direction.

          - **LocalPortDetails** *(dict) --*

            Local port information of the connection.

            - **Port** *(integer) --*

              Port number of the local connection.

            - **PortName** *(string) --*

              Port name of the local connection.

          - **Protocol** *(string) --*

            Network connection protocol.

          - **RemoteIpDetails** *(dict) --*

            Remote IP information of the connection.

            - **City** *(dict) --*

              City information of the remote IP address.

              - **CityName** *(string) --*

                City name of the remote IP address.

            - **Country** *(dict) --*

              Country code of the remote IP address.

              - **CountryCode** *(string) --*

                Country code of the remote IP address.

              - **CountryName** *(string) --*

                Country name of the remote IP address.

            - **GeoLocation** *(dict) --*

              Location information of the remote IP address.

              - **Lat** *(float) --*

                Latitude information of remote IP address.

              - **Lon** *(float) --*

                Longitude information of remote IP address.

            - **IpAddressV4** *(string) --*

              IPV4 remote address of the connection.

            - **Organization** *(dict) --*

              ISP Organization information of the remote IP address.

              - **Asn** *(string) --*

                Autonomous system number of the internet provider of the remote IP address.

              - **AsnOrg** *(string) --*

                Organization that registered this ASN.

              - **Isp** *(string) --*

                ISP information for the internet provider.

              - **Org** *(string) --*

                Name of the internet provider.

          - **RemotePortDetails** *(dict) --*

            Remote port information of the connection.

            - **Port** *(integer) --*

              Port number of the remote connection.

            - **PortName** *(string) --*

              Port name of the remote connection.

        - **PortProbeAction** *(dict) --*

          Information about the PORT_PROBE action described in this finding.

          - **Blocked** *(boolean) --*

            Port probe blocked information.

          - **PortProbeDetails** *(list) --*

            A list of port probe details objects.

            - *(dict) --*

              Contains information about the port probe details.

              - **LocalPortDetails** *(dict) --*

                Local port information of the connection.

                - **Port** *(integer) --*

                  Port number of the local connection.

                - **PortName** *(string) --*

                  Port name of the local connection.

              - **RemoteIpDetails** *(dict) --*

                Remote IP information of the connection.

                - **City** *(dict) --*

                  City information of the remote IP address.

                  - **CityName** *(string) --*

                    City name of the remote IP address.

                - **Country** *(dict) --*

                  Country code of the remote IP address.

                  - **CountryCode** *(string) --*

                    Country code of the remote IP address.

                  - **CountryName** *(string) --*

                    Country name of the remote IP address.

                - **GeoLocation** *(dict) --*

                  Location information of the remote IP address.

                  - **Lat** *(float) --*

                    Latitude information of remote IP address.

                  - **Lon** *(float) --*

                    Longitude information of remote IP address.

                - **IpAddressV4** *(string) --*

                  IPV4 remote address of the connection.

                - **Organization** *(dict) --*

                  ISP Organization information of the remote IP address.

                  - **Asn** *(string) --*

                    Autonomous system number of the internet provider of the remote IP address.

                  - **AsnOrg** *(string) --*

                    Organization that registered this ASN.

                  - **Isp** *(string) --*

                    ISP information for the internet provider.

                  - **Org** *(string) --*

                    Name of the internet provider.

      - **Evidence** *(dict) --*

        An evidence object associated with the service.

        - **ThreatIntelligenceDetails** *(list) --*

          A list of threat intelligence details related to the evidence.

          - *(dict) --*

            An instance of a threat intelligence detail that constitutes evidence for the
            finding.

            - **ThreatListName** *(string) --*

              The name of the threat intelligence list that triggered the finding.

            - **ThreatNames** *(list) --*

              A list of names of the threats in the threat intelligence list that triggered the
              finding.

              - *(string) --*

      - **Archived** *(boolean) --*

        Indicates whether this finding is archived.

      - **Count** *(integer) --*

        Total count of the occurrences of this finding type.

      - **DetectorId** *(string) --*

        Detector ID for the GuardDuty service.

      - **EventFirstSeen** *(string) --*

        First seen timestamp of the activity that prompted GuardDuty to generate this finding.

      - **EventLastSeen** *(string) --*

        Last seen timestamp of the activity that prompted GuardDuty to generate this finding.

      - **ResourceRole** *(string) --*

        Resource role information for this finding.

      - **ServiceName** *(string) --*

        The name of the AWS service (GuardDuty) that generated a finding.

      - **UserFeedback** *(string) --*

        Feedback left about the finding.

    - **Severity** *(float) --*

      The severity of the finding.

    - **Title** *(string) --*

      The title for the finding.

    - **Type** *(string) --*

      The type of the finding.

    - **UpdatedAt** *(string) --*

      The time and date at which the finding was laste updated.
    """


_ClientGetFindingsResponseTypeDef = TypedDict(
    "_ClientGetFindingsResponseTypeDef",
    {"Findings": List[ClientGetFindingsResponseFindingsTypeDef]},
    total=False,
)


class ClientGetFindingsResponseTypeDef(_ClientGetFindingsResponseTypeDef):
    """
    Type definition for `ClientGetFindings` `Response`

    - **Findings** *(list) --*

      A list of findings.

      - *(dict) --*

        Contains information about the finding, which is generated when abnormal or suspicious
        activity is detected.

        - **AccountId** *(string) --*

          The ID of the account in which the finding was generated.

        - **Arn** *(string) --*

          The ARN for the finding.

        - **Confidence** *(float) --*

          The confidence score for the finding.

        - **CreatedAt** *(string) --*

          The time and date at which the finding was created.

        - **Description** *(string) --*

          The description of the finding.

        - **Id** *(string) --*

          The ID of the finding.

        - **Partition** *(string) --*

          The partition associated with the finding.

        - **Region** *(string) --*

          The Region in which the finding was generated.

        - **Resource** *(dict) --*

          Contains information about the AWS resource associated with the activity that prompted
          GuardDuty to generate a finding.

          - **AccessKeyDetails** *(dict) --*

            The IAM access key details (IAM user information) of a user that engaged in the
            activity that prompted GuardDuty to generate a finding.

            - **AccessKeyId** *(string) --*

              Access key ID of the user.

            - **PrincipalId** *(string) --*

              The principal ID of the user.

            - **UserName** *(string) --*

              The name of the user.

            - **UserType** *(string) --*

              The type of the user.

          - **InstanceDetails** *(dict) --*

            The information about the EC2 instance associated with the activity that prompted
            GuardDuty to generate a finding.

            - **AvailabilityZone** *(string) --*

              The availability zone of the EC2 instance.

            - **IamInstanceProfile** *(dict) --*

              The profile information of the EC2 instance.

              - **Arn** *(string) --*

                AWS EC2 instance profile ARN.

              - **Id** *(string) --*

                AWS EC2 instance profile ID.

            - **ImageDescription** *(string) --*

              The image description of the EC2 instance.

            - **ImageId** *(string) --*

              The image ID of the EC2 instance.

            - **InstanceId** *(string) --*

              The ID of the EC2 instance.

            - **InstanceState** *(string) --*

              The state of the EC2 instance.

            - **InstanceType** *(string) --*

              The type of the EC2 instance.

            - **LaunchTime** *(string) --*

              The launch time of the EC2 instance.

            - **NetworkInterfaces** *(list) --*

              The network interface information of the EC2 instance.

              - *(dict) --*

                Contains information about the network interface of the Ec2 instance.

                - **Ipv6Addresses** *(list) --*

                  A list of EC2 instance IPv6 address information.

                  - *(string) --*

                - **NetworkInterfaceId** *(string) --*

                  The ID of the network interface

                - **PrivateDnsName** *(string) --*

                  Private DNS name of the EC2 instance.

                - **PrivateIpAddress** *(string) --*

                  Private IP address of the EC2 instance.

                - **PrivateIpAddresses** *(list) --*

                  Other private IP address information of the EC2 instance.

                  - *(dict) --*

                    Contains other private IP address information of the EC2 instance.

                    - **PrivateDnsName** *(string) --*

                      Private DNS name of the EC2 instance.

                    - **PrivateIpAddress** *(string) --*

                      Private IP address of the EC2 instance.

                - **PublicDnsName** *(string) --*

                  Public DNS name of the EC2 instance.

                - **PublicIp** *(string) --*

                  Public IP address of the EC2 instance.

                - **SecurityGroups** *(list) --*

                  Security groups associated with the EC2 instance.

                  - *(dict) --*

                    Contains information about the security groups associated with the EC2 instance.

                    - **GroupId** *(string) --*

                      EC2 instance's security group ID.

                    - **GroupName** *(string) --*

                      EC2 instance's security group name.

                - **SubnetId** *(string) --*

                  The subnet ID of the EC2 instance.

                - **VpcId** *(string) --*

                  The VPC ID of the EC2 instance.

            - **Platform** *(string) --*

              The platform of the EC2 instance.

            - **ProductCodes** *(list) --*

              The product code of the EC2 instance.

              - *(dict) --*

                Contains information about the product code for the Ec2 instance.

                - **Code** *(string) --*

                  Product code information.

                - **ProductType** *(string) --*

                  Product code type.

            - **Tags** *(list) --*

              The tags of the EC2 instance.

              - *(dict) --*

                Contains information about a tag associated with the Ec2 instance.

                - **Key** *(string) --*

                  EC2 instance tag key.

                - **Value** *(string) --*

                  EC2 instance tag value.

          - **ResourceType** *(string) --*

            The type of the AWS resource.

        - **SchemaVersion** *(string) --*

          The version of the schema used for the finding.

        - **Service** *(dict) --*

          Contains additional information about the generated finding.

          - **Action** *(dict) --*

            Information about the activity described in a finding.

            - **ActionType** *(string) --*

              GuardDuty Finding activity type.

            - **AwsApiCallAction** *(dict) --*

              Information about the AWS_API_CALL action described in this finding.

              - **Api** *(string) --*

                AWS API name.

              - **CallerType** *(string) --*

                AWS API caller type.

              - **DomainDetails** *(dict) --*

                Domain information for the AWS API call.

                - **Domain** *(string) --*

                  Domain information for the AWS API call.

              - **RemoteIpDetails** *(dict) --*

                Remote IP information of the connection.

                - **City** *(dict) --*

                  City information of the remote IP address.

                  - **CityName** *(string) --*

                    City name of the remote IP address.

                - **Country** *(dict) --*

                  Country code of the remote IP address.

                  - **CountryCode** *(string) --*

                    Country code of the remote IP address.

                  - **CountryName** *(string) --*

                    Country name of the remote IP address.

                - **GeoLocation** *(dict) --*

                  Location information of the remote IP address.

                  - **Lat** *(float) --*

                    Latitude information of remote IP address.

                  - **Lon** *(float) --*

                    Longitude information of remote IP address.

                - **IpAddressV4** *(string) --*

                  IPV4 remote address of the connection.

                - **Organization** *(dict) --*

                  ISP Organization information of the remote IP address.

                  - **Asn** *(string) --*

                    Autonomous system number of the internet provider of the remote IP address.

                  - **AsnOrg** *(string) --*

                    Organization that registered this ASN.

                  - **Isp** *(string) --*

                    ISP information for the internet provider.

                  - **Org** *(string) --*

                    Name of the internet provider.

              - **ServiceName** *(string) --*

                AWS service name whose API was invoked.

            - **DnsRequestAction** *(dict) --*

              Information about the DNS_REQUEST action described in this finding.

              - **Domain** *(string) --*

                Domain information for the API request.

            - **NetworkConnectionAction** *(dict) --*

              Information about the NETWORK_CONNECTION action described in this finding.

              - **Blocked** *(boolean) --*

                Network connection blocked information.

              - **ConnectionDirection** *(string) --*

                Network connection direction.

              - **LocalPortDetails** *(dict) --*

                Local port information of the connection.

                - **Port** *(integer) --*

                  Port number of the local connection.

                - **PortName** *(string) --*

                  Port name of the local connection.

              - **Protocol** *(string) --*

                Network connection protocol.

              - **RemoteIpDetails** *(dict) --*

                Remote IP information of the connection.

                - **City** *(dict) --*

                  City information of the remote IP address.

                  - **CityName** *(string) --*

                    City name of the remote IP address.

                - **Country** *(dict) --*

                  Country code of the remote IP address.

                  - **CountryCode** *(string) --*

                    Country code of the remote IP address.

                  - **CountryName** *(string) --*

                    Country name of the remote IP address.

                - **GeoLocation** *(dict) --*

                  Location information of the remote IP address.

                  - **Lat** *(float) --*

                    Latitude information of remote IP address.

                  - **Lon** *(float) --*

                    Longitude information of remote IP address.

                - **IpAddressV4** *(string) --*

                  IPV4 remote address of the connection.

                - **Organization** *(dict) --*

                  ISP Organization information of the remote IP address.

                  - **Asn** *(string) --*

                    Autonomous system number of the internet provider of the remote IP address.

                  - **AsnOrg** *(string) --*

                    Organization that registered this ASN.

                  - **Isp** *(string) --*

                    ISP information for the internet provider.

                  - **Org** *(string) --*

                    Name of the internet provider.

              - **RemotePortDetails** *(dict) --*

                Remote port information of the connection.

                - **Port** *(integer) --*

                  Port number of the remote connection.

                - **PortName** *(string) --*

                  Port name of the remote connection.

            - **PortProbeAction** *(dict) --*

              Information about the PORT_PROBE action described in this finding.

              - **Blocked** *(boolean) --*

                Port probe blocked information.

              - **PortProbeDetails** *(list) --*

                A list of port probe details objects.

                - *(dict) --*

                  Contains information about the port probe details.

                  - **LocalPortDetails** *(dict) --*

                    Local port information of the connection.

                    - **Port** *(integer) --*

                      Port number of the local connection.

                    - **PortName** *(string) --*

                      Port name of the local connection.

                  - **RemoteIpDetails** *(dict) --*

                    Remote IP information of the connection.

                    - **City** *(dict) --*

                      City information of the remote IP address.

                      - **CityName** *(string) --*

                        City name of the remote IP address.

                    - **Country** *(dict) --*

                      Country code of the remote IP address.

                      - **CountryCode** *(string) --*

                        Country code of the remote IP address.

                      - **CountryName** *(string) --*

                        Country name of the remote IP address.

                    - **GeoLocation** *(dict) --*

                      Location information of the remote IP address.

                      - **Lat** *(float) --*

                        Latitude information of remote IP address.

                      - **Lon** *(float) --*

                        Longitude information of remote IP address.

                    - **IpAddressV4** *(string) --*

                      IPV4 remote address of the connection.

                    - **Organization** *(dict) --*

                      ISP Organization information of the remote IP address.

                      - **Asn** *(string) --*

                        Autonomous system number of the internet provider of the remote IP address.

                      - **AsnOrg** *(string) --*

                        Organization that registered this ASN.

                      - **Isp** *(string) --*

                        ISP information for the internet provider.

                      - **Org** *(string) --*

                        Name of the internet provider.

          - **Evidence** *(dict) --*

            An evidence object associated with the service.

            - **ThreatIntelligenceDetails** *(list) --*

              A list of threat intelligence details related to the evidence.

              - *(dict) --*

                An instance of a threat intelligence detail that constitutes evidence for the
                finding.

                - **ThreatListName** *(string) --*

                  The name of the threat intelligence list that triggered the finding.

                - **ThreatNames** *(list) --*

                  A list of names of the threats in the threat intelligence list that triggered the
                  finding.

                  - *(string) --*

          - **Archived** *(boolean) --*

            Indicates whether this finding is archived.

          - **Count** *(integer) --*

            Total count of the occurrences of this finding type.

          - **DetectorId** *(string) --*

            Detector ID for the GuardDuty service.

          - **EventFirstSeen** *(string) --*

            First seen timestamp of the activity that prompted GuardDuty to generate this finding.

          - **EventLastSeen** *(string) --*

            Last seen timestamp of the activity that prompted GuardDuty to generate this finding.

          - **ResourceRole** *(string) --*

            Resource role information for this finding.

          - **ServiceName** *(string) --*

            The name of the AWS service (GuardDuty) that generated a finding.

          - **UserFeedback** *(string) --*

            Feedback left about the finding.

        - **Severity** *(float) --*

          The severity of the finding.

        - **Title** *(string) --*

          The title for the finding.

        - **Type** *(string) --*

          The type of the finding.

        - **UpdatedAt** *(string) --*

          The time and date at which the finding was laste updated.
    """


_ClientGetFindingsSortCriteriaTypeDef = TypedDict(
    "_ClientGetFindingsSortCriteriaTypeDef",
    {"AttributeName": str, "OrderBy": str},
    total=False,
)


class ClientGetFindingsSortCriteriaTypeDef(_ClientGetFindingsSortCriteriaTypeDef):
    """
    Type definition for `ClientGetFindings` `SortCriteria`

    Represents the criteria used for sorting findings.

    - **AttributeName** *(string) --*

      Represents the finding attribute (for example, accountId) by which to sort findings.

    - **OrderBy** *(string) --*

      Order by which the sorted findings are to be displayed.
    """


_ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef = TypedDict(
    "_ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef(
    _ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef
):
    """
    Type definition for `ClientGetFindingsStatisticsFindingCriteria` `Criterion`

    Contains information about the condition.

    - **Eq** *(list) --*

      Represents the equal condition to be applied to a single field when querying for findings.

      - *(string) --*

    - **Neq** *(list) --*

      Represents the not equal condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **Gt** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **Gte** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when querying
      for findings.

    - **Lt** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **Lte** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying for
      findings.

    - **Equals** *(list) --*

      Represents an **equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **NotEquals** *(list) --*

      Represents an **not equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **GreaterThan** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **GreaterThanOrEqual** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when querying
      for findings.

    - **LessThan** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **LessThanOrEqual** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying for
      findings.
    """


_ClientGetFindingsStatisticsFindingCriteriaTypeDef = TypedDict(
    "_ClientGetFindingsStatisticsFindingCriteriaTypeDef",
    {
        "Criterion": Dict[
            str, ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef
        ]
    },
    total=False,
)


class ClientGetFindingsStatisticsFindingCriteriaTypeDef(
    _ClientGetFindingsStatisticsFindingCriteriaTypeDef
):
    """
    Type definition for `ClientGetFindingsStatistics` `FindingCriteria`

    Represents the criteria used for querying findings.

    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when querying
      findings.

      - *(string) --*

        - *(dict) --*

          Contains information about the condition.

          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for findings.

            - *(string) --*

          - **Neq** *(list) --*

            Represents the not equal condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **Gt** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **Gte** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when querying
            for findings.

          - **Lt** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **Lte** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying for
            findings.

          - **Equals** *(list) --*

            Represents an **equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **NotEquals** *(list) --*

            Represents an **not equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **GreaterThan** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **GreaterThanOrEqual** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when querying
            for findings.

          - **LessThan** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **LessThanOrEqual** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying for
            findings.
    """


_ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef = TypedDict(
    "_ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef",
    {"CountBySeverity": Dict[str, int]},
    total=False,
)


class ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef(
    _ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef
):
    """
    Type definition for `ClientGetFindingsStatisticsResponse` `FindingStatistics`

    Finding statistics object.

    - **CountBySeverity** *(dict) --*

      Represents a map of severity to count statistic for a set of findings

      - *(string) --*

        - *(integer) --*
    """


_ClientGetFindingsStatisticsResponseTypeDef = TypedDict(
    "_ClientGetFindingsStatisticsResponseTypeDef",
    {"FindingStatistics": ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef},
    total=False,
)


class ClientGetFindingsStatisticsResponseTypeDef(
    _ClientGetFindingsStatisticsResponseTypeDef
):
    """
    Type definition for `ClientGetFindingsStatistics` `Response`

    - **FindingStatistics** *(dict) --*

      Finding statistics object.

      - **CountBySeverity** *(dict) --*

        Represents a map of severity to count statistic for a set of findings

        - *(string) --*

          - *(integer) --*
    """


_ClientGetInvitationsCountResponseTypeDef = TypedDict(
    "_ClientGetInvitationsCountResponseTypeDef", {"InvitationsCount": int}, total=False
)


class ClientGetInvitationsCountResponseTypeDef(
    _ClientGetInvitationsCountResponseTypeDef
):
    """
    Type definition for `ClientGetInvitationsCount` `Response`

    - **InvitationsCount** *(integer) --*

      The number of received invitations.
    """


_ClientGetIpSetResponseTypeDef = TypedDict(
    "_ClientGetIpSetResponseTypeDef",
    {
        "Name": str,
        "Format": str,
        "Location": str,
        "Status": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetIpSetResponseTypeDef(_ClientGetIpSetResponseTypeDef):
    """
    Type definition for `ClientGetIpSet` `Response`

    - **Name** *(string) --*

      The user friendly name for the IPSet.

    - **Format** *(string) --*

      The format of the file that contains the IPSet.

    - **Location** *(string) --*

      The URI of the file that contains the IPSet. For example
      (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)

    - **Status** *(string) --*

      The status of ipSet file uploaded.

    - **Tags** *(dict) --*

      The tags of the IP set resource.

      - *(string) --*

        - *(string) --*
    """


_ClientGetMasterAccountResponseMasterTypeDef = TypedDict(
    "_ClientGetMasterAccountResponseMasterTypeDef",
    {
        "AccountId": str,
        "InvitationId": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
    },
    total=False,
)


class ClientGetMasterAccountResponseMasterTypeDef(
    _ClientGetMasterAccountResponseMasterTypeDef
):
    """
    Type definition for `ClientGetMasterAccountResponse` `Master`

    Master account details.

    - **AccountId** *(string) --*

      The ID of the account used as the Master account.

    - **InvitationId** *(string) --*

      This value is used to validate the master account to the member account.

    - **RelationshipStatus** *(string) --*

      The status of the relationship between the master and member accounts.

    - **InvitedAt** *(string) --*

      Timestamp at which the invitation was sent.
    """


_ClientGetMasterAccountResponseTypeDef = TypedDict(
    "_ClientGetMasterAccountResponseTypeDef",
    {"Master": ClientGetMasterAccountResponseMasterTypeDef},
    total=False,
)


class ClientGetMasterAccountResponseTypeDef(_ClientGetMasterAccountResponseTypeDef):
    """
    Type definition for `ClientGetMasterAccount` `Response`

    - **Master** *(dict) --*

      Master account details.

      - **AccountId** *(string) --*

        The ID of the account used as the Master account.

      - **InvitationId** *(string) --*

        This value is used to validate the master account to the member account.

      - **RelationshipStatus** *(string) --*

        The status of the relationship between the master and member accounts.

      - **InvitedAt** *(string) --*

        Timestamp at which the invitation was sent.
    """


_ClientGetMembersResponseMembersTypeDef = TypedDict(
    "_ClientGetMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "DetectorId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
        "UpdatedAt": str,
    },
    total=False,
)


class ClientGetMembersResponseMembersTypeDef(_ClientGetMembersResponseMembersTypeDef):
    """
    Type definition for `ClientGetMembersResponse` `Members`

    Continas information about the member account

    - **AccountId** *(string) --*

      Member account ID.

    - **DetectorId** *(string) --*

      Member account's detector ID.

    - **MasterId** *(string) --*

      Master account ID.

    - **Email** *(string) --*

      Member account's email address.

    - **RelationshipStatus** *(string) --*

      The status of the relationship between the member and the master.

    - **InvitedAt** *(string) --*

      Timestamp at which the invitation was sent

    - **UpdatedAt** *(string) --*

      Member last updated timestamp.
    """


_ClientGetMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientGetMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientGetMembersResponseUnprocessedAccountsTypeDef(
    _ClientGetMembersResponseUnprocessedAccountsTypeDef
):
    """
    Type definition for `ClientGetMembersResponse` `UnprocessedAccounts`

    Contains information about the accounts that were not processed.

    - **AccountId** *(string) --*

      AWS Account ID.

    - **Result** *(string) --*

      A reason why the account hasn't been processed.
    """


_ClientGetMembersResponseTypeDef = TypedDict(
    "_ClientGetMembersResponseTypeDef",
    {
        "Members": List[ClientGetMembersResponseMembersTypeDef],
        "UnprocessedAccounts": List[ClientGetMembersResponseUnprocessedAccountsTypeDef],
    },
    total=False,
)


class ClientGetMembersResponseTypeDef(_ClientGetMembersResponseTypeDef):
    """
    Type definition for `ClientGetMembers` `Response`

    - **Members** *(list) --*

      A list of members.

      - *(dict) --*

        Continas information about the member account

        - **AccountId** *(string) --*

          Member account ID.

        - **DetectorId** *(string) --*

          Member account's detector ID.

        - **MasterId** *(string) --*

          Master account ID.

        - **Email** *(string) --*

          Member account's email address.

        - **RelationshipStatus** *(string) --*

          The status of the relationship between the member and the master.

        - **InvitedAt** *(string) --*

          Timestamp at which the invitation was sent

        - **UpdatedAt** *(string) --*

          Member last updated timestamp.

    - **UnprocessedAccounts** *(list) --*

      A list of objects containing the unprocessed account and a result string explaining why it
      was unprocessed.

      - *(dict) --*

        Contains information about the accounts that were not processed.

        - **AccountId** *(string) --*

          AWS Account ID.

        - **Result** *(string) --*

          A reason why the account hasn't been processed.
    """


_ClientGetThreatIntelSetResponseTypeDef = TypedDict(
    "_ClientGetThreatIntelSetResponseTypeDef",
    {
        "Name": str,
        "Format": str,
        "Location": str,
        "Status": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetThreatIntelSetResponseTypeDef(_ClientGetThreatIntelSetResponseTypeDef):
    """
    Type definition for `ClientGetThreatIntelSet` `Response`

    - **Name** *(string) --*

      A user-friendly ThreatIntelSet name that is displayed in all finding generated by activity
      that involves IP addresses included in this ThreatIntelSet.

    - **Format** *(string) --*

      The format of the threatIntelSet.

    - **Location** *(string) --*

      The URI of the file that contains the ThreatIntelSet. For example
      (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).

    - **Status** *(string) --*

      The status of threatIntelSet file uploaded.

    - **Tags** *(dict) --*

      The tags of the Threat List resource.

      - *(string) --*

        - *(string) --*
    """


_ClientInviteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientInviteMembersResponseUnprocessedAccountsTypeDef(
    _ClientInviteMembersResponseUnprocessedAccountsTypeDef
):
    """
    Type definition for `ClientInviteMembersResponse` `UnprocessedAccounts`

    Contains information about the accounts that were not processed.

    - **AccountId** *(string) --*

      AWS Account ID.

    - **Result** *(string) --*

      A reason why the account hasn't been processed.
    """


_ClientInviteMembersResponseTypeDef = TypedDict(
    "_ClientInviteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[
            ClientInviteMembersResponseUnprocessedAccountsTypeDef
        ]
    },
    total=False,
)


class ClientInviteMembersResponseTypeDef(_ClientInviteMembersResponseTypeDef):
    """
    Type definition for `ClientInviteMembers` `Response`

    - **UnprocessedAccounts** *(list) --*

      A list of objects containing the unprocessed account and a result string explaining why it
      was unprocessed.

      - *(dict) --*

        Contains information about the accounts that were not processed.

        - **AccountId** *(string) --*

          AWS Account ID.

        - **Result** *(string) --*

          A reason why the account hasn't been processed.
    """


_ClientListDetectorsResponseTypeDef = TypedDict(
    "_ClientListDetectorsResponseTypeDef",
    {"DetectorIds": List[str], "NextToken": str},
    total=False,
)


class ClientListDetectorsResponseTypeDef(_ClientListDetectorsResponseTypeDef):
    """
    Type definition for `ClientListDetectors` `Response`

    - **DetectorIds** *(list) --*

      A list of detector Ids.

      - *(string) --*

    - **NextToken** *(string) --*

      Pagination parameter to be used on the next list operation to retrieve more items.
    """


_ClientListFiltersResponseTypeDef = TypedDict(
    "_ClientListFiltersResponseTypeDef",
    {"FilterNames": List[str], "NextToken": str},
    total=False,
)


class ClientListFiltersResponseTypeDef(_ClientListFiltersResponseTypeDef):
    """
    Type definition for `ClientListFilters` `Response`

    - **FilterNames** *(list) --*

      A list of filter names

      - *(string) --*

    - **NextToken** *(string) --*

      Pagination parameter to be used on the next list operation to retrieve more items.
    """


_ClientListFindingsFindingCriteriaCriterionTypeDef = TypedDict(
    "_ClientListFindingsFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ClientListFindingsFindingCriteriaCriterionTypeDef(
    _ClientListFindingsFindingCriteriaCriterionTypeDef
):
    """
    Type definition for `ClientListFindingsFindingCriteria` `Criterion`

    Contains information about the condition.

    - **Eq** *(list) --*

      Represents the equal condition to be applied to a single field when querying for findings.

      - *(string) --*

    - **Neq** *(list) --*

      Represents the not equal condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **Gt** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **Gte** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when querying
      for findings.

    - **Lt** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **Lte** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying for
      findings.

    - **Equals** *(list) --*

      Represents an **equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **NotEquals** *(list) --*

      Represents an **not equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **GreaterThan** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **GreaterThanOrEqual** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when querying
      for findings.

    - **LessThan** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **LessThanOrEqual** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying for
      findings.
    """


_ClientListFindingsFindingCriteriaTypeDef = TypedDict(
    "_ClientListFindingsFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientListFindingsFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ClientListFindingsFindingCriteriaTypeDef(
    _ClientListFindingsFindingCriteriaTypeDef
):
    """
    Type definition for `ClientListFindings` `FindingCriteria`

    Represents the criteria used for querying findings. Valid values include:

    * JSON field name

    * accountId

    * region

    * confidence

    * id

    * resource.accessKeyDetails.accessKeyId

    * resource.accessKeyDetails.principalId

    * resource.accessKeyDetails.userName

    * resource.accessKeyDetails.userType

    * resource.instanceDetails.iamInstanceProfile.id

    * resource.instanceDetails.imageId

    * resource.instanceDetails.instanceId

    * resource.instanceDetails.networkInterfaces.ipv6Addresses

    * resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress

    * resource.instanceDetails.networkInterfaces.publicDnsName

    * resource.instanceDetails.networkInterfaces.publicIp

    * resource.instanceDetails.networkInterfaces.securityGroups.groupId

    * resource.instanceDetails.networkInterfaces.securityGroups.groupName

    * resource.instanceDetails.networkInterfaces.subnetId

    * resource.instanceDetails.networkInterfaces.vpcId

    * resource.instanceDetails.tags.key

    * resource.instanceDetails.tags.value

    * resource.resourceType

    * service.action.actionType

    * service.action.awsApiCallAction.api

    * service.action.awsApiCallAction.callerType

    * service.action.awsApiCallAction.remoteIpDetails.city.cityName

    * service.action.awsApiCallAction.remoteIpDetails.country.countryName

    * service.action.awsApiCallAction.remoteIpDetails.ipAddressV4

    * service.action.awsApiCallAction.remoteIpDetails.organization.asn

    * service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg

    * service.action.awsApiCallAction.serviceName

    * service.action.dnsRequestAction.domain

    * service.action.networkConnectionAction.blocked

    * service.action.networkConnectionAction.connectionDirection

    * service.action.networkConnectionAction.localPortDetails.port

    * service.action.networkConnectionAction.protocol

    * service.action.networkConnectionAction.remoteIpDetails.city.cityName

    * service.action.networkConnectionAction.remoteIpDetails.country.countryName

    * service.action.networkConnectionAction.remoteIpDetails.ipAddressV4

    * service.action.networkConnectionAction.remoteIpDetails.organization.asn

    * service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg

    * service.action.networkConnectionAction.remotePortDetails.port

    * service.additionalInfo.threatListName

    * service.archived When this attribute is set to 'true', only archived findings are listed. When
    it's set to 'false', only unarchived findings are listed. When this attribute is not set, all
    existing findings are listed.

    * service.resourceRole

    * severity

    * type

    * updatedAt Type: Timestamp in Unix Epoch millisecond format: 1486685375000

    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when querying
      findings.

      - *(string) --*

        - *(dict) --*

          Contains information about the condition.

          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for findings.

            - *(string) --*

          - **Neq** *(list) --*

            Represents the not equal condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **Gt** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **Gte** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when querying
            for findings.

          - **Lt** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **Lte** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying for
            findings.

          - **Equals** *(list) --*

            Represents an **equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **NotEquals** *(list) --*

            Represents an **not equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **GreaterThan** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **GreaterThanOrEqual** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when querying
            for findings.

          - **LessThan** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **LessThanOrEqual** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying for
            findings.
    """


_ClientListFindingsResponseTypeDef = TypedDict(
    "_ClientListFindingsResponseTypeDef",
    {"FindingIds": List[str], "NextToken": str},
    total=False,
)


class ClientListFindingsResponseTypeDef(_ClientListFindingsResponseTypeDef):
    """
    Type definition for `ClientListFindings` `Response`

    - **FindingIds** *(list) --*

      The IDs of the findings you are listing.

      - *(string) --*

    - **NextToken** *(string) --*

      Pagination parameter to be used on the next list operation to retrieve more items.
    """


_ClientListFindingsSortCriteriaTypeDef = TypedDict(
    "_ClientListFindingsSortCriteriaTypeDef",
    {"AttributeName": str, "OrderBy": str},
    total=False,
)


class ClientListFindingsSortCriteriaTypeDef(_ClientListFindingsSortCriteriaTypeDef):
    """
    Type definition for `ClientListFindings` `SortCriteria`

    Represents the criteria used for sorting findings.

    - **AttributeName** *(string) --*

      Represents the finding attribute (for example, accountId) by which to sort findings.

    - **OrderBy** *(string) --*

      Order by which the sorted findings are to be displayed.
    """


_ClientListInvitationsResponseInvitationsTypeDef = TypedDict(
    "_ClientListInvitationsResponseInvitationsTypeDef",
    {
        "AccountId": str,
        "InvitationId": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
    },
    total=False,
)


class ClientListInvitationsResponseInvitationsTypeDef(
    _ClientListInvitationsResponseInvitationsTypeDef
):
    """
    Type definition for `ClientListInvitationsResponse` `Invitations`

    Contains information about the invitation to become a member account.

    - **AccountId** *(string) --*

      The ID of the account from which the invitations was sent.

    - **InvitationId** *(string) --*

      The ID of the invitation. This value is used to validate the inviter account to the
      member account.

    - **RelationshipStatus** *(string) --*

      The status of the relationship between the inviter and invitee accounts.

    - **InvitedAt** *(string) --*

      Timestamp at which the invitation was sent.
    """


_ClientListInvitationsResponseTypeDef = TypedDict(
    "_ClientListInvitationsResponseTypeDef",
    {
        "Invitations": List[ClientListInvitationsResponseInvitationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListInvitationsResponseTypeDef(_ClientListInvitationsResponseTypeDef):
    """
    Type definition for `ClientListInvitations` `Response`

    - **Invitations** *(list) --*

      A list of invitation descriptions.

      - *(dict) --*

        Contains information about the invitation to become a member account.

        - **AccountId** *(string) --*

          The ID of the account from which the invitations was sent.

        - **InvitationId** *(string) --*

          The ID of the invitation. This value is used to validate the inviter account to the
          member account.

        - **RelationshipStatus** *(string) --*

          The status of the relationship between the inviter and invitee accounts.

        - **InvitedAt** *(string) --*

          Timestamp at which the invitation was sent.

    - **NextToken** *(string) --*

      Pagination parameter to be used on the next list operation to retrieve more items.
    """


_ClientListIpSetsResponseTypeDef = TypedDict(
    "_ClientListIpSetsResponseTypeDef",
    {"IpSetIds": List[str], "NextToken": str},
    total=False,
)


class ClientListIpSetsResponseTypeDef(_ClientListIpSetsResponseTypeDef):
    """
    Type definition for `ClientListIpSets` `Response`

    - **IpSetIds** *(list) --*

      The IDs of the IPSet resources.

      - *(string) --*

    - **NextToken** *(string) --*

      Pagination parameter to be used on the next list operation to retrieve more items.
    """


_ClientListMembersResponseMembersTypeDef = TypedDict(
    "_ClientListMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "DetectorId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
        "UpdatedAt": str,
    },
    total=False,
)


class ClientListMembersResponseMembersTypeDef(_ClientListMembersResponseMembersTypeDef):
    """
    Type definition for `ClientListMembersResponse` `Members`

    Continas information about the member account

    - **AccountId** *(string) --*

      Member account ID.

    - **DetectorId** *(string) --*

      Member account's detector ID.

    - **MasterId** *(string) --*

      Master account ID.

    - **Email** *(string) --*

      Member account's email address.

    - **RelationshipStatus** *(string) --*

      The status of the relationship between the member and the master.

    - **InvitedAt** *(string) --*

      Timestamp at which the invitation was sent

    - **UpdatedAt** *(string) --*

      Member last updated timestamp.
    """


_ClientListMembersResponseTypeDef = TypedDict(
    "_ClientListMembersResponseTypeDef",
    {"Members": List[ClientListMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)


class ClientListMembersResponseTypeDef(_ClientListMembersResponseTypeDef):
    """
    Type definition for `ClientListMembers` `Response`

    - **Members** *(list) --*

      A list of members.

      - *(dict) --*

        Continas information about the member account

        - **AccountId** *(string) --*

          Member account ID.

        - **DetectorId** *(string) --*

          Member account's detector ID.

        - **MasterId** *(string) --*

          Master account ID.

        - **Email** *(string) --*

          Member account's email address.

        - **RelationshipStatus** *(string) --*

          The status of the relationship between the member and the master.

        - **InvitedAt** *(string) --*

          Timestamp at which the invitation was sent

        - **UpdatedAt** *(string) --*

          Member last updated timestamp.

    - **NextToken** *(string) --*

      Pagination parameter to be used on the next list operation to retrieve more items.
    """


_ClientListPublishingDestinationsResponseDestinationsTypeDef = TypedDict(
    "_ClientListPublishingDestinationsResponseDestinationsTypeDef",
    {"DestinationId": str, "DestinationType": str, "Status": str},
    total=False,
)


class ClientListPublishingDestinationsResponseDestinationsTypeDef(
    _ClientListPublishingDestinationsResponseDestinationsTypeDef
):
    """
    Type definition for `ClientListPublishingDestinationsResponse` `Destinations`

    Contains information about a publishing destination, including the ID, type, and status.

    - **DestinationId** *(string) --*

      The unique ID of the publishing destination.

    - **DestinationType** *(string) --*

      The type of resource used for the publishing destination. Currently, only S3 is supported.

    - **Status** *(string) --*

      The status of the publishing destination.
    """


_ClientListPublishingDestinationsResponseTypeDef = TypedDict(
    "_ClientListPublishingDestinationsResponseTypeDef",
    {
        "Destinations": List[
            ClientListPublishingDestinationsResponseDestinationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPublishingDestinationsResponseTypeDef(
    _ClientListPublishingDestinationsResponseTypeDef
):
    """
    Type definition for `ClientListPublishingDestinations` `Response`

    - **Destinations** *(list) --*

      A ``Destinations`` obect that includes information about each publishing destination returned.

      - *(dict) --*

        Contains information about a publishing destination, including the ID, type, and status.

        - **DestinationId** *(string) --*

          The unique ID of the publishing destination.

        - **DestinationType** *(string) --*

          The type of resource used for the publishing destination. Currently, only S3 is supported.

        - **Status** *(string) --*

          The status of the publishing destination.

    - **NextToken** *(string) --*

      A token to use for paginating results returned in the repsonse. Set the value of this
      parameter to null for the first request to a list action. For subsequent calls, use the
      ``NextToken`` value returned from the previous request to continue listing results after the
      first page.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(dict) --*

      The tags associated with the resource.

      - *(string) --*

        - *(string) --*
    """


_ClientListThreatIntelSetsResponseTypeDef = TypedDict(
    "_ClientListThreatIntelSetsResponseTypeDef",
    {"ThreatIntelSetIds": List[str], "NextToken": str},
    total=False,
)


class ClientListThreatIntelSetsResponseTypeDef(
    _ClientListThreatIntelSetsResponseTypeDef
):
    """
    Type definition for `ClientListThreatIntelSets` `Response`

    - **ThreatIntelSetIds** *(list) --*

      The IDs of the ThreatIntelSet resources.

      - *(string) --*

    - **NextToken** *(string) --*

      Pagination parameter to be used on the next list operation to retrieve more items.
    """


_ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef(
    _ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef
):
    """
    Type definition for `ClientStartMonitoringMembersResponse` `UnprocessedAccounts`

    Contains information about the accounts that were not processed.

    - **AccountId** *(string) --*

      AWS Account ID.

    - **Result** *(string) --*

      A reason why the account hasn't been processed.
    """


_ClientStartMonitoringMembersResponseTypeDef = TypedDict(
    "_ClientStartMonitoringMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[
            ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef
        ]
    },
    total=False,
)


class ClientStartMonitoringMembersResponseTypeDef(
    _ClientStartMonitoringMembersResponseTypeDef
):
    """
    Type definition for `ClientStartMonitoringMembers` `Response`

    - **UnprocessedAccounts** *(list) --*

      A list of objects containing the unprocessed account and a result string explaining why it
      was unprocessed.

      - *(dict) --*

        Contains information about the accounts that were not processed.

        - **AccountId** *(string) --*

          AWS Account ID.

        - **Result** *(string) --*

          A reason why the account hasn't been processed.
    """


_ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef(
    _ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef
):
    """
    Type definition for `ClientStopMonitoringMembersResponse` `UnprocessedAccounts`

    Contains information about the accounts that were not processed.

    - **AccountId** *(string) --*

      AWS Account ID.

    - **Result** *(string) --*

      A reason why the account hasn't been processed.
    """


_ClientStopMonitoringMembersResponseTypeDef = TypedDict(
    "_ClientStopMonitoringMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[
            ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef
        ]
    },
    total=False,
)


class ClientStopMonitoringMembersResponseTypeDef(
    _ClientStopMonitoringMembersResponseTypeDef
):
    """
    Type definition for `ClientStopMonitoringMembers` `Response`

    - **UnprocessedAccounts** *(list) --*

      A list of objects containing the unprocessed account and a result string explaining why it
      was unprocessed.

      - *(dict) --*

        Contains information about the accounts that were not processed.

        - **AccountId** *(string) --*

          AWS Account ID.

        - **Result** *(string) --*

          A reason why the account hasn't been processed.
    """


_ClientUpdateFilterFindingCriteriaCriterionTypeDef = TypedDict(
    "_ClientUpdateFilterFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ClientUpdateFilterFindingCriteriaCriterionTypeDef(
    _ClientUpdateFilterFindingCriteriaCriterionTypeDef
):
    """
    Type definition for `ClientUpdateFilterFindingCriteria` `Criterion`

    Contains information about the condition.

    - **Eq** *(list) --*

      Represents the equal condition to be applied to a single field when querying for findings.

      - *(string) --*

    - **Neq** *(list) --*

      Represents the not equal condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **Gt** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **Gte** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when querying
      for findings.

    - **Lt** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **Lte** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying for
      findings.

    - **Equals** *(list) --*

      Represents an **equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **NotEquals** *(list) --*

      Represents an **not equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **GreaterThan** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **GreaterThanOrEqual** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when querying
      for findings.

    - **LessThan** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **LessThanOrEqual** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying for
      findings.
    """


_ClientUpdateFilterFindingCriteriaTypeDef = TypedDict(
    "_ClientUpdateFilterFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientUpdateFilterFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ClientUpdateFilterFindingCriteriaTypeDef(
    _ClientUpdateFilterFindingCriteriaTypeDef
):
    """
    Type definition for `ClientUpdateFilter` `FindingCriteria`

    Represents the criteria to be used in the filter for querying findings.

    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when querying
      findings.

      - *(string) --*

        - *(dict) --*

          Contains information about the condition.

          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for findings.

            - *(string) --*

          - **Neq** *(list) --*

            Represents the not equal condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **Gt** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **Gte** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when querying
            for findings.

          - **Lt** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **Lte** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying for
            findings.

          - **Equals** *(list) --*

            Represents an **equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **NotEquals** *(list) --*

            Represents an **not equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **GreaterThan** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **GreaterThanOrEqual** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when querying
            for findings.

          - **LessThan** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **LessThanOrEqual** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying for
            findings.
    """


_ClientUpdateFilterResponseTypeDef = TypedDict(
    "_ClientUpdateFilterResponseTypeDef", {"Name": str}, total=False
)


class ClientUpdateFilterResponseTypeDef(_ClientUpdateFilterResponseTypeDef):
    """
    Type definition for `ClientUpdateFilter` `Response`

    - **Name** *(string) --*

      The name of the filter.
    """


_ClientUpdatePublishingDestinationDestinationPropertiesTypeDef = TypedDict(
    "_ClientUpdatePublishingDestinationDestinationPropertiesTypeDef",
    {"DestinationArn": str, "KmsKeyArn": str},
    total=False,
)


class ClientUpdatePublishingDestinationDestinationPropertiesTypeDef(
    _ClientUpdatePublishingDestinationDestinationPropertiesTypeDef
):
    """
    Type definition for `ClientUpdatePublishingDestination` `DestinationProperties`

    A ``DestinationProperties`` object that includes the ``DestinationArn`` and ``KmsKeyArn`` of the
    publishing destination.

    - **DestinationArn** *(string) --*

      The ARN of the resource to publish to.

    - **KmsKeyArn** *(string) --*

      The ARN of the KMS key to use for encryption.
    """


_ListDetectorsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDetectorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDetectorsPaginatePaginationConfigTypeDef(
    _ListDetectorsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDetectorsPaginate` `PaginationConfig`

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


_ListDetectorsPaginateResponseTypeDef = TypedDict(
    "_ListDetectorsPaginateResponseTypeDef", {"DetectorIds": List[str]}, total=False
)


class ListDetectorsPaginateResponseTypeDef(_ListDetectorsPaginateResponseTypeDef):
    """
    Type definition for `ListDetectorsPaginate` `Response`

    - **DetectorIds** *(list) --*

      A list of detector Ids.

      - *(string) --*
    """


_ListFiltersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFiltersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFiltersPaginatePaginationConfigTypeDef(
    _ListFiltersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFiltersPaginate` `PaginationConfig`

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


_ListFiltersPaginateResponseTypeDef = TypedDict(
    "_ListFiltersPaginateResponseTypeDef", {"FilterNames": List[str]}, total=False
)


class ListFiltersPaginateResponseTypeDef(_ListFiltersPaginateResponseTypeDef):
    """
    Type definition for `ListFiltersPaginate` `Response`

    - **FilterNames** *(list) --*

      A list of filter names

      - *(string) --*
    """


_ListFindingsPaginateFindingCriteriaCriterionTypeDef = TypedDict(
    "_ListFindingsPaginateFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ListFindingsPaginateFindingCriteriaCriterionTypeDef(
    _ListFindingsPaginateFindingCriteriaCriterionTypeDef
):
    """
    Type definition for `ListFindingsPaginateFindingCriteria` `Criterion`

    Contains information about the condition.

    - **Eq** *(list) --*

      Represents the equal condition to be applied to a single field when querying for findings.

      - *(string) --*

    - **Neq** *(list) --*

      Represents the not equal condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **Gt** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **Gte** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when querying
      for findings.

    - **Lt** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **Lte** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying for
      findings.

    - **Equals** *(list) --*

      Represents an **equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **NotEquals** *(list) --*

      Represents an **not equal** condition to be applied to a single field when querying for
      findings.

      - *(string) --*

    - **GreaterThan** *(integer) --*

      Represents a greater than condition to be applied to a single field when querying for
      findings.

    - **GreaterThanOrEqual** *(integer) --*

      Represents a greater than equal condition to be applied to a single field when querying
      for findings.

    - **LessThan** *(integer) --*

      Represents a less than condition to be applied to a single field when querying for
      findings.

    - **LessThanOrEqual** *(integer) --*

      Represents a less than equal condition to be applied to a single field when querying for
      findings.
    """


_ListFindingsPaginateFindingCriteriaTypeDef = TypedDict(
    "_ListFindingsPaginateFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ListFindingsPaginateFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ListFindingsPaginateFindingCriteriaTypeDef(
    _ListFindingsPaginateFindingCriteriaTypeDef
):
    """
    Type definition for `ListFindingsPaginate` `FindingCriteria`

    Represents the criteria used for querying findings. Valid values include:

    * JSON field name

    * accountId

    * region

    * confidence

    * id

    * resource.accessKeyDetails.accessKeyId

    * resource.accessKeyDetails.principalId

    * resource.accessKeyDetails.userName

    * resource.accessKeyDetails.userType

    * resource.instanceDetails.iamInstanceProfile.id

    * resource.instanceDetails.imageId

    * resource.instanceDetails.instanceId

    * resource.instanceDetails.networkInterfaces.ipv6Addresses

    * resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress

    * resource.instanceDetails.networkInterfaces.publicDnsName

    * resource.instanceDetails.networkInterfaces.publicIp

    * resource.instanceDetails.networkInterfaces.securityGroups.groupId

    * resource.instanceDetails.networkInterfaces.securityGroups.groupName

    * resource.instanceDetails.networkInterfaces.subnetId

    * resource.instanceDetails.networkInterfaces.vpcId

    * resource.instanceDetails.tags.key

    * resource.instanceDetails.tags.value

    * resource.resourceType

    * service.action.actionType

    * service.action.awsApiCallAction.api

    * service.action.awsApiCallAction.callerType

    * service.action.awsApiCallAction.remoteIpDetails.city.cityName

    * service.action.awsApiCallAction.remoteIpDetails.country.countryName

    * service.action.awsApiCallAction.remoteIpDetails.ipAddressV4

    * service.action.awsApiCallAction.remoteIpDetails.organization.asn

    * service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg

    * service.action.awsApiCallAction.serviceName

    * service.action.dnsRequestAction.domain

    * service.action.networkConnectionAction.blocked

    * service.action.networkConnectionAction.connectionDirection

    * service.action.networkConnectionAction.localPortDetails.port

    * service.action.networkConnectionAction.protocol

    * service.action.networkConnectionAction.remoteIpDetails.city.cityName

    * service.action.networkConnectionAction.remoteIpDetails.country.countryName

    * service.action.networkConnectionAction.remoteIpDetails.ipAddressV4

    * service.action.networkConnectionAction.remoteIpDetails.organization.asn

    * service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg

    * service.action.networkConnectionAction.remotePortDetails.port

    * service.additionalInfo.threatListName

    * service.archived When this attribute is set to 'true', only archived findings are listed. When
    it's set to 'false', only unarchived findings are listed. When this attribute is not set, all
    existing findings are listed.

    * service.resourceRole

    * severity

    * type

    * updatedAt Type: Timestamp in Unix Epoch millisecond format: 1486685375000

    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when querying
      findings.

      - *(string) --*

        - *(dict) --*

          Contains information about the condition.

          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for findings.

            - *(string) --*

          - **Neq** *(list) --*

            Represents the not equal condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **Gt** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **Gte** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when querying
            for findings.

          - **Lt** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **Lte** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying for
            findings.

          - **Equals** *(list) --*

            Represents an **equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **NotEquals** *(list) --*

            Represents an **not equal** condition to be applied to a single field when querying for
            findings.

            - *(string) --*

          - **GreaterThan** *(integer) --*

            Represents a greater than condition to be applied to a single field when querying for
            findings.

          - **GreaterThanOrEqual** *(integer) --*

            Represents a greater than equal condition to be applied to a single field when querying
            for findings.

          - **LessThan** *(integer) --*

            Represents a less than condition to be applied to a single field when querying for
            findings.

          - **LessThanOrEqual** *(integer) --*

            Represents a less than equal condition to be applied to a single field when querying for
            findings.
    """


_ListFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFindingsPaginatePaginationConfigTypeDef(
    _ListFindingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFindingsPaginate` `PaginationConfig`

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


_ListFindingsPaginateResponseTypeDef = TypedDict(
    "_ListFindingsPaginateResponseTypeDef", {"FindingIds": List[str]}, total=False
)


class ListFindingsPaginateResponseTypeDef(_ListFindingsPaginateResponseTypeDef):
    """
    Type definition for `ListFindingsPaginate` `Response`

    - **FindingIds** *(list) --*

      The IDs of the findings you are listing.

      - *(string) --*
    """


_ListFindingsPaginateSortCriteriaTypeDef = TypedDict(
    "_ListFindingsPaginateSortCriteriaTypeDef",
    {"AttributeName": str, "OrderBy": str},
    total=False,
)


class ListFindingsPaginateSortCriteriaTypeDef(_ListFindingsPaginateSortCriteriaTypeDef):
    """
    Type definition for `ListFindingsPaginate` `SortCriteria`

    Represents the criteria used for sorting findings.

    - **AttributeName** *(string) --*

      Represents the finding attribute (for example, accountId) by which to sort findings.

    - **OrderBy** *(string) --*

      Order by which the sorted findings are to be displayed.
    """


_ListIPSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIPSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIPSetsPaginatePaginationConfigTypeDef(
    _ListIPSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListIPSetsPaginate` `PaginationConfig`

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


_ListIPSetsPaginateResponseTypeDef = TypedDict(
    "_ListIPSetsPaginateResponseTypeDef", {"IpSetIds": List[str]}, total=False
)


class ListIPSetsPaginateResponseTypeDef(_ListIPSetsPaginateResponseTypeDef):
    """
    Type definition for `ListIPSetsPaginate` `Response`

    - **IpSetIds** *(list) --*

      The IDs of the IPSet resources.

      - *(string) --*
    """


_ListInvitationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInvitationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInvitationsPaginatePaginationConfigTypeDef(
    _ListInvitationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListInvitationsPaginate` `PaginationConfig`

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


_ListInvitationsPaginateResponseInvitationsTypeDef = TypedDict(
    "_ListInvitationsPaginateResponseInvitationsTypeDef",
    {
        "AccountId": str,
        "InvitationId": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
    },
    total=False,
)


class ListInvitationsPaginateResponseInvitationsTypeDef(
    _ListInvitationsPaginateResponseInvitationsTypeDef
):
    """
    Type definition for `ListInvitationsPaginateResponse` `Invitations`

    Contains information about the invitation to become a member account.

    - **AccountId** *(string) --*

      The ID of the account from which the invitations was sent.

    - **InvitationId** *(string) --*

      The ID of the invitation. This value is used to validate the inviter account to the
      member account.

    - **RelationshipStatus** *(string) --*

      The status of the relationship between the inviter and invitee accounts.

    - **InvitedAt** *(string) --*

      Timestamp at which the invitation was sent.
    """


_ListInvitationsPaginateResponseTypeDef = TypedDict(
    "_ListInvitationsPaginateResponseTypeDef",
    {"Invitations": List[ListInvitationsPaginateResponseInvitationsTypeDef]},
    total=False,
)


class ListInvitationsPaginateResponseTypeDef(_ListInvitationsPaginateResponseTypeDef):
    """
    Type definition for `ListInvitationsPaginate` `Response`

    - **Invitations** *(list) --*

      A list of invitation descriptions.

      - *(dict) --*

        Contains information about the invitation to become a member account.

        - **AccountId** *(string) --*

          The ID of the account from which the invitations was sent.

        - **InvitationId** *(string) --*

          The ID of the invitation. This value is used to validate the inviter account to the
          member account.

        - **RelationshipStatus** *(string) --*

          The status of the relationship between the inviter and invitee accounts.

        - **InvitedAt** *(string) --*

          Timestamp at which the invitation was sent.
    """


_ListMembersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMembersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMembersPaginatePaginationConfigTypeDef(
    _ListMembersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListMembersPaginate` `PaginationConfig`

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


_ListMembersPaginateResponseMembersTypeDef = TypedDict(
    "_ListMembersPaginateResponseMembersTypeDef",
    {
        "AccountId": str,
        "DetectorId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
        "UpdatedAt": str,
    },
    total=False,
)


class ListMembersPaginateResponseMembersTypeDef(
    _ListMembersPaginateResponseMembersTypeDef
):
    """
    Type definition for `ListMembersPaginateResponse` `Members`

    Continas information about the member account

    - **AccountId** *(string) --*

      Member account ID.

    - **DetectorId** *(string) --*

      Member account's detector ID.

    - **MasterId** *(string) --*

      Master account ID.

    - **Email** *(string) --*

      Member account's email address.

    - **RelationshipStatus** *(string) --*

      The status of the relationship between the member and the master.

    - **InvitedAt** *(string) --*

      Timestamp at which the invitation was sent

    - **UpdatedAt** *(string) --*

      Member last updated timestamp.
    """


_ListMembersPaginateResponseTypeDef = TypedDict(
    "_ListMembersPaginateResponseTypeDef",
    {"Members": List[ListMembersPaginateResponseMembersTypeDef]},
    total=False,
)


class ListMembersPaginateResponseTypeDef(_ListMembersPaginateResponseTypeDef):
    """
    Type definition for `ListMembersPaginate` `Response`

    - **Members** *(list) --*

      A list of members.

      - *(dict) --*

        Continas information about the member account

        - **AccountId** *(string) --*

          Member account ID.

        - **DetectorId** *(string) --*

          Member account's detector ID.

        - **MasterId** *(string) --*

          Master account ID.

        - **Email** *(string) --*

          Member account's email address.

        - **RelationshipStatus** *(string) --*

          The status of the relationship between the member and the master.

        - **InvitedAt** *(string) --*

          Timestamp at which the invitation was sent

        - **UpdatedAt** *(string) --*

          Member last updated timestamp.
    """


_ListThreatIntelSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThreatIntelSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThreatIntelSetsPaginatePaginationConfigTypeDef(
    _ListThreatIntelSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListThreatIntelSetsPaginate` `PaginationConfig`

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


_ListThreatIntelSetsPaginateResponseTypeDef = TypedDict(
    "_ListThreatIntelSetsPaginateResponseTypeDef",
    {"ThreatIntelSetIds": List[str]},
    total=False,
)


class ListThreatIntelSetsPaginateResponseTypeDef(
    _ListThreatIntelSetsPaginateResponseTypeDef
):
    """
    Type definition for `ListThreatIntelSetsPaginate` `Response`

    - **ThreatIntelSetIds** *(list) --*

      The IDs of the ThreatIntelSet resources.

      - *(string) --*
    """
