# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.comprehend.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Comprehend](index.md#comprehend) / Client
    - [Client](#client)
        - [Client().batch_detect_dominant_language](#clientbatch_detect_dominant_language)
        - [Client().batch_detect_entities](#clientbatch_detect_entities)
        - [Client().batch_detect_key_phrases](#clientbatch_detect_key_phrases)
        - [Client().batch_detect_sentiment](#clientbatch_detect_sentiment)
        - [Client().batch_detect_syntax](#clientbatch_detect_syntax)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_document_classifier](#clientcreate_document_classifier)
        - [Client().create_entity_recognizer](#clientcreate_entity_recognizer)
        - [Client().delete_document_classifier](#clientdelete_document_classifier)
        - [Client().delete_entity_recognizer](#clientdelete_entity_recognizer)
        - [Client().describe_document_classification_job](#clientdescribe_document_classification_job)
        - [Client().describe_document_classifier](#clientdescribe_document_classifier)
        - [Client().describe_dominant_language_detection_job](#clientdescribe_dominant_language_detection_job)
        - [Client().describe_entities_detection_job](#clientdescribe_entities_detection_job)
        - [Client().describe_entity_recognizer](#clientdescribe_entity_recognizer)
        - [Client().describe_key_phrases_detection_job](#clientdescribe_key_phrases_detection_job)
        - [Client().describe_sentiment_detection_job](#clientdescribe_sentiment_detection_job)
        - [Client().describe_topics_detection_job](#clientdescribe_topics_detection_job)
        - [Client().detect_dominant_language](#clientdetect_dominant_language)
        - [Client().detect_entities](#clientdetect_entities)
        - [Client().detect_key_phrases](#clientdetect_key_phrases)
        - [Client().detect_sentiment](#clientdetect_sentiment)
        - [Client().detect_syntax](#clientdetect_syntax)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_document_classification_jobs](#clientlist_document_classification_jobs)
        - [Client().list_document_classifiers](#clientlist_document_classifiers)
        - [Client().list_dominant_language_detection_jobs](#clientlist_dominant_language_detection_jobs)
        - [Client().list_entities_detection_jobs](#clientlist_entities_detection_jobs)
        - [Client().list_entity_recognizers](#clientlist_entity_recognizers)
        - [Client().list_key_phrases_detection_jobs](#clientlist_key_phrases_detection_jobs)
        - [Client().list_sentiment_detection_jobs](#clientlist_sentiment_detection_jobs)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_topics_detection_jobs](#clientlist_topics_detection_jobs)
        - [Client().start_document_classification_job](#clientstart_document_classification_job)
        - [Client().start_dominant_language_detection_job](#clientstart_dominant_language_detection_job)
        - [Client().start_entities_detection_job](#clientstart_entities_detection_job)
        - [Client().start_key_phrases_detection_job](#clientstart_key_phrases_detection_job)
        - [Client().start_sentiment_detection_job](#clientstart_sentiment_detection_job)
        - [Client().start_topics_detection_job](#clientstart_topics_detection_job)
        - [Client().stop_dominant_language_detection_job](#clientstop_dominant_language_detection_job)
        - [Client().stop_entities_detection_job](#clientstop_entities_detection_job)
        - [Client().stop_key_phrases_detection_job](#clientstop_key_phrases_detection_job)
        - [Client().stop_sentiment_detection_job](#clientstop_sentiment_detection_job)
        - [Client().stop_training_document_classifier](#clientstop_training_document_classifier)
        - [Client().stop_training_entity_recognizer](#clientstop_training_entity_recognizer)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_detect_dominant_language

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L15)

```python
def batch_detect_dominant_language(TextList: List[Any]) -> Dict[str, Any]:
```

### Client().batch_detect_entities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L19)

```python
def batch_detect_entities(
    TextList: List[Any],
    LanguageCode: str,
) -> Dict[str, Any]:
```

### Client().batch_detect_key_phrases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L25)

```python
def batch_detect_key_phrases(
    TextList: List[Any],
    LanguageCode: str,
) -> Dict[str, Any]:
```

### Client().batch_detect_sentiment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L31)

```python
def batch_detect_sentiment(
    TextList: List[Any],
    LanguageCode: str,
) -> Dict[str, Any]:
```

### Client().batch_detect_syntax

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L37)

```python
def batch_detect_syntax(
    TextList: List[Any],
    LanguageCode: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L43)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_document_classifier

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L47)

```python
def create_document_classifier(
    DocumentClassifierName: str,
    DataAccessRoleArn: str,
    InputDataConfig: Dict[str, Any],
    LanguageCode: str,
    Tags: List[Any] = None,
    OutputDataConfig: Dict[str, Any] = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_entity_recognizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L62)

```python
def create_entity_recognizer(
    RecognizerName: str,
    DataAccessRoleArn: str,
    InputDataConfig: Dict[str, Any],
    LanguageCode: str,
    Tags: List[Any] = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_document_classifier

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L76)

```python
def delete_document_classifier(DocumentClassifierArn: str) -> Dict[str, Any]:
```

### Client().delete_entity_recognizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L80)

```python
def delete_entity_recognizer(EntityRecognizerArn: str) -> Dict[str, Any]:
```

### Client().describe_document_classification_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L84)

```python
def describe_document_classification_job(JobId: str) -> Dict[str, Any]:
```

### Client().describe_document_classifier

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L88)

```python
def describe_document_classifier(
    DocumentClassifierArn: str,
) -> Dict[str, Any]:
```

### Client().describe_dominant_language_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L94)

```python
def describe_dominant_language_detection_job(JobId: str) -> Dict[str, Any]:
```

### Client().describe_entities_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L98)

```python
def describe_entities_detection_job(JobId: str) -> Dict[str, Any]:
```

### Client().describe_entity_recognizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L102)

```python
def describe_entity_recognizer(EntityRecognizerArn: str) -> Dict[str, Any]:
```

### Client().describe_key_phrases_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L106)

```python
def describe_key_phrases_detection_job(JobId: str) -> Dict[str, Any]:
```

### Client().describe_sentiment_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L110)

```python
def describe_sentiment_detection_job(JobId: str) -> Dict[str, Any]:
```

### Client().describe_topics_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L114)

```python
def describe_topics_detection_job(JobId: str) -> Dict[str, Any]:
```

### Client().detect_dominant_language

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L118)

```python
def detect_dominant_language(Text: str) -> Dict[str, Any]:
```

### Client().detect_entities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L122)

```python
def detect_entities(Text: str, LanguageCode: str) -> Dict[str, Any]:
```

### Client().detect_key_phrases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L126)

```python
def detect_key_phrases(Text: str, LanguageCode: str) -> Dict[str, Any]:
```

### Client().detect_sentiment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L130)

```python
def detect_sentiment(Text: str, LanguageCode: str) -> Dict[str, Any]:
```

### Client().detect_syntax

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L134)

```python
def detect_syntax(Text: str, LanguageCode: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L138)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L148)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L152)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_document_classification_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L156)

```python
def list_document_classification_jobs(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_document_classifiers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L165)

```python
def list_document_classifiers(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_dominant_language_detection_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L174)

```python
def list_dominant_language_detection_jobs(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_entities_detection_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L183)

```python
def list_entities_detection_jobs(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_entity_recognizers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L192)

```python
def list_entity_recognizers(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_key_phrases_detection_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L201)

```python
def list_key_phrases_detection_jobs(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_sentiment_detection_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L210)

```python
def list_sentiment_detection_jobs(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L219)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().list_topics_detection_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L223)

```python
def list_topics_detection_jobs(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().start_document_classification_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L232)

```python
def start_document_classification_job(
    DocumentClassifierArn: str,
    InputDataConfig: Dict[str, Any],
    OutputDataConfig: Dict[str, Any],
    DataAccessRoleArn: str,
    JobName: str = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().start_dominant_language_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L246)

```python
def start_dominant_language_detection_job(
    InputDataConfig: Dict[str, Any],
    OutputDataConfig: Dict[str, Any],
    DataAccessRoleArn: str,
    JobName: str = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().start_entities_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L259)

```python
def start_entities_detection_job(
    InputDataConfig: Dict[str, Any],
    OutputDataConfig: Dict[str, Any],
    DataAccessRoleArn: str,
    LanguageCode: str,
    JobName: str = None,
    EntityRecognizerArn: str = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().start_key_phrases_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L274)

```python
def start_key_phrases_detection_job(
    InputDataConfig: Dict[str, Any],
    OutputDataConfig: Dict[str, Any],
    DataAccessRoleArn: str,
    LanguageCode: str,
    JobName: str = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().start_sentiment_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L288)

```python
def start_sentiment_detection_job(
    InputDataConfig: Dict[str, Any],
    OutputDataConfig: Dict[str, Any],
    DataAccessRoleArn: str,
    LanguageCode: str,
    JobName: str = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().start_topics_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L302)

```python
def start_topics_detection_job(
    InputDataConfig: Dict[str, Any],
    OutputDataConfig: Dict[str, Any],
    DataAccessRoleArn: str,
    JobName: str = None,
    NumberOfTopics: int = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().stop_dominant_language_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L316)

```python
def stop_dominant_language_detection_job(JobId: str) -> Dict[str, Any]:
```

### Client().stop_entities_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L320)

```python
def stop_entities_detection_job(JobId: str) -> Dict[str, Any]:
```

### Client().stop_key_phrases_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L324)

```python
def stop_key_phrases_detection_job(JobId: str) -> Dict[str, Any]:
```

### Client().stop_sentiment_detection_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L328)

```python
def stop_sentiment_detection_job(JobId: str) -> Dict[str, Any]:
```

### Client().stop_training_document_classifier

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L332)

```python
def stop_training_document_classifier(
    DocumentClassifierArn: str,
) -> Dict[str, Any]:
```

### Client().stop_training_entity_recognizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L338)

```python
def stop_training_entity_recognizer(
    EntityRecognizerArn: str,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L344)

```python
def tag_resource(ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/comprehend/client.py#L348)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```
