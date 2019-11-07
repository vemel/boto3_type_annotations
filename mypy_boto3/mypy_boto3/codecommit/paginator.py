from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribePullRequestEvents(Paginator):
    def paginate(
        self,
        pullRequestId: str,
        pullRequestEventType: Optional[str] = None,
        actorArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetCommentsForComparedCommit(Paginator):
    def paginate(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetCommentsForPullRequest(Paginator):
    def paginate(
        self,
        pullRequestId: str,
        repositoryName: Optional[str] = None,
        beforeCommitId: Optional[str] = None,
        afterCommitId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetDifferences(Paginator):
    def paginate(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: Optional[str] = None,
        beforePath: Optional[str] = None,
        afterPath: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListBranches(Paginator):
    def paginate(
        self,
        repositoryName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPullRequests(Paginator):
    def paginate(
        self,
        repositoryName: str,
        authorArn: Optional[str] = None,
        pullRequestStatus: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRepositories(Paginator):
    def paginate(
        self,
        sortBy: Optional[str] = None,
        order: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

