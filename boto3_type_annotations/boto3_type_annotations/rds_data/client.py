from typing import Optional
from typing import Union
from botocore.waiter import Waiter
from botocore.client import BaseClient
from botocore.paginate import Paginator
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def execute_sql(self, awsSecretStoreArn: str, dbClusterOrInstanceArn: str, sqlStatements: str, database: str = None, schema: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass
