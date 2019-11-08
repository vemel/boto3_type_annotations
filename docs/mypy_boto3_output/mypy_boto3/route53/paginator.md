# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.route53.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Route53](index.md#route53) / Paginator
    - [ListHealthChecks](#listhealthchecks)
        - [ListHealthChecks().paginate](#listhealthcheckspaginate)
    - [ListHostedZones](#listhostedzones)
        - [ListHostedZones().paginate](#listhostedzonespaginate)
    - [ListQueryLoggingConfigs](#listqueryloggingconfigs)
        - [ListQueryLoggingConfigs().paginate](#listqueryloggingconfigspaginate)
    - [ListResourceRecordSets](#listresourcerecordsets)
        - [ListResourceRecordSets().paginate](#listresourcerecordsetspaginate)
    - [ListVPCAssociationAuthorizations](#listvpcassociationauthorizations)
        - [ListVPCAssociationAuthorizations().paginate](#listvpcassociationauthorizationspaginate)

## ListHealthChecks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py#L9)

```python
class ListHealthChecks(Paginator):
```

### ListHealthChecks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListHostedZones

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py#L16)

```python
class ListHostedZones(Paginator):
```

### ListHostedZones().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py#L19)

```python
def paginate(
    DelegationSetId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListQueryLoggingConfigs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py#L25)

```python
class ListQueryLoggingConfigs(Paginator):
```

### ListQueryLoggingConfigs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py#L28)

```python
def paginate(
    HostedZoneId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListResourceRecordSets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py#L34)

```python
class ListResourceRecordSets(Paginator):
```

### ListResourceRecordSets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py#L37)

```python
def paginate(
    HostedZoneId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListVPCAssociationAuthorizations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py#L43)

```python
class ListVPCAssociationAuthorizations(Paginator):
```

### ListVPCAssociationAuthorizations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53/paginator.py#L46)

```python
def paginate(
    HostedZoneId: str,
    MaxResults: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
