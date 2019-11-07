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


    def create_detector_model(
        self,
        detectorModelName: str,
        detectorModelDefinition: Dict,
        roleArn: str,
        detectorModelDescription: Optional[str] = None,
        key: Optional[str] = None,
        tags: Optional[List] = None,
        evaluationMethod: Optional[str] = None,
    ) -> Dict:
        pass


    def create_input(
        self,
        inputName: str,
        inputDefinition: Dict,
        inputDescription: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_detector_model(
        self,
        detectorModelName: str,
    ) -> Dict:
        pass


    def delete_input(
        self,
        inputName: str,
    ) -> Dict:
        pass


    def describe_detector_model(
        self,
        detectorModelName: str,
        detectorModelVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_input(
        self,
        inputName: str,
    ) -> Dict:
        pass


    def describe_logging_options(
        self,
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


    def list_detector_model_versions(
        self,
        detectorModelName: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_detector_models(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_inputs(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def put_logging_options(
        self,
        loggingOptions: Dict,
    ):
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_detector_model(
        self,
        detectorModelName: str,
        detectorModelDefinition: Dict,
        roleArn: str,
        detectorModelDescription: Optional[str] = None,
        evaluationMethod: Optional[str] = None,
    ) -> Dict:
        pass


    def update_input(
        self,
        inputName: str,
        inputDefinition: Dict,
        inputDescription: Optional[str] = None,
    ) -> Dict:
        pass

