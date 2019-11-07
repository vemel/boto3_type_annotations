from datetime import datetime
from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class BucketExists(Waiter):
    def wait(
        self,
        Bucket: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class BucketNotExists(Waiter):
    def wait(
        self,
        Bucket: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ObjectExists(Waiter):
    def wait(
        self,
        Bucket: str,
        Key: str,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        VersionId: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ObjectNotExists(Waiter):
    def wait(
        self,
        Bucket: str,
        Key: str,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        VersionId: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

