# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.health.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Health](index.md#health) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().describe_affected_entities](#clientdescribe_affected_entities)
        - [Client().describe_entity_aggregates](#clientdescribe_entity_aggregates)
        - [Client().describe_event_aggregates](#clientdescribe_event_aggregates)
        - [Client().describe_event_details](#clientdescribe_event_details)
        - [Client().describe_event_types](#clientdescribe_event_types)
        - [Client().describe_events](#clientdescribe_events)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().describe_affected_entities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L19)

```python
def describe_affected_entities(
    filter: Dict[str, Any],
    locale: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_entity_aggregates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L29)

```python
def describe_entity_aggregates(eventArns: List[Any] = None) -> Dict[str, Any]:
```

### Client().describe_event_aggregates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L33)

```python
def describe_event_aggregates(
    aggregateField: str,
    filter: Dict[str, Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_event_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L43)

```python
def describe_event_details(
    eventArns: List[Any],
    locale: str = None,
) -> Dict[str, Any]:
```

### Client().describe_event_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L49)

```python
def describe_event_types(
    filter: Dict[str, Any] = None,
    locale: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L59)

```python
def describe_events(
    filter: Dict[str, Any] = None,
    nextToken: str = None,
    maxResults: int = None,
    locale: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L69)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L79)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/client.py#L83)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```
