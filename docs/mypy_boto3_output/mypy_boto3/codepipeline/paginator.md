# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codepipeline.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codepipeline](index.md#codepipeline) / Paginator
    - [ListActionExecutions](#listactionexecutions)
        - [ListActionExecutions().paginate](#listactionexecutionspaginate)
    - [ListActionTypes](#listactiontypes)
        - [ListActionTypes().paginate](#listactiontypespaginate)
    - [ListPipelineExecutions](#listpipelineexecutions)
        - [ListPipelineExecutions().paginate](#listpipelineexecutionspaginate)
    - [ListPipelines](#listpipelines)
        - [ListPipelines().paginate](#listpipelinespaginate)
    - [ListTagsForResource](#listtagsforresource)
        - [ListTagsForResource().paginate](#listtagsforresourcepaginate)
    - [ListWebhooks](#listwebhooks)
        - [ListWebhooks().paginate](#listwebhookspaginate)

## ListActionExecutions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L9)

```python
class ListActionExecutions(Paginator):
```

### ListActionExecutions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L12)

```python
def paginate(
    pipelineName: str,
    filter: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListActionTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L21)

```python
class ListActionTypes(Paginator):
```

### ListActionTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L24)

```python
def paginate(
    actionOwnerFilter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPipelineExecutions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L30)

```python
class ListPipelineExecutions(Paginator):
```

### ListPipelineExecutions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L33)

```python
def paginate(
    pipelineName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPipelines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L39)

```python
class ListPipelines(Paginator):
```

### ListPipelines().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L42)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListTagsForResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L46)

```python
class ListTagsForResource(Paginator):
```

### ListTagsForResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L49)

```python
def paginate(
    resourceArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListWebhooks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L55)

```python
class ListWebhooks(Paginator):
```

### ListWebhooks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/paginator.py#L58)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
