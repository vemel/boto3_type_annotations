# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ecs.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ecs](index.md#ecs) / Paginator
    - [ListAccountSettings](#listaccountsettings)
        - [ListAccountSettings().paginate](#listaccountsettingspaginate)
    - [ListAttributes](#listattributes)
        - [ListAttributes().paginate](#listattributespaginate)
    - [ListClusters](#listclusters)
        - [ListClusters().paginate](#listclusterspaginate)
    - [ListContainerInstances](#listcontainerinstances)
        - [ListContainerInstances().paginate](#listcontainerinstancespaginate)
    - [ListServices](#listservices)
        - [ListServices().paginate](#listservicespaginate)
    - [ListTaskDefinitionFamilies](#listtaskdefinitionfamilies)
        - [ListTaskDefinitionFamilies().paginate](#listtaskdefinitionfamiliespaginate)
    - [ListTaskDefinitions](#listtaskdefinitions)
        - [ListTaskDefinitions().paginate](#listtaskdefinitionspaginate)
    - [ListTasks](#listtasks)
        - [ListTasks().paginate](#listtaskspaginate)

## ListAccountSettings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L9)

```python
class ListAccountSettings(Paginator):
```

### ListAccountSettings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L12)

```python
def paginate(
    name: str = None,
    value: str = None,
    principalArn: str = None,
    effectiveSettings: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAttributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L23)

```python
class ListAttributes(Paginator):
```

### ListAttributes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L26)

```python
def paginate(
    targetType: str,
    cluster: str = None,
    attributeName: str = None,
    attributeValue: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L37)

```python
class ListClusters(Paginator):
```

### ListClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L40)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListContainerInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L44)

```python
class ListContainerInstances(Paginator):
```

### ListContainerInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L47)

```python
def paginate(
    cluster: str = None,
    filter: str = None,
    status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListServices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L57)

```python
class ListServices(Paginator):
```

### ListServices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L60)

```python
def paginate(
    cluster: str = None,
    launchType: str = None,
    schedulingStrategy: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTaskDefinitionFamilies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L70)

```python
class ListTaskDefinitionFamilies(Paginator):
```

### ListTaskDefinitionFamilies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L73)

```python
def paginate(
    familyPrefix: str = None,
    status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTaskDefinitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L82)

```python
class ListTaskDefinitions(Paginator):
```

### ListTaskDefinitions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L85)

```python
def paginate(
    familyPrefix: str = None,
    status: str = None,
    sort: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L95)

```python
class ListTasks(Paginator):
```

### ListTasks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/paginator.py#L98)

```python
def paginate(
    cluster: str = None,
    containerInstance: str = None,
    family: str = None,
    startedBy: str = None,
    serviceName: str = None,
    desiredStatus: str = None,
    launchType: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
