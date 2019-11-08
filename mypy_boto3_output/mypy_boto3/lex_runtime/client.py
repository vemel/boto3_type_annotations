from __future__ import annotations

from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Union

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_session(
        self, botName: str, botAlias: str, userId: str
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
    def get_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        checkpointLabelFilter: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def post_content(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        contentType: str,
        inputStream: Union[bytes, IO],
        sessionAttributes: str = None,
        requestAttributes: str = None,
        accept: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def post_text(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        inputText: str,
        sessionAttributes: Dict[str, Any] = None,
        requestAttributes: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        sessionAttributes: Dict[str, Any] = None,
        dialogAction: Dict[str, Any] = None,
        recentIntentSummaryView: List[Any] = None,
        accept: str = None,
    ) -> Dict[str, Any]:
        pass
