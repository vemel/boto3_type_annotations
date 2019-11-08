# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.swf.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Swf](index.md#swf) / Paginator
    - [GetWorkflowExecutionHistory](#getworkflowexecutionhistory)
        - [GetWorkflowExecutionHistory().paginate](#getworkflowexecutionhistorypaginate)
    - [ListActivityTypes](#listactivitytypes)
        - [ListActivityTypes().paginate](#listactivitytypespaginate)
    - [ListClosedWorkflowExecutions](#listclosedworkflowexecutions)
        - [ListClosedWorkflowExecutions().paginate](#listclosedworkflowexecutionspaginate)
    - [ListDomains](#listdomains)
        - [ListDomains().paginate](#listdomainspaginate)
    - [ListOpenWorkflowExecutions](#listopenworkflowexecutions)
        - [ListOpenWorkflowExecutions().paginate](#listopenworkflowexecutionspaginate)
    - [ListWorkflowTypes](#listworkflowtypes)
        - [ListWorkflowTypes().paginate](#listworkflowtypespaginate)
    - [PollForDecisionTask](#pollfordecisiontask)
        - [PollForDecisionTask().paginate](#pollfordecisiontaskpaginate)

## GetWorkflowExecutionHistory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L9)

```python
class GetWorkflowExecutionHistory(Paginator):
```

### GetWorkflowExecutionHistory().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L12)

```python
def paginate(
    domain: str,
    execution: Dict[str, Any],
    reverseOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListActivityTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L22)

```python
class ListActivityTypes(Paginator):
```

### ListActivityTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L25)

```python
def paginate(
    domain: str,
    registrationStatus: str,
    name: str = None,
    reverseOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListClosedWorkflowExecutions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L36)

```python
class ListClosedWorkflowExecutions(Paginator):
```

### ListClosedWorkflowExecutions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L39)

```python
def paginate(
    domain: str,
    startTimeFilter: Dict[str, Any] = None,
    closeTimeFilter: Dict[str, Any] = None,
    executionFilter: Dict[str, Any] = None,
    closeStatusFilter: Dict[str, Any] = None,
    typeFilter: Dict[str, Any] = None,
    tagFilter: Dict[str, Any] = None,
    reverseOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDomains

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L54)

```python
class ListDomains(Paginator):
```

### ListDomains().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L57)

```python
def paginate(
    registrationStatus: str,
    reverseOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListOpenWorkflowExecutions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L66)

```python
class ListOpenWorkflowExecutions(Paginator):
```

### ListOpenWorkflowExecutions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L69)

```python
def paginate(
    domain: str,
    startTimeFilter: Dict[str, Any],
    typeFilter: Dict[str, Any] = None,
    tagFilter: Dict[str, Any] = None,
    reverseOrder: bool = None,
    executionFilter: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListWorkflowTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L82)

```python
class ListWorkflowTypes(Paginator):
```

### ListWorkflowTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L85)

```python
def paginate(
    domain: str,
    registrationStatus: str,
    name: str = None,
    reverseOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## PollForDecisionTask

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L96)

```python
class PollForDecisionTask(Paginator):
```

### PollForDecisionTask().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/paginator.py#L99)

```python
def paginate(
    domain: str,
    taskList: Dict[str, Any],
    identity: str = None,
    reverseOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
