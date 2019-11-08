from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListAssessmentRunAgents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        assessmentRunArn: str,
        filter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAssessmentRuns(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        assessmentTemplateArns: List[Any] = None,
        filter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAssessmentTargets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListAssessmentTemplates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        assessmentTargetArns: List[Any] = None,
        filter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListEventSubscriptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, resourceArn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListExclusions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, assessmentRunArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListFindings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        assessmentRunArns: List[Any] = None,
        filter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListRulesPackages(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class PreviewAgents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, previewAgentsArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
