# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.savingsplans.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Savingsplans](index.md#savingsplans) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_savings_plan](#clientcreate_savings_plan)
        - [Client().describe_savings_plan_rates](#clientdescribe_savings_plan_rates)
        - [Client().describe_savings_plans](#clientdescribe_savings_plans)
        - [Client().describe_savings_plans_offering_rates](#clientdescribe_savings_plans_offering_rates)
        - [Client().describe_savings_plans_offerings](#clientdescribe_savings_plans_offerings)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_savings_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L19)

```python
def create_savings_plan(
    savingsPlanOfferingId: str,
    commitment: str,
    upfrontPaymentAmount: str = None,
    clientToken: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_savings_plan_rates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L30)

```python
def describe_savings_plan_rates(
    savingsPlanId: str,
    filters: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_savings_plans

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L40)

```python
def describe_savings_plans(
    savingsPlanArns: List[Any] = None,
    savingsPlanIds: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
    states: List[Any] = None,
    filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_savings_plans_offering_rates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L52)

```python
def describe_savings_plans_offering_rates(
    savingsPlanOfferingIds: List[Any] = None,
    savingsPlanPaymentOptions: List[Any] = None,
    savingsPlanTypes: List[Any] = None,
    products: List[Any] = None,
    serviceCodes: List[Any] = None,
    usageTypes: List[Any] = None,
    operations: List[Any] = None,
    filters: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_savings_plans_offerings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L68)

```python
def describe_savings_plans_offerings(
    offeringIds: List[Any] = None,
    paymentOptions: List[Any] = None,
    productType: str = None,
    planTypes: List[Any] = None,
    durations: List[Any] = None,
    currencies: List[Any] = None,
    descriptions: List[Any] = None,
    serviceCodes: List[Any] = None,
    usageTypes: List[Any] = None,
    operations: List[Any] = None,
    filters: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L87)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L97)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L101)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L105)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L109)

```python
def tag_resource(resourceArn: str, tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/savingsplans/client.py#L113)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```
