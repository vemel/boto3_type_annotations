from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeBudgets(Paginator):
    def paginate(
        self,
        AccountId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeNotificationsForBudget(Paginator):
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSubscribersForNotification(Paginator):
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: Dict,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

