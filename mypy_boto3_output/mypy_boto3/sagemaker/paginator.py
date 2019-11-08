from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListAlgorithms(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: str = None,
        SortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListCodeRepositories(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: str = None,
        SortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListCompilationJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: str = None,
        SortBy: str = None,
        SortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListEndpointConfigs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SortBy: str = None,
        SortOrder: str = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListEndpoints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SortBy: str = None,
        SortOrder: str = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListHyperParameterTuningJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SortBy: str = None,
        SortOrder: str = None,
        NameContains: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        StatusEquals: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListLabelingJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: str = None,
        SortOrder: str = None,
        StatusEquals: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListLabelingJobsForWorkteam(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        WorkteamArn: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        JobReferenceCodeContains: str = None,
        SortBy: str = None,
        SortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListModelPackages(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: str = None,
        SortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListModels(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SortBy: str = None,
        SortOrder: str = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListNotebookInstanceLifecycleConfigs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SortBy: str = None,
        SortOrder: str = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListNotebookInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SortBy: str = None,
        SortOrder: str = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: str = None,
        NotebookInstanceLifecycleConfigNameContains: str = None,
        DefaultCodeRepositoryContains: str = None,
        AdditionalCodeRepositoryEquals: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListSubscribedWorkteams(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, NameContains: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTrainingJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: str = None,
        SortBy: str = None,
        SortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTrainingJobsForHyperParameterTuningJob(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        HyperParameterTuningJobName: str,
        StatusEquals: str = None,
        SortBy: str = None,
        SortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTransformJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: str = None,
        SortBy: str = None,
        SortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListWorkteams(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SortBy: str = None,
        SortOrder: str = None,
        NameContains: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class Search(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Resource: str,
        SearchExpression: Dict[str, Any] = None,
        SortBy: str = None,
        SortOrder: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
