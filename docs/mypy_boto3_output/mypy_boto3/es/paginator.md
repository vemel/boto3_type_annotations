# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.es.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Es](index.md#es) / Paginator
    - [DescribeReservedElasticsearchInstanceOfferings](#describereservedelasticsearchinstanceofferings)
        - [DescribeReservedElasticsearchInstanceOfferings().paginate](#describereservedelasticsearchinstanceofferingspaginate)
    - [DescribeReservedElasticsearchInstances](#describereservedelasticsearchinstances)
        - [DescribeReservedElasticsearchInstances().paginate](#describereservedelasticsearchinstancespaginate)
    - [GetUpgradeHistory](#getupgradehistory)
        - [GetUpgradeHistory().paginate](#getupgradehistorypaginate)
    - [ListElasticsearchInstanceTypes](#listelasticsearchinstancetypes)
        - [ListElasticsearchInstanceTypes().paginate](#listelasticsearchinstancetypespaginate)
    - [ListElasticsearchVersions](#listelasticsearchversions)
        - [ListElasticsearchVersions().paginate](#listelasticsearchversionspaginate)

## DescribeReservedElasticsearchInstanceOfferings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py#L9)

```python
class DescribeReservedElasticsearchInstanceOfferings(Paginator):
```

### DescribeReservedElasticsearchInstanceOfferings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py#L12)

```python
def paginate(
    ReservedElasticsearchInstanceOfferingId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeReservedElasticsearchInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py#L20)

```python
class DescribeReservedElasticsearchInstances(Paginator):
```

### DescribeReservedElasticsearchInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py#L23)

```python
def paginate(
    ReservedElasticsearchInstanceId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetUpgradeHistory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py#L31)

```python
class GetUpgradeHistory(Paginator):
```

### GetUpgradeHistory().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py#L34)

```python
def paginate(
    DomainName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListElasticsearchInstanceTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py#L40)

```python
class ListElasticsearchInstanceTypes(Paginator):
```

### ListElasticsearchInstanceTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py#L43)

```python
def paginate(
    ElasticsearchVersion: str,
    DomainName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListElasticsearchVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py#L52)

```python
class ListElasticsearchVersions(Paginator):
```

### ListElasticsearchVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/paginator.py#L55)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
