from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def analyze_document(
        self,
        Document: Dict,
        FeatureTypes: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def detect_document_text(
        self,
        Document: Dict,
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


    def get_document_analysis(
        self,
        JobId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_document_text_detection(
        self,
        JobId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def start_document_analysis(
        self,
        DocumentLocation: Dict,
        FeatureTypes: List,
        ClientRequestToken: Optional[str] = None,
        JobTag: Optional[str] = None,
        NotificationChannel: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_document_text_detection(
        self,
        DocumentLocation: Dict,
        ClientRequestToken: Optional[str] = None,
        JobTag: Optional[str] = None,
        NotificationChannel: Optional[Dict] = None,
    ) -> Dict:
        pass

