# ServiceResource

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sns.service_resource](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sns](index.md#sns) / ServiceResource
    - [PlatformApplication](#platformapplication)
        - [PlatformApplication().create_platform_endpoint](#platformapplicationcreate_platform_endpoint)
        - [PlatformApplication().delete](#platformapplicationdelete)
        - [PlatformApplication().get_available_subresources](#platformapplicationget_available_subresources)
        - [PlatformApplication().load](#platformapplicationload)
        - [PlatformApplication().reload](#platformapplicationreload)
        - [PlatformApplication().set_attributes](#platformapplicationset_attributes)
    - [PlatformEndpoint](#platformendpoint)
        - [PlatformEndpoint().delete](#platformendpointdelete)
        - [PlatformEndpoint().get_available_subresources](#platformendpointget_available_subresources)
        - [PlatformEndpoint().load](#platformendpointload)
        - [PlatformEndpoint().publish](#platformendpointpublish)
        - [PlatformEndpoint().reload](#platformendpointreload)
        - [PlatformEndpoint().set_attributes](#platformendpointset_attributes)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().PlatformApplication](#serviceresourceplatformapplication)
        - [ServiceResource().PlatformEndpoint](#serviceresourceplatformendpoint)
        - [ServiceResource().Subscription](#serviceresourcesubscription)
        - [ServiceResource().Topic](#serviceresourcetopic)
        - [ServiceResource().create_platform_application](#serviceresourcecreate_platform_application)
        - [ServiceResource().create_topic](#serviceresourcecreate_topic)
        - [ServiceResource().get_available_subresources](#serviceresourceget_available_subresources)
    - [Subscription](#subscription)
        - [Subscription().delete](#subscriptiondelete)
        - [Subscription().get_available_subresources](#subscriptionget_available_subresources)
        - [Subscription().load](#subscriptionload)
        - [Subscription().reload](#subscriptionreload)
        - [Subscription().set_attributes](#subscriptionset_attributes)
    - [Topic](#topic)
        - [Topic().add_permission](#topicadd_permission)
        - [Topic().confirm_subscription](#topicconfirm_subscription)
        - [Topic().delete](#topicdelete)
        - [Topic().get_available_subresources](#topicget_available_subresources)
        - [Topic().load](#topicload)
        - [Topic().publish](#topicpublish)
        - [Topic().reload](#topicreload)
        - [Topic().remove_permission](#topicremove_permission)
        - [Topic().set_attributes](#topicset_attributes)
        - [Topic().subscribe](#topicsubscribe)
    - [endpoints](#endpoints)
        - [endpoints.all](#endpointsall)
        - [endpoints.filter](#endpointsfilter)
        - [endpoints.iterator](#endpointsiterator)
        - [endpoints.limit](#endpointslimit)
        - [endpoints.page_size](#endpointspage_size)
        - [endpoints.pages](#endpointspages)
    - [platform_applications](#platform_applications)
        - [platform_applications.all](#platform_applicationsall)
        - [platform_applications.filter](#platform_applicationsfilter)
        - [platform_applications.iterator](#platform_applicationsiterator)
        - [platform_applications.limit](#platform_applicationslimit)
        - [platform_applications.page_size](#platform_applicationspage_size)
        - [platform_applications.pages](#platform_applicationspages)
    - [subscriptions](#subscriptions)
        - [subscriptions.all](#subscriptionsall)
        - [subscriptions.filter](#subscriptionsfilter)
        - [subscriptions.iterator](#subscriptionsiterator)
        - [subscriptions.limit](#subscriptionslimit)
        - [subscriptions.page_size](#subscriptionspage_size)
        - [subscriptions.pages](#subscriptionspages)
    - [topics](#topics)
        - [topics.all](#topicsall)
        - [topics.filter](#topicsfilter)
        - [topics.iterator](#topicsiterator)
        - [topics.limit](#topicslimit)
        - [topics.page_size](#topicspage_size)
        - [topics.pages](#topicspages)

## PlatformApplication

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L56)

```python
class PlatformApplication(Boto3ServiceResource):
```

### PlatformApplication().create_platform_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L62)

```python
def create_platform_endpoint(
    Token: str,
    CustomUserData: str = None,
    Attributes: Dict[str, Any] = None,
) -> sns_service_resource_scope.PlatformEndpoint:
```

### PlatformApplication().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L68)

```python
def delete() -> None:
```

### PlatformApplication().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L72)

```python
def get_available_subresources() -> List[str]:
```

### PlatformApplication().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L76)

```python
def load() -> None:
```

### PlatformApplication().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L80)

```python
def reload() -> None:
```

### PlatformApplication().set_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L84)

```python
def set_attributes(Attributes: Dict[str, Any]) -> None:
```

## PlatformEndpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L88)

```python
class PlatformEndpoint(Boto3ServiceResource):
```

### PlatformEndpoint().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L93)

```python
def delete() -> None:
```

### PlatformEndpoint().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L97)

```python
def get_available_subresources() -> List[str]:
```

### PlatformEndpoint().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L101)

```python
def load() -> None:
```

### PlatformEndpoint().publish

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L105)

```python
def publish(
    Message: str,
    TopicArn: str = None,
    PhoneNumber: str = None,
    Subject: str = None,
    MessageStructure: str = None,
    MessageAttributes: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### PlatformEndpoint().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L117)

```python
def reload() -> None:
```

### PlatformEndpoint().set_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L121)

```python
def set_attributes(Attributes: Dict[str, Any]) -> None:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L14)

```python
class ServiceResource(Boto3ServiceResource):
```

### ServiceResource().PlatformApplication

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L20)

```python
def PlatformApplication(
    arn: str = None,
) -> sns_service_resource_scope.PlatformApplication:
```

### ServiceResource().PlatformEndpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L26)

```python
def PlatformEndpoint(
    arn: str = None,
) -> sns_service_resource_scope.PlatformEndpoint:
```

### ServiceResource().Subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L32)

```python
def Subscription(arn: str = None) -> sns_service_resource_scope.Subscription:
```

### ServiceResource().Topic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L36)

```python
def Topic(arn: str = None) -> sns_service_resource_scope.Topic:
```

### ServiceResource().create_platform_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L40)

```python
def create_platform_application(
    Name: str,
    Platform: str,
    Attributes: Dict[str, Any],
) -> sns_service_resource_scope.PlatformApplication:
```

### ServiceResource().create_topic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L46)

```python
def create_topic(
    Name: str,
    Attributes: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> sns_service_resource_scope.Topic:
```

### ServiceResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L52)

```python
def get_available_subresources() -> List[str]:
```

## Subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L125)

```python
class Subscription(Boto3ServiceResource):
```

### Subscription().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L130)

```python
def delete() -> None:
```

### Subscription().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L134)

```python
def get_available_subresources() -> List[str]:
```

### Subscription().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L138)

```python
def load() -> None:
```

### Subscription().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L142)

```python
def reload() -> None:
```

### Subscription().set_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L146)

```python
def set_attributes(AttributeName: str, AttributeValue: str = None) -> None:
```

## Topic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L150)

```python
class Topic(Boto3ServiceResource):
```

### Topic().add_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L156)

```python
def add_permission(
    Label: str,
    AWSAccountId: List[Any],
    ActionName: List[Any],
) -> None:
```

### Topic().confirm_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L162)

```python
def confirm_subscription(
    Token: str,
    AuthenticateOnUnsubscribe: str = None,
) -> sns_service_resource_scope.Subscription:
```

### Topic().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L168)

```python
def delete() -> None:
```

### Topic().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L172)

```python
def get_available_subresources() -> List[str]:
```

### Topic().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L176)

```python
def load() -> None:
```

### Topic().publish

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L180)

```python
def publish(
    Message: str,
    TargetArn: str = None,
    PhoneNumber: str = None,
    Subject: str = None,
    MessageStructure: str = None,
    MessageAttributes: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Topic().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L192)

```python
def reload() -> None:
```

### Topic().remove_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L196)

```python
def remove_permission(Label: str) -> None:
```

### Topic().set_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L200)

```python
def set_attributes(AttributeName: str, AttributeValue: str = None) -> None:
```

### Topic().subscribe

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L204)

```python
def subscribe(
    Protocol: str,
    Endpoint: str = None,
    Attributes: Dict[str, Any] = None,
    ReturnSubscriptionArn: bool = None,
) -> sns_service_resource_scope.Subscription:
```

## endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L320)

```python
class endpoints(ResourceCollection):
```

### endpoints.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L321)

```python
@classmethod
def all() -> List[sns_service_resource_scope.PlatformEndpoint]:
```

### endpoints.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L326)

```python
@classmethod
def filter(
    NextToken: str = None,
) -> List[sns_service_resource_scope.PlatformEndpoint]:
```

### endpoints.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L333)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### endpoints.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L338)

```python
@classmethod
def limit(
    count: int = None,
) -> List[sns_service_resource_scope.PlatformEndpoint]:
```

### endpoints.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L345)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[sns_service_resource_scope.PlatformEndpoint]:
```

### endpoints.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L352)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## platform_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L214)

```python
class platform_applications(ResourceCollection):
```

### platform_applications.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L215)

```python
@classmethod
def all() -> List[sns_service_resource_scope.PlatformApplication]:
```

### platform_applications.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L220)

```python
@classmethod
def filter(
    NextToken: str = None,
) -> List[sns_service_resource_scope.PlatformApplication]:
```

### platform_applications.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L227)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### platform_applications.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L232)

```python
@classmethod
def limit(
    count: int = None,
) -> List[sns_service_resource_scope.PlatformApplication]:
```

### platform_applications.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L239)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[sns_service_resource_scope.PlatformApplication]:
```

### platform_applications.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L246)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## subscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L252)

```python
class subscriptions(ResourceCollection):
```

### subscriptions.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L253)

```python
@classmethod
def all() -> List[sns_service_resource_scope.Subscription]:
```

### subscriptions.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L258)

```python
@classmethod
def filter(
    NextToken: str = None,
) -> List[sns_service_resource_scope.Subscription]:
```

### subscriptions.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L265)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### subscriptions.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L270)

```python
@classmethod
def limit(count: int = None) -> List[sns_service_resource_scope.Subscription]:
```

### subscriptions.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L275)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[sns_service_resource_scope.Subscription]:
```

### subscriptions.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L282)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## topics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L288)

```python
class topics(ResourceCollection):
```

### topics.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L289)

```python
@classmethod
def all() -> List[sns_service_resource_scope.Topic]:
```

### topics.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L294)

```python
@classmethod
def filter(NextToken: str = None) -> List[sns_service_resource_scope.Topic]:
```

### topics.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L299)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### topics.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L304)

```python
@classmethod
def limit(count: int = None) -> List[sns_service_resource_scope.Topic]:
```

### topics.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L309)

```python
@classmethod
def page_size(count: int = None) -> List[sns_service_resource_scope.Topic]:
```

### topics.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/service_resource.py#L314)

```python
@classmethod
def pages() -> List[ServiceResource]:
```
