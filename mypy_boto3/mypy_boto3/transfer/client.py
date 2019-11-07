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


    def create_server(
        self,
        EndpointDetails: Optional[Dict] = None,
        EndpointType: Optional[str] = None,
        HostKey: Optional[str] = None,
        IdentityProviderDetails: Optional[Dict] = None,
        IdentityProviderType: Optional[str] = None,
        LoggingRole: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_user(
        self,
        Role: str,
        ServerId: str,
        UserName: str,
        HomeDirectory: Optional[str] = None,
        HomeDirectoryType: Optional[str] = None,
        HomeDirectoryMappings: Optional[List] = None,
        Policy: Optional[str] = None,
        SshPublicKeyBody: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_server(
        self,
        ServerId: str,
    ):
        pass


    def delete_ssh_public_key(
        self,
        ServerId: str,
        SshPublicKeyId: str,
        UserName: str,
    ):
        pass


    def delete_user(
        self,
        ServerId: str,
        UserName: str,
    ):
        pass


    def describe_server(
        self,
        ServerId: str,
    ) -> Dict:
        pass


    def describe_user(
        self,
        ServerId: str,
        UserName: str,
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


    def import_ssh_public_key(
        self,
        ServerId: str,
        SshPublicKeyBody: str,
        UserName: str,
    ) -> Dict:
        pass


    def list_servers(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        Arn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_users(
        self,
        ServerId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def start_server(
        self,
        ServerId: str,
    ):
        pass


    def stop_server(
        self,
        ServerId: str,
    ):
        pass


    def tag_resource(
        self,
        Arn: str,
        Tags: List,
    ):
        pass


    def test_identity_provider(
        self,
        ServerId: str,
        UserName: str,
        UserPassword: Optional[str] = None,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        Arn: str,
        TagKeys: List,
    ):
        pass


    def update_server(
        self,
        ServerId: str,
        EndpointDetails: Optional[Dict] = None,
        EndpointType: Optional[str] = None,
        HostKey: Optional[str] = None,
        IdentityProviderDetails: Optional[Dict] = None,
        LoggingRole: Optional[str] = None,
    ) -> Dict:
        pass


    def update_user(
        self,
        ServerId: str,
        UserName: str,
        HomeDirectory: Optional[str] = None,
        HomeDirectoryType: Optional[str] = None,
        HomeDirectoryMappings: Optional[List] = None,
        Policy: Optional[str] = None,
        Role: Optional[str] = None,
    ) -> Dict:
        pass

