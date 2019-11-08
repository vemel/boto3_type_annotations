from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeCases(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        caseIdList: List[Any] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        language: str = None,
        includeCommunications: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeCommunications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
