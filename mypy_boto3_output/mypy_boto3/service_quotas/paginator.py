from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListAWSDefaultServiceQuotas(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ServiceCode: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListRequestedServiceQuotaChangeHistory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceCode: str = None,
        Status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListRequestedServiceQuotaChangeHistoryByQuota(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListServiceQuotaIncreaseRequestsInTemplate(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceCode: str = None,
        AwsRegion: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListServiceQuotas(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ServiceCode: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListServices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
