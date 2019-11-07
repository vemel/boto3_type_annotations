from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
        PolicyArns: Optional[List] = None,
        Policy: Optional[str] = None,
        DurationSeconds: Optional[int] = None,
        ExternalId: Optional[str] = None,
        SerialNumber: Optional[str] = None,
        TokenCode: Optional[str] = None,
    ) -> Dict:
        pass


    def assume_role_with_saml(
        self,
        RoleArn: str,
        PrincipalArn: str,
        SAMLAssertion: str,
        PolicyArns: Optional[List] = None,
        Policy: Optional[str] = None,
        DurationSeconds: Optional[int] = None,
    ) -> Dict:
        pass


    def assume_role_with_web_identity(
        self,
        RoleArn: str,
        RoleSessionName: str,
        WebIdentityToken: str,
        ProviderId: Optional[str] = None,
        PolicyArns: Optional[List] = None,
        Policy: Optional[str] = None,
        DurationSeconds: Optional[int] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def decode_authorization_message(
        self,
        EncodedMessage: str,
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


    def get_access_key_info(
        self,
        AccessKeyId: str,
    ) -> Dict:
        pass


    def get_caller_identity(
        self,
    ) -> Dict:
        pass


    def get_federation_token(
        self,
        Name: str,
        Policy: Optional[str] = None,
        PolicyArns: Optional[List] = None,
        DurationSeconds: Optional[int] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_session_token(
        self,
        DurationSeconds: Optional[int] = None,
        SerialNumber: Optional[str] = None,
        TokenCode: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass

