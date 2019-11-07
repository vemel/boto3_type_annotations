from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListAssignmentsForHIT(Paginator):
    def paginate(
        self,
        HITId: str,
        AssignmentStatuses: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListBonusPayments(Paginator):
    def paginate(
        self,
        HITId: Optional[str] = None,
        AssignmentId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListHITs(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListHITsForQualificationType(Paginator):
    def paginate(
        self,
        QualificationTypeId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListQualificationRequests(Paginator):
    def paginate(
        self,
        QualificationTypeId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListQualificationTypes(Paginator):
    def paginate(
        self,
        MustBeRequestable: bool,
        Query: Optional[str] = None,
        MustBeOwnedByCaller: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListReviewableHITs(Paginator):
    def paginate(
        self,
        HITTypeId: Optional[str] = None,
        Status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListWorkerBlocks(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListWorkersWithQualificationType(Paginator):
    def paginate(
        self,
        QualificationTypeId: str,
        Status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

