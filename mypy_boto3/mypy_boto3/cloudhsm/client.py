from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags_to_resource(
        self,
        ResourceArn: str,
        TagList: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_hapg(
        self,
        Label: str,
    ) -> Dict:
        pass


    def create_hsm(
        self,
        SubnetId: str,
        SshKey: str,
        IamRoleArn: str,
        SubscriptionType: str,
        EniIp: Optional[str] = None,
        ExternalId: Optional[str] = None,
        ClientToken: Optional[str] = None,
        SyslogIp: Optional[str] = None,
    ) -> Dict:
        pass


    def create_luna_client(
        self,
        Certificate: str,
        Label: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_hapg(
        self,
        HapgArn: str,
    ) -> Dict:
        pass


    def delete_hsm(
        self,
        HsmArn: str,
    ) -> Dict:
        pass


    def delete_luna_client(
        self,
        ClientArn: str,
    ) -> Dict:
        pass


    def describe_hapg(
        self,
        HapgArn: str,
    ) -> Dict:
        pass


    def describe_hsm(
        self,
        HsmArn: Optional[str] = None,
        HsmSerialNumber: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_luna_client(
        self,
        ClientArn: Optional[str] = None,
        CertificateFingerprint: Optional[str] = None,
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


    def get_config(
        self,
        ClientArn: str,
        ClientVersion: str,
        HapgList: List,
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


    def list_available_zones(
        self,
    ) -> Dict:
        pass


    def list_hapgs(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_hsms(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_luna_clients(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def modify_hapg(
        self,
        HapgArn: str,
        Label: Optional[str] = None,
        PartitionSerialList: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_hsm(
        self,
        HsmArn: str,
        SubnetId: Optional[str] = None,
        EniIp: Optional[str] = None,
        IamRoleArn: Optional[str] = None,
        ExternalId: Optional[str] = None,
        SyslogIp: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_luna_client(
        self,
        ClientArn: str,
        Certificate: str,
    ) -> Dict:
        pass


    def remove_tags_from_resource(
        self,
        ResourceArn: str,
        TagKeyList: List,
    ) -> Dict:
        pass

