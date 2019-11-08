from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class GetWorkflowExecutionHistory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        domain: str,
        execution: Dict[str, Any],
        reverseOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListActivityTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        domain: str,
        registrationStatus: str,
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListClosedWorkflowExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        domain: str,
        startTimeFilter: Dict[str, Any] = None,
        closeTimeFilter: Dict[str, Any] = None,
        executionFilter: Dict[str, Any] = None,
        closeStatusFilter: Dict[str, Any] = None,
        typeFilter: Dict[str, Any] = None,
        tagFilter: Dict[str, Any] = None,
        reverseOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListDomains(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        registrationStatus: str,
        reverseOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListOpenWorkflowExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        domain: str,
        startTimeFilter: Dict[str, Any],
        typeFilter: Dict[str, Any] = None,
        tagFilter: Dict[str, Any] = None,
        reverseOrder: bool = None,
        executionFilter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListWorkflowTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        domain: str,
        registrationStatus: str,
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class PollForDecisionTask(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        domain: str,
        taskList: Dict[str, Any],
        identity: str = None,
        reverseOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
