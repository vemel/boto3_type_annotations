from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeServices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceCode: str = None,
        FormatVersion: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetAttributeValues(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceCode: str,
        AttributeName: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetProducts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceCode: str = None,
        Filters: List[Any] = None,
        FormatVersion: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
