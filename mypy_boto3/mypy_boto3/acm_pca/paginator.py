from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListCertificateAuthorities(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPermissions(Paginator):
    def paginate(
        self,
        CertificateAuthorityArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTags(Paginator):
    def paginate(
        self,
        CertificateAuthorityArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

