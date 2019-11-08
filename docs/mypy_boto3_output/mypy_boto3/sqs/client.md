# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sqs.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sqs](index.md#sqs) / Client
    - [Client](#client)
        - [Client().add_permission](#clientadd_permission)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().change_message_visibility](#clientchange_message_visibility)
        - [Client().change_message_visibility_batch](#clientchange_message_visibility_batch)
        - [Client().create_queue](#clientcreate_queue)
        - [Client().delete_message](#clientdelete_message)
        - [Client().delete_message_batch](#clientdelete_message_batch)
        - [Client().delete_queue](#clientdelete_queue)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_queue_attributes](#clientget_queue_attributes)
        - [Client().get_queue_url](#clientget_queue_url)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_dead_letter_source_queues](#clientlist_dead_letter_source_queues)
        - [Client().list_queue_tags](#clientlist_queue_tags)
        - [Client().list_queues](#clientlist_queues)
        - [Client().purge_queue](#clientpurge_queue)
        - [Client().receive_message](#clientreceive_message)
        - [Client().remove_permission](#clientremove_permission)
        - [Client().send_message](#clientsend_message)
        - [Client().send_message_batch](#clientsend_message_batch)
        - [Client().set_queue_attributes](#clientset_queue_attributes)
        - [Client().tag_queue](#clienttag_queue)
        - [Client().untag_queue](#clientuntag_queue)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L15)

```python
def add_permission(
    QueueUrl: str,
    Label: str,
    AWSAccountIds: List[Any],
    Actions: List[Any],
) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L21)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().change_message_visibility

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L25)

```python
def change_message_visibility(
    QueueUrl: str,
    ReceiptHandle: str,
    VisibilityTimeout: int,
) -> None:
```

### Client().change_message_visibility_batch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L31)

```python
def change_message_visibility_batch(
    QueueUrl: str,
    Entries: List[Any],
) -> Dict[str, Any]:
```

### Client().create_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L37)

```python
def create_queue(
    QueueName: str,
    Attributes: Dict[str, Any] = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_message

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L46)

```python
def delete_message(QueueUrl: str, ReceiptHandle: str) -> None:
```

### Client().delete_message_batch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L50)

```python
def delete_message_batch(QueueUrl: str, Entries: List[Any]) -> Dict[str, Any]:
```

### Client().delete_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L54)

```python
def delete_queue(QueueUrl: str) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L58)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L68)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_queue_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L72)

```python
def get_queue_attributes(
    QueueUrl: str,
    AttributeNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_queue_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L78)

```python
def get_queue_url(
    QueueName: str,
    QueueOwnerAWSAccountId: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L84)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_dead_letter_source_queues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L88)

```python
def list_dead_letter_source_queues(QueueUrl: str) -> Dict[str, Any]:
```

### Client().list_queue_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L92)

```python
def list_queue_tags(QueueUrl: str) -> Dict[str, Any]:
```

### Client().list_queues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L96)

```python
def list_queues(QueueNamePrefix: str = None) -> Dict[str, Any]:
```

### Client().purge_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L100)

```python
def purge_queue(QueueUrl: str) -> None:
```

### Client().receive_message

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L104)

```python
def receive_message(
    QueueUrl: str,
    AttributeNames: List[Any] = None,
    MessageAttributeNames: List[Any] = None,
    MaxNumberOfMessages: int = None,
    VisibilityTimeout: int = None,
    WaitTimeSeconds: int = None,
    ReceiveRequestAttemptId: str = None,
) -> Dict[str, Any]:
```

### Client().remove_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L117)

```python
def remove_permission(QueueUrl: str, Label: str) -> None:
```

### Client().send_message

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L121)

```python
def send_message(
    QueueUrl: str,
    MessageBody: str,
    DelaySeconds: int = None,
    MessageAttributes: Dict[str, Any] = None,
    MessageSystemAttributes: Dict[str, Any] = None,
    MessageDeduplicationId: str = None,
    MessageGroupId: str = None,
) -> Dict[str, Any]:
```

### Client().send_message_batch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L134)

```python
def send_message_batch(QueueUrl: str, Entries: List[Any]) -> Dict[str, Any]:
```

### Client().set_queue_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L138)

```python
def set_queue_attributes(QueueUrl: str, Attributes: Dict[str, Any]) -> None:
```

### Client().tag_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L142)

```python
def tag_queue(QueueUrl: str, Tags: Dict[str, Any]) -> None:
```

### Client().untag_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sqs/client.py#L146)

```python
def untag_queue(QueueUrl: str, TagKeys: List[Any]) -> None:
```
