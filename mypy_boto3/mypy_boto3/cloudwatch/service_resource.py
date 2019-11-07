from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from boto3.resources.base import ServiceResource
from boto3.resources.collection import ResourceCollection


class ServiceResource(base.ServiceResource):
    alarms: 'alarms'
    metrics: 'metrics'

    def Alarm(
        self,
        name: Optional[str] = None,
    ) -> 'Alarm':
        pass


    def Metric(
        self,
        namespace: Optional[str] = None,
        name: Optional[str] = None,
    ) -> 'Metric':
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass



class Alarm(base.ServiceResource):
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

    def delete(
        self,
    ):
        pass


    def describe_history(
        self,
        HistoryItemType: Optional[str] = None,
        StartDate: Optional[datetime] = None,
        EndDate: Optional[datetime] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def disable_actions(
        self,
    ):
        pass


    def enable_actions(
        self,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass


    def set_state(
        self,
        StateValue: str,
        StateReason: str,
        StateReasonData: Optional[str] = None,
    ):
        pass



class Metric(base.ServiceResource):
    metric_name: str
    dimensions: List
    namespace: str
    name: str
    alarms: 'alarms'

    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def get_statistics(
        self,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        Dimensions: Optional[List] = None,
        Statistics: Optional[List] = None,
        ExtendedStatistics: Optional[List] = None,
        Unit: Optional[str] = None,
    ) -> Dict:
        pass


    def load(
        self,
    ):
        pass


    def put_alarm(
        self,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: str,
        AlarmDescription: Optional[str] = None,
        ActionsEnabled: Optional[bool] = None,
        OKActions: Optional[List] = None,
        AlarmActions: Optional[List] = None,
        InsufficientDataActions: Optional[List] = None,
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
    ) -> 'Alarm':
        pass


    def put_data(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class alarms(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Alarm']:
        pass


    @classmethod
    def delete(
        cls,
    ):
        pass


    @classmethod
    def disable_actions(
        cls,
    ):
        pass


    @classmethod
    def enable_actions(
        cls,
    ):
        pass


    @classmethod
    def filter(
        cls,
        AlarmNames: Optional[List] = None,
        AlarmNamePrefix: Optional[str] = None,
        StateValue: Optional[str] = None,
        ActionPrefix: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> List['Alarm']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Alarm']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Alarm']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class metrics(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Metric']:
        pass


    @classmethod
    def filter(
        cls,
        Namespace: Optional[str] = None,
        MetricName: Optional[str] = None,
        Dimensions: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> List['Metric']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Metric']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Metric']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass

