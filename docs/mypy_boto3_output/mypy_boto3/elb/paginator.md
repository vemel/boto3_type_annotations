# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elb.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elb](index.md#elb) / Paginator
    - [DescribeAccountLimits](#describeaccountlimits)
        - [DescribeAccountLimits().paginate](#describeaccountlimitspaginate)
    - [DescribeLoadBalancers](#describeloadbalancers)
        - [DescribeLoadBalancers().paginate](#describeloadbalancerspaginate)

## DescribeAccountLimits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/paginator.py#L10)

```python
class DescribeAccountLimits(Paginator):
```

### DescribeAccountLimits().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/paginator.py#L13)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## DescribeLoadBalancers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/paginator.py#L17)

```python
class DescribeLoadBalancers(Paginator):
```

### DescribeLoadBalancers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/paginator.py#L20)

```python
def paginate(
    LoadBalancerNames: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
