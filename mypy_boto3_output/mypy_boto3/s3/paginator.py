from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListMultipartUploads(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListObjectVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListObjects(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        RequestPayer: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListObjectsV2(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        FetchOwner: bool = None,
        StartAfter: str = None,
        RequestPayer: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListParts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
