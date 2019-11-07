from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeServices(Paginator):
    def paginate(
        self,
        ServiceCode: Optional[str] = None,
        FormatVersion: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetAttributeValues(Paginator):
    def paginate(
        self,
        ServiceCode: str,
        AttributeName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetProducts(Paginator):
    def paginate(
        self,
        ServiceCode: Optional[str] = None,
        Filters: Optional[List] = None,
        FormatVersion: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

