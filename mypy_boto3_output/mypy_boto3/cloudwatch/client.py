from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_alarms(self, AlarmNames: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_anomaly_detector(
        self, Namespace: str, MetricName: str, Stat: str, Dimensions: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_dashboards(self, DashboardNames: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_alarm_history(
        self,
        AlarmName: str = None,
        HistoryItemType: str = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_alarms(
        self,
        AlarmNames: List[Any] = None,
        AlarmNamePrefix: str = None,
        StateValue: str = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_alarms_for_metric(
        self,
        MetricName: str,
        Namespace: str,
        Statistic: str = None,
        ExtendedStatistic: str = None,
        Dimensions: List[Any] = None,
        Period: int = None,
        Unit: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_anomaly_detectors(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_alarm_actions(self, AlarmNames: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def enable_alarm_actions(self, AlarmNames: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_dashboard(self, DashboardName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_metric_data(
        self,
        MetricDataQueries: List[Any],
        StartTime: datetime,
        EndTime: datetime,
        NextToken: str = None,
        ScanBy: str = None,
        MaxDatapoints: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_metric_statistics(
        self,
        Namespace: str,
        MetricName: str,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        Dimensions: List[Any] = None,
        Statistics: List[Any] = None,
        ExtendedStatistics: List[Any] = None,
        Unit: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_metric_widget_image(
        self, MetricWidget: str, OutputFormat: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_dashboards(
        self, DashboardNamePrefix: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_metrics(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[Any] = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_anomaly_detector(
        self,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: List[Any] = None,
        Configuration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_dashboard(self, DashboardName: str, DashboardBody: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_metric_alarm(
        self,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: str,
        AlarmDescription: str = None,
        ActionsEnabled: bool = None,
        OKActions: List[Any] = None,
        AlarmActions: List[Any] = None,
        InsufficientDataActions: List[Any] = None,
        MetricName: str = None,
        Namespace: str = None,
        Statistic: str = None,
        ExtendedStatistic: str = None,
        Dimensions: List[Any] = None,
        Period: int = None,
        Unit: str = None,
        DatapointsToAlarm: int = None,
        Threshold: float = None,
        TreatMissingData: str = None,
        EvaluateLowSampleCountPercentile: str = None,
        Metrics: List[Any] = None,
        Tags: List[Any] = None,
        ThresholdMetricId: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def put_metric_data(self, Namespace: str, MetricData: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_alarm_state(
        self,
        AlarmName: str,
        StateValue: str,
        StateReason: str,
        StateReasonData: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass
