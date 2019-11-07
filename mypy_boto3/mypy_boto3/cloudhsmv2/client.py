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


    def copy_backup_to_region(
        self,
        DestinationRegion: str,
        BackupId: str,
    ) -> Dict:
        pass


    def create_cluster(
        self,
        SubnetIds: List,
        HsmType: str,
        SourceBackupId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_hsm(
        self,
        ClusterId: str,
        AvailabilityZone: str,
        IpAddress: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_backup(
        self,
        BackupId: str,
    ) -> Dict:
        pass


    def delete_cluster(
        self,
        ClusterId: str,
    ) -> Dict:
        pass


    def delete_hsm(
        self,
        ClusterId: str,
        HsmId: Optional[str] = None,
        EniId: Optional[str] = None,
        EniIp: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_backups(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[Dict] = None,
        SortAscending: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_clusters(
        self,
        Filters: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
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


    def initialize_cluster(
        self,
        ClusterId: str,
        SignedCert: str,
        TrustAnchor: str,
    ) -> Dict:
        pass


    def list_tags(
        self,
        ResourceId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def restore_backup(
        self,
        BackupId: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceId: str,
        TagList: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceId: str,
        TagKeyList: List,
    ) -> Dict:
        pass

