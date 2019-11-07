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
        BrokerNodeGroupInfo: Dict,
        ClusterName: str,
        KafkaVersion: str,
        NumberOfBrokerNodes: int,
        ClientAuthentication: Optional[Dict] = None,
        ConfigurationInfo: Optional[Dict] = None,
        EncryptionInfo: Optional[Dict] = None,
        EnhancedMonitoring: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_configuration(
        self,
        KafkaVersions: List,
        Name: str,
        ServerProperties: bytes,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_cluster(
        self,
        ClusterArn: str,
        CurrentVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_cluster(
        self,
        ClusterArn: str,
    ) -> Dict:
        pass


    def describe_cluster_operation(
        self,
        ClusterOperationArn: str,
    ) -> Dict:
        pass


    def describe_configuration(
        self,
        Arn: str,
    ) -> Dict:
        pass


    def describe_configuration_revision(
        self,
        Arn: str,
        Revision: int,
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


    def get_bootstrap_brokers(
        self,
        ClusterArn: str,
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


    def list_cluster_operations(
        self,
        ClusterArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_clusters(
        self,
        ClusterNameFilter: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_configuration_revisions(
        self,
        Arn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_configurations(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_nodes(
        self,
        ClusterArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Dict,
    ):
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass


    def update_broker_count(
        self,
        ClusterArn: str,
        CurrentVersion: str,
        TargetNumberOfBrokerNodes: int,
    ) -> Dict:
        pass


    def update_broker_storage(
        self,
        ClusterArn: str,
        CurrentVersion: str,
        TargetBrokerEBSVolumeInfo: List,
    ) -> Dict:
        pass


    def update_cluster_configuration(
        self,
        ClusterArn: str,
        ConfigurationInfo: Dict,
        CurrentVersion: str,
    ) -> Dict:
        pass

