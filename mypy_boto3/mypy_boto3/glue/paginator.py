from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class GetClassifiers(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetConnections(Paginator):
    def paginate(
        self,
        CatalogId: Optional[str] = None,
        Filter: Optional[Dict] = None,
        HidePassword: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetCrawlerMetrics(Paginator):
    def paginate(
        self,
        CrawlerNameList: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetCrawlers(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetDatabases(Paginator):
    def paginate(
        self,
        CatalogId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetDevEndpoints(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetJobRuns(Paginator):
    def paginate(
        self,
        JobName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetJobs(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetPartitions(Paginator):
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: Optional[str] = None,
        Expression: Optional[str] = None,
        Segment: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetSecurityConfigurations(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTableVersions(Paginator):
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTables(Paginator):
    def paginate(
        self,
        DatabaseName: str,
        CatalogId: Optional[str] = None,
        Expression: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTriggers(Paginator):
    def paginate(
        self,
        DependentJobName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetUserDefinedFunctions(Paginator):
    def paginate(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

