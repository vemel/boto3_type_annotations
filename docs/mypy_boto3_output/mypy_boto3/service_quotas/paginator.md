# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.service_quotas.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Service Quotas](index.md#service-quotas) / Paginator
    - [ListAWSDefaultServiceQuotas](#listawsdefaultservicequotas)
        - [ListAWSDefaultServiceQuotas().paginate](#listawsdefaultservicequotaspaginate)
    - [ListRequestedServiceQuotaChangeHistory](#listrequestedservicequotachangehistory)
        - [ListRequestedServiceQuotaChangeHistory().paginate](#listrequestedservicequotachangehistorypaginate)
    - [ListRequestedServiceQuotaChangeHistoryByQuota](#listrequestedservicequotachangehistorybyquota)
        - [ListRequestedServiceQuotaChangeHistoryByQuota().paginate](#listrequestedservicequotachangehistorybyquotapaginate)
    - [ListServiceQuotaIncreaseRequestsInTemplate](#listservicequotaincreaserequestsintemplate)
        - [ListServiceQuotaIncreaseRequestsInTemplate().paginate](#listservicequotaincreaserequestsintemplatepaginate)
    - [ListServiceQuotas](#listservicequotas)
        - [ListServiceQuotas().paginate](#listservicequotaspaginate)
    - [ListServices](#listservices)
        - [ListServices().paginate](#listservicespaginate)

## ListAWSDefaultServiceQuotas

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L9)

```python
class ListAWSDefaultServiceQuotas(Paginator):
```

### ListAWSDefaultServiceQuotas().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L12)

```python
def paginate(
    ServiceCode: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRequestedServiceQuotaChangeHistory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L18)

```python
class ListRequestedServiceQuotaChangeHistory(Paginator):
```

### ListRequestedServiceQuotaChangeHistory().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L21)

```python
def paginate(
    ServiceCode: str = None,
    Status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRequestedServiceQuotaChangeHistoryByQuota

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L30)

```python
class ListRequestedServiceQuotaChangeHistoryByQuota(Paginator):
```

### ListRequestedServiceQuotaChangeHistoryByQuota().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L33)

```python
def paginate(
    ServiceCode: str,
    QuotaCode: str,
    Status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListServiceQuotaIncreaseRequestsInTemplate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L43)

```python
class ListServiceQuotaIncreaseRequestsInTemplate(Paginator):
```

### ListServiceQuotaIncreaseRequestsInTemplate().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L46)

```python
def paginate(
    ServiceCode: str = None,
    AwsRegion: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListServiceQuotas

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L55)

```python
class ListServiceQuotas(Paginator):
```

### ListServiceQuotas().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L58)

```python
def paginate(
    ServiceCode: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListServices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L64)

```python
class ListServices(Paginator):
```

### ListServices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/paginator.py#L67)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
