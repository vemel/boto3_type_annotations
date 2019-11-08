from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class BucketExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, Bucket: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class BucketNotExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, Bucket: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class ObjectExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Bucket: str,
        Key: str,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: str = None,
        PartNumber: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ObjectNotExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Bucket: str,
        Key: str,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: str = None,
        PartNumber: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
