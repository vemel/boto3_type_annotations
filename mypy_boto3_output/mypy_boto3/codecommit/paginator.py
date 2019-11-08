from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class DescribePullRequestEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        pullRequestId: str,
        pullRequestEventType: str = None,
        actorArn: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetCommentsForComparedCommit(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetCommentsForPullRequest(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetDifferences(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListBranches(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, repositoryName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPullRequests(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListRepositories(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        sortBy: str = None,
        order: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
