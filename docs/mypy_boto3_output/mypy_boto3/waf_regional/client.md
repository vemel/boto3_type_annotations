# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.waf_regional.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Waf Regional](index.md#waf-regional) / Client
    - [Client](#client)
        - [Client().associate_web_acl](#clientassociate_web_acl)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_byte_match_set](#clientcreate_byte_match_set)
        - [Client().create_geo_match_set](#clientcreate_geo_match_set)
        - [Client().create_ip_set](#clientcreate_ip_set)
        - [Client().create_rate_based_rule](#clientcreate_rate_based_rule)
        - [Client().create_regex_match_set](#clientcreate_regex_match_set)
        - [Client().create_regex_pattern_set](#clientcreate_regex_pattern_set)
        - [Client().create_rule](#clientcreate_rule)
        - [Client().create_rule_group](#clientcreate_rule_group)
        - [Client().create_size_constraint_set](#clientcreate_size_constraint_set)
        - [Client().create_sql_injection_match_set](#clientcreate_sql_injection_match_set)
        - [Client().create_web_acl](#clientcreate_web_acl)
        - [Client().create_xss_match_set](#clientcreate_xss_match_set)
        - [Client().delete_byte_match_set](#clientdelete_byte_match_set)
        - [Client().delete_geo_match_set](#clientdelete_geo_match_set)
        - [Client().delete_ip_set](#clientdelete_ip_set)
        - [Client().delete_logging_configuration](#clientdelete_logging_configuration)
        - [Client().delete_permission_policy](#clientdelete_permission_policy)
        - [Client().delete_rate_based_rule](#clientdelete_rate_based_rule)
        - [Client().delete_regex_match_set](#clientdelete_regex_match_set)
        - [Client().delete_regex_pattern_set](#clientdelete_regex_pattern_set)
        - [Client().delete_rule](#clientdelete_rule)
        - [Client().delete_rule_group](#clientdelete_rule_group)
        - [Client().delete_size_constraint_set](#clientdelete_size_constraint_set)
        - [Client().delete_sql_injection_match_set](#clientdelete_sql_injection_match_set)
        - [Client().delete_web_acl](#clientdelete_web_acl)
        - [Client().delete_xss_match_set](#clientdelete_xss_match_set)
        - [Client().disassociate_web_acl](#clientdisassociate_web_acl)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_byte_match_set](#clientget_byte_match_set)
        - [Client().get_change_token](#clientget_change_token)
        - [Client().get_change_token_status](#clientget_change_token_status)
        - [Client().get_geo_match_set](#clientget_geo_match_set)
        - [Client().get_ip_set](#clientget_ip_set)
        - [Client().get_logging_configuration](#clientget_logging_configuration)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_permission_policy](#clientget_permission_policy)
        - [Client().get_rate_based_rule](#clientget_rate_based_rule)
        - [Client().get_rate_based_rule_managed_keys](#clientget_rate_based_rule_managed_keys)
        - [Client().get_regex_match_set](#clientget_regex_match_set)
        - [Client().get_regex_pattern_set](#clientget_regex_pattern_set)
        - [Client().get_rule](#clientget_rule)
        - [Client().get_rule_group](#clientget_rule_group)
        - [Client().get_sampled_requests](#clientget_sampled_requests)
        - [Client().get_size_constraint_set](#clientget_size_constraint_set)
        - [Client().get_sql_injection_match_set](#clientget_sql_injection_match_set)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().get_web_acl](#clientget_web_acl)
        - [Client().get_web_acl_for_resource](#clientget_web_acl_for_resource)
        - [Client().get_xss_match_set](#clientget_xss_match_set)
        - [Client().list_activated_rules_in_rule_group](#clientlist_activated_rules_in_rule_group)
        - [Client().list_byte_match_sets](#clientlist_byte_match_sets)
        - [Client().list_geo_match_sets](#clientlist_geo_match_sets)
        - [Client().list_ip_sets](#clientlist_ip_sets)
        - [Client().list_logging_configurations](#clientlist_logging_configurations)
        - [Client().list_rate_based_rules](#clientlist_rate_based_rules)
        - [Client().list_regex_match_sets](#clientlist_regex_match_sets)
        - [Client().list_regex_pattern_sets](#clientlist_regex_pattern_sets)
        - [Client().list_resources_for_web_acl](#clientlist_resources_for_web_acl)
        - [Client().list_rule_groups](#clientlist_rule_groups)
        - [Client().list_rules](#clientlist_rules)
        - [Client().list_size_constraint_sets](#clientlist_size_constraint_sets)
        - [Client().list_sql_injection_match_sets](#clientlist_sql_injection_match_sets)
        - [Client().list_subscribed_rule_groups](#clientlist_subscribed_rule_groups)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_web_acls](#clientlist_web_acls)
        - [Client().list_xss_match_sets](#clientlist_xss_match_sets)
        - [Client().put_logging_configuration](#clientput_logging_configuration)
        - [Client().put_permission_policy](#clientput_permission_policy)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_byte_match_set](#clientupdate_byte_match_set)
        - [Client().update_geo_match_set](#clientupdate_geo_match_set)
        - [Client().update_ip_set](#clientupdate_ip_set)
        - [Client().update_rate_based_rule](#clientupdate_rate_based_rule)
        - [Client().update_regex_match_set](#clientupdate_regex_match_set)
        - [Client().update_regex_pattern_set](#clientupdate_regex_pattern_set)
        - [Client().update_rule](#clientupdate_rule)
        - [Client().update_rule_group](#clientupdate_rule_group)
        - [Client().update_size_constraint_set](#clientupdate_size_constraint_set)
        - [Client().update_sql_injection_match_set](#clientupdate_sql_injection_match_set)
        - [Client().update_web_acl](#clientupdate_web_acl)
        - [Client().update_xss_match_set](#clientupdate_xss_match_set)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_web_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L15)

```python
def associate_web_acl(WebACLId: str, ResourceArn: str) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_byte_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L23)

```python
def create_byte_match_set(Name: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().create_geo_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L27)

```python
def create_geo_match_set(Name: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().create_ip_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L31)

```python
def create_ip_set(Name: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().create_rate_based_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L35)

```python
def create_rate_based_rule(
    Name: str,
    MetricName: str,
    RateKey: str,
    RateLimit: int,
    ChangeToken: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_regex_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L47)

```python
def create_regex_match_set(Name: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().create_regex_pattern_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L51)

```python
def create_regex_pattern_set(Name: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().create_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L55)

```python
def create_rule(
    Name: str,
    MetricName: str,
    ChangeToken: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_rule_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L61)

```python
def create_rule_group(
    Name: str,
    MetricName: str,
    ChangeToken: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_size_constraint_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L67)

```python
def create_size_constraint_set(Name: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().create_sql_injection_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L71)

```python
def create_sql_injection_match_set(
    Name: str,
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().create_web_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L77)

```python
def create_web_acl(
    Name: str,
    MetricName: str,
    DefaultAction: Dict[str, Any],
    ChangeToken: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_xss_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L88)

```python
def create_xss_match_set(Name: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().delete_byte_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L92)

```python
def delete_byte_match_set(
    ByteMatchSetId: str,
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().delete_geo_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L98)

```python
def delete_geo_match_set(
    GeoMatchSetId: str,
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().delete_ip_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L104)

```python
def delete_ip_set(IPSetId: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().delete_logging_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L108)

```python
def delete_logging_configuration(ResourceArn: str) -> Dict[str, Any]:
```

### Client().delete_permission_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L112)

```python
def delete_permission_policy(ResourceArn: str) -> Dict[str, Any]:
```

### Client().delete_rate_based_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L116)

```python
def delete_rate_based_rule(RuleId: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().delete_regex_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L120)

```python
def delete_regex_match_set(
    RegexMatchSetId: str,
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().delete_regex_pattern_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L126)

```python
def delete_regex_pattern_set(
    RegexPatternSetId: str,
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().delete_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L132)

```python
def delete_rule(RuleId: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().delete_rule_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L136)

```python
def delete_rule_group(RuleGroupId: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().delete_size_constraint_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L140)

```python
def delete_size_constraint_set(
    SizeConstraintSetId: str,
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().delete_sql_injection_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L146)

```python
def delete_sql_injection_match_set(
    SqlInjectionMatchSetId: str,
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().delete_web_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L152)

```python
def delete_web_acl(WebACLId: str, ChangeToken: str) -> Dict[str, Any]:
```

### Client().delete_xss_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L156)

```python
def delete_xss_match_set(
    XssMatchSetId: str,
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().disassociate_web_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L162)

```python
def disassociate_web_acl(ResourceArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L166)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_byte_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L176)

```python
def get_byte_match_set(ByteMatchSetId: str) -> Dict[str, Any]:
```

### Client().get_change_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L180)

```python
def get_change_token() -> Dict[str, Any]:
```

### Client().get_change_token_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L184)

```python
def get_change_token_status(ChangeToken: str) -> Dict[str, Any]:
```

### Client().get_geo_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L188)

```python
def get_geo_match_set(GeoMatchSetId: str) -> Dict[str, Any]:
```

### Client().get_ip_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L192)

```python
def get_ip_set(IPSetId: str) -> Dict[str, Any]:
```

### Client().get_logging_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L196)

```python
def get_logging_configuration(ResourceArn: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L200)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_permission_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L204)

```python
def get_permission_policy(ResourceArn: str) -> Dict[str, Any]:
```

### Client().get_rate_based_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L208)

```python
def get_rate_based_rule(RuleId: str) -> Dict[str, Any]:
```

### Client().get_rate_based_rule_managed_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L212)

```python
def get_rate_based_rule_managed_keys(
    RuleId: str,
    NextMarker: str = None,
) -> Dict[str, Any]:
```

### Client().get_regex_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L218)

```python
def get_regex_match_set(RegexMatchSetId: str) -> Dict[str, Any]:
```

### Client().get_regex_pattern_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L222)

```python
def get_regex_pattern_set(RegexPatternSetId: str) -> Dict[str, Any]:
```

### Client().get_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L226)

```python
def get_rule(RuleId: str) -> Dict[str, Any]:
```

### Client().get_rule_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L230)

```python
def get_rule_group(RuleGroupId: str) -> Dict[str, Any]:
```

### Client().get_sampled_requests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L234)

```python
def get_sampled_requests(
    WebAclId: str,
    RuleId: str,
    TimeWindow: Dict[str, Any],
    MaxItems: int,
) -> Dict[str, Any]:
```

### Client().get_size_constraint_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L240)

```python
def get_size_constraint_set(SizeConstraintSetId: str) -> Dict[str, Any]:
```

### Client().get_sql_injection_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L244)

```python
def get_sql_injection_match_set(
    SqlInjectionMatchSetId: str,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L250)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().get_web_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L254)

```python
def get_web_acl(WebACLId: str) -> Dict[str, Any]:
```

### Client().get_web_acl_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L258)

```python
def get_web_acl_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().get_xss_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L262)

```python
def get_xss_match_set(XssMatchSetId: str) -> Dict[str, Any]:
```

### Client().list_activated_rules_in_rule_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L266)

```python
def list_activated_rules_in_rule_group(
    RuleGroupId: str = None,
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_byte_match_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L272)

```python
def list_byte_match_sets(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_geo_match_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L278)

```python
def list_geo_match_sets(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_ip_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L284)

```python
def list_ip_sets(NextMarker: str = None, Limit: int = None) -> Dict[str, Any]:
```

### Client().list_logging_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L288)

```python
def list_logging_configurations(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_rate_based_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L294)

```python
def list_rate_based_rules(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_regex_match_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L300)

```python
def list_regex_match_sets(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_regex_pattern_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L306)

```python
def list_regex_pattern_sets(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_resources_for_web_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L312)

```python
def list_resources_for_web_acl(
    WebACLId: str,
    ResourceType: str = None,
) -> Dict[str, Any]:
```

### Client().list_rule_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L318)

```python
def list_rule_groups(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L324)

```python
def list_rules(NextMarker: str = None, Limit: int = None) -> Dict[str, Any]:
```

### Client().list_size_constraint_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L328)

```python
def list_size_constraint_sets(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_sql_injection_match_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L334)

```python
def list_sql_injection_match_sets(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_subscribed_rule_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L340)

```python
def list_subscribed_rule_groups(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L346)

```python
def list_tags_for_resource(
    ResourceARN: str,
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_web_acls

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L352)

```python
def list_web_acls(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_xss_match_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L358)

```python
def list_xss_match_sets(
    NextMarker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().put_logging_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L364)

```python
def put_logging_configuration(
    LoggingConfiguration: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_permission_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L370)

```python
def put_permission_policy(ResourceArn: str, Policy: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L374)

```python
def tag_resource(ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L378)

```python
def untag_resource(ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_byte_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L382)

```python
def update_byte_match_set(
    ByteMatchSetId: str,
    ChangeToken: str,
    Updates: List[Any],
) -> Dict[str, Any]:
```

### Client().update_geo_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L388)

```python
def update_geo_match_set(
    GeoMatchSetId: str,
    ChangeToken: str,
    Updates: List[Any],
) -> Dict[str, Any]:
```

### Client().update_ip_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L394)

```python
def update_ip_set(
    IPSetId: str,
    ChangeToken: str,
    Updates: List[Any],
) -> Dict[str, Any]:
```

### Client().update_rate_based_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L400)

```python
def update_rate_based_rule(
    RuleId: str,
    ChangeToken: str,
    Updates: List[Any],
    RateLimit: int,
) -> Dict[str, Any]:
```

### Client().update_regex_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L406)

```python
def update_regex_match_set(
    RegexMatchSetId: str,
    Updates: List[Any],
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().update_regex_pattern_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L412)

```python
def update_regex_pattern_set(
    RegexPatternSetId: str,
    Updates: List[Any],
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().update_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L418)

```python
def update_rule(
    RuleId: str,
    ChangeToken: str,
    Updates: List[Any],
) -> Dict[str, Any]:
```

### Client().update_rule_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L424)

```python
def update_rule_group(
    RuleGroupId: str,
    Updates: List[Any],
    ChangeToken: str,
) -> Dict[str, Any]:
```

### Client().update_size_constraint_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L430)

```python
def update_size_constraint_set(
    SizeConstraintSetId: str,
    ChangeToken: str,
    Updates: List[Any],
) -> Dict[str, Any]:
```

### Client().update_sql_injection_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L436)

```python
def update_sql_injection_match_set(
    SqlInjectionMatchSetId: str,
    ChangeToken: str,
    Updates: List[Any],
) -> Dict[str, Any]:
```

### Client().update_web_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L442)

```python
def update_web_acl(
    WebACLId: str,
    ChangeToken: str,
    Updates: List[Any] = None,
    DefaultAction: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_xss_match_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/waf_regional/client.py#L452)

```python
def update_xss_match_set(
    XssMatchSetId: str,
    ChangeToken: str,
    Updates: List[Any],
) -> Dict[str, Any]:
```
