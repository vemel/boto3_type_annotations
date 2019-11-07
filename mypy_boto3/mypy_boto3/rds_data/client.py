from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        database: Optional[str] = None,
        parameterSets: Optional[List] = None,
        schema: Optional[str] = None,
        transactionId: Optional[str] = None,
    ) -> Dict:
        pass


    def begin_transaction(
        self,
        resourceArn: str,
        secretArn: str,
        database: Optional[str] = None,
        schema: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def commit_transaction(
        self,
        resourceArn: str,
        secretArn: str,
        transactionId: str,
    ) -> Dict:
        pass


    def execute_sql(
        self,
        awsSecretStoreArn: str,
        dbClusterOrInstanceArn: str,
        sqlStatements: str,
        database: Optional[str] = None,
        schema: Optional[str] = None,
    ) -> Dict:
        pass


    def execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        continueAfterTimeout: Optional[bool] = None,
        database: Optional[str] = None,
        includeResultMetadata: Optional[bool] = None,
        parameters: Optional[List] = None,
        resultSetOptions: Optional[Dict] = None,
        schema: Optional[str] = None,
        transactionId: Optional[str] = None,
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


    def rollback_transaction(
        self,
        resourceArn: str,
        secretArn: str,
        transactionId: str,
    ) -> Dict:
        pass

