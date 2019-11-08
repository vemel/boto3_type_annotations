from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_attachments_to_set(
        self, attachments: List[Any], attachmentSetId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_communication_to_case(
        self,
        communicationBody: str,
        caseId: str = None,
        ccEmailAddresses: List[Any] = None,
        attachmentSetId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_case(
        self,
        subject: str,
        communicationBody: str,
        serviceCode: str = None,
        severityCode: str = None,
        categoryCode: str = None,
        ccEmailAddresses: List[Any] = None,
        language: str = None,
        issueType: str = None,
        attachmentSetId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_attachment(self, attachmentId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cases(
        self,
        caseIdList: List[Any] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        nextToken: str = None,
        maxResults: int = None,
        language: str = None,
        includeCommunications: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_communications(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_services(
        self, serviceCodeList: List[Any] = None, language: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_severity_levels(self, language: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_trusted_advisor_check_refresh_statuses(
        self, checkIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_trusted_advisor_check_result(
        self, checkId: str, language: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_trusted_advisor_check_summaries(
        self, checkIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_trusted_advisor_checks(self, language: str) -> Dict[str, Any]:
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
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def refresh_trusted_advisor_check(self, checkId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def resolve_case(self, caseId: str = None) -> Dict[str, Any]:
        pass
