# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codecommit.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codecommit](index.md#codecommit) / Client
    - [Client](#client)
        - [Client().batch_describe_merge_conflicts](#clientbatch_describe_merge_conflicts)
        - [Client().batch_get_commits](#clientbatch_get_commits)
        - [Client().batch_get_repositories](#clientbatch_get_repositories)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_branch](#clientcreate_branch)
        - [Client().create_commit](#clientcreate_commit)
        - [Client().create_pull_request](#clientcreate_pull_request)
        - [Client().create_repository](#clientcreate_repository)
        - [Client().create_unreferenced_merge_commit](#clientcreate_unreferenced_merge_commit)
        - [Client().delete_branch](#clientdelete_branch)
        - [Client().delete_comment_content](#clientdelete_comment_content)
        - [Client().delete_file](#clientdelete_file)
        - [Client().delete_repository](#clientdelete_repository)
        - [Client().describe_merge_conflicts](#clientdescribe_merge_conflicts)
        - [Client().describe_pull_request_events](#clientdescribe_pull_request_events)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_blob](#clientget_blob)
        - [Client().get_branch](#clientget_branch)
        - [Client().get_comment](#clientget_comment)
        - [Client().get_comments_for_compared_commit](#clientget_comments_for_compared_commit)
        - [Client().get_comments_for_pull_request](#clientget_comments_for_pull_request)
        - [Client().get_commit](#clientget_commit)
        - [Client().get_differences](#clientget_differences)
        - [Client().get_file](#clientget_file)
        - [Client().get_folder](#clientget_folder)
        - [Client().get_merge_commit](#clientget_merge_commit)
        - [Client().get_merge_conflicts](#clientget_merge_conflicts)
        - [Client().get_merge_options](#clientget_merge_options)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_pull_request](#clientget_pull_request)
        - [Client().get_repository](#clientget_repository)
        - [Client().get_repository_triggers](#clientget_repository_triggers)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_branches](#clientlist_branches)
        - [Client().list_pull_requests](#clientlist_pull_requests)
        - [Client().list_repositories](#clientlist_repositories)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().merge_branches_by_fast_forward](#clientmerge_branches_by_fast_forward)
        - [Client().merge_branches_by_squash](#clientmerge_branches_by_squash)
        - [Client().merge_branches_by_three_way](#clientmerge_branches_by_three_way)
        - [Client().merge_pull_request_by_fast_forward](#clientmerge_pull_request_by_fast_forward)
        - [Client().merge_pull_request_by_squash](#clientmerge_pull_request_by_squash)
        - [Client().merge_pull_request_by_three_way](#clientmerge_pull_request_by_three_way)
        - [Client().post_comment_for_compared_commit](#clientpost_comment_for_compared_commit)
        - [Client().post_comment_for_pull_request](#clientpost_comment_for_pull_request)
        - [Client().post_comment_reply](#clientpost_comment_reply)
        - [Client().put_file](#clientput_file)
        - [Client().put_repository_triggers](#clientput_repository_triggers)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().test_repository_triggers](#clienttest_repository_triggers)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_comment](#clientupdate_comment)
        - [Client().update_default_branch](#clientupdate_default_branch)
        - [Client().update_pull_request_description](#clientupdate_pull_request_description)
        - [Client().update_pull_request_status](#clientupdate_pull_request_status)
        - [Client().update_pull_request_title](#clientupdate_pull_request_title)
        - [Client().update_repository_description](#clientupdate_repository_description)
        - [Client().update_repository_name](#clientupdate_repository_name)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_describe_merge_conflicts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L15)

```python
def batch_describe_merge_conflicts(
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
```

### Client().batch_get_commits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L31)

```python
def batch_get_commits(
    commitIds: List[Any],
    repositoryName: str,
) -> Dict[str, Any]:
```

### Client().batch_get_repositories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L37)

```python
def batch_get_repositories(repositoryNames: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L41)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_branch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L45)

```python
def create_branch(
    repositoryName: str,
    branchName: str,
    commitId: str,
) -> None:
```

### Client().create_commit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L51)

```python
def create_commit(
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
```

### Client().create_pull_request

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L67)

```python
def create_pull_request(
    title: str,
    targets: List[Any],
    description: str = None,
    clientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_repository

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L77)

```python
def create_repository(
    repositoryName: str,
    repositoryDescription: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_unreferenced_merge_commit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L86)

```python
def create_unreferenced_merge_commit(
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
```

### Client().delete_branch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L103)

```python
def delete_branch(repositoryName: str, branchName: str) -> Dict[str, Any]:
```

### Client().delete_comment_content

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L107)

```python
def delete_comment_content(commentId: str) -> Dict[str, Any]:
```

### Client().delete_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L111)

```python
def delete_file(
    repositoryName: str,
    branchName: str,
    filePath: str,
    parentCommitId: str,
    keepEmptyFolders: bool = None,
    commitMessage: str = None,
    name: str = None,
    email: str = None,
) -> Dict[str, Any]:
```

### Client().delete_repository

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L125)

```python
def delete_repository(repositoryName: str) -> Dict[str, Any]:
```

### Client().describe_merge_conflicts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L129)

```python
def describe_merge_conflicts(
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
```

### Client().describe_pull_request_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L144)

```python
def describe_pull_request_events(
    pullRequestId: str,
    pullRequestEventType: str = None,
    actorArn: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L155)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_blob

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L165)

```python
def get_blob(repositoryName: str, blobId: str) -> Dict[str, Any]:
```

### Client().get_branch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L169)

```python
def get_branch(
    repositoryName: str = None,
    branchName: str = None,
) -> Dict[str, Any]:
```

### Client().get_comment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L175)

```python
def get_comment(commentId: str) -> Dict[str, Any]:
```

### Client().get_comments_for_compared_commit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L179)

```python
def get_comments_for_compared_commit(
    repositoryName: str,
    afterCommitId: str,
    beforeCommitId: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_comments_for_pull_request

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L190)

```python
def get_comments_for_pull_request(
    pullRequestId: str,
    repositoryName: str = None,
    beforeCommitId: str = None,
    afterCommitId: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_commit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L202)

```python
def get_commit(repositoryName: str, commitId: str) -> Dict[str, Any]:
```

### Client().get_differences

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L206)

```python
def get_differences(
    repositoryName: str,
    afterCommitSpecifier: str,
    beforeCommitSpecifier: str = None,
    beforePath: str = None,
    afterPath: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L219)

```python
def get_file(
    repositoryName: str,
    filePath: str,
    commitSpecifier: str = None,
) -> Dict[str, Any]:
```

### Client().get_folder

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L225)

```python
def get_folder(
    repositoryName: str,
    folderPath: str,
    commitSpecifier: str = None,
) -> Dict[str, Any]:
```

### Client().get_merge_commit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L231)

```python
def get_merge_commit(
    repositoryName: str,
    sourceCommitSpecifier: str,
    destinationCommitSpecifier: str,
    conflictDetailLevel: str = None,
    conflictResolutionStrategy: str = None,
) -> Dict[str, Any]:
```

### Client().get_merge_conflicts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L242)

```python
def get_merge_conflicts(
    repositoryName: str,
    destinationCommitSpecifier: str,
    sourceCommitSpecifier: str,
    mergeOption: str,
    conflictDetailLevel: str = None,
    maxConflictFiles: int = None,
    conflictResolutionStrategy: str = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_merge_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L256)

```python
def get_merge_options(
    repositoryName: str,
    sourceCommitSpecifier: str,
    destinationCommitSpecifier: str,
    conflictDetailLevel: str = None,
    conflictResolutionStrategy: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L267)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_pull_request

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L271)

```python
def get_pull_request(pullRequestId: str) -> Dict[str, Any]:
```

### Client().get_repository

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L275)

```python
def get_repository(repositoryName: str) -> Dict[str, Any]:
```

### Client().get_repository_triggers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L279)

```python
def get_repository_triggers(repositoryName: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L283)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_branches

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L287)

```python
def list_branches(
    repositoryName: str,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_pull_requests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L293)

```python
def list_pull_requests(
    repositoryName: str,
    authorArn: str = None,
    pullRequestStatus: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_repositories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L304)

```python
def list_repositories(
    nextToken: str = None,
    sortBy: str = None,
    order: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L310)

```python
def list_tags_for_resource(
    resourceArn: str,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().merge_branches_by_fast_forward

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L316)

```python
def merge_branches_by_fast_forward(
    repositoryName: str,
    sourceCommitSpecifier: str,
    destinationCommitSpecifier: str,
    targetBranch: str = None,
) -> Dict[str, Any]:
```

### Client().merge_branches_by_squash

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L326)

```python
def merge_branches_by_squash(
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
```

### Client().merge_branches_by_three_way

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L343)

```python
def merge_branches_by_three_way(
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
```

### Client().merge_pull_request_by_fast_forward

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L360)

```python
def merge_pull_request_by_fast_forward(
    pullRequestId: str,
    repositoryName: str,
    sourceCommitId: str = None,
) -> Dict[str, Any]:
```

### Client().merge_pull_request_by_squash

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L366)

```python
def merge_pull_request_by_squash(
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
```

### Client().merge_pull_request_by_three_way

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L382)

```python
def merge_pull_request_by_three_way(
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
```

### Client().post_comment_for_compared_commit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L398)

```python
def post_comment_for_compared_commit(
    repositoryName: str,
    afterCommitId: str,
    content: str,
    beforeCommitId: str = None,
    location: Dict[str, Any] = None,
    clientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().post_comment_for_pull_request

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L410)

```python
def post_comment_for_pull_request(
    pullRequestId: str,
    repositoryName: str,
    beforeCommitId: str,
    afterCommitId: str,
    content: str,
    location: Dict[str, Any] = None,
    clientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().post_comment_reply

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L423)

```python
def post_comment_reply(
    inReplyTo: str,
    content: str,
    clientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L429)

```python
def put_file(
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
```

### Client().put_repository_triggers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L444)

```python
def put_repository_triggers(
    repositoryName: str,
    triggers: List[Any],
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L450)

```python
def tag_resource(resourceArn: str, tags: Dict[str, Any]) -> None:
```

### Client().test_repository_triggers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L454)

```python
def test_repository_triggers(
    repositoryName: str,
    triggers: List[Any],
) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L460)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> None:
```

### Client().update_comment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L464)

```python
def update_comment(commentId: str, content: str) -> Dict[str, Any]:
```

### Client().update_default_branch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L468)

```python
def update_default_branch(
    repositoryName: str,
    defaultBranchName: str,
) -> None:
```

### Client().update_pull_request_description

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L474)

```python
def update_pull_request_description(
    pullRequestId: str,
    description: str,
) -> Dict[str, Any]:
```

### Client().update_pull_request_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L480)

```python
def update_pull_request_status(
    pullRequestId: str,
    pullRequestStatus: str,
) -> Dict[str, Any]:
```

### Client().update_pull_request_title

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L486)

```python
def update_pull_request_title(
    pullRequestId: str,
    title: str,
) -> Dict[str, Any]:
```

### Client().update_repository_description

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L492)

```python
def update_repository_description(
    repositoryName: str,
    repositoryDescription: str = None,
) -> None:
```

### Client().update_repository_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/client.py#L498)

```python
def update_repository_name(oldName: str, newName: str) -> None:
```
