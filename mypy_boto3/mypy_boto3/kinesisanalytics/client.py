from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_application_cloud_watch_logging_option(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOption: Dict,
    ) -> Dict:
        pass


    def add_application_input(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        Input: Dict,
    ) -> Dict:
        pass


    def add_application_input_processing_configuration(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: Dict,
    ) -> Dict:
        pass


    def add_application_output(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        Output: Dict,
    ) -> Dict:
        pass


    def add_application_reference_data_source(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: Dict,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_application(
        self,
        ApplicationName: str,
        ApplicationDescription: Optional[str] = None,
        Inputs: Optional[List] = None,
        Outputs: Optional[List] = None,
        CloudWatchLoggingOptions: Optional[List] = None,
        ApplicationCode: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_application(
        self,
        ApplicationName: str,
        CreateTimestamp: datetime,
    ) -> Dict:
        pass


    def delete_application_cloud_watch_logging_option(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOptionId: str,
    ) -> Dict:
        pass


    def delete_application_input_processing_configuration(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
    ) -> Dict:
        pass


    def delete_application_output(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        OutputId: str,
    ) -> Dict:
        pass


    def delete_application_reference_data_source(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceId: str,
    ) -> Dict:
        pass


    def describe_application(
        self,
        ApplicationName: str,
    ) -> Dict:
        pass


    def discover_input_schema(
        self,
        ResourceARN: Optional[str] = None,
        RoleARN: Optional[str] = None,
        InputStartingPositionConfiguration: Optional[Dict] = None,
        S3Configuration: Optional[Dict] = None,
        InputProcessingConfiguration: Optional[Dict] = None,
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


    def list_applications(
        self,
        Limit: Optional[int] = None,
        ExclusiveStartApplicationName: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceARN: str,
    ) -> Dict:
        pass


    def start_application(
        self,
        ApplicationName: str,
        InputConfigurations: List,
    ) -> Dict:
        pass


    def stop_application(
        self,
        ApplicationName: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceARN: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceARN: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_application(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ApplicationUpdate: Dict,
    ) -> Dict:
        pass

