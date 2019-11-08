from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListCertificateAuthorities(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListPermissions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, CertificateAuthorityArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, CertificateAuthorityArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
