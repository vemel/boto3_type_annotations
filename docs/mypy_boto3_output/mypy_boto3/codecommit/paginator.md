# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codecommit.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codecommit](index.md#codecommit) / Paginator
    - [DescribePullRequestEvents](#describepullrequestevents)
        - [DescribePullRequestEvents().paginate](#describepullrequesteventspaginate)
    - [GetCommentsForComparedCommit](#getcommentsforcomparedcommit)
        - [GetCommentsForComparedCommit().paginate](#getcommentsforcomparedcommitpaginate)
    - [GetCommentsForPullRequest](#getcommentsforpullrequest)
        - [GetCommentsForPullRequest().paginate](#getcommentsforpullrequestpaginate)
    - [GetDifferences](#getdifferences)
        - [GetDifferences().paginate](#getdifferencespaginate)
    - [ListBranches](#listbranches)
        - [ListBranches().paginate](#listbranchespaginate)
    - [ListPullRequests](#listpullrequests)
        - [ListPullRequests().paginate](#listpullrequestspaginate)
    - [ListRepositories](#listrepositories)
        - [ListRepositories().paginate](#listrepositoriespaginate)

## DescribePullRequestEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L9)

```python
class DescribePullRequestEvents(Paginator):
```

### DescribePullRequestEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L12)

```python
def paginate(
    pullRequestId: str,
    pullRequestEventType: str = None,
    actorArn: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetCommentsForComparedCommit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L22)

```python
class GetCommentsForComparedCommit(Paginator):
```

### GetCommentsForComparedCommit().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L25)

```python
def paginate(
    repositoryName: str,
    afterCommitId: str,
    beforeCommitId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetCommentsForPullRequest

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L35)

```python
class GetCommentsForPullRequest(Paginator):
```

### GetCommentsForPullRequest().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L38)

```python
def paginate(
    pullRequestId: str,
    repositoryName: str = None,
    beforeCommitId: str = None,
    afterCommitId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetDifferences

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L49)

```python
class GetDifferences(Paginator):
```

### GetDifferences().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L52)

```python
def paginate(
    repositoryName: str,
    afterCommitSpecifier: str,
    beforeCommitSpecifier: str = None,
    beforePath: str = None,
    afterPath: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListBranches

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L64)

```python
class ListBranches(Paginator):
```

### ListBranches().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L67)

```python
def paginate(
    repositoryName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPullRequests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L73)

```python
class ListPullRequests(Paginator):
```

### ListPullRequests().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L76)

```python
def paginate(
    repositoryName: str,
    authorArn: str = None,
    pullRequestStatus: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRepositories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L86)

```python
class ListRepositories(Paginator):
```

### ListRepositories().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codecommit/paginator.py#L89)

```python
def paginate(
    sortBy: str = None,
    order: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
