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


    def create_http_namespace(
        self,
        Name: str,
        CreatorRequestId: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_private_dns_namespace(
        self,
        Name: str,
        Vpc: str,
        CreatorRequestId: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_public_dns_namespace(
        self,
        Name: str,
        CreatorRequestId: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_service(
        self,
        Name: str,
        NamespaceId: Optional[str] = None,
        CreatorRequestId: Optional[str] = None,
        Description: Optional[str] = None,
        DnsConfig: Optional[Dict] = None,
        HealthCheckConfig: Optional[Dict] = None,
        HealthCheckCustomConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_namespace(
        self,
        Id: str,
    ) -> Dict:
        pass


    def delete_service(
        self,
        Id: str,
    ) -> Dict:
        pass


    def deregister_instance(
        self,
        ServiceId: str,
        InstanceId: str,
    ) -> Dict:
        pass


    def discover_instances(
        self,
        NamespaceName: str,
        ServiceName: str,
        MaxResults: Optional[int] = None,
        QueryParameters: Optional[Dict] = None,
        HealthStatus: Optional[str] = None,
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


    def get_instance(
        self,
        ServiceId: str,
        InstanceId: str,
    ) -> Dict:
        pass


    def get_instances_health_status(
        self,
        ServiceId: str,
        Instances: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_namespace(
        self,
        Id: str,
    ) -> Dict:
        pass


    def get_operation(
        self,
        OperationId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_service(
        self,
        Id: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_instances(
        self,
        ServiceId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_namespaces(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_operations(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_services(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def register_instance(
        self,
        ServiceId: str,
        InstanceId: str,
        Attributes: Dict,
        CreatorRequestId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_instance_custom_health_status(
        self,
        ServiceId: str,
        InstanceId: str,
        Status: str,
    ):
        pass


    def update_service(
        self,
        Id: str,
        Service: Dict,
    ) -> Dict:
        pass

