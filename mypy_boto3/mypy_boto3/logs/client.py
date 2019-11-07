from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_kms_key(
        self,
        logGroupName: str,
        kmsKeyId: str,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_export_task(
        self,
        taskId: str,
    ):
        pass


    def create_export_task(
        self,
        logGroupName: str,
        fromTime: int,
        to: int,
        destination: str,
        taskName: Optional[str] = None,
        logStreamNamePrefix: Optional[str] = None,
        destinationPrefix: Optional[str] = None,
    ) -> Dict:
        pass


    def create_log_group(
        self,
        logGroupName: str,
        kmsKeyId: Optional[str] = None,
        tags: Optional[Dict] = None,
    ):
        pass


    def create_log_stream(
        self,
        logGroupName: str,
        logStreamName: str,
    ):
        pass


    def delete_destination(
        self,
        destinationName: str,
    ):
        pass


    def delete_log_group(
        self,
        logGroupName: str,
    ):
        pass


    def delete_log_stream(
        self,
        logGroupName: str,
        logStreamName: str,
    ):
        pass


    def delete_metric_filter(
        self,
        logGroupName: str,
        filterName: str,
    ):
        pass


    def delete_resource_policy(
        self,
        policyName: Optional[str] = None,
    ):
        pass


    def delete_retention_policy(
        self,
        logGroupName: str,
    ):
        pass


    def delete_subscription_filter(
        self,
        logGroupName: str,
        filterName: str,
    ):
        pass


    def describe_destinations(
        self,
        DestinationNamePrefix: Optional[str] = None,
        nextToken: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_export_tasks(
        self,
        taskId: Optional[str] = None,
        statusCode: Optional[str] = None,
        nextToken: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_log_groups(
        self,
        logGroupNamePrefix: Optional[str] = None,
        nextToken: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_log_streams(
        self,
        logGroupName: str,
        logStreamNamePrefix: Optional[str] = None,
        orderBy: Optional[str] = None,
        descending: Optional[bool] = None,
        nextToken: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_metric_filters(
        self,
        logGroupName: Optional[str] = None,
        filterNamePrefix: Optional[str] = None,
        nextToken: Optional[str] = None,
        limit: Optional[int] = None,
        metricName: Optional[str] = None,
        metricNamespace: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_queries(
        self,
        logGroupName: Optional[str] = None,
        status: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_resource_policies(
        self,
        nextToken: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_subscription_filters(
        self,
        logGroupName: str,
        filterNamePrefix: Optional[str] = None,
        nextToken: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def disassociate_kms_key(
        self,
        logGroupName: str,
    ):
        pass


    def filter_log_events(
        self,
        logGroupName: str,
        logStreamNames: Optional[List] = None,
        logStreamNamePrefix: Optional[str] = None,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        filterPattern: Optional[str] = None,
        nextToken: Optional[str] = None,
        limit: Optional[int] = None,
        interleaved: Optional[bool] = None,
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


    def get_log_events(
        self,
        logGroupName: str,
        logStreamName: str,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        nextToken: Optional[str] = None,
        limit: Optional[int] = None,
        startFromHead: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_log_group_fields(
        self,
        logGroupName: str,
        time: Optional[int] = None,
    ) -> Dict:
        pass


    def get_log_record(
        self,
        logRecordPointer: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_query_results(
        self,
        queryId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_tags_log_group(
        self,
        logGroupName: str,
    ) -> Dict:
        pass


    def put_destination(
        self,
        destinationName: str,
        targetArn: str,
        roleArn: str,
    ) -> Dict:
        pass


    def put_destination_policy(
        self,
        destinationName: str,
        accessPolicy: str,
    ):
        pass


    def put_log_events(
        self,
        logGroupName: str,
        logStreamName: str,
        logEvents: List,
        sequenceToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_metric_filter(
        self,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        metricTransformations: List,
    ):
        pass


    def put_resource_policy(
        self,
        policyName: Optional[str] = None,
        policyDocument: Optional[str] = None,
    ) -> Dict:
        pass


    def put_retention_policy(
        self,
        logGroupName: str,
        retentionInDays: int,
    ):
        pass


    def put_subscription_filter(
        self,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        destinationArn: str,
        roleArn: Optional[str] = None,
        distribution: Optional[str] = None,
    ):
        pass


    def start_query(
        self,
        startTime: int,
        endTime: int,
        queryString: str,
        logGroupName: Optional[str] = None,
        logGroupNames: Optional[List] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def stop_query(
        self,
        queryId: str,
    ) -> Dict:
        pass


    def tag_log_group(
        self,
        logGroupName: str,
        tags: Dict,
    ):
        pass


    def test_metric_filter(
        self,
        filterPattern: str,
        logEventMessages: List,
    ) -> Dict:
        pass


    def untag_log_group(
        self,
        logGroupName: str,
        tags: List,
    ):
        pass

