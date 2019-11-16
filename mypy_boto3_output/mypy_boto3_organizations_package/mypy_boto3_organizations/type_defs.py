"Main interface for organizations type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAcceptHandshakeResponseHandshakePartiesTypeDef",
    "ClientAcceptHandshakeResponseHandshakeResourcesTypeDef",
    "ClientAcceptHandshakeResponseHandshakeTypeDef",
    "ClientAcceptHandshakeResponseTypeDef",
    "ClientCancelHandshakeResponseHandshakePartiesTypeDef",
    "ClientCancelHandshakeResponseHandshakeResourcesTypeDef",
    "ClientCancelHandshakeResponseHandshakeTypeDef",
    "ClientCancelHandshakeResponseTypeDef",
    "ClientCreateAccountResponseCreateAccountStatusTypeDef",
    "ClientCreateAccountResponseTypeDef",
    "ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef",
    "ClientCreateGovCloudAccountResponseTypeDef",
    "ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    "ClientCreateOrganizationResponseOrganizationTypeDef",
    "ClientCreateOrganizationResponseTypeDef",
    "ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    "ClientCreateOrganizationalUnitResponseTypeDef",
    "ClientCreatePolicyResponsePolicyPolicySummaryTypeDef",
    "ClientCreatePolicyResponsePolicyTypeDef",
    "ClientCreatePolicyResponseTypeDef",
    "ClientDeclineHandshakeResponseHandshakePartiesTypeDef",
    "ClientDeclineHandshakeResponseHandshakeResourcesTypeDef",
    "ClientDeclineHandshakeResponseHandshakeTypeDef",
    "ClientDeclineHandshakeResponseTypeDef",
    "ClientDescribeAccountResponseAccountTypeDef",
    "ClientDescribeAccountResponseTypeDef",
    "ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef",
    "ClientDescribeCreateAccountStatusResponseTypeDef",
    "ClientDescribeHandshakeResponseHandshakePartiesTypeDef",
    "ClientDescribeHandshakeResponseHandshakeResourcesTypeDef",
    "ClientDescribeHandshakeResponseHandshakeTypeDef",
    "ClientDescribeHandshakeResponseTypeDef",
    "ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    "ClientDescribeOrganizationResponseOrganizationTypeDef",
    "ClientDescribeOrganizationResponseTypeDef",
    "ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef",
    "ClientDescribeOrganizationalUnitResponseTypeDef",
    "ClientDescribePolicyResponsePolicyPolicySummaryTypeDef",
    "ClientDescribePolicyResponsePolicyTypeDef",
    "ClientDescribePolicyResponseTypeDef",
    "ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef",
    "ClientDisablePolicyTypeResponseRootTypeDef",
    "ClientDisablePolicyTypeResponseTypeDef",
    "ClientEnableAllFeaturesResponseHandshakePartiesTypeDef",
    "ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef",
    "ClientEnableAllFeaturesResponseHandshakeTypeDef",
    "ClientEnableAllFeaturesResponseTypeDef",
    "ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef",
    "ClientEnablePolicyTypeResponseRootTypeDef",
    "ClientEnablePolicyTypeResponseTypeDef",
    "ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef",
    "ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef",
    "ClientInviteAccountToOrganizationResponseHandshakeTypeDef",
    "ClientInviteAccountToOrganizationResponseTypeDef",
    "ClientInviteAccountToOrganizationTargetTypeDef",
    "ClientListAccountsForParentResponseAccountsTypeDef",
    "ClientListAccountsForParentResponseTypeDef",
    "ClientListAccountsResponseAccountsTypeDef",
    "ClientListAccountsResponseTypeDef",
    "ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef",
    "ClientListAwsServiceAccessForOrganizationResponseTypeDef",
    "ClientListChildrenResponseChildrenTypeDef",
    "ClientListChildrenResponseTypeDef",
    "ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef",
    "ClientListCreateAccountStatusResponseTypeDef",
    "ClientListHandshakesForAccountFilterTypeDef",
    "ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef",
    "ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef",
    "ClientListHandshakesForAccountResponseHandshakesTypeDef",
    "ClientListHandshakesForAccountResponseTypeDef",
    "ClientListHandshakesForOrganizationFilterTypeDef",
    "ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef",
    "ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef",
    "ClientListHandshakesForOrganizationResponseHandshakesTypeDef",
    "ClientListHandshakesForOrganizationResponseTypeDef",
    "ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef",
    "ClientListOrganizationalUnitsForParentResponseTypeDef",
    "ClientListParentsResponseParentsTypeDef",
    "ClientListParentsResponseTypeDef",
    "ClientListPoliciesForTargetResponsePoliciesTypeDef",
    "ClientListPoliciesForTargetResponseTypeDef",
    "ClientListPoliciesResponsePoliciesTypeDef",
    "ClientListPoliciesResponseTypeDef",
    "ClientListRootsResponseRootsPolicyTypesTypeDef",
    "ClientListRootsResponseRootsTypeDef",
    "ClientListRootsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTargetsForPolicyResponseTargetsTypeDef",
    "ClientListTargetsForPolicyResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    "ClientUpdateOrganizationalUnitResponseTypeDef",
    "ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef",
    "ClientUpdatePolicyResponsePolicyTypeDef",
    "ClientUpdatePolicyResponseTypeDef",
    "ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef",
    "ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef",
    "ListAWSServiceAccessForOrganizationPaginateResponseTypeDef",
    "ListAccountsForParentPaginatePaginationConfigTypeDef",
    "ListAccountsForParentPaginateResponseAccountsTypeDef",
    "ListAccountsForParentPaginateResponseTypeDef",
    "ListAccountsPaginatePaginationConfigTypeDef",
    "ListAccountsPaginateResponseAccountsTypeDef",
    "ListAccountsPaginateResponseTypeDef",
    "ListChildrenPaginatePaginationConfigTypeDef",
    "ListChildrenPaginateResponseChildrenTypeDef",
    "ListChildrenPaginateResponseTypeDef",
    "ListCreateAccountStatusPaginatePaginationConfigTypeDef",
    "ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef",
    "ListCreateAccountStatusPaginateResponseTypeDef",
    "ListHandshakesForAccountPaginateFilterTypeDef",
    "ListHandshakesForAccountPaginatePaginationConfigTypeDef",
    "ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef",
    "ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef",
    "ListHandshakesForAccountPaginateResponseHandshakesTypeDef",
    "ListHandshakesForAccountPaginateResponseTypeDef",
    "ListHandshakesForOrganizationPaginateFilterTypeDef",
    "ListHandshakesForOrganizationPaginatePaginationConfigTypeDef",
    "ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef",
    "ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef",
    "ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef",
    "ListHandshakesForOrganizationPaginateResponseTypeDef",
    "ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef",
    "ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef",
    "ListOrganizationalUnitsForParentPaginateResponseTypeDef",
    "ListParentsPaginatePaginationConfigTypeDef",
    "ListParentsPaginateResponseParentsTypeDef",
    "ListParentsPaginateResponseTypeDef",
    "ListPoliciesForTargetPaginatePaginationConfigTypeDef",
    "ListPoliciesForTargetPaginateResponsePoliciesTypeDef",
    "ListPoliciesForTargetPaginateResponseTypeDef",
    "ListPoliciesPaginatePaginationConfigTypeDef",
    "ListPoliciesPaginateResponsePoliciesTypeDef",
    "ListPoliciesPaginateResponseTypeDef",
    "ListRootsPaginatePaginationConfigTypeDef",
    "ListRootsPaginateResponseRootsPolicyTypesTypeDef",
    "ListRootsPaginateResponseRootsTypeDef",
    "ListRootsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListTargetsForPolicyPaginatePaginationConfigTypeDef",
    "ListTargetsForPolicyPaginateResponseTargetsTypeDef",
    "ListTargetsForPolicyPaginateResponseTypeDef",
)


_ClientAcceptHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientAcceptHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ClientAcceptHandshakeResponseHandshakePartiesTypeDef(
    _ClientAcceptHandshakeResponseHandshakePartiesTypeDef
):
    """
    Type definition for `ClientAcceptHandshakeResponseHandshake` `Parties`

    Identifies a participant in a handshake.

    - **Id** *(string) --*

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
      requires "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --*

      The type of party.
    """


_ClientAcceptHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientAcceptHandshakeResponseHandshakeResourcesTypeDef",
    {"Value": str, "Type": str, "Resources": List[Any]},
    total=False,
)


class ClientAcceptHandshakeResponseHandshakeResourcesTypeDef(
    _ClientAcceptHandshakeResponseHandshakeResourcesTypeDef
):
    """
    Type definition for `ClientAcceptHandshakeResponseHandshake` `Resources`

    Contains additional data that is needed to process a handshake.

    - **Value** *(string) --*

      The information that is passed to the other party in the handshake. The format of the
      value string must match the requirements of the specified type.

    - **Type** *(string) --*

      The type of information being passed, specifying how the value is to be interpreted by
      the other party:

      * ``ACCOUNT`` - Specifies an AWS account ID number.

      * ``ORGANIZATION`` - Specifies an organization ID number.

      * ``EMAIL`` - Specifies the email address that is associated with the account that
      receives the handshake.

      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
      Included as information about an organization.

      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
      information about an organization.

      * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
      recipient to read.

    - **Resources** *(list) --*

      When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientAcceptHandshakeResponseHandshakeTypeDef = TypedDict(
    "_ClientAcceptHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientAcceptHandshakeResponseHandshakePartiesTypeDef],
        "State": str,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": str,
        "Resources": List[ClientAcceptHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientAcceptHandshakeResponseHandshakeTypeDef(
    _ClientAcceptHandshakeResponseHandshakeTypeDef
):
    """
    Type definition for `ClientAcceptHandshakeResponse` `Handshake`

    A structure that contains details about the accepted handshake.

    - **Id** *(string) --*

      The unique identifier (ID) of a handshake. The originating account creates the ID when it
      initiates the handshake.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
      "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of a handshake.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Parties** *(list) --*

      Information about the two accounts that are participating in the handshake.

      - *(dict) --*

        Identifies a participant in a handshake.

        - **Id** *(string) --*

          The unique identifier (ID) for the party.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
          requires "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Type** *(string) --*

          The type of party.

    - **State** *(string) --*

      The current state of the handshake. Use the state to trace the flow of the handshake
      through the process from its creation to its acceptance. The meaning of each of the valid
      values is as follows:

      * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
      handshake types) and not all recipients have responded yet. The request stays in this state
      until all recipients respond.

      * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
      types) and all recipients have responded, allowing the originator to complete the handshake
      action.

      * **CANCELED** : This handshake is no longer active because it was canceled by the
      originating account.

      * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

      * **DECLINED** : This handshake is no longer active because it was declined by the
      recipient account.

      * **EXPIRED** : This handshake is no longer active because the originator did not receive a
      response of any kind from the recipient before the expiration time (15 days).

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the handshake request was made.

    - **ExpirationTimestamp** *(datetime) --*

      The date and time that the handshake expires. If the recipient of the handshake request
      fails to respond before the specified date and time, the handshake becomes inactive and is
      no longer valid.

    - **Action** *(string) --*

      The type of handshake, indicating what action occurs when the recipient accepts the
      handshake. The following handshake types are supported:

      * **INVITE** : This type of handshake represents a request to join an organization. It is
      always sent from the master account to only non-member accounts.

      * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
      features in an organization. It is always sent from the master account to only *invited*
      member accounts. Created accounts do not receive this because those accounts were created
      by the organization's master account and approval is inferred.

      * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
      when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
      only to the master account and signals the master that it can finalize the process to
      enable all features.

    - **Resources** *(list) --*

      Additional information that is needed to process the handshake.

      - *(dict) --*

        Contains additional data that is needed to process a handshake.

        - **Value** *(string) --*

          The information that is passed to the other party in the handshake. The format of the
          value string must match the requirements of the specified type.

        - **Type** *(string) --*

          The type of information being passed, specifying how the value is to be interpreted by
          the other party:

          * ``ACCOUNT`` - Specifies an AWS account ID number.

          * ``ORGANIZATION`` - Specifies an organization ID number.

          * ``EMAIL`` - Specifies the email address that is associated with the account that
          receives the handshake.

          * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
          Included as information about an organization.

          * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
          information about an organization.

          * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
          recipient to read.

        - **Resources** *(list) --*

          When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientAcceptHandshakeResponseTypeDef = TypedDict(
    "_ClientAcceptHandshakeResponseTypeDef",
    {"Handshake": ClientAcceptHandshakeResponseHandshakeTypeDef},
    total=False,
)


class ClientAcceptHandshakeResponseTypeDef(_ClientAcceptHandshakeResponseTypeDef):
    """
    Type definition for `ClientAcceptHandshake` `Response`

    - **Handshake** *(dict) --*

      A structure that contains details about the accepted handshake.

      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of a handshake.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Parties** *(list) --*

        Information about the two accounts that are participating in the handshake.

        - *(dict) --*

          Identifies a participant in a handshake.

          - **Id** *(string) --*

            The unique identifier (ID) for the party.

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
            requires "h-" followed by from 8 to 32 lower-case letters or digits.

          - **Type** *(string) --*

            The type of party.

      - **State** *(string) --*

        The current state of the handshake. Use the state to trace the flow of the handshake
        through the process from its creation to its acceptance. The meaning of each of the valid
        values is as follows:

        * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
        handshake types) and not all recipients have responded yet. The request stays in this state
        until all recipients respond.

        * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
        types) and all recipients have responded, allowing the originator to complete the handshake
        action.

        * **CANCELED** : This handshake is no longer active because it was canceled by the
        originating account.

        * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

        * **DECLINED** : This handshake is no longer active because it was declined by the
        recipient account.

        * **EXPIRED** : This handshake is no longer active because the originator did not receive a
        response of any kind from the recipient before the expiration time (15 days).

      - **RequestedTimestamp** *(datetime) --*

        The date and time that the handshake request was made.

      - **ExpirationTimestamp** *(datetime) --*

        The date and time that the handshake expires. If the recipient of the handshake request
        fails to respond before the specified date and time, the handshake becomes inactive and is
        no longer valid.

      - **Action** *(string) --*

        The type of handshake, indicating what action occurs when the recipient accepts the
        handshake. The following handshake types are supported:

        * **INVITE** : This type of handshake represents a request to join an organization. It is
        always sent from the master account to only non-member accounts.

        * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
        features in an organization. It is always sent from the master account to only *invited*
        member accounts. Created accounts do not receive this because those accounts were created
        by the organization's master account and approval is inferred.

        * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
        when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
        only to the master account and signals the master that it can finalize the process to
        enable all features.

      - **Resources** *(list) --*

        Additional information that is needed to process the handshake.

        - *(dict) --*

          Contains additional data that is needed to process a handshake.

          - **Value** *(string) --*

            The information that is passed to the other party in the handshake. The format of the
            value string must match the requirements of the specified type.

          - **Type** *(string) --*

            The type of information being passed, specifying how the value is to be interpreted by
            the other party:

            * ``ACCOUNT`` - Specifies an AWS account ID number.

            * ``ORGANIZATION`` - Specifies an organization ID number.

            * ``EMAIL`` - Specifies the email address that is associated with the account that
            receives the handshake.

            * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
            Included as information about an organization.

            * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
            information about an organization.

            * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
            recipient to read.

          - **Resources** *(list) --*

            When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientCancelHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientCancelHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ClientCancelHandshakeResponseHandshakePartiesTypeDef(
    _ClientCancelHandshakeResponseHandshakePartiesTypeDef
):
    """
    Type definition for `ClientCancelHandshakeResponseHandshake` `Parties`

    Identifies a participant in a handshake.

    - **Id** *(string) --*

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
      requires "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --*

      The type of party.
    """


_ClientCancelHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientCancelHandshakeResponseHandshakeResourcesTypeDef",
    {"Value": str, "Type": str, "Resources": List[Any]},
    total=False,
)


class ClientCancelHandshakeResponseHandshakeResourcesTypeDef(
    _ClientCancelHandshakeResponseHandshakeResourcesTypeDef
):
    """
    Type definition for `ClientCancelHandshakeResponseHandshake` `Resources`

    Contains additional data that is needed to process a handshake.

    - **Value** *(string) --*

      The information that is passed to the other party in the handshake. The format of the
      value string must match the requirements of the specified type.

    - **Type** *(string) --*

      The type of information being passed, specifying how the value is to be interpreted by
      the other party:

      * ``ACCOUNT`` - Specifies an AWS account ID number.

      * ``ORGANIZATION`` - Specifies an organization ID number.

      * ``EMAIL`` - Specifies the email address that is associated with the account that
      receives the handshake.

      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
      Included as information about an organization.

      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
      information about an organization.

      * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
      recipient to read.

    - **Resources** *(list) --*

      When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientCancelHandshakeResponseHandshakeTypeDef = TypedDict(
    "_ClientCancelHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientCancelHandshakeResponseHandshakePartiesTypeDef],
        "State": str,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": str,
        "Resources": List[ClientCancelHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientCancelHandshakeResponseHandshakeTypeDef(
    _ClientCancelHandshakeResponseHandshakeTypeDef
):
    """
    Type definition for `ClientCancelHandshakeResponse` `Handshake`

    A structure that contains details about the handshake that you canceled.

    - **Id** *(string) --*

      The unique identifier (ID) of a handshake. The originating account creates the ID when it
      initiates the handshake.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
      "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of a handshake.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Parties** *(list) --*

      Information about the two accounts that are participating in the handshake.

      - *(dict) --*

        Identifies a participant in a handshake.

        - **Id** *(string) --*

          The unique identifier (ID) for the party.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
          requires "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Type** *(string) --*

          The type of party.

    - **State** *(string) --*

      The current state of the handshake. Use the state to trace the flow of the handshake
      through the process from its creation to its acceptance. The meaning of each of the valid
      values is as follows:

      * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
      handshake types) and not all recipients have responded yet. The request stays in this state
      until all recipients respond.

      * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
      types) and all recipients have responded, allowing the originator to complete the handshake
      action.

      * **CANCELED** : This handshake is no longer active because it was canceled by the
      originating account.

      * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

      * **DECLINED** : This handshake is no longer active because it was declined by the
      recipient account.

      * **EXPIRED** : This handshake is no longer active because the originator did not receive a
      response of any kind from the recipient before the expiration time (15 days).

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the handshake request was made.

    - **ExpirationTimestamp** *(datetime) --*

      The date and time that the handshake expires. If the recipient of the handshake request
      fails to respond before the specified date and time, the handshake becomes inactive and is
      no longer valid.

    - **Action** *(string) --*

      The type of handshake, indicating what action occurs when the recipient accepts the
      handshake. The following handshake types are supported:

      * **INVITE** : This type of handshake represents a request to join an organization. It is
      always sent from the master account to only non-member accounts.

      * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
      features in an organization. It is always sent from the master account to only *invited*
      member accounts. Created accounts do not receive this because those accounts were created
      by the organization's master account and approval is inferred.

      * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
      when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
      only to the master account and signals the master that it can finalize the process to
      enable all features.

    - **Resources** *(list) --*

      Additional information that is needed to process the handshake.

      - *(dict) --*

        Contains additional data that is needed to process a handshake.

        - **Value** *(string) --*

          The information that is passed to the other party in the handshake. The format of the
          value string must match the requirements of the specified type.

        - **Type** *(string) --*

          The type of information being passed, specifying how the value is to be interpreted by
          the other party:

          * ``ACCOUNT`` - Specifies an AWS account ID number.

          * ``ORGANIZATION`` - Specifies an organization ID number.

          * ``EMAIL`` - Specifies the email address that is associated with the account that
          receives the handshake.

          * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
          Included as information about an organization.

          * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
          information about an organization.

          * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
          recipient to read.

        - **Resources** *(list) --*

          When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientCancelHandshakeResponseTypeDef = TypedDict(
    "_ClientCancelHandshakeResponseTypeDef",
    {"Handshake": ClientCancelHandshakeResponseHandshakeTypeDef},
    total=False,
)


class ClientCancelHandshakeResponseTypeDef(_ClientCancelHandshakeResponseTypeDef):
    """
    Type definition for `ClientCancelHandshake` `Response`

    - **Handshake** *(dict) --*

      A structure that contains details about the handshake that you canceled.

      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of a handshake.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Parties** *(list) --*

        Information about the two accounts that are participating in the handshake.

        - *(dict) --*

          Identifies a participant in a handshake.

          - **Id** *(string) --*

            The unique identifier (ID) for the party.

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
            requires "h-" followed by from 8 to 32 lower-case letters or digits.

          - **Type** *(string) --*

            The type of party.

      - **State** *(string) --*

        The current state of the handshake. Use the state to trace the flow of the handshake
        through the process from its creation to its acceptance. The meaning of each of the valid
        values is as follows:

        * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
        handshake types) and not all recipients have responded yet. The request stays in this state
        until all recipients respond.

        * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
        types) and all recipients have responded, allowing the originator to complete the handshake
        action.

        * **CANCELED** : This handshake is no longer active because it was canceled by the
        originating account.

        * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

        * **DECLINED** : This handshake is no longer active because it was declined by the
        recipient account.

        * **EXPIRED** : This handshake is no longer active because the originator did not receive a
        response of any kind from the recipient before the expiration time (15 days).

      - **RequestedTimestamp** *(datetime) --*

        The date and time that the handshake request was made.

      - **ExpirationTimestamp** *(datetime) --*

        The date and time that the handshake expires. If the recipient of the handshake request
        fails to respond before the specified date and time, the handshake becomes inactive and is
        no longer valid.

      - **Action** *(string) --*

        The type of handshake, indicating what action occurs when the recipient accepts the
        handshake. The following handshake types are supported:

        * **INVITE** : This type of handshake represents a request to join an organization. It is
        always sent from the master account to only non-member accounts.

        * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
        features in an organization. It is always sent from the master account to only *invited*
        member accounts. Created accounts do not receive this because those accounts were created
        by the organization's master account and approval is inferred.

        * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
        when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
        only to the master account and signals the master that it can finalize the process to
        enable all features.

      - **Resources** *(list) --*

        Additional information that is needed to process the handshake.

        - *(dict) --*

          Contains additional data that is needed to process a handshake.

          - **Value** *(string) --*

            The information that is passed to the other party in the handshake. The format of the
            value string must match the requirements of the specified type.

          - **Type** *(string) --*

            The type of information being passed, specifying how the value is to be interpreted by
            the other party:

            * ``ACCOUNT`` - Specifies an AWS account ID number.

            * ``ORGANIZATION`` - Specifies an organization ID number.

            * ``EMAIL`` - Specifies the email address that is associated with the account that
            receives the handshake.

            * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
            Included as information about an organization.

            * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
            information about an organization.

            * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
            recipient to read.

          - **Resources** *(list) --*

            When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientCreateAccountResponseCreateAccountStatusTypeDef = TypedDict(
    "_ClientCreateAccountResponseCreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": str,
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": str,
    },
    total=False,
)


class ClientCreateAccountResponseCreateAccountStatusTypeDef(
    _ClientCreateAccountResponseCreateAccountStatusTypeDef
):
    """
    Type definition for `ClientCreateAccountResponse` `CreateAccountStatus`

    A structure that contains details about the request to create an account. This response
    structure might not be fully populated when you first receive it because account creation is
    an asynchronous process. You can pass the returned ``CreateAccountStatus`` ID as a parameter
    to  DescribeCreateAccountStatus to get status about the progress of the request at later
    times. You can also check the AWS CloudTrail log for the ``CreateAccountResult`` event. For
    more information, see `Monitoring the Activity in Your Organization
    <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_monitoring.html>`__ in the
    *AWS Organizations User Guide* .

    - **Id** *(string) --*

      The unique identifier (ID) that references this request. You get this value from the
      response of the initial  CreateAccount request to create the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID
      string requires "car-" followed by from 8 to 32 lower-case letters or digits.

    - **AccountName** *(string) --*

      The account name given to the account when it was created.

    - **State** *(string) --*

      The status of the request.

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the request was made for the account creation.

    - **CompletedTimestamp** *(datetime) --*

      The date and time that the account was created and the request completed.

    - **AccountId** *(string) --*

      If the account was created successfully, the unique identifier (ID) of the new account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **GovCloudAccountId** *(string) --*

      If the account was created successfully, the unique identifier (ID) of the new account in
      the AWS GovCloud (US) Region.

    - **FailureReason** *(string) --*

      If the request failed, a description of the reason for the failure.

      * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the
      limit on the number of accounts in your organization.

      * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with
      that email address already exists.

      * GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be
      created because this Region already includes an account with that email address.

      * INVALID_ADDRESS: The account could not be created because the address you provided is not
      valid.

      * INVALID_EMAIL: The account could not be created because the email address you provided is
      not valid.

      * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try
      again later. If the problem persists, contact Customer Support.
    """


_ClientCreateAccountResponseTypeDef = TypedDict(
    "_ClientCreateAccountResponseTypeDef",
    {"CreateAccountStatus": ClientCreateAccountResponseCreateAccountStatusTypeDef},
    total=False,
)


class ClientCreateAccountResponseTypeDef(_ClientCreateAccountResponseTypeDef):
    """
    Type definition for `ClientCreateAccount` `Response`

    - **CreateAccountStatus** *(dict) --*

      A structure that contains details about the request to create an account. This response
      structure might not be fully populated when you first receive it because account creation is
      an asynchronous process. You can pass the returned ``CreateAccountStatus`` ID as a parameter
      to  DescribeCreateAccountStatus to get status about the progress of the request at later
      times. You can also check the AWS CloudTrail log for the ``CreateAccountResult`` event. For
      more information, see `Monitoring the Activity in Your Organization
      <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_monitoring.html>`__ in the
      *AWS Organizations User Guide* .

      - **Id** *(string) --*

        The unique identifier (ID) that references this request. You get this value from the
        response of the initial  CreateAccount request to create the account.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID
        string requires "car-" followed by from 8 to 32 lower-case letters or digits.

      - **AccountName** *(string) --*

        The account name given to the account when it was created.

      - **State** *(string) --*

        The status of the request.

      - **RequestedTimestamp** *(datetime) --*

        The date and time that the request was made for the account creation.

      - **CompletedTimestamp** *(datetime) --*

        The date and time that the account was created and the request completed.

      - **AccountId** *(string) --*

        If the account was created successfully, the unique identifier (ID) of the new account.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.

      - **GovCloudAccountId** *(string) --*

        If the account was created successfully, the unique identifier (ID) of the new account in
        the AWS GovCloud (US) Region.

      - **FailureReason** *(string) --*

        If the request failed, a description of the reason for the failure.

        * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the
        limit on the number of accounts in your organization.

        * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with
        that email address already exists.

        * GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be
        created because this Region already includes an account with that email address.

        * INVALID_ADDRESS: The account could not be created because the address you provided is not
        valid.

        * INVALID_EMAIL: The account could not be created because the email address you provided is
        not valid.

        * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try
        again later. If the problem persists, contact Customer Support.
    """


_ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef = TypedDict(
    "_ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": str,
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": str,
    },
    total=False,
)


class ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef(
    _ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef
):
    """
    Type definition for `ClientCreateGovCloudAccountResponse` `CreateAccountStatus`

    Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an AWS
    account or an AWS GovCloud (US) account in an organization.

    - **Id** *(string) --*

      The unique identifier (ID) that references this request. You get this value from the
      response of the initial  CreateAccount request to create the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID
      string requires "car-" followed by from 8 to 32 lower-case letters or digits.

    - **AccountName** *(string) --*

      The account name given to the account when it was created.

    - **State** *(string) --*

      The status of the request.

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the request was made for the account creation.

    - **CompletedTimestamp** *(datetime) --*

      The date and time that the account was created and the request completed.

    - **AccountId** *(string) --*

      If the account was created successfully, the unique identifier (ID) of the new account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **GovCloudAccountId** *(string) --*

      If the account was created successfully, the unique identifier (ID) of the new account in
      the AWS GovCloud (US) Region.

    - **FailureReason** *(string) --*

      If the request failed, a description of the reason for the failure.

      * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the
      limit on the number of accounts in your organization.

      * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with
      that email address already exists.

      * GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be
      created because this Region already includes an account with that email address.

      * INVALID_ADDRESS: The account could not be created because the address you provided is not
      valid.

      * INVALID_EMAIL: The account could not be created because the email address you provided is
      not valid.

      * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try
      again later. If the problem persists, contact Customer Support.
    """


_ClientCreateGovCloudAccountResponseTypeDef = TypedDict(
    "_ClientCreateGovCloudAccountResponseTypeDef",
    {
        "CreateAccountStatus": ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef
    },
    total=False,
)


class ClientCreateGovCloudAccountResponseTypeDef(
    _ClientCreateGovCloudAccountResponseTypeDef
):
    """
    Type definition for `ClientCreateGovCloudAccount` `Response`

    - **CreateAccountStatus** *(dict) --*

      Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an AWS
      account or an AWS GovCloud (US) account in an organization.

      - **Id** *(string) --*

        The unique identifier (ID) that references this request. You get this value from the
        response of the initial  CreateAccount request to create the account.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID
        string requires "car-" followed by from 8 to 32 lower-case letters or digits.

      - **AccountName** *(string) --*

        The account name given to the account when it was created.

      - **State** *(string) --*

        The status of the request.

      - **RequestedTimestamp** *(datetime) --*

        The date and time that the request was made for the account creation.

      - **CompletedTimestamp** *(datetime) --*

        The date and time that the account was created and the request completed.

      - **AccountId** *(string) --*

        If the account was created successfully, the unique identifier (ID) of the new account.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.

      - **GovCloudAccountId** *(string) --*

        If the account was created successfully, the unique identifier (ID) of the new account in
        the AWS GovCloud (US) Region.

      - **FailureReason** *(string) --*

        If the request failed, a description of the reason for the failure.

        * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the
        limit on the number of accounts in your organization.

        * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with
        that email address already exists.

        * GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be
        created because this Region already includes an account with that email address.

        * INVALID_ADDRESS: The account could not be created because the address you provided is not
        valid.

        * INVALID_EMAIL: The account could not be created because the email address you provided is
        not valid.

        * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try
        again later. If the problem persists, contact Customer Support.
    """


_ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef = TypedDict(
    "_ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    {"Type": str, "Status": str},
    total=False,
)


class ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef(
    _ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef
):
    """
    Type definition for `ClientCreateOrganizationResponseOrganization` `AvailablePolicyTypes`

    Contains information about a policy type and its status in the associated root.

    - **Type** *(string) --*

      The name of the policy type.

    - **Status** *(string) --*

      The status of the policy type as it relates to the associated root. To attach a policy
      of the specified type to a root or to an OU or account in that root, it must be
      available in the organization and enabled for that root.
    """


_ClientCreateOrganizationResponseOrganizationTypeDef = TypedDict(
    "_ClientCreateOrganizationResponseOrganizationTypeDef",
    {
        "Id": str,
        "Arn": str,
        "FeatureSet": str,
        "MasterAccountArn": str,
        "MasterAccountId": str,
        "MasterAccountEmail": str,
        "AvailablePolicyTypes": List[
            ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef
        ],
    },
    total=False,
)


class ClientCreateOrganizationResponseOrganizationTypeDef(
    _ClientCreateOrganizationResponseOrganizationTypeDef
):
    """
    Type definition for `ClientCreateOrganizationResponse` `Organization`

    A structure that contains details about the newly created organization.

    - **Id** *(string) --*

      The unique identifier (ID) of an organization.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organization ID string
      requires "o-" followed by from 10 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of an organization.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **FeatureSet** *(string) --*

      Specifies the functionality that currently is available to the organization. If set to
      "ALL", then all features are enabled and policies can be applied to accounts in the
      organization. If set to "CONSOLIDATED_BILLING", then only consolidated billing
      functionality is available. For more information, see `Enabling All Features in Your
      Organization
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html>`__
      in the *AWS Organizations User Guide* .

    - **MasterAccountArn** *(string) --*

      The Amazon Resource Name (ARN) of the account that is designated as the master account for
      the organization.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **MasterAccountId** *(string) --*

      The unique identifier (ID) of the master account of an organization.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **MasterAccountEmail** *(string) --*

      The email address that is associated with the AWS account that is designated as the master
      account for the organization.

    - **AvailablePolicyTypes** *(list) --*

      A list of policy types that are enabled for this organization. For example, if your
      organization has all features enabled, then service control policies (SCPs) are included in
      the list.

      .. note::

        Even if a policy type is shown as available in the organization, you can separately
        enable and disable them at the root level by using  EnablePolicyType and
        DisablePolicyType . Use  ListRoots to see the status of a policy type in that root.

      - *(dict) --*

        Contains information about a policy type and its status in the associated root.

        - **Type** *(string) --*

          The name of the policy type.

        - **Status** *(string) --*

          The status of the policy type as it relates to the associated root. To attach a policy
          of the specified type to a root or to an OU or account in that root, it must be
          available in the organization and enabled for that root.
    """


_ClientCreateOrganizationResponseTypeDef = TypedDict(
    "_ClientCreateOrganizationResponseTypeDef",
    {"Organization": ClientCreateOrganizationResponseOrganizationTypeDef},
    total=False,
)


class ClientCreateOrganizationResponseTypeDef(_ClientCreateOrganizationResponseTypeDef):
    """
    Type definition for `ClientCreateOrganization` `Response`

    - **Organization** *(dict) --*

      A structure that contains details about the newly created organization.

      - **Id** *(string) --*

        The unique identifier (ID) of an organization.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organization ID string
        requires "o-" followed by from 10 to 32 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of an organization.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **FeatureSet** *(string) --*

        Specifies the functionality that currently is available to the organization. If set to
        "ALL", then all features are enabled and policies can be applied to accounts in the
        organization. If set to "CONSOLIDATED_BILLING", then only consolidated billing
        functionality is available. For more information, see `Enabling All Features in Your
        Organization
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html>`__
        in the *AWS Organizations User Guide* .

      - **MasterAccountArn** *(string) --*

        The Amazon Resource Name (ARN) of the account that is designated as the master account for
        the organization.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **MasterAccountId** *(string) --*

        The unique identifier (ID) of the master account of an organization.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.

      - **MasterAccountEmail** *(string) --*

        The email address that is associated with the AWS account that is designated as the master
        account for the organization.

      - **AvailablePolicyTypes** *(list) --*

        A list of policy types that are enabled for this organization. For example, if your
        organization has all features enabled, then service control policies (SCPs) are included in
        the list.

        .. note::

          Even if a policy type is shown as available in the organization, you can separately
          enable and disable them at the root level by using  EnablePolicyType and
          DisablePolicyType . Use  ListRoots to see the status of a policy type in that root.

        - *(dict) --*

          Contains information about a policy type and its status in the associated root.

          - **Type** *(string) --*

            The name of the policy type.

          - **Status** *(string) --*

            The status of the policy type as it relates to the associated root. To attach a policy
            of the specified type to a root or to an OU or account in that root, it must be
            available in the organization and enabled for that root.
    """


_ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef = TypedDict(
    "_ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef(
    _ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef
):
    """
    Type definition for `ClientCreateOrganizationalUnitResponse` `OrganizationalUnit`

    A structure that contains details about the newly created OU.

    - **Id** *(string) --*

      The unique identifier (ID) associated with this OU.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
      string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the
      root that contains the OU) followed by a second "-" dash and from 8 to 32 additional
      lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of this OU.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of this OU.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.
    """


_ClientCreateOrganizationalUnitResponseTypeDef = TypedDict(
    "_ClientCreateOrganizationalUnitResponseTypeDef",
    {
        "OrganizationalUnit": ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef
    },
    total=False,
)


class ClientCreateOrganizationalUnitResponseTypeDef(
    _ClientCreateOrganizationalUnitResponseTypeDef
):
    """
    Type definition for `ClientCreateOrganizationalUnit` `Response`

    - **OrganizationalUnit** *(dict) --*

      A structure that contains details about the newly created OU.

      - **Id** *(string) --*

        The unique identifier (ID) associated with this OU.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
        string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the
        root that contains the OU) followed by a second "-" dash and from 8 to 32 additional
        lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of this OU.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Name** *(string) --*

        The friendly name of this OU.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
        parameter is a string of any of the characters in the ASCII character range.
    """


_ClientCreatePolicyResponsePolicyPolicySummaryTypeDef = TypedDict(
    "_ClientCreatePolicyResponsePolicyPolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "AwsManaged": bool,
    },
    total=False,
)


class ClientCreatePolicyResponsePolicyPolicySummaryTypeDef(
    _ClientCreatePolicyResponsePolicyPolicySummaryTypeDef
):
    """
    Type definition for `ClientCreatePolicyResponsePolicy` `PolicySummary`

    A structure that contains additional details about the policy.

    - **Id** *(string) --*

      The unique identifier (ID) of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
      "p-" followed by from 8 to 128 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the policy.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Description** *(string) --*

      The description of the policy.

    - **Type** *(string) --*

      The type of policy.

    - **AwsManaged** *(boolean) --*

      A boolean value that indicates whether the specified policy is an AWS managed policy. If
      true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
    """


_ClientCreatePolicyResponsePolicyTypeDef = TypedDict(
    "_ClientCreatePolicyResponsePolicyTypeDef",
    {
        "PolicySummary": ClientCreatePolicyResponsePolicyPolicySummaryTypeDef,
        "Content": str,
    },
    total=False,
)


class ClientCreatePolicyResponsePolicyTypeDef(_ClientCreatePolicyResponsePolicyTypeDef):
    """
    Type definition for `ClientCreatePolicyResponse` `Policy`

    A structure that contains details about the newly created policy.

    - **PolicySummary** *(dict) --*

      A structure that contains additional details about the policy.

      - **Id** *(string) --*

        The unique identifier (ID) of the policy.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
        "p-" followed by from 8 to 128 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the policy.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Name** *(string) --*

        The friendly name of the policy.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
        parameter is a string of any of the characters in the ASCII character range.

      - **Description** *(string) --*

        The description of the policy.

      - **Type** *(string) --*

        The type of policy.

      - **AwsManaged** *(boolean) --*

        A boolean value that indicates whether the specified policy is an AWS managed policy. If
        true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

    - **Content** *(string) --*

      The text content of the policy.
    """


_ClientCreatePolicyResponseTypeDef = TypedDict(
    "_ClientCreatePolicyResponseTypeDef",
    {"Policy": ClientCreatePolicyResponsePolicyTypeDef},
    total=False,
)


class ClientCreatePolicyResponseTypeDef(_ClientCreatePolicyResponseTypeDef):
    """
    Type definition for `ClientCreatePolicy` `Response`

    - **Policy** *(dict) --*

      A structure that contains details about the newly created policy.

      - **PolicySummary** *(dict) --*

        A structure that contains additional details about the policy.

        - **Id** *(string) --*

          The unique identifier (ID) of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
          "p-" followed by from 8 to 128 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the policy.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Description** *(string) --*

          The description of the policy.

        - **Type** *(string) --*

          The type of policy.

        - **AwsManaged** *(boolean) --*

          A boolean value that indicates whether the specified policy is an AWS managed policy. If
          true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

      - **Content** *(string) --*

        The text content of the policy.
    """


_ClientDeclineHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientDeclineHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ClientDeclineHandshakeResponseHandshakePartiesTypeDef(
    _ClientDeclineHandshakeResponseHandshakePartiesTypeDef
):
    """
    Type definition for `ClientDeclineHandshakeResponseHandshake` `Parties`

    Identifies a participant in a handshake.

    - **Id** *(string) --*

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
      requires "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --*

      The type of party.
    """


_ClientDeclineHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientDeclineHandshakeResponseHandshakeResourcesTypeDef",
    {"Value": str, "Type": str, "Resources": List[Any]},
    total=False,
)


class ClientDeclineHandshakeResponseHandshakeResourcesTypeDef(
    _ClientDeclineHandshakeResponseHandshakeResourcesTypeDef
):
    """
    Type definition for `ClientDeclineHandshakeResponseHandshake` `Resources`

    Contains additional data that is needed to process a handshake.

    - **Value** *(string) --*

      The information that is passed to the other party in the handshake. The format of the
      value string must match the requirements of the specified type.

    - **Type** *(string) --*

      The type of information being passed, specifying how the value is to be interpreted by
      the other party:

      * ``ACCOUNT`` - Specifies an AWS account ID number.

      * ``ORGANIZATION`` - Specifies an organization ID number.

      * ``EMAIL`` - Specifies the email address that is associated with the account that
      receives the handshake.

      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
      Included as information about an organization.

      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
      information about an organization.

      * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
      recipient to read.

    - **Resources** *(list) --*

      When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientDeclineHandshakeResponseHandshakeTypeDef = TypedDict(
    "_ClientDeclineHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientDeclineHandshakeResponseHandshakePartiesTypeDef],
        "State": str,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": str,
        "Resources": List[ClientDeclineHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientDeclineHandshakeResponseHandshakeTypeDef(
    _ClientDeclineHandshakeResponseHandshakeTypeDef
):
    """
    Type definition for `ClientDeclineHandshakeResponse` `Handshake`

    A structure that contains details about the declined handshake. The state is updated to show
    the value ``DECLINED`` .

    - **Id** *(string) --*

      The unique identifier (ID) of a handshake. The originating account creates the ID when it
      initiates the handshake.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
      "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of a handshake.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Parties** *(list) --*

      Information about the two accounts that are participating in the handshake.

      - *(dict) --*

        Identifies a participant in a handshake.

        - **Id** *(string) --*

          The unique identifier (ID) for the party.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
          requires "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Type** *(string) --*

          The type of party.

    - **State** *(string) --*

      The current state of the handshake. Use the state to trace the flow of the handshake
      through the process from its creation to its acceptance. The meaning of each of the valid
      values is as follows:

      * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
      handshake types) and not all recipients have responded yet. The request stays in this state
      until all recipients respond.

      * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
      types) and all recipients have responded, allowing the originator to complete the handshake
      action.

      * **CANCELED** : This handshake is no longer active because it was canceled by the
      originating account.

      * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

      * **DECLINED** : This handshake is no longer active because it was declined by the
      recipient account.

      * **EXPIRED** : This handshake is no longer active because the originator did not receive a
      response of any kind from the recipient before the expiration time (15 days).

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the handshake request was made.

    - **ExpirationTimestamp** *(datetime) --*

      The date and time that the handshake expires. If the recipient of the handshake request
      fails to respond before the specified date and time, the handshake becomes inactive and is
      no longer valid.

    - **Action** *(string) --*

      The type of handshake, indicating what action occurs when the recipient accepts the
      handshake. The following handshake types are supported:

      * **INVITE** : This type of handshake represents a request to join an organization. It is
      always sent from the master account to only non-member accounts.

      * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
      features in an organization. It is always sent from the master account to only *invited*
      member accounts. Created accounts do not receive this because those accounts were created
      by the organization's master account and approval is inferred.

      * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
      when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
      only to the master account and signals the master that it can finalize the process to
      enable all features.

    - **Resources** *(list) --*

      Additional information that is needed to process the handshake.

      - *(dict) --*

        Contains additional data that is needed to process a handshake.

        - **Value** *(string) --*

          The information that is passed to the other party in the handshake. The format of the
          value string must match the requirements of the specified type.

        - **Type** *(string) --*

          The type of information being passed, specifying how the value is to be interpreted by
          the other party:

          * ``ACCOUNT`` - Specifies an AWS account ID number.

          * ``ORGANIZATION`` - Specifies an organization ID number.

          * ``EMAIL`` - Specifies the email address that is associated with the account that
          receives the handshake.

          * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
          Included as information about an organization.

          * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
          information about an organization.

          * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
          recipient to read.

        - **Resources** *(list) --*

          When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientDeclineHandshakeResponseTypeDef = TypedDict(
    "_ClientDeclineHandshakeResponseTypeDef",
    {"Handshake": ClientDeclineHandshakeResponseHandshakeTypeDef},
    total=False,
)


class ClientDeclineHandshakeResponseTypeDef(_ClientDeclineHandshakeResponseTypeDef):
    """
    Type definition for `ClientDeclineHandshake` `Response`

    - **Handshake** *(dict) --*

      A structure that contains details about the declined handshake. The state is updated to show
      the value ``DECLINED`` .

      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of a handshake.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Parties** *(list) --*

        Information about the two accounts that are participating in the handshake.

        - *(dict) --*

          Identifies a participant in a handshake.

          - **Id** *(string) --*

            The unique identifier (ID) for the party.

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
            requires "h-" followed by from 8 to 32 lower-case letters or digits.

          - **Type** *(string) --*

            The type of party.

      - **State** *(string) --*

        The current state of the handshake. Use the state to trace the flow of the handshake
        through the process from its creation to its acceptance. The meaning of each of the valid
        values is as follows:

        * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
        handshake types) and not all recipients have responded yet. The request stays in this state
        until all recipients respond.

        * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
        types) and all recipients have responded, allowing the originator to complete the handshake
        action.

        * **CANCELED** : This handshake is no longer active because it was canceled by the
        originating account.

        * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

        * **DECLINED** : This handshake is no longer active because it was declined by the
        recipient account.

        * **EXPIRED** : This handshake is no longer active because the originator did not receive a
        response of any kind from the recipient before the expiration time (15 days).

      - **RequestedTimestamp** *(datetime) --*

        The date and time that the handshake request was made.

      - **ExpirationTimestamp** *(datetime) --*

        The date and time that the handshake expires. If the recipient of the handshake request
        fails to respond before the specified date and time, the handshake becomes inactive and is
        no longer valid.

      - **Action** *(string) --*

        The type of handshake, indicating what action occurs when the recipient accepts the
        handshake. The following handshake types are supported:

        * **INVITE** : This type of handshake represents a request to join an organization. It is
        always sent from the master account to only non-member accounts.

        * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
        features in an organization. It is always sent from the master account to only *invited*
        member accounts. Created accounts do not receive this because those accounts were created
        by the organization's master account and approval is inferred.

        * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
        when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
        only to the master account and signals the master that it can finalize the process to
        enable all features.

      - **Resources** *(list) --*

        Additional information that is needed to process the handshake.

        - *(dict) --*

          Contains additional data that is needed to process a handshake.

          - **Value** *(string) --*

            The information that is passed to the other party in the handshake. The format of the
            value string must match the requirements of the specified type.

          - **Type** *(string) --*

            The type of information being passed, specifying how the value is to be interpreted by
            the other party:

            * ``ACCOUNT`` - Specifies an AWS account ID number.

            * ``ORGANIZATION`` - Specifies an organization ID number.

            * ``EMAIL`` - Specifies the email address that is associated with the account that
            receives the handshake.

            * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
            Included as information about an organization.

            * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
            information about an organization.

            * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
            recipient to read.

          - **Resources** *(list) --*

            When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientDescribeAccountResponseAccountTypeDef = TypedDict(
    "_ClientDescribeAccountResponseAccountTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": str,
        "JoinedMethod": str,
        "JoinedTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeAccountResponseAccountTypeDef(
    _ClientDescribeAccountResponseAccountTypeDef
):
    """
    Type definition for `ClientDescribeAccountResponse` `Account`

    A structure that contains information about the requested account.

    - **Id** *(string) --*

      The unique identifier (ID) of the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the account.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Email** *(string) --*

      The email address associated with the AWS account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of
      characters that represents a standard Internet email address.

    - **Name** *(string) --*

      The friendly name of the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Status** *(string) --*

      The status of the account in the organization.

    - **JoinedMethod** *(string) --*

      The method by which the account joined the organization.

    - **JoinedTimestamp** *(datetime) --*

      The date the account became a part of the organization.
    """


_ClientDescribeAccountResponseTypeDef = TypedDict(
    "_ClientDescribeAccountResponseTypeDef",
    {"Account": ClientDescribeAccountResponseAccountTypeDef},
    total=False,
)


class ClientDescribeAccountResponseTypeDef(_ClientDescribeAccountResponseTypeDef):
    """
    Type definition for `ClientDescribeAccount` `Response`

    - **Account** *(dict) --*

      A structure that contains information about the requested account.

      - **Id** *(string) --*

        The unique identifier (ID) of the account.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the account.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Email** *(string) --*

        The email address associated with the AWS account.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of
        characters that represents a standard Internet email address.

      - **Name** *(string) --*

        The friendly name of the account.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
        parameter is a string of any of the characters in the ASCII character range.

      - **Status** *(string) --*

        The status of the account in the organization.

      - **JoinedMethod** *(string) --*

        The method by which the account joined the organization.

      - **JoinedTimestamp** *(datetime) --*

        The date the account became a part of the organization.
    """


_ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef = TypedDict(
    "_ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": str,
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": str,
    },
    total=False,
)


class ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef(
    _ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef
):
    """
    Type definition for `ClientDescribeCreateAccountStatusResponse` `CreateAccountStatus`

    A structure that contains the current status of an account creation request.

    - **Id** *(string) --*

      The unique identifier (ID) that references this request. You get this value from the
      response of the initial  CreateAccount request to create the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID
      string requires "car-" followed by from 8 to 32 lower-case letters or digits.

    - **AccountName** *(string) --*

      The account name given to the account when it was created.

    - **State** *(string) --*

      The status of the request.

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the request was made for the account creation.

    - **CompletedTimestamp** *(datetime) --*

      The date and time that the account was created and the request completed.

    - **AccountId** *(string) --*

      If the account was created successfully, the unique identifier (ID) of the new account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **GovCloudAccountId** *(string) --*

      If the account was created successfully, the unique identifier (ID) of the new account in
      the AWS GovCloud (US) Region.

    - **FailureReason** *(string) --*

      If the request failed, a description of the reason for the failure.

      * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the
      limit on the number of accounts in your organization.

      * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with
      that email address already exists.

      * GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be
      created because this Region already includes an account with that email address.

      * INVALID_ADDRESS: The account could not be created because the address you provided is not
      valid.

      * INVALID_EMAIL: The account could not be created because the email address you provided is
      not valid.

      * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try
      again later. If the problem persists, contact Customer Support.
    """


_ClientDescribeCreateAccountStatusResponseTypeDef = TypedDict(
    "_ClientDescribeCreateAccountStatusResponseTypeDef",
    {
        "CreateAccountStatus": ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef
    },
    total=False,
)


class ClientDescribeCreateAccountStatusResponseTypeDef(
    _ClientDescribeCreateAccountStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeCreateAccountStatus` `Response`

    - **CreateAccountStatus** *(dict) --*

      A structure that contains the current status of an account creation request.

      - **Id** *(string) --*

        The unique identifier (ID) that references this request. You get this value from the
        response of the initial  CreateAccount request to create the account.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID
        string requires "car-" followed by from 8 to 32 lower-case letters or digits.

      - **AccountName** *(string) --*

        The account name given to the account when it was created.

      - **State** *(string) --*

        The status of the request.

      - **RequestedTimestamp** *(datetime) --*

        The date and time that the request was made for the account creation.

      - **CompletedTimestamp** *(datetime) --*

        The date and time that the account was created and the request completed.

      - **AccountId** *(string) --*

        If the account was created successfully, the unique identifier (ID) of the new account.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.

      - **GovCloudAccountId** *(string) --*

        If the account was created successfully, the unique identifier (ID) of the new account in
        the AWS GovCloud (US) Region.

      - **FailureReason** *(string) --*

        If the request failed, a description of the reason for the failure.

        * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the
        limit on the number of accounts in your organization.

        * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with
        that email address already exists.

        * GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be
        created because this Region already includes an account with that email address.

        * INVALID_ADDRESS: The account could not be created because the address you provided is not
        valid.

        * INVALID_EMAIL: The account could not be created because the email address you provided is
        not valid.

        * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try
        again later. If the problem persists, contact Customer Support.
    """


_ClientDescribeHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientDescribeHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ClientDescribeHandshakeResponseHandshakePartiesTypeDef(
    _ClientDescribeHandshakeResponseHandshakePartiesTypeDef
):
    """
    Type definition for `ClientDescribeHandshakeResponseHandshake` `Parties`

    Identifies a participant in a handshake.

    - **Id** *(string) --*

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
      requires "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --*

      The type of party.
    """


_ClientDescribeHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientDescribeHandshakeResponseHandshakeResourcesTypeDef",
    {"Value": str, "Type": str, "Resources": List[Any]},
    total=False,
)


class ClientDescribeHandshakeResponseHandshakeResourcesTypeDef(
    _ClientDescribeHandshakeResponseHandshakeResourcesTypeDef
):
    """
    Type definition for `ClientDescribeHandshakeResponseHandshake` `Resources`

    Contains additional data that is needed to process a handshake.

    - **Value** *(string) --*

      The information that is passed to the other party in the handshake. The format of the
      value string must match the requirements of the specified type.

    - **Type** *(string) --*

      The type of information being passed, specifying how the value is to be interpreted by
      the other party:

      * ``ACCOUNT`` - Specifies an AWS account ID number.

      * ``ORGANIZATION`` - Specifies an organization ID number.

      * ``EMAIL`` - Specifies the email address that is associated with the account that
      receives the handshake.

      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
      Included as information about an organization.

      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
      information about an organization.

      * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
      recipient to read.

    - **Resources** *(list) --*

      When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientDescribeHandshakeResponseHandshakeTypeDef = TypedDict(
    "_ClientDescribeHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientDescribeHandshakeResponseHandshakePartiesTypeDef],
        "State": str,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": str,
        "Resources": List[ClientDescribeHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientDescribeHandshakeResponseHandshakeTypeDef(
    _ClientDescribeHandshakeResponseHandshakeTypeDef
):
    """
    Type definition for `ClientDescribeHandshakeResponse` `Handshake`

    A structure that contains information about the specified handshake.

    - **Id** *(string) --*

      The unique identifier (ID) of a handshake. The originating account creates the ID when it
      initiates the handshake.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
      "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of a handshake.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Parties** *(list) --*

      Information about the two accounts that are participating in the handshake.

      - *(dict) --*

        Identifies a participant in a handshake.

        - **Id** *(string) --*

          The unique identifier (ID) for the party.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
          requires "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Type** *(string) --*

          The type of party.

    - **State** *(string) --*

      The current state of the handshake. Use the state to trace the flow of the handshake
      through the process from its creation to its acceptance. The meaning of each of the valid
      values is as follows:

      * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
      handshake types) and not all recipients have responded yet. The request stays in this state
      until all recipients respond.

      * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
      types) and all recipients have responded, allowing the originator to complete the handshake
      action.

      * **CANCELED** : This handshake is no longer active because it was canceled by the
      originating account.

      * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

      * **DECLINED** : This handshake is no longer active because it was declined by the
      recipient account.

      * **EXPIRED** : This handshake is no longer active because the originator did not receive a
      response of any kind from the recipient before the expiration time (15 days).

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the handshake request was made.

    - **ExpirationTimestamp** *(datetime) --*

      The date and time that the handshake expires. If the recipient of the handshake request
      fails to respond before the specified date and time, the handshake becomes inactive and is
      no longer valid.

    - **Action** *(string) --*

      The type of handshake, indicating what action occurs when the recipient accepts the
      handshake. The following handshake types are supported:

      * **INVITE** : This type of handshake represents a request to join an organization. It is
      always sent from the master account to only non-member accounts.

      * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
      features in an organization. It is always sent from the master account to only *invited*
      member accounts. Created accounts do not receive this because those accounts were created
      by the organization's master account and approval is inferred.

      * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
      when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
      only to the master account and signals the master that it can finalize the process to
      enable all features.

    - **Resources** *(list) --*

      Additional information that is needed to process the handshake.

      - *(dict) --*

        Contains additional data that is needed to process a handshake.

        - **Value** *(string) --*

          The information that is passed to the other party in the handshake. The format of the
          value string must match the requirements of the specified type.

        - **Type** *(string) --*

          The type of information being passed, specifying how the value is to be interpreted by
          the other party:

          * ``ACCOUNT`` - Specifies an AWS account ID number.

          * ``ORGANIZATION`` - Specifies an organization ID number.

          * ``EMAIL`` - Specifies the email address that is associated with the account that
          receives the handshake.

          * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
          Included as information about an organization.

          * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
          information about an organization.

          * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
          recipient to read.

        - **Resources** *(list) --*

          When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientDescribeHandshakeResponseTypeDef = TypedDict(
    "_ClientDescribeHandshakeResponseTypeDef",
    {"Handshake": ClientDescribeHandshakeResponseHandshakeTypeDef},
    total=False,
)


class ClientDescribeHandshakeResponseTypeDef(_ClientDescribeHandshakeResponseTypeDef):
    """
    Type definition for `ClientDescribeHandshake` `Response`

    - **Handshake** *(dict) --*

      A structure that contains information about the specified handshake.

      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of a handshake.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Parties** *(list) --*

        Information about the two accounts that are participating in the handshake.

        - *(dict) --*

          Identifies a participant in a handshake.

          - **Id** *(string) --*

            The unique identifier (ID) for the party.

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
            requires "h-" followed by from 8 to 32 lower-case letters or digits.

          - **Type** *(string) --*

            The type of party.

      - **State** *(string) --*

        The current state of the handshake. Use the state to trace the flow of the handshake
        through the process from its creation to its acceptance. The meaning of each of the valid
        values is as follows:

        * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
        handshake types) and not all recipients have responded yet. The request stays in this state
        until all recipients respond.

        * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
        types) and all recipients have responded, allowing the originator to complete the handshake
        action.

        * **CANCELED** : This handshake is no longer active because it was canceled by the
        originating account.

        * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

        * **DECLINED** : This handshake is no longer active because it was declined by the
        recipient account.

        * **EXPIRED** : This handshake is no longer active because the originator did not receive a
        response of any kind from the recipient before the expiration time (15 days).

      - **RequestedTimestamp** *(datetime) --*

        The date and time that the handshake request was made.

      - **ExpirationTimestamp** *(datetime) --*

        The date and time that the handshake expires. If the recipient of the handshake request
        fails to respond before the specified date and time, the handshake becomes inactive and is
        no longer valid.

      - **Action** *(string) --*

        The type of handshake, indicating what action occurs when the recipient accepts the
        handshake. The following handshake types are supported:

        * **INVITE** : This type of handshake represents a request to join an organization. It is
        always sent from the master account to only non-member accounts.

        * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
        features in an organization. It is always sent from the master account to only *invited*
        member accounts. Created accounts do not receive this because those accounts were created
        by the organization's master account and approval is inferred.

        * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
        when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
        only to the master account and signals the master that it can finalize the process to
        enable all features.

      - **Resources** *(list) --*

        Additional information that is needed to process the handshake.

        - *(dict) --*

          Contains additional data that is needed to process a handshake.

          - **Value** *(string) --*

            The information that is passed to the other party in the handshake. The format of the
            value string must match the requirements of the specified type.

          - **Type** *(string) --*

            The type of information being passed, specifying how the value is to be interpreted by
            the other party:

            * ``ACCOUNT`` - Specifies an AWS account ID number.

            * ``ORGANIZATION`` - Specifies an organization ID number.

            * ``EMAIL`` - Specifies the email address that is associated with the account that
            receives the handshake.

            * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
            Included as information about an organization.

            * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
            information about an organization.

            * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
            recipient to read.

          - **Resources** *(list) --*

            When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef = TypedDict(
    "_ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    {"Type": str, "Status": str},
    total=False,
)


class ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef(
    _ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationResponseOrganization` `AvailablePolicyTypes`

    Contains information about a policy type and its status in the associated root.

    - **Type** *(string) --*

      The name of the policy type.

    - **Status** *(string) --*

      The status of the policy type as it relates to the associated root. To attach a policy
      of the specified type to a root or to an OU or account in that root, it must be
      available in the organization and enabled for that root.
    """


_ClientDescribeOrganizationResponseOrganizationTypeDef = TypedDict(
    "_ClientDescribeOrganizationResponseOrganizationTypeDef",
    {
        "Id": str,
        "Arn": str,
        "FeatureSet": str,
        "MasterAccountArn": str,
        "MasterAccountId": str,
        "MasterAccountEmail": str,
        "AvailablePolicyTypes": List[
            ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeOrganizationResponseOrganizationTypeDef(
    _ClientDescribeOrganizationResponseOrganizationTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationResponse` `Organization`

    A structure that contains information about the organization.

    - **Id** *(string) --*

      The unique identifier (ID) of an organization.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organization ID string
      requires "o-" followed by from 10 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of an organization.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **FeatureSet** *(string) --*

      Specifies the functionality that currently is available to the organization. If set to
      "ALL", then all features are enabled and policies can be applied to accounts in the
      organization. If set to "CONSOLIDATED_BILLING", then only consolidated billing
      functionality is available. For more information, see `Enabling All Features in Your
      Organization
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html>`__
      in the *AWS Organizations User Guide* .

    - **MasterAccountArn** *(string) --*

      The Amazon Resource Name (ARN) of the account that is designated as the master account for
      the organization.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **MasterAccountId** *(string) --*

      The unique identifier (ID) of the master account of an organization.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **MasterAccountEmail** *(string) --*

      The email address that is associated with the AWS account that is designated as the master
      account for the organization.

    - **AvailablePolicyTypes** *(list) --*

      A list of policy types that are enabled for this organization. For example, if your
      organization has all features enabled, then service control policies (SCPs) are included in
      the list.

      .. note::

        Even if a policy type is shown as available in the organization, you can separately
        enable and disable them at the root level by using  EnablePolicyType and
        DisablePolicyType . Use  ListRoots to see the status of a policy type in that root.

      - *(dict) --*

        Contains information about a policy type and its status in the associated root.

        - **Type** *(string) --*

          The name of the policy type.

        - **Status** *(string) --*

          The status of the policy type as it relates to the associated root. To attach a policy
          of the specified type to a root or to an OU or account in that root, it must be
          available in the organization and enabled for that root.
    """


_ClientDescribeOrganizationResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationResponseTypeDef",
    {"Organization": ClientDescribeOrganizationResponseOrganizationTypeDef},
    total=False,
)


class ClientDescribeOrganizationResponseTypeDef(
    _ClientDescribeOrganizationResponseTypeDef
):
    """
    Type definition for `ClientDescribeOrganization` `Response`

    - **Organization** *(dict) --*

      A structure that contains information about the organization.

      - **Id** *(string) --*

        The unique identifier (ID) of an organization.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organization ID string
        requires "o-" followed by from 10 to 32 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of an organization.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **FeatureSet** *(string) --*

        Specifies the functionality that currently is available to the organization. If set to
        "ALL", then all features are enabled and policies can be applied to accounts in the
        organization. If set to "CONSOLIDATED_BILLING", then only consolidated billing
        functionality is available. For more information, see `Enabling All Features in Your
        Organization
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html>`__
        in the *AWS Organizations User Guide* .

      - **MasterAccountArn** *(string) --*

        The Amazon Resource Name (ARN) of the account that is designated as the master account for
        the organization.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **MasterAccountId** *(string) --*

        The unique identifier (ID) of the master account of an organization.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.

      - **MasterAccountEmail** *(string) --*

        The email address that is associated with the AWS account that is designated as the master
        account for the organization.

      - **AvailablePolicyTypes** *(list) --*

        A list of policy types that are enabled for this organization. For example, if your
        organization has all features enabled, then service control policies (SCPs) are included in
        the list.

        .. note::

          Even if a policy type is shown as available in the organization, you can separately
          enable and disable them at the root level by using  EnablePolicyType and
          DisablePolicyType . Use  ListRoots to see the status of a policy type in that root.

        - *(dict) --*

          Contains information about a policy type and its status in the associated root.

          - **Type** *(string) --*

            The name of the policy type.

          - **Status** *(string) --*

            The status of the policy type as it relates to the associated root. To attach a policy
            of the specified type to a root or to an OU or account in that root, it must be
            available in the organization and enabled for that root.
    """


_ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef = TypedDict(
    "_ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef(
    _ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationalUnitResponse` `OrganizationalUnit`

    A structure that contains details about the specified OU.

    - **Id** *(string) --*

      The unique identifier (ID) associated with this OU.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
      string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the
      root that contains the OU) followed by a second "-" dash and from 8 to 32 additional
      lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of this OU.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of this OU.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.
    """


_ClientDescribeOrganizationalUnitResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationalUnitResponseTypeDef",
    {
        "OrganizationalUnit": ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef
    },
    total=False,
)


class ClientDescribeOrganizationalUnitResponseTypeDef(
    _ClientDescribeOrganizationalUnitResponseTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationalUnit` `Response`

    - **OrganizationalUnit** *(dict) --*

      A structure that contains details about the specified OU.

      - **Id** *(string) --*

        The unique identifier (ID) associated with this OU.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
        string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the
        root that contains the OU) followed by a second "-" dash and from 8 to 32 additional
        lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of this OU.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Name** *(string) --*

        The friendly name of this OU.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
        parameter is a string of any of the characters in the ASCII character range.
    """


_ClientDescribePolicyResponsePolicyPolicySummaryTypeDef = TypedDict(
    "_ClientDescribePolicyResponsePolicyPolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "AwsManaged": bool,
    },
    total=False,
)


class ClientDescribePolicyResponsePolicyPolicySummaryTypeDef(
    _ClientDescribePolicyResponsePolicyPolicySummaryTypeDef
):
    """
    Type definition for `ClientDescribePolicyResponsePolicy` `PolicySummary`

    A structure that contains additional details about the policy.

    - **Id** *(string) --*

      The unique identifier (ID) of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
      "p-" followed by from 8 to 128 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the policy.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Description** *(string) --*

      The description of the policy.

    - **Type** *(string) --*

      The type of policy.

    - **AwsManaged** *(boolean) --*

      A boolean value that indicates whether the specified policy is an AWS managed policy. If
      true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
    """


_ClientDescribePolicyResponsePolicyTypeDef = TypedDict(
    "_ClientDescribePolicyResponsePolicyTypeDef",
    {
        "PolicySummary": ClientDescribePolicyResponsePolicyPolicySummaryTypeDef,
        "Content": str,
    },
    total=False,
)


class ClientDescribePolicyResponsePolicyTypeDef(
    _ClientDescribePolicyResponsePolicyTypeDef
):
    """
    Type definition for `ClientDescribePolicyResponse` `Policy`

    A structure that contains details about the specified policy.

    - **PolicySummary** *(dict) --*

      A structure that contains additional details about the policy.

      - **Id** *(string) --*

        The unique identifier (ID) of the policy.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
        "p-" followed by from 8 to 128 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the policy.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Name** *(string) --*

        The friendly name of the policy.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
        parameter is a string of any of the characters in the ASCII character range.

      - **Description** *(string) --*

        The description of the policy.

      - **Type** *(string) --*

        The type of policy.

      - **AwsManaged** *(boolean) --*

        A boolean value that indicates whether the specified policy is an AWS managed policy. If
        true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

    - **Content** *(string) --*

      The text content of the policy.
    """


_ClientDescribePolicyResponseTypeDef = TypedDict(
    "_ClientDescribePolicyResponseTypeDef",
    {"Policy": ClientDescribePolicyResponsePolicyTypeDef},
    total=False,
)


class ClientDescribePolicyResponseTypeDef(_ClientDescribePolicyResponseTypeDef):
    """
    Type definition for `ClientDescribePolicy` `Response`

    - **Policy** *(dict) --*

      A structure that contains details about the specified policy.

      - **PolicySummary** *(dict) --*

        A structure that contains additional details about the policy.

        - **Id** *(string) --*

          The unique identifier (ID) of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
          "p-" followed by from 8 to 128 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the policy.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Description** *(string) --*

          The description of the policy.

        - **Type** *(string) --*

          The type of policy.

        - **AwsManaged** *(boolean) --*

          A boolean value that indicates whether the specified policy is an AWS managed policy. If
          true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

      - **Content** *(string) --*

        The text content of the policy.
    """


_ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef = TypedDict(
    "_ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef",
    {"Type": str, "Status": str},
    total=False,
)


class ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef(
    _ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef
):
    """
    Type definition for `ClientDisablePolicyTypeResponseRoot` `PolicyTypes`

    Contains information about a policy type and its status in the associated root.

    - **Type** *(string) --*

      The name of the policy type.

    - **Status** *(string) --*

      The status of the policy type as it relates to the associated root. To attach a policy
      of the specified type to a root or to an OU or account in that root, it must be
      available in the organization and enabled for that root.
    """


_ClientDisablePolicyTypeResponseRootTypeDef = TypedDict(
    "_ClientDisablePolicyTypeResponseRootTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef],
    },
    total=False,
)


class ClientDisablePolicyTypeResponseRootTypeDef(
    _ClientDisablePolicyTypeResponseRootTypeDef
):
    """
    Type definition for `ClientDisablePolicyTypeResponse` `Root`

    A structure that shows the root with the updated list of enabled policy types.

    - **Id** *(string) --*

      The unique identifier (ID) for the root.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-"
      followed by from 4 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the root.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the root.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **PolicyTypes** *(list) --*

      The types of policies that are currently enabled for the root and therefore can be attached
      to the root or to its OUs or accounts.

      .. note::

        Even if a policy type is shown as available in the organization, you can separately
        enable and disable them at the root level by using  EnablePolicyType and
        DisablePolicyType . Use  DescribeOrganization to see the availability of the policy types
        in that organization.

      - *(dict) --*

        Contains information about a policy type and its status in the associated root.

        - **Type** *(string) --*

          The name of the policy type.

        - **Status** *(string) --*

          The status of the policy type as it relates to the associated root. To attach a policy
          of the specified type to a root or to an OU or account in that root, it must be
          available in the organization and enabled for that root.
    """


_ClientDisablePolicyTypeResponseTypeDef = TypedDict(
    "_ClientDisablePolicyTypeResponseTypeDef",
    {"Root": ClientDisablePolicyTypeResponseRootTypeDef},
    total=False,
)


class ClientDisablePolicyTypeResponseTypeDef(_ClientDisablePolicyTypeResponseTypeDef):
    """
    Type definition for `ClientDisablePolicyType` `Response`

    - **Root** *(dict) --*

      A structure that shows the root with the updated list of enabled policy types.

      - **Id** *(string) --*

        The unique identifier (ID) for the root.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-"
        followed by from 4 to 32 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the root.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Name** *(string) --*

        The friendly name of the root.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
        parameter is a string of any of the characters in the ASCII character range.

      - **PolicyTypes** *(list) --*

        The types of policies that are currently enabled for the root and therefore can be attached
        to the root or to its OUs or accounts.

        .. note::

          Even if a policy type is shown as available in the organization, you can separately
          enable and disable them at the root level by using  EnablePolicyType and
          DisablePolicyType . Use  DescribeOrganization to see the availability of the policy types
          in that organization.

        - *(dict) --*

          Contains information about a policy type and its status in the associated root.

          - **Type** *(string) --*

            The name of the policy type.

          - **Status** *(string) --*

            The status of the policy type as it relates to the associated root. To attach a policy
            of the specified type to a root or to an OU or account in that root, it must be
            available in the organization and enabled for that root.
    """


_ClientEnableAllFeaturesResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientEnableAllFeaturesResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ClientEnableAllFeaturesResponseHandshakePartiesTypeDef(
    _ClientEnableAllFeaturesResponseHandshakePartiesTypeDef
):
    """
    Type definition for `ClientEnableAllFeaturesResponseHandshake` `Parties`

    Identifies a participant in a handshake.

    - **Id** *(string) --*

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
      requires "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --*

      The type of party.
    """


_ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef",
    {"Value": str, "Type": str, "Resources": List[Any]},
    total=False,
)


class ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef(
    _ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef
):
    """
    Type definition for `ClientEnableAllFeaturesResponseHandshake` `Resources`

    Contains additional data that is needed to process a handshake.

    - **Value** *(string) --*

      The information that is passed to the other party in the handshake. The format of the
      value string must match the requirements of the specified type.

    - **Type** *(string) --*

      The type of information being passed, specifying how the value is to be interpreted by
      the other party:

      * ``ACCOUNT`` - Specifies an AWS account ID number.

      * ``ORGANIZATION`` - Specifies an organization ID number.

      * ``EMAIL`` - Specifies the email address that is associated with the account that
      receives the handshake.

      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
      Included as information about an organization.

      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
      information about an organization.

      * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
      recipient to read.

    - **Resources** *(list) --*

      When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientEnableAllFeaturesResponseHandshakeTypeDef = TypedDict(
    "_ClientEnableAllFeaturesResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientEnableAllFeaturesResponseHandshakePartiesTypeDef],
        "State": str,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": str,
        "Resources": List[ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientEnableAllFeaturesResponseHandshakeTypeDef(
    _ClientEnableAllFeaturesResponseHandshakeTypeDef
):
    """
    Type definition for `ClientEnableAllFeaturesResponse` `Handshake`

    A structure that contains details about the handshake created to support this request to
    enable all features in the organization.

    - **Id** *(string) --*

      The unique identifier (ID) of a handshake. The originating account creates the ID when it
      initiates the handshake.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
      "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of a handshake.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Parties** *(list) --*

      Information about the two accounts that are participating in the handshake.

      - *(dict) --*

        Identifies a participant in a handshake.

        - **Id** *(string) --*

          The unique identifier (ID) for the party.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
          requires "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Type** *(string) --*

          The type of party.

    - **State** *(string) --*

      The current state of the handshake. Use the state to trace the flow of the handshake
      through the process from its creation to its acceptance. The meaning of each of the valid
      values is as follows:

      * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
      handshake types) and not all recipients have responded yet. The request stays in this state
      until all recipients respond.

      * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
      types) and all recipients have responded, allowing the originator to complete the handshake
      action.

      * **CANCELED** : This handshake is no longer active because it was canceled by the
      originating account.

      * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

      * **DECLINED** : This handshake is no longer active because it was declined by the
      recipient account.

      * **EXPIRED** : This handshake is no longer active because the originator did not receive a
      response of any kind from the recipient before the expiration time (15 days).

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the handshake request was made.

    - **ExpirationTimestamp** *(datetime) --*

      The date and time that the handshake expires. If the recipient of the handshake request
      fails to respond before the specified date and time, the handshake becomes inactive and is
      no longer valid.

    - **Action** *(string) --*

      The type of handshake, indicating what action occurs when the recipient accepts the
      handshake. The following handshake types are supported:

      * **INVITE** : This type of handshake represents a request to join an organization. It is
      always sent from the master account to only non-member accounts.

      * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
      features in an organization. It is always sent from the master account to only *invited*
      member accounts. Created accounts do not receive this because those accounts were created
      by the organization's master account and approval is inferred.

      * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
      when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
      only to the master account and signals the master that it can finalize the process to
      enable all features.

    - **Resources** *(list) --*

      Additional information that is needed to process the handshake.

      - *(dict) --*

        Contains additional data that is needed to process a handshake.

        - **Value** *(string) --*

          The information that is passed to the other party in the handshake. The format of the
          value string must match the requirements of the specified type.

        - **Type** *(string) --*

          The type of information being passed, specifying how the value is to be interpreted by
          the other party:

          * ``ACCOUNT`` - Specifies an AWS account ID number.

          * ``ORGANIZATION`` - Specifies an organization ID number.

          * ``EMAIL`` - Specifies the email address that is associated with the account that
          receives the handshake.

          * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
          Included as information about an organization.

          * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
          information about an organization.

          * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
          recipient to read.

        - **Resources** *(list) --*

          When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientEnableAllFeaturesResponseTypeDef = TypedDict(
    "_ClientEnableAllFeaturesResponseTypeDef",
    {"Handshake": ClientEnableAllFeaturesResponseHandshakeTypeDef},
    total=False,
)


class ClientEnableAllFeaturesResponseTypeDef(_ClientEnableAllFeaturesResponseTypeDef):
    """
    Type definition for `ClientEnableAllFeatures` `Response`

    - **Handshake** *(dict) --*

      A structure that contains details about the handshake created to support this request to
      enable all features in the organization.

      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of a handshake.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Parties** *(list) --*

        Information about the two accounts that are participating in the handshake.

        - *(dict) --*

          Identifies a participant in a handshake.

          - **Id** *(string) --*

            The unique identifier (ID) for the party.

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
            requires "h-" followed by from 8 to 32 lower-case letters or digits.

          - **Type** *(string) --*

            The type of party.

      - **State** *(string) --*

        The current state of the handshake. Use the state to trace the flow of the handshake
        through the process from its creation to its acceptance. The meaning of each of the valid
        values is as follows:

        * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
        handshake types) and not all recipients have responded yet. The request stays in this state
        until all recipients respond.

        * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
        types) and all recipients have responded, allowing the originator to complete the handshake
        action.

        * **CANCELED** : This handshake is no longer active because it was canceled by the
        originating account.

        * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

        * **DECLINED** : This handshake is no longer active because it was declined by the
        recipient account.

        * **EXPIRED** : This handshake is no longer active because the originator did not receive a
        response of any kind from the recipient before the expiration time (15 days).

      - **RequestedTimestamp** *(datetime) --*

        The date and time that the handshake request was made.

      - **ExpirationTimestamp** *(datetime) --*

        The date and time that the handshake expires. If the recipient of the handshake request
        fails to respond before the specified date and time, the handshake becomes inactive and is
        no longer valid.

      - **Action** *(string) --*

        The type of handshake, indicating what action occurs when the recipient accepts the
        handshake. The following handshake types are supported:

        * **INVITE** : This type of handshake represents a request to join an organization. It is
        always sent from the master account to only non-member accounts.

        * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
        features in an organization. It is always sent from the master account to only *invited*
        member accounts. Created accounts do not receive this because those accounts were created
        by the organization's master account and approval is inferred.

        * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
        when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
        only to the master account and signals the master that it can finalize the process to
        enable all features.

      - **Resources** *(list) --*

        Additional information that is needed to process the handshake.

        - *(dict) --*

          Contains additional data that is needed to process a handshake.

          - **Value** *(string) --*

            The information that is passed to the other party in the handshake. The format of the
            value string must match the requirements of the specified type.

          - **Type** *(string) --*

            The type of information being passed, specifying how the value is to be interpreted by
            the other party:

            * ``ACCOUNT`` - Specifies an AWS account ID number.

            * ``ORGANIZATION`` - Specifies an organization ID number.

            * ``EMAIL`` - Specifies the email address that is associated with the account that
            receives the handshake.

            * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
            Included as information about an organization.

            * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
            information about an organization.

            * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
            recipient to read.

          - **Resources** *(list) --*

            When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef = TypedDict(
    "_ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef",
    {"Type": str, "Status": str},
    total=False,
)


class ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef(
    _ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef
):
    """
    Type definition for `ClientEnablePolicyTypeResponseRoot` `PolicyTypes`

    Contains information about a policy type and its status in the associated root.

    - **Type** *(string) --*

      The name of the policy type.

    - **Status** *(string) --*

      The status of the policy type as it relates to the associated root. To attach a policy
      of the specified type to a root or to an OU or account in that root, it must be
      available in the organization and enabled for that root.
    """


_ClientEnablePolicyTypeResponseRootTypeDef = TypedDict(
    "_ClientEnablePolicyTypeResponseRootTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef],
    },
    total=False,
)


class ClientEnablePolicyTypeResponseRootTypeDef(
    _ClientEnablePolicyTypeResponseRootTypeDef
):
    """
    Type definition for `ClientEnablePolicyTypeResponse` `Root`

    A structure that shows the root with the updated list of enabled policy types.

    - **Id** *(string) --*

      The unique identifier (ID) for the root.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-"
      followed by from 4 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the root.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the root.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **PolicyTypes** *(list) --*

      The types of policies that are currently enabled for the root and therefore can be attached
      to the root or to its OUs or accounts.

      .. note::

        Even if a policy type is shown as available in the organization, you can separately
        enable and disable them at the root level by using  EnablePolicyType and
        DisablePolicyType . Use  DescribeOrganization to see the availability of the policy types
        in that organization.

      - *(dict) --*

        Contains information about a policy type and its status in the associated root.

        - **Type** *(string) --*

          The name of the policy type.

        - **Status** *(string) --*

          The status of the policy type as it relates to the associated root. To attach a policy
          of the specified type to a root or to an OU or account in that root, it must be
          available in the organization and enabled for that root.
    """


_ClientEnablePolicyTypeResponseTypeDef = TypedDict(
    "_ClientEnablePolicyTypeResponseTypeDef",
    {"Root": ClientEnablePolicyTypeResponseRootTypeDef},
    total=False,
)


class ClientEnablePolicyTypeResponseTypeDef(_ClientEnablePolicyTypeResponseTypeDef):
    """
    Type definition for `ClientEnablePolicyType` `Response`

    - **Root** *(dict) --*

      A structure that shows the root with the updated list of enabled policy types.

      - **Id** *(string) --*

        The unique identifier (ID) for the root.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-"
        followed by from 4 to 32 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the root.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Name** *(string) --*

        The friendly name of the root.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
        parameter is a string of any of the characters in the ASCII character range.

      - **PolicyTypes** *(list) --*

        The types of policies that are currently enabled for the root and therefore can be attached
        to the root or to its OUs or accounts.

        .. note::

          Even if a policy type is shown as available in the organization, you can separately
          enable and disable them at the root level by using  EnablePolicyType and
          DisablePolicyType . Use  DescribeOrganization to see the availability of the policy types
          in that organization.

        - *(dict) --*

          Contains information about a policy type and its status in the associated root.

          - **Type** *(string) --*

            The name of the policy type.

          - **Status** *(string) --*

            The status of the policy type as it relates to the associated root. To attach a policy
            of the specified type to a root or to an OU or account in that root, it must be
            available in the organization and enabled for that root.
    """


_ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef(
    _ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef
):
    """
    Type definition for `ClientInviteAccountToOrganizationResponseHandshake` `Parties`

    Identifies a participant in a handshake.

    - **Id** *(string) --*

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
      requires "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --*

      The type of party.
    """


_ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef",
    {"Value": str, "Type": str, "Resources": List[Any]},
    total=False,
)


class ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef(
    _ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef
):
    """
    Type definition for `ClientInviteAccountToOrganizationResponseHandshake` `Resources`

    Contains additional data that is needed to process a handshake.

    - **Value** *(string) --*

      The information that is passed to the other party in the handshake. The format of the
      value string must match the requirements of the specified type.

    - **Type** *(string) --*

      The type of information being passed, specifying how the value is to be interpreted by
      the other party:

      * ``ACCOUNT`` - Specifies an AWS account ID number.

      * ``ORGANIZATION`` - Specifies an organization ID number.

      * ``EMAIL`` - Specifies the email address that is associated with the account that
      receives the handshake.

      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
      Included as information about an organization.

      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
      information about an organization.

      * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
      recipient to read.

    - **Resources** *(list) --*

      When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientInviteAccountToOrganizationResponseHandshakeTypeDef = TypedDict(
    "_ClientInviteAccountToOrganizationResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[
            ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef
        ],
        "State": str,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": str,
        "Resources": List[
            ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef
        ],
    },
    total=False,
)


class ClientInviteAccountToOrganizationResponseHandshakeTypeDef(
    _ClientInviteAccountToOrganizationResponseHandshakeTypeDef
):
    """
    Type definition for `ClientInviteAccountToOrganizationResponse` `Handshake`

    A structure that contains details about the handshake that is created to support this
    invitation request.

    - **Id** *(string) --*

      The unique identifier (ID) of a handshake. The originating account creates the ID when it
      initiates the handshake.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
      "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of a handshake.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Parties** *(list) --*

      Information about the two accounts that are participating in the handshake.

      - *(dict) --*

        Identifies a participant in a handshake.

        - **Id** *(string) --*

          The unique identifier (ID) for the party.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
          requires "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Type** *(string) --*

          The type of party.

    - **State** *(string) --*

      The current state of the handshake. Use the state to trace the flow of the handshake
      through the process from its creation to its acceptance. The meaning of each of the valid
      values is as follows:

      * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
      handshake types) and not all recipients have responded yet. The request stays in this state
      until all recipients respond.

      * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
      types) and all recipients have responded, allowing the originator to complete the handshake
      action.

      * **CANCELED** : This handshake is no longer active because it was canceled by the
      originating account.

      * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

      * **DECLINED** : This handshake is no longer active because it was declined by the
      recipient account.

      * **EXPIRED** : This handshake is no longer active because the originator did not receive a
      response of any kind from the recipient before the expiration time (15 days).

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the handshake request was made.

    - **ExpirationTimestamp** *(datetime) --*

      The date and time that the handshake expires. If the recipient of the handshake request
      fails to respond before the specified date and time, the handshake becomes inactive and is
      no longer valid.

    - **Action** *(string) --*

      The type of handshake, indicating what action occurs when the recipient accepts the
      handshake. The following handshake types are supported:

      * **INVITE** : This type of handshake represents a request to join an organization. It is
      always sent from the master account to only non-member accounts.

      * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
      features in an organization. It is always sent from the master account to only *invited*
      member accounts. Created accounts do not receive this because those accounts were created
      by the organization's master account and approval is inferred.

      * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
      when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
      only to the master account and signals the master that it can finalize the process to
      enable all features.

    - **Resources** *(list) --*

      Additional information that is needed to process the handshake.

      - *(dict) --*

        Contains additional data that is needed to process a handshake.

        - **Value** *(string) --*

          The information that is passed to the other party in the handshake. The format of the
          value string must match the requirements of the specified type.

        - **Type** *(string) --*

          The type of information being passed, specifying how the value is to be interpreted by
          the other party:

          * ``ACCOUNT`` - Specifies an AWS account ID number.

          * ``ORGANIZATION`` - Specifies an organization ID number.

          * ``EMAIL`` - Specifies the email address that is associated with the account that
          receives the handshake.

          * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
          Included as information about an organization.

          * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
          information about an organization.

          * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
          recipient to read.

        - **Resources** *(list) --*

          When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientInviteAccountToOrganizationResponseTypeDef = TypedDict(
    "_ClientInviteAccountToOrganizationResponseTypeDef",
    {"Handshake": ClientInviteAccountToOrganizationResponseHandshakeTypeDef},
    total=False,
)


class ClientInviteAccountToOrganizationResponseTypeDef(
    _ClientInviteAccountToOrganizationResponseTypeDef
):
    """
    Type definition for `ClientInviteAccountToOrganization` `Response`

    - **Handshake** *(dict) --*

      A structure that contains details about the handshake that is created to support this
      invitation request.

      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of a handshake.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Parties** *(list) --*

        Information about the two accounts that are participating in the handshake.

        - *(dict) --*

          Identifies a participant in a handshake.

          - **Id** *(string) --*

            The unique identifier (ID) for the party.

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
            requires "h-" followed by from 8 to 32 lower-case letters or digits.

          - **Type** *(string) --*

            The type of party.

      - **State** *(string) --*

        The current state of the handshake. Use the state to trace the flow of the handshake
        through the process from its creation to its acceptance. The meaning of each of the valid
        values is as follows:

        * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
        handshake types) and not all recipients have responded yet. The request stays in this state
        until all recipients respond.

        * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy
        types) and all recipients have responded, allowing the originator to complete the handshake
        action.

        * **CANCELED** : This handshake is no longer active because it was canceled by the
        originating account.

        * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

        * **DECLINED** : This handshake is no longer active because it was declined by the
        recipient account.

        * **EXPIRED** : This handshake is no longer active because the originator did not receive a
        response of any kind from the recipient before the expiration time (15 days).

      - **RequestedTimestamp** *(datetime) --*

        The date and time that the handshake request was made.

      - **ExpirationTimestamp** *(datetime) --*

        The date and time that the handshake expires. If the recipient of the handshake request
        fails to respond before the specified date and time, the handshake becomes inactive and is
        no longer valid.

      - **Action** *(string) --*

        The type of handshake, indicating what action occurs when the recipient accepts the
        handshake. The following handshake types are supported:

        * **INVITE** : This type of handshake represents a request to join an organization. It is
        always sent from the master account to only non-member accounts.

        * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
        features in an organization. It is always sent from the master account to only *invited*
        member accounts. Created accounts do not receive this because those accounts were created
        by the organization's master account and approval is inferred.

        * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service
        when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent
        only to the master account and signals the master that it can finalize the process to
        enable all features.

      - **Resources** *(list) --*

        Additional information that is needed to process the handshake.

        - *(dict) --*

          Contains additional data that is needed to process a handshake.

          - **Value** *(string) --*

            The information that is passed to the other party in the handshake. The format of the
            value string must match the requirements of the specified type.

          - **Type** *(string) --*

            The type of information being passed, specifying how the value is to be interpreted by
            the other party:

            * ``ACCOUNT`` - Specifies an AWS account ID number.

            * ``ORGANIZATION`` - Specifies an organization ID number.

            * ``EMAIL`` - Specifies the email address that is associated with the account that
            receives the handshake.

            * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
            Included as information about an organization.

            * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
            information about an organization.

            * ``NOTES`` - Additional text provided by the handshake initiator and intended for the
            recipient to read.

          - **Resources** *(list) --*

            When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientInviteAccountToOrganizationTargetTypeDef = TypedDict(
    "_ClientInviteAccountToOrganizationTargetTypeDef", {"Id": str, "Type": str}
)


class ClientInviteAccountToOrganizationTargetTypeDef(
    _ClientInviteAccountToOrganizationTargetTypeDef
):
    """
    Type definition for `ClientInviteAccountToOrganization` `Target`

    The identifier (ID) of the AWS account that you want to invite to join your organization. This is
    a JSON object that contains the following elements:

     ``{ "Type": "ACCOUNT", "Id": "<* **account id number** * >" }``

    If you use the AWS CLI, you can submit this as a single string, similar to the following example:

     ``--target Id=123456789012,Type=ACCOUNT``

    If you specify ``"Type": "ACCOUNT"`` , you must provide the AWS account ID number as the ``Id`` .
    If you specify ``"Type": "EMAIL"`` , you must specify the email address that is associated with
    the account.

     ``--target Id=diego@example.com,Type=EMAIL``

    - **Id** *(string) --* **[REQUIRED]**

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-"
      followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --* **[REQUIRED]**

      The type of party.
    """


_ClientListAccountsForParentResponseAccountsTypeDef = TypedDict(
    "_ClientListAccountsForParentResponseAccountsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": str,
        "JoinedMethod": str,
        "JoinedTimestamp": datetime,
    },
    total=False,
)


class ClientListAccountsForParentResponseAccountsTypeDef(
    _ClientListAccountsForParentResponseAccountsTypeDef
):
    """
    Type definition for `ClientListAccountsForParentResponse` `Accounts`

    Contains information about an AWS account that is a member of an organization.

    - **Id** *(string) --*

      The unique identifier (ID) of the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the account.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Email** *(string) --*

      The email address associated with the AWS account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of
      characters that represents a standard Internet email address.

    - **Name** *(string) --*

      The friendly name of the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Status** *(string) --*

      The status of the account in the organization.

    - **JoinedMethod** *(string) --*

      The method by which the account joined the organization.

    - **JoinedTimestamp** *(datetime) --*

      The date the account became a part of the organization.
    """


_ClientListAccountsForParentResponseTypeDef = TypedDict(
    "_ClientListAccountsForParentResponseTypeDef",
    {
        "Accounts": List[ClientListAccountsForParentResponseAccountsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListAccountsForParentResponseTypeDef(
    _ClientListAccountsForParentResponseTypeDef
):
    """
    Type definition for `ClientListAccountsForParent` `Response`

    - **Accounts** *(list) --*

      A list of the accounts in the specified root or OU.

      - *(dict) --*

        Contains information about an AWS account that is a member of an organization.

        - **Id** *(string) --*

          The unique identifier (ID) of the account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
          exactly 12 digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the account.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Email** *(string) --*

          The email address associated with the AWS account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of
          characters that represents a standard Internet email address.

        - **Name** *(string) --*

          The friendly name of the account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Status** *(string) --*

          The status of the account in the organization.

        - **JoinedMethod** *(string) --*

          The method by which the account joined the organization.

        - **JoinedTimestamp** *(datetime) --*

          The date the account became a part of the organization.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListAccountsResponseAccountsTypeDef = TypedDict(
    "_ClientListAccountsResponseAccountsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": str,
        "JoinedMethod": str,
        "JoinedTimestamp": datetime,
    },
    total=False,
)


class ClientListAccountsResponseAccountsTypeDef(
    _ClientListAccountsResponseAccountsTypeDef
):
    """
    Type definition for `ClientListAccountsResponse` `Accounts`

    Contains information about an AWS account that is a member of an organization.

    - **Id** *(string) --*

      The unique identifier (ID) of the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the account.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Email** *(string) --*

      The email address associated with the AWS account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of
      characters that represents a standard Internet email address.

    - **Name** *(string) --*

      The friendly name of the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Status** *(string) --*

      The status of the account in the organization.

    - **JoinedMethod** *(string) --*

      The method by which the account joined the organization.

    - **JoinedTimestamp** *(datetime) --*

      The date the account became a part of the organization.
    """


_ClientListAccountsResponseTypeDef = TypedDict(
    "_ClientListAccountsResponseTypeDef",
    {"Accounts": List[ClientListAccountsResponseAccountsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAccountsResponseTypeDef(_ClientListAccountsResponseTypeDef):
    """
    Type definition for `ClientListAccounts` `Response`

    - **Accounts** *(list) --*

      A list of objects in the organization.

      - *(dict) --*

        Contains information about an AWS account that is a member of an organization.

        - **Id** *(string) --*

          The unique identifier (ID) of the account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
          exactly 12 digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the account.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Email** *(string) --*

          The email address associated with the AWS account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of
          characters that represents a standard Internet email address.

        - **Name** *(string) --*

          The friendly name of the account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Status** *(string) --*

          The status of the account in the organization.

        - **JoinedMethod** *(string) --*

          The method by which the account joined the organization.

        - **JoinedTimestamp** *(datetime) --*

          The date the account became a part of the organization.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef = TypedDict(
    "_ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef",
    {"ServicePrincipal": str, "DateEnabled": datetime},
    total=False,
)


class ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef(
    _ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef
):
    """
    Type definition for `ClientListAwsServiceAccessForOrganizationResponse` `EnabledServicePrincipals`

    A structure that contains details of a service principal that is enabled to integrate with
    AWS Organizations.

    - **ServicePrincipal** *(string) --*

      The name of the service principal. This is typically in the form of a URL, such as: ``
      *servicename* .amazonaws.com`` .

    - **DateEnabled** *(datetime) --*

      The date that the service principal was enabled for integration with AWS Organizations.
    """


_ClientListAwsServiceAccessForOrganizationResponseTypeDef = TypedDict(
    "_ClientListAwsServiceAccessForOrganizationResponseTypeDef",
    {
        "EnabledServicePrincipals": List[
            ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListAwsServiceAccessForOrganizationResponseTypeDef(
    _ClientListAwsServiceAccessForOrganizationResponseTypeDef
):
    """
    Type definition for `ClientListAwsServiceAccessForOrganization` `Response`

    - **EnabledServicePrincipals** *(list) --*

      A list of the service principals for the services that are enabled to integrate with your
      organization. Each principal is a structure that includes the name and the date that it was
      enabled for integration with AWS Organizations.

      - *(dict) --*

        A structure that contains details of a service principal that is enabled to integrate with
        AWS Organizations.

        - **ServicePrincipal** *(string) --*

          The name of the service principal. This is typically in the form of a URL, such as: ``
          *servicename* .amazonaws.com`` .

        - **DateEnabled** *(datetime) --*

          The date that the service principal was enabled for integration with AWS Organizations.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListChildrenResponseChildrenTypeDef = TypedDict(
    "_ClientListChildrenResponseChildrenTypeDef", {"Id": str, "Type": str}, total=False
)


class ClientListChildrenResponseChildrenTypeDef(
    _ClientListChildrenResponseChildrenTypeDef
):
    """
    Type definition for `ClientListChildrenResponse` `Children`

    Contains a list of child entities, either OUs or accounts.

    - **Id** *(string) --*

      The unique identifier (ID) of this child entity.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires
      one of the following:

      * Account: a string that consists of exactly 12 digits.

      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
      lower-case letters or digits (the ID of the root that contains the OU) followed by a
      second "-" dash and from 8 to 32 additional lower-case letters or digits.

    - **Type** *(string) --*

      The type of this child entity.
    """


_ClientListChildrenResponseTypeDef = TypedDict(
    "_ClientListChildrenResponseTypeDef",
    {"Children": List[ClientListChildrenResponseChildrenTypeDef], "NextToken": str},
    total=False,
)


class ClientListChildrenResponseTypeDef(_ClientListChildrenResponseTypeDef):
    """
    Type definition for `ClientListChildren` `Response`

    - **Children** *(list) --*

      The list of children of the specified parent container.

      - *(dict) --*

        Contains a list of child entities, either OUs or accounts.

        - **Id** *(string) --*

          The unique identifier (ID) of this child entity.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires
          one of the following:

          * Account: a string that consists of exactly 12 digits.

          * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
          lower-case letters or digits (the ID of the root that contains the OU) followed by a
          second "-" dash and from 8 to 32 additional lower-case letters or digits.

        - **Type** *(string) --*

          The type of this child entity.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef = TypedDict(
    "_ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": str,
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": str,
    },
    total=False,
)


class ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef(
    _ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef
):
    """
    Type definition for `ClientListCreateAccountStatusResponse` `CreateAccountStatuses`

    Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an
    AWS account or an AWS GovCloud (US) account in an organization.

    - **Id** *(string) --*

      The unique identifier (ID) that references this request. You get this value from the
      response of the initial  CreateAccount request to create the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID
      string requires "car-" followed by from 8 to 32 lower-case letters or digits.

    - **AccountName** *(string) --*

      The account name given to the account when it was created.

    - **State** *(string) --*

      The status of the request.

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the request was made for the account creation.

    - **CompletedTimestamp** *(datetime) --*

      The date and time that the account was created and the request completed.

    - **AccountId** *(string) --*

      If the account was created successfully, the unique identifier (ID) of the new account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **GovCloudAccountId** *(string) --*

      If the account was created successfully, the unique identifier (ID) of the new account in
      the AWS GovCloud (US) Region.

    - **FailureReason** *(string) --*

      If the request failed, a description of the reason for the failure.

      * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the
      limit on the number of accounts in your organization.

      * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with
      that email address already exists.

      * GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not
      be created because this Region already includes an account with that email address.

      * INVALID_ADDRESS: The account could not be created because the address you provided is
      not valid.

      * INVALID_EMAIL: The account could not be created because the email address you provided
      is not valid.

      * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try
      again later. If the problem persists, contact Customer Support.
    """


_ClientListCreateAccountStatusResponseTypeDef = TypedDict(
    "_ClientListCreateAccountStatusResponseTypeDef",
    {
        "CreateAccountStatuses": List[
            ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListCreateAccountStatusResponseTypeDef(
    _ClientListCreateAccountStatusResponseTypeDef
):
    """
    Type definition for `ClientListCreateAccountStatus` `Response`

    - **CreateAccountStatuses** *(list) --*

      A list of objects with details about the requests. Certain elements, such as the accountId
      number, are present in the output only after the account has been successfully created.

      - *(dict) --*

        Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an
        AWS account or an AWS GovCloud (US) account in an organization.

        - **Id** *(string) --*

          The unique identifier (ID) that references this request. You get this value from the
          response of the initial  CreateAccount request to create the account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID
          string requires "car-" followed by from 8 to 32 lower-case letters or digits.

        - **AccountName** *(string) --*

          The account name given to the account when it was created.

        - **State** *(string) --*

          The status of the request.

        - **RequestedTimestamp** *(datetime) --*

          The date and time that the request was made for the account creation.

        - **CompletedTimestamp** *(datetime) --*

          The date and time that the account was created and the request completed.

        - **AccountId** *(string) --*

          If the account was created successfully, the unique identifier (ID) of the new account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
          exactly 12 digits.

        - **GovCloudAccountId** *(string) --*

          If the account was created successfully, the unique identifier (ID) of the new account in
          the AWS GovCloud (US) Region.

        - **FailureReason** *(string) --*

          If the request failed, a description of the reason for the failure.

          * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the
          limit on the number of accounts in your organization.

          * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with
          that email address already exists.

          * GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not
          be created because this Region already includes an account with that email address.

          * INVALID_ADDRESS: The account could not be created because the address you provided is
          not valid.

          * INVALID_EMAIL: The account could not be created because the email address you provided
          is not valid.

          * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try
          again later. If the problem persists, contact Customer Support.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListHandshakesForAccountFilterTypeDef = TypedDict(
    "_ClientListHandshakesForAccountFilterTypeDef",
    {"ActionType": str, "ParentHandshakeId": str},
    total=False,
)


class ClientListHandshakesForAccountFilterTypeDef(
    _ClientListHandshakesForAccountFilterTypeDef
):
    """
    Type definition for `ClientListHandshakesForAccount` `Filter`

    Filters the handshakes that you want included in the response. The default is all types. Use the
    ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` ,
    ``ENABLE_ALL_FEATURES`` , or ``APPROVE_ALL_FEATURES`` . Alternatively, for the
    ``ENABLE_ALL_FEATURES`` handshake that generates a separate child handshake for each member
    account, you can specify ``ParentHandshakeId`` to see only the handshakes that were generated by
    that parent request.

    - **ActionType** *(string) --*

      Specifies the type of handshake action.

      If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .

    - **ParentHandshakeId** *(string) --*

      Specifies the parent handshake. Only used for handshake types that are a child of another type.

      If you specify ``ParentHandshakeId`` , you cannot also specify ``ActionType`` .

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-"
      followed by from 8 to 32 lower-case letters or digits.
    """


_ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef = TypedDict(
    "_ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef(
    _ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef
):
    """
    Type definition for `ClientListHandshakesForAccountResponseHandshakes` `Parties`

    Identifies a participant in a handshake.

    - **Id** *(string) --*

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
      requires "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --*

      The type of party.
    """


_ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef = TypedDict(
    "_ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef",
    {"Value": str, "Type": str, "Resources": List[Any]},
    total=False,
)


class ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef(
    _ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef
):
    """
    Type definition for `ClientListHandshakesForAccountResponseHandshakes` `Resources`

    Contains additional data that is needed to process a handshake.

    - **Value** *(string) --*

      The information that is passed to the other party in the handshake. The format of the
      value string must match the requirements of the specified type.

    - **Type** *(string) --*

      The type of information being passed, specifying how the value is to be interpreted
      by the other party:

      * ``ACCOUNT`` - Specifies an AWS account ID number.

      * ``ORGANIZATION`` - Specifies an organization ID number.

      * ``EMAIL`` - Specifies the email address that is associated with the account that
      receives the handshake.

      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
      Included as information about an organization.

      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
      information about an organization.

      * ``NOTES`` - Additional text provided by the handshake initiator and intended for
      the recipient to read.

    - **Resources** *(list) --*

      When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientListHandshakesForAccountResponseHandshakesTypeDef = TypedDict(
    "_ClientListHandshakesForAccountResponseHandshakesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef],
        "State": str,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": str,
        "Resources": List[
            ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef
        ],
    },
    total=False,
)


class ClientListHandshakesForAccountResponseHandshakesTypeDef(
    _ClientListHandshakesForAccountResponseHandshakesTypeDef
):
    """
    Type definition for `ClientListHandshakesForAccountResponse` `Handshakes`

    Contains information that must be exchanged to securely establish a relationship between
    two accounts (an *originator* and a *recipient* ). For example, when a master account (the
    originator) invites another account (the recipient) to join its organization, the two
    accounts exchange information as a series of handshake requests and responses.

     **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
     days after entering that state After that they are deleted.

    - **Id** *(string) --*

      The unique identifier (ID) of a handshake. The originating account creates the ID when it
      initiates the handshake.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
      "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of a handshake.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Parties** *(list) --*

      Information about the two accounts that are participating in the handshake.

      - *(dict) --*

        Identifies a participant in a handshake.

        - **Id** *(string) --*

          The unique identifier (ID) for the party.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
          requires "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Type** *(string) --*

          The type of party.

    - **State** *(string) --*

      The current state of the handshake. Use the state to trace the flow of the handshake
      through the process from its creation to its acceptance. The meaning of each of the valid
      values is as follows:

      * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
      handshake types) and not all recipients have responded yet. The request stays in this
      state until all recipients respond.

      * **OPEN** : This handshake was sent to multiple recipients (applicable to only some
      policy types) and all recipients have responded, allowing the originator to complete the
      handshake action.

      * **CANCELED** : This handshake is no longer active because it was canceled by the
      originating account.

      * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

      * **DECLINED** : This handshake is no longer active because it was declined by the
      recipient account.

      * **EXPIRED** : This handshake is no longer active because the originator did not receive
      a response of any kind from the recipient before the expiration time (15 days).

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the handshake request was made.

    - **ExpirationTimestamp** *(datetime) --*

      The date and time that the handshake expires. If the recipient of the handshake request
      fails to respond before the specified date and time, the handshake becomes inactive and
      is no longer valid.

    - **Action** *(string) --*

      The type of handshake, indicating what action occurs when the recipient accepts the
      handshake. The following handshake types are supported:

      * **INVITE** : This type of handshake represents a request to join an organization. It is
      always sent from the master account to only non-member accounts.

      * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
      features in an organization. It is always sent from the master account to only *invited*
      member accounts. Created accounts do not receive this because those accounts were created
      by the organization's master account and approval is inferred.

      * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations
      service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It
      is sent only to the master account and signals the master that it can finalize the
      process to enable all features.

    - **Resources** *(list) --*

      Additional information that is needed to process the handshake.

      - *(dict) --*

        Contains additional data that is needed to process a handshake.

        - **Value** *(string) --*

          The information that is passed to the other party in the handshake. The format of the
          value string must match the requirements of the specified type.

        - **Type** *(string) --*

          The type of information being passed, specifying how the value is to be interpreted
          by the other party:

          * ``ACCOUNT`` - Specifies an AWS account ID number.

          * ``ORGANIZATION`` - Specifies an organization ID number.

          * ``EMAIL`` - Specifies the email address that is associated with the account that
          receives the handshake.

          * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
          Included as information about an organization.

          * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
          information about an organization.

          * ``NOTES`` - Additional text provided by the handshake initiator and intended for
          the recipient to read.

        - **Resources** *(list) --*

          When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientListHandshakesForAccountResponseTypeDef = TypedDict(
    "_ClientListHandshakesForAccountResponseTypeDef",
    {
        "Handshakes": List[ClientListHandshakesForAccountResponseHandshakesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListHandshakesForAccountResponseTypeDef(
    _ClientListHandshakesForAccountResponseTypeDef
):
    """
    Type definition for `ClientListHandshakesForAccount` `Response`

    - **Handshakes** *(list) --*

      A list of  Handshake objects with details about each of the handshakes that is associated
      with the specified account.

      - *(dict) --*

        Contains information that must be exchanged to securely establish a relationship between
        two accounts (an *originator* and a *recipient* ). For example, when a master account (the
        originator) invites another account (the recipient) to join its organization, the two
        accounts exchange information as a series of handshake requests and responses.

         **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
         days after entering that state After that they are deleted.

        - **Id** *(string) --*

          The unique identifier (ID) of a handshake. The originating account creates the ID when it
          initiates the handshake.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
          "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of a handshake.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Parties** *(list) --*

          Information about the two accounts that are participating in the handshake.

          - *(dict) --*

            Identifies a participant in a handshake.

            - **Id** *(string) --*

              The unique identifier (ID) for the party.

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
              requires "h-" followed by from 8 to 32 lower-case letters or digits.

            - **Type** *(string) --*

              The type of party.

        - **State** *(string) --*

          The current state of the handshake. Use the state to trace the flow of the handshake
          through the process from its creation to its acceptance. The meaning of each of the valid
          values is as follows:

          * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
          handshake types) and not all recipients have responded yet. The request stays in this
          state until all recipients respond.

          * **OPEN** : This handshake was sent to multiple recipients (applicable to only some
          policy types) and all recipients have responded, allowing the originator to complete the
          handshake action.

          * **CANCELED** : This handshake is no longer active because it was canceled by the
          originating account.

          * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

          * **DECLINED** : This handshake is no longer active because it was declined by the
          recipient account.

          * **EXPIRED** : This handshake is no longer active because the originator did not receive
          a response of any kind from the recipient before the expiration time (15 days).

        - **RequestedTimestamp** *(datetime) --*

          The date and time that the handshake request was made.

        - **ExpirationTimestamp** *(datetime) --*

          The date and time that the handshake expires. If the recipient of the handshake request
          fails to respond before the specified date and time, the handshake becomes inactive and
          is no longer valid.

        - **Action** *(string) --*

          The type of handshake, indicating what action occurs when the recipient accepts the
          handshake. The following handshake types are supported:

          * **INVITE** : This type of handshake represents a request to join an organization. It is
          always sent from the master account to only non-member accounts.

          * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
          features in an organization. It is always sent from the master account to only *invited*
          member accounts. Created accounts do not receive this because those accounts were created
          by the organization's master account and approval is inferred.

          * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations
          service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It
          is sent only to the master account and signals the master that it can finalize the
          process to enable all features.

        - **Resources** *(list) --*

          Additional information that is needed to process the handshake.

          - *(dict) --*

            Contains additional data that is needed to process a handshake.

            - **Value** *(string) --*

              The information that is passed to the other party in the handshake. The format of the
              value string must match the requirements of the specified type.

            - **Type** *(string) --*

              The type of information being passed, specifying how the value is to be interpreted
              by the other party:

              * ``ACCOUNT`` - Specifies an AWS account ID number.

              * ``ORGANIZATION`` - Specifies an organization ID number.

              * ``EMAIL`` - Specifies the email address that is associated with the account that
              receives the handshake.

              * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
              Included as information about an organization.

              * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
              information about an organization.

              * ``NOTES`` - Additional text provided by the handshake initiator and intended for
              the recipient to read.

            - **Resources** *(list) --*

              When needed, contains an additional array of ``HandshakeResource`` objects.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListHandshakesForOrganizationFilterTypeDef = TypedDict(
    "_ClientListHandshakesForOrganizationFilterTypeDef",
    {"ActionType": str, "ParentHandshakeId": str},
    total=False,
)


class ClientListHandshakesForOrganizationFilterTypeDef(
    _ClientListHandshakesForOrganizationFilterTypeDef
):
    """
    Type definition for `ClientListHandshakesForOrganization` `Filter`

    A filter of the handshakes that you want included in the response. The default is all types. Use
    the ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` ,
    ``ENABLE-ALL-FEATURES`` , or ``APPROVE-ALL-FEATURES`` . Alternatively, for the
    ``ENABLE-ALL-FEATURES`` handshake that generates a separate child handshake for each member
    account, you can specify the ``ParentHandshakeId`` to see only the handshakes that were generated
    by that parent request.

    - **ActionType** *(string) --*

      Specifies the type of handshake action.

      If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .

    - **ParentHandshakeId** *(string) --*

      Specifies the parent handshake. Only used for handshake types that are a child of another type.

      If you specify ``ParentHandshakeId`` , you cannot also specify ``ActionType`` .

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-"
      followed by from 8 to 32 lower-case letters or digits.
    """


_ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef = TypedDict(
    "_ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef(
    _ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef
):
    """
    Type definition for `ClientListHandshakesForOrganizationResponseHandshakes` `Parties`

    Identifies a participant in a handshake.

    - **Id** *(string) --*

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
      requires "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --*

      The type of party.
    """


_ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef = TypedDict(
    "_ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef",
    {"Value": str, "Type": str, "Resources": List[Any]},
    total=False,
)


class ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef(
    _ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef
):
    """
    Type definition for `ClientListHandshakesForOrganizationResponseHandshakes` `Resources`

    Contains additional data that is needed to process a handshake.

    - **Value** *(string) --*

      The information that is passed to the other party in the handshake. The format of the
      value string must match the requirements of the specified type.

    - **Type** *(string) --*

      The type of information being passed, specifying how the value is to be interpreted
      by the other party:

      * ``ACCOUNT`` - Specifies an AWS account ID number.

      * ``ORGANIZATION`` - Specifies an organization ID number.

      * ``EMAIL`` - Specifies the email address that is associated with the account that
      receives the handshake.

      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
      Included as information about an organization.

      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
      information about an organization.

      * ``NOTES`` - Additional text provided by the handshake initiator and intended for
      the recipient to read.

    - **Resources** *(list) --*

      When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientListHandshakesForOrganizationResponseHandshakesTypeDef = TypedDict(
    "_ClientListHandshakesForOrganizationResponseHandshakesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[
            ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef
        ],
        "State": str,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": str,
        "Resources": List[
            ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef
        ],
    },
    total=False,
)


class ClientListHandshakesForOrganizationResponseHandshakesTypeDef(
    _ClientListHandshakesForOrganizationResponseHandshakesTypeDef
):
    """
    Type definition for `ClientListHandshakesForOrganizationResponse` `Handshakes`

    Contains information that must be exchanged to securely establish a relationship between
    two accounts (an *originator* and a *recipient* ). For example, when a master account (the
    originator) invites another account (the recipient) to join its organization, the two
    accounts exchange information as a series of handshake requests and responses.

     **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
     days after entering that state After that they are deleted.

    - **Id** *(string) --*

      The unique identifier (ID) of a handshake. The originating account creates the ID when it
      initiates the handshake.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
      "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of a handshake.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Parties** *(list) --*

      Information about the two accounts that are participating in the handshake.

      - *(dict) --*

        Identifies a participant in a handshake.

        - **Id** *(string) --*

          The unique identifier (ID) for the party.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
          requires "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Type** *(string) --*

          The type of party.

    - **State** *(string) --*

      The current state of the handshake. Use the state to trace the flow of the handshake
      through the process from its creation to its acceptance. The meaning of each of the valid
      values is as follows:

      * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
      handshake types) and not all recipients have responded yet. The request stays in this
      state until all recipients respond.

      * **OPEN** : This handshake was sent to multiple recipients (applicable to only some
      policy types) and all recipients have responded, allowing the originator to complete the
      handshake action.

      * **CANCELED** : This handshake is no longer active because it was canceled by the
      originating account.

      * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

      * **DECLINED** : This handshake is no longer active because it was declined by the
      recipient account.

      * **EXPIRED** : This handshake is no longer active because the originator did not receive
      a response of any kind from the recipient before the expiration time (15 days).

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the handshake request was made.

    - **ExpirationTimestamp** *(datetime) --*

      The date and time that the handshake expires. If the recipient of the handshake request
      fails to respond before the specified date and time, the handshake becomes inactive and
      is no longer valid.

    - **Action** *(string) --*

      The type of handshake, indicating what action occurs when the recipient accepts the
      handshake. The following handshake types are supported:

      * **INVITE** : This type of handshake represents a request to join an organization. It is
      always sent from the master account to only non-member accounts.

      * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
      features in an organization. It is always sent from the master account to only *invited*
      member accounts. Created accounts do not receive this because those accounts were created
      by the organization's master account and approval is inferred.

      * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations
      service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It
      is sent only to the master account and signals the master that it can finalize the
      process to enable all features.

    - **Resources** *(list) --*

      Additional information that is needed to process the handshake.

      - *(dict) --*

        Contains additional data that is needed to process a handshake.

        - **Value** *(string) --*

          The information that is passed to the other party in the handshake. The format of the
          value string must match the requirements of the specified type.

        - **Type** *(string) --*

          The type of information being passed, specifying how the value is to be interpreted
          by the other party:

          * ``ACCOUNT`` - Specifies an AWS account ID number.

          * ``ORGANIZATION`` - Specifies an organization ID number.

          * ``EMAIL`` - Specifies the email address that is associated with the account that
          receives the handshake.

          * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
          Included as information about an organization.

          * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
          information about an organization.

          * ``NOTES`` - Additional text provided by the handshake initiator and intended for
          the recipient to read.

        - **Resources** *(list) --*

          When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ClientListHandshakesForOrganizationResponseTypeDef = TypedDict(
    "_ClientListHandshakesForOrganizationResponseTypeDef",
    {
        "Handshakes": List[
            ClientListHandshakesForOrganizationResponseHandshakesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListHandshakesForOrganizationResponseTypeDef(
    _ClientListHandshakesForOrganizationResponseTypeDef
):
    """
    Type definition for `ClientListHandshakesForOrganization` `Response`

    - **Handshakes** *(list) --*

      A list of  Handshake objects with details about each of the handshakes that are associated
      with an organization.

      - *(dict) --*

        Contains information that must be exchanged to securely establish a relationship between
        two accounts (an *originator* and a *recipient* ). For example, when a master account (the
        originator) invites another account (the recipient) to join its organization, the two
        accounts exchange information as a series of handshake requests and responses.

         **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
         days after entering that state After that they are deleted.

        - **Id** *(string) --*

          The unique identifier (ID) of a handshake. The originating account creates the ID when it
          initiates the handshake.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
          "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of a handshake.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Parties** *(list) --*

          Information about the two accounts that are participating in the handshake.

          - *(dict) --*

            Identifies a participant in a handshake.

            - **Id** *(string) --*

              The unique identifier (ID) for the party.

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
              requires "h-" followed by from 8 to 32 lower-case letters or digits.

            - **Type** *(string) --*

              The type of party.

        - **State** *(string) --*

          The current state of the handshake. Use the state to trace the flow of the handshake
          through the process from its creation to its acceptance. The meaning of each of the valid
          values is as follows:

          * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
          handshake types) and not all recipients have responded yet. The request stays in this
          state until all recipients respond.

          * **OPEN** : This handshake was sent to multiple recipients (applicable to only some
          policy types) and all recipients have responded, allowing the originator to complete the
          handshake action.

          * **CANCELED** : This handshake is no longer active because it was canceled by the
          originating account.

          * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

          * **DECLINED** : This handshake is no longer active because it was declined by the
          recipient account.

          * **EXPIRED** : This handshake is no longer active because the originator did not receive
          a response of any kind from the recipient before the expiration time (15 days).

        - **RequestedTimestamp** *(datetime) --*

          The date and time that the handshake request was made.

        - **ExpirationTimestamp** *(datetime) --*

          The date and time that the handshake expires. If the recipient of the handshake request
          fails to respond before the specified date and time, the handshake becomes inactive and
          is no longer valid.

        - **Action** *(string) --*

          The type of handshake, indicating what action occurs when the recipient accepts the
          handshake. The following handshake types are supported:

          * **INVITE** : This type of handshake represents a request to join an organization. It is
          always sent from the master account to only non-member accounts.

          * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
          features in an organization. It is always sent from the master account to only *invited*
          member accounts. Created accounts do not receive this because those accounts were created
          by the organization's master account and approval is inferred.

          * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations
          service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It
          is sent only to the master account and signals the master that it can finalize the
          process to enable all features.

        - **Resources** *(list) --*

          Additional information that is needed to process the handshake.

          - *(dict) --*

            Contains additional data that is needed to process a handshake.

            - **Value** *(string) --*

              The information that is passed to the other party in the handshake. The format of the
              value string must match the requirements of the specified type.

            - **Type** *(string) --*

              The type of information being passed, specifying how the value is to be interpreted
              by the other party:

              * ``ACCOUNT`` - Specifies an AWS account ID number.

              * ``ORGANIZATION`` - Specifies an organization ID number.

              * ``EMAIL`` - Specifies the email address that is associated with the account that
              receives the handshake.

              * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
              Included as information about an organization.

              * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
              information about an organization.

              * ``NOTES`` - Additional text provided by the handshake initiator and intended for
              the recipient to read.

            - **Resources** *(list) --*

              When needed, contains an additional array of ``HandshakeResource`` objects.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef = TypedDict(
    "_ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef(
    _ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef
):
    """
    Type definition for `ClientListOrganizationalUnitsForParentResponse` `OrganizationalUnits`

    Contains details about an organizational unit (OU). An OU is a container of AWS accounts
    within a root of an organization. Policies that are attached to an OU apply to all accounts
    contained in that OU and in any child OUs.

    - **Id** *(string) --*

      The unique identifier (ID) associated with this OU.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
      string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of
      the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional
      lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of this OU.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of this OU.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.
    """


_ClientListOrganizationalUnitsForParentResponseTypeDef = TypedDict(
    "_ClientListOrganizationalUnitsForParentResponseTypeDef",
    {
        "OrganizationalUnits": List[
            ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListOrganizationalUnitsForParentResponseTypeDef(
    _ClientListOrganizationalUnitsForParentResponseTypeDef
):
    """
    Type definition for `ClientListOrganizationalUnitsForParent` `Response`

    - **OrganizationalUnits** *(list) --*

      A list of the OUs in the specified root or parent OU.

      - *(dict) --*

        Contains details about an organizational unit (OU). An OU is a container of AWS accounts
        within a root of an organization. Policies that are attached to an OU apply to all accounts
        contained in that OU and in any child OUs.

        - **Id** *(string) --*

          The unique identifier (ID) associated with this OU.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
          string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of
          the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional
          lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of this OU.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of this OU.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListParentsResponseParentsTypeDef = TypedDict(
    "_ClientListParentsResponseParentsTypeDef", {"Id": str, "Type": str}, total=False
)


class ClientListParentsResponseParentsTypeDef(_ClientListParentsResponseParentsTypeDef):
    """
    Type definition for `ClientListParentsResponse` `Parents`

    Contains information about either a root or an organizational unit (OU) that can contain
    OUs or accounts in an organization.

    - **Id** *(string) --*

      The unique identifier (ID) of the parent entity.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires
      one of the following:

      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or
      digits.

      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
      lower-case letters or digits (the ID of the root that the OU is in) followed by a second
      "-" dash and from 8 to 32 additional lower-case letters or digits.

    - **Type** *(string) --*

      The type of the parent entity.
    """


_ClientListParentsResponseTypeDef = TypedDict(
    "_ClientListParentsResponseTypeDef",
    {"Parents": List[ClientListParentsResponseParentsTypeDef], "NextToken": str},
    total=False,
)


class ClientListParentsResponseTypeDef(_ClientListParentsResponseTypeDef):
    """
    Type definition for `ClientListParents` `Response`

    - **Parents** *(list) --*

      A list of parents for the specified child account or OU.

      - *(dict) --*

        Contains information about either a root or an organizational unit (OU) that can contain
        OUs or accounts in an organization.

        - **Id** *(string) --*

          The unique identifier (ID) of the parent entity.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires
          one of the following:

          * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or
          digits.

          * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
          lower-case letters or digits (the ID of the root that the OU is in) followed by a second
          "-" dash and from 8 to 32 additional lower-case letters or digits.

        - **Type** *(string) --*

          The type of the parent entity.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListPoliciesForTargetResponsePoliciesTypeDef = TypedDict(
    "_ClientListPoliciesForTargetResponsePoliciesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "AwsManaged": bool,
    },
    total=False,
)


class ClientListPoliciesForTargetResponsePoliciesTypeDef(
    _ClientListPoliciesForTargetResponsePoliciesTypeDef
):
    """
    Type definition for `ClientListPoliciesForTargetResponse` `Policies`

    Contains information about a policy, but does not include the content. To see the content
    of a policy, see  DescribePolicy .

    - **Id** *(string) --*

      The unique identifier (ID) of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
      "p-" followed by from 8 to 128 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the policy.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Description** *(string) --*

      The description of the policy.

    - **Type** *(string) --*

      The type of policy.

    - **AwsManaged** *(boolean) --*

      A boolean value that indicates whether the specified policy is an AWS managed policy. If
      true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
    """


_ClientListPoliciesForTargetResponseTypeDef = TypedDict(
    "_ClientListPoliciesForTargetResponseTypeDef",
    {
        "Policies": List[ClientListPoliciesForTargetResponsePoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListPoliciesForTargetResponseTypeDef(
    _ClientListPoliciesForTargetResponseTypeDef
):
    """
    Type definition for `ClientListPoliciesForTarget` `Response`

    - **Policies** *(list) --*

      The list of policies that match the criteria in the request.

      - *(dict) --*

        Contains information about a policy, but does not include the content. To see the content
        of a policy, see  DescribePolicy .

        - **Id** *(string) --*

          The unique identifier (ID) of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
          "p-" followed by from 8 to 128 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the policy.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Description** *(string) --*

          The description of the policy.

        - **Type** *(string) --*

          The type of policy.

        - **AwsManaged** *(boolean) --*

          A boolean value that indicates whether the specified policy is an AWS managed policy. If
          true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListPoliciesResponsePoliciesTypeDef = TypedDict(
    "_ClientListPoliciesResponsePoliciesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "AwsManaged": bool,
    },
    total=False,
)


class ClientListPoliciesResponsePoliciesTypeDef(
    _ClientListPoliciesResponsePoliciesTypeDef
):
    """
    Type definition for `ClientListPoliciesResponse` `Policies`

    Contains information about a policy, but does not include the content. To see the content
    of a policy, see  DescribePolicy .

    - **Id** *(string) --*

      The unique identifier (ID) of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
      "p-" followed by from 8 to 128 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the policy.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Description** *(string) --*

      The description of the policy.

    - **Type** *(string) --*

      The type of policy.

    - **AwsManaged** *(boolean) --*

      A boolean value that indicates whether the specified policy is an AWS managed policy. If
      true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
    """


_ClientListPoliciesResponseTypeDef = TypedDict(
    "_ClientListPoliciesResponseTypeDef",
    {"Policies": List[ClientListPoliciesResponsePoliciesTypeDef], "NextToken": str},
    total=False,
)


class ClientListPoliciesResponseTypeDef(_ClientListPoliciesResponseTypeDef):
    """
    Type definition for `ClientListPolicies` `Response`

    - **Policies** *(list) --*

      A list of policies that match the filter criteria in the request. The output list doesn't
      include the policy contents. To see the content for a policy, see  DescribePolicy .

      - *(dict) --*

        Contains information about a policy, but does not include the content. To see the content
        of a policy, see  DescribePolicy .

        - **Id** *(string) --*

          The unique identifier (ID) of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
          "p-" followed by from 8 to 128 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the policy.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Description** *(string) --*

          The description of the policy.

        - **Type** *(string) --*

          The type of policy.

        - **AwsManaged** *(boolean) --*

          A boolean value that indicates whether the specified policy is an AWS managed policy. If
          true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListRootsResponseRootsPolicyTypesTypeDef = TypedDict(
    "_ClientListRootsResponseRootsPolicyTypesTypeDef",
    {"Type": str, "Status": str},
    total=False,
)


class ClientListRootsResponseRootsPolicyTypesTypeDef(
    _ClientListRootsResponseRootsPolicyTypesTypeDef
):
    """
    Type definition for `ClientListRootsResponseRoots` `PolicyTypes`

    Contains information about a policy type and its status in the associated root.

    - **Type** *(string) --*

      The name of the policy type.

    - **Status** *(string) --*

      The status of the policy type as it relates to the associated root. To attach a
      policy of the specified type to a root or to an OU or account in that root, it must
      be available in the organization and enabled for that root.
    """


_ClientListRootsResponseRootsTypeDef = TypedDict(
    "_ClientListRootsResponseRootsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ClientListRootsResponseRootsPolicyTypesTypeDef],
    },
    total=False,
)


class ClientListRootsResponseRootsTypeDef(_ClientListRootsResponseRootsTypeDef):
    """
    Type definition for `ClientListRootsResponse` `Roots`

    Contains details about a root. A root is a top-level parent node in the hierarchy of an
    organization that can contain organizational units (OUs) and accounts. Every root contains
    every AWS account in the organization. Each root enables the accounts to be organized in a
    different way and to have different policy types enabled for use in that root.

    - **Id** *(string) --*

      The unique identifier (ID) for the root.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires
      "r-" followed by from 4 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the root.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the root.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **PolicyTypes** *(list) --*

      The types of policies that are currently enabled for the root and therefore can be
      attached to the root or to its OUs or accounts.

      .. note::

        Even if a policy type is shown as available in the organization, you can separately
        enable and disable them at the root level by using  EnablePolicyType and
        DisablePolicyType . Use  DescribeOrganization to see the availability of the policy
        types in that organization.

      - *(dict) --*

        Contains information about a policy type and its status in the associated root.

        - **Type** *(string) --*

          The name of the policy type.

        - **Status** *(string) --*

          The status of the policy type as it relates to the associated root. To attach a
          policy of the specified type to a root or to an OU or account in that root, it must
          be available in the organization and enabled for that root.
    """


_ClientListRootsResponseTypeDef = TypedDict(
    "_ClientListRootsResponseTypeDef",
    {"Roots": List[ClientListRootsResponseRootsTypeDef], "NextToken": str},
    total=False,
)


class ClientListRootsResponseTypeDef(_ClientListRootsResponseTypeDef):
    """
    Type definition for `ClientListRoots` `Response`

    - **Roots** *(list) --*

      A list of roots that are defined in an organization.

      - *(dict) --*

        Contains details about a root. A root is a top-level parent node in the hierarchy of an
        organization that can contain organizational units (OUs) and accounts. Every root contains
        every AWS account in the organization. Each root enables the accounts to be organized in a
        different way and to have different policy types enabled for use in that root.

        - **Id** *(string) --*

          The unique identifier (ID) for the root.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires
          "r-" followed by from 4 to 32 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the root.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the root.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **PolicyTypes** *(list) --*

          The types of policies that are currently enabled for the root and therefore can be
          attached to the root or to its OUs or accounts.

          .. note::

            Even if a policy type is shown as available in the organization, you can separately
            enable and disable them at the root level by using  EnablePolicyType and
            DisablePolicyType . Use  DescribeOrganization to see the availability of the policy
            types in that organization.

          - *(dict) --*

            Contains information about a policy type and its status in the associated root.

            - **Type** *(string) --*

              The name of the policy type.

            - **Status** *(string) --*

              The status of the policy type as it relates to the associated root. To attach a
              policy of the specified type to a root or to an OU or account in that root, it must
              be available in the organization and enabled for that root.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

    A custom key-value pair associated with a resource such as an account within your
    organization.

    - **Key** *(string) --*

      The key identifier, or name, of the tag.

    - **Value** *(string) --*

      The string value that's associated with the key of the tag. You can set the value of a
      tag to an empty string, but you can't set the value of a tag to null.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(list) --*

      The tags that are assigned to the resource.

      - *(dict) --*

        A custom key-value pair associated with a resource such as an account within your
        organization.

        - **Key** *(string) --*

          The key identifier, or name, of the tag.

        - **Value** *(string) --*

          The string value that's associated with the key of the tag. You can set the value of a
          tag to an empty string, but you can't set the value of a tag to null.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientListTargetsForPolicyResponseTargetsTypeDef = TypedDict(
    "_ClientListTargetsForPolicyResponseTargetsTypeDef",
    {"TargetId": str, "Arn": str, "Name": str, "Type": str},
    total=False,
)


class ClientListTargetsForPolicyResponseTargetsTypeDef(
    _ClientListTargetsForPolicyResponseTargetsTypeDef
):
    """
    Type definition for `ClientListTargetsForPolicyResponse` `Targets`

    Contains information about a root, OU, or account that a policy is attached to.

    - **TargetId** *(string) --*

      The unique identifier (ID) of the policy target.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires
      one of the following:

      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or
      digits.

      * Account: a string that consists of exactly 12 digits.

      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
      lower-case letters or digits (the ID of the root that the OU is in) followed by a second
      "-" dash and from 8 to 32 additional lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the policy target.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the policy target.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Type** *(string) --*

      The type of the policy target.
    """


_ClientListTargetsForPolicyResponseTypeDef = TypedDict(
    "_ClientListTargetsForPolicyResponseTypeDef",
    {
        "Targets": List[ClientListTargetsForPolicyResponseTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTargetsForPolicyResponseTypeDef(
    _ClientListTargetsForPolicyResponseTypeDef
):
    """
    Type definition for `ClientListTargetsForPolicy` `Response`

    - **Targets** *(list) --*

      A list of structures, each of which contains details about one of the entities to which the
      specified policy is attached.

      - *(dict) --*

        Contains information about a root, OU, or account that a policy is attached to.

        - **TargetId** *(string) --*

          The unique identifier (ID) of the policy target.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires
          one of the following:

          * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or
          digits.

          * Account: a string that consists of exactly 12 digits.

          * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
          lower-case letters or digits (the ID of the root that the OU is in) followed by a second
          "-" dash and from 8 to 32 additional lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the policy target.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the policy target.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Type** *(string) --*

          The type of the policy target.

    - **NextToken** *(string) --*

      If present, this value indicates that there is more output available than is included in the
      current response. Use this value in the ``NextToken`` request parameter in a subsequent call
      to the operation to get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back as ``null`` .
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    A custom key-value pair associated with a resource such as an account within your organization.

    - **Key** *(string) --* **[REQUIRED]**

      The key identifier, or name, of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      The string value that's associated with the key of the tag. You can set the value of a tag to
      an empty string, but you can't set the value of a tag to null.
    """


_ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef = TypedDict(
    "_ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef(
    _ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef
):
    """
    Type definition for `ClientUpdateOrganizationalUnitResponse` `OrganizationalUnit`

    A structure that contains the details about the specified OU, including its new name.

    - **Id** *(string) --*

      The unique identifier (ID) associated with this OU.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
      string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the
      root that contains the OU) followed by a second "-" dash and from 8 to 32 additional
      lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of this OU.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of this OU.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.
    """


_ClientUpdateOrganizationalUnitResponseTypeDef = TypedDict(
    "_ClientUpdateOrganizationalUnitResponseTypeDef",
    {
        "OrganizationalUnit": ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef
    },
    total=False,
)


class ClientUpdateOrganizationalUnitResponseTypeDef(
    _ClientUpdateOrganizationalUnitResponseTypeDef
):
    """
    Type definition for `ClientUpdateOrganizationalUnit` `Response`

    - **OrganizationalUnit** *(dict) --*

      A structure that contains the details about the specified OU, including its new name.

      - **Id** *(string) --*

        The unique identifier (ID) associated with this OU.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
        string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the
        root that contains the OU) followed by a second "-" dash and from 8 to 32 additional
        lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of this OU.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Name** *(string) --*

        The friendly name of this OU.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
        parameter is a string of any of the characters in the ASCII character range.
    """


_ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef = TypedDict(
    "_ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "AwsManaged": bool,
    },
    total=False,
)


class ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef(
    _ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef
):
    """
    Type definition for `ClientUpdatePolicyResponsePolicy` `PolicySummary`

    A structure that contains additional details about the policy.

    - **Id** *(string) --*

      The unique identifier (ID) of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
      "p-" followed by from 8 to 128 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the policy.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Description** *(string) --*

      The description of the policy.

    - **Type** *(string) --*

      The type of policy.

    - **AwsManaged** *(boolean) --*

      A boolean value that indicates whether the specified policy is an AWS managed policy. If
      true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
    """


_ClientUpdatePolicyResponsePolicyTypeDef = TypedDict(
    "_ClientUpdatePolicyResponsePolicyTypeDef",
    {
        "PolicySummary": ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef,
        "Content": str,
    },
    total=False,
)


class ClientUpdatePolicyResponsePolicyTypeDef(_ClientUpdatePolicyResponsePolicyTypeDef):
    """
    Type definition for `ClientUpdatePolicyResponse` `Policy`

    A structure that contains details about the updated policy, showing the requested changes.

    - **PolicySummary** *(dict) --*

      A structure that contains additional details about the policy.

      - **Id** *(string) --*

        The unique identifier (ID) of the policy.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
        "p-" followed by from 8 to 128 lower-case letters or digits.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the policy.

        For more information about ARNs in Organizations, see `ARN Formats Supported by
        Organizations
        <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
        in the *AWS Organizations User Guide* .

      - **Name** *(string) --*

        The friendly name of the policy.

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
        parameter is a string of any of the characters in the ASCII character range.

      - **Description** *(string) --*

        The description of the policy.

      - **Type** *(string) --*

        The type of policy.

      - **AwsManaged** *(boolean) --*

        A boolean value that indicates whether the specified policy is an AWS managed policy. If
        true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

    - **Content** *(string) --*

      The text content of the policy.
    """


_ClientUpdatePolicyResponseTypeDef = TypedDict(
    "_ClientUpdatePolicyResponseTypeDef",
    {"Policy": ClientUpdatePolicyResponsePolicyTypeDef},
    total=False,
)


class ClientUpdatePolicyResponseTypeDef(_ClientUpdatePolicyResponseTypeDef):
    """
    Type definition for `ClientUpdatePolicy` `Response`

    - **Policy** *(dict) --*

      A structure that contains details about the updated policy, showing the requested changes.

      - **PolicySummary** *(dict) --*

        A structure that contains additional details about the policy.

        - **Id** *(string) --*

          The unique identifier (ID) of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
          "p-" followed by from 8 to 128 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the policy.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Description** *(string) --*

          The description of the policy.

        - **Type** *(string) --*

          The type of policy.

        - **AwsManaged** *(boolean) --*

          A boolean value that indicates whether the specified policy is an AWS managed policy. If
          true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

      - **Content** *(string) --*

        The text content of the policy.
    """


_ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef(
    _ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAWSServiceAccessForOrganizationPaginate` `PaginationConfig`

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


_ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef = TypedDict(
    "_ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef",
    {"ServicePrincipal": str, "DateEnabled": datetime},
    total=False,
)


class ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef(
    _ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef
):
    """
    Type definition for `ListAWSServiceAccessForOrganizationPaginateResponse` `EnabledServicePrincipals`

    A structure that contains details of a service principal that is enabled to integrate with
    AWS Organizations.

    - **ServicePrincipal** *(string) --*

      The name of the service principal. This is typically in the form of a URL, such as: ``
      *servicename* .amazonaws.com`` .

    - **DateEnabled** *(datetime) --*

      The date that the service principal was enabled for integration with AWS Organizations.
    """


_ListAWSServiceAccessForOrganizationPaginateResponseTypeDef = TypedDict(
    "_ListAWSServiceAccessForOrganizationPaginateResponseTypeDef",
    {
        "EnabledServicePrincipals": List[
            ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef
        ]
    },
    total=False,
)


class ListAWSServiceAccessForOrganizationPaginateResponseTypeDef(
    _ListAWSServiceAccessForOrganizationPaginateResponseTypeDef
):
    """
    Type definition for `ListAWSServiceAccessForOrganizationPaginate` `Response`

    - **EnabledServicePrincipals** *(list) --*

      A list of the service principals for the services that are enabled to integrate with your
      organization. Each principal is a structure that includes the name and the date that it was
      enabled for integration with AWS Organizations.

      - *(dict) --*

        A structure that contains details of a service principal that is enabled to integrate with
        AWS Organizations.

        - **ServicePrincipal** *(string) --*

          The name of the service principal. This is typically in the form of a URL, such as: ``
          *servicename* .amazonaws.com`` .

        - **DateEnabled** *(datetime) --*

          The date that the service principal was enabled for integration with AWS Organizations.
    """


_ListAccountsForParentPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccountsForParentPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccountsForParentPaginatePaginationConfigTypeDef(
    _ListAccountsForParentPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAccountsForParentPaginate` `PaginationConfig`

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


_ListAccountsForParentPaginateResponseAccountsTypeDef = TypedDict(
    "_ListAccountsForParentPaginateResponseAccountsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": str,
        "JoinedMethod": str,
        "JoinedTimestamp": datetime,
    },
    total=False,
)


class ListAccountsForParentPaginateResponseAccountsTypeDef(
    _ListAccountsForParentPaginateResponseAccountsTypeDef
):
    """
    Type definition for `ListAccountsForParentPaginateResponse` `Accounts`

    Contains information about an AWS account that is a member of an organization.

    - **Id** *(string) --*

      The unique identifier (ID) of the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the account.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Email** *(string) --*

      The email address associated with the AWS account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of
      characters that represents a standard Internet email address.

    - **Name** *(string) --*

      The friendly name of the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Status** *(string) --*

      The status of the account in the organization.

    - **JoinedMethod** *(string) --*

      The method by which the account joined the organization.

    - **JoinedTimestamp** *(datetime) --*

      The date the account became a part of the organization.
    """


_ListAccountsForParentPaginateResponseTypeDef = TypedDict(
    "_ListAccountsForParentPaginateResponseTypeDef",
    {"Accounts": List[ListAccountsForParentPaginateResponseAccountsTypeDef]},
    total=False,
)


class ListAccountsForParentPaginateResponseTypeDef(
    _ListAccountsForParentPaginateResponseTypeDef
):
    """
    Type definition for `ListAccountsForParentPaginate` `Response`

    - **Accounts** *(list) --*

      A list of the accounts in the specified root or OU.

      - *(dict) --*

        Contains information about an AWS account that is a member of an organization.

        - **Id** *(string) --*

          The unique identifier (ID) of the account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
          exactly 12 digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the account.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Email** *(string) --*

          The email address associated with the AWS account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of
          characters that represents a standard Internet email address.

        - **Name** *(string) --*

          The friendly name of the account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Status** *(string) --*

          The status of the account in the organization.

        - **JoinedMethod** *(string) --*

          The method by which the account joined the organization.

        - **JoinedTimestamp** *(datetime) --*

          The date the account became a part of the organization.
    """


_ListAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccountsPaginatePaginationConfigTypeDef(
    _ListAccountsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAccountsPaginate` `PaginationConfig`

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


_ListAccountsPaginateResponseAccountsTypeDef = TypedDict(
    "_ListAccountsPaginateResponseAccountsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": str,
        "JoinedMethod": str,
        "JoinedTimestamp": datetime,
    },
    total=False,
)


class ListAccountsPaginateResponseAccountsTypeDef(
    _ListAccountsPaginateResponseAccountsTypeDef
):
    """
    Type definition for `ListAccountsPaginateResponse` `Accounts`

    Contains information about an AWS account that is a member of an organization.

    - **Id** *(string) --*

      The unique identifier (ID) of the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the account.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Email** *(string) --*

      The email address associated with the AWS account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of
      characters that represents a standard Internet email address.

    - **Name** *(string) --*

      The friendly name of the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Status** *(string) --*

      The status of the account in the organization.

    - **JoinedMethod** *(string) --*

      The method by which the account joined the organization.

    - **JoinedTimestamp** *(datetime) --*

      The date the account became a part of the organization.
    """


_ListAccountsPaginateResponseTypeDef = TypedDict(
    "_ListAccountsPaginateResponseTypeDef",
    {"Accounts": List[ListAccountsPaginateResponseAccountsTypeDef]},
    total=False,
)


class ListAccountsPaginateResponseTypeDef(_ListAccountsPaginateResponseTypeDef):
    """
    Type definition for `ListAccountsPaginate` `Response`

    - **Accounts** *(list) --*

      A list of objects in the organization.

      - *(dict) --*

        Contains information about an AWS account that is a member of an organization.

        - **Id** *(string) --*

          The unique identifier (ID) of the account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
          exactly 12 digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the account.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Email** *(string) --*

          The email address associated with the AWS account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of
          characters that represents a standard Internet email address.

        - **Name** *(string) --*

          The friendly name of the account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Status** *(string) --*

          The status of the account in the organization.

        - **JoinedMethod** *(string) --*

          The method by which the account joined the organization.

        - **JoinedTimestamp** *(datetime) --*

          The date the account became a part of the organization.
    """


_ListChildrenPaginatePaginationConfigTypeDef = TypedDict(
    "_ListChildrenPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListChildrenPaginatePaginationConfigTypeDef(
    _ListChildrenPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListChildrenPaginate` `PaginationConfig`

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


_ListChildrenPaginateResponseChildrenTypeDef = TypedDict(
    "_ListChildrenPaginateResponseChildrenTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ListChildrenPaginateResponseChildrenTypeDef(
    _ListChildrenPaginateResponseChildrenTypeDef
):
    """
    Type definition for `ListChildrenPaginateResponse` `Children`

    Contains a list of child entities, either OUs or accounts.

    - **Id** *(string) --*

      The unique identifier (ID) of this child entity.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires
      one of the following:

      * Account: a string that consists of exactly 12 digits.

      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
      lower-case letters or digits (the ID of the root that contains the OU) followed by a
      second "-" dash and from 8 to 32 additional lower-case letters or digits.

    - **Type** *(string) --*

      The type of this child entity.
    """


_ListChildrenPaginateResponseTypeDef = TypedDict(
    "_ListChildrenPaginateResponseTypeDef",
    {"Children": List[ListChildrenPaginateResponseChildrenTypeDef]},
    total=False,
)


class ListChildrenPaginateResponseTypeDef(_ListChildrenPaginateResponseTypeDef):
    """
    Type definition for `ListChildrenPaginate` `Response`

    - **Children** *(list) --*

      The list of children of the specified parent container.

      - *(dict) --*

        Contains a list of child entities, either OUs or accounts.

        - **Id** *(string) --*

          The unique identifier (ID) of this child entity.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires
          one of the following:

          * Account: a string that consists of exactly 12 digits.

          * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
          lower-case letters or digits (the ID of the root that contains the OU) followed by a
          second "-" dash and from 8 to 32 additional lower-case letters or digits.

        - **Type** *(string) --*

          The type of this child entity.
    """


_ListCreateAccountStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCreateAccountStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCreateAccountStatusPaginatePaginationConfigTypeDef(
    _ListCreateAccountStatusPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCreateAccountStatusPaginate` `PaginationConfig`

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


_ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef = TypedDict(
    "_ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": str,
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": str,
    },
    total=False,
)


class ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef(
    _ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef
):
    """
    Type definition for `ListCreateAccountStatusPaginateResponse` `CreateAccountStatuses`

    Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an
    AWS account or an AWS GovCloud (US) account in an organization.

    - **Id** *(string) --*

      The unique identifier (ID) that references this request. You get this value from the
      response of the initial  CreateAccount request to create the account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID
      string requires "car-" followed by from 8 to 32 lower-case letters or digits.

    - **AccountName** *(string) --*

      The account name given to the account when it was created.

    - **State** *(string) --*

      The status of the request.

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the request was made for the account creation.

    - **CompletedTimestamp** *(datetime) --*

      The date and time that the account was created and the request completed.

    - **AccountId** *(string) --*

      If the account was created successfully, the unique identifier (ID) of the new account.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
      exactly 12 digits.

    - **GovCloudAccountId** *(string) --*

      If the account was created successfully, the unique identifier (ID) of the new account in
      the AWS GovCloud (US) Region.

    - **FailureReason** *(string) --*

      If the request failed, a description of the reason for the failure.

      * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the
      limit on the number of accounts in your organization.

      * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with
      that email address already exists.

      * GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not
      be created because this Region already includes an account with that email address.

      * INVALID_ADDRESS: The account could not be created because the address you provided is
      not valid.

      * INVALID_EMAIL: The account could not be created because the email address you provided
      is not valid.

      * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try
      again later. If the problem persists, contact Customer Support.
    """


_ListCreateAccountStatusPaginateResponseTypeDef = TypedDict(
    "_ListCreateAccountStatusPaginateResponseTypeDef",
    {
        "CreateAccountStatuses": List[
            ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef
        ]
    },
    total=False,
)


class ListCreateAccountStatusPaginateResponseTypeDef(
    _ListCreateAccountStatusPaginateResponseTypeDef
):
    """
    Type definition for `ListCreateAccountStatusPaginate` `Response`

    - **CreateAccountStatuses** *(list) --*

      A list of objects with details about the requests. Certain elements, such as the accountId
      number, are present in the output only after the account has been successfully created.

      - *(dict) --*

        Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an
        AWS account or an AWS GovCloud (US) account in an organization.

        - **Id** *(string) --*

          The unique identifier (ID) that references this request. You get this value from the
          response of the initial  CreateAccount request to create the account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID
          string requires "car-" followed by from 8 to 32 lower-case letters or digits.

        - **AccountName** *(string) --*

          The account name given to the account when it was created.

        - **State** *(string) --*

          The status of the request.

        - **RequestedTimestamp** *(datetime) --*

          The date and time that the request was made for the account creation.

        - **CompletedTimestamp** *(datetime) --*

          The date and time that the account was created and the request completed.

        - **AccountId** *(string) --*

          If the account was created successfully, the unique identifier (ID) of the new account.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
          exactly 12 digits.

        - **GovCloudAccountId** *(string) --*

          If the account was created successfully, the unique identifier (ID) of the new account in
          the AWS GovCloud (US) Region.

        - **FailureReason** *(string) --*

          If the request failed, a description of the reason for the failure.

          * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the
          limit on the number of accounts in your organization.

          * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with
          that email address already exists.

          * GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not
          be created because this Region already includes an account with that email address.

          * INVALID_ADDRESS: The account could not be created because the address you provided is
          not valid.

          * INVALID_EMAIL: The account could not be created because the email address you provided
          is not valid.

          * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try
          again later. If the problem persists, contact Customer Support.
    """


_ListHandshakesForAccountPaginateFilterTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginateFilterTypeDef",
    {"ActionType": str, "ParentHandshakeId": str},
    total=False,
)


class ListHandshakesForAccountPaginateFilterTypeDef(
    _ListHandshakesForAccountPaginateFilterTypeDef
):
    """
    Type definition for `ListHandshakesForAccountPaginate` `Filter`

    Filters the handshakes that you want included in the response. The default is all types. Use the
    ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` ,
    ``ENABLE_ALL_FEATURES`` , or ``APPROVE_ALL_FEATURES`` . Alternatively, for the
    ``ENABLE_ALL_FEATURES`` handshake that generates a separate child handshake for each member
    account, you can specify ``ParentHandshakeId`` to see only the handshakes that were generated by
    that parent request.

    - **ActionType** *(string) --*

      Specifies the type of handshake action.

      If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .

    - **ParentHandshakeId** *(string) --*

      Specifies the parent handshake. Only used for handshake types that are a child of another type.

      If you specify ``ParentHandshakeId`` , you cannot also specify ``ActionType`` .

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-"
      followed by from 8 to 32 lower-case letters or digits.
    """


_ListHandshakesForAccountPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHandshakesForAccountPaginatePaginationConfigTypeDef(
    _ListHandshakesForAccountPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListHandshakesForAccountPaginate` `PaginationConfig`

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


_ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef(
    _ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef
):
    """
    Type definition for `ListHandshakesForAccountPaginateResponseHandshakes` `Parties`

    Identifies a participant in a handshake.

    - **Id** *(string) --*

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
      requires "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --*

      The type of party.
    """


_ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef",
    {"Value": str, "Type": str, "Resources": List[Any]},
    total=False,
)


class ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef(
    _ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef
):
    """
    Type definition for `ListHandshakesForAccountPaginateResponseHandshakes` `Resources`

    Contains additional data that is needed to process a handshake.

    - **Value** *(string) --*

      The information that is passed to the other party in the handshake. The format of the
      value string must match the requirements of the specified type.

    - **Type** *(string) --*

      The type of information being passed, specifying how the value is to be interpreted
      by the other party:

      * ``ACCOUNT`` - Specifies an AWS account ID number.

      * ``ORGANIZATION`` - Specifies an organization ID number.

      * ``EMAIL`` - Specifies the email address that is associated with the account that
      receives the handshake.

      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
      Included as information about an organization.

      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
      information about an organization.

      * ``NOTES`` - Additional text provided by the handshake initiator and intended for
      the recipient to read.

    - **Resources** *(list) --*

      When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ListHandshakesForAccountPaginateResponseHandshakesTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginateResponseHandshakesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[
            ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef
        ],
        "State": str,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": str,
        "Resources": List[
            ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef
        ],
    },
    total=False,
)


class ListHandshakesForAccountPaginateResponseHandshakesTypeDef(
    _ListHandshakesForAccountPaginateResponseHandshakesTypeDef
):
    """
    Type definition for `ListHandshakesForAccountPaginateResponse` `Handshakes`

    Contains information that must be exchanged to securely establish a relationship between
    two accounts (an *originator* and a *recipient* ). For example, when a master account (the
    originator) invites another account (the recipient) to join its organization, the two
    accounts exchange information as a series of handshake requests and responses.

     **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
     days after entering that state After that they are deleted.

    - **Id** *(string) --*

      The unique identifier (ID) of a handshake. The originating account creates the ID when it
      initiates the handshake.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
      "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of a handshake.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Parties** *(list) --*

      Information about the two accounts that are participating in the handshake.

      - *(dict) --*

        Identifies a participant in a handshake.

        - **Id** *(string) --*

          The unique identifier (ID) for the party.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
          requires "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Type** *(string) --*

          The type of party.

    - **State** *(string) --*

      The current state of the handshake. Use the state to trace the flow of the handshake
      through the process from its creation to its acceptance. The meaning of each of the valid
      values is as follows:

      * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
      handshake types) and not all recipients have responded yet. The request stays in this
      state until all recipients respond.

      * **OPEN** : This handshake was sent to multiple recipients (applicable to only some
      policy types) and all recipients have responded, allowing the originator to complete the
      handshake action.

      * **CANCELED** : This handshake is no longer active because it was canceled by the
      originating account.

      * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

      * **DECLINED** : This handshake is no longer active because it was declined by the
      recipient account.

      * **EXPIRED** : This handshake is no longer active because the originator did not receive
      a response of any kind from the recipient before the expiration time (15 days).

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the handshake request was made.

    - **ExpirationTimestamp** *(datetime) --*

      The date and time that the handshake expires. If the recipient of the handshake request
      fails to respond before the specified date and time, the handshake becomes inactive and
      is no longer valid.

    - **Action** *(string) --*

      The type of handshake, indicating what action occurs when the recipient accepts the
      handshake. The following handshake types are supported:

      * **INVITE** : This type of handshake represents a request to join an organization. It is
      always sent from the master account to only non-member accounts.

      * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
      features in an organization. It is always sent from the master account to only *invited*
      member accounts. Created accounts do not receive this because those accounts were created
      by the organization's master account and approval is inferred.

      * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations
      service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It
      is sent only to the master account and signals the master that it can finalize the
      process to enable all features.

    - **Resources** *(list) --*

      Additional information that is needed to process the handshake.

      - *(dict) --*

        Contains additional data that is needed to process a handshake.

        - **Value** *(string) --*

          The information that is passed to the other party in the handshake. The format of the
          value string must match the requirements of the specified type.

        - **Type** *(string) --*

          The type of information being passed, specifying how the value is to be interpreted
          by the other party:

          * ``ACCOUNT`` - Specifies an AWS account ID number.

          * ``ORGANIZATION`` - Specifies an organization ID number.

          * ``EMAIL`` - Specifies the email address that is associated with the account that
          receives the handshake.

          * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
          Included as information about an organization.

          * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
          information about an organization.

          * ``NOTES`` - Additional text provided by the handshake initiator and intended for
          the recipient to read.

        - **Resources** *(list) --*

          When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ListHandshakesForAccountPaginateResponseTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginateResponseTypeDef",
    {"Handshakes": List[ListHandshakesForAccountPaginateResponseHandshakesTypeDef]},
    total=False,
)


class ListHandshakesForAccountPaginateResponseTypeDef(
    _ListHandshakesForAccountPaginateResponseTypeDef
):
    """
    Type definition for `ListHandshakesForAccountPaginate` `Response`

    - **Handshakes** *(list) --*

      A list of  Handshake objects with details about each of the handshakes that is associated
      with the specified account.

      - *(dict) --*

        Contains information that must be exchanged to securely establish a relationship between
        two accounts (an *originator* and a *recipient* ). For example, when a master account (the
        originator) invites another account (the recipient) to join its organization, the two
        accounts exchange information as a series of handshake requests and responses.

         **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
         days after entering that state After that they are deleted.

        - **Id** *(string) --*

          The unique identifier (ID) of a handshake. The originating account creates the ID when it
          initiates the handshake.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
          "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of a handshake.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Parties** *(list) --*

          Information about the two accounts that are participating in the handshake.

          - *(dict) --*

            Identifies a participant in a handshake.

            - **Id** *(string) --*

              The unique identifier (ID) for the party.

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
              requires "h-" followed by from 8 to 32 lower-case letters or digits.

            - **Type** *(string) --*

              The type of party.

        - **State** *(string) --*

          The current state of the handshake. Use the state to trace the flow of the handshake
          through the process from its creation to its acceptance. The meaning of each of the valid
          values is as follows:

          * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
          handshake types) and not all recipients have responded yet. The request stays in this
          state until all recipients respond.

          * **OPEN** : This handshake was sent to multiple recipients (applicable to only some
          policy types) and all recipients have responded, allowing the originator to complete the
          handshake action.

          * **CANCELED** : This handshake is no longer active because it was canceled by the
          originating account.

          * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

          * **DECLINED** : This handshake is no longer active because it was declined by the
          recipient account.

          * **EXPIRED** : This handshake is no longer active because the originator did not receive
          a response of any kind from the recipient before the expiration time (15 days).

        - **RequestedTimestamp** *(datetime) --*

          The date and time that the handshake request was made.

        - **ExpirationTimestamp** *(datetime) --*

          The date and time that the handshake expires. If the recipient of the handshake request
          fails to respond before the specified date and time, the handshake becomes inactive and
          is no longer valid.

        - **Action** *(string) --*

          The type of handshake, indicating what action occurs when the recipient accepts the
          handshake. The following handshake types are supported:

          * **INVITE** : This type of handshake represents a request to join an organization. It is
          always sent from the master account to only non-member accounts.

          * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
          features in an organization. It is always sent from the master account to only *invited*
          member accounts. Created accounts do not receive this because those accounts were created
          by the organization's master account and approval is inferred.

          * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations
          service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It
          is sent only to the master account and signals the master that it can finalize the
          process to enable all features.

        - **Resources** *(list) --*

          Additional information that is needed to process the handshake.

          - *(dict) --*

            Contains additional data that is needed to process a handshake.

            - **Value** *(string) --*

              The information that is passed to the other party in the handshake. The format of the
              value string must match the requirements of the specified type.

            - **Type** *(string) --*

              The type of information being passed, specifying how the value is to be interpreted
              by the other party:

              * ``ACCOUNT`` - Specifies an AWS account ID number.

              * ``ORGANIZATION`` - Specifies an organization ID number.

              * ``EMAIL`` - Specifies the email address that is associated with the account that
              receives the handshake.

              * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
              Included as information about an organization.

              * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
              information about an organization.

              * ``NOTES`` - Additional text provided by the handshake initiator and intended for
              the recipient to read.

            - **Resources** *(list) --*

              When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ListHandshakesForOrganizationPaginateFilterTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginateFilterTypeDef",
    {"ActionType": str, "ParentHandshakeId": str},
    total=False,
)


class ListHandshakesForOrganizationPaginateFilterTypeDef(
    _ListHandshakesForOrganizationPaginateFilterTypeDef
):
    """
    Type definition for `ListHandshakesForOrganizationPaginate` `Filter`

    A filter of the handshakes that you want included in the response. The default is all types. Use
    the ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` ,
    ``ENABLE-ALL-FEATURES`` , or ``APPROVE-ALL-FEATURES`` . Alternatively, for the
    ``ENABLE-ALL-FEATURES`` handshake that generates a separate child handshake for each member
    account, you can specify the ``ParentHandshakeId`` to see only the handshakes that were generated
    by that parent request.

    - **ActionType** *(string) --*

      Specifies the type of handshake action.

      If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .

    - **ParentHandshakeId** *(string) --*

      Specifies the parent handshake. Only used for handshake types that are a child of another type.

      If you specify ``ParentHandshakeId`` , you cannot also specify ``ActionType`` .

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-"
      followed by from 8 to 32 lower-case letters or digits.
    """


_ListHandshakesForOrganizationPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHandshakesForOrganizationPaginatePaginationConfigTypeDef(
    _ListHandshakesForOrganizationPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListHandshakesForOrganizationPaginate` `PaginationConfig`

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


_ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef",
    {"Id": str, "Type": str},
    total=False,
)


class ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef(
    _ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef
):
    """
    Type definition for `ListHandshakesForOrganizationPaginateResponseHandshakes` `Parties`

    Identifies a participant in a handshake.

    - **Id** *(string) --*

      The unique identifier (ID) for the party.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
      requires "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Type** *(string) --*

      The type of party.
    """


_ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef",
    {"Value": str, "Type": str, "Resources": List[Any]},
    total=False,
)


class ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef(
    _ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef
):
    """
    Type definition for `ListHandshakesForOrganizationPaginateResponseHandshakes` `Resources`

    Contains additional data that is needed to process a handshake.

    - **Value** *(string) --*

      The information that is passed to the other party in the handshake. The format of the
      value string must match the requirements of the specified type.

    - **Type** *(string) --*

      The type of information being passed, specifying how the value is to be interpreted
      by the other party:

      * ``ACCOUNT`` - Specifies an AWS account ID number.

      * ``ORGANIZATION`` - Specifies an organization ID number.

      * ``EMAIL`` - Specifies the email address that is associated with the account that
      receives the handshake.

      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
      Included as information about an organization.

      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
      information about an organization.

      * ``NOTES`` - Additional text provided by the handshake initiator and intended for
      the recipient to read.

    - **Resources** *(list) --*

      When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[
            ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef
        ],
        "State": str,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": str,
        "Resources": List[
            ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef
        ],
    },
    total=False,
)


class ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef(
    _ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef
):
    """
    Type definition for `ListHandshakesForOrganizationPaginateResponse` `Handshakes`

    Contains information that must be exchanged to securely establish a relationship between
    two accounts (an *originator* and a *recipient* ). For example, when a master account (the
    originator) invites another account (the recipient) to join its organization, the two
    accounts exchange information as a series of handshake requests and responses.

     **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
     days after entering that state After that they are deleted.

    - **Id** *(string) --*

      The unique identifier (ID) of a handshake. The originating account creates the ID when it
      initiates the handshake.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
      "h-" followed by from 8 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of a handshake.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Parties** *(list) --*

      Information about the two accounts that are participating in the handshake.

      - *(dict) --*

        Identifies a participant in a handshake.

        - **Id** *(string) --*

          The unique identifier (ID) for the party.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
          requires "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Type** *(string) --*

          The type of party.

    - **State** *(string) --*

      The current state of the handshake. Use the state to trace the flow of the handshake
      through the process from its creation to its acceptance. The meaning of each of the valid
      values is as follows:

      * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
      handshake types) and not all recipients have responded yet. The request stays in this
      state until all recipients respond.

      * **OPEN** : This handshake was sent to multiple recipients (applicable to only some
      policy types) and all recipients have responded, allowing the originator to complete the
      handshake action.

      * **CANCELED** : This handshake is no longer active because it was canceled by the
      originating account.

      * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

      * **DECLINED** : This handshake is no longer active because it was declined by the
      recipient account.

      * **EXPIRED** : This handshake is no longer active because the originator did not receive
      a response of any kind from the recipient before the expiration time (15 days).

    - **RequestedTimestamp** *(datetime) --*

      The date and time that the handshake request was made.

    - **ExpirationTimestamp** *(datetime) --*

      The date and time that the handshake expires. If the recipient of the handshake request
      fails to respond before the specified date and time, the handshake becomes inactive and
      is no longer valid.

    - **Action** *(string) --*

      The type of handshake, indicating what action occurs when the recipient accepts the
      handshake. The following handshake types are supported:

      * **INVITE** : This type of handshake represents a request to join an organization. It is
      always sent from the master account to only non-member accounts.

      * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
      features in an organization. It is always sent from the master account to only *invited*
      member accounts. Created accounts do not receive this because those accounts were created
      by the organization's master account and approval is inferred.

      * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations
      service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It
      is sent only to the master account and signals the master that it can finalize the
      process to enable all features.

    - **Resources** *(list) --*

      Additional information that is needed to process the handshake.

      - *(dict) --*

        Contains additional data that is needed to process a handshake.

        - **Value** *(string) --*

          The information that is passed to the other party in the handshake. The format of the
          value string must match the requirements of the specified type.

        - **Type** *(string) --*

          The type of information being passed, specifying how the value is to be interpreted
          by the other party:

          * ``ACCOUNT`` - Specifies an AWS account ID number.

          * ``ORGANIZATION`` - Specifies an organization ID number.

          * ``EMAIL`` - Specifies the email address that is associated with the account that
          receives the handshake.

          * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
          Included as information about an organization.

          * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
          information about an organization.

          * ``NOTES`` - Additional text provided by the handshake initiator and intended for
          the recipient to read.

        - **Resources** *(list) --*

          When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ListHandshakesForOrganizationPaginateResponseTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginateResponseTypeDef",
    {
        "Handshakes": List[
            ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef
        ]
    },
    total=False,
)


class ListHandshakesForOrganizationPaginateResponseTypeDef(
    _ListHandshakesForOrganizationPaginateResponseTypeDef
):
    """
    Type definition for `ListHandshakesForOrganizationPaginate` `Response`

    - **Handshakes** *(list) --*

      A list of  Handshake objects with details about each of the handshakes that are associated
      with an organization.

      - *(dict) --*

        Contains information that must be exchanged to securely establish a relationship between
        two accounts (an *originator* and a *recipient* ). For example, when a master account (the
        originator) invites another account (the recipient) to join its organization, the two
        accounts exchange information as a series of handshake requests and responses.

         **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
         days after entering that state After that they are deleted.

        - **Id** *(string) --*

          The unique identifier (ID) of a handshake. The originating account creates the ID when it
          initiates the handshake.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
          "h-" followed by from 8 to 32 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of a handshake.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Parties** *(list) --*

          Information about the two accounts that are participating in the handshake.

          - *(dict) --*

            Identifies a participant in a handshake.

            - **Id** *(string) --*

              The unique identifier (ID) for the party.

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string
              requires "h-" followed by from 8 to 32 lower-case letters or digits.

            - **Type** *(string) --*

              The type of party.

        - **State** *(string) --*

          The current state of the handshake. Use the state to trace the flow of the handshake
          through the process from its creation to its acceptance. The meaning of each of the valid
          values is as follows:

          * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some
          handshake types) and not all recipients have responded yet. The request stays in this
          state until all recipients respond.

          * **OPEN** : This handshake was sent to multiple recipients (applicable to only some
          policy types) and all recipients have responded, allowing the originator to complete the
          handshake action.

          * **CANCELED** : This handshake is no longer active because it was canceled by the
          originating account.

          * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient.

          * **DECLINED** : This handshake is no longer active because it was declined by the
          recipient account.

          * **EXPIRED** : This handshake is no longer active because the originator did not receive
          a response of any kind from the recipient before the expiration time (15 days).

        - **RequestedTimestamp** *(datetime) --*

          The date and time that the handshake request was made.

        - **ExpirationTimestamp** *(datetime) --*

          The date and time that the handshake expires. If the recipient of the handshake request
          fails to respond before the specified date and time, the handshake becomes inactive and
          is no longer valid.

        - **Action** *(string) --*

          The type of handshake, indicating what action occurs when the recipient accepts the
          handshake. The following handshake types are supported:

          * **INVITE** : This type of handshake represents a request to join an organization. It is
          always sent from the master account to only non-member accounts.

          * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all
          features in an organization. It is always sent from the master account to only *invited*
          member accounts. Created accounts do not receive this because those accounts were created
          by the organization's master account and approval is inferred.

          * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations
          service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It
          is sent only to the master account and signals the master that it can finalize the
          process to enable all features.

        - **Resources** *(list) --*

          Additional information that is needed to process the handshake.

          - *(dict) --*

            Contains additional data that is needed to process a handshake.

            - **Value** *(string) --*

              The information that is passed to the other party in the handshake. The format of the
              value string must match the requirements of the specified type.

            - **Type** *(string) --*

              The type of information being passed, specifying how the value is to be interpreted
              by the other party:

              * ``ACCOUNT`` - Specifies an AWS account ID number.

              * ``ORGANIZATION`` - Specifies an organization ID number.

              * ``EMAIL`` - Specifies the email address that is associated with the account that
              receives the handshake.

              * ``OWNER_EMAIL`` - Specifies the email address associated with the master account.
              Included as information about an organization.

              * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as
              information about an organization.

              * ``NOTES`` - Additional text provided by the handshake initiator and intended for
              the recipient to read.

            - **Resources** *(list) --*

              When needed, contains an additional array of ``HandshakeResource`` objects.
    """


_ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef(
    _ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListOrganizationalUnitsForParentPaginate` `PaginationConfig`

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


_ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef = TypedDict(
    "_ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef(
    _ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef
):
    """
    Type definition for `ListOrganizationalUnitsForParentPaginateResponse` `OrganizationalUnits`

    Contains details about an organizational unit (OU). An OU is a container of AWS accounts
    within a root of an organization. Policies that are attached to an OU apply to all accounts
    contained in that OU and in any child OUs.

    - **Id** *(string) --*

      The unique identifier (ID) associated with this OU.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
      string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of
      the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional
      lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of this OU.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of this OU.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.
    """


_ListOrganizationalUnitsForParentPaginateResponseTypeDef = TypedDict(
    "_ListOrganizationalUnitsForParentPaginateResponseTypeDef",
    {
        "OrganizationalUnits": List[
            ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef
        ]
    },
    total=False,
)


class ListOrganizationalUnitsForParentPaginateResponseTypeDef(
    _ListOrganizationalUnitsForParentPaginateResponseTypeDef
):
    """
    Type definition for `ListOrganizationalUnitsForParentPaginate` `Response`

    - **OrganizationalUnits** *(list) --*

      A list of the OUs in the specified root or parent OU.

      - *(dict) --*

        Contains details about an organizational unit (OU). An OU is a container of AWS accounts
        within a root of an organization. Policies that are attached to an OU apply to all accounts
        contained in that OU and in any child OUs.

        - **Id** *(string) --*

          The unique identifier (ID) associated with this OU.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
          string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of
          the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional
          lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of this OU.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of this OU.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.
    """


_ListParentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListParentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListParentsPaginatePaginationConfigTypeDef(
    _ListParentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListParentsPaginate` `PaginationConfig`

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


_ListParentsPaginateResponseParentsTypeDef = TypedDict(
    "_ListParentsPaginateResponseParentsTypeDef", {"Id": str, "Type": str}, total=False
)


class ListParentsPaginateResponseParentsTypeDef(
    _ListParentsPaginateResponseParentsTypeDef
):
    """
    Type definition for `ListParentsPaginateResponse` `Parents`

    Contains information about either a root or an organizational unit (OU) that can contain
    OUs or accounts in an organization.

    - **Id** *(string) --*

      The unique identifier (ID) of the parent entity.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires
      one of the following:

      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or
      digits.

      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
      lower-case letters or digits (the ID of the root that the OU is in) followed by a second
      "-" dash and from 8 to 32 additional lower-case letters or digits.

    - **Type** *(string) --*

      The type of the parent entity.
    """


_ListParentsPaginateResponseTypeDef = TypedDict(
    "_ListParentsPaginateResponseTypeDef",
    {"Parents": List[ListParentsPaginateResponseParentsTypeDef]},
    total=False,
)


class ListParentsPaginateResponseTypeDef(_ListParentsPaginateResponseTypeDef):
    """
    Type definition for `ListParentsPaginate` `Response`

    - **Parents** *(list) --*

      A list of parents for the specified child account or OU.

      - *(dict) --*

        Contains information about either a root or an organizational unit (OU) that can contain
        OUs or accounts in an organization.

        - **Id** *(string) --*

          The unique identifier (ID) of the parent entity.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires
          one of the following:

          * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or
          digits.

          * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
          lower-case letters or digits (the ID of the root that the OU is in) followed by a second
          "-" dash and from 8 to 32 additional lower-case letters or digits.

        - **Type** *(string) --*

          The type of the parent entity.
    """


_ListPoliciesForTargetPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPoliciesForTargetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPoliciesForTargetPaginatePaginationConfigTypeDef(
    _ListPoliciesForTargetPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPoliciesForTargetPaginate` `PaginationConfig`

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


_ListPoliciesForTargetPaginateResponsePoliciesTypeDef = TypedDict(
    "_ListPoliciesForTargetPaginateResponsePoliciesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "AwsManaged": bool,
    },
    total=False,
)


class ListPoliciesForTargetPaginateResponsePoliciesTypeDef(
    _ListPoliciesForTargetPaginateResponsePoliciesTypeDef
):
    """
    Type definition for `ListPoliciesForTargetPaginateResponse` `Policies`

    Contains information about a policy, but does not include the content. To see the content
    of a policy, see  DescribePolicy .

    - **Id** *(string) --*

      The unique identifier (ID) of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
      "p-" followed by from 8 to 128 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the policy.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Description** *(string) --*

      The description of the policy.

    - **Type** *(string) --*

      The type of policy.

    - **AwsManaged** *(boolean) --*

      A boolean value that indicates whether the specified policy is an AWS managed policy. If
      true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
    """


_ListPoliciesForTargetPaginateResponseTypeDef = TypedDict(
    "_ListPoliciesForTargetPaginateResponseTypeDef",
    {"Policies": List[ListPoliciesForTargetPaginateResponsePoliciesTypeDef]},
    total=False,
)


class ListPoliciesForTargetPaginateResponseTypeDef(
    _ListPoliciesForTargetPaginateResponseTypeDef
):
    """
    Type definition for `ListPoliciesForTargetPaginate` `Response`

    - **Policies** *(list) --*

      The list of policies that match the criteria in the request.

      - *(dict) --*

        Contains information about a policy, but does not include the content. To see the content
        of a policy, see  DescribePolicy .

        - **Id** *(string) --*

          The unique identifier (ID) of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
          "p-" followed by from 8 to 128 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the policy.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Description** *(string) --*

          The description of the policy.

        - **Type** *(string) --*

          The type of policy.

        - **AwsManaged** *(boolean) --*

          A boolean value that indicates whether the specified policy is an AWS managed policy. If
          true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
    """


_ListPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPoliciesPaginatePaginationConfigTypeDef(
    _ListPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPoliciesPaginate` `PaginationConfig`

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


_ListPoliciesPaginateResponsePoliciesTypeDef = TypedDict(
    "_ListPoliciesPaginateResponsePoliciesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "AwsManaged": bool,
    },
    total=False,
)


class ListPoliciesPaginateResponsePoliciesTypeDef(
    _ListPoliciesPaginateResponsePoliciesTypeDef
):
    """
    Type definition for `ListPoliciesPaginateResponse` `Policies`

    Contains information about a policy, but does not include the content. To see the content
    of a policy, see  DescribePolicy .

    - **Id** *(string) --*

      The unique identifier (ID) of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
      "p-" followed by from 8 to 128 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the policy.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the policy.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Description** *(string) --*

      The description of the policy.

    - **Type** *(string) --*

      The type of policy.

    - **AwsManaged** *(boolean) --*

      A boolean value that indicates whether the specified policy is an AWS managed policy. If
      true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
    """


_ListPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListPoliciesPaginateResponseTypeDef",
    {"Policies": List[ListPoliciesPaginateResponsePoliciesTypeDef]},
    total=False,
)


class ListPoliciesPaginateResponseTypeDef(_ListPoliciesPaginateResponseTypeDef):
    """
    Type definition for `ListPoliciesPaginate` `Response`

    - **Policies** *(list) --*

      A list of policies that match the filter criteria in the request. The output list doesn't
      include the policy contents. To see the content for a policy, see  DescribePolicy .

      - *(dict) --*

        Contains information about a policy, but does not include the content. To see the content
        of a policy, see  DescribePolicy .

        - **Id** *(string) --*

          The unique identifier (ID) of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
          "p-" followed by from 8 to 128 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the policy.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the policy.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Description** *(string) --*

          The description of the policy.

        - **Type** *(string) --*

          The type of policy.

        - **AwsManaged** *(boolean) --*

          A boolean value that indicates whether the specified policy is an AWS managed policy. If
          true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
    """


_ListRootsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRootsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRootsPaginatePaginationConfigTypeDef(
    _ListRootsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRootsPaginate` `PaginationConfig`

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


_ListRootsPaginateResponseRootsPolicyTypesTypeDef = TypedDict(
    "_ListRootsPaginateResponseRootsPolicyTypesTypeDef",
    {"Type": str, "Status": str},
    total=False,
)


class ListRootsPaginateResponseRootsPolicyTypesTypeDef(
    _ListRootsPaginateResponseRootsPolicyTypesTypeDef
):
    """
    Type definition for `ListRootsPaginateResponseRoots` `PolicyTypes`

    Contains information about a policy type and its status in the associated root.

    - **Type** *(string) --*

      The name of the policy type.

    - **Status** *(string) --*

      The status of the policy type as it relates to the associated root. To attach a
      policy of the specified type to a root or to an OU or account in that root, it must
      be available in the organization and enabled for that root.
    """


_ListRootsPaginateResponseRootsTypeDef = TypedDict(
    "_ListRootsPaginateResponseRootsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ListRootsPaginateResponseRootsPolicyTypesTypeDef],
    },
    total=False,
)


class ListRootsPaginateResponseRootsTypeDef(_ListRootsPaginateResponseRootsTypeDef):
    """
    Type definition for `ListRootsPaginateResponse` `Roots`

    Contains details about a root. A root is a top-level parent node in the hierarchy of an
    organization that can contain organizational units (OUs) and accounts. Every root contains
    every AWS account in the organization. Each root enables the accounts to be organized in a
    different way and to have different policy types enabled for use in that root.

    - **Id** *(string) --*

      The unique identifier (ID) for the root.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires
      "r-" followed by from 4 to 32 lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the root.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the root.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **PolicyTypes** *(list) --*

      The types of policies that are currently enabled for the root and therefore can be
      attached to the root or to its OUs or accounts.

      .. note::

        Even if a policy type is shown as available in the organization, you can separately
        enable and disable them at the root level by using  EnablePolicyType and
        DisablePolicyType . Use  DescribeOrganization to see the availability of the policy
        types in that organization.

      - *(dict) --*

        Contains information about a policy type and its status in the associated root.

        - **Type** *(string) --*

          The name of the policy type.

        - **Status** *(string) --*

          The status of the policy type as it relates to the associated root. To attach a
          policy of the specified type to a root or to an OU or account in that root, it must
          be available in the organization and enabled for that root.
    """


_ListRootsPaginateResponseTypeDef = TypedDict(
    "_ListRootsPaginateResponseTypeDef",
    {"Roots": List[ListRootsPaginateResponseRootsTypeDef]},
    total=False,
)


class ListRootsPaginateResponseTypeDef(_ListRootsPaginateResponseTypeDef):
    """
    Type definition for `ListRootsPaginate` `Response`

    - **Roots** *(list) --*

      A list of roots that are defined in an organization.

      - *(dict) --*

        Contains details about a root. A root is a top-level parent node in the hierarchy of an
        organization that can contain organizational units (OUs) and accounts. Every root contains
        every AWS account in the organization. Each root enables the accounts to be organized in a
        different way and to have different policy types enabled for use in that root.

        - **Id** *(string) --*

          The unique identifier (ID) for the root.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires
          "r-" followed by from 4 to 32 lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the root.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the root.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **PolicyTypes** *(list) --*

          The types of policies that are currently enabled for the root and therefore can be
          attached to the root or to its OUs or accounts.

          .. note::

            Even if a policy type is shown as available in the organization, you can separately
            enable and disable them at the root level by using  EnablePolicyType and
            DisablePolicyType . Use  DescribeOrganization to see the availability of the policy
            types in that organization.

          - *(dict) --*

            Contains information about a policy type and its status in the associated root.

            - **Type** *(string) --*

              The name of the policy type.

            - **Status** *(string) --*

              The status of the policy type as it relates to the associated root. To attach a
              policy of the specified type to a root or to an OU or account in that root, it must
              be available in the organization and enabled for that root.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginateResponse` `Tags`

    A custom key-value pair associated with a resource such as an account within your
    organization.

    - **Key** *(string) --*

      The key identifier, or name, of the tag.

    - **Value** *(string) --*

      The string value that's associated with the key of the tag. You can set the value of a
      tag to an empty string, but you can't set the value of a tag to null.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(
    _ListTagsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `Response`

    - **Tags** *(list) --*

      The tags that are assigned to the resource.

      - *(dict) --*

        A custom key-value pair associated with a resource such as an account within your
        organization.

        - **Key** *(string) --*

          The key identifier, or name, of the tag.

        - **Value** *(string) --*

          The string value that's associated with the key of the tag. You can set the value of a
          tag to an empty string, but you can't set the value of a tag to null.
    """


_ListTargetsForPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTargetsForPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTargetsForPolicyPaginatePaginationConfigTypeDef(
    _ListTargetsForPolicyPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTargetsForPolicyPaginate` `PaginationConfig`

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


_ListTargetsForPolicyPaginateResponseTargetsTypeDef = TypedDict(
    "_ListTargetsForPolicyPaginateResponseTargetsTypeDef",
    {"TargetId": str, "Arn": str, "Name": str, "Type": str},
    total=False,
)


class ListTargetsForPolicyPaginateResponseTargetsTypeDef(
    _ListTargetsForPolicyPaginateResponseTargetsTypeDef
):
    """
    Type definition for `ListTargetsForPolicyPaginateResponse` `Targets`

    Contains information about a root, OU, or account that a policy is attached to.

    - **TargetId** *(string) --*

      The unique identifier (ID) of the policy target.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires
      one of the following:

      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or
      digits.

      * Account: a string that consists of exactly 12 digits.

      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
      lower-case letters or digits (the ID of the root that the OU is in) followed by a second
      "-" dash and from 8 to 32 additional lower-case letters or digits.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the policy target.

      For more information about ARNs in Organizations, see `ARN Formats Supported by
      Organizations
      <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
      in the *AWS Organizations User Guide* .

    - **Name** *(string) --*

      The friendly name of the policy target.

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
      parameter is a string of any of the characters in the ASCII character range.

    - **Type** *(string) --*

      The type of the policy target.
    """


_ListTargetsForPolicyPaginateResponseTypeDef = TypedDict(
    "_ListTargetsForPolicyPaginateResponseTypeDef",
    {"Targets": List[ListTargetsForPolicyPaginateResponseTargetsTypeDef]},
    total=False,
)


class ListTargetsForPolicyPaginateResponseTypeDef(
    _ListTargetsForPolicyPaginateResponseTypeDef
):
    """
    Type definition for `ListTargetsForPolicyPaginate` `Response`

    - **Targets** *(list) --*

      A list of structures, each of which contains details about one of the entities to which the
      specified policy is attached.

      - *(dict) --*

        Contains information about a root, OU, or account that a policy is attached to.

        - **TargetId** *(string) --*

          The unique identifier (ID) of the policy target.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires
          one of the following:

          * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or
          digits.

          * Account: a string that consists of exactly 12 digits.

          * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32
          lower-case letters or digits (the ID of the root that the OU is in) followed by a second
          "-" dash and from 8 to 32 additional lower-case letters or digits.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the policy target.

          For more information about ARNs in Organizations, see `ARN Formats Supported by
          Organizations
          <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__
          in the *AWS Organizations User Guide* .

        - **Name** *(string) --*

          The friendly name of the policy target.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of any of the characters in the ASCII character range.

        - **Type** *(string) --*

          The type of the policy target.
    """
