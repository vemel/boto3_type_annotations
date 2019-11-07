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


    def cancel_rotate_secret(
        self,
        SecretId: str,
    ) -> Dict:
        pass


    def create_secret(
        self,
        Name: str,
        ClientRequestToken: Optional[str] = None,
        Description: Optional[str] = None,
        KmsKeyId: Optional[str] = None,
        SecretBinary: Optional[bytes] = None,
        SecretString: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_resource_policy(
        self,
        SecretId: str,
    ) -> Dict:
        pass


    def delete_secret(
        self,
        SecretId: str,
        RecoveryWindowInDays: Optional[int] = None,
        ForceDeleteWithoutRecovery: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_secret(
        self,
        SecretId: str,
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


    def get_random_password(
        self,
        PasswordLength: Optional[int] = None,
        ExcludeCharacters: Optional[str] = None,
        ExcludeNumbers: Optional[bool] = None,
        ExcludePunctuation: Optional[bool] = None,
        ExcludeUppercase: Optional[bool] = None,
        ExcludeLowercase: Optional[bool] = None,
        IncludeSpace: Optional[bool] = None,
        RequireEachIncludedType: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_resource_policy(
        self,
        SecretId: str,
    ) -> Dict:
        pass


    def get_secret_value(
        self,
        SecretId: str,
        VersionId: Optional[str] = None,
        VersionStage: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_secret_version_ids(
        self,
        SecretId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        IncludeDeprecated: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_secrets(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_resource_policy(
        self,
        SecretId: str,
        ResourcePolicy: str,
    ) -> Dict:
        pass


    def put_secret_value(
        self,
        SecretId: str,
        ClientRequestToken: Optional[str] = None,
        SecretBinary: Optional[bytes] = None,
        SecretString: Optional[str] = None,
        VersionStages: Optional[List] = None,
    ) -> Dict:
        pass


    def restore_secret(
        self,
        SecretId: str,
    ) -> Dict:
        pass


    def rotate_secret(
        self,
        SecretId: str,
        ClientRequestToken: Optional[str] = None,
        RotationLambdaARN: Optional[str] = None,
        RotationRules: Optional[Dict] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        SecretId: str,
        Tags: List,
    ):
        pass


    def untag_resource(
        self,
        SecretId: str,
        TagKeys: List,
    ):
        pass


    def update_secret(
        self,
        SecretId: str,
        ClientRequestToken: Optional[str] = None,
        Description: Optional[str] = None,
        KmsKeyId: Optional[str] = None,
        SecretBinary: Optional[bytes] = None,
        SecretString: Optional[str] = None,
    ) -> Dict:
        pass


    def update_secret_version_stage(
        self,
        SecretId: str,
        VersionStage: str,
        RemoveFromVersionId: Optional[str] = None,
        MoveToVersionId: Optional[str] = None,
    ) -> Dict:
        pass

