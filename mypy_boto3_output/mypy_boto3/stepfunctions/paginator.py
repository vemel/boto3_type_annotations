from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class GetExecutionHistory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        executionArn: str,
        reverseOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListActivities(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        stateMachineArn: str,
        statusFilter: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListStateMachines(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
