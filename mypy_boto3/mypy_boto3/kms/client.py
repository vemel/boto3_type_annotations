from datetime import datetime
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


    def cancel_key_deletion(
        self,
        KeyId: str,
    ) -> Dict:
        pass


    def connect_custom_key_store(
        self,
        CustomKeyStoreId: str,
    ) -> Dict:
        pass


    def create_alias(
        self,
        AliasName: str,
        TargetKeyId: str,
    ):
        pass


    def create_custom_key_store(
        self,
        CustomKeyStoreName: str,
        CloudHsmClusterId: str,
        TrustAnchorCertificate: str,
        KeyStorePassword: str,
    ) -> Dict:
        pass


    def create_grant(
        self,
        KeyId: str,
        GranteePrincipal: str,
        Operations: List,
        RetiringPrincipal: Optional[str] = None,
        Constraints: Optional[Dict] = None,
        GrantTokens: Optional[List] = None,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def create_key(
        self,
        Policy: Optional[str] = None,
        Description: Optional[str] = None,
        KeyUsage: Optional[str] = None,
        Origin: Optional[str] = None,
        CustomKeyStoreId: Optional[str] = None,
        BypassPolicyLockoutSafetyCheck: Optional[bool] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def decrypt(
        self,
        CiphertextBlob: bytes,
        EncryptionContext: Optional[Dict] = None,
        GrantTokens: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_alias(
        self,
        AliasName: str,
    ):
        pass


    def delete_custom_key_store(
        self,
        CustomKeyStoreId: str,
    ) -> Dict:
        pass


    def delete_imported_key_material(
        self,
        KeyId: str,
    ):
        pass


    def describe_custom_key_stores(
        self,
        CustomKeyStoreId: Optional[str] = None,
        CustomKeyStoreName: Optional[str] = None,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_key(
        self,
        KeyId: str,
        GrantTokens: Optional[List] = None,
    ) -> Dict:
        pass


    def disable_key(
        self,
        KeyId: str,
    ):
        pass


    def disable_key_rotation(
        self,
        KeyId: str,
    ):
        pass


    def disconnect_custom_key_store(
        self,
        CustomKeyStoreId: str,
    ) -> Dict:
        pass


    def enable_key(
        self,
        KeyId: str,
    ):
        pass


    def enable_key_rotation(
        self,
        KeyId: str,
    ):
        pass


    def encrypt(
        self,
        KeyId: str,
        Plaintext: bytes,
        EncryptionContext: Optional[Dict] = None,
        GrantTokens: Optional[List] = None,
    ) -> Dict:
        pass


    def generate_data_key(
        self,
        KeyId: str,
        EncryptionContext: Optional[Dict] = None,
        NumberOfBytes: Optional[int] = None,
        KeySpec: Optional[str] = None,
        GrantTokens: Optional[List] = None,
    ) -> Dict:
        pass


    def generate_data_key_without_plaintext(
        self,
        KeyId: str,
        EncryptionContext: Optional[Dict] = None,
        KeySpec: Optional[str] = None,
        NumberOfBytes: Optional[int] = None,
        GrantTokens: Optional[List] = None,
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


    def generate_random(
        self,
        NumberOfBytes: Optional[int] = None,
        CustomKeyStoreId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_key_policy(
        self,
        KeyId: str,
        PolicyName: str,
    ) -> Dict:
        pass


    def get_key_rotation_status(
        self,
        KeyId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_parameters_for_import(
        self,
        KeyId: str,
        WrappingAlgorithm: str,
        WrappingKeySpec: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def import_key_material(
        self,
        KeyId: str,
        ImportToken: bytes,
        EncryptedKeyMaterial: bytes,
        ValidTo: Optional[datetime] = None,
        ExpirationModel: Optional[str] = None,
    ) -> Dict:
        pass


    def list_aliases(
        self,
        KeyId: Optional[str] = None,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_grants(
        self,
        KeyId: str,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_key_policies(
        self,
        KeyId: str,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_keys(
        self,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_resource_tags(
        self,
        KeyId: str,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_retirable_grants(
        self,
        RetiringPrincipal: str,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def put_key_policy(
        self,
        KeyId: str,
        PolicyName: str,
        Policy: str,
        BypassPolicyLockoutSafetyCheck: Optional[bool] = None,
    ):
        pass


    def re_encrypt(
        self,
        CiphertextBlob: bytes,
        DestinationKeyId: str,
        SourceEncryptionContext: Optional[Dict] = None,
        DestinationEncryptionContext: Optional[Dict] = None,
        GrantTokens: Optional[List] = None,
    ) -> Dict:
        pass


    def retire_grant(
        self,
        GrantToken: Optional[str] = None,
        KeyId: Optional[str] = None,
        GrantId: Optional[str] = None,
    ):
        pass


    def revoke_grant(
        self,
        KeyId: str,
        GrantId: str,
    ):
        pass


    def schedule_key_deletion(
        self,
        KeyId: str,
        PendingWindowInDays: Optional[int] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        KeyId: str,
        Tags: List,
    ):
        pass


    def untag_resource(
        self,
        KeyId: str,
        TagKeys: List,
    ):
        pass


    def update_alias(
        self,
        AliasName: str,
        TargetKeyId: str,
    ):
        pass


    def update_custom_key_store(
        self,
        CustomKeyStoreId: str,
        NewCustomKeyStoreName: Optional[str] = None,
        KeyStorePassword: Optional[str] = None,
        CloudHsmClusterId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_key_description(
        self,
        KeyId: str,
        Description: str,
    ):
        pass

