from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_invitation(
        self,
        DetectorId: str,
        MasterId: str,
        InvitationId: str,
    ) -> Dict:
        pass


    def archive_findings(
        self,
        DetectorId: str,
        FindingIds: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_detector(
        self,
        Enable: bool,
        ClientToken: Optional[str] = None,
        FindingPublishingFrequency: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_filter(
        self,
        DetectorId: str,
        Name: str,
        FindingCriteria: Dict,
        Description: Optional[str] = None,
        Action: Optional[str] = None,
        Rank: Optional[int] = None,
        ClientToken: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_ip_set(
        self,
        DetectorId: str,
        Name: str,
        Format: str,
        Location: str,
        Activate: bool,
        ClientToken: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_members(
        self,
        DetectorId: str,
        AccountDetails: List,
    ) -> Dict:
        pass


    def create_sample_findings(
        self,
        DetectorId: str,
        FindingTypes: Optional[List] = None,
    ) -> Dict:
        pass


    def create_threat_intel_set(
        self,
        DetectorId: str,
        Name: str,
        Format: str,
        Location: str,
        Activate: bool,
        ClientToken: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def decline_invitations(
        self,
        AccountIds: List,
    ) -> Dict:
        pass


    def delete_detector(
        self,
        DetectorId: str,
    ) -> Dict:
        pass


    def delete_filter(
        self,
        DetectorId: str,
        FilterName: str,
    ) -> Dict:
        pass


    def delete_invitations(
        self,
        AccountIds: List,
    ) -> Dict:
        pass


    def delete_ip_set(
        self,
        DetectorId: str,
        IpSetId: str,
    ) -> Dict:
        pass


    def delete_members(
        self,
        DetectorId: str,
        AccountIds: List,
    ) -> Dict:
        pass


    def delete_threat_intel_set(
        self,
        DetectorId: str,
        ThreatIntelSetId: str,
    ) -> Dict:
        pass


    def disassociate_from_master_account(
        self,
        DetectorId: str,
    ) -> Dict:
        pass


    def disassociate_members(
        self,
        DetectorId: str,
        AccountIds: List,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_detector(
        self,
        DetectorId: str,
    ) -> Dict:
        pass


    def get_filter(
        self,
        DetectorId: str,
        FilterName: str,
    ) -> Dict:
        pass


    def get_findings(
        self,
        DetectorId: str,
        FindingIds: List,
        SortCriteria: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_findings_statistics(
        self,
        DetectorId: str,
        FindingStatisticTypes: List,
        FindingCriteria: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_invitations_count(
        self,
    ) -> Dict:
        pass


    def get_ip_set(
        self,
        DetectorId: str,
        IpSetId: str,
    ) -> Dict:
        pass


    def get_master_account(
        self,
        DetectorId: str,
    ) -> Dict:
        pass


    def get_members(
        self,
        DetectorId: str,
        AccountIds: List,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_threat_intel_set(
        self,
        DetectorId: str,
        ThreatIntelSetId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def invite_members(
        self,
        DetectorId: str,
        AccountIds: List,
        DisableEmailNotification: Optional[bool] = None,
        Message: Optional[str] = None,
    ) -> Dict:
        pass


    def list_detectors(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_filters(
        self,
        DetectorId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_findings(
        self,
        DetectorId: str,
        FindingCriteria: Optional[Dict] = None,
        SortCriteria: Optional[Dict] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_invitations(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_ip_sets(
        self,
        DetectorId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_members(
        self,
        DetectorId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        OnlyAssociated: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def list_threat_intel_sets(
        self,
        DetectorId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def start_monitoring_members(
        self,
        DetectorId: str,
        AccountIds: List,
    ) -> Dict:
        pass


    def stop_monitoring_members(
        self,
        DetectorId: str,
        AccountIds: List,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Dict,
    ) -> Dict:
        pass


    def unarchive_findings(
        self,
        DetectorId: str,
        FindingIds: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_detector(
        self,
        DetectorId: str,
        Enable: Optional[bool] = None,
        FindingPublishingFrequency: Optional[str] = None,
    ) -> Dict:
        pass


    def update_filter(
        self,
        DetectorId: str,
        FilterName: str,
        Description: Optional[str] = None,
        Action: Optional[str] = None,
        Rank: Optional[int] = None,
        FindingCriteria: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_findings_feedback(
        self,
        DetectorId: str,
        FindingIds: List,
        Feedback: str,
        Comments: Optional[str] = None,
    ) -> Dict:
        pass


    def update_ip_set(
        self,
        DetectorId: str,
        IpSetId: str,
        Name: Optional[str] = None,
        Location: Optional[str] = None,
        Activate: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_threat_intel_set(
        self,
        DetectorId: str,
        ThreatIntelSetId: str,
        Name: Optional[str] = None,
        Location: Optional[str] = None,
        Activate: Optional[bool] = None,
    ) -> Dict:
        pass

