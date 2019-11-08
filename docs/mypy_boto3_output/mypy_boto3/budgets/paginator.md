# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.budgets.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Budgets](index.md#budgets) / Paginator
    - [DescribeBudgets](#describebudgets)
        - [DescribeBudgets().paginate](#describebudgetspaginate)
    - [DescribeNotificationsForBudget](#describenotificationsforbudget)
        - [DescribeNotificationsForBudget().paginate](#describenotificationsforbudgetpaginate)
    - [DescribeSubscribersForNotification](#describesubscribersfornotification)
        - [DescribeSubscribersForNotification().paginate](#describesubscribersfornotificationpaginate)

## DescribeBudgets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/paginator.py#L9)

```python
class DescribeBudgets(Paginator):
```

### DescribeBudgets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/paginator.py#L12)

```python
def paginate(
    AccountId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeNotificationsForBudget

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/paginator.py#L18)

```python
class DescribeNotificationsForBudget(Paginator):
```

### DescribeNotificationsForBudget().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/paginator.py#L21)

```python
def paginate(
    AccountId: str,
    BudgetName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeSubscribersForNotification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/paginator.py#L27)

```python
class DescribeSubscribersForNotification(Paginator):
```

### DescribeSubscribersForNotification().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/budgets/paginator.py#L30)

```python
def paginate(
    AccountId: str,
    BudgetName: str,
    Notification: Dict[str, Any],
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
