# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloud9.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloud9](index.md#cloud9) / Paginator
    - [DescribeEnvironmentMemberships](#describeenvironmentmemberships)
        - [DescribeEnvironmentMemberships().paginate](#describeenvironmentmembershipspaginate)
    - [ListEnvironments](#listenvironments)
        - [ListEnvironments().paginate](#listenvironmentspaginate)

## DescribeEnvironmentMemberships

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/paginator.py#L10)

```python
class DescribeEnvironmentMemberships(Paginator):
```

### DescribeEnvironmentMemberships().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/paginator.py#L13)

```python
def paginate(
    userArn: str = None,
    environmentId: str = None,
    permissions: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListEnvironments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/paginator.py#L23)

```python
class ListEnvironments(Paginator):
```

### ListEnvironments().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloud9/paginator.py#L26)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
