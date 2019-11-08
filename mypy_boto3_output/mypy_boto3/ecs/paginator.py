from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListAccountSettings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        name: str = None,
        value: str = None,
        principalArn: str = None,
        effectiveSettings: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAttributes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        targetType: str,
        cluster: str = None,
        attributeName: str = None,
        attributeValue: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListContainerInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        cluster: str = None,
        filter: str = None,
        status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListServices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        cluster: str = None,
        launchType: str = None,
        schedulingStrategy: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTaskDefinitionFamilies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        familyPrefix: str = None,
        status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTaskDefinitions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        familyPrefix: str = None,
        status: str = None,
        sort: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        cluster: str = None,
        containerInstance: str = None,
        family: str = None,
        startedBy: str = None,
        serviceName: str = None,
        desiredStatus: str = None,
        launchType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
