from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeImageScanFindings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        repositoryName: str,
        imageId: Dict[str, Any],
        registryId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeImages(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[Any] = None,
        filter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeRepositories(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        registryId: str = None,
        repositoryNames: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetLifecyclePolicyPreview(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[Any] = None,
        filter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListImages(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        filter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
