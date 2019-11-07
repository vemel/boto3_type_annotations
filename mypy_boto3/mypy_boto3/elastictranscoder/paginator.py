from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListJobsByPipeline(Paginator):
    def paginate(
        self,
        PipelineId: str,
        Ascending: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListJobsByStatus(Paginator):
    def paginate(
        self,
        Status: str,
        Ascending: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPipelines(Paginator):
    def paginate(
        self,
        Ascending: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPresets(Paginator):
    def paginate(
        self,
        Ascending: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

