# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mturk.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mturk](index.md#mturk) / Client
    - [Client](#client)
        - [Client().accept_qualification_request](#clientaccept_qualification_request)
        - [Client().approve_assignment](#clientapprove_assignment)
        - [Client().associate_qualification_with_worker](#clientassociate_qualification_with_worker)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_additional_assignments_for_hit](#clientcreate_additional_assignments_for_hit)
        - [Client().create_hit](#clientcreate_hit)
        - [Client().create_hit_type](#clientcreate_hit_type)
        - [Client().create_hit_with_hit_type](#clientcreate_hit_with_hit_type)
        - [Client().create_qualification_type](#clientcreate_qualification_type)
        - [Client().create_worker_block](#clientcreate_worker_block)
        - [Client().delete_hit](#clientdelete_hit)
        - [Client().delete_qualification_type](#clientdelete_qualification_type)
        - [Client().delete_worker_block](#clientdelete_worker_block)
        - [Client().disassociate_qualification_from_worker](#clientdisassociate_qualification_from_worker)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_account_balance](#clientget_account_balance)
        - [Client().get_assignment](#clientget_assignment)
        - [Client().get_file_upload_url](#clientget_file_upload_url)
        - [Client().get_hit](#clientget_hit)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_qualification_score](#clientget_qualification_score)
        - [Client().get_qualification_type](#clientget_qualification_type)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_assignments_for_hit](#clientlist_assignments_for_hit)
        - [Client().list_bonus_payments](#clientlist_bonus_payments)
        - [Client().list_hits](#clientlist_hits)
        - [Client().list_hits_for_qualification_type](#clientlist_hits_for_qualification_type)
        - [Client().list_qualification_requests](#clientlist_qualification_requests)
        - [Client().list_qualification_types](#clientlist_qualification_types)
        - [Client().list_review_policy_results_for_hit](#clientlist_review_policy_results_for_hit)
        - [Client().list_reviewable_hits](#clientlist_reviewable_hits)
        - [Client().list_worker_blocks](#clientlist_worker_blocks)
        - [Client().list_workers_with_qualification_type](#clientlist_workers_with_qualification_type)
        - [Client().notify_workers](#clientnotify_workers)
        - [Client().reject_assignment](#clientreject_assignment)
        - [Client().reject_qualification_request](#clientreject_qualification_request)
        - [Client().send_bonus](#clientsend_bonus)
        - [Client().send_test_event_notification](#clientsend_test_event_notification)
        - [Client().update_expiration_for_hit](#clientupdate_expiration_for_hit)
        - [Client().update_hit_review_status](#clientupdate_hit_review_status)
        - [Client().update_hit_type_of_hit](#clientupdate_hit_type_of_hit)
        - [Client().update_notification_settings](#clientupdate_notification_settings)
        - [Client().update_qualification_type](#clientupdate_qualification_type)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L13)

```python
class Client(BaseClient):
```

### Client().accept_qualification_request

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L16)

```python
def accept_qualification_request(
    QualificationRequestId: str,
    IntegerValue: int = None,
) -> Dict[str, Any]:
```

### Client().approve_assignment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L22)

```python
def approve_assignment(
    AssignmentId: str,
    RequesterFeedback: str = None,
    OverrideRejection: bool = None,
) -> Dict[str, Any]:
```

### Client().associate_qualification_with_worker

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L31)

```python
def associate_qualification_with_worker(
    QualificationTypeId: str,
    WorkerId: str,
    IntegerValue: int = None,
    SendNotification: bool = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L41)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_additional_assignments_for_hit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L45)

```python
def create_additional_assignments_for_hit(
    HITId: str,
    NumberOfAdditionalAssignments: int,
    UniqueRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_hit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L54)

```python
def create_hit(
    LifetimeInSeconds: int,
    AssignmentDurationInSeconds: int,
    Reward: str,
    Title: str,
    Description: str,
    MaxAssignments: int = None,
    AutoApprovalDelayInSeconds: int = None,
    Keywords: str = None,
    Question: str = None,
    RequesterAnnotation: str = None,
    QualificationRequirements: List[Any] = None,
    UniqueRequestToken: str = None,
    AssignmentReviewPolicy: Dict[str, Any] = None,
    HITReviewPolicy: Dict[str, Any] = None,
    HITLayoutId: str = None,
    HITLayoutParameters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_hit_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L76)

```python
def create_hit_type(
    AssignmentDurationInSeconds: int,
    Reward: str,
    Title: str,
    Description: str,
    AutoApprovalDelayInSeconds: int = None,
    Keywords: str = None,
    QualificationRequirements: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_hit_with_hit_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L89)

```python
def create_hit_with_hit_type(
    HITTypeId: str,
    LifetimeInSeconds: int,
    MaxAssignments: int = None,
    Question: str = None,
    RequesterAnnotation: str = None,
    UniqueRequestToken: str = None,
    AssignmentReviewPolicy: Dict[str, Any] = None,
    HITReviewPolicy: Dict[str, Any] = None,
    HITLayoutId: str = None,
    HITLayoutParameters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_qualification_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L105)

```python
def create_qualification_type(
    Name: str,
    Description: str,
    QualificationTypeStatus: str,
    Keywords: str = None,
    RetryDelayInSeconds: int = None,
    Test: str = None,
    AnswerKey: str = None,
    TestDurationInSeconds: int = None,
    AutoGranted: bool = None,
    AutoGrantedValue: int = None,
) -> Dict[str, Any]:
```

### Client().create_worker_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L121)

```python
def create_worker_block(WorkerId: str, Reason: str) -> Dict[str, Any]:
```

### Client().delete_hit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L125)

```python
def delete_hit(HITId: str) -> Dict[str, Any]:
```

### Client().delete_qualification_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L129)

```python
def delete_qualification_type(QualificationTypeId: str) -> Dict[str, Any]:
```

### Client().delete_worker_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L133)

```python
def delete_worker_block(WorkerId: str, Reason: str = None) -> Dict[str, Any]:
```

### Client().disassociate_qualification_from_worker

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L137)

```python
def disassociate_qualification_from_worker(
    WorkerId: str,
    QualificationTypeId: str,
    Reason: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L143)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_account_balance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L153)

```python
def get_account_balance() -> Dict[str, Any]:
```

### Client().get_assignment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L157)

```python
def get_assignment(AssignmentId: str) -> Dict[str, Any]:
```

### Client().get_file_upload_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L161)

```python
def get_file_upload_url(
    AssignmentId: str,
    QuestionIdentifier: str,
) -> Dict[str, Any]:
```

### Client().get_hit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L167)

```python
def get_hit(HITId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L171)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_qualification_score

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L175)

```python
def get_qualification_score(
    QualificationTypeId: str,
    WorkerId: str,
) -> Dict[str, Any]:
```

### Client().get_qualification_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L181)

```python
def get_qualification_type(QualificationTypeId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L185)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_assignments_for_hit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L189)

```python
def list_assignments_for_hit(
    HITId: str,
    NextToken: str = None,
    MaxResults: int = None,
    AssignmentStatuses: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_bonus_payments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L199)

```python
def list_bonus_payments(
    HITId: str = None,
    AssignmentId: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_hits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L209)

```python
def list_hits(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_hits_for_qualification_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L215)

```python
def list_hits_for_qualification_type(
    QualificationTypeId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_qualification_requests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L221)

```python
def list_qualification_requests(
    QualificationTypeId: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_qualification_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L230)

```python
def list_qualification_types(
    MustBeRequestable: bool,
    Query: str = None,
    MustBeOwnedByCaller: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_review_policy_results_for_hit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L241)

```python
def list_review_policy_results_for_hit(
    HITId: str,
    PolicyLevels: List[Any] = None,
    RetrieveActions: bool = None,
    RetrieveResults: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_reviewable_hits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L253)

```python
def list_reviewable_hits(
    HITTypeId: str = None,
    Status: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_worker_blocks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L263)

```python
def list_worker_blocks(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_workers_with_qualification_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L269)

```python
def list_workers_with_qualification_type(
    QualificationTypeId: str,
    Status: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().notify_workers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L279)

```python
def notify_workers(
    Subject: str,
    MessageText: str,
    WorkerIds: List[Any],
) -> Dict[str, Any]:
```

### Client().reject_assignment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L285)

```python
def reject_assignment(
    AssignmentId: str,
    RequesterFeedback: str,
) -> Dict[str, Any]:
```

### Client().reject_qualification_request

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L291)

```python
def reject_qualification_request(
    QualificationRequestId: str,
    Reason: str = None,
) -> Dict[str, Any]:
```

### Client().send_bonus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L297)

```python
def send_bonus(
    WorkerId: str,
    BonusAmount: str,
    AssignmentId: str,
    Reason: str,
    UniqueRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().send_test_event_notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L308)

```python
def send_test_event_notification(
    Notification: Dict[str, Any],
    TestEventType: str,
) -> Dict[str, Any]:
```

### Client().update_expiration_for_hit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L314)

```python
def update_expiration_for_hit(
    HITId: str,
    ExpireAt: datetime,
) -> Dict[str, Any]:
```

### Client().update_hit_review_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L320)

```python
def update_hit_review_status(
    HITId: str,
    Revert: bool = None,
) -> Dict[str, Any]:
```

### Client().update_hit_type_of_hit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L326)

```python
def update_hit_type_of_hit(HITId: str, HITTypeId: str) -> Dict[str, Any]:
```

### Client().update_notification_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L330)

```python
def update_notification_settings(
    HITTypeId: str,
    Notification: Dict[str, Any] = None,
    Active: bool = None,
) -> Dict[str, Any]:
```

### Client().update_qualification_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/client.py#L336)

```python
def update_qualification_type(
    QualificationTypeId: str,
    Description: str = None,
    QualificationTypeStatus: str = None,
    Test: str = None,
    AnswerKey: str = None,
    TestDurationInSeconds: int = None,
    RetryDelayInSeconds: int = None,
    AutoGranted: bool = None,
    AutoGrantedValue: int = None,
) -> Dict[str, Any]:
```
