from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListCertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CertificateStatuses: List[Any] = None,
        Includes: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
