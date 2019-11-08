# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kafka.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kafka](index.md#kafka) / Paginator
    - [ListClusterOperations](#listclusteroperations)
        - [ListClusterOperations().paginate](#listclusteroperationspaginate)
    - [ListClusters](#listclusters)
        - [ListClusters().paginate](#listclusterspaginate)
    - [ListConfigurationRevisions](#listconfigurationrevisions)
        - [ListConfigurationRevisions().paginate](#listconfigurationrevisionspaginate)
    - [ListConfigurations](#listconfigurations)
        - [ListConfigurations().paginate](#listconfigurationspaginate)
    - [ListNodes](#listnodes)
        - [ListNodes().paginate](#listnodespaginate)

## ListClusterOperations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py#L9)

```python
class ListClusterOperations(Paginator):
```

### ListClusterOperations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py#L12)

```python
def paginate(
    ClusterArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py#L18)

```python
class ListClusters(Paginator):
```

### ListClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py#L21)

```python
def paginate(
    ClusterNameFilter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListConfigurationRevisions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py#L27)

```python
class ListConfigurationRevisions(Paginator):
```

### ListConfigurationRevisions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py#L30)

```python
def paginate(
    Arn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListConfigurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py#L36)

```python
class ListConfigurations(Paginator):
```

### ListConfigurations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py#L39)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListNodes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py#L43)

```python
class ListNodes(Paginator):
```

### ListNodes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kafka/paginator.py#L46)

```python
def paginate(
    ClusterArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
