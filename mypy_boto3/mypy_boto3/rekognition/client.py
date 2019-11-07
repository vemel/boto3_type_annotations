from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def compare_faces(
        self,
        SourceImage: Dict,
        TargetImage: Dict,
        SimilarityThreshold: Optional[float] = None,
    ) -> Dict:
        pass


    def create_collection(
        self,
        CollectionId: str,
    ) -> Dict:
        pass


    def create_stream_processor(
        self,
        Input: Dict,
        Output: Dict,
        Name: str,
        Settings: Dict,
        RoleArn: str,
    ) -> Dict:
        pass


    def delete_collection(
        self,
        CollectionId: str,
    ) -> Dict:
        pass


    def delete_faces(
        self,
        CollectionId: str,
        FaceIds: List,
    ) -> Dict:
        pass


    def delete_stream_processor(
        self,
        Name: str,
    ) -> Dict:
        pass


    def describe_collection(
        self,
        CollectionId: str,
    ) -> Dict:
        pass


    def describe_stream_processor(
        self,
        Name: str,
    ) -> Dict:
        pass


    def detect_faces(
        self,
        Image: Dict,
        Attributes: Optional[List] = None,
    ) -> Dict:
        pass


    def detect_labels(
        self,
        Image: Dict,
        MaxLabels: Optional[int] = None,
        MinConfidence: Optional[float] = None,
    ) -> Dict:
        pass


    def detect_moderation_labels(
        self,
        Image: Dict,
        MinConfidence: Optional[float] = None,
    ) -> Dict:
        pass


    def detect_text(
        self,
        Image: Dict,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_celebrity_info(
        self,
        Id: str,
    ) -> Dict:
        pass


    def get_celebrity_recognition(
        self,
        JobId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        SortBy: Optional[str] = None,
    ) -> Dict:
        pass


    def get_content_moderation(
        self,
        JobId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        SortBy: Optional[str] = None,
    ) -> Dict:
        pass


    def get_face_detection(
        self,
        JobId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_face_search(
        self,
        JobId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        SortBy: Optional[str] = None,
    ) -> Dict:
        pass


    def get_label_detection(
        self,
        JobId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        SortBy: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_person_tracking(
        self,
        JobId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        SortBy: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def index_faces(
        self,
        CollectionId: str,
        Image: Dict,
        ExternalImageId: Optional[str] = None,
        DetectionAttributes: Optional[List] = None,
        MaxFaces: Optional[int] = None,
        QualityFilter: Optional[str] = None,
    ) -> Dict:
        pass


    def list_collections(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_faces(
        self,
        CollectionId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_stream_processors(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def recognize_celebrities(
        self,
        Image: Dict,
    ) -> Dict:
        pass


    def search_faces(
        self,
        CollectionId: str,
        FaceId: str,
        MaxFaces: Optional[int] = None,
        FaceMatchThreshold: Optional[float] = None,
    ) -> Dict:
        pass


    def search_faces_by_image(
        self,
        CollectionId: str,
        Image: Dict,
        MaxFaces: Optional[int] = None,
        FaceMatchThreshold: Optional[float] = None,
    ) -> Dict:
        pass


    def start_celebrity_recognition(
        self,
        Video: Dict,
        ClientRequestToken: Optional[str] = None,
        NotificationChannel: Optional[Dict] = None,
        JobTag: Optional[str] = None,
    ) -> Dict:
        pass


    def start_content_moderation(
        self,
        Video: Dict,
        MinConfidence: Optional[float] = None,
        ClientRequestToken: Optional[str] = None,
        NotificationChannel: Optional[Dict] = None,
        JobTag: Optional[str] = None,
    ) -> Dict:
        pass


    def start_face_detection(
        self,
        Video: Dict,
        ClientRequestToken: Optional[str] = None,
        NotificationChannel: Optional[Dict] = None,
        FaceAttributes: Optional[str] = None,
        JobTag: Optional[str] = None,
    ) -> Dict:
        pass


    def start_face_search(
        self,
        Video: Dict,
        CollectionId: str,
        ClientRequestToken: Optional[str] = None,
        FaceMatchThreshold: Optional[float] = None,
        NotificationChannel: Optional[Dict] = None,
        JobTag: Optional[str] = None,
    ) -> Dict:
        pass


    def start_label_detection(
        self,
        Video: Dict,
        ClientRequestToken: Optional[str] = None,
        MinConfidence: Optional[float] = None,
        NotificationChannel: Optional[Dict] = None,
        JobTag: Optional[str] = None,
    ) -> Dict:
        pass


    def start_person_tracking(
        self,
        Video: Dict,
        ClientRequestToken: Optional[str] = None,
        NotificationChannel: Optional[Dict] = None,
        JobTag: Optional[str] = None,
    ) -> Dict:
        pass


    def start_stream_processor(
        self,
        Name: str,
    ) -> Dict:
        pass


    def stop_stream_processor(
        self,
        Name: str,
    ) -> Dict:
        pass

