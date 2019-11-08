from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def batch_execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        database: str = None,
        parameterSets: List[Any] = None,
        schema: str = None,
        transactionId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def begin_transaction(
        self, resourceArn: str, secretArn: str, database: str = None, schema: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def commit_transaction(
        self, resourceArn: str, secretArn: str, transactionId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def execute_sql(
        self,
        awsSecretStoreArn: str,
        dbClusterOrInstanceArn: str,
        sqlStatements: str,
        database: str = None,
        schema: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        continueAfterTimeout: bool = None,
        database: str = None,
        includeResultMetadata: bool = None,
        parameters: List[Any] = None,
        resultSetOptions: Dict[str, Any] = None,
        schema: str = None,
        transactionId: str = None,
    ) -> Dict[str, Any]:
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
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def rollback_transaction(
        self, resourceArn: str, secretArn: str, transactionId: str
    ) -> Dict[str, Any]:
        pass
