from datetime import datetime
from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListChannels(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDatasetContents(Paginator):
    def paginate(
        self,
        datasetName: str,
        scheduledOnOrAfter: Optional[datetime] = None,
        scheduledBefore: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDatasets(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDatastores(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPipelines(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

