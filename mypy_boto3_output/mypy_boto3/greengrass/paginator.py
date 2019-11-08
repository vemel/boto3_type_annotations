from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListBulkDeploymentDetailedReports(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, BulkDeploymentId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListBulkDeployments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListConnectorDefinitionVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ConnectorDefinitionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListConnectorDefinitions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListCoreDefinitionVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, CoreDefinitionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListCoreDefinitions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListDeployments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, GroupId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDeviceDefinitionVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DeviceDefinitionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDeviceDefinitions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListFunctionDefinitionVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, FunctionDefinitionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListFunctionDefinitions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListGroupVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, GroupId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListLoggerDefinitionVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, LoggerDefinitionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListLoggerDefinitions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListResourceDefinitionVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceDefinitionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListResourceDefinitions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListSubscriptionDefinitionVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, SubscriptionDefinitionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSubscriptionDefinitions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
