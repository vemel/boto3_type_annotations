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
    def create_cluster(
        self,
        ClusterName: str,
        NodeType: str,
        ReplicationFactor: int,
        IamRoleArn: str,
        Description: str = None,
        AvailabilityZones: List[Any] = None,
        SubnetGroupName: str = None,
        SecurityGroupIds: List[Any] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        ParameterGroupName: str = None,
        Tags: List[Any] = None,
        SSESpecification: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_parameter_group(
        self, ParameterGroupName: str, Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_subnet_group(
        self, SubnetGroupName: str, SubnetIds: List[Any], Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def decrease_replication_factor(
        self,
        ClusterName: str,
        NewReplicationFactor: int,
        AvailabilityZones: List[Any] = None,
        NodeIdsToRemove: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_cluster(self, ClusterName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_parameter_group(self, ParameterGroupName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_subnet_group(self, SubnetGroupName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_clusters(
        self,
        ClusterNames: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_default_parameters(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_events(
        self,
        SourceName: str = None,
        SourceType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_parameter_groups(
        self,
        ParameterGroupNames: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_parameters(
        self,
        ParameterGroupName: str,
        Source: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_subnet_groups(
        self,
        SubnetGroupNames: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
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
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def increase_replication_factor(
        self,
        ClusterName: str,
        NewReplicationFactor: int,
        AvailabilityZones: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags(self, ResourceName: str, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot_node(self, ClusterName: str, NodeId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceName: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceName: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_cluster(
        self,
        ClusterName: str,
        Description: str = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        NotificationTopicStatus: str = None,
        ParameterGroupName: str = None,
        SecurityGroupIds: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_parameter_group(
        self, ParameterGroupName: str, ParameterNameValues: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_subnet_group(
        self, SubnetGroupName: str, Description: str = None, SubnetIds: List[Any] = None
    ) -> Dict[str, Any]:
        pass
