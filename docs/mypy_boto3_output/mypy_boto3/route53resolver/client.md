# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.route53resolver.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Route53resolver](index.md#route53resolver) / Client
    - [Client](#client)
        - [Client().associate_resolver_endpoint_ip_address](#clientassociate_resolver_endpoint_ip_address)
        - [Client().associate_resolver_rule](#clientassociate_resolver_rule)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_resolver_endpoint](#clientcreate_resolver_endpoint)
        - [Client().create_resolver_rule](#clientcreate_resolver_rule)
        - [Client().delete_resolver_endpoint](#clientdelete_resolver_endpoint)
        - [Client().delete_resolver_rule](#clientdelete_resolver_rule)
        - [Client().disassociate_resolver_endpoint_ip_address](#clientdisassociate_resolver_endpoint_ip_address)
        - [Client().disassociate_resolver_rule](#clientdisassociate_resolver_rule)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_resolver_endpoint](#clientget_resolver_endpoint)
        - [Client().get_resolver_rule](#clientget_resolver_rule)
        - [Client().get_resolver_rule_association](#clientget_resolver_rule_association)
        - [Client().get_resolver_rule_policy](#clientget_resolver_rule_policy)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_resolver_endpoint_ip_addresses](#clientlist_resolver_endpoint_ip_addresses)
        - [Client().list_resolver_endpoints](#clientlist_resolver_endpoints)
        - [Client().list_resolver_rule_associations](#clientlist_resolver_rule_associations)
        - [Client().list_resolver_rules](#clientlist_resolver_rules)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_resolver_rule_policy](#clientput_resolver_rule_policy)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_resolver_endpoint](#clientupdate_resolver_endpoint)
        - [Client().update_resolver_rule](#clientupdate_resolver_rule)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_resolver_endpoint_ip_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L15)

```python
def associate_resolver_endpoint_ip_address(
    ResolverEndpointId: str,
    IpAddress: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().associate_resolver_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L21)

```python
def associate_resolver_rule(
    ResolverRuleId: str,
    VPCId: str,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L27)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_resolver_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L31)

```python
def create_resolver_endpoint(
    CreatorRequestId: str,
    SecurityGroupIds: List[Any],
    Direction: str,
    IpAddresses: List[Any],
    Name: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_resolver_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L43)

```python
def create_resolver_rule(
    CreatorRequestId: str,
    RuleType: str,
    DomainName: str,
    Name: str = None,
    TargetIps: List[Any] = None,
    ResolverEndpointId: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_resolver_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L56)

```python
def delete_resolver_endpoint(ResolverEndpointId: str) -> Dict[str, Any]:
```

### Client().delete_resolver_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L60)

```python
def delete_resolver_rule(ResolverRuleId: str) -> Dict[str, Any]:
```

### Client().disassociate_resolver_endpoint_ip_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L64)

```python
def disassociate_resolver_endpoint_ip_address(
    ResolverEndpointId: str,
    IpAddress: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().disassociate_resolver_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L70)

```python
def disassociate_resolver_rule(
    VPCId: str,
    ResolverRuleId: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L76)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L86)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_resolver_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L90)

```python
def get_resolver_endpoint(ResolverEndpointId: str) -> Dict[str, Any]:
```

### Client().get_resolver_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L94)

```python
def get_resolver_rule(ResolverRuleId: str) -> Dict[str, Any]:
```

### Client().get_resolver_rule_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L98)

```python
def get_resolver_rule_association(
    ResolverRuleAssociationId: str,
) -> Dict[str, Any]:
```

### Client().get_resolver_rule_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L104)

```python
def get_resolver_rule_policy(Arn: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L108)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_resolver_endpoint_ip_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L112)

```python
def list_resolver_endpoint_ip_addresses(
    ResolverEndpointId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_resolver_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L118)

```python
def list_resolver_endpoints(
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_resolver_rule_associations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L124)

```python
def list_resolver_rule_associations(
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_resolver_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L130)

```python
def list_resolver_rules(
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L136)

```python
def list_tags_for_resource(
    ResourceArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_resolver_rule_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L142)

```python
def put_resolver_rule_policy(
    Arn: str,
    ResolverRulePolicy: str,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L148)

```python
def tag_resource(ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L152)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_resolver_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L156)

```python
def update_resolver_endpoint(
    ResolverEndpointId: str,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().update_resolver_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53resolver/client.py#L162)

```python
def update_resolver_rule(
    ResolverRuleId: str,
    Config: Dict[str, Any],
) -> Dict[str, Any]:
```
