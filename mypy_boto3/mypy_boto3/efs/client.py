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


    def create_file_system(
        self,
        CreationToken: str,
        PerformanceMode: Optional[str] = None,
        Encrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
        ThroughputMode: Optional[str] = None,
        ProvisionedThroughputInMibps: Optional[float] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_mount_target(
        self,
        FileSystemId: str,
        SubnetId: str,
        IpAddress: Optional[str] = None,
        SecurityGroups: Optional[List] = None,
    ) -> Dict:
        pass


    def create_tags(
        self,
        FileSystemId: str,
        Tags: List,
    ):
        pass


    def delete_file_system(
        self,
        FileSystemId: str,
    ):
        pass


    def delete_mount_target(
        self,
        MountTargetId: str,
    ):
        pass


    def delete_tags(
        self,
        FileSystemId: str,
        TagKeys: List,
    ):
        pass


    def describe_file_systems(
        self,
        MaxItems: Optional[int] = None,
        Marker: Optional[str] = None,
        CreationToken: Optional[str] = None,
        FileSystemId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_lifecycle_configuration(
        self,
        FileSystemId: str,
    ) -> Dict:
        pass


    def describe_mount_target_security_groups(
        self,
        MountTargetId: str,
    ) -> Dict:
        pass


    def describe_mount_targets(
        self,
        MaxItems: Optional[int] = None,
        Marker: Optional[str] = None,
        FileSystemId: Optional[str] = None,
        MountTargetId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_tags(
        self,
        FileSystemId: str,
        MaxItems: Optional[int] = None,
        Marker: Optional[str] = None,
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


    def modify_mount_target_security_groups(
        self,
        MountTargetId: str,
        SecurityGroups: Optional[List] = None,
    ):
        pass


    def put_lifecycle_configuration(
        self,
        FileSystemId: str,
        LifecyclePolicies: List,
    ) -> Dict:
        pass


    def update_file_system(
        self,
        FileSystemId: str,
        ThroughputMode: Optional[str] = None,
        ProvisionedThroughputInMibps: Optional[float] = None,
    ) -> Dict:
        pass

