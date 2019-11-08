# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elastictranscoder.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elastictranscoder](index.md#elastictranscoder) / Paginator
    - [ListJobsByPipeline](#listjobsbypipeline)
        - [ListJobsByPipeline().paginate](#listjobsbypipelinepaginate)
    - [ListJobsByStatus](#listjobsbystatus)
        - [ListJobsByStatus().paginate](#listjobsbystatuspaginate)
    - [ListPipelines](#listpipelines)
        - [ListPipelines().paginate](#listpipelinespaginate)
    - [ListPresets](#listpresets)
        - [ListPresets().paginate](#listpresetspaginate)

## ListJobsByPipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/paginator.py#L9)

```python
class ListJobsByPipeline(Paginator):
```

### ListJobsByPipeline().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/paginator.py#L12)

```python
def paginate(
    PipelineId: str,
    Ascending: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListJobsByStatus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/paginator.py#L21)

```python
class ListJobsByStatus(Paginator):
```

### ListJobsByStatus().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/paginator.py#L24)

```python
def paginate(
    Status: str,
    Ascending: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPipelines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/paginator.py#L33)

```python
class ListPipelines(Paginator):
```

### ListPipelines().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/paginator.py#L36)

```python
def paginate(
    Ascending: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPresets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/paginator.py#L42)

```python
class ListPresets(Paginator):
```

### ListPresets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/paginator.py#L45)

```python
def paginate(
    Ascending: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
