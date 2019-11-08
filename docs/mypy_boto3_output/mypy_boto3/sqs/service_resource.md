# ServiceResource

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sqs.service_resource](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sqs](index.md#sqs) / ServiceResource
    - [Message](#message)
        - [Message().change_visibility](#messagechange_visibility)
        - [Message().delete](#messagedelete)
        - [Message().get_available_subresources](#messageget_available_subresources)
    - [Queue](#queue)
        - [Queue().add_permission](#queueadd_permission)
        - [Queue().change_message_visibility_batch](#queuechange_message_visibility_batch)
        - [Queue().delete](#queuedelete)
        - [Queue().delete_messages](#queuedelete_messages)
        - [Queue().get_available_subresources](#queueget_available_subresources)
        - [Queue().load](#queueload)
        - [Queue().purge](#queuepurge)
        - [Queue().receive_messages](#queuereceive_messages)
        - [Queue().reload](#queuereload)
        - [Queue().remove_permission](#queueremove_permission)
        - [Queue().send_message](#queuesend_message)
        - [Queue().send_messages](#queuesend_messages)
        - [Queue().set_attributes](#queueset_attributes)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().Message](#serviceresourcemessage)
        - [ServiceResource().Queue](#serviceresourcequeue)
        - [ServiceResource().create_queue](#serviceresourcecreate_queue)
        - [ServiceResource().get_available_subresources](#serviceresourceget_available_subresources)
        - [ServiceResource().get_queue_by_name](#serviceresourceget_queue_by_name)
    - [dead_letter_source_queues](#dead_letter_source_queues)
        - [dead_letter_source_queues.all](#dead_letter_source_queuesall)
        - [dead_letter_source_queues.filter](#dead_letter_source_queuesfilter)
        - [dead_letter_source_queues.iterator](#dead_letter_source_queuesiterator)
        - [dead_letter_source_queues.limit](#dead_letter_source_queueslimit)
        - [dead_letter_source_queues.page_size](#dead_letter_source_queuespage_size)
        - [dead_letter_source_queues.pages](#dead_letter_source_queuespages)
    - [queues](#queues)
        - [queues.all](#queuesall)
        - [queues.filter](#queuesfilter)
        - [queues.iterator](#queuesiterator)
        - [queues.limit](#queueslimit)
        - [queues.page_size](#queuespage_size)
        - [queues.pages](#queuespages)

## Message

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L47)

```python
class Message(Boto3ServiceResource):
```

### Message().change_visibility

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L58)

```python
def change_visibility(VisibilityTimeout: int) -> None:
```

### Message().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L62)

```python
def delete() -> None:
```

### Message().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L66)

```python
def get_available_subresources() -> List[str]:
```

## Queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L70)

```python
class Queue(Boto3ServiceResource):
```

### Queue().add_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L76)

```python
def add_permission(
    Label: str,
    AWSAccountIds: List[Any],
    Actions: List[Any],
) -> None:
```

### Queue().change_message_visibility_batch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L82)

```python
def change_message_visibility_batch(Entries: List[Any]) -> Dict[str, Any]:
```

### Queue().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L86)

```python
def delete() -> None:
```

### Queue().delete_messages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L90)

```python
def delete_messages(Entries: List[Any]) -> Dict[str, Any]:
```

### Queue().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L94)

```python
def get_available_subresources() -> List[str]:
```

### Queue().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L98)

```python
def load() -> None:
```

### Queue().purge

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L102)

```python
def purge() -> None:
```

### Queue().receive_messages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L106)

```python
def receive_messages(
    AttributeNames: List[Any] = None,
    MessageAttributeNames: List[Any] = None,
    MaxNumberOfMessages: int = None,
    VisibilityTimeout: int = None,
    WaitTimeSeconds: int = None,
    ReceiveRequestAttemptId: str = None,
) -> List[sqs_service_resource_scope.Message]:
```

### Queue().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L118)

```python
def reload() -> None:
```

### Queue().remove_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L122)

```python
def remove_permission(Label: str) -> None:
```

### Queue().send_message

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L126)

```python
def send_message(
    MessageBody: str,
    DelaySeconds: int = None,
    MessageAttributes: Dict[str, Any] = None,
    MessageSystemAttributes: Dict[str, Any] = None,
    MessageDeduplicationId: str = None,
    MessageGroupId: str = None,
) -> Dict[str, Any]:
```

### Queue().send_messages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L138)

```python
def send_messages(Entries: List[Any]) -> Dict[str, Any]:
```

### Queue().set_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L142)

```python
def set_attributes(Attributes: Dict[str, Any]) -> None:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L14)

```python
class ServiceResource(Boto3ServiceResource):
```

### ServiceResource().Message

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L18)

```python
def Message(
    queue_url: str = None,
    receipt_handle: str = None,
) -> sqs_service_resource_scope.Message:
```

### ServiceResource().Queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L24)

```python
def Queue(url: str = None) -> sqs_service_resource_scope.Queue:
```

### ServiceResource().create_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L28)

```python
def create_queue(
    QueueName: str,
    Attributes: Dict[str, Any] = None,
    tags: Dict[str, Any] = None,
) -> sqs_service_resource_scope.Queue:
```

### ServiceResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L37)

```python
def get_available_subresources() -> List[str]:
```

### ServiceResource().get_queue_by_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L41)

```python
def get_queue_by_name(
    QueueName: str,
    QueueOwnerAWSAccountId: str = None,
) -> sqs_service_resource_scope.Queue:
```

## dead_letter_source_queues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L180)

```python
class dead_letter_source_queues(ResourceCollection):
```

### dead_letter_source_queues.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L181)

```python
@classmethod
def all() -> List[sqs_service_resource_scope.Queue]:
```

### dead_letter_source_queues.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L186)

```python
@classmethod
def filter() -> List[sqs_service_resource_scope.Queue]:
```

### dead_letter_source_queues.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L191)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### dead_letter_source_queues.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L196)

```python
@classmethod
def limit(count: int = None) -> List[sqs_service_resource_scope.Queue]:
```

### dead_letter_source_queues.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L201)

```python
@classmethod
def page_size(count: int = None) -> List[sqs_service_resource_scope.Queue]:
```

### dead_letter_source_queues.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L206)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## queues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L146)

```python
class queues(ResourceCollection):
```

### queues.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L147)

```python
@classmethod
def all() -> List[sqs_service_resource_scope.Queue]:
```

### queues.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L152)

```python
@classmethod
def filter(
    QueueNamePrefix: str = None,
) -> List[sqs_service_resource_scope.Queue]:
```

### queues.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L159)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### queues.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L164)

```python
@classmethod
def limit(count: int = None) -> List[sqs_service_resource_scope.Queue]:
```

### queues.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L169)

```python
@classmethod
def page_size(count: int = None) -> List[sqs_service_resource_scope.Queue]:
```

### queues.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/service_resource.py#L174)

```python
@classmethod
def pages() -> List[ServiceResource]:
```
