# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elbv2.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elbv2](index.md#elbv2) / Client
    - [Client](#client)
        - [Client().add_listener_certificates](#clientadd_listener_certificates)
        - [Client().add_tags](#clientadd_tags)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_listener](#clientcreate_listener)
        - [Client().create_load_balancer](#clientcreate_load_balancer)
        - [Client().create_rule](#clientcreate_rule)
        - [Client().create_target_group](#clientcreate_target_group)
        - [Client().delete_listener](#clientdelete_listener)
        - [Client().delete_load_balancer](#clientdelete_load_balancer)
        - [Client().delete_rule](#clientdelete_rule)
        - [Client().delete_target_group](#clientdelete_target_group)
        - [Client().deregister_targets](#clientderegister_targets)
        - [Client().describe_account_limits](#clientdescribe_account_limits)
        - [Client().describe_listener_certificates](#clientdescribe_listener_certificates)
        - [Client().describe_listeners](#clientdescribe_listeners)
        - [Client().describe_load_balancer_attributes](#clientdescribe_load_balancer_attributes)
        - [Client().describe_load_balancers](#clientdescribe_load_balancers)
        - [Client().describe_rules](#clientdescribe_rules)
        - [Client().describe_ssl_policies](#clientdescribe_ssl_policies)
        - [Client().describe_tags](#clientdescribe_tags)
        - [Client().describe_target_group_attributes](#clientdescribe_target_group_attributes)
        - [Client().describe_target_groups](#clientdescribe_target_groups)
        - [Client().describe_target_health](#clientdescribe_target_health)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().modify_listener](#clientmodify_listener)
        - [Client().modify_load_balancer_attributes](#clientmodify_load_balancer_attributes)
        - [Client().modify_rule](#clientmodify_rule)
        - [Client().modify_target_group](#clientmodify_target_group)
        - [Client().modify_target_group_attributes](#clientmodify_target_group_attributes)
        - [Client().register_targets](#clientregister_targets)
        - [Client().remove_listener_certificates](#clientremove_listener_certificates)
        - [Client().remove_tags](#clientremove_tags)
        - [Client().set_ip_address_type](#clientset_ip_address_type)
        - [Client().set_rule_priorities](#clientset_rule_priorities)
        - [Client().set_security_groups](#clientset_security_groups)
        - [Client().set_subnets](#clientset_subnets)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_listener_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L15)

```python
def add_listener_certificates(
    ListenerArn: str,
    Certificates: List[Any],
) -> Dict[str, Any]:
```

### Client().add_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L21)

```python
def add_tags(ResourceArns: List[Any], Tags: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L25)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_listener

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L29)

```python
def create_listener(
    LoadBalancerArn: str,
    Protocol: str,
    Port: int,
    DefaultActions: List[Any],
    SslPolicy: str = None,
    Certificates: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L41)

```python
def create_load_balancer(
    Name: str,
    Subnets: List[Any] = None,
    SubnetMappings: List[Any] = None,
    SecurityGroups: List[Any] = None,
    Scheme: str = None,
    Tags: List[Any] = None,
    Type: str = None,
    IpAddressType: str = None,
) -> Dict[str, Any]:
```

### Client().create_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L55)

```python
def create_rule(
    ListenerArn: str,
    Conditions: List[Any],
    Priority: int,
    Actions: List[Any],
) -> Dict[str, Any]:
```

### Client().create_target_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L61)

```python
def create_target_group(
    Name: str,
    Protocol: str = None,
    Port: int = None,
    VpcId: str = None,
    HealthCheckProtocol: str = None,
    HealthCheckPort: str = None,
    HealthCheckEnabled: bool = None,
    HealthCheckPath: str = None,
    HealthCheckIntervalSeconds: int = None,
    HealthCheckTimeoutSeconds: int = None,
    HealthyThresholdCount: int = None,
    UnhealthyThresholdCount: int = None,
    Matcher: Dict[str, Any] = None,
    TargetType: str = None,
) -> Dict[str, Any]:
```

### Client().delete_listener

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L81)

```python
def delete_listener(ListenerArn: str) -> Dict[str, Any]:
```

### Client().delete_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L85)

```python
def delete_load_balancer(LoadBalancerArn: str) -> Dict[str, Any]:
```

### Client().delete_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L89)

```python
def delete_rule(RuleArn: str) -> Dict[str, Any]:
```

### Client().delete_target_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L93)

```python
def delete_target_group(TargetGroupArn: str) -> Dict[str, Any]:
```

### Client().deregister_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L97)

```python
def deregister_targets(
    TargetGroupArn: str,
    Targets: List[Any],
) -> Dict[str, Any]:
```

### Client().describe_account_limits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L103)

```python
def describe_account_limits(
    Marker: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().describe_listener_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L109)

```python
def describe_listener_certificates(
    ListenerArn: str,
    Marker: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().describe_listeners

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L115)

```python
def describe_listeners(
    LoadBalancerArn: str = None,
    ListenerArns: List[Any] = None,
    Marker: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().describe_load_balancer_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L125)

```python
def describe_load_balancer_attributes(LoadBalancerArn: str) -> Dict[str, Any]:
```

### Client().describe_load_balancers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L129)

```python
def describe_load_balancers(
    LoadBalancerArns: List[Any] = None,
    Names: List[Any] = None,
    Marker: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().describe_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L139)

```python
def describe_rules(
    ListenerArn: str = None,
    RuleArns: List[Any] = None,
    Marker: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().describe_ssl_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L149)

```python
def describe_ssl_policies(
    Names: List[Any] = None,
    Marker: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().describe_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L155)

```python
def describe_tags(ResourceArns: List[Any]) -> Dict[str, Any]:
```

### Client().describe_target_group_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L159)

```python
def describe_target_group_attributes(TargetGroupArn: str) -> Dict[str, Any]:
```

### Client().describe_target_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L163)

```python
def describe_target_groups(
    LoadBalancerArn: str = None,
    TargetGroupArns: List[Any] = None,
    Names: List[Any] = None,
    Marker: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().describe_target_health

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L174)

```python
def describe_target_health(
    TargetGroupArn: str,
    Targets: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L180)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L190)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L194)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().modify_listener

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L198)

```python
def modify_listener(
    ListenerArn: str,
    Port: int = None,
    Protocol: str = None,
    SslPolicy: str = None,
    Certificates: List[Any] = None,
    DefaultActions: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_load_balancer_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L210)

```python
def modify_load_balancer_attributes(
    LoadBalancerArn: str,
    Attributes: List[Any],
) -> Dict[str, Any]:
```

### Client().modify_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L216)

```python
def modify_rule(
    RuleArn: str,
    Conditions: List[Any] = None,
    Actions: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_target_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L222)

```python
def modify_target_group(
    TargetGroupArn: str,
    HealthCheckProtocol: str = None,
    HealthCheckPort: str = None,
    HealthCheckPath: str = None,
    HealthCheckEnabled: bool = None,
    HealthCheckIntervalSeconds: int = None,
    HealthCheckTimeoutSeconds: int = None,
    HealthyThresholdCount: int = None,
    UnhealthyThresholdCount: int = None,
    Matcher: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_target_group_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L238)

```python
def modify_target_group_attributes(
    TargetGroupArn: str,
    Attributes: List[Any],
) -> Dict[str, Any]:
```

### Client().register_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L244)

```python
def register_targets(
    TargetGroupArn: str,
    Targets: List[Any],
) -> Dict[str, Any]:
```

### Client().remove_listener_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L250)

```python
def remove_listener_certificates(
    ListenerArn: str,
    Certificates: List[Any],
) -> Dict[str, Any]:
```

### Client().remove_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L256)

```python
def remove_tags(
    ResourceArns: List[Any],
    TagKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().set_ip_address_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L262)

```python
def set_ip_address_type(
    LoadBalancerArn: str,
    IpAddressType: str,
) -> Dict[str, Any]:
```

### Client().set_rule_priorities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L268)

```python
def set_rule_priorities(RulePriorities: List[Any]) -> Dict[str, Any]:
```

### Client().set_security_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L272)

```python
def set_security_groups(
    LoadBalancerArn: str,
    SecurityGroups: List[Any],
) -> Dict[str, Any]:
```

### Client().set_subnets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/client.py#L278)

```python
def set_subnets(
    LoadBalancerArn: str,
    Subnets: List[Any] = None,
    SubnetMappings: List[Any] = None,
) -> Dict[str, Any]:
```
