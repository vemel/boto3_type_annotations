from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_get_named_query(
        self,
        NamedQueryIds: List,
    ) -> Dict:
        pass


    def batch_get_query_execution(
        self,
        QueryExecutionIds: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_named_query(
        self,
        Name: str,
        Database: str,
        QueryString: str,
        Description: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        WorkGroup: Optional[str] = None,
    ) -> Dict:
        pass


    def create_work_group(
        self,
        Name: str,
        Configuration: Optional[Dict] = None,
        Description: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_named_query(
        self,
        NamedQueryId: str,
    ) -> Dict:
        pass


    def delete_work_group(
        self,
        WorkGroup: str,
        RecursiveDeleteOption: Optional[bool] = None,
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


    def get_named_query(
        self,
        NamedQueryId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_query_execution(
        self,
        QueryExecutionId: str,
    ) -> Dict:
        pass


    def get_query_results(
        self,
        QueryExecutionId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def get_work_group(
        self,
        WorkGroup: str,
    ) -> Dict:
        pass


    def list_named_queries(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        WorkGroup: Optional[str] = None,
    ) -> Dict:
        pass


    def list_query_executions(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        WorkGroup: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceARN: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_work_groups(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def start_query_execution(
        self,
        QueryString: str,
        ClientRequestToken: Optional[str] = None,
        QueryExecutionContext: Optional[Dict] = None,
        ResultConfiguration: Optional[Dict] = None,
        WorkGroup: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_query_execution(
        self,
        QueryExecutionId: str,
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


    def update_work_group(
        self,
        WorkGroup: str,
        Description: Optional[str] = None,
        ConfigurationUpdates: Optional[Dict] = None,
        State: Optional[str] = None,
    ) -> Dict:
        pass

