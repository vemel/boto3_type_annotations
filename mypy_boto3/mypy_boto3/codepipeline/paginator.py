from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListActionExecutions(Paginator):
    def paginate(
        self,
        pipelineName: str,
        filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListActionTypes(Paginator):
    def paginate(
        self,
        actionOwnerFilter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPipelineExecutions(Paginator):
    def paginate(
        self,
        pipelineName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPipelines(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTagsForResource(Paginator):
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListWebhooks(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

