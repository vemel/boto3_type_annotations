"Main interface for managedblockchain type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef",
    "ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef",
    "ClientCreateMemberMemberConfigurationTypeDef",
    "ClientCreateMemberResponseTypeDef",
    "ClientCreateNetworkFrameworkConfigurationFabricTypeDef",
    "ClientCreateNetworkFrameworkConfigurationTypeDef",
    "ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef",
    "ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef",
    "ClientCreateNetworkMemberConfigurationTypeDef",
    "ClientCreateNetworkResponseTypeDef",
    "ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    "ClientCreateNetworkVotingPolicyTypeDef",
    "ClientCreateNodeNodeConfigurationTypeDef",
    "ClientCreateNodeResponseTypeDef",
    "ClientCreateProposalActionsInvitationsTypeDef",
    "ClientCreateProposalActionsRemovalsTypeDef",
    "ClientCreateProposalActionsTypeDef",
    "ClientCreateProposalResponseTypeDef",
    "ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef",
    "ClientGetMemberResponseMemberFrameworkAttributesTypeDef",
    "ClientGetMemberResponseMemberTypeDef",
    "ClientGetMemberResponseTypeDef",
    "ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef",
    "ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef",
    "ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    "ClientGetNetworkResponseNetworkVotingPolicyTypeDef",
    "ClientGetNetworkResponseNetworkTypeDef",
    "ClientGetNetworkResponseTypeDef",
    "ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef",
    "ClientGetNodeResponseNodeFrameworkAttributesTypeDef",
    "ClientGetNodeResponseNodeTypeDef",
    "ClientGetNodeResponseTypeDef",
    "ClientGetProposalResponseProposalActionsInvitationsTypeDef",
    "ClientGetProposalResponseProposalActionsRemovalsTypeDef",
    "ClientGetProposalResponseProposalActionsTypeDef",
    "ClientGetProposalResponseProposalTypeDef",
    "ClientGetProposalResponseTypeDef",
    "ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef",
    "ClientListInvitationsResponseInvitationsTypeDef",
    "ClientListInvitationsResponseTypeDef",
    "ClientListMembersResponseMembersTypeDef",
    "ClientListMembersResponseTypeDef",
    "ClientListNetworksResponseNetworksTypeDef",
    "ClientListNetworksResponseTypeDef",
    "ClientListNodesResponseNodesTypeDef",
    "ClientListNodesResponseTypeDef",
    "ClientListProposalVotesResponseProposalVotesTypeDef",
    "ClientListProposalVotesResponseTypeDef",
    "ClientListProposalsResponseProposalsTypeDef",
    "ClientListProposalsResponseTypeDef",
)


_ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef = TypedDict(
    "_ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef",
    {"AdminUsername": str, "AdminPassword": str},
)


class ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef(
    _ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef
):
    """
    Type definition for `ClientCreateMemberMemberConfigurationFrameworkConfiguration` `Fabric`

    Attributes of Hyperledger Fabric for a member on a Managed Blockchain network that uses
    Hyperledger Fabric.

    - **AdminUsername** *(string) --* **[REQUIRED]**

      The user name for the member's initial administrative user.

    - **AdminPassword** *(string) --* **[REQUIRED]**

      The password for the member's initial administrative user. The ``AdminPassword`` must be at
      least eight characters long and no more than 32 characters. It must contain at least one
      uppercase letter, one lowercase letter, and one digit. It cannot have a single quote(‘),
      double quote(“), forward slash(/), backward slash(\\), @, or a space.
    """


_ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef = TypedDict(
    "_ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef",
    {
        "Fabric": ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef
    },
    total=False,
)


class ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef(
    _ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef
):
    """
    Type definition for `ClientCreateMemberMemberConfiguration` `FrameworkConfiguration`

    Configuration properties of the blockchain framework relevant to the member.

    - **Fabric** *(dict) --*

      Attributes of Hyperledger Fabric for a member on a Managed Blockchain network that uses
      Hyperledger Fabric.

      - **AdminUsername** *(string) --* **[REQUIRED]**

        The user name for the member's initial administrative user.

      - **AdminPassword** *(string) --* **[REQUIRED]**

        The password for the member's initial administrative user. The ``AdminPassword`` must be at
        least eight characters long and no more than 32 characters. It must contain at least one
        uppercase letter, one lowercase letter, and one digit. It cannot have a single quote(‘),
        double quote(“), forward slash(/), backward slash(\\), @, or a space.
    """


_RequiredClientCreateMemberMemberConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateMemberMemberConfigurationTypeDef",
    {
        "Name": str,
        "FrameworkConfiguration": ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef,
    },
)
_OptionalClientCreateMemberMemberConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateMemberMemberConfigurationTypeDef",
    {"Description": str},
    total=False,
)


class ClientCreateMemberMemberConfigurationTypeDef(
    _RequiredClientCreateMemberMemberConfigurationTypeDef,
    _OptionalClientCreateMemberMemberConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateMember` `MemberConfiguration`

    Member configuration parameters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the member.

    - **Description** *(string) --*

      An optional description of the member.

    - **FrameworkConfiguration** *(dict) --* **[REQUIRED]**

      Configuration properties of the blockchain framework relevant to the member.

      - **Fabric** *(dict) --*

        Attributes of Hyperledger Fabric for a member on a Managed Blockchain network that uses
        Hyperledger Fabric.

        - **AdminUsername** *(string) --* **[REQUIRED]**

          The user name for the member's initial administrative user.

        - **AdminPassword** *(string) --* **[REQUIRED]**

          The password for the member's initial administrative user. The ``AdminPassword`` must be at
          least eight characters long and no more than 32 characters. It must contain at least one
          uppercase letter, one lowercase letter, and one digit. It cannot have a single quote(‘),
          double quote(“), forward slash(/), backward slash(\\), @, or a space.
    """


_ClientCreateMemberResponseTypeDef = TypedDict(
    "_ClientCreateMemberResponseTypeDef", {"MemberId": str}, total=False
)


class ClientCreateMemberResponseTypeDef(_ClientCreateMemberResponseTypeDef):
    """
    Type definition for `ClientCreateMember` `Response`

    - **MemberId** *(string) --*

      The unique identifier of the member.
    """


_ClientCreateNetworkFrameworkConfigurationFabricTypeDef = TypedDict(
    "_ClientCreateNetworkFrameworkConfigurationFabricTypeDef", {"Edition": str}
)


class ClientCreateNetworkFrameworkConfigurationFabricTypeDef(
    _ClientCreateNetworkFrameworkConfigurationFabricTypeDef
):
    """
    Type definition for `ClientCreateNetworkFrameworkConfiguration` `Fabric`

    Hyperledger Fabric configuration properties for a Managed Blockchain network that uses
    Hyperledger Fabric.

    - **Edition** *(string) --* **[REQUIRED]**

      The edition of Amazon Managed Blockchain that the network uses. For more information, see
      `Amazon Managed Blockchain Pricing <https://aws.amazon.com/managed-blockchain/pricing/>`__ .
    """


_ClientCreateNetworkFrameworkConfigurationTypeDef = TypedDict(
    "_ClientCreateNetworkFrameworkConfigurationTypeDef",
    {"Fabric": ClientCreateNetworkFrameworkConfigurationFabricTypeDef},
    total=False,
)


class ClientCreateNetworkFrameworkConfigurationTypeDef(
    _ClientCreateNetworkFrameworkConfigurationTypeDef
):
    """
    Type definition for `ClientCreateNetwork` `FrameworkConfiguration`

    Configuration properties of the blockchain framework relevant to the network configuration.

    - **Fabric** *(dict) --*

      Hyperledger Fabric configuration properties for a Managed Blockchain network that uses
      Hyperledger Fabric.

      - **Edition** *(string) --* **[REQUIRED]**

        The edition of Amazon Managed Blockchain that the network uses. For more information, see
        `Amazon Managed Blockchain Pricing <https://aws.amazon.com/managed-blockchain/pricing/>`__ .
    """


_ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef = TypedDict(
    "_ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef",
    {"AdminUsername": str, "AdminPassword": str},
)


class ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef(
    _ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef
):
    """
    Type definition for `ClientCreateNetworkMemberConfigurationFrameworkConfiguration` `Fabric`

    Attributes of Hyperledger Fabric for a member on a Managed Blockchain network that uses
    Hyperledger Fabric.

    - **AdminUsername** *(string) --* **[REQUIRED]**

      The user name for the member's initial administrative user.

    - **AdminPassword** *(string) --* **[REQUIRED]**

      The password for the member's initial administrative user. The ``AdminPassword`` must be at
      least eight characters long and no more than 32 characters. It must contain at least one
      uppercase letter, one lowercase letter, and one digit. It cannot have a single quote(‘),
      double quote(“), forward slash(/), backward slash(\\), @, or a space.
    """


_ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef = TypedDict(
    "_ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef",
    {
        "Fabric": ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef
    },
    total=False,
)


class ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef(
    _ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef
):
    """
    Type definition for `ClientCreateNetworkMemberConfiguration` `FrameworkConfiguration`

    Configuration properties of the blockchain framework relevant to the member.

    - **Fabric** *(dict) --*

      Attributes of Hyperledger Fabric for a member on a Managed Blockchain network that uses
      Hyperledger Fabric.

      - **AdminUsername** *(string) --* **[REQUIRED]**

        The user name for the member's initial administrative user.

      - **AdminPassword** *(string) --* **[REQUIRED]**

        The password for the member's initial administrative user. The ``AdminPassword`` must be at
        least eight characters long and no more than 32 characters. It must contain at least one
        uppercase letter, one lowercase letter, and one digit. It cannot have a single quote(‘),
        double quote(“), forward slash(/), backward slash(\\), @, or a space.
    """


_RequiredClientCreateNetworkMemberConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateNetworkMemberConfigurationTypeDef",
    {
        "Name": str,
        "FrameworkConfiguration": ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef,
    },
)
_OptionalClientCreateNetworkMemberConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateNetworkMemberConfigurationTypeDef",
    {"Description": str},
    total=False,
)


class ClientCreateNetworkMemberConfigurationTypeDef(
    _RequiredClientCreateNetworkMemberConfigurationTypeDef,
    _OptionalClientCreateNetworkMemberConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateNetwork` `MemberConfiguration`

    Configuration properties for the first member within the network.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the member.

    - **Description** *(string) --*

      An optional description of the member.

    - **FrameworkConfiguration** *(dict) --* **[REQUIRED]**

      Configuration properties of the blockchain framework relevant to the member.

      - **Fabric** *(dict) --*

        Attributes of Hyperledger Fabric for a member on a Managed Blockchain network that uses
        Hyperledger Fabric.

        - **AdminUsername** *(string) --* **[REQUIRED]**

          The user name for the member's initial administrative user.

        - **AdminPassword** *(string) --* **[REQUIRED]**

          The password for the member's initial administrative user. The ``AdminPassword`` must be at
          least eight characters long and no more than 32 characters. It must contain at least one
          uppercase letter, one lowercase letter, and one digit. It cannot have a single quote(‘),
          double quote(“), forward slash(/), backward slash(\\), @, or a space.
    """


_ClientCreateNetworkResponseTypeDef = TypedDict(
    "_ClientCreateNetworkResponseTypeDef",
    {"NetworkId": str, "MemberId": str},
    total=False,
)


class ClientCreateNetworkResponseTypeDef(_ClientCreateNetworkResponseTypeDef):
    """
    Type definition for `ClientCreateNetwork` `Response`

    - **NetworkId** *(string) --*

      The unique identifier for the network.

    - **MemberId** *(string) --*

      The unique identifier for the first member within the network.
    """


_ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef = TypedDict(
    "_ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": int,
        "ProposalDurationInHours": int,
        "ThresholdComparator": str,
    },
    total=False,
)


class ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef(
    _ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef
):
    """
    Type definition for `ClientCreateNetworkVotingPolicy` `ApprovalThresholdPolicy`

    Defines the rules for the network for voting on proposals, such as the percentage of ``YES``
    votes required for the proposal to be approved and the duration of the proposal. The policy
    applies to all proposals and is specified when the network is created.

    - **ThresholdPercentage** *(integer) --*

      The percentage of votes among all members that must be ``YES`` for a proposal to be approved.
      For example, a ``ThresholdPercentage`` value of ``50`` indicates 50%. The
      ``ThresholdComparator`` determines the precise comparison. If a ``ThresholdPercentage`` value
      of ``50`` is specified on a network with 10 members, along with a ``ThresholdComparator``
      value of ``GREATER_THAN`` , this indicates that 6 ``YES`` votes are required for the proposal
      to be approved.

    - **ProposalDurationInHours** *(integer) --*

      The duration from the time that a proposal is created until it expires. If members cast
      neither the required number of ``YES`` votes to approve the proposal nor the number of ``NO``
      votes required to reject it before the duration expires, the proposal is ``EXPIRED`` and
      ``ProposalActions`` are not carried out.

    - **ThresholdComparator** *(string) --*

      Determines whether the vote percentage must be greater than the ``ThresholdPercentage`` or
      must be greater than or equal to the ``ThreholdPercentage`` to be approved.
    """


_ClientCreateNetworkVotingPolicyTypeDef = TypedDict(
    "_ClientCreateNetworkVotingPolicyTypeDef",
    {
        "ApprovalThresholdPolicy": ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef
    },
    total=False,
)


class ClientCreateNetworkVotingPolicyTypeDef(_ClientCreateNetworkVotingPolicyTypeDef):
    """
    Type definition for `ClientCreateNetwork` `VotingPolicy`

    The voting rules used by the network to determine if a proposal is approved.

    - **ApprovalThresholdPolicy** *(dict) --*

      Defines the rules for the network for voting on proposals, such as the percentage of ``YES``
      votes required for the proposal to be approved and the duration of the proposal. The policy
      applies to all proposals and is specified when the network is created.

      - **ThresholdPercentage** *(integer) --*

        The percentage of votes among all members that must be ``YES`` for a proposal to be approved.
        For example, a ``ThresholdPercentage`` value of ``50`` indicates 50%. The
        ``ThresholdComparator`` determines the precise comparison. If a ``ThresholdPercentage`` value
        of ``50`` is specified on a network with 10 members, along with a ``ThresholdComparator``
        value of ``GREATER_THAN`` , this indicates that 6 ``YES`` votes are required for the proposal
        to be approved.

      - **ProposalDurationInHours** *(integer) --*

        The duration from the time that a proposal is created until it expires. If members cast
        neither the required number of ``YES`` votes to approve the proposal nor the number of ``NO``
        votes required to reject it before the duration expires, the proposal is ``EXPIRED`` and
        ``ProposalActions`` are not carried out.

      - **ThresholdComparator** *(string) --*

        Determines whether the vote percentage must be greater than the ``ThresholdPercentage`` or
        must be greater than or equal to the ``ThreholdPercentage`` to be approved.
    """


_ClientCreateNodeNodeConfigurationTypeDef = TypedDict(
    "_ClientCreateNodeNodeConfigurationTypeDef",
    {"InstanceType": str, "AvailabilityZone": str},
)


class ClientCreateNodeNodeConfigurationTypeDef(
    _ClientCreateNodeNodeConfigurationTypeDef
):
    """
    Type definition for `ClientCreateNode` `NodeConfiguration`

    The properties of a node configuration.

    - **InstanceType** *(string) --* **[REQUIRED]**

      The Amazon Managed Blockchain instance type for the node.

    - **AvailabilityZone** *(string) --* **[REQUIRED]**

      The Availability Zone in which the node exists.
    """


_ClientCreateNodeResponseTypeDef = TypedDict(
    "_ClientCreateNodeResponseTypeDef", {"NodeId": str}, total=False
)


class ClientCreateNodeResponseTypeDef(_ClientCreateNodeResponseTypeDef):
    """
    Type definition for `ClientCreateNode` `Response`

    - **NodeId** *(string) --*

      The unique identifier of the node.
    """


_ClientCreateProposalActionsInvitationsTypeDef = TypedDict(
    "_ClientCreateProposalActionsInvitationsTypeDef", {"Principal": str}
)


class ClientCreateProposalActionsInvitationsTypeDef(
    _ClientCreateProposalActionsInvitationsTypeDef
):
    """
    Type definition for `ClientCreateProposalActions` `Invitations`

    An action to invite a specific AWS account to create a member and join the network. The
    ``InviteAction`` is carried out when a ``Proposal`` is ``APPROVED`` .

    - **Principal** *(string) --* **[REQUIRED]**

      The AWS account ID to invite.
    """


_ClientCreateProposalActionsRemovalsTypeDef = TypedDict(
    "_ClientCreateProposalActionsRemovalsTypeDef", {"MemberId": str}
)


class ClientCreateProposalActionsRemovalsTypeDef(
    _ClientCreateProposalActionsRemovalsTypeDef
):
    """
    Type definition for `ClientCreateProposalActions` `Removals`

    An action to remove a member from a Managed Blockchain network as the result of a removal
    proposal that is ``APPROVED`` . The member and all associated resources are deleted from the
    network.

    - **MemberId** *(string) --* **[REQUIRED]**

      The unique identifier of the member to remove.
    """


_ClientCreateProposalActionsTypeDef = TypedDict(
    "_ClientCreateProposalActionsTypeDef",
    {
        "Invitations": List[ClientCreateProposalActionsInvitationsTypeDef],
        "Removals": List[ClientCreateProposalActionsRemovalsTypeDef],
    },
    total=False,
)


class ClientCreateProposalActionsTypeDef(_ClientCreateProposalActionsTypeDef):
    """
    Type definition for `ClientCreateProposal` `Actions`

    The type of actions proposed, such as inviting a member or removing a member. The types of
    ``Actions`` in a proposal are mutually exclusive. For example, a proposal with ``Invitations``
    actions cannot also contain ``Removals`` actions.

    - **Invitations** *(list) --*

      The actions to perform for an ``APPROVED`` proposal to invite an AWS account to create a member
      and join the network.

      - *(dict) --*

        An action to invite a specific AWS account to create a member and join the network. The
        ``InviteAction`` is carried out when a ``Proposal`` is ``APPROVED`` .

        - **Principal** *(string) --* **[REQUIRED]**

          The AWS account ID to invite.

    - **Removals** *(list) --*

      The actions to perform for an ``APPROVED`` proposal to remove a member from the network, which
      deletes the member and all associated member resources from the network.

      - *(dict) --*

        An action to remove a member from a Managed Blockchain network as the result of a removal
        proposal that is ``APPROVED`` . The member and all associated resources are deleted from the
        network.

        - **MemberId** *(string) --* **[REQUIRED]**

          The unique identifier of the member to remove.
    """


_ClientCreateProposalResponseTypeDef = TypedDict(
    "_ClientCreateProposalResponseTypeDef", {"ProposalId": str}, total=False
)


class ClientCreateProposalResponseTypeDef(_ClientCreateProposalResponseTypeDef):
    """
    Type definition for `ClientCreateProposal` `Response`

    - **ProposalId** *(string) --*

      The unique identifier of the proposal.
    """


_ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef = TypedDict(
    "_ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef",
    {"AdminUsername": str, "CaEndpoint": str},
    total=False,
)


class ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef(
    _ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef
):
    """
    Type definition for `ClientGetMemberResponseMemberFrameworkAttributes` `Fabric`

    Attributes of Hyperledger Fabric relevant to a member on a Managed Blockchain network
    that uses Hyperledger Fabric.

    - **AdminUsername** *(string) --*

      The user name for the initial administrator user for the member.

    - **CaEndpoint** *(string) --*

      The endpoint used to access the member's certificate authority.
    """


_ClientGetMemberResponseMemberFrameworkAttributesTypeDef = TypedDict(
    "_ClientGetMemberResponseMemberFrameworkAttributesTypeDef",
    {"Fabric": ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef},
    total=False,
)


class ClientGetMemberResponseMemberFrameworkAttributesTypeDef(
    _ClientGetMemberResponseMemberFrameworkAttributesTypeDef
):
    """
    Type definition for `ClientGetMemberResponseMember` `FrameworkAttributes`

    Attributes relevant to a member for the blockchain framework that the Managed Blockchain
    network uses.

    - **Fabric** *(dict) --*

      Attributes of Hyperledger Fabric relevant to a member on a Managed Blockchain network
      that uses Hyperledger Fabric.

      - **AdminUsername** *(string) --*

        The user name for the initial administrator user for the member.

      - **CaEndpoint** *(string) --*

        The endpoint used to access the member's certificate authority.
    """


_ClientGetMemberResponseMemberTypeDef = TypedDict(
    "_ClientGetMemberResponseMemberTypeDef",
    {
        "NetworkId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "FrameworkAttributes": ClientGetMemberResponseMemberFrameworkAttributesTypeDef,
        "Status": str,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetMemberResponseMemberTypeDef(_ClientGetMemberResponseMemberTypeDef):
    """
    Type definition for `ClientGetMemberResponse` `Member`

    The properties of a member.

    - **NetworkId** *(string) --*

      The unique identifier of the network to which the member belongs.

    - **Id** *(string) --*

      The unique identifier of the member.

    - **Name** *(string) --*

      The name of the member.

    - **Description** *(string) --*

      An optional description for the member.

    - **FrameworkAttributes** *(dict) --*

      Attributes relevant to a member for the blockchain framework that the Managed Blockchain
      network uses.

      - **Fabric** *(dict) --*

        Attributes of Hyperledger Fabric relevant to a member on a Managed Blockchain network
        that uses Hyperledger Fabric.

        - **AdminUsername** *(string) --*

          The user name for the initial administrator user for the member.

        - **CaEndpoint** *(string) --*

          The endpoint used to access the member's certificate authority.

    - **Status** *(string) --*

      The status of a member.

      * ``CREATING`` - The AWS account is in the process of creating a member.

      * ``AVAILABLE`` - The member has been created and can participate in the network.

      * ``CREATE_FAILED`` - The AWS account attempted to create a member and creation failed.

      * ``DELETING`` - The member and all associated resources are in the process of being
      deleted. Either the AWS account that owns the member deleted it, or the member is being
      deleted as the result of an ``APPROVED``  ``PROPOSAL`` to remove the member.

      * ``DELETED`` - The member can no longer participate on the network and all associated
      resources are deleted. Either the AWS account that owns the member deleted it, or the
      member is being deleted as the result of an ``APPROVED``  ``PROPOSAL`` to remove the member.

    - **CreationDate** *(datetime) --*

      The date and time that the member was created.
    """


_ClientGetMemberResponseTypeDef = TypedDict(
    "_ClientGetMemberResponseTypeDef",
    {"Member": ClientGetMemberResponseMemberTypeDef},
    total=False,
)


class ClientGetMemberResponseTypeDef(_ClientGetMemberResponseTypeDef):
    """
    Type definition for `ClientGetMember` `Response`

    - **Member** *(dict) --*

      The properties of a member.

      - **NetworkId** *(string) --*

        The unique identifier of the network to which the member belongs.

      - **Id** *(string) --*

        The unique identifier of the member.

      - **Name** *(string) --*

        The name of the member.

      - **Description** *(string) --*

        An optional description for the member.

      - **FrameworkAttributes** *(dict) --*

        Attributes relevant to a member for the blockchain framework that the Managed Blockchain
        network uses.

        - **Fabric** *(dict) --*

          Attributes of Hyperledger Fabric relevant to a member on a Managed Blockchain network
          that uses Hyperledger Fabric.

          - **AdminUsername** *(string) --*

            The user name for the initial administrator user for the member.

          - **CaEndpoint** *(string) --*

            The endpoint used to access the member's certificate authority.

      - **Status** *(string) --*

        The status of a member.

        * ``CREATING`` - The AWS account is in the process of creating a member.

        * ``AVAILABLE`` - The member has been created and can participate in the network.

        * ``CREATE_FAILED`` - The AWS account attempted to create a member and creation failed.

        * ``DELETING`` - The member and all associated resources are in the process of being
        deleted. Either the AWS account that owns the member deleted it, or the member is being
        deleted as the result of an ``APPROVED``  ``PROPOSAL`` to remove the member.

        * ``DELETED`` - The member can no longer participate on the network and all associated
        resources are deleted. Either the AWS account that owns the member deleted it, or the
        member is being deleted as the result of an ``APPROVED``  ``PROPOSAL`` to remove the member.

      - **CreationDate** *(datetime) --*

        The date and time that the member was created.
    """


_ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef = TypedDict(
    "_ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef",
    {"OrderingServiceEndpoint": str, "Edition": str},
    total=False,
)


class ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef(
    _ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef
):
    """
    Type definition for `ClientGetNetworkResponseNetworkFrameworkAttributes` `Fabric`

    Attributes of Hyperledger Fabric for a Managed Blockchain network that uses Hyperledger
    Fabric.

    - **OrderingServiceEndpoint** *(string) --*

      The endpoint of the ordering service for the network.

    - **Edition** *(string) --*

      The edition of Amazon Managed Blockchain that Hyperledger Fabric uses. For more
      information, see `Amazon Managed Blockchain Pricing
      <https://aws.amazon.com/managed-blockchain/pricing/>`__ .
    """


_ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef = TypedDict(
    "_ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef",
    {"Fabric": ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef},
    total=False,
)


class ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef(
    _ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef
):
    """
    Type definition for `ClientGetNetworkResponseNetwork` `FrameworkAttributes`

    Attributes of the blockchain framework that the network uses.

    - **Fabric** *(dict) --*

      Attributes of Hyperledger Fabric for a Managed Blockchain network that uses Hyperledger
      Fabric.

      - **OrderingServiceEndpoint** *(string) --*

        The endpoint of the ordering service for the network.

      - **Edition** *(string) --*

        The edition of Amazon Managed Blockchain that Hyperledger Fabric uses. For more
        information, see `Amazon Managed Blockchain Pricing
        <https://aws.amazon.com/managed-blockchain/pricing/>`__ .
    """


_ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef = TypedDict(
    "_ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": int,
        "ProposalDurationInHours": int,
        "ThresholdComparator": str,
    },
    total=False,
)


class ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef(
    _ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef
):
    """
    Type definition for `ClientGetNetworkResponseNetworkVotingPolicy` `ApprovalThresholdPolicy`

    Defines the rules for the network for voting on proposals, such as the percentage of
    ``YES`` votes required for the proposal to be approved and the duration of the proposal.
    The policy applies to all proposals and is specified when the network is created.

    - **ThresholdPercentage** *(integer) --*

      The percentage of votes among all members that must be ``YES`` for a proposal to be
      approved. For example, a ``ThresholdPercentage`` value of ``50`` indicates 50%. The
      ``ThresholdComparator`` determines the precise comparison. If a ``ThresholdPercentage``
      value of ``50`` is specified on a network with 10 members, along with a
      ``ThresholdComparator`` value of ``GREATER_THAN`` , this indicates that 6 ``YES`` votes
      are required for the proposal to be approved.

    - **ProposalDurationInHours** *(integer) --*

      The duration from the time that a proposal is created until it expires. If members cast
      neither the required number of ``YES`` votes to approve the proposal nor the number of
      ``NO`` votes required to reject it before the duration expires, the proposal is
      ``EXPIRED`` and ``ProposalActions`` are not carried out.

    - **ThresholdComparator** *(string) --*

      Determines whether the vote percentage must be greater than the ``ThresholdPercentage``
      or must be greater than or equal to the ``ThreholdPercentage`` to be approved.
    """


_ClientGetNetworkResponseNetworkVotingPolicyTypeDef = TypedDict(
    "_ClientGetNetworkResponseNetworkVotingPolicyTypeDef",
    {
        "ApprovalThresholdPolicy": ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef
    },
    total=False,
)


class ClientGetNetworkResponseNetworkVotingPolicyTypeDef(
    _ClientGetNetworkResponseNetworkVotingPolicyTypeDef
):
    """
    Type definition for `ClientGetNetworkResponseNetwork` `VotingPolicy`

    The voting rules for the network to decide if a proposal is accepted.

    - **ApprovalThresholdPolicy** *(dict) --*

      Defines the rules for the network for voting on proposals, such as the percentage of
      ``YES`` votes required for the proposal to be approved and the duration of the proposal.
      The policy applies to all proposals and is specified when the network is created.

      - **ThresholdPercentage** *(integer) --*

        The percentage of votes among all members that must be ``YES`` for a proposal to be
        approved. For example, a ``ThresholdPercentage`` value of ``50`` indicates 50%. The
        ``ThresholdComparator`` determines the precise comparison. If a ``ThresholdPercentage``
        value of ``50`` is specified on a network with 10 members, along with a
        ``ThresholdComparator`` value of ``GREATER_THAN`` , this indicates that 6 ``YES`` votes
        are required for the proposal to be approved.

      - **ProposalDurationInHours** *(integer) --*

        The duration from the time that a proposal is created until it expires. If members cast
        neither the required number of ``YES`` votes to approve the proposal nor the number of
        ``NO`` votes required to reject it before the duration expires, the proposal is
        ``EXPIRED`` and ``ProposalActions`` are not carried out.

      - **ThresholdComparator** *(string) --*

        Determines whether the vote percentage must be greater than the ``ThresholdPercentage``
        or must be greater than or equal to the ``ThreholdPercentage`` to be approved.
    """


_ClientGetNetworkResponseNetworkTypeDef = TypedDict(
    "_ClientGetNetworkResponseNetworkTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": str,
        "FrameworkVersion": str,
        "FrameworkAttributes": ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef,
        "VpcEndpointServiceName": str,
        "VotingPolicy": ClientGetNetworkResponseNetworkVotingPolicyTypeDef,
        "Status": str,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetNetworkResponseNetworkTypeDef(_ClientGetNetworkResponseNetworkTypeDef):
    """
    Type definition for `ClientGetNetworkResponse` `Network`

    An object containing network configuration parameters.

    - **Id** *(string) --*

      The unique identifier of the network.

    - **Name** *(string) --*

      The name of the network.

    - **Description** *(string) --*

      Attributes of the blockchain framework for the network.

    - **Framework** *(string) --*

      The blockchain framework that the network uses.

    - **FrameworkVersion** *(string) --*

      The version of the blockchain framework that the network uses.

    - **FrameworkAttributes** *(dict) --*

      Attributes of the blockchain framework that the network uses.

      - **Fabric** *(dict) --*

        Attributes of Hyperledger Fabric for a Managed Blockchain network that uses Hyperledger
        Fabric.

        - **OrderingServiceEndpoint** *(string) --*

          The endpoint of the ordering service for the network.

        - **Edition** *(string) --*

          The edition of Amazon Managed Blockchain that Hyperledger Fabric uses. For more
          information, see `Amazon Managed Blockchain Pricing
          <https://aws.amazon.com/managed-blockchain/pricing/>`__ .

    - **VpcEndpointServiceName** *(string) --*

      The VPC endpoint service name of the VPC endpoint service of the network. Members use the
      VPC endpoint service name to create a VPC endpoint to access network resources.

    - **VotingPolicy** *(dict) --*

      The voting rules for the network to decide if a proposal is accepted.

      - **ApprovalThresholdPolicy** *(dict) --*

        Defines the rules for the network for voting on proposals, such as the percentage of
        ``YES`` votes required for the proposal to be approved and the duration of the proposal.
        The policy applies to all proposals and is specified when the network is created.

        - **ThresholdPercentage** *(integer) --*

          The percentage of votes among all members that must be ``YES`` for a proposal to be
          approved. For example, a ``ThresholdPercentage`` value of ``50`` indicates 50%. The
          ``ThresholdComparator`` determines the precise comparison. If a ``ThresholdPercentage``
          value of ``50`` is specified on a network with 10 members, along with a
          ``ThresholdComparator`` value of ``GREATER_THAN`` , this indicates that 6 ``YES`` votes
          are required for the proposal to be approved.

        - **ProposalDurationInHours** *(integer) --*

          The duration from the time that a proposal is created until it expires. If members cast
          neither the required number of ``YES`` votes to approve the proposal nor the number of
          ``NO`` votes required to reject it before the duration expires, the proposal is
          ``EXPIRED`` and ``ProposalActions`` are not carried out.

        - **ThresholdComparator** *(string) --*

          Determines whether the vote percentage must be greater than the ``ThresholdPercentage``
          or must be greater than or equal to the ``ThreholdPercentage`` to be approved.

    - **Status** *(string) --*

      The current status of the network.

    - **CreationDate** *(datetime) --*

      The date and time that the network was created.
    """


_ClientGetNetworkResponseTypeDef = TypedDict(
    "_ClientGetNetworkResponseTypeDef",
    {"Network": ClientGetNetworkResponseNetworkTypeDef},
    total=False,
)


class ClientGetNetworkResponseTypeDef(_ClientGetNetworkResponseTypeDef):
    """
    Type definition for `ClientGetNetwork` `Response`

    - **Network** *(dict) --*

      An object containing network configuration parameters.

      - **Id** *(string) --*

        The unique identifier of the network.

      - **Name** *(string) --*

        The name of the network.

      - **Description** *(string) --*

        Attributes of the blockchain framework for the network.

      - **Framework** *(string) --*

        The blockchain framework that the network uses.

      - **FrameworkVersion** *(string) --*

        The version of the blockchain framework that the network uses.

      - **FrameworkAttributes** *(dict) --*

        Attributes of the blockchain framework that the network uses.

        - **Fabric** *(dict) --*

          Attributes of Hyperledger Fabric for a Managed Blockchain network that uses Hyperledger
          Fabric.

          - **OrderingServiceEndpoint** *(string) --*

            The endpoint of the ordering service for the network.

          - **Edition** *(string) --*

            The edition of Amazon Managed Blockchain that Hyperledger Fabric uses. For more
            information, see `Amazon Managed Blockchain Pricing
            <https://aws.amazon.com/managed-blockchain/pricing/>`__ .

      - **VpcEndpointServiceName** *(string) --*

        The VPC endpoint service name of the VPC endpoint service of the network. Members use the
        VPC endpoint service name to create a VPC endpoint to access network resources.

      - **VotingPolicy** *(dict) --*

        The voting rules for the network to decide if a proposal is accepted.

        - **ApprovalThresholdPolicy** *(dict) --*

          Defines the rules for the network for voting on proposals, such as the percentage of
          ``YES`` votes required for the proposal to be approved and the duration of the proposal.
          The policy applies to all proposals and is specified when the network is created.

          - **ThresholdPercentage** *(integer) --*

            The percentage of votes among all members that must be ``YES`` for a proposal to be
            approved. For example, a ``ThresholdPercentage`` value of ``50`` indicates 50%. The
            ``ThresholdComparator`` determines the precise comparison. If a ``ThresholdPercentage``
            value of ``50`` is specified on a network with 10 members, along with a
            ``ThresholdComparator`` value of ``GREATER_THAN`` , this indicates that 6 ``YES`` votes
            are required for the proposal to be approved.

          - **ProposalDurationInHours** *(integer) --*

            The duration from the time that a proposal is created until it expires. If members cast
            neither the required number of ``YES`` votes to approve the proposal nor the number of
            ``NO`` votes required to reject it before the duration expires, the proposal is
            ``EXPIRED`` and ``ProposalActions`` are not carried out.

          - **ThresholdComparator** *(string) --*

            Determines whether the vote percentage must be greater than the ``ThresholdPercentage``
            or must be greater than or equal to the ``ThreholdPercentage`` to be approved.

      - **Status** *(string) --*

        The current status of the network.

      - **CreationDate** *(datetime) --*

        The date and time that the network was created.
    """


_ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef = TypedDict(
    "_ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef",
    {"PeerEndpoint": str, "PeerEventEndpoint": str},
    total=False,
)


class ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef(
    _ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef
):
    """
    Type definition for `ClientGetNodeResponseNodeFrameworkAttributes` `Fabric`

    Attributes of Hyperledger Fabric for a peer node on a Managed Blockchain network that
    uses Hyperledger Fabric.

    - **PeerEndpoint** *(string) --*

      The endpoint that identifies the peer node for all services except peer channel-based
      event services.

    - **PeerEventEndpoint** *(string) --*

      The endpoint that identifies the peer node for peer channel-based event services.
    """


_ClientGetNodeResponseNodeFrameworkAttributesTypeDef = TypedDict(
    "_ClientGetNodeResponseNodeFrameworkAttributesTypeDef",
    {"Fabric": ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef},
    total=False,
)


class ClientGetNodeResponseNodeFrameworkAttributesTypeDef(
    _ClientGetNodeResponseNodeFrameworkAttributesTypeDef
):
    """
    Type definition for `ClientGetNodeResponseNode` `FrameworkAttributes`

    Attributes of the blockchain framework being used.

    - **Fabric** *(dict) --*

      Attributes of Hyperledger Fabric for a peer node on a Managed Blockchain network that
      uses Hyperledger Fabric.

      - **PeerEndpoint** *(string) --*

        The endpoint that identifies the peer node for all services except peer channel-based
        event services.

      - **PeerEventEndpoint** *(string) --*

        The endpoint that identifies the peer node for peer channel-based event services.
    """


_ClientGetNodeResponseNodeTypeDef = TypedDict(
    "_ClientGetNodeResponseNodeTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "Id": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "FrameworkAttributes": ClientGetNodeResponseNodeFrameworkAttributesTypeDef,
        "Status": str,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetNodeResponseNodeTypeDef(_ClientGetNodeResponseNodeTypeDef):
    """
    Type definition for `ClientGetNodeResponse` `Node`

    Properties of the node configuration.

    - **NetworkId** *(string) --*

      The unique identifier of the network that the node is in.

    - **MemberId** *(string) --*

      The unique identifier of the member to which the node belongs.

    - **Id** *(string) --*

      The unique identifier of the node.

    - **InstanceType** *(string) --*

      The instance type of the node.

    - **AvailabilityZone** *(string) --*

      The Availability Zone in which the node exists.

    - **FrameworkAttributes** *(dict) --*

      Attributes of the blockchain framework being used.

      - **Fabric** *(dict) --*

        Attributes of Hyperledger Fabric for a peer node on a Managed Blockchain network that
        uses Hyperledger Fabric.

        - **PeerEndpoint** *(string) --*

          The endpoint that identifies the peer node for all services except peer channel-based
          event services.

        - **PeerEventEndpoint** *(string) --*

          The endpoint that identifies the peer node for peer channel-based event services.

    - **Status** *(string) --*

      The status of the node.

    - **CreationDate** *(datetime) --*

      The date and time that the node was created.
    """


_ClientGetNodeResponseTypeDef = TypedDict(
    "_ClientGetNodeResponseTypeDef",
    {"Node": ClientGetNodeResponseNodeTypeDef},
    total=False,
)


class ClientGetNodeResponseTypeDef(_ClientGetNodeResponseTypeDef):
    """
    Type definition for `ClientGetNode` `Response`

    - **Node** *(dict) --*

      Properties of the node configuration.

      - **NetworkId** *(string) --*

        The unique identifier of the network that the node is in.

      - **MemberId** *(string) --*

        The unique identifier of the member to which the node belongs.

      - **Id** *(string) --*

        The unique identifier of the node.

      - **InstanceType** *(string) --*

        The instance type of the node.

      - **AvailabilityZone** *(string) --*

        The Availability Zone in which the node exists.

      - **FrameworkAttributes** *(dict) --*

        Attributes of the blockchain framework being used.

        - **Fabric** *(dict) --*

          Attributes of Hyperledger Fabric for a peer node on a Managed Blockchain network that
          uses Hyperledger Fabric.

          - **PeerEndpoint** *(string) --*

            The endpoint that identifies the peer node for all services except peer channel-based
            event services.

          - **PeerEventEndpoint** *(string) --*

            The endpoint that identifies the peer node for peer channel-based event services.

      - **Status** *(string) --*

        The status of the node.

      - **CreationDate** *(datetime) --*

        The date and time that the node was created.
    """


_ClientGetProposalResponseProposalActionsInvitationsTypeDef = TypedDict(
    "_ClientGetProposalResponseProposalActionsInvitationsTypeDef",
    {"Principal": str},
    total=False,
)


class ClientGetProposalResponseProposalActionsInvitationsTypeDef(
    _ClientGetProposalResponseProposalActionsInvitationsTypeDef
):
    """
    Type definition for `ClientGetProposalResponseProposalActions` `Invitations`

    An action to invite a specific AWS account to create a member and join the network. The
    ``InviteAction`` is carried out when a ``Proposal`` is ``APPROVED`` .

    - **Principal** *(string) --*

      The AWS account ID to invite.
    """


_ClientGetProposalResponseProposalActionsRemovalsTypeDef = TypedDict(
    "_ClientGetProposalResponseProposalActionsRemovalsTypeDef",
    {"MemberId": str},
    total=False,
)


class ClientGetProposalResponseProposalActionsRemovalsTypeDef(
    _ClientGetProposalResponseProposalActionsRemovalsTypeDef
):
    """
    Type definition for `ClientGetProposalResponseProposalActions` `Removals`

    An action to remove a member from a Managed Blockchain network as the result of a
    removal proposal that is ``APPROVED`` . The member and all associated resources are
    deleted from the network.

    - **MemberId** *(string) --*

      The unique identifier of the member to remove.
    """


_ClientGetProposalResponseProposalActionsTypeDef = TypedDict(
    "_ClientGetProposalResponseProposalActionsTypeDef",
    {
        "Invitations": List[ClientGetProposalResponseProposalActionsInvitationsTypeDef],
        "Removals": List[ClientGetProposalResponseProposalActionsRemovalsTypeDef],
    },
    total=False,
)


class ClientGetProposalResponseProposalActionsTypeDef(
    _ClientGetProposalResponseProposalActionsTypeDef
):
    """
    Type definition for `ClientGetProposalResponseProposal` `Actions`

    The actions to perform on the network if the proposal is ``APPROVED`` .

    - **Invitations** *(list) --*

      The actions to perform for an ``APPROVED`` proposal to invite an AWS account to create a
      member and join the network.

      - *(dict) --*

        An action to invite a specific AWS account to create a member and join the network. The
        ``InviteAction`` is carried out when a ``Proposal`` is ``APPROVED`` .

        - **Principal** *(string) --*

          The AWS account ID to invite.

    - **Removals** *(list) --*

      The actions to perform for an ``APPROVED`` proposal to remove a member from the network,
      which deletes the member and all associated member resources from the network.

      - *(dict) --*

        An action to remove a member from a Managed Blockchain network as the result of a
        removal proposal that is ``APPROVED`` . The member and all associated resources are
        deleted from the network.

        - **MemberId** *(string) --*

          The unique identifier of the member to remove.
    """


_ClientGetProposalResponseProposalTypeDef = TypedDict(
    "_ClientGetProposalResponseProposalTypeDef",
    {
        "ProposalId": str,
        "NetworkId": str,
        "Description": str,
        "Actions": ClientGetProposalResponseProposalActionsTypeDef,
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": str,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "YesVoteCount": int,
        "NoVoteCount": int,
        "OutstandingVoteCount": int,
    },
    total=False,
)


class ClientGetProposalResponseProposalTypeDef(
    _ClientGetProposalResponseProposalTypeDef
):
    """
    Type definition for `ClientGetProposalResponse` `Proposal`

    Information about a proposal.

    - **ProposalId** *(string) --*

      The unique identifier of the proposal.

    - **NetworkId** *(string) --*

      The unique identifier of the network for which the proposal is made.

    - **Description** *(string) --*

      The description of the proposal.

    - **Actions** *(dict) --*

      The actions to perform on the network if the proposal is ``APPROVED`` .

      - **Invitations** *(list) --*

        The actions to perform for an ``APPROVED`` proposal to invite an AWS account to create a
        member and join the network.

        - *(dict) --*

          An action to invite a specific AWS account to create a member and join the network. The
          ``InviteAction`` is carried out when a ``Proposal`` is ``APPROVED`` .

          - **Principal** *(string) --*

            The AWS account ID to invite.

      - **Removals** *(list) --*

        The actions to perform for an ``APPROVED`` proposal to remove a member from the network,
        which deletes the member and all associated member resources from the network.

        - *(dict) --*

          An action to remove a member from a Managed Blockchain network as the result of a
          removal proposal that is ``APPROVED`` . The member and all associated resources are
          deleted from the network.

          - **MemberId** *(string) --*

            The unique identifier of the member to remove.

    - **ProposedByMemberId** *(string) --*

      The unique identifier of the member that created the proposal.

    - **ProposedByMemberName** *(string) --*

      The name of the member that created the proposal.

    - **Status** *(string) --*

      The status of the proposal. Values are as follows:

      * ``IN_PROGRESS`` - The proposal is active and open for member voting.

      * ``APPROVED`` - The proposal was approved with sufficient ``YES`` votes among members
      according to the ``VotingPolicy`` specified for the ``Network`` . The specified proposal
      actions are carried out.

      * ``REJECTED`` - The proposal was rejected with insufficient ``YES`` votes among members
      according to the ``VotingPolicy`` specified for the ``Network`` . The specified
      ``ProposalActions`` are not carried out.

      * ``EXPIRED`` - Members did not cast the number of votes required to determine the proposal
      outcome before the proposal expired. The specified ``ProposalActions`` are not carried out.

      * ``ACTION_FAILED`` - One or more of the specified ``ProposalActions`` in a proposal that
      was approved could not be completed because of an error.

    - **CreationDate** *(datetime) --*

      The date and time that the proposal was created.

    - **ExpirationDate** *(datetime) --*

      The date and time that the proposal expires. This is the ``CreationDate`` plus the
      ``ProposalDurationInHours`` that is specified in the ``ProposalThresholdPolicy`` . After
      this date and time, if members have not cast enough votes to determine the outcome
      according to the voting policy, the proposal is ``EXPIRED`` and ``Actions`` are not carried
      out.

    - **YesVoteCount** *(integer) --*

      The current total of ``YES`` votes cast on the proposal by members.

    - **NoVoteCount** *(integer) --*

      The current total of ``NO`` votes cast on the proposal by members.

    - **OutstandingVoteCount** *(integer) --*

      The number of votes remaining to be cast on the proposal by members. In other words, the
      number of members minus the sum of ``YES`` votes and ``NO`` votes.
    """


_ClientGetProposalResponseTypeDef = TypedDict(
    "_ClientGetProposalResponseTypeDef",
    {"Proposal": ClientGetProposalResponseProposalTypeDef},
    total=False,
)


class ClientGetProposalResponseTypeDef(_ClientGetProposalResponseTypeDef):
    """
    Type definition for `ClientGetProposal` `Response`

    - **Proposal** *(dict) --*

      Information about a proposal.

      - **ProposalId** *(string) --*

        The unique identifier of the proposal.

      - **NetworkId** *(string) --*

        The unique identifier of the network for which the proposal is made.

      - **Description** *(string) --*

        The description of the proposal.

      - **Actions** *(dict) --*

        The actions to perform on the network if the proposal is ``APPROVED`` .

        - **Invitations** *(list) --*

          The actions to perform for an ``APPROVED`` proposal to invite an AWS account to create a
          member and join the network.

          - *(dict) --*

            An action to invite a specific AWS account to create a member and join the network. The
            ``InviteAction`` is carried out when a ``Proposal`` is ``APPROVED`` .

            - **Principal** *(string) --*

              The AWS account ID to invite.

        - **Removals** *(list) --*

          The actions to perform for an ``APPROVED`` proposal to remove a member from the network,
          which deletes the member and all associated member resources from the network.

          - *(dict) --*

            An action to remove a member from a Managed Blockchain network as the result of a
            removal proposal that is ``APPROVED`` . The member and all associated resources are
            deleted from the network.

            - **MemberId** *(string) --*

              The unique identifier of the member to remove.

      - **ProposedByMemberId** *(string) --*

        The unique identifier of the member that created the proposal.

      - **ProposedByMemberName** *(string) --*

        The name of the member that created the proposal.

      - **Status** *(string) --*

        The status of the proposal. Values are as follows:

        * ``IN_PROGRESS`` - The proposal is active and open for member voting.

        * ``APPROVED`` - The proposal was approved with sufficient ``YES`` votes among members
        according to the ``VotingPolicy`` specified for the ``Network`` . The specified proposal
        actions are carried out.

        * ``REJECTED`` - The proposal was rejected with insufficient ``YES`` votes among members
        according to the ``VotingPolicy`` specified for the ``Network`` . The specified
        ``ProposalActions`` are not carried out.

        * ``EXPIRED`` - Members did not cast the number of votes required to determine the proposal
        outcome before the proposal expired. The specified ``ProposalActions`` are not carried out.

        * ``ACTION_FAILED`` - One or more of the specified ``ProposalActions`` in a proposal that
        was approved could not be completed because of an error.

      - **CreationDate** *(datetime) --*

        The date and time that the proposal was created.

      - **ExpirationDate** *(datetime) --*

        The date and time that the proposal expires. This is the ``CreationDate`` plus the
        ``ProposalDurationInHours`` that is specified in the ``ProposalThresholdPolicy`` . After
        this date and time, if members have not cast enough votes to determine the outcome
        according to the voting policy, the proposal is ``EXPIRED`` and ``Actions`` are not carried
        out.

      - **YesVoteCount** *(integer) --*

        The current total of ``YES`` votes cast on the proposal by members.

      - **NoVoteCount** *(integer) --*

        The current total of ``NO`` votes cast on the proposal by members.

      - **OutstandingVoteCount** *(integer) --*

        The number of votes remaining to be cast on the proposal by members. In other words, the
        number of members minus the sum of ``YES`` votes and ``NO`` votes.
    """


_ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef = TypedDict(
    "_ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": str,
        "FrameworkVersion": str,
        "Status": str,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef(
    _ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef
):
    """
    Type definition for `ClientListInvitationsResponseInvitations` `NetworkSummary`

    A summary of network configuration properties.

    - **Id** *(string) --*

      The unique identifier of the network.

    - **Name** *(string) --*

      The name of the network.

    - **Description** *(string) --*

      An optional description of the network.

    - **Framework** *(string) --*

      The blockchain framework that the network uses.

    - **FrameworkVersion** *(string) --*

      The version of the blockchain framework that the network uses.

    - **Status** *(string) --*

      The current status of the network.

    - **CreationDate** *(datetime) --*

      The date and time that the network was created.
    """


_ClientListInvitationsResponseInvitationsTypeDef = TypedDict(
    "_ClientListInvitationsResponseInvitationsTypeDef",
    {
        "InvitationId": str,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "Status": str,
        "NetworkSummary": ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef,
    },
    total=False,
)


class ClientListInvitationsResponseInvitationsTypeDef(
    _ClientListInvitationsResponseInvitationsTypeDef
):
    """
    Type definition for `ClientListInvitationsResponse` `Invitations`

    An invitation to an AWS account to create a member and join the network.

    - **InvitationId** *(string) --*

      The unique identifier for the invitation.

    - **CreationDate** *(datetime) --*

      The date and time that the invitation was created.

    - **ExpirationDate** *(datetime) --*

      The date and time that the invitation expires. This is the ``CreationDate`` plus the
      ``ProposalDurationInHours`` that is specified in the ``ProposalThresholdPolicy`` . After
      this date and time, the invitee can no longer create a member and join the network using
      this ``InvitationId`` .

    - **Status** *(string) --*

      The status of the invitation:

      * ``PENDING`` - The invitee has not created a member to join the network, and the
      invitation has not yet expired.

      * ``ACCEPTING`` - The invitee has begun creating a member, and creation has not yet
      completed.

      * ``ACCEPTED`` - The invitee created a member and joined the network using the
      ``InvitationID`` .

      * ``REJECTED`` - The invitee rejected the invitation.

      * ``EXPIRED`` - The invitee neither created a member nor rejected the invitation before
      the ``ExpirationDate`` .

    - **NetworkSummary** *(dict) --*

      A summary of network configuration properties.

      - **Id** *(string) --*

        The unique identifier of the network.

      - **Name** *(string) --*

        The name of the network.

      - **Description** *(string) --*

        An optional description of the network.

      - **Framework** *(string) --*

        The blockchain framework that the network uses.

      - **FrameworkVersion** *(string) --*

        The version of the blockchain framework that the network uses.

      - **Status** *(string) --*

        The current status of the network.

      - **CreationDate** *(datetime) --*

        The date and time that the network was created.
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

      The invitations for the network.

      - *(dict) --*

        An invitation to an AWS account to create a member and join the network.

        - **InvitationId** *(string) --*

          The unique identifier for the invitation.

        - **CreationDate** *(datetime) --*

          The date and time that the invitation was created.

        - **ExpirationDate** *(datetime) --*

          The date and time that the invitation expires. This is the ``CreationDate`` plus the
          ``ProposalDurationInHours`` that is specified in the ``ProposalThresholdPolicy`` . After
          this date and time, the invitee can no longer create a member and join the network using
          this ``InvitationId`` .

        - **Status** *(string) --*

          The status of the invitation:

          * ``PENDING`` - The invitee has not created a member to join the network, and the
          invitation has not yet expired.

          * ``ACCEPTING`` - The invitee has begun creating a member, and creation has not yet
          completed.

          * ``ACCEPTED`` - The invitee created a member and joined the network using the
          ``InvitationID`` .

          * ``REJECTED`` - The invitee rejected the invitation.

          * ``EXPIRED`` - The invitee neither created a member nor rejected the invitation before
          the ``ExpirationDate`` .

        - **NetworkSummary** *(dict) --*

          A summary of network configuration properties.

          - **Id** *(string) --*

            The unique identifier of the network.

          - **Name** *(string) --*

            The name of the network.

          - **Description** *(string) --*

            An optional description of the network.

          - **Framework** *(string) --*

            The blockchain framework that the network uses.

          - **FrameworkVersion** *(string) --*

            The version of the blockchain framework that the network uses.

          - **Status** *(string) --*

            The current status of the network.

          - **CreationDate** *(datetime) --*

            The date and time that the network was created.

    - **NextToken** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientListMembersResponseMembersTypeDef = TypedDict(
    "_ClientListMembersResponseMembersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": str,
        "CreationDate": datetime,
        "IsOwned": bool,
    },
    total=False,
)


class ClientListMembersResponseMembersTypeDef(_ClientListMembersResponseMembersTypeDef):
    """
    Type definition for `ClientListMembersResponse` `Members`

    A summary of configuration properties for a member.

    - **Id** *(string) --*

      The unique identifier of the member.

    - **Name** *(string) --*

      The name of the member.

    - **Description** *(string) --*

      An optional description of the member.

    - **Status** *(string) --*

      The status of the member.

      * ``CREATING`` - The AWS account is in the process of creating a member.

      * ``AVAILABLE`` - The member has been created and can participate in the network.

      * ``CREATE_FAILED`` - The AWS account attempted to create a member and creation failed.

      * ``DELETING`` - The member and all associated resources are in the process of being
      deleted. Either the AWS account that owns the member deleted it, or the member is being
      deleted as the result of an ``APPROVED``  ``PROPOSAL`` to remove the member.

      * ``DELETED`` - The member can no longer participate on the network and all associated
      resources are deleted. Either the AWS account that owns the member deleted it, or the
      member is being deleted as the result of an ``APPROVED``  ``PROPOSAL`` to remove the
      member.

    - **CreationDate** *(datetime) --*

      The date and time that the member was created.

    - **IsOwned** *(boolean) --*

      An indicator of whether the member is owned by your AWS account or a different AWS
      account.
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

      An array of ``MemberSummary`` objects. Each object contains details about a network member.

      - *(dict) --*

        A summary of configuration properties for a member.

        - **Id** *(string) --*

          The unique identifier of the member.

        - **Name** *(string) --*

          The name of the member.

        - **Description** *(string) --*

          An optional description of the member.

        - **Status** *(string) --*

          The status of the member.

          * ``CREATING`` - The AWS account is in the process of creating a member.

          * ``AVAILABLE`` - The member has been created and can participate in the network.

          * ``CREATE_FAILED`` - The AWS account attempted to create a member and creation failed.

          * ``DELETING`` - The member and all associated resources are in the process of being
          deleted. Either the AWS account that owns the member deleted it, or the member is being
          deleted as the result of an ``APPROVED``  ``PROPOSAL`` to remove the member.

          * ``DELETED`` - The member can no longer participate on the network and all associated
          resources are deleted. Either the AWS account that owns the member deleted it, or the
          member is being deleted as the result of an ``APPROVED``  ``PROPOSAL`` to remove the
          member.

        - **CreationDate** *(datetime) --*

          The date and time that the member was created.

        - **IsOwned** *(boolean) --*

          An indicator of whether the member is owned by your AWS account or a different AWS
          account.

    - **NextToken** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientListNetworksResponseNetworksTypeDef = TypedDict(
    "_ClientListNetworksResponseNetworksTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": str,
        "FrameworkVersion": str,
        "Status": str,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientListNetworksResponseNetworksTypeDef(
    _ClientListNetworksResponseNetworksTypeDef
):
    """
    Type definition for `ClientListNetworksResponse` `Networks`

    A summary of network configuration properties.

    - **Id** *(string) --*

      The unique identifier of the network.

    - **Name** *(string) --*

      The name of the network.

    - **Description** *(string) --*

      An optional description of the network.

    - **Framework** *(string) --*

      The blockchain framework that the network uses.

    - **FrameworkVersion** *(string) --*

      The version of the blockchain framework that the network uses.

    - **Status** *(string) --*

      The current status of the network.

    - **CreationDate** *(datetime) --*

      The date and time that the network was created.
    """


_ClientListNetworksResponseTypeDef = TypedDict(
    "_ClientListNetworksResponseTypeDef",
    {"Networks": List[ClientListNetworksResponseNetworksTypeDef], "NextToken": str},
    total=False,
)


class ClientListNetworksResponseTypeDef(_ClientListNetworksResponseTypeDef):
    """
    Type definition for `ClientListNetworks` `Response`

    - **Networks** *(list) --*

      An array of ``NetworkSummary`` objects that contain configuration properties for each network.

      - *(dict) --*

        A summary of network configuration properties.

        - **Id** *(string) --*

          The unique identifier of the network.

        - **Name** *(string) --*

          The name of the network.

        - **Description** *(string) --*

          An optional description of the network.

        - **Framework** *(string) --*

          The blockchain framework that the network uses.

        - **FrameworkVersion** *(string) --*

          The version of the blockchain framework that the network uses.

        - **Status** *(string) --*

          The current status of the network.

        - **CreationDate** *(datetime) --*

          The date and time that the network was created.

    - **NextToken** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientListNodesResponseNodesTypeDef = TypedDict(
    "_ClientListNodesResponseNodesTypeDef",
    {
        "Id": str,
        "Status": str,
        "CreationDate": datetime,
        "AvailabilityZone": str,
        "InstanceType": str,
    },
    total=False,
)


class ClientListNodesResponseNodesTypeDef(_ClientListNodesResponseNodesTypeDef):
    """
    Type definition for `ClientListNodesResponse` `Nodes`

    A summary of configuration properties for a peer node.

    - **Id** *(string) --*

      The unique identifier of the node.

    - **Status** *(string) --*

      The status of the node.

    - **CreationDate** *(datetime) --*

      The date and time that the node was created.

    - **AvailabilityZone** *(string) --*

      The Availability Zone in which the node exists.

    - **InstanceType** *(string) --*

      The EC2 instance type for the node.
    """


_ClientListNodesResponseTypeDef = TypedDict(
    "_ClientListNodesResponseTypeDef",
    {"Nodes": List[ClientListNodesResponseNodesTypeDef], "NextToken": str},
    total=False,
)


class ClientListNodesResponseTypeDef(_ClientListNodesResponseTypeDef):
    """
    Type definition for `ClientListNodes` `Response`

    - **Nodes** *(list) --*

      An array of ``NodeSummary`` objects that contain configuration properties for each node.

      - *(dict) --*

        A summary of configuration properties for a peer node.

        - **Id** *(string) --*

          The unique identifier of the node.

        - **Status** *(string) --*

          The status of the node.

        - **CreationDate** *(datetime) --*

          The date and time that the node was created.

        - **AvailabilityZone** *(string) --*

          The Availability Zone in which the node exists.

        - **InstanceType** *(string) --*

          The EC2 instance type for the node.

    - **NextToken** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientListProposalVotesResponseProposalVotesTypeDef = TypedDict(
    "_ClientListProposalVotesResponseProposalVotesTypeDef",
    {"Vote": str, "MemberName": str, "MemberId": str},
    total=False,
)


class ClientListProposalVotesResponseProposalVotesTypeDef(
    _ClientListProposalVotesResponseProposalVotesTypeDef
):
    """
    Type definition for `ClientListProposalVotesResponse` `ProposalVotes`

    Properties of an individual vote that a member cast for a proposal.

    - **Vote** *(string) --*

      The vote value, either ``YES`` or ``NO`` .

    - **MemberName** *(string) --*

      The name of the member that cast the vote.

    - **MemberId** *(string) --*

      The unique identifier of the member that cast the vote.
    """


_ClientListProposalVotesResponseTypeDef = TypedDict(
    "_ClientListProposalVotesResponseTypeDef",
    {
        "ProposalVotes": List[ClientListProposalVotesResponseProposalVotesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListProposalVotesResponseTypeDef(_ClientListProposalVotesResponseTypeDef):
    """
    Type definition for `ClientListProposalVotes` `Response`

    - **ProposalVotes** *(list) --*

      The listing of votes.

      - *(dict) --*

        Properties of an individual vote that a member cast for a proposal.

        - **Vote** *(string) --*

          The vote value, either ``YES`` or ``NO`` .

        - **MemberName** *(string) --*

          The name of the member that cast the vote.

        - **MemberId** *(string) --*

          The unique identifier of the member that cast the vote.

    - **NextToken** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientListProposalsResponseProposalsTypeDef = TypedDict(
    "_ClientListProposalsResponseProposalsTypeDef",
    {
        "ProposalId": str,
        "Description": str,
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": str,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
    },
    total=False,
)


class ClientListProposalsResponseProposalsTypeDef(
    _ClientListProposalsResponseProposalsTypeDef
):
    """
    Type definition for `ClientListProposalsResponse` `Proposals`

    Properties of a proposal.

    - **ProposalId** *(string) --*

      The unique identifier of the proposal.

    - **Description** *(string) --*

      The description of the proposal.

    - **ProposedByMemberId** *(string) --*

      The unique identifier of the member that created the proposal.

    - **ProposedByMemberName** *(string) --*

      The name of the member that created the proposal.

    - **Status** *(string) --*

      The status of the proposal. Values are as follows:

      * ``IN_PROGRESS`` - The proposal is active and open for member voting.

      * ``APPROVED`` - The proposal was approved with sufficient ``YES`` votes among members
      according to the ``VotingPolicy`` specified for the ``Network`` . The specified proposal
      actions are carried out.

      * ``REJECTED`` - The proposal was rejected with insufficient ``YES`` votes among members
      according to the ``VotingPolicy`` specified for the ``Network`` . The specified
      ``ProposalActions`` are not carried out.

      * ``EXPIRED`` - Members did not cast the number of votes required to determine the
      proposal outcome before the proposal expired. The specified ``ProposalActions`` are not
      carried out.

      * ``ACTION_FAILED`` - One or more of the specified ``ProposalActions`` in a proposal that
      was approved could not be completed because of an error.

    - **CreationDate** *(datetime) --*

      The date and time that the proposal was created.

    - **ExpirationDate** *(datetime) --*

      The date and time that the proposal expires. This is the ``CreationDate`` plus the
      ``ProposalDurationInHours`` that is specified in the ``ProposalThresholdPolicy`` . After
      this date and time, if members have not cast enough votes to determine the outcome
      according to the voting policy, the proposal is ``EXPIRED`` and ``Actions`` are not
      carried out.
    """


_ClientListProposalsResponseTypeDef = TypedDict(
    "_ClientListProposalsResponseTypeDef",
    {"Proposals": List[ClientListProposalsResponseProposalsTypeDef], "NextToken": str},
    total=False,
)


class ClientListProposalsResponseTypeDef(_ClientListProposalsResponseTypeDef):
    """
    Type definition for `ClientListProposals` `Response`

    - **Proposals** *(list) --*

      The summary of each proposal made on the network.

      - *(dict) --*

        Properties of a proposal.

        - **ProposalId** *(string) --*

          The unique identifier of the proposal.

        - **Description** *(string) --*

          The description of the proposal.

        - **ProposedByMemberId** *(string) --*

          The unique identifier of the member that created the proposal.

        - **ProposedByMemberName** *(string) --*

          The name of the member that created the proposal.

        - **Status** *(string) --*

          The status of the proposal. Values are as follows:

          * ``IN_PROGRESS`` - The proposal is active and open for member voting.

          * ``APPROVED`` - The proposal was approved with sufficient ``YES`` votes among members
          according to the ``VotingPolicy`` specified for the ``Network`` . The specified proposal
          actions are carried out.

          * ``REJECTED`` - The proposal was rejected with insufficient ``YES`` votes among members
          according to the ``VotingPolicy`` specified for the ``Network`` . The specified
          ``ProposalActions`` are not carried out.

          * ``EXPIRED`` - Members did not cast the number of votes required to determine the
          proposal outcome before the proposal expired. The specified ``ProposalActions`` are not
          carried out.

          * ``ACTION_FAILED`` - One or more of the specified ``ProposalActions`` in a proposal that
          was approved could not be completed because of an error.

        - **CreationDate** *(datetime) --*

          The date and time that the proposal was created.

        - **ExpirationDate** *(datetime) --*

          The date and time that the proposal expires. This is the ``CreationDate`` plus the
          ``ProposalDurationInHours`` that is specified in the ``ProposalThresholdPolicy`` . After
          this date and time, if members have not cast enough votes to determine the outcome
          according to the voting policy, the proposal is ``EXPIRED`` and ``Actions`` are not
          carried out.

    - **NextToken** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """
