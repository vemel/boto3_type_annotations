from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListCampaigns(Paginator):
    def paginate(
        self,
        solutionArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDatasetGroups(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDatasetImportJobs(Paginator):
    def paginate(
        self,
        datasetArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDatasets(Paginator):
    def paginate(
        self,
        datasetGroupArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEventTrackers(Paginator):
    def paginate(
        self,
        datasetGroupArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRecipes(Paginator):
    def paginate(
        self,
        recipeProvider: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSchemas(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSolutionVersions(Paginator):
    def paginate(
        self,
        solutionArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSolutions(Paginator):
    def paginate(
        self,
        datasetGroupArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

