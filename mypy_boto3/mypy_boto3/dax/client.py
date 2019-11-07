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


    def create_cluster(
        self,
        ClusterName: str,
        NodeType: str,
        ReplicationFactor: int,
        IamRoleArn: str,
        Description: Optional[str] = None,
        AvailabilityZones: Optional[List] = None,
        SubnetGroupName: Optional[str] = None,
        SecurityGroupIds: Optional[List] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        NotificationTopicArn: Optional[str] = None,
        ParameterGroupName: Optional[str] = None,
        Tags: Optional[List] = None,
        SSESpecification: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_parameter_group(
        self,
        ParameterGroupName: str,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_subnet_group(
        self,
        SubnetGroupName: str,
        SubnetIds: List,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def decrease_replication_factor(
        self,
        ClusterName: str,
        NewReplicationFactor: int,
        AvailabilityZones: Optional[List] = None,
        NodeIdsToRemove: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_cluster(
        self,
        ClusterName: str,
    ) -> Dict:
        pass


    def delete_parameter_group(
        self,
        ParameterGroupName: str,
    ) -> Dict:
        pass


    def delete_subnet_group(
        self,
        SubnetGroupName: str,
    ) -> Dict:
        pass


    def describe_clusters(
        self,
        ClusterNames: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_default_parameters(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_events(
        self,
        SourceName: Optional[str] = None,
        SourceType: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        Duration: Optional[int] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_parameter_groups(
        self,
        ParameterGroupNames: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_parameters(
        self,
        ParameterGroupName: str,
        Source: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_subnet_groups(
        self,
        SubnetGroupNames: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
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


    def increase_replication_factor(
        self,
        ClusterName: str,
        NewReplicationFactor: int,
        AvailabilityZones: Optional[List] = None,
    ) -> Dict:
        pass


    def list_tags(
        self,
        ResourceName: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def reboot_node(
        self,
        ClusterName: str,
        NodeId: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceName: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceName: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_cluster(
        self,
        ClusterName: str,
        Description: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        NotificationTopicArn: Optional[str] = None,
        NotificationTopicStatus: Optional[str] = None,
        ParameterGroupName: Optional[str] = None,
        SecurityGroupIds: Optional[List] = None,
    ) -> Dict:
        pass


    def update_parameter_group(
        self,
        ParameterGroupName: str,
        ParameterNameValues: List,
    ) -> Dict:
        pass


    def update_subnet_group(
        self,
        SubnetGroupName: str,
        Description: Optional[str] = None,
        SubnetIds: Optional[List] = None,
    ) -> Dict:
        pass

