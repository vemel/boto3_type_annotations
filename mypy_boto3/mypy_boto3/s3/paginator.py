from __future__ import annotations

from typing import Any
from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListMultipartUploads(Paginator):
    def paginate(
        self,
        Bucket: str,
        Delimiter: Optional[str] = None,
        EncodingType: Optional[str] = None,
        Prefix: Optional[str] = None,
        PaginationConfig: Optional[Dict[str, Any]] = None,
    ) -> Dict:
        pass



class ListObjectVersions(Paginator):
    def paginate(
        self,
        Bucket: str,
        Delimiter: Optional[str] = None,
        EncodingType: Optional[str] = None,
        Prefix: Optional[str] = None,
        PaginationConfig: Optional[Dict[str, Any]] = None,
    ) -> Dict:
        pass



class ListObjects(Paginator):
    def paginate(
        self,
        Bucket: str,
        Delimiter: Optional[str] = None,
        EncodingType: Optional[str] = None,
        Prefix: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PaginationConfig: Optional[Dict[str, Any]] = None,
    ) -> Dict:
        pass



class ListObjectsV2(Paginator):
    def paginate(
        self,
        Bucket: str,
        Delimiter: Optional[str] = None,
        EncodingType: Optional[str] = None,
        Prefix: Optional[str] = None,
        FetchOwner: Optional[bool] = None,
        StartAfter: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PaginationConfig: Optional[Dict[str, Any]] = None,
    ) -> Dict:
        pass



class ListParts(Paginator):
    def paginate(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: Optional[str] = None,
        PaginationConfig: Optional[Dict[str, Any]] = None,
    ) -> Dict:
        pass

