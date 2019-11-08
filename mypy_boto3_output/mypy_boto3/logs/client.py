from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_kms_key(self, logGroupName: str, kmsKeyId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_export_task(self, taskId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_export_task(
        self,
        logGroupName: str,
        fromTime: int,
        to: int,
        destination: str,
        taskName: str = None,
        logStreamNamePrefix: str = None,
        destinationPrefix: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_log_group(
        self, logGroupName: str, kmsKeyId: str = None, tags: Dict[str, Any] = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_log_stream(self, logGroupName: str, logStreamName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_destination(self, destinationName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_log_group(self, logGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_log_stream(self, logGroupName: str, logStreamName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_metric_filter(self, logGroupName: str, filterName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_resource_policy(self, policyName: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_retention_policy(self, logGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_subscription_filter(self, logGroupName: str, filterName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_destinations(
        self,
        DestinationNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_export_tasks(
        self,
        taskId: str = None,
        statusCode: str = None,
        nextToken: str = None,
        limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_log_groups(
        self, logGroupNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_log_streams(
        self,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: str = None,
        descending: bool = None,
        nextToken: str = None,
        limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_metric_filters(
        self,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
        metricName: str = None,
        metricNamespace: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_queries(
        self,
        logGroupName: str = None,
        status: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_resource_policies(
        self, nextToken: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_subscription_filters(
        self,
        logGroupName: str,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_kms_key(self, logGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def filter_log_events(
        self,
        logGroupName: str,
        logStreamNames: List[Any] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        nextToken: str = None,
        limit: int = None,
        interleaved: bool = None,
    ) -> Dict[str, Any]:
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
    def get_log_events(
        self,
        logGroupName: str,
        logStreamName: str,
        startTime: int = None,
        endTime: int = None,
        nextToken: str = None,
        limit: int = None,
        startFromHead: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_log_group_fields(
        self, logGroupName: str, time: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_log_record(self, logRecordPointer: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_query_results(self, queryId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_tags_log_group(self, logGroupName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_destination(
        self, destinationName: str, targetArn: str, roleArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_destination_policy(self, destinationName: str, accessPolicy: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def put_log_events(
        self,
        logGroupName: str,
        logStreamName: str,
        logEvents: List[Any],
        sequenceToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_metric_filter(
        self,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        metricTransformations: List[Any],
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def put_resource_policy(
        self, policyName: str = None, policyDocument: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_retention_policy(self, logGroupName: str, retentionInDays: int) -> None:
        pass

    # pylint: disable=arguments-differ
    def put_subscription_filter(
        self,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        destinationArn: str,
        roleArn: str = None,
        distribution: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def start_query(
        self,
        startTime: int,
        endTime: int,
        queryString: str,
        logGroupName: str = None,
        logGroupNames: List[Any] = None,
        limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_query(self, queryId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_log_group(self, logGroupName: str, tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def test_metric_filter(
        self, filterPattern: str, logEventMessages: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_log_group(self, logGroupName: str, tags: List[Any]) -> None:
        pass
