from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class GetFlowTemplateRevisions(Paginator):
    def paginate(
        self,
        id: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetSystemTemplateRevisions(Paginator):
    def paginate(
        self,
        id: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListFlowExecutionMessages(Paginator):
    def paginate(
        self,
        flowExecutionId: str,
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



class SearchEntities(Paginator):
    def paginate(
        self,
        entityTypes: List,
        filters: Optional[List] = None,
        namespaceVersion: Optional[int] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchFlowExecutions(Paginator):
    def paginate(
        self,
        systemInstanceId: str,
        flowExecutionId: Optional[str] = None,
        startTime: Optional[datetime] = None,
        endTime: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchFlowTemplates(Paginator):
    def paginate(
        self,
        filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchSystemInstances(Paginator):
    def paginate(
        self,
        filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchSystemTemplates(Paginator):
    def paginate(
        self,
        filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchThings(Paginator):
    def paginate(
        self,
        entityId: str,
        namespaceVersion: Optional[int] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

