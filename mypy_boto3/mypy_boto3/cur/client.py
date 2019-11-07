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


    def delete_report_definition(
        self,
        ReportName: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_report_definitions(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
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


    def modify_report_definition(
        self,
        ReportName: str,
        ReportDefinition: Dict,
    ) -> Dict:
        pass


    def put_report_definition(
        self,
        ReportDefinition: Dict,
    ) -> Dict:
        pass

