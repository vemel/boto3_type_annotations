from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListSecrets(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

