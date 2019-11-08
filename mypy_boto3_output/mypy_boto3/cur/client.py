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
    def delete_report_definition(self, ReportName: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_report_definitions(
        self, MaxResults: int = None, NextToken: str = None
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
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def modify_report_definition(
        self, ReportName: str, ReportDefinition: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_report_definition(self, ReportDefinition: Dict[str, Any]) -> Dict[str, Any]:
        pass
