from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListAssociationsForLicenseConfiguration(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, LicenseConfigurationArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListLicenseConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        LicenseConfigurationArns: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListLicenseSpecificationsForResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListResourceInventory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUsageForLicenseConfiguration(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        LicenseConfigurationArn: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
