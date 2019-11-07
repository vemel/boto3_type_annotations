from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class AuditReportCreated(Waiter):
    def wait(
        self,
        CertificateAuthorityArn: str,
        AuditReportId: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class CertificateAuthorityCSRCreated(Waiter):
    def wait(
        self,
        CertificateAuthorityArn: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class CertificateIssued(Waiter):
    def wait(
        self,
        CertificateAuthorityArn: str,
        CertificateArn: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

