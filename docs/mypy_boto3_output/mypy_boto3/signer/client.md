# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.signer.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Signer](index.md#signer) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_signing_profile](#clientcancel_signing_profile)
        - [Client().describe_signing_job](#clientdescribe_signing_job)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_signing_platform](#clientget_signing_platform)
        - [Client().get_signing_profile](#clientget_signing_profile)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_signing_jobs](#clientlist_signing_jobs)
        - [Client().list_signing_platforms](#clientlist_signing_platforms)
        - [Client().list_signing_profiles](#clientlist_signing_profiles)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_signing_profile](#clientput_signing_profile)
        - [Client().start_signing_job](#clientstart_signing_job)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_signing_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L19)

```python
def cancel_signing_profile(profileName: str) -> None:
```

### Client().describe_signing_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L23)

```python
def describe_signing_job(jobId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L27)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L37)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_signing_platform

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L41)

```python
def get_signing_platform(platformId: str) -> Dict[str, Any]:
```

### Client().get_signing_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L45)

```python
def get_signing_profile(profileName: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L49)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_signing_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L53)

```python
def list_signing_jobs(
    status: str = None,
    platformId: str = None,
    requestedBy: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_signing_platforms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L64)

```python
def list_signing_platforms(
    category: str = None,
    partner: str = None,
    target: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_signing_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L75)

```python
def list_signing_profiles(
    includeCanceled: bool = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L84)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().put_signing_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L88)

```python
def put_signing_profile(
    profileName: str,
    signingMaterial: Dict[str, Any],
    platformId: str,
    overrides: Dict[str, Any] = None,
    signingParameters: Dict[str, Any] = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().start_signing_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L100)

```python
def start_signing_job(
    source: Dict[str, Any],
    destination: Dict[str, Any],
    clientRequestToken: str,
    profileName: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L110)

```python
def tag_resource(resourceArn: str, tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/client.py#L114)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```
