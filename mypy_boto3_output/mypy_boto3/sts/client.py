from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
        PolicyArns: List[Any] = None,
        Policy: str = None,
        DurationSeconds: int = None,
        ExternalId: str = None,
        SerialNumber: str = None,
        TokenCode: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def assume_role_with_saml(
        self,
        RoleArn: str,
        PrincipalArn: str,
        SAMLAssertion: str,
        PolicyArns: List[Any] = None,
        Policy: str = None,
        DurationSeconds: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def assume_role_with_web_identity(
        self,
        RoleArn: str,
        RoleSessionName: str,
        WebIdentityToken: str,
        ProviderId: str = None,
        PolicyArns: List[Any] = None,
        Policy: str = None,
        DurationSeconds: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def decode_authorization_message(self, EncodedMessage: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_access_key_info(self, AccessKeyId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_caller_identity(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_federation_token(
        self,
        Name: str,
        Policy: str = None,
        PolicyArns: List[Any] = None,
        DurationSeconds: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_session_token(
        self,
        DurationSeconds: int = None,
        SerialNumber: str = None,
        TokenCode: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass
