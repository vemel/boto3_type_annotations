# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mediaconvert.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mediaconvert](index.md#mediaconvert) / Client
    - [Client](#client)
        - [Client().associate_certificate](#clientassociate_certificate)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_job](#clientcancel_job)
        - [Client().create_job](#clientcreate_job)
        - [Client().create_job_template](#clientcreate_job_template)
        - [Client().create_preset](#clientcreate_preset)
        - [Client().create_queue](#clientcreate_queue)
        - [Client().delete_job_template](#clientdelete_job_template)
        - [Client().delete_preset](#clientdelete_preset)
        - [Client().delete_queue](#clientdelete_queue)
        - [Client().describe_endpoints](#clientdescribe_endpoints)
        - [Client().disassociate_certificate](#clientdisassociate_certificate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_job](#clientget_job)
        - [Client().get_job_template](#clientget_job_template)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_preset](#clientget_preset)
        - [Client().get_queue](#clientget_queue)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_job_templates](#clientlist_job_templates)
        - [Client().list_jobs](#clientlist_jobs)
        - [Client().list_presets](#clientlist_presets)
        - [Client().list_queues](#clientlist_queues)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_job_template](#clientupdate_job_template)
        - [Client().update_preset](#clientupdate_preset)
        - [Client().update_queue](#clientupdate_queue)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L15)

```python
def associate_certificate(Arn: str) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L23)

```python
def cancel_job(Id: str) -> Dict[str, Any]:
```

### Client().create_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L27)

```python
def create_job(
    Role: str,
    Settings: Dict[str, Any],
    AccelerationSettings: Dict[str, Any] = None,
    BillingTagsSource: str = None,
    ClientRequestToken: str = None,
    JobTemplate: str = None,
    Priority: int = None,
    Queue: str = None,
    SimulateReservedQueue: str = None,
    StatusUpdateInterval: str = None,
    Tags: Dict[str, Any] = None,
    UserMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_job_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L45)

```python
def create_job_template(
    Name: str,
    Settings: Dict[str, Any],
    AccelerationSettings: Dict[str, Any] = None,
    Category: str = None,
    Description: str = None,
    Priority: int = None,
    Queue: str = None,
    StatusUpdateInterval: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_preset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L60)

```python
def create_preset(
    Name: str,
    Settings: Dict[str, Any],
    Category: str = None,
    Description: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L71)

```python
def create_queue(
    Name: str,
    Description: str = None,
    PricingPlan: str = None,
    ReservationPlanSettings: Dict[str, Any] = None,
    Status: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_job_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L83)

```python
def delete_job_template(Name: str) -> Dict[str, Any]:
```

### Client().delete_preset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L87)

```python
def delete_preset(Name: str) -> Dict[str, Any]:
```

### Client().delete_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L91)

```python
def delete_queue(Name: str) -> Dict[str, Any]:
```

### Client().describe_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L95)

```python
def describe_endpoints(
    MaxResults: int = None,
    Mode: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().disassociate_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L101)

```python
def disassociate_certificate(Arn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L105)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L115)

```python
def get_job(Id: str) -> Dict[str, Any]:
```

### Client().get_job_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L119)

```python
def get_job_template(Name: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L123)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_preset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L127)

```python
def get_preset(Name: str) -> Dict[str, Any]:
```

### Client().get_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L131)

```python
def get_queue(Name: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L135)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_job_templates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L139)

```python
def list_job_templates(
    Category: str = None,
    ListBy: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    Order: str = None,
) -> Dict[str, Any]:
```

### Client().list_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L150)

```python
def list_jobs(
    MaxResults: int = None,
    NextToken: str = None,
    Order: str = None,
    Queue: str = None,
    Status: str = None,
) -> Dict[str, Any]:
```

### Client().list_presets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L161)

```python
def list_presets(
    Category: str = None,
    ListBy: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    Order: str = None,
) -> Dict[str, Any]:
```

### Client().list_queues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L172)

```python
def list_queues(
    ListBy: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    Order: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L182)

```python
def list_tags_for_resource(Arn: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L186)

```python
def tag_resource(Arn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L190)

```python
def untag_resource(Arn: str, TagKeys: List[Any] = None) -> Dict[str, Any]:
```

### Client().update_job_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L194)

```python
def update_job_template(
    Name: str,
    AccelerationSettings: Dict[str, Any] = None,
    Category: str = None,
    Description: str = None,
    Priority: int = None,
    Queue: str = None,
    Settings: Dict[str, Any] = None,
    StatusUpdateInterval: str = None,
) -> Dict[str, Any]:
```

### Client().update_preset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L208)

```python
def update_preset(
    Name: str,
    Category: str = None,
    Description: str = None,
    Settings: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/client.py#L218)

```python
def update_queue(
    Name: str,
    Description: str = None,
    ReservationPlanSettings: Dict[str, Any] = None,
    Status: str = None,
) -> Dict[str, Any]:
```
