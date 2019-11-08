# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sns.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sns](index.md#sns) / Client
    - [Client](#client)
        - [Client().add_permission](#clientadd_permission)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().check_if_phone_number_is_opted_out](#clientcheck_if_phone_number_is_opted_out)
        - [Client().confirm_subscription](#clientconfirm_subscription)
        - [Client().create_platform_application](#clientcreate_platform_application)
        - [Client().create_platform_endpoint](#clientcreate_platform_endpoint)
        - [Client().create_topic](#clientcreate_topic)
        - [Client().delete_endpoint](#clientdelete_endpoint)
        - [Client().delete_platform_application](#clientdelete_platform_application)
        - [Client().delete_topic](#clientdelete_topic)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_endpoint_attributes](#clientget_endpoint_attributes)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_platform_application_attributes](#clientget_platform_application_attributes)
        - [Client().get_sms_attributes](#clientget_sms_attributes)
        - [Client().get_subscription_attributes](#clientget_subscription_attributes)
        - [Client().get_topic_attributes](#clientget_topic_attributes)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_endpoints_by_platform_application](#clientlist_endpoints_by_platform_application)
        - [Client().list_phone_numbers_opted_out](#clientlist_phone_numbers_opted_out)
        - [Client().list_platform_applications](#clientlist_platform_applications)
        - [Client().list_subscriptions](#clientlist_subscriptions)
        - [Client().list_subscriptions_by_topic](#clientlist_subscriptions_by_topic)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_topics](#clientlist_topics)
        - [Client().opt_in_phone_number](#clientopt_in_phone_number)
        - [Client().publish](#clientpublish)
        - [Client().remove_permission](#clientremove_permission)
        - [Client().set_endpoint_attributes](#clientset_endpoint_attributes)
        - [Client().set_platform_application_attributes](#clientset_platform_application_attributes)
        - [Client().set_sms_attributes](#clientset_sms_attributes)
        - [Client().set_subscription_attributes](#clientset_subscription_attributes)
        - [Client().set_topic_attributes](#clientset_topic_attributes)
        - [Client().subscribe](#clientsubscribe)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().unsubscribe](#clientunsubscribe)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L15)

```python
def add_permission(
    TopicArn: str,
    Label: str,
    AWSAccountId: List[Any],
    ActionName: List[Any],
) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L21)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().check_if_phone_number_is_opted_out

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L25)

```python
def check_if_phone_number_is_opted_out(phoneNumber: str) -> Dict[str, Any]:
```

### Client().confirm_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L29)

```python
def confirm_subscription(
    TopicArn: str,
    Token: str,
    AuthenticateOnUnsubscribe: str = None,
) -> Dict[str, Any]:
```

### Client().create_platform_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L35)

```python
def create_platform_application(
    Name: str,
    Platform: str,
    Attributes: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_platform_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L41)

```python
def create_platform_endpoint(
    PlatformApplicationArn: str,
    Token: str,
    CustomUserData: str = None,
    Attributes: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_topic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L51)

```python
def create_topic(
    Name: str,
    Attributes: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L57)

```python
def delete_endpoint(EndpointArn: str) -> None:
```

### Client().delete_platform_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L61)

```python
def delete_platform_application(PlatformApplicationArn: str) -> None:
```

### Client().delete_topic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L65)

```python
def delete_topic(TopicArn: str) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L69)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_endpoint_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L79)

```python
def get_endpoint_attributes(EndpointArn: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L83)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_platform_application_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L87)

```python
def get_platform_application_attributes(
    PlatformApplicationArn: str,
) -> Dict[str, Any]:
```

### Client().get_sms_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L93)

```python
def get_sms_attributes(attributes: List[Any] = None) -> Dict[str, Any]:
```

### Client().get_subscription_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L97)

```python
def get_subscription_attributes(SubscriptionArn: str) -> Dict[str, Any]:
```

### Client().get_topic_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L101)

```python
def get_topic_attributes(TopicArn: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L105)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_endpoints_by_platform_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L109)

```python
def list_endpoints_by_platform_application(
    PlatformApplicationArn: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_phone_numbers_opted_out

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L115)

```python
def list_phone_numbers_opted_out(nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_platform_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L119)

```python
def list_platform_applications(NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_subscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L123)

```python
def list_subscriptions(NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_subscriptions_by_topic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L127)

```python
def list_subscriptions_by_topic(
    TopicArn: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L133)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().list_topics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L137)

```python
def list_topics(NextToken: str = None) -> Dict[str, Any]:
```

### Client().opt_in_phone_number

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L141)

```python
def opt_in_phone_number(phoneNumber: str) -> Dict[str, Any]:
```

### Client().publish

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L145)

```python
def publish(
    Message: str,
    TopicArn: str = None,
    TargetArn: str = None,
    PhoneNumber: str = None,
    Subject: str = None,
    MessageStructure: str = None,
    MessageAttributes: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().remove_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L158)

```python
def remove_permission(TopicArn: str, Label: str) -> None:
```

### Client().set_endpoint_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L162)

```python
def set_endpoint_attributes(
    EndpointArn: str,
    Attributes: Dict[str, Any],
) -> None:
```

### Client().set_platform_application_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L168)

```python
def set_platform_application_attributes(
    PlatformApplicationArn: str,
    Attributes: Dict[str, Any],
) -> None:
```

### Client().set_sms_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L174)

```python
def set_sms_attributes(attributes: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().set_subscription_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L178)

```python
def set_subscription_attributes(
    SubscriptionArn: str,
    AttributeName: str,
    AttributeValue: str = None,
) -> None:
```

### Client().set_topic_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L184)

```python
def set_topic_attributes(
    TopicArn: str,
    AttributeName: str,
    AttributeValue: str = None,
) -> None:
```

### Client().subscribe

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L190)

```python
def subscribe(
    TopicArn: str,
    Protocol: str,
    Endpoint: str = None,
    Attributes: Dict[str, Any] = None,
    ReturnSubscriptionArn: bool = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L201)

```python
def tag_resource(ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().unsubscribe

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L205)

```python
def unsubscribe(SubscriptionArn: str) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/client.py#L209)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```
