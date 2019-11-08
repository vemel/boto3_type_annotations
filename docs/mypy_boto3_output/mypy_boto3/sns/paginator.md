# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sns.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sns](index.md#sns) / Paginator
    - [ListEndpointsByPlatformApplication](#listendpointsbyplatformapplication)
        - [ListEndpointsByPlatformApplication().paginate](#listendpointsbyplatformapplicationpaginate)
    - [ListPhoneNumbersOptedOut](#listphonenumbersoptedout)
        - [ListPhoneNumbersOptedOut().paginate](#listphonenumbersoptedoutpaginate)
    - [ListPlatformApplications](#listplatformapplications)
        - [ListPlatformApplications().paginate](#listplatformapplicationspaginate)
    - [ListSubscriptions](#listsubscriptions)
        - [ListSubscriptions().paginate](#listsubscriptionspaginate)
    - [ListSubscriptionsByTopic](#listsubscriptionsbytopic)
        - [ListSubscriptionsByTopic().paginate](#listsubscriptionsbytopicpaginate)
    - [ListTopics](#listtopics)
        - [ListTopics().paginate](#listtopicspaginate)

## ListEndpointsByPlatformApplication

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L9)

```python
class ListEndpointsByPlatformApplication(Paginator):
```

### ListEndpointsByPlatformApplication().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L12)

```python
def paginate(
    PlatformApplicationArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPhoneNumbersOptedOut

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L18)

```python
class ListPhoneNumbersOptedOut(Paginator):
```

### ListPhoneNumbersOptedOut().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L21)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListPlatformApplications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L25)

```python
class ListPlatformApplications(Paginator):
```

### ListPlatformApplications().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L28)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListSubscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L32)

```python
class ListSubscriptions(Paginator):
```

### ListSubscriptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L35)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListSubscriptionsByTopic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L39)

```python
class ListSubscriptionsByTopic(Paginator):
```

### ListSubscriptionsByTopic().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L42)

```python
def paginate(
    TopicArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTopics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L48)

```python
class ListTopics(Paginator):
```

### ListTopics().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sns/paginator.py#L51)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
