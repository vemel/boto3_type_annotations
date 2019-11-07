from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeCases(Paginator):
    def paginate(
        self,
        caseIdList: Optional[List] = None,
        displayId: Optional[str] = None,
        afterTime: Optional[str] = None,
        beforeTime: Optional[str] = None,
        includeResolvedCases: Optional[bool] = None,
        language: Optional[str] = None,
        includeCommunications: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeCommunications(Paginator):
    def paginate(
        self,
        caseId: str,
        beforeTime: Optional[str] = None,
        afterTime: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

