from typing import Dict
from typing import IO
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


    def delete_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
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


    def get_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        checkpointLabelFilter: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def post_content(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        contentType: str,
        inputStream: Union[bytes, IO],
        sessionAttributes: Optional[str] = None,
        requestAttributes: Optional[str] = None,
        accept: Optional[str] = None,
    ) -> Dict:
        pass


    def post_text(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        inputText: str,
        sessionAttributes: Optional[Dict] = None,
        requestAttributes: Optional[Dict] = None,
    ) -> Dict:
        pass


    def put_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        sessionAttributes: Optional[Dict] = None,
        dialogAction: Optional[Dict] = None,
        recentIntentSummaryView: Optional[List] = None,
        accept: Optional[str] = None,
    ) -> Dict:
        pass

