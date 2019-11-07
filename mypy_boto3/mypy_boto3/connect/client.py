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


    def create_user(
        self,
        Username: str,
        PhoneConfig: Dict,
        SecurityProfileIds: List,
        RoutingProfileId: str,
        InstanceId: str,
        Password: Optional[str] = None,
        IdentityInfo: Optional[Dict] = None,
        DirectoryUserId: Optional[str] = None,
        HierarchyGroupId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_user(
        self,
        InstanceId: str,
        UserId: str,
    ):
        pass


    def describe_user(
        self,
        UserId: str,
        InstanceId: str,
    ) -> Dict:
        pass


    def describe_user_hierarchy_group(
        self,
        HierarchyGroupId: str,
        InstanceId: str,
    ) -> Dict:
        pass


    def describe_user_hierarchy_structure(
        self,
        InstanceId: str,
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


    def get_contact_attributes(
        self,
        InstanceId: str,
        InitialContactId: str,
    ) -> Dict:
        pass


    def get_current_metric_data(
        self,
        InstanceId: str,
        Filters: Dict,
        CurrentMetrics: List,
        Groupings: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_federation_token(
        self,
        InstanceId: str,
    ) -> Dict:
        pass


    def get_metric_data(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: Dict,
        HistoricalMetrics: List,
        Groupings: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
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


    def list_contact_flows(
        self,
        InstanceId: str,
        ContactFlowTypes: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_hours_of_operations(
        self,
        InstanceId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_phone_numbers(
        self,
        InstanceId: str,
        PhoneNumberTypes: Optional[List] = None,
        PhoneNumberCountryCodes: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_queues(
        self,
        InstanceId: str,
        QueueTypes: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_routing_profiles(
        self,
        InstanceId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_security_profiles(
        self,
        InstanceId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_user_hierarchy_groups(
        self,
        InstanceId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_users(
        self,
        InstanceId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def start_outbound_voice_contact(
        self,
        DestinationPhoneNumber: str,
        ContactFlowId: str,
        InstanceId: str,
        ClientToken: Optional[str] = None,
        SourcePhoneNumber: Optional[str] = None,
        QueueId: Optional[str] = None,
        Attributes: Optional[Dict] = None,
    ) -> Dict:
        pass


    def stop_contact(
        self,
        ContactId: str,
        InstanceId: str,
    ) -> Dict:
        pass


    def update_contact_attributes(
        self,
        InitialContactId: str,
        InstanceId: str,
        Attributes: Dict,
    ) -> Dict:
        pass


    def update_user_hierarchy(
        self,
        UserId: str,
        InstanceId: str,
        HierarchyGroupId: Optional[str] = None,
    ):
        pass


    def update_user_identity_info(
        self,
        IdentityInfo: Dict,
        UserId: str,
        InstanceId: str,
    ):
        pass


    def update_user_phone_config(
        self,
        PhoneConfig: Dict,
        UserId: str,
        InstanceId: str,
    ):
        pass


    def update_user_routing_profile(
        self,
        RoutingProfileId: str,
        UserId: str,
        InstanceId: str,
    ):
        pass


    def update_user_security_profiles(
        self,
        SecurityProfileIds: List,
        UserId: str,
        InstanceId: str,
    ):
        pass

