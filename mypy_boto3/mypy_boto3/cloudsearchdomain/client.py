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


    def search(
        self,
        query: str,
        cursor: Optional[str] = None,
        expr: Optional[str] = None,
        facet: Optional[str] = None,
        filterQuery: Optional[str] = None,
        highlight: Optional[str] = None,
        partial: Optional[bool] = None,
        queryOptions: Optional[str] = None,
        queryParser: Optional[str] = None,
        returnFields: Optional[str] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        start: Optional[int] = None,
        stats: Optional[str] = None,
    ) -> Dict:
        pass


    def suggest(
        self,
        query: str,
        suggester: str,
        size: Optional[int] = None,
    ) -> Dict:
        pass


    def upload_documents(
        self,
        documents: Union[bytes, IO],
        contentType: str,
    ) -> Dict:
        pass

