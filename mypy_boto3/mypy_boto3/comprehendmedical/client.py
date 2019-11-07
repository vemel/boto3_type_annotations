from typing import Dict
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def describe_entities_detection_v2_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def describe_phi_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def detect_entities(
        self,
        Text: str,
    ) -> Dict:
        pass


    def detect_entities_v2(
        self,
        Text: str,
    ) -> Dict:
        pass


    def detect_phi(
        self,
        Text: str,
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


    def list_entities_detection_v2_jobs(
        self,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_phi_detection_jobs(
        self,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def start_entities_detection_v2_job(
        self,
        InputDataConfig: Dict,
        OutputDataConfig: Dict,
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        KMSKey: Optional[str] = None,
    ) -> Dict:
        pass


    def start_phi_detection_job(
        self,
        InputDataConfig: Dict,
        OutputDataConfig: Dict,
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        KMSKey: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_entities_detection_v2_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def stop_phi_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass

