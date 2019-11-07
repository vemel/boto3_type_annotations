from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def delete_alarms(
        self,
        AlarmNames: List,
    ):
        pass


    def delete_anomaly_detector(
        self,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_dashboards(
        self,
        DashboardNames: List,
    ) -> Dict:
        pass


    def describe_alarm_history(
        self,
        AlarmName: Optional[str] = None,
        HistoryItemType: Optional[str] = None,
        StartDate: Optional[datetime] = None,
        EndDate: Optional[datetime] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_alarms(
        self,
        AlarmNames: Optional[List] = None,
        AlarmNamePrefix: Optional[str] = None,
        StateValue: Optional[str] = None,
        ActionPrefix: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_alarms_for_metric(
        self,
        MetricName: str,
        Namespace: str,
        Statistic: Optional[str] = None,
        ExtendedStatistic: Optional[str] = None,
        Dimensions: Optional[List] = None,
        Period: Optional[int] = None,
        Unit: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_anomaly_detectors(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Namespace: Optional[str] = None,
        MetricName: Optional[str] = None,
        Dimensions: Optional[List] = None,
    ) -> Dict:
        pass


    def disable_alarm_actions(
        self,
        AlarmNames: List,
    ):
        pass


    def enable_alarm_actions(
        self,
        AlarmNames: List,
    ):
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_dashboard(
        self,
        DashboardName: str,
    ) -> Dict:
        pass


    def get_metric_data(
        self,
        MetricDataQueries: List,
        StartTime: datetime,
        EndTime: datetime,
        NextToken: Optional[str] = None,
        ScanBy: Optional[str] = None,
        MaxDatapoints: Optional[int] = None,
    ) -> Dict:
        pass


    def get_metric_statistics(
        self,
        Namespace: str,
        MetricName: str,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        Dimensions: Optional[List] = None,
        Statistics: Optional[List] = None,
        ExtendedStatistics: Optional[List] = None,
        Unit: Optional[str] = None,
    ) -> Dict:
        pass


    def get_metric_widget_image(
        self,
        MetricWidget: str,
        OutputFormat: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_dashboards(
        self,
        DashboardNamePrefix: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_metrics(
        self,
        Namespace: Optional[str] = None,
        MetricName: Optional[str] = None,
        Dimensions: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceARN: str,
    ) -> Dict:
        pass


    def put_anomaly_detector(
        self,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: Optional[List] = None,
        Configuration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def put_dashboard(
        self,
        DashboardName: str,
        DashboardBody: str,
    ) -> Dict:
        pass


    def put_metric_alarm(
        self,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: str,
        AlarmDescription: Optional[str] = None,
        ActionsEnabled: Optional[bool] = None,
        OKActions: Optional[List] = None,
        AlarmActions: Optional[List] = None,
        InsufficientDataActions: Optional[List] = None,
        MetricName: Optional[str] = None,
        Namespace: Optional[str] = None,
        Statistic: Optional[str] = None,
        ExtendedStatistic: Optional[str] = None,
        Dimensions: Optional[List] = None,
        Period: Optional[int] = None,
        Unit: Optional[str] = None,
        DatapointsToAlarm: Optional[int] = None,
        Threshold: Optional[float] = None,
        TreatMissingData: Optional[str] = None,
        EvaluateLowSampleCountPercentile: Optional[str] = None,
        Metrics: Optional[List] = None,
        Tags: Optional[List] = None,
        ThresholdMetricId: Optional[str] = None,
    ):
        pass


    def put_metric_data(
        self,
        Namespace: str,
        MetricData: List,
    ):
        pass


    def set_alarm_state(
        self,
        AlarmName: str,
        StateValue: str,
        StateReason: str,
        StateReasonData: Optional[str] = None,
    ):
        pass


    def tag_resource(
        self,
        ResourceARN: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceARN: str,
        TagKeys: List,
    ) -> Dict:
        pass

