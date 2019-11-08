from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def compare_faces(
        self,
        SourceImage: Dict[str, Any],
        TargetImage: Dict[str, Any],
        SimilarityThreshold: float = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_collection(self, CollectionId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_stream_processor(
        self,
        Input: Dict[str, Any],
        Output: Dict[str, Any],
        Name: str,
        Settings: Dict[str, Any],
        RoleArn: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_collection(self, CollectionId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_faces(self, CollectionId: str, FaceIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_stream_processor(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_collection(self, CollectionId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stream_processor(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_faces(
        self, Image: Dict[str, Any], Attributes: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_labels(
        self, Image: Dict[str, Any], MaxLabels: int = None, MinConfidence: float = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_moderation_labels(
        self, Image: Dict[str, Any], MinConfidence: float = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_text(self, Image: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_celebrity_info(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_celebrity_recognition(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_content_moderation(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_face_detection(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_face_search(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_label_detection(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_person_tracking(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def index_faces(
        self,
        CollectionId: str,
        Image: Dict[str, Any],
        ExternalImageId: str = None,
        DetectionAttributes: List[Any] = None,
        MaxFaces: int = None,
        QualityFilter: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_collections(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_faces(
        self, CollectionId: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_stream_processors(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def recognize_celebrities(self, Image: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def search_faces(
        self,
        CollectionId: str,
        FaceId: str,
        MaxFaces: int = None,
        FaceMatchThreshold: float = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def search_faces_by_image(
        self,
        CollectionId: str,
        Image: Dict[str, Any],
        MaxFaces: int = None,
        FaceMatchThreshold: float = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_celebrity_recognition(
        self,
        Video: Dict[str, Any],
        ClientRequestToken: str = None,
        NotificationChannel: Dict[str, Any] = None,
        JobTag: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_content_moderation(
        self,
        Video: Dict[str, Any],
        MinConfidence: float = None,
        ClientRequestToken: str = None,
        NotificationChannel: Dict[str, Any] = None,
        JobTag: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_face_detection(
        self,
        Video: Dict[str, Any],
        ClientRequestToken: str = None,
        NotificationChannel: Dict[str, Any] = None,
        FaceAttributes: str = None,
        JobTag: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_face_search(
        self,
        Video: Dict[str, Any],
        CollectionId: str,
        ClientRequestToken: str = None,
        FaceMatchThreshold: float = None,
        NotificationChannel: Dict[str, Any] = None,
        JobTag: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_label_detection(
        self,
        Video: Dict[str, Any],
        ClientRequestToken: str = None,
        MinConfidence: float = None,
        NotificationChannel: Dict[str, Any] = None,
        JobTag: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_person_tracking(
        self,
        Video: Dict[str, Any],
        ClientRequestToken: str = None,
        NotificationChannel: Dict[str, Any] = None,
        JobTag: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_stream_processor(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_stream_processor(self, Name: str) -> Dict[str, Any]:
        pass
