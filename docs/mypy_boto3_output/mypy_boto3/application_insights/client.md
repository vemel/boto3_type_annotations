# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.application_insights.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Application Insights](index.md#application-insights) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_application](#clientcreate_application)
        - [Client().create_component](#clientcreate_component)
        - [Client().delete_application](#clientdelete_application)
        - [Client().delete_component](#clientdelete_component)
        - [Client().describe_application](#clientdescribe_application)
        - [Client().describe_component](#clientdescribe_component)
        - [Client().describe_component_configuration](#clientdescribe_component_configuration)
        - [Client().describe_component_configuration_recommendation](#clientdescribe_component_configuration_recommendation)
        - [Client().describe_observation](#clientdescribe_observation)
        - [Client().describe_problem](#clientdescribe_problem)
        - [Client().describe_problem_observations](#clientdescribe_problem_observations)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_applications](#clientlist_applications)
        - [Client().list_components](#clientlist_components)
        - [Client().list_problems](#clientlist_problems)
        - [Client().update_application](#clientupdate_application)
        - [Client().update_component](#clientupdate_component)
        - [Client().update_component_configuration](#clientupdate_component_configuration)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L20)

```python
def create_application(
    ResourceGroupName: str,
    OpsCenterEnabled: bool = None,
    OpsItemSNSTopicArn: str = None,
) -> Dict[str, Any]:
```

### Client().create_component

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L29)

```python
def create_component(
    ResourceGroupName: str,
    ComponentName: str,
    ResourceList: List[Any],
) -> Dict[str, Any]:
```

### Client().delete_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L35)

```python
def delete_application(ResourceGroupName: str) -> Dict[str, Any]:
```

### Client().delete_component

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L39)

```python
def delete_component(
    ResourceGroupName: str,
    ComponentName: str,
) -> Dict[str, Any]:
```

### Client().describe_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L45)

```python
def describe_application(ResourceGroupName: str) -> Dict[str, Any]:
```

### Client().describe_component

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L49)

```python
def describe_component(
    ResourceGroupName: str,
    ComponentName: str,
) -> Dict[str, Any]:
```

### Client().describe_component_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L55)

```python
def describe_component_configuration(
    ResourceGroupName: str,
    ComponentName: str,
) -> Dict[str, Any]:
```

### Client().describe_component_configuration_recommendation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L61)

```python
def describe_component_configuration_recommendation(
    ResourceGroupName: str,
    ComponentName: str,
    Tier: str,
) -> Dict[str, Any]:
```

### Client().describe_observation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L67)

```python
def describe_observation(ObservationId: str) -> Dict[str, Any]:
```

### Client().describe_problem

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L71)

```python
def describe_problem(ProblemId: str) -> Dict[str, Any]:
```

### Client().describe_problem_observations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L75)

```python
def describe_problem_observations(ProblemId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L79)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L89)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L93)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L97)

```python
def list_applications(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_components

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L103)

```python
def list_components(
    ResourceGroupName: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_problems

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L109)

```python
def list_problems(
    ResourceGroupName: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().update_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L120)

```python
def update_application(
    ResourceGroupName: str,
    OpsCenterEnabled: bool = None,
    OpsItemSNSTopicArn: str = None,
    RemoveSNSTopic: bool = None,
) -> Dict[str, Any]:
```

### Client().update_component

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L130)

```python
def update_component(
    ResourceGroupName: str,
    ComponentName: str,
    NewComponentName: str = None,
    ResourceList: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_component_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_insights/client.py#L140)

```python
def update_component_configuration(
    ResourceGroupName: str,
    ComponentName: str,
    Monitor: bool = None,
    Tier: str = None,
    ComponentConfiguration: str = None,
) -> Dict[str, Any]:
```
