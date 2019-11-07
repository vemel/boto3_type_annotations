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


    def create_identity_pool(
        self,
        IdentityPoolName: str,
        AllowUnauthenticatedIdentities: bool,
        SupportedLoginProviders: Optional[Dict] = None,
        DeveloperProviderName: Optional[str] = None,
        OpenIdConnectProviderARNs: Optional[List] = None,
        CognitoIdentityProviders: Optional[List] = None,
        SamlProviderARNs: Optional[List] = None,
        IdentityPoolTags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_identities(
        self,
        IdentityIdsToDelete: List,
    ) -> Dict:
        pass


    def delete_identity_pool(
        self,
        IdentityPoolId: str,
    ):
        pass


    def describe_identity(
        self,
        IdentityId: str,
    ) -> Dict:
        pass


    def describe_identity_pool(
        self,
        IdentityPoolId: str,
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


    def get_credentials_for_identity(
        self,
        IdentityId: str,
        Logins: Optional[Dict] = None,
        CustomRoleArn: Optional[str] = None,
    ) -> Dict:
        pass


    def get_id(
        self,
        IdentityPoolId: str,
        AccountId: Optional[str] = None,
        Logins: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_identity_pool_roles(
        self,
        IdentityPoolId: str,
    ) -> Dict:
        pass


    def get_open_id_token(
        self,
        IdentityId: str,
        Logins: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_open_id_token_for_developer_identity(
        self,
        IdentityPoolId: str,
        Logins: Dict,
        IdentityId: Optional[str] = None,
        TokenDuration: Optional[int] = None,
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


    def list_identities(
        self,
        IdentityPoolId: str,
        MaxResults: int,
        NextToken: Optional[str] = None,
        HideDisabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_identity_pools(
        self,
        MaxResults: int,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def lookup_developer_identity(
        self,
        IdentityPoolId: str,
        IdentityId: Optional[str] = None,
        DeveloperUserIdentifier: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def merge_developer_identities(
        self,
        SourceUserIdentifier: str,
        DestinationUserIdentifier: str,
        DeveloperProviderName: str,
        IdentityPoolId: str,
    ) -> Dict:
        pass


    def set_identity_pool_roles(
        self,
        IdentityPoolId: str,
        Roles: Dict,
        RoleMappings: Optional[Dict] = None,
    ):
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def unlink_developer_identity(
        self,
        IdentityId: str,
        IdentityPoolId: str,
        DeveloperProviderName: str,
        DeveloperUserIdentifier: str,
    ):
        pass


    def unlink_identity(
        self,
        IdentityId: str,
        Logins: Dict,
        LoginsToRemove: List,
    ):
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: Optional[List] = None,
    ) -> Dict:
        pass


    def update_identity_pool(
        self,
        IdentityPoolId: str,
        IdentityPoolName: str,
        AllowUnauthenticatedIdentities: bool,
        SupportedLoginProviders: Optional[Dict] = None,
        DeveloperProviderName: Optional[str] = None,
        OpenIdConnectProviderARNs: Optional[List] = None,
        CognitoIdentityProviders: Optional[List] = None,
        SamlProviderARNs: Optional[List] = None,
        IdentityPoolTags: Optional[Dict] = None,
    ) -> Dict:
        pass

