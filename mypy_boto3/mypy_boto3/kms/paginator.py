from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListAliases(Paginator):
    def paginate(
        self,
        KeyId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListGrants(Paginator):
    def paginate(
        self,
        KeyId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListKeyPolicies(Paginator):
    def paginate(
        self,
        KeyId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListKeys(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

