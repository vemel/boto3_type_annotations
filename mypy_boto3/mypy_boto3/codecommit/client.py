from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_describe_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: str,
        maxMergeHunks: Optional[int] = None,
        maxConflictFiles: Optional[int] = None,
        filePaths: Optional[List] = None,
        conflictDetailLevel: Optional[str] = None,
        conflictResolutionStrategy: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_get_commits(
        self,
        commitIds: List,
        repositoryName: str,
    ) -> Dict:
        pass


    def batch_get_repositories(
        self,
        repositoryNames: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_branch(
        self,
        repositoryName: str,
        branchName: str,
        commitId: str,
    ):
        pass


    def create_commit(
        self,
        repositoryName: str,
        branchName: str,
        parentCommitId: Optional[str] = None,
        authorName: Optional[str] = None,
        email: Optional[str] = None,
        commitMessage: Optional[str] = None,
        keepEmptyFolders: Optional[bool] = None,
        putFiles: Optional[List] = None,
        deleteFiles: Optional[List] = None,
        setFileModes: Optional[List] = None,
    ) -> Dict:
        pass


    def create_pull_request(
        self,
        title: str,
        targets: List,
        description: Optional[str] = None,
        clientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_repository(
        self,
        repositoryName: str,
        repositoryDescription: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_unreferenced_merge_commit(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        mergeOption: str,
        conflictDetailLevel: Optional[str] = None,
        conflictResolutionStrategy: Optional[str] = None,
        authorName: Optional[str] = None,
        email: Optional[str] = None,
        commitMessage: Optional[str] = None,
        keepEmptyFolders: Optional[bool] = None,
        conflictResolution: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_branch(
        self,
        repositoryName: str,
        branchName: str,
    ) -> Dict:
        pass


    def delete_comment_content(
        self,
        commentId: str,
    ) -> Dict:
        pass


    def delete_file(
        self,
        repositoryName: str,
        branchName: str,
        filePath: str,
        parentCommitId: str,
        keepEmptyFolders: Optional[bool] = None,
        commitMessage: Optional[str] = None,
        name: Optional[str] = None,
        email: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_repository(
        self,
        repositoryName: str,
    ) -> Dict:
        pass


    def describe_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: str,
        filePath: str,
        maxMergeHunks: Optional[int] = None,
        conflictDetailLevel: Optional[str] = None,
        conflictResolutionStrategy: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_pull_request_events(
        self,
        pullRequestId: str,
        pullRequestEventType: Optional[str] = None,
        actorArn: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_blob(
        self,
        repositoryName: str,
        blobId: str,
    ) -> Dict:
        pass


    def get_branch(
        self,
        repositoryName: Optional[str] = None,
        branchName: Optional[str] = None,
    ) -> Dict:
        pass


    def get_comment(
        self,
        commentId: str,
    ) -> Dict:
        pass


    def get_comments_for_compared_commit(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_comments_for_pull_request(
        self,
        pullRequestId: str,
        repositoryName: Optional[str] = None,
        beforeCommitId: Optional[str] = None,
        afterCommitId: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_commit(
        self,
        repositoryName: str,
        commitId: str,
    ) -> Dict:
        pass


    def get_differences(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: Optional[str] = None,
        beforePath: Optional[str] = None,
        afterPath: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_file(
        self,
        repositoryName: str,
        filePath: str,
        commitSpecifier: Optional[str] = None,
    ) -> Dict:
        pass


    def get_folder(
        self,
        repositoryName: str,
        folderPath: str,
        commitSpecifier: Optional[str] = None,
    ) -> Dict:
        pass


    def get_merge_commit(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: Optional[str] = None,
        conflictResolutionStrategy: Optional[str] = None,
    ) -> Dict:
        pass


    def get_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: str,
        conflictDetailLevel: Optional[str] = None,
        maxConflictFiles: Optional[int] = None,
        conflictResolutionStrategy: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_merge_options(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: Optional[str] = None,
        conflictResolutionStrategy: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_pull_request(
        self,
        pullRequestId: str,
    ) -> Dict:
        pass


    def get_repository(
        self,
        repositoryName: str,
    ) -> Dict:
        pass


    def get_repository_triggers(
        self,
        repositoryName: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_branches(
        self,
        repositoryName: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_pull_requests(
        self,
        repositoryName: str,
        authorArn: Optional[str] = None,
        pullRequestStatus: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_repositories(
        self,
        nextToken: Optional[str] = None,
        sortBy: Optional[str] = None,
        order: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def merge_branches_by_fast_forward(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: Optional[str] = None,
    ) -> Dict:
        pass


    def merge_branches_by_squash(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: Optional[str] = None,
        conflictDetailLevel: Optional[str] = None,
        conflictResolutionStrategy: Optional[str] = None,
        authorName: Optional[str] = None,
        email: Optional[str] = None,
        commitMessage: Optional[str] = None,
        keepEmptyFolders: Optional[bool] = None,
        conflictResolution: Optional[Dict] = None,
    ) -> Dict:
        pass


    def merge_branches_by_three_way(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: Optional[str] = None,
        conflictDetailLevel: Optional[str] = None,
        conflictResolutionStrategy: Optional[str] = None,
        authorName: Optional[str] = None,
        email: Optional[str] = None,
        commitMessage: Optional[str] = None,
        keepEmptyFolders: Optional[bool] = None,
        conflictResolution: Optional[Dict] = None,
    ) -> Dict:
        pass


    def merge_pull_request_by_fast_forward(
        self,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: Optional[str] = None,
    ) -> Dict:
        pass


    def merge_pull_request_by_squash(
        self,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: Optional[str] = None,
        conflictDetailLevel: Optional[str] = None,
        conflictResolutionStrategy: Optional[str] = None,
        commitMessage: Optional[str] = None,
        authorName: Optional[str] = None,
        email: Optional[str] = None,
        keepEmptyFolders: Optional[bool] = None,
        conflictResolution: Optional[Dict] = None,
    ) -> Dict:
        pass


    def merge_pull_request_by_three_way(
        self,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: Optional[str] = None,
        conflictDetailLevel: Optional[str] = None,
        conflictResolutionStrategy: Optional[str] = None,
        commitMessage: Optional[str] = None,
        authorName: Optional[str] = None,
        email: Optional[str] = None,
        keepEmptyFolders: Optional[bool] = None,
        conflictResolution: Optional[Dict] = None,
    ) -> Dict:
        pass


    def post_comment_for_compared_commit(
        self,
        repositoryName: str,
        afterCommitId: str,
        content: str,
        beforeCommitId: Optional[str] = None,
        location: Optional[Dict] = None,
        clientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def post_comment_for_pull_request(
        self,
        pullRequestId: str,
        repositoryName: str,
        beforeCommitId: str,
        afterCommitId: str,
        content: str,
        location: Optional[Dict] = None,
        clientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def post_comment_reply(
        self,
        inReplyTo: str,
        content: str,
        clientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_file(
        self,
        repositoryName: str,
        branchName: str,
        fileContent: bytes,
        filePath: str,
        fileMode: Optional[str] = None,
        parentCommitId: Optional[str] = None,
        commitMessage: Optional[str] = None,
        name: Optional[str] = None,
        email: Optional[str] = None,
    ) -> Dict:
        pass


    def put_repository_triggers(
        self,
        repositoryName: str,
        triggers: List,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: Dict,
    ):
        pass


    def test_repository_triggers(
        self,
        repositoryName: str,
        triggers: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ):
        pass


    def update_comment(
        self,
        commentId: str,
        content: str,
    ) -> Dict:
        pass


    def update_default_branch(
        self,
        repositoryName: str,
        defaultBranchName: str,
    ):
        pass


    def update_pull_request_description(
        self,
        pullRequestId: str,
        description: str,
    ) -> Dict:
        pass


    def update_pull_request_status(
        self,
        pullRequestId: str,
        pullRequestStatus: str,
    ) -> Dict:
        pass


    def update_pull_request_title(
        self,
        pullRequestId: str,
        title: str,
    ) -> Dict:
        pass


    def update_repository_description(
        self,
        repositoryName: str,
        repositoryDescription: Optional[str] = None,
    ):
        pass


    def update_repository_name(
        self,
        oldName: str,
        newName: str,
    ):
        pass

