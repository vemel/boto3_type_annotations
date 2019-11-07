from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeFleetAttributes(Paginator):
    def paginate(
        self,
        FleetIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeFleetCapacity(Paginator):
    def paginate(
        self,
        FleetIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeFleetEvents(Paginator):
    def paginate(
        self,
        FleetId: str,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeFleetUtilization(Paginator):
    def paginate(
        self,
        FleetIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeGameSessionDetails(Paginator):
    def paginate(
        self,
        FleetId: Optional[str] = None,
        GameSessionId: Optional[str] = None,
        AliasId: Optional[str] = None,
        StatusFilter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeGameSessionQueues(Paginator):
    def paginate(
        self,
        Names: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeGameSessions(Paginator):
    def paginate(
        self,
        FleetId: Optional[str] = None,
        GameSessionId: Optional[str] = None,
        AliasId: Optional[str] = None,
        StatusFilter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInstances(Paginator):
    def paginate(
        self,
        FleetId: str,
        InstanceId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMatchmakingConfigurations(Paginator):
    def paginate(
        self,
        Names: Optional[List] = None,
        RuleSetName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMatchmakingRuleSets(Paginator):
    def paginate(
        self,
        Names: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribePlayerSessions(Paginator):
    def paginate(
        self,
        GameSessionId: Optional[str] = None,
        PlayerId: Optional[str] = None,
        PlayerSessionId: Optional[str] = None,
        PlayerSessionStatusFilter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeScalingPolicies(Paginator):
    def paginate(
        self,
        FleetId: str,
        StatusFilter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAliases(Paginator):
    def paginate(
        self,
        RoutingStrategyType: Optional[str] = None,
        Name: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListBuilds(Paginator):
    def paginate(
        self,
        Status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListFleets(Paginator):
    def paginate(
        self,
        BuildId: Optional[str] = None,
        ScriptId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchGameSessions(Paginator):
    def paginate(
        self,
        FleetId: Optional[str] = None,
        AliasId: Optional[str] = None,
        FilterExpression: Optional[str] = None,
        SortExpression: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

