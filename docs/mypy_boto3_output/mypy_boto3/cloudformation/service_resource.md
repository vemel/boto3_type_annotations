# ServiceResource

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudformation.service_resource](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudformation](index.md#cloudformation) / ServiceResource
    - [Event](#event)
        - [Event().get_available_subresources](#eventget_available_subresources)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().Event](#serviceresourceevent)
        - [ServiceResource().Stack](#serviceresourcestack)
        - [ServiceResource().StackResource](#serviceresourcestackresource)
        - [ServiceResource().StackResourceSummary](#serviceresourcestackresourcesummary)
        - [ServiceResource().create_stack](#serviceresourcecreate_stack)
        - [ServiceResource().get_available_subresources](#serviceresourceget_available_subresources)
    - [Stack](#stack)
        - [Stack().cancel_update](#stackcancel_update)
        - [Stack().delete](#stackdelete)
        - [Stack().get_available_subresources](#stackget_available_subresources)
        - [Stack().load](#stackload)
        - [Stack().reload](#stackreload)
        - [Stack().update](#stackupdate)
    - [StackResource](#stackresource)
        - [StackResource().get_available_subresources](#stackresourceget_available_subresources)
        - [StackResource().load](#stackresourceload)
        - [StackResource().reload](#stackresourcereload)
    - [StackResourceSummary](#stackresourcesummary)
        - [StackResourceSummary().get_available_subresources](#stackresourcesummaryget_available_subresources)
    - [events](#events)
        - [events.all](#eventsall)
        - [events.filter](#eventsfilter)
        - [events.iterator](#eventsiterator)
        - [events.limit](#eventslimit)
        - [events.page_size](#eventspage_size)
        - [events.pages](#eventspages)
    - [resource_summaries](#resource_summaries)
        - [resource_summaries.all](#resource_summariesall)
        - [resource_summaries.filter](#resource_summariesfilter)
        - [resource_summaries.iterator](#resource_summariesiterator)
        - [resource_summaries.limit](#resource_summarieslimit)
        - [resource_summaries.page_size](#resource_summariespage_size)
        - [resource_summaries.pages](#resource_summariespages)
    - [stacks](#stacks)
        - [stacks.all](#stacksall)
        - [stacks.filter](#stacksfilter)
        - [stacks.iterator](#stacksiterator)
        - [stacks.limit](#stackslimit)
        - [stacks.page_size](#stackspage_size)
        - [stacks.pages](#stackspages)

## Event

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L66)

```python
class Event(Boto3ServiceResource):
```

### Event().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L81)

```python
def get_available_subresources() -> List[str]:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L15)

```python
class ServiceResource(Boto3ServiceResource):
```

### ServiceResource().Event

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L19)

```python
def Event(id: str = None) -> cloudformation_service_resource_scope.Event:
```

### ServiceResource().Stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L23)

```python
def Stack(name: str = None) -> cloudformation_service_resource_scope.Stack:
```

### ServiceResource().StackResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L27)

```python
def StackResource(
    stack_name: str = None,
    logical_id: str = None,
) -> cloudformation_service_resource_scope.StackResource:
```

### ServiceResource().StackResourceSummary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L33)

```python
def StackResourceSummary(
    stack_name: str = None,
    logical_id: str = None,
) -> cloudformation_service_resource_scope.StackResourceSummary:
```

### ServiceResource().create_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L39)

```python
def create_stack(
    StackName: str,
    TemplateBody: str = None,
    TemplateURL: str = None,
    Parameters: List[Any] = None,
    DisableRollback: bool = None,
    RollbackConfiguration: Dict[str, Any] = None,
    TimeoutInMinutes: int = None,
    NotificationARNs: List[Any] = None,
    Capabilities: List[Any] = None,
    ResourceTypes: List[Any] = None,
    RoleARN: str = None,
    OnFailure: str = None,
    StackPolicyBody: str = None,
    StackPolicyURL: str = None,
    Tags: List[Any] = None,
    ClientRequestToken: str = None,
    EnableTerminationProtection: bool = None,
) -> cloudformation_service_resource_scope.Stack:
```

### ServiceResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L62)

```python
def get_available_subresources() -> List[str]:
```

## Stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L85)

```python
class Stack(Boto3ServiceResource):
```

### Stack().cancel_update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L113)

```python
def cancel_update(ClientRequestToken: str = None) -> None:
```

### Stack().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L117)

```python
def delete(
    RetainResources: List[Any] = None,
    RoleARN: str = None,
    ClientRequestToken: str = None,
) -> None:
```

### Stack().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L126)

```python
def get_available_subresources() -> List[str]:
```

### Stack().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L130)

```python
def load() -> None:
```

### Stack().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L134)

```python
def reload() -> None:
```

### Stack().update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L138)

```python
def update(
    TemplateBody: str = None,
    TemplateURL: str = None,
    UsePreviousTemplate: bool = None,
    StackPolicyDuringUpdateBody: str = None,
    StackPolicyDuringUpdateURL: str = None,
    Parameters: List[Any] = None,
    Capabilities: List[Any] = None,
    ResourceTypes: List[Any] = None,
    RoleARN: str = None,
    RollbackConfiguration: Dict[str, Any] = None,
    StackPolicyBody: str = None,
    StackPolicyURL: str = None,
    NotificationARNs: List[Any] = None,
    Tags: List[Any] = None,
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

## StackResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L159)

```python
class StackResource(Boto3ServiceResource):
```

### StackResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L174)

```python
def get_available_subresources() -> List[str]:
```

### StackResource().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L178)

```python
def load() -> None:
```

### StackResource().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L182)

```python
def reload() -> None:
```

## StackResourceSummary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L186)

```python
class StackResourceSummary(Boto3ServiceResource):
```

### StackResourceSummary().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L198)

```python
def get_available_subresources() -> List[str]:
```

## events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L240)

```python
class events(ResourceCollection):
```

### events.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L241)

```python
@classmethod
def all() -> List[cloudformation_service_resource_scope.Event]:
```

### events.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L246)

```python
@classmethod
def filter(
    NextToken: str = None,
) -> List[cloudformation_service_resource_scope.Event]:
```

### events.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L253)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### events.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L258)

```python
@classmethod
def limit(
    count: int = None,
) -> List[cloudformation_service_resource_scope.Event]:
```

### events.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L265)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[cloudformation_service_resource_scope.Event]:
```

### events.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L272)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## resource_summaries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L278)

```python
class resource_summaries(ResourceCollection):
```

### resource_summaries.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L279)

```python
@classmethod
def all() -> List[cloudformation_service_resource_scope.StackResourceSummary]:
```

### resource_summaries.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L284)

```python
@classmethod
def filter(
    NextToken: str = None,
) -> List[cloudformation_service_resource_scope.StackResourceSummary]:
```

### resource_summaries.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L291)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### resource_summaries.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L296)

```python
@classmethod
def limit(
    count: int = None,
) -> List[cloudformation_service_resource_scope.StackResourceSummary]:
```

### resource_summaries.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L303)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[cloudformation_service_resource_scope.StackResourceSummary]:
```

### resource_summaries.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L310)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## stacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L202)

```python
class stacks(ResourceCollection):
```

### stacks.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L203)

```python
@classmethod
def all() -> List[cloudformation_service_resource_scope.Stack]:
```

### stacks.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L208)

```python
@classmethod
def filter(
    StackName: str = None,
    NextToken: str = None,
) -> List[cloudformation_service_resource_scope.Stack]:
```

### stacks.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L215)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### stacks.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L220)

```python
@classmethod
def limit(
    count: int = None,
) -> List[cloudformation_service_resource_scope.Stack]:
```

### stacks.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L227)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[cloudformation_service_resource_scope.Stack]:
```

### stacks.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/service_resource.py#L234)

```python
@classmethod
def pages() -> List[ServiceResource]:
```
