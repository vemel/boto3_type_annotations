from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_attachments_to_set(
        self,
        attachments: List,
        attachmentSetId: Optional[str] = None,
    ) -> Dict:
        pass


    def add_communication_to_case(
        self,
        communicationBody: str,
        caseId: Optional[str] = None,
        ccEmailAddresses: Optional[List] = None,
        attachmentSetId: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_case(
        self,
        subject: str,
        communicationBody: str,
        serviceCode: Optional[str] = None,
        severityCode: Optional[str] = None,
        categoryCode: Optional[str] = None,
        ccEmailAddresses: Optional[List] = None,
        language: Optional[str] = None,
        issueType: Optional[str] = None,
        attachmentSetId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_attachment(
        self,
        attachmentId: str,
    ) -> Dict:
        pass


    def describe_cases(
        self,
        caseIdList: Optional[List] = None,
        displayId: Optional[str] = None,
        afterTime: Optional[str] = None,
        beforeTime: Optional[str] = None,
        includeResolvedCases: Optional[bool] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        language: Optional[str] = None,
        includeCommunications: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_communications(
        self,
        caseId: str,
        beforeTime: Optional[str] = None,
        afterTime: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_services(
        self,
        serviceCodeList: Optional[List] = None,
        language: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_severity_levels(
        self,
        language: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_trusted_advisor_check_refresh_statuses(
        self,
        checkIds: List,
    ) -> Dict:
        pass


    def describe_trusted_advisor_check_result(
        self,
        checkId: str,
        language: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_trusted_advisor_check_summaries(
        self,
        checkIds: List,
    ) -> Dict:
        pass


    def describe_trusted_advisor_checks(
        self,
        language: str,
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


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def refresh_trusted_advisor_check(
        self,
        checkId: str,
    ) -> Dict:
        pass


    def resolve_case(
        self,
        caseId: Optional[str] = None,
    ) -> Dict:
        pass

