from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListComplianceStatus(Paginator):
    def paginate(
        self,
        PolicyId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListMemberAccounts(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPolicies(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

