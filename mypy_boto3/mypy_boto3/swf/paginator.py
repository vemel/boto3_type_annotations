from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class GetWorkflowExecutionHistory(Paginator):
    def paginate(
        self,
        domain: str,
        execution: Dict,
        reverseOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListActivityTypes(Paginator):
    def paginate(
        self,
        domain: str,
        registrationStatus: str,
        name: Optional[str] = None,
        reverseOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListClosedWorkflowExecutions(Paginator):
    def paginate(
        self,
        domain: str,
        startTimeFilter: Optional[Dict] = None,
        closeTimeFilter: Optional[Dict] = None,
        executionFilter: Optional[Dict] = None,
        closeStatusFilter: Optional[Dict] = None,
        typeFilter: Optional[Dict] = None,
        tagFilter: Optional[Dict] = None,
        reverseOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDomains(Paginator):
    def paginate(
        self,
        registrationStatus: str,
        reverseOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOpenWorkflowExecutions(Paginator):
    def paginate(
        self,
        domain: str,
        startTimeFilter: Dict,
        typeFilter: Optional[Dict] = None,
        tagFilter: Optional[Dict] = None,
        reverseOrder: Optional[bool] = None,
        executionFilter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListWorkflowTypes(Paginator):
    def paginate(
        self,
        domain: str,
        registrationStatus: str,
        name: Optional[str] = None,
        reverseOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class PollForDecisionTask(Paginator):
    def paginate(
        self,
        domain: str,
        taskList: Dict,
        identity: Optional[str] = None,
        reverseOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

