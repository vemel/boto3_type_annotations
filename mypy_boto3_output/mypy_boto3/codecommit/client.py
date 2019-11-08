from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def batch_describe_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: str,
        maxMergeHunks: int = None,
        maxConflictFiles: int = None,
        filePaths: List[Any] = None,
        conflictDetailLevel: str = None,
        conflictResolutionStrategy: str = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_commits(
        self, commitIds: List[Any], repositoryName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_repositories(self, repositoryNames: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_branch(
        self, repositoryName: str, branchName: str, commitId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_commit(
        self,
        repositoryName: str,
        branchName: str,
        parentCommitId: str = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        putFiles: List[Any] = None,
        deleteFiles: List[Any] = None,
        setFileModes: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_pull_request(
        self,
        title: str,
        targets: List[Any],
        description: str = None,
        clientRequestToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_repository(
        self,
        repositoryName: str,
        repositoryDescription: str = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_unreferenced_merge_commit(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        mergeOption: str,
        conflictDetailLevel: str = None,
        conflictResolutionStrategy: str = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_branch(self, repositoryName: str, branchName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_comment_content(self, commentId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_file(
        self,
        repositoryName: str,
        branchName: str,
        filePath: str,
        parentCommitId: str,
        keepEmptyFolders: bool = None,
        commitMessage: str = None,
        name: str = None,
        email: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_repository(self, repositoryName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: str,
        filePath: str,
        maxMergeHunks: int = None,
        conflictDetailLevel: str = None,
        conflictResolutionStrategy: str = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_pull_request_events(
        self,
        pullRequestId: str,
        pullRequestEventType: str = None,
        actorArn: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_blob(self, repositoryName: str, blobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_branch(
        self, repositoryName: str = None, branchName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_comment(self, commentId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_comments_for_compared_commit(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_comments_for_pull_request(
        self,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_commit(self, repositoryName: str, commitId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_differences(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_file(
        self, repositoryName: str, filePath: str, commitSpecifier: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_folder(
        self, repositoryName: str, folderPath: str, commitSpecifier: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_merge_commit(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: str = None,
        conflictResolutionStrategy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: str,
        conflictDetailLevel: str = None,
        maxConflictFiles: int = None,
        conflictResolutionStrategy: str = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_merge_options(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: str = None,
        conflictResolutionStrategy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_pull_request(self, pullRequestId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_repository(self, repositoryName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_repository_triggers(self, repositoryName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_branches(
        self, repositoryName: str, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_pull_requests(
        self,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_repositories(
        self, nextToken: str = None, sortBy: str = None, order: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def merge_branches_by_fast_forward(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def merge_branches_by_squash(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
        conflictDetailLevel: str = None,
        conflictResolutionStrategy: str = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def merge_branches_by_three_way(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
        conflictDetailLevel: str = None,
        conflictResolutionStrategy: str = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def merge_pull_request_by_fast_forward(
        self, pullRequestId: str, repositoryName: str, sourceCommitId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def merge_pull_request_by_squash(
        self,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str = None,
        conflictDetailLevel: str = None,
        conflictResolutionStrategy: str = None,
        commitMessage: str = None,
        authorName: str = None,
        email: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def merge_pull_request_by_three_way(
        self,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str = None,
        conflictDetailLevel: str = None,
        conflictResolutionStrategy: str = None,
        commitMessage: str = None,
        authorName: str = None,
        email: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def post_comment_for_compared_commit(
        self,
        repositoryName: str,
        afterCommitId: str,
        content: str,
        beforeCommitId: str = None,
        location: Dict[str, Any] = None,
        clientRequestToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def post_comment_for_pull_request(
        self,
        pullRequestId: str,
        repositoryName: str,
        beforeCommitId: str,
        afterCommitId: str,
        content: str,
        location: Dict[str, Any] = None,
        clientRequestToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def post_comment_reply(
        self, inReplyTo: str, content: str, clientRequestToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_file(
        self,
        repositoryName: str,
        branchName: str,
        fileContent: bytes,
        filePath: str,
        fileMode: str = None,
        parentCommitId: str = None,
        commitMessage: str = None,
        name: str = None,
        email: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_repository_triggers(
        self, repositoryName: str, triggers: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def test_repository_triggers(
        self, repositoryName: str, triggers: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_comment(self, commentId: str, content: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_default_branch(
        self, repositoryName: str, defaultBranchName: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_pull_request_description(
        self, pullRequestId: str, description: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_pull_request_status(
        self, pullRequestId: str, pullRequestStatus: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_pull_request_title(
        self, pullRequestId: str, title: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_repository_description(
        self, repositoryName: str, repositoryDescription: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_repository_name(self, oldName: str, newName: str) -> None:
        pass
