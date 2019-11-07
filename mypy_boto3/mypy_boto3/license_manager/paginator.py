from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListAssociationsForLicenseConfiguration(Paginator):
    def paginate(
        self,
        LicenseConfigurationArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListLicenseConfigurations(Paginator):
    def paginate(
        self,
        LicenseConfigurationArns: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListLicenseSpecificationsForResource(Paginator):
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListResourceInventory(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUsageForLicenseConfiguration(Paginator):
    def paginate(
        self,
        LicenseConfigurationArn: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

