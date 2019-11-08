from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListChannels(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListDatasetContents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        datasetName: str,
        scheduledOnOrAfter: datetime = None,
        scheduledBefore: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListDatasets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListDatastores(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListPipelines(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
