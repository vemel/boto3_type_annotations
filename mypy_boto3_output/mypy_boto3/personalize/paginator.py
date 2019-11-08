from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListCampaigns(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, solutionArn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDatasetGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListDatasetImportJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, datasetArn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDatasets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListEventTrackers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListRecipes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, recipeProvider: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSchemas(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListSolutionVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, solutionArn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSolutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
