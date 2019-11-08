# ServiceResource

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.opsworks.service_resource](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Opsworks](index.md#opsworks) / ServiceResource
    - [Layer](#layer)
        - [Layer().delete](#layerdelete)
        - [Layer().get_available_subresources](#layerget_available_subresources)
        - [Layer().load](#layerload)
        - [Layer().reload](#layerreload)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().Layer](#serviceresourcelayer)
        - [ServiceResource().Stack](#serviceresourcestack)
        - [ServiceResource().StackSummary](#serviceresourcestacksummary)
        - [ServiceResource().create_stack](#serviceresourcecreate_stack)
        - [ServiceResource().get_available_subresources](#serviceresourceget_available_subresources)
    - [Stack](#stack)
        - [Stack().create_layer](#stackcreate_layer)
        - [Stack().delete](#stackdelete)
        - [Stack().get_available_subresources](#stackget_available_subresources)
        - [Stack().load](#stackload)
        - [Stack().reload](#stackreload)
    - [StackSummary](#stacksummary)
        - [StackSummary().get_available_subresources](#stacksummaryget_available_subresources)
        - [StackSummary().load](#stacksummaryload)
        - [StackSummary().reload](#stacksummaryreload)
    - [layers](#layers)
        - [layers.all](#layersall)
        - [layers.filter](#layersfilter)
        - [layers.iterator](#layersiterator)
        - [layers.limit](#layerslimit)
        - [layers.page_size](#layerspage_size)
        - [layers.pages](#layerspages)
    - [stacks](#stacks)
        - [stacks.all](#stacksall)
        - [stacks.filter](#stacksfilter)
        - [stacks.iterator](#stacksiterator)
        - [stacks.limit](#stackslimit)
        - [stacks.page_size](#stackspage_size)
        - [stacks.pages](#stackspages)

## Layer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L61)

```python
class Layer(Boto3ServiceResource):
```

### Layer().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L88)

```python
def delete() -> None:
```

### Layer().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L92)

```python
def get_available_subresources() -> List[str]:
```

### Layer().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L96)

```python
def load() -> None:
```

### Layer().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L100)

```python
def reload() -> None:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L14)

```python
class ServiceResource(Boto3ServiceResource):
```

### ServiceResource().Layer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L18)

```python
def Layer(id: str = None) -> opsworks_service_resource_scope.Layer:
```

### ServiceResource().Stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L22)

```python
def Stack(id: str = None) -> opsworks_service_resource_scope.Stack:
```

### ServiceResource().StackSummary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L26)

```python
def StackSummary(
    stack_id: str = None,
) -> opsworks_service_resource_scope.StackSummary:
```

### ServiceResource().create_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L32)

```python
def create_stack(
    Name: str,
    Region: str,
    ServiceRoleArn: str,
    DefaultInstanceProfileArn: str,
    VpcId: str = None,
    Attributes: Dict[str, Any] = None,
    DefaultOs: str = None,
    HostnameTheme: str = None,
    DefaultAvailabilityZone: str = None,
    DefaultSubnetId: str = None,
    CustomJson: str = None,
    ConfigurationManager: Dict[str, Any] = None,
    ChefConfiguration: Dict[str, Any] = None,
    UseCustomCookbooks: bool = None,
    UseOpsworksSecurityGroups: bool = None,
    CustomCookbooksSource: Dict[str, Any] = None,
    DefaultSshKeyName: str = None,
    DefaultRootDeviceType: str = None,
    AgentVersion: str = None,
) -> opsworks_service_resource_scope.Stack:
```

### ServiceResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L57)

```python
def get_available_subresources() -> List[str]:
```

## Stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L104)

```python
class Stack(Boto3ServiceResource):
```

### Stack().create_layer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L131)

```python
def create_layer(
    Type: str,
    Name: str,
    Shortname: str,
    Attributes: Dict[str, Any] = None,
    CloudWatchLogsConfiguration: Dict[str, Any] = None,
    CustomInstanceProfileArn: str = None,
    CustomJson: str = None,
    CustomSecurityGroupIds: List[Any] = None,
    Packages: List[Any] = None,
    VolumeConfigurations: List[Any] = None,
    EnableAutoHealing: bool = None,
    AutoAssignElasticIps: bool = None,
    AutoAssignPublicIps: bool = None,
    CustomRecipes: Dict[str, Any] = None,
    InstallUpdatesOnBoot: bool = None,
    UseEbsOptimizedInstances: bool = None,
    LifecycleEventConfiguration: Dict[str, Any] = None,
) -> opsworks_service_resource_scope.Layer:
```

### Stack().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L154)

```python
def delete() -> None:
```

### Stack().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L158)

```python
def get_available_subresources() -> List[str]:
```

### Stack().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L162)

```python
def load() -> None:
```

### Stack().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L166)

```python
def reload() -> None:
```

## StackSummary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L170)

```python
class StackSummary(Boto3ServiceResource):
```

### StackSummary().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L179)

```python
def get_available_subresources() -> List[str]:
```

### StackSummary().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L183)

```python
def load() -> None:
```

### StackSummary().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L187)

```python
def reload() -> None:
```

## layers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L227)

```python
class layers(ResourceCollection):
```

### layers.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L228)

```python
@classmethod
def all() -> List[opsworks_service_resource_scope.Layer]:
```

### layers.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L233)

```python
@classmethod
def filter(
    LayerIds: List[Any] = None,
) -> List[opsworks_service_resource_scope.Layer]:
```

### layers.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L240)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### layers.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L245)

```python
@classmethod
def limit(count: int = None) -> List[opsworks_service_resource_scope.Layer]:
```

### layers.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L250)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[opsworks_service_resource_scope.Layer]:
```

### layers.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L257)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## stacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L191)

```python
class stacks(ResourceCollection):
```

### stacks.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L192)

```python
@classmethod
def all() -> List[opsworks_service_resource_scope.Stack]:
```

### stacks.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L197)

```python
@classmethod
def filter(
    StackIds: List[Any] = None,
) -> List[opsworks_service_resource_scope.Stack]:
```

### stacks.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L204)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### stacks.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L209)

```python
@classmethod
def limit(count: int = None) -> List[opsworks_service_resource_scope.Stack]:
```

### stacks.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L214)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[opsworks_service_resource_scope.Stack]:
```

### stacks.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/service_resource.py#L221)

```python
@classmethod
def pages() -> List[ServiceResource]:
```
