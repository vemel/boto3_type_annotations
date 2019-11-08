# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elbv2.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elbv2](index.md#elbv2) / Paginator
    - [DescribeAccountLimits](#describeaccountlimits)
        - [DescribeAccountLimits().paginate](#describeaccountlimitspaginate)
    - [DescribeListenerCertificates](#describelistenercertificates)
        - [DescribeListenerCertificates().paginate](#describelistenercertificatespaginate)
    - [DescribeListeners](#describelisteners)
        - [DescribeListeners().paginate](#describelistenerspaginate)
    - [DescribeLoadBalancers](#describeloadbalancers)
        - [DescribeLoadBalancers().paginate](#describeloadbalancerspaginate)
    - [DescribeRules](#describerules)
        - [DescribeRules().paginate](#describerulespaginate)
    - [DescribeSSLPolicies](#describesslpolicies)
        - [DescribeSSLPolicies().paginate](#describesslpoliciespaginate)
    - [DescribeTargetGroups](#describetargetgroups)
        - [DescribeTargetGroups().paginate](#describetargetgroupspaginate)

## DescribeAccountLimits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L10)

```python
class DescribeAccountLimits(Paginator):
```

### DescribeAccountLimits().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L13)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## DescribeListenerCertificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L17)

```python
class DescribeListenerCertificates(Paginator):
```

### DescribeListenerCertificates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L20)

```python
def paginate(
    ListenerArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeListeners

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L26)

```python
class DescribeListeners(Paginator):
```

### DescribeListeners().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L29)

```python
def paginate(
    LoadBalancerArn: str = None,
    ListenerArns: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeLoadBalancers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L38)

```python
class DescribeLoadBalancers(Paginator):
```

### DescribeLoadBalancers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L41)

```python
def paginate(
    LoadBalancerArns: List[Any] = None,
    Names: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeRules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L50)

```python
class DescribeRules(Paginator):
```

### DescribeRules().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L53)

```python
def paginate(
    ListenerArn: str = None,
    RuleArns: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeSSLPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L62)

```python
class DescribeSSLPolicies(Paginator):
```

### DescribeSSLPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L65)

```python
def paginate(
    Names: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeTargetGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L71)

```python
class DescribeTargetGroups(Paginator):
```

### DescribeTargetGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/paginator.py#L74)

```python
def paginate(
    LoadBalancerArn: str = None,
    TargetGroupArns: List[Any] = None,
    Names: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
