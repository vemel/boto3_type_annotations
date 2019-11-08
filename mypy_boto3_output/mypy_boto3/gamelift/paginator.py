from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeFleetAttributes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, FleetIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeFleetCapacity(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, FleetIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeFleetEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        FleetId: str,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeFleetUtilization(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, FleetIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeGameSessionDetails(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        StatusFilter: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeGameSessionQueues(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Names: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeGameSessions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        StatusFilter: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        FleetId: str,
        InstanceId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMatchmakingConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Names: List[Any] = None,
        RuleSetName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMatchmakingRuleSets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Names: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribePlayerSessions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        GameSessionId: str = None,
        PlayerId: str = None,
        PlayerSessionId: str = None,
        PlayerSessionStatusFilter: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeScalingPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        FleetId: str,
        StatusFilter: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAliases(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        RoutingStrategyType: str = None,
        Name: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListBuilds(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Status: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListFleets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        BuildId: str = None,
        ScriptId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class SearchGameSessions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        FleetId: str = None,
        AliasId: str = None,
        FilterExpression: str = None,
        SortExpression: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
