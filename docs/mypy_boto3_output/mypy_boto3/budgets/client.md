# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.budgets.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Budgets](index.md#budgets) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_budget](#clientcreate_budget)
        - [Client().create_notification](#clientcreate_notification)
        - [Client().create_subscriber](#clientcreate_subscriber)
        - [Client().delete_budget](#clientdelete_budget)
        - [Client().delete_notification](#clientdelete_notification)
        - [Client().delete_subscriber](#clientdelete_subscriber)
        - [Client().describe_budget](#clientdescribe_budget)
        - [Client().describe_budget_performance_history](#clientdescribe_budget_performance_history)
        - [Client().describe_budgets](#clientdescribe_budgets)
        - [Client().describe_notifications_for_budget](#clientdescribe_notifications_for_budget)
        - [Client().describe_subscribers_for_notification](#clientdescribe_subscribers_for_notification)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().update_budget](#clientupdate_budget)
        - [Client().update_notification](#clientupdate_notification)
        - [Client().update_subscriber](#clientupdate_subscriber)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_budget

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L19)

```python
def create_budget(
    AccountId: str,
    Budget: Dict[str, Any],
    NotificationsWithSubscribers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L28)

```python
def create_notification(
    AccountId: str,
    BudgetName: str,
    Notification: Dict[str, Any],
    Subscribers: List[Any],
) -> Dict[str, Any]:
```

### Client().create_subscriber

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L38)

```python
def create_subscriber(
    AccountId: str,
    BudgetName: str,
    Notification: Dict[str, Any],
    Subscriber: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_budget

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L48)

```python
def delete_budget(AccountId: str, BudgetName: str) -> Dict[str, Any]:
```

### Client().delete_notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L52)

```python
def delete_notification(
    AccountId: str,
    BudgetName: str,
    Notification: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_subscriber

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L58)

```python
def delete_subscriber(
    AccountId: str,
    BudgetName: str,
    Notification: Dict[str, Any],
    Subscriber: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().describe_budget

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L68)

```python
def describe_budget(AccountId: str, BudgetName: str) -> Dict[str, Any]:
```

### Client().describe_budget_performance_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L72)

```python
def describe_budget_performance_history(
    AccountId: str,
    BudgetName: str,
    TimePeriod: Dict[str, Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_budgets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L83)

```python
def describe_budgets(
    AccountId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_notifications_for_budget

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L89)

```python
def describe_notifications_for_budget(
    AccountId: str,
    BudgetName: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_subscribers_for_notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L99)

```python
def describe_subscribers_for_notification(
    AccountId: str,
    BudgetName: str,
    Notification: Dict[str, Any],
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L110)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L120)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L124)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().update_budget

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L128)

```python
def update_budget(
    AccountId: str,
    NewBudget: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L134)

```python
def update_notification(
    AccountId: str,
    BudgetName: str,
    OldNotification: Dict[str, Any],
    NewNotification: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_subscriber

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/client.py#L144)

```python
def update_subscriber(
    AccountId: str,
    BudgetName: str,
    Notification: Dict[str, Any],
    OldSubscriber: Dict[str, Any],
    NewSubscriber: Dict[str, Any],
) -> Dict[str, Any]:
```
