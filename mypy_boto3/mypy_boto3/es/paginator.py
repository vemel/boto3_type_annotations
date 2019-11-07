from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeReservedElasticsearchInstanceOfferings(Paginator):
    def paginate(
        self,
        ReservedElasticsearchInstanceOfferingId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeReservedElasticsearchInstances(Paginator):
    def paginate(
        self,
        ReservedElasticsearchInstanceId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetUpgradeHistory(Paginator):
    def paginate(
        self,
        DomainName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListElasticsearchInstanceTypes(Paginator):
    def paginate(
        self,
        ElasticsearchVersion: str,
        DomainName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListElasticsearchVersions(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

