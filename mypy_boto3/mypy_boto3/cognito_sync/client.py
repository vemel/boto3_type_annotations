from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def bulk_publish(
        self,
        IdentityPoolId: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def delete_dataset(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
    ) -> Dict:
        pass


    def describe_dataset(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
    ) -> Dict:
        pass


    def describe_identity_pool_usage(
        self,
        IdentityPoolId: str,
    ) -> Dict:
        pass


    def describe_identity_usage(
        self,
        IdentityPoolId: str,
        IdentityId: str,
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


    def get_bulk_publish_details(
        self,
        IdentityPoolId: str,
    ) -> Dict:
        pass


    def get_cognito_events(
        self,
        IdentityPoolId: str,
    ) -> Dict:
        pass


    def get_identity_pool_configuration(
        self,
        IdentityPoolId: str,
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


    def list_datasets(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_identity_pool_usage(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_records(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        LastSyncCount: Optional[int] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        SyncSessionToken: Optional[str] = None,
    ) -> Dict:
        pass


    def register_device(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        Platform: str,
        Token: str,
    ) -> Dict:
        pass


    def set_cognito_events(
        self,
        IdentityPoolId: str,
        Events: Dict,
    ):
        pass


    def set_identity_pool_configuration(
        self,
        IdentityPoolId: str,
        PushSync: Optional[Dict] = None,
        CognitoStreams: Optional[Dict] = None,
    ) -> Dict:
        pass


    def subscribe_to_dataset(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        DeviceId: str,
    ) -> Dict:
        pass


    def unsubscribe_from_dataset(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        DeviceId: str,
    ) -> Dict:
        pass


    def update_records(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        SyncSessionToken: str,
        DeviceId: Optional[str] = None,
        RecordPatches: Optional[List] = None,
        ClientContext: Optional[str] = None,
    ) -> Dict:
        pass

