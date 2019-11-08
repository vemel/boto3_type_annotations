from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeBackups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        BackupIds: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeFileSystems(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, FileSystemIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTagsForResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceARN: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
