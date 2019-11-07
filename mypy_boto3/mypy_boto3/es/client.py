from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags(
        self,
        ARN: str,
        TagList: List,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_elasticsearch_service_software_update(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def create_elasticsearch_domain(
        self,
        DomainName: str,
        ElasticsearchVersion: Optional[str] = None,
        ElasticsearchClusterConfig: Optional[Dict] = None,
        EBSOptions: Optional[Dict] = None,
        AccessPolicies: Optional[str] = None,
        SnapshotOptions: Optional[Dict] = None,
        VPCOptions: Optional[Dict] = None,
        CognitoOptions: Optional[Dict] = None,
        EncryptionAtRestOptions: Optional[Dict] = None,
        NodeToNodeEncryptionOptions: Optional[Dict] = None,
        AdvancedOptions: Optional[Dict] = None,
        LogPublishingOptions: Optional[Dict] = None,
        DomainEndpointOptions: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_elasticsearch_domain(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def delete_elasticsearch_service_role(
        self,
    ):
        pass


    def describe_elasticsearch_domain(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def describe_elasticsearch_domain_config(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def describe_elasticsearch_domains(
        self,
        DomainNames: List,
    ) -> Dict:
        pass


    def describe_elasticsearch_instance_type_limits(
        self,
        InstanceType: str,
        ElasticsearchVersion: str,
        DomainName: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_reserved_elasticsearch_instance_offerings(
        self,
        ReservedElasticsearchInstanceOfferingId: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_reserved_elasticsearch_instances(
        self,
        ReservedElasticsearchInstanceId: Optional[str] = None,
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


    def get_compatible_elasticsearch_versions(
        self,
        DomainName: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_upgrade_history(
        self,
        DomainName: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_upgrade_status(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_domain_names(
        self,
    ) -> Dict:
        pass


    def list_elasticsearch_instance_types(
        self,
        ElasticsearchVersion: str,
        DomainName: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_elasticsearch_versions(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags(
        self,
        ARN: str,
    ) -> Dict:
        pass


    def purchase_reserved_elasticsearch_instance_offering(
        self,
        ReservedElasticsearchInstanceOfferingId: str,
        ReservationName: str,
        InstanceCount: Optional[int] = None,
    ) -> Dict:
        pass


    def remove_tags(
        self,
        ARN: str,
        TagKeys: List,
    ):
        pass


    def start_elasticsearch_service_software_update(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def update_elasticsearch_domain_config(
        self,
        DomainName: str,
        ElasticsearchClusterConfig: Optional[Dict] = None,
        EBSOptions: Optional[Dict] = None,
        SnapshotOptions: Optional[Dict] = None,
        VPCOptions: Optional[Dict] = None,
        CognitoOptions: Optional[Dict] = None,
        AdvancedOptions: Optional[Dict] = None,
        AccessPolicies: Optional[str] = None,
        LogPublishingOptions: Optional[Dict] = None,
        DomainEndpointOptions: Optional[Dict] = None,
    ) -> Dict:
        pass


    def upgrade_elasticsearch_domain(
        self,
        DomainName: str,
        TargetVersion: str,
        PerformCheckOnly: Optional[bool] = None,
    ) -> Dict:
        pass

