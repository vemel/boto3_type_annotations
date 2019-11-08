from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3.cloudwatch.service_resource as cloudwatch_service_resource_scope


class ServiceResource(Boto3ServiceResource):
    alarms: cloudwatch_service_resource_scope.alarms
    metrics: cloudwatch_service_resource_scope.metrics

    # pylint: disable=arguments-differ
    def Alarm(self, name: str = None) -> cloudwatch_service_resource_scope.Alarm:
        pass

    # pylint: disable=arguments-differ
    def Metric(
        self, namespace: str = None, name: str = None
    ) -> cloudwatch_service_resource_scope.Metric:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class Alarm(Boto3ServiceResource):
    alarm_name: str
    alarm_arn: str
    alarm_description: str
    alarm_configuration_updated_timestamp: datetime
    actions_enabled: bool
    ok_actions: List
    alarm_actions: List
    insufficient_data_actions: List
    state_value: str
    state_reason: str
    state_reason_data: str
    state_updated_timestamp: datetime
    metric_name: str
    namespace: str
    statistic: str
    extended_statistic: str
    dimensions: List
    period: int
    unit: str
    evaluation_periods: int
    datapoints_to_alarm: int
    threshold: float
    comparison_operator: str
    treat_missing_data: str
    evaluate_low_sample_count_percentile: str
    metrics: List
    threshold_metric_id: str
    name: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_history(
        self,
        HistoryItemType: str = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_actions(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def enable_actions(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_state(
        self, StateValue: str, StateReason: str, StateReasonData: str = None
    ) -> None:
        pass


class Metric(Boto3ServiceResource):
    metric_name: str
    dimensions: List
    namespace: str
    name: str
    alarms: cloudwatch_service_resource_scope.alarms

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def get_statistics(
        self,
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
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put_alarm(
        self,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: str,
        AlarmDescription: str = None,
        ActionsEnabled: bool = None,
        OKActions: List[Any] = None,
        AlarmActions: List[Any] = None,
        InsufficientDataActions: List[Any] = None,
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
    ) -> cloudwatch_service_resource_scope.Alarm:
        pass

    # pylint: disable=arguments-differ
    def put_data(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class alarms(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[cloudwatch_service_resource_scope.Alarm]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def delete(cls) -> None:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def disable_actions(cls) -> None:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def enable_actions(cls) -> None:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        AlarmNames: List[Any] = None,
        AlarmNamePrefix: str = None,
        StateValue: str = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> List[cloudwatch_service_resource_scope.Alarm]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[cloudwatch_service_resource_scope.Alarm]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[cloudwatch_service_resource_scope.Alarm]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class metrics(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[cloudwatch_service_resource_scope.Metric]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[Any] = None,
        NextToken: str = None,
    ) -> List[cloudwatch_service_resource_scope.Metric]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[cloudwatch_service_resource_scope.Metric]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[cloudwatch_service_resource_scope.Metric]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass
