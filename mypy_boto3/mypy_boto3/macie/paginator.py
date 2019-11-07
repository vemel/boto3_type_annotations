from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListMemberAccounts(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListS3Resources(Paginator):
    def paginate(
        self,
        memberAccountId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

