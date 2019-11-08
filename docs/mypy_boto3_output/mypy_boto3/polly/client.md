# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.polly.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Polly](index.md#polly) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_lexicon](#clientdelete_lexicon)
        - [Client().describe_voices](#clientdescribe_voices)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_lexicon](#clientget_lexicon)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_speech_synthesis_task](#clientget_speech_synthesis_task)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_lexicons](#clientlist_lexicons)
        - [Client().list_speech_synthesis_tasks](#clientlist_speech_synthesis_tasks)
        - [Client().put_lexicon](#clientput_lexicon)
        - [Client().start_speech_synthesis_task](#clientstart_speech_synthesis_task)
        - [Client().synthesize_speech](#clientsynthesize_speech)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_lexicon

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L19)

```python
def delete_lexicon(Name: str) -> Dict[str, Any]:
```

### Client().describe_voices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L23)

```python
def describe_voices(
    Engine: str = None,
    LanguageCode: str = None,
    IncludeAdditionalLanguageCodes: bool = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L33)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_lexicon

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L43)

```python
def get_lexicon(Name: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L47)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_speech_synthesis_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L51)

```python
def get_speech_synthesis_task(TaskId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L55)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_lexicons

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L59)

```python
def list_lexicons(NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_speech_synthesis_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L63)

```python
def list_speech_synthesis_tasks(
    MaxResults: int = None,
    NextToken: str = None,
    Status: str = None,
) -> Dict[str, Any]:
```

### Client().put_lexicon

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L69)

```python
def put_lexicon(Name: str, Content: str) -> Dict[str, Any]:
```

### Client().start_speech_synthesis_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L73)

```python
def start_speech_synthesis_task(
    OutputFormat: str,
    OutputS3BucketName: str,
    Text: str,
    VoiceId: str,
    Engine: str = None,
    LanguageCode: str = None,
    LexiconNames: List[Any] = None,
    OutputS3KeyPrefix: str = None,
    SampleRate: str = None,
    SnsTopicArn: str = None,
    SpeechMarkTypes: List[Any] = None,
    TextType: str = None,
) -> Dict[str, Any]:
```

### Client().synthesize_speech

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/client.py#L91)

```python
def synthesize_speech(
    OutputFormat: str,
    Text: str,
    VoiceId: str,
    Engine: str = None,
    LanguageCode: str = None,
    LexiconNames: List[Any] = None,
    SampleRate: str = None,
    SpeechMarkTypes: List[Any] = None,
    TextType: str = None,
) -> Dict[str, Any]:
```
