from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def accept_qualification_request(
        self, QualificationRequestId: str, IntegerValue: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def approve_assignment(
        self,
        AssignmentId: str,
        RequesterFeedback: str = None,
        OverrideRejection: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_qualification_with_worker(
        self,
        QualificationTypeId: str,
        WorkerId: str,
        IntegerValue: int = None,
        SendNotification: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_additional_assignments_for_hit(
        self,
        HITId: str,
        NumberOfAdditionalAssignments: int,
        UniqueRequestToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_hit(
        self,
        LifetimeInSeconds: int,
        AssignmentDurationInSeconds: int,
        Reward: str,
        Title: str,
        Description: str,
        MaxAssignments: int = None,
        AutoApprovalDelayInSeconds: int = None,
        Keywords: str = None,
        Question: str = None,
        RequesterAnnotation: str = None,
        QualificationRequirements: List[Any] = None,
        UniqueRequestToken: str = None,
        AssignmentReviewPolicy: Dict[str, Any] = None,
        HITReviewPolicy: Dict[str, Any] = None,
        HITLayoutId: str = None,
        HITLayoutParameters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_hit_type(
        self,
        AssignmentDurationInSeconds: int,
        Reward: str,
        Title: str,
        Description: str,
        AutoApprovalDelayInSeconds: int = None,
        Keywords: str = None,
        QualificationRequirements: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_hit_with_hit_type(
        self,
        HITTypeId: str,
        LifetimeInSeconds: int,
        MaxAssignments: int = None,
        Question: str = None,
        RequesterAnnotation: str = None,
        UniqueRequestToken: str = None,
        AssignmentReviewPolicy: Dict[str, Any] = None,
        HITReviewPolicy: Dict[str, Any] = None,
        HITLayoutId: str = None,
        HITLayoutParameters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_qualification_type(
        self,
        Name: str,
        Description: str,
        QualificationTypeStatus: str,
        Keywords: str = None,
        RetryDelayInSeconds: int = None,
        Test: str = None,
        AnswerKey: str = None,
        TestDurationInSeconds: int = None,
        AutoGranted: bool = None,
        AutoGrantedValue: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_worker_block(self, WorkerId: str, Reason: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_hit(self, HITId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_qualification_type(self, QualificationTypeId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_worker_block(self, WorkerId: str, Reason: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_qualification_from_worker(
        self, WorkerId: str, QualificationTypeId: str, Reason: str = None
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
    def get_account_balance(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_assignment(self, AssignmentId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_file_upload_url(
        self, AssignmentId: str, QuestionIdentifier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_hit(self, HITId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_qualification_score(
        self, QualificationTypeId: str, WorkerId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_qualification_type(self, QualificationTypeId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_assignments_for_hit(
        self,
        HITId: str,
        NextToken: str = None,
        MaxResults: int = None,
        AssignmentStatuses: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_bonus_payments(
        self,
        HITId: str = None,
        AssignmentId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_hits(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_hits_for_qualification_type(
        self, QualificationTypeId: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_qualification_requests(
        self,
        QualificationTypeId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_qualification_types(
        self,
        MustBeRequestable: bool,
        Query: str = None,
        MustBeOwnedByCaller: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_review_policy_results_for_hit(
        self,
        HITId: str,
        PolicyLevels: List[Any] = None,
        RetrieveActions: bool = None,
        RetrieveResults: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_reviewable_hits(
        self,
        HITTypeId: str = None,
        Status: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_worker_blocks(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_workers_with_qualification_type(
        self,
        QualificationTypeId: str,
        Status: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def notify_workers(
        self, Subject: str, MessageText: str, WorkerIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reject_assignment(
        self, AssignmentId: str, RequesterFeedback: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reject_qualification_request(
        self, QualificationRequestId: str, Reason: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_bonus(
        self,
        WorkerId: str,
        BonusAmount: str,
        AssignmentId: str,
        Reason: str,
        UniqueRequestToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_test_event_notification(
        self, Notification: Dict[str, Any], TestEventType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_expiration_for_hit(
        self, HITId: str, ExpireAt: datetime
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_hit_review_status(
        self, HITId: str, Revert: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_hit_type_of_hit(self, HITId: str, HITTypeId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_notification_settings(
        self, HITTypeId: str, Notification: Dict[str, Any] = None, Active: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_qualification_type(
        self,
        QualificationTypeId: str,
        Description: str = None,
        QualificationTypeStatus: str = None,
        Test: str = None,
        AnswerKey: str = None,
        TestDurationInSeconds: int = None,
        RetryDelayInSeconds: int = None,
        AutoGranted: bool = None,
        AutoGrantedValue: int = None,
    ) -> Dict[str, Any]:
        pass
