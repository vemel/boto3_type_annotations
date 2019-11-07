from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListCertificates(Paginator):
    def paginate(
        self,
        CertificateStatuses: Optional[List] = None,
        Includes: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

