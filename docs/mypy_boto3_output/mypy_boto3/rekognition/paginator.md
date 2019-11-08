# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.rekognition.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Rekognition](index.md#rekognition) / Paginator
    - [ListCollections](#listcollections)
        - [ListCollections().paginate](#listcollectionspaginate)
    - [ListFaces](#listfaces)
        - [ListFaces().paginate](#listfacespaginate)
    - [ListStreamProcessors](#liststreamprocessors)
        - [ListStreamProcessors().paginate](#liststreamprocessorspaginate)

## ListCollections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/paginator.py#L9)

```python
class ListCollections(Paginator):
```

### ListCollections().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListFaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/paginator.py#L16)

```python
class ListFaces(Paginator):
```

### ListFaces().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/paginator.py#L19)

```python
def paginate(
    CollectionId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStreamProcessors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/paginator.py#L25)

```python
class ListStreamProcessors(Paginator):
```

### ListStreamProcessors().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/paginator.py#L28)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
