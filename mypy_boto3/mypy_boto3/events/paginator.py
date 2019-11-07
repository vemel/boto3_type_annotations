from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListRuleNamesByTarget(Paginator):
    def paginate(
        self,
        TargetArn: str,
        EventBusName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRules(Paginator):
    def paginate(
        self,
        NamePrefix: Optional[str] = None,
        EventBusName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTargetsByRule(Paginator):
    def paginate(
        self,
        Rule: str,
        EventBusName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

