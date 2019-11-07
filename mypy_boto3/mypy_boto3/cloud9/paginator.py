from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeEnvironmentMemberships(Paginator):
    def paginate(
        self,
        userArn: Optional[str] = None,
        environmentId: Optional[str] = None,
        permissions: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEnvironments(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

