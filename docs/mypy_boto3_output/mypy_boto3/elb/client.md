# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elb.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elb](index.md#elb) / Client
    - [Client](#client)
        - [Client().add_tags](#clientadd_tags)
        - [Client().apply_security_groups_to_load_balancer](#clientapply_security_groups_to_load_balancer)
        - [Client().attach_load_balancer_to_subnets](#clientattach_load_balancer_to_subnets)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().configure_health_check](#clientconfigure_health_check)
        - [Client().create_app_cookie_stickiness_policy](#clientcreate_app_cookie_stickiness_policy)
        - [Client().create_lb_cookie_stickiness_policy](#clientcreate_lb_cookie_stickiness_policy)
        - [Client().create_load_balancer](#clientcreate_load_balancer)
        - [Client().create_load_balancer_listeners](#clientcreate_load_balancer_listeners)
        - [Client().create_load_balancer_policy](#clientcreate_load_balancer_policy)
        - [Client().delete_load_balancer](#clientdelete_load_balancer)
        - [Client().delete_load_balancer_listeners](#clientdelete_load_balancer_listeners)
        - [Client().delete_load_balancer_policy](#clientdelete_load_balancer_policy)
        - [Client().deregister_instances_from_load_balancer](#clientderegister_instances_from_load_balancer)
        - [Client().describe_account_limits](#clientdescribe_account_limits)
        - [Client().describe_instance_health](#clientdescribe_instance_health)
        - [Client().describe_load_balancer_attributes](#clientdescribe_load_balancer_attributes)
        - [Client().describe_load_balancer_policies](#clientdescribe_load_balancer_policies)
        - [Client().describe_load_balancer_policy_types](#clientdescribe_load_balancer_policy_types)
        - [Client().describe_load_balancers](#clientdescribe_load_balancers)
        - [Client().describe_tags](#clientdescribe_tags)
        - [Client().detach_load_balancer_from_subnets](#clientdetach_load_balancer_from_subnets)
        - [Client().disable_availability_zones_for_load_balancer](#clientdisable_availability_zones_for_load_balancer)
        - [Client().enable_availability_zones_for_load_balancer](#clientenable_availability_zones_for_load_balancer)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().modify_load_balancer_attributes](#clientmodify_load_balancer_attributes)
        - [Client().register_instances_with_load_balancer](#clientregister_instances_with_load_balancer)
        - [Client().remove_tags](#clientremove_tags)
        - [Client().set_load_balancer_listener_ssl_certificate](#clientset_load_balancer_listener_ssl_certificate)
        - [Client().set_load_balancer_policies_for_backend_server](#clientset_load_balancer_policies_for_backend_server)
        - [Client().set_load_balancer_policies_of_listener](#clientset_load_balancer_policies_of_listener)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L15)

```python
def add_tags(LoadBalancerNames: List[Any], Tags: List[Any]) -> Dict[str, Any]:
```

### Client().apply_security_groups_to_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L19)

```python
def apply_security_groups_to_load_balancer(
    LoadBalancerName: str,
    SecurityGroups: List[Any],
) -> Dict[str, Any]:
```

### Client().attach_load_balancer_to_subnets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L25)

```python
def attach_load_balancer_to_subnets(
    LoadBalancerName: str,
    Subnets: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L31)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().configure_health_check

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L35)

```python
def configure_health_check(
    LoadBalancerName: str,
    HealthCheck: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_app_cookie_stickiness_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L41)

```python
def create_app_cookie_stickiness_policy(
    LoadBalancerName: str,
    PolicyName: str,
    CookieName: str,
) -> Dict[str, Any]:
```

### Client().create_lb_cookie_stickiness_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L47)

```python
def create_lb_cookie_stickiness_policy(
    LoadBalancerName: str,
    PolicyName: str,
    CookieExpirationPeriod: int = None,
) -> Dict[str, Any]:
```

### Client().create_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L53)

```python
def create_load_balancer(
    LoadBalancerName: str,
    Listeners: List[Any],
    AvailabilityZones: List[Any] = None,
    Subnets: List[Any] = None,
    SecurityGroups: List[Any] = None,
    Scheme: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_load_balancer_listeners

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L66)

```python
def create_load_balancer_listeners(
    LoadBalancerName: str,
    Listeners: List[Any],
) -> Dict[str, Any]:
```

### Client().create_load_balancer_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L72)

```python
def create_load_balancer_policy(
    LoadBalancerName: str,
    PolicyName: str,
    PolicyTypeName: str,
    PolicyAttributes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L82)

```python
def delete_load_balancer(LoadBalancerName: str) -> Dict[str, Any]:
```

### Client().delete_load_balancer_listeners

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L86)

```python
def delete_load_balancer_listeners(
    LoadBalancerName: str,
    LoadBalancerPorts: List[Any],
) -> Dict[str, Any]:
```

### Client().delete_load_balancer_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L92)

```python
def delete_load_balancer_policy(
    LoadBalancerName: str,
    PolicyName: str,
) -> Dict[str, Any]:
```

### Client().deregister_instances_from_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L98)

```python
def deregister_instances_from_load_balancer(
    LoadBalancerName: str,
    Instances: List[Any],
) -> Dict[str, Any]:
```

### Client().describe_account_limits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L104)

```python
def describe_account_limits(
    Marker: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().describe_instance_health

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L110)

```python
def describe_instance_health(
    LoadBalancerName: str,
    Instances: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_load_balancer_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L116)

```python
def describe_load_balancer_attributes(
    LoadBalancerName: str,
) -> Dict[str, Any]:
```

### Client().describe_load_balancer_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L122)

```python
def describe_load_balancer_policies(
    LoadBalancerName: str = None,
    PolicyNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_load_balancer_policy_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L128)

```python
def describe_load_balancer_policy_types(
    PolicyTypeNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_load_balancers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L134)

```python
def describe_load_balancers(
    LoadBalancerNames: List[Any] = None,
    Marker: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().describe_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L143)

```python
def describe_tags(LoadBalancerNames: List[Any]) -> Dict[str, Any]:
```

### Client().detach_load_balancer_from_subnets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L147)

```python
def detach_load_balancer_from_subnets(
    LoadBalancerName: str,
    Subnets: List[Any],
) -> Dict[str, Any]:
```

### Client().disable_availability_zones_for_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L153)

```python
def disable_availability_zones_for_load_balancer(
    LoadBalancerName: str,
    AvailabilityZones: List[Any],
) -> Dict[str, Any]:
```

### Client().enable_availability_zones_for_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L159)

```python
def enable_availability_zones_for_load_balancer(
    LoadBalancerName: str,
    AvailabilityZones: List[Any],
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L165)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L175)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L179)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().modify_load_balancer_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L183)

```python
def modify_load_balancer_attributes(
    LoadBalancerName: str,
    LoadBalancerAttributes: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().register_instances_with_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L189)

```python
def register_instances_with_load_balancer(
    LoadBalancerName: str,
    Instances: List[Any],
) -> Dict[str, Any]:
```

### Client().remove_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L195)

```python
def remove_tags(
    LoadBalancerNames: List[Any],
    Tags: List[Any],
) -> Dict[str, Any]:
```

### Client().set_load_balancer_listener_ssl_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L201)

```python
def set_load_balancer_listener_ssl_certificate(
    LoadBalancerName: str,
    LoadBalancerPort: int,
    SSLCertificateId: str,
) -> Dict[str, Any]:
```

### Client().set_load_balancer_policies_for_backend_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L207)

```python
def set_load_balancer_policies_for_backend_server(
    LoadBalancerName: str,
    InstancePort: int,
    PolicyNames: List[Any],
) -> Dict[str, Any]:
```

### Client().set_load_balancer_policies_of_listener

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/client.py#L213)

```python
def set_load_balancer_policies_of_listener(
    LoadBalancerName: str,
    LoadBalancerPort: int,
    PolicyNames: List[Any],
) -> Dict[str, Any]:
```
