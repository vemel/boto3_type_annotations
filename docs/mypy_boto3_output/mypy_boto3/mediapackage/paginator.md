# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mediapackage.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mediapackage](index.md#mediapackage) / Paginator
    - [ListChannels](#listchannels)
        - [ListChannels().paginate](#listchannelspaginate)
    - [ListHarvestJobs](#listharvestjobs)
        - [ListHarvestJobs().paginate](#listharvestjobspaginate)
    - [ListOriginEndpoints](#listoriginendpoints)
        - [ListOriginEndpoints().paginate](#listoriginendpointspaginate)

## ListChannels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/paginator.py#L9)

```python
class ListChannels(Paginator):
```

### ListChannels().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListHarvestJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/paginator.py#L16)

```python
class ListHarvestJobs(Paginator):
```

### ListHarvestJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/paginator.py#L19)

```python
def paginate(
    IncludeChannelId: str = None,
    IncludeStatus: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListOriginEndpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/paginator.py#L28)

```python
class ListOriginEndpoints(Paginator):
```

### ListOriginEndpoints().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/paginator.py#L31)

```python
def paginate(
    ChannelId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
