from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class GetExecutionHistory(Paginator):
    def paginate(
        self,
        executionArn: str,
        reverseOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListActivities(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListExecutions(Paginator):
    def paginate(
        self,
        stateMachineArn: str,
        statusFilter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStateMachines(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

