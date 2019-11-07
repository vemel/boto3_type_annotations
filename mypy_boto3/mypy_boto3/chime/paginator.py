from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListAccounts(Paginator):
    def paginate(
        self,
        Name: Optional[str] = None,
        UserEmail: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUsers(Paginator):
    def paginate(
        self,
        AccountId: str,
        UserEmail: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

