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


    def delete_terminology(
        self,
        Name: str,
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


    def get_terminology(
        self,
        Name: str,
        TerminologyDataFormat: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def import_terminology(
        self,
        Name: str,
        MergeStrategy: str,
        TerminologyData: Dict,
        Description: Optional[str] = None,
        EncryptionKey: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_terminologies(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def translate_text(
        self,
        Text: str,
        SourceLanguageCode: str,
        TargetLanguageCode: str,
        TerminologyNames: Optional[List] = None,
    ) -> Dict:
        pass

