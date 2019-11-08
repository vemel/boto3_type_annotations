# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.support.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Support](index.md#support) / Client
    - [Client](#client)
        - [Client().add_attachments_to_set](#clientadd_attachments_to_set)
        - [Client().add_communication_to_case](#clientadd_communication_to_case)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_case](#clientcreate_case)
        - [Client().describe_attachment](#clientdescribe_attachment)
        - [Client().describe_cases](#clientdescribe_cases)
        - [Client().describe_communications](#clientdescribe_communications)
        - [Client().describe_services](#clientdescribe_services)
        - [Client().describe_severity_levels](#clientdescribe_severity_levels)
        - [Client().describe_trusted_advisor_check_refresh_statuses](#clientdescribe_trusted_advisor_check_refresh_statuses)
        - [Client().describe_trusted_advisor_check_result](#clientdescribe_trusted_advisor_check_result)
        - [Client().describe_trusted_advisor_check_summaries](#clientdescribe_trusted_advisor_check_summaries)
        - [Client().describe_trusted_advisor_checks](#clientdescribe_trusted_advisor_checks)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().refresh_trusted_advisor_check](#clientrefresh_trusted_advisor_check)
        - [Client().resolve_case](#clientresolve_case)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_attachments_to_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L15)

```python
def add_attachments_to_set(
    attachments: List[Any],
    attachmentSetId: str = None,
) -> Dict[str, Any]:
```

### Client().add_communication_to_case

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L21)

```python
def add_communication_to_case(
    communicationBody: str,
    caseId: str = None,
    ccEmailAddresses: List[Any] = None,
    attachmentSetId: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L31)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_case

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L35)

```python
def create_case(
    subject: str,
    communicationBody: str,
    serviceCode: str = None,
    severityCode: str = None,
    categoryCode: str = None,
    ccEmailAddresses: List[Any] = None,
    language: str = None,
    issueType: str = None,
    attachmentSetId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_attachment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L50)

```python
def describe_attachment(attachmentId: str) -> Dict[str, Any]:
```

### Client().describe_cases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L54)

```python
def describe_cases(
    caseIdList: List[Any] = None,
    displayId: str = None,
    afterTime: str = None,
    beforeTime: str = None,
    includeResolvedCases: bool = None,
    nextToken: str = None,
    maxResults: int = None,
    language: str = None,
    includeCommunications: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_communications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L69)

```python
def describe_communications(
    caseId: str,
    beforeTime: str = None,
    afterTime: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_services

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L80)

```python
def describe_services(
    serviceCodeList: List[Any] = None,
    language: str = None,
) -> Dict[str, Any]:
```

### Client().describe_severity_levels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L86)

```python
def describe_severity_levels(language: str = None) -> Dict[str, Any]:
```

### Client().describe_trusted_advisor_check_refresh_statuses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L90)

```python
def describe_trusted_advisor_check_refresh_statuses(
    checkIds: List[Any],
) -> Dict[str, Any]:
```

### Client().describe_trusted_advisor_check_result

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L96)

```python
def describe_trusted_advisor_check_result(
    checkId: str,
    language: str = None,
) -> Dict[str, Any]:
```

### Client().describe_trusted_advisor_check_summaries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L102)

```python
def describe_trusted_advisor_check_summaries(
    checkIds: List[Any],
) -> Dict[str, Any]:
```

### Client().describe_trusted_advisor_checks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L108)

```python
def describe_trusted_advisor_checks(language: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L112)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L122)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L126)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().refresh_trusted_advisor_check

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L130)

```python
def refresh_trusted_advisor_check(checkId: str) -> Dict[str, Any]:
```

### Client().resolve_case

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/client.py#L134)

```python
def resolve_case(caseId: str = None) -> Dict[str, Any]:
```
