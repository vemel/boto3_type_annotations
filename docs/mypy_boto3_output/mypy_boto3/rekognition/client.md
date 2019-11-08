# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.rekognition.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Rekognition](index.md#rekognition) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().compare_faces](#clientcompare_faces)
        - [Client().create_collection](#clientcreate_collection)
        - [Client().create_stream_processor](#clientcreate_stream_processor)
        - [Client().delete_collection](#clientdelete_collection)
        - [Client().delete_faces](#clientdelete_faces)
        - [Client().delete_stream_processor](#clientdelete_stream_processor)
        - [Client().describe_collection](#clientdescribe_collection)
        - [Client().describe_stream_processor](#clientdescribe_stream_processor)
        - [Client().detect_faces](#clientdetect_faces)
        - [Client().detect_labels](#clientdetect_labels)
        - [Client().detect_moderation_labels](#clientdetect_moderation_labels)
        - [Client().detect_text](#clientdetect_text)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_celebrity_info](#clientget_celebrity_info)
        - [Client().get_celebrity_recognition](#clientget_celebrity_recognition)
        - [Client().get_content_moderation](#clientget_content_moderation)
        - [Client().get_face_detection](#clientget_face_detection)
        - [Client().get_face_search](#clientget_face_search)
        - [Client().get_label_detection](#clientget_label_detection)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_person_tracking](#clientget_person_tracking)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().index_faces](#clientindex_faces)
        - [Client().list_collections](#clientlist_collections)
        - [Client().list_faces](#clientlist_faces)
        - [Client().list_stream_processors](#clientlist_stream_processors)
        - [Client().recognize_celebrities](#clientrecognize_celebrities)
        - [Client().search_faces](#clientsearch_faces)
        - [Client().search_faces_by_image](#clientsearch_faces_by_image)
        - [Client().start_celebrity_recognition](#clientstart_celebrity_recognition)
        - [Client().start_content_moderation](#clientstart_content_moderation)
        - [Client().start_face_detection](#clientstart_face_detection)
        - [Client().start_face_search](#clientstart_face_search)
        - [Client().start_label_detection](#clientstart_label_detection)
        - [Client().start_person_tracking](#clientstart_person_tracking)
        - [Client().start_stream_processor](#clientstart_stream_processor)
        - [Client().stop_stream_processor](#clientstop_stream_processor)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().compare_faces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L19)

```python
def compare_faces(
    SourceImage: Dict[str, Any],
    TargetImage: Dict[str, Any],
    SimilarityThreshold: float = None,
) -> Dict[str, Any]:
```

### Client().create_collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L28)

```python
def create_collection(CollectionId: str) -> Dict[str, Any]:
```

### Client().create_stream_processor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L32)

```python
def create_stream_processor(
    Input: Dict[str, Any],
    Output: Dict[str, Any],
    Name: str,
    Settings: Dict[str, Any],
    RoleArn: str,
) -> Dict[str, Any]:
```

### Client().delete_collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L43)

```python
def delete_collection(CollectionId: str) -> Dict[str, Any]:
```

### Client().delete_faces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L47)

```python
def delete_faces(CollectionId: str, FaceIds: List[Any]) -> Dict[str, Any]:
```

### Client().delete_stream_processor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L51)

```python
def delete_stream_processor(Name: str) -> Dict[str, Any]:
```

### Client().describe_collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L55)

```python
def describe_collection(CollectionId: str) -> Dict[str, Any]:
```

### Client().describe_stream_processor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L59)

```python
def describe_stream_processor(Name: str) -> Dict[str, Any]:
```

### Client().detect_faces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L63)

```python
def detect_faces(
    Image: Dict[str, Any],
    Attributes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().detect_labels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L69)

```python
def detect_labels(
    Image: Dict[str, Any],
    MaxLabels: int = None,
    MinConfidence: float = None,
) -> Dict[str, Any]:
```

### Client().detect_moderation_labels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L75)

```python
def detect_moderation_labels(
    Image: Dict[str, Any],
    MinConfidence: float = None,
) -> Dict[str, Any]:
```

### Client().detect_text

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L81)

```python
def detect_text(Image: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L85)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_celebrity_info

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L95)

```python
def get_celebrity_info(Id: str) -> Dict[str, Any]:
```

### Client().get_celebrity_recognition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L99)

```python
def get_celebrity_recognition(
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: str = None,
) -> Dict[str, Any]:
```

### Client().get_content_moderation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L109)

```python
def get_content_moderation(
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: str = None,
) -> Dict[str, Any]:
```

### Client().get_face_detection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L119)

```python
def get_face_detection(
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_face_search

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L125)

```python
def get_face_search(
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: str = None,
) -> Dict[str, Any]:
```

### Client().get_label_detection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L135)

```python
def get_label_detection(
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L145)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_person_tracking

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L149)

```python
def get_person_tracking(
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L159)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().index_faces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L163)

```python
def index_faces(
    CollectionId: str,
    Image: Dict[str, Any],
    ExternalImageId: str = None,
    DetectionAttributes: List[Any] = None,
    MaxFaces: int = None,
    QualityFilter: str = None,
) -> Dict[str, Any]:
```

### Client().list_collections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L175)

```python
def list_collections(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_faces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L181)

```python
def list_faces(
    CollectionId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_stream_processors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L187)

```python
def list_stream_processors(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().recognize_celebrities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L193)

```python
def recognize_celebrities(Image: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().search_faces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L197)

```python
def search_faces(
    CollectionId: str,
    FaceId: str,
    MaxFaces: int = None,
    FaceMatchThreshold: float = None,
) -> Dict[str, Any]:
```

### Client().search_faces_by_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L207)

```python
def search_faces_by_image(
    CollectionId: str,
    Image: Dict[str, Any],
    MaxFaces: int = None,
    FaceMatchThreshold: float = None,
) -> Dict[str, Any]:
```

### Client().start_celebrity_recognition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L217)

```python
def start_celebrity_recognition(
    Video: Dict[str, Any],
    ClientRequestToken: str = None,
    NotificationChannel: Dict[str, Any] = None,
    JobTag: str = None,
) -> Dict[str, Any]:
```

### Client().start_content_moderation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L227)

```python
def start_content_moderation(
    Video: Dict[str, Any],
    MinConfidence: float = None,
    ClientRequestToken: str = None,
    NotificationChannel: Dict[str, Any] = None,
    JobTag: str = None,
) -> Dict[str, Any]:
```

### Client().start_face_detection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L238)

```python
def start_face_detection(
    Video: Dict[str, Any],
    ClientRequestToken: str = None,
    NotificationChannel: Dict[str, Any] = None,
    FaceAttributes: str = None,
    JobTag: str = None,
) -> Dict[str, Any]:
```

### Client().start_face_search

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L249)

```python
def start_face_search(
    Video: Dict[str, Any],
    CollectionId: str,
    ClientRequestToken: str = None,
    FaceMatchThreshold: float = None,
    NotificationChannel: Dict[str, Any] = None,
    JobTag: str = None,
) -> Dict[str, Any]:
```

### Client().start_label_detection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L261)

```python
def start_label_detection(
    Video: Dict[str, Any],
    ClientRequestToken: str = None,
    MinConfidence: float = None,
    NotificationChannel: Dict[str, Any] = None,
    JobTag: str = None,
) -> Dict[str, Any]:
```

### Client().start_person_tracking

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L272)

```python
def start_person_tracking(
    Video: Dict[str, Any],
    ClientRequestToken: str = None,
    NotificationChannel: Dict[str, Any] = None,
    JobTag: str = None,
) -> Dict[str, Any]:
```

### Client().start_stream_processor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L282)

```python
def start_stream_processor(Name: str) -> Dict[str, Any]:
```

### Client().stop_stream_processor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rekognition/client.py#L286)

```python
def stop_stream_processor(Name: str) -> Dict[str, Any]:
```
