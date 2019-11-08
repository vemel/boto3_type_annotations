# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kinesis_video_archived_media.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kinesis Video Archived Media](index.md#kinesis-video-archived-media) / Paginator
    - [ListFragments](#listfragments)
        - [ListFragments().paginate](#listfragmentspaginate)

## ListFragments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/paginator.py#L9)

```python
class ListFragments(Paginator):
```

### ListFragments().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/paginator.py#L12)

```python
def paginate(
    StreamName: str,
    FragmentSelector: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
