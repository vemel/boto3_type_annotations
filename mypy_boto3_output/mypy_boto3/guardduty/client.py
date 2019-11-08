from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def accept_invitation(
        self, DetectorId: str, MasterId: str, InvitationId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def archive_findings(
        self, DetectorId: str, FindingIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_detector(
        self,
        Enable: bool,
        ClientToken: str = None,
        FindingPublishingFrequency: str = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_filter(
        self,
        DetectorId: str,
        Name: str,
        FindingCriteria: Dict[str, Any],
        Description: str = None,
        Action: str = None,
        Rank: int = None,
        ClientToken: str = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_ip_set(
        self,
        DetectorId: str,
        Name: str,
        Format: str,
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_members(
        self, DetectorId: str, AccountDetails: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_sample_findings(
        self, DetectorId: str, FindingTypes: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_threat_intel_set(
        self,
        DetectorId: str,
        Name: str,
        Format: str,
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def decline_invitations(self, AccountIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_detector(self, DetectorId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_filter(self, DetectorId: str, FilterName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_invitations(self, AccountIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_ip_set(self, DetectorId: str, IpSetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_members(self, DetectorId: str, AccountIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_threat_intel_set(
        self, DetectorId: str, ThreatIntelSetId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_from_master_account(self, DetectorId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_members(
        self, DetectorId: str, AccountIds: List[Any]
    ) -> Dict[str, Any]:
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
    def get_detector(self, DetectorId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_filter(self, DetectorId: str, FilterName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_findings(
        self,
        DetectorId: str,
        FindingIds: List[Any],
        SortCriteria: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_findings_statistics(
        self,
        DetectorId: str,
        FindingStatisticTypes: List[Any],
        FindingCriteria: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_invitations_count(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_ip_set(self, DetectorId: str, IpSetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_master_account(self, DetectorId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_members(self, DetectorId: str, AccountIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_threat_intel_set(
        self, DetectorId: str, ThreatIntelSetId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def invite_members(
        self,
        DetectorId: str,
        AccountIds: List[Any],
        DisableEmailNotification: bool = None,
        Message: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_detectors(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_filters(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_findings(
        self,
        DetectorId: str,
        FindingCriteria: Dict[str, Any] = None,
        SortCriteria: Dict[str, Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_ip_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_members(
        self,
        DetectorId: str,
        MaxResults: int = None,
        NextToken: str = None,
        OnlyAssociated: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_threat_intel_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_monitoring_members(
        self, DetectorId: str, AccountIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_monitoring_members(
        self, DetectorId: str, AccountIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def unarchive_findings(
        self, DetectorId: str, FindingIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_detector(
        self,
        DetectorId: str,
        Enable: bool = None,
        FindingPublishingFrequency: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_filter(
        self,
        DetectorId: str,
        FilterName: str,
        Description: str = None,
        Action: str = None,
        Rank: int = None,
        FindingCriteria: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_findings_feedback(
        self,
        DetectorId: str,
        FindingIds: List[Any],
        Feedback: str,
        Comments: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_ip_set(
        self,
        DetectorId: str,
        IpSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_threat_intel_set(
        self,
        DetectorId: str,
        ThreatIntelSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        pass
