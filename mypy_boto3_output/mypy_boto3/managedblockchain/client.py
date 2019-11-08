from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_member(
        self,
        ClientRequestToken: str,
        InvitationId: str,
        NetworkId: str,
        MemberConfiguration: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_network(
        self,
        ClientRequestToken: str,
        Name: str,
        Framework: str,
        FrameworkVersion: str,
        VotingPolicy: Dict[str, Any],
        MemberConfiguration: Dict[str, Any],
        Description: str = None,
        FrameworkConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_node(
        self,
        ClientRequestToken: str,
        NetworkId: str,
        MemberId: str,
        NodeConfiguration: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_proposal(
        self,
        ClientRequestToken: str,
        NetworkId: str,
        MemberId: str,
        Actions: Dict[str, Any],
        Description: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_member(self, NetworkId: str, MemberId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_node(self, NetworkId: str, MemberId: str, NodeId: str) -> Dict[str, Any]:
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
    def get_member(self, NetworkId: str, MemberId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_network(self, NetworkId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_node(self, NetworkId: str, MemberId: str, NodeId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_proposal(self, NetworkId: str, ProposalId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_members(
        self,
        NetworkId: str,
        Name: str = None,
        Status: str = None,
        IsOwned: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_networks(
        self,
        Name: str = None,
        Framework: str = None,
        Status: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_nodes(
        self,
        NetworkId: str,
        MemberId: str,
        Status: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_proposal_votes(
        self,
        NetworkId: str,
        ProposalId: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_proposals(
        self, NetworkId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reject_invitation(self, InvitationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def vote_on_proposal(
        self, NetworkId: str, ProposalId: str, VoterMemberId: str, Vote: str
    ) -> Dict[str, Any]:
        pass
