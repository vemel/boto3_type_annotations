# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sms.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sms](index.md#sms) / Paginator
    - [GetConnectors](#getconnectors)
        - [GetConnectors().paginate](#getconnectorspaginate)
    - [GetReplicationJobs](#getreplicationjobs)
        - [GetReplicationJobs().paginate](#getreplicationjobspaginate)
    - [GetReplicationRuns](#getreplicationruns)
        - [GetReplicationRuns().paginate](#getreplicationrunspaginate)
    - [GetServers](#getservers)
        - [GetServers().paginate](#getserverspaginate)
    - [ListApps](#listapps)
        - [ListApps().paginate](#listappspaginate)

## GetConnectors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py#L10)

```python
class GetConnectors(Paginator):
```

### GetConnectors().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py#L13)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetReplicationJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py#L17)

```python
class GetReplicationJobs(Paginator):
```

### GetReplicationJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py#L20)

```python
def paginate(
    replicationJobId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetReplicationRuns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py#L26)

```python
class GetReplicationRuns(Paginator):
```

### GetReplicationRuns().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py#L29)

```python
def paginate(
    replicationJobId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetServers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py#L35)

```python
class GetServers(Paginator):
```

### GetServers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py#L38)

```python
def paginate(
    vmServerAddressList: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListApps

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py#L46)

```python
class ListApps(Paginator):
```

### ListApps().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/paginator.py#L49)

```python
def paginate(
    appIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
