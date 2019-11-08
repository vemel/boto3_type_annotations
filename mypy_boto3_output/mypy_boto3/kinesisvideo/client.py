from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_stream(
        self,
        StreamName: str,
        DeviceName: str = None,
        MediaType: str = None,
        KmsKeyId: str = None,
        DataRetentionInHours: int = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_stream(
        self, StreamARN: str, CurrentVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stream(
        self, StreamName: str = None, StreamARN: str = None
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
    def get_data_endpoint(
        self, APIName: str, StreamName: str = None, StreamARN: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_streams(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        StreamNameCondition: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_stream(
        self, NextToken: str = None, StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_stream(
        self, Tags: Dict[str, Any], StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_stream(
        self, TagKeyList: List[Any], StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_data_retention(
        self,
        CurrentVersion: str,
        Operation: str,
        DataRetentionChangeInHours: int,
        StreamName: str = None,
        StreamARN: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_stream(
        self,
        CurrentVersion: str,
        StreamName: str = None,
        StreamARN: str = None,
        DeviceName: str = None,
        MediaType: str = None,
    ) -> Dict[str, Any]:
        pass
