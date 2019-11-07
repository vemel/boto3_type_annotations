from typing import Dict
from typing import IO
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def delete_object(
        self,
        Path: str,
    ) -> Dict:
        pass


    def describe_object(
        self,
        Path: str,
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


    def get_object(
        self,
        Path: str,
        Range: Optional[str] = None,
    ) -> Dict:
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


    def list_items(
        self,
        Path: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_object(
        self,
        Body: Union[bytes, IO],
        Path: str,
        ContentType: Optional[str] = None,
        CacheControl: Optional[str] = None,
        StorageClass: Optional[str] = None,
        UploadAvailability: Optional[str] = None,
    ) -> Dict:
        pass

