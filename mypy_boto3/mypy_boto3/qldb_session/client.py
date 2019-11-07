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


    def send_command(
        self,
        SessionToken: Optional[str] = None,
        StartSession: Optional[Dict] = None,
        StartTransaction: Optional[Dict] = None,
        EndSession: Optional[Dict] = None,
        CommitTransaction: Optional[Dict] = None,
        AbortTransaction: Optional[Dict] = None,
        ExecuteStatement: Optional[Dict] = None,
        FetchPage: Optional[Dict] = None,
    ) -> Dict:
        pass

