from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_key_deletion(self, KeyId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def connect_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_alias(self, AliasName: str, TargetKeyId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_custom_key_store(
        self,
        CustomKeyStoreName: str,
        CloudHsmClusterId: str,
        TrustAnchorCertificate: str,
        KeyStorePassword: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_grant(
        self,
        KeyId: str,
        GranteePrincipal: str,
        Operations: List[Any],
        RetiringPrincipal: str = None,
        Constraints: Dict[str, Any] = None,
        GrantTokens: List[Any] = None,
        Name: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_key(
        self,
        Policy: str = None,
        Description: str = None,
        KeyUsage: str = None,
        Origin: str = None,
        CustomKeyStoreId: str = None,
        BypassPolicyLockoutSafetyCheck: bool = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def decrypt(
        self,
        CiphertextBlob: bytes,
        EncryptionContext: Dict[str, Any] = None,
        GrantTokens: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_alias(self, AliasName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_imported_key_material(self, KeyId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_custom_key_stores(
        self,
        CustomKeyStoreId: str = None,
        CustomKeyStoreName: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_key(self, KeyId: str, GrantTokens: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_key(self, KeyId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def disable_key_rotation(self, KeyId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def disconnect_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_key(self, KeyId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def enable_key_rotation(self, KeyId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def encrypt(
        self,
        KeyId: str,
        Plaintext: bytes,
        EncryptionContext: Dict[str, Any] = None,
        GrantTokens: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_data_key(
        self,
        KeyId: str,
        EncryptionContext: Dict[str, Any] = None,
        NumberOfBytes: int = None,
        KeySpec: str = None,
        GrantTokens: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_data_key_without_plaintext(
        self,
        KeyId: str,
        EncryptionContext: Dict[str, Any] = None,
        KeySpec: str = None,
        NumberOfBytes: int = None,
        GrantTokens: List[Any] = None,
    ) -> Dict[str, Any]:
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
    def generate_random(
        self, NumberOfBytes: int = None, CustomKeyStoreId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_key_policy(self, KeyId: str, PolicyName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_key_rotation_status(self, KeyId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_parameters_for_import(
        self, KeyId: str, WrappingAlgorithm: str, WrappingKeySpec: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def import_key_material(
        self,
        KeyId: str,
        ImportToken: bytes,
        EncryptedKeyMaterial: bytes,
        ValidTo: datetime = None,
        ExpirationModel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_aliases(
        self, KeyId: str = None, Limit: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_grants(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_key_policies(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_keys(self, Limit: int = None, Marker: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resource_tags(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_retirable_grants(
        self, RetiringPrincipal: str, Limit: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_key_policy(
        self,
        KeyId: str,
        PolicyName: str,
        Policy: str,
        BypassPolicyLockoutSafetyCheck: bool = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def re_encrypt(
        self,
        CiphertextBlob: bytes,
        DestinationKeyId: str,
        SourceEncryptionContext: Dict[str, Any] = None,
        DestinationEncryptionContext: Dict[str, Any] = None,
        GrantTokens: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def retire_grant(
        self, GrantToken: str = None, KeyId: str = None, GrantId: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def revoke_grant(self, KeyId: str, GrantId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def schedule_key_deletion(
        self, KeyId: str, PendingWindowInDays: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, KeyId: str, Tags: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, KeyId: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_alias(self, AliasName: str, TargetKeyId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_custom_key_store(
        self,
        CustomKeyStoreId: str,
        NewCustomKeyStoreName: str = None,
        KeyStorePassword: str = None,
        CloudHsmClusterId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_key_description(self, KeyId: str, Description: str) -> None:
        pass
