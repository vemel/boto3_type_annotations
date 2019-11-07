from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListAWSDefaultServiceQuotas(Paginator):
    def paginate(
        self,
        ServiceCode: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRequestedServiceQuotaChangeHistory(Paginator):
    def paginate(
        self,
        ServiceCode: Optional[str] = None,
        Status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRequestedServiceQuotaChangeHistoryByQuota(Paginator):
    def paginate(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListServiceQuotaIncreaseRequestsInTemplate(Paginator):
    def paginate(
        self,
        ServiceCode: Optional[str] = None,
        AwsRegion: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListServiceQuotas(Paginator):
    def paginate(
        self,
        ServiceCode: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListServices(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

