from datetime import datetime
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


    def create_ledger(
        self,
        Name: str,
        PermissionsMode: str,
        Tags: Optional[Dict] = None,
        DeletionProtection: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_ledger(
        self,
        Name: str,
    ):
        pass


    def describe_journal_s3_export(
        self,
        Name: str,
        ExportId: str,
    ) -> Dict:
        pass


    def describe_ledger(
        self,
        Name: str,
    ) -> Dict:
        pass


    def export_journal_to_s3(
        self,
        Name: str,
        InclusiveStartTime: datetime,
        ExclusiveEndTime: datetime,
        S3ExportConfiguration: Dict,
        RoleArn: str,
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


    def get_block(
        self,
        Name: str,
        BlockAddress: Dict,
        DigestTipAddress: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_digest(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_revision(
        self,
        Name: str,
        BlockAddress: Dict,
        DocumentId: str,
        DigestTipAddress: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_journal_s3_exports(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_journal_s3_exports_for_ledger(
        self,
        Name: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_ledgers(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_ledger(
        self,
        Name: str,
        DeletionProtection: Optional[bool] = None,
    ) -> Dict:
        pass

