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


    def create_backup(
        self,
        FileSystemId: str,
        ClientRequestToken: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_file_system(
        self,
        FileSystemType: str,
        StorageCapacity: int,
        SubnetIds: List,
        ClientRequestToken: Optional[str] = None,
        SecurityGroupIds: Optional[List] = None,
        Tags: Optional[List] = None,
        KmsKeyId: Optional[str] = None,
        WindowsConfiguration: Optional[Dict] = None,
        LustreConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_file_system_from_backup(
        self,
        BackupId: str,
        SubnetIds: List,
        ClientRequestToken: Optional[str] = None,
        SecurityGroupIds: Optional[List] = None,
        Tags: Optional[List] = None,
        WindowsConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_backup(
        self,
        BackupId: str,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: Optional[str] = None,
        WindowsConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def describe_backups(
        self,
        BackupIds: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_file_systems(
        self,
        FileSystemIds: Optional[List] = None,
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


    def list_tags_for_resource(
        self,
        ResourceARN: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceARN: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceARN: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: Optional[str] = None,
        WindowsConfiguration: Optional[Dict] = None,
        LustreConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass

