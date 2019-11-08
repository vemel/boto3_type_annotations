# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.events.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Events](index.md#events) / Paginator
    - [ListRuleNamesByTarget](#listrulenamesbytarget)
        - [ListRuleNamesByTarget().paginate](#listrulenamesbytargetpaginate)
    - [ListRules](#listrules)
        - [ListRules().paginate](#listrulespaginate)
    - [ListTargetsByRule](#listtargetsbyrule)
        - [ListTargetsByRule().paginate](#listtargetsbyrulepaginate)

## ListRuleNamesByTarget

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/paginator.py#L9)

```python
class ListRuleNamesByTarget(Paginator):
```

### ListRuleNamesByTarget().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/paginator.py#L12)

```python
def paginate(
    TargetArn: str,
    EventBusName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/paginator.py#L21)

```python
class ListRules(Paginator):
```

### ListRules().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/paginator.py#L24)

```python
def paginate(
    NamePrefix: str = None,
    EventBusName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTargetsByRule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/paginator.py#L33)

```python
class ListTargetsByRule(Paginator):
```

### ListTargetsByRule().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/paginator.py#L36)

```python
def paginate(
    Rule: str,
    EventBusName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
