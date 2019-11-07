from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_get_traces(
        self,
        TraceIds: List,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_group(
        self,
        GroupName: str,
        FilterExpression: Optional[str] = None,
    ) -> Dict:
        pass


    def create_sampling_rule(
        self,
        SamplingRule: Dict,
    ) -> Dict:
        pass


    def delete_group(
        self,
        GroupName: Optional[str] = None,
        GroupARN: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_sampling_rule(
        self,
        RuleName: Optional[str] = None,
        RuleARN: Optional[str] = None,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_encryption_config(
        self,
    ) -> Dict:
        pass


    def get_group(
        self,
        GroupName: Optional[str] = None,
        GroupARN: Optional[str] = None,
    ) -> Dict:
        pass


    def get_groups(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_sampling_rules(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_sampling_statistic_summaries(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_sampling_targets(
        self,
        SamplingStatisticsDocuments: List,
    ) -> Dict:
        pass


    def get_service_graph(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: Optional[str] = None,
        GroupARN: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_time_series_service_statistics(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: Optional[str] = None,
        GroupARN: Optional[str] = None,
        EntitySelectorExpression: Optional[str] = None,
        Period: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_trace_graph(
        self,
        TraceIds: List,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_trace_summaries(
        self,
        StartTime: datetime,
        EndTime: datetime,
        TimeRangeType: Optional[str] = None,
        Sampling: Optional[bool] = None,
        SamplingStrategy: Optional[Dict] = None,
        FilterExpression: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def put_encryption_config(
        self,
        Type: str,
        KeyId: Optional[str] = None,
    ) -> Dict:
        pass


    def put_telemetry_records(
        self,
        TelemetryRecords: List,
        EC2InstanceId: Optional[str] = None,
        Hostname: Optional[str] = None,
        ResourceARN: Optional[str] = None,
    ) -> Dict:
        pass


    def put_trace_segments(
        self,
        TraceSegmentDocuments: List,
    ) -> Dict:
        pass


    def update_group(
        self,
        GroupName: Optional[str] = None,
        GroupARN: Optional[str] = None,
        FilterExpression: Optional[str] = None,
    ) -> Dict:
        pass


    def update_sampling_rule(
        self,
        SamplingRuleUpdate: Dict,
    ) -> Dict:
        pass

