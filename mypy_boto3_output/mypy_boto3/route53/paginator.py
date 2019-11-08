from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class ListHealthChecks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListHostedZones(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DelegationSetId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListQueryLoggingConfigs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, HostedZoneId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListResourceRecordSets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, HostedZoneId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListVPCAssociationAuthorizations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        HostedZoneId: str,
        MaxResults: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass