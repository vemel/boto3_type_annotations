from datetime import datetime
from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListAlgorithms(Paginator):
    def paginate(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        NameContains: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListCodeRepositories(Paginator):
    def paginate(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        NameContains: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListCompilationJobs(Paginator):
    def paginate(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        NameContains: Optional[str] = None,
        StatusEquals: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEndpointConfigs(Paginator):
    def paginate(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        CreationTimeBefore: Optional[datetime] = None,
        CreationTimeAfter: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEndpoints(Paginator):
    def paginate(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        CreationTimeBefore: Optional[datetime] = None,
        CreationTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        StatusEquals: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListHyperParameterTuningJobs(Paginator):
    def paginate(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        StatusEquals: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListLabelingJobs(Paginator):
    def paginate(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        NameContains: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        StatusEquals: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListLabelingJobsForWorkteam(Paginator):
    def paginate(
        self,
        WorkteamArn: str,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        JobReferenceCodeContains: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListModelPackages(Paginator):
    def paginate(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        NameContains: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListModels(Paginator):
    def paginate(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        CreationTimeBefore: Optional[datetime] = None,
        CreationTimeAfter: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListNotebookInstanceLifecycleConfigs(Paginator):
    def paginate(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        CreationTimeBefore: Optional[datetime] = None,
        CreationTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListNotebookInstances(Paginator):
    def paginate(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        CreationTimeBefore: Optional[datetime] = None,
        CreationTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        StatusEquals: Optional[str] = None,
        NotebookInstanceLifecycleConfigNameContains: Optional[str] = None,
        DefaultCodeRepositoryContains: Optional[str] = None,
        AdditionalCodeRepositoryEquals: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSubscribedWorkteams(Paginator):
    def paginate(
        self,
        NameContains: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTags(Paginator):
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTrainingJobs(Paginator):
    def paginate(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        NameContains: Optional[str] = None,
        StatusEquals: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTrainingJobsForHyperParameterTuningJob(Paginator):
    def paginate(
        self,
        HyperParameterTuningJobName: str,
        StatusEquals: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTransformJobs(Paginator):
    def paginate(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        NameContains: Optional[str] = None,
        StatusEquals: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListWorkteams(Paginator):
    def paginate(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class Search(Paginator):
    def paginate(
        self,
        Resource: str,
        SearchExpression: Optional[Dict] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

