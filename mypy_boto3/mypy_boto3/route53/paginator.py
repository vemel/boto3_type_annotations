from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListHealthChecks(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListHostedZones(Paginator):
    def paginate(
        self,
        DelegationSetId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListQueryLoggingConfigs(Paginator):
    def paginate(
        self,
        HostedZoneId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListResourceRecordSets(Paginator):
    def paginate(
        self,
        HostedZoneId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListVPCAssociationAuthorizations(Paginator):
    def paginate(
        self,
        HostedZoneId: str,
        MaxResults: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

