from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_qualification_request(
        self,
        QualificationRequestId: str,
        IntegerValue: Optional[int] = None,
    ) -> Dict:
        pass


    def approve_assignment(
        self,
        AssignmentId: str,
        RequesterFeedback: Optional[str] = None,
        OverrideRejection: Optional[bool] = None,
    ) -> Dict:
        pass


    def associate_qualification_with_worker(
        self,
        QualificationTypeId: str,
        WorkerId: str,
        IntegerValue: Optional[int] = None,
        SendNotification: Optional[bool] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_additional_assignments_for_hit(
        self,
        HITId: str,
        NumberOfAdditionalAssignments: int,
        UniqueRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_hit(
        self,
        LifetimeInSeconds: int,
        AssignmentDurationInSeconds: int,
        Reward: str,
        Title: str,
        Description: str,
        MaxAssignments: Optional[int] = None,
        AutoApprovalDelayInSeconds: Optional[int] = None,
        Keywords: Optional[str] = None,
        Question: Optional[str] = None,
        RequesterAnnotation: Optional[str] = None,
        QualificationRequirements: Optional[List] = None,
        UniqueRequestToken: Optional[str] = None,
        AssignmentReviewPolicy: Optional[Dict] = None,
        HITReviewPolicy: Optional[Dict] = None,
        HITLayoutId: Optional[str] = None,
        HITLayoutParameters: Optional[List] = None,
    ) -> Dict:
        pass


    def create_hit_type(
        self,
        AssignmentDurationInSeconds: int,
        Reward: str,
        Title: str,
        Description: str,
        AutoApprovalDelayInSeconds: Optional[int] = None,
        Keywords: Optional[str] = None,
        QualificationRequirements: Optional[List] = None,
    ) -> Dict:
        pass


    def create_hit_with_hit_type(
        self,
        HITTypeId: str,
        LifetimeInSeconds: int,
        MaxAssignments: Optional[int] = None,
        Question: Optional[str] = None,
        RequesterAnnotation: Optional[str] = None,
        UniqueRequestToken: Optional[str] = None,
        AssignmentReviewPolicy: Optional[Dict] = None,
        HITReviewPolicy: Optional[Dict] = None,
        HITLayoutId: Optional[str] = None,
        HITLayoutParameters: Optional[List] = None,
    ) -> Dict:
        pass


    def create_qualification_type(
        self,
        Name: str,
        Description: str,
        QualificationTypeStatus: str,
        Keywords: Optional[str] = None,
        RetryDelayInSeconds: Optional[int] = None,
        Test: Optional[str] = None,
        AnswerKey: Optional[str] = None,
        TestDurationInSeconds: Optional[int] = None,
        AutoGranted: Optional[bool] = None,
        AutoGrantedValue: Optional[int] = None,
    ) -> Dict:
        pass


    def create_worker_block(
        self,
        WorkerId: str,
        Reason: str,
    ) -> Dict:
        pass


    def delete_hit(
        self,
        HITId: str,
    ) -> Dict:
        pass


    def delete_qualification_type(
        self,
        QualificationTypeId: str,
    ) -> Dict:
        pass


    def delete_worker_block(
        self,
        WorkerId: str,
        Reason: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_qualification_from_worker(
        self,
        WorkerId: str,
        QualificationTypeId: str,
        Reason: Optional[str] = None,
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


    def get_account_balance(
        self,
    ) -> Dict:
        pass


    def get_assignment(
        self,
        AssignmentId: str,
    ) -> Dict:
        pass


    def get_file_upload_url(
        self,
        AssignmentId: str,
        QuestionIdentifier: str,
    ) -> Dict:
        pass


    def get_hit(
        self,
        HITId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_qualification_score(
        self,
        QualificationTypeId: str,
        WorkerId: str,
    ) -> Dict:
        pass


    def get_qualification_type(
        self,
        QualificationTypeId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_assignments_for_hit(
        self,
        HITId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        AssignmentStatuses: Optional[List] = None,
    ) -> Dict:
        pass


    def list_bonus_payments(
        self,
        HITId: Optional[str] = None,
        AssignmentId: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_hits(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_hits_for_qualification_type(
        self,
        QualificationTypeId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_qualification_requests(
        self,
        QualificationTypeId: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_qualification_types(
        self,
        MustBeRequestable: bool,
        Query: Optional[str] = None,
        MustBeOwnedByCaller: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_review_policy_results_for_hit(
        self,
        HITId: str,
        PolicyLevels: Optional[List] = None,
        RetrieveActions: Optional[bool] = None,
        RetrieveResults: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_reviewable_hits(
        self,
        HITTypeId: Optional[str] = None,
        Status: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_worker_blocks(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_workers_with_qualification_type(
        self,
        QualificationTypeId: str,
        Status: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def notify_workers(
        self,
        Subject: str,
        MessageText: str,
        WorkerIds: List,
    ) -> Dict:
        pass


    def reject_assignment(
        self,
        AssignmentId: str,
        RequesterFeedback: str,
    ) -> Dict:
        pass


    def reject_qualification_request(
        self,
        QualificationRequestId: str,
        Reason: Optional[str] = None,
    ) -> Dict:
        pass


    def send_bonus(
        self,
        WorkerId: str,
        BonusAmount: str,
        AssignmentId: str,
        Reason: str,
        UniqueRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def send_test_event_notification(
        self,
        Notification: Dict,
        TestEventType: str,
    ) -> Dict:
        pass


    def update_expiration_for_hit(
        self,
        HITId: str,
        ExpireAt: datetime,
    ) -> Dict:
        pass


    def update_hit_review_status(
        self,
        HITId: str,
        Revert: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_hit_type_of_hit(
        self,
        HITId: str,
        HITTypeId: str,
    ) -> Dict:
        pass


    def update_notification_settings(
        self,
        HITTypeId: str,
        Notification: Optional[Dict] = None,
        Active: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_qualification_type(
        self,
        QualificationTypeId: str,
        Description: Optional[str] = None,
        QualificationTypeStatus: Optional[str] = None,
        Test: Optional[str] = None,
        AnswerKey: Optional[str] = None,
        TestDurationInSeconds: Optional[int] = None,
        RetryDelayInSeconds: Optional[int] = None,
        AutoGranted: Optional[bool] = None,
        AutoGrantedValue: Optional[int] = None,
    ) -> Dict:
        pass

