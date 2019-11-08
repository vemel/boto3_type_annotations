# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.transcribe.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Transcribe](index.md#transcribe) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_vocabulary](#clientcreate_vocabulary)
        - [Client().delete_transcription_job](#clientdelete_transcription_job)
        - [Client().delete_vocabulary](#clientdelete_vocabulary)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_transcription_job](#clientget_transcription_job)
        - [Client().get_vocabulary](#clientget_vocabulary)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_transcription_jobs](#clientlist_transcription_jobs)
        - [Client().list_vocabularies](#clientlist_vocabularies)
        - [Client().start_transcription_job](#clientstart_transcription_job)
        - [Client().update_vocabulary](#clientupdate_vocabulary)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_vocabulary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L19)

```python
def create_vocabulary(
    VocabularyName: str,
    LanguageCode: str,
    Phrases: List[Any] = None,
    VocabularyFileUri: str = None,
) -> Dict[str, Any]:
```

### Client().delete_transcription_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L29)

```python
def delete_transcription_job(TranscriptionJobName: str) -> None:
```

### Client().delete_vocabulary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L33)

```python
def delete_vocabulary(VocabularyName: str) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L37)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L47)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_transcription_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L51)

```python
def get_transcription_job(TranscriptionJobName: str) -> Dict[str, Any]:
```

### Client().get_vocabulary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L55)

```python
def get_vocabulary(VocabularyName: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L59)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_transcription_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L63)

```python
def list_transcription_jobs(
    Status: str = None,
    JobNameContains: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_vocabularies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L73)

```python
def list_vocabularies(
    NextToken: str = None,
    MaxResults: int = None,
    StateEquals: str = None,
    NameContains: str = None,
) -> Dict[str, Any]:
```

### Client().start_transcription_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L83)

```python
def start_transcription_job(
    TranscriptionJobName: str,
    LanguageCode: str,
    Media: Dict[str, Any],
    MediaSampleRateHertz: int = None,
    MediaFormat: str = None,
    OutputBucketName: str = None,
    OutputEncryptionKMSKeyId: str = None,
    Settings: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_vocabulary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transcribe/client.py#L97)

```python
def update_vocabulary(
    VocabularyName: str,
    LanguageCode: str,
    Phrases: List[Any] = None,
    VocabularyFileUri: str = None,
) -> Dict[str, Any]:
```
