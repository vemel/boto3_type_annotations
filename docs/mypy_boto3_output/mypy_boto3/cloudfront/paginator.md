# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudfront.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudfront](index.md#cloudfront) / Paginator
    - [ListCloudFrontOriginAccessIdentities](#listcloudfrontoriginaccessidentities)
        - [ListCloudFrontOriginAccessIdentities().paginate](#listcloudfrontoriginaccessidentitiespaginate)
    - [ListDistributions](#listdistributions)
        - [ListDistributions().paginate](#listdistributionspaginate)
    - [ListInvalidations](#listinvalidations)
        - [ListInvalidations().paginate](#listinvalidationspaginate)
    - [ListStreamingDistributions](#liststreamingdistributions)
        - [ListStreamingDistributions().paginate](#liststreamingdistributionspaginate)

## ListCloudFrontOriginAccessIdentities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/paginator.py#L9)

```python
class ListCloudFrontOriginAccessIdentities(Paginator):
```

### ListCloudFrontOriginAccessIdentities().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListDistributions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/paginator.py#L16)

```python
class ListDistributions(Paginator):
```

### ListDistributions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/paginator.py#L19)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListInvalidations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/paginator.py#L23)

```python
class ListInvalidations(Paginator):
```

### ListInvalidations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/paginator.py#L26)

```python
def paginate(
    DistributionId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStreamingDistributions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/paginator.py#L32)

```python
class ListStreamingDistributions(Paginator):
```

### ListStreamingDistributions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/paginator.py#L35)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
