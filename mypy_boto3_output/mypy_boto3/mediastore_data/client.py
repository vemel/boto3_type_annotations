from __future__ import annotations

from typing import Any
from typing import Dict
from typing import IO
from typing import Union

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_object(self, Path: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_object(self, Path: str) -> Dict[str, Any]:
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
    def get_object(self, Path: str, Range: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_items(
        self, Path: str = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_object(
        self,
        Body: Union[bytes, IO],
        Path: str,
        ContentType: str = None,
        CacheControl: str = None,
        StorageClass: str = None,
        UploadAvailability: str = None,
    ) -> Dict[str, Any]:
        pass
