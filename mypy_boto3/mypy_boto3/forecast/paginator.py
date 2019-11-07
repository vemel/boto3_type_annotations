from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListDatasetGroups(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDatasetImportJobs(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDatasets(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListForecastExportJobs(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListForecasts(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPredictors(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

