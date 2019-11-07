from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_client_id_to_open_id_connect_provider(
        self,
        OpenIDConnectProviderArn: str,
        ClientID: str,
    ):
        pass


    def add_role_to_instance_profile(
        self,
        InstanceProfileName: str,
        RoleName: str,
    ):
        pass


    def add_user_to_group(
        self,
        GroupName: str,
        UserName: str,
    ):
        pass


    def attach_group_policy(
        self,
        GroupName: str,
        PolicyArn: str,
    ):
        pass


    def attach_role_policy(
        self,
        RoleName: str,
        PolicyArn: str,
    ):
        pass


    def attach_user_policy(
        self,
        UserName: str,
        PolicyArn: str,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def change_password(
        self,
        OldPassword: str,
        NewPassword: str,
    ):
        pass


    def create_access_key(
        self,
        UserName: Optional[str] = None,
    ) -> Dict:
        pass


    def create_account_alias(
        self,
        AccountAlias: str,
    ):
        pass


    def create_group(
        self,
        GroupName: str,
        Path: Optional[str] = None,
    ) -> Dict:
        pass


    def create_instance_profile(
        self,
        InstanceProfileName: str,
        Path: Optional[str] = None,
    ) -> Dict:
        pass


    def create_login_profile(
        self,
        UserName: str,
        Password: str,
        PasswordResetRequired: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_open_id_connect_provider(
        self,
        Url: str,
        ThumbprintList: List,
        ClientIDList: Optional[List] = None,
    ) -> Dict:
        pass


    def create_policy(
        self,
        PolicyName: str,
        PolicyDocument: str,
        Path: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_policy_version(
        self,
        PolicyArn: str,
        PolicyDocument: str,
        SetAsDefault: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_role(
        self,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: Optional[str] = None,
        Description: Optional[str] = None,
        MaxSessionDuration: Optional[int] = None,
        PermissionsBoundary: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_saml_provider(
        self,
        SAMLMetadataDocument: str,
        Name: str,
    ) -> Dict:
        pass


    def create_service_linked_role(
        self,
        AWSServiceName: str,
        Description: Optional[str] = None,
        CustomSuffix: Optional[str] = None,
    ) -> Dict:
        pass


    def create_service_specific_credential(
        self,
        UserName: str,
        ServiceName: str,
    ) -> Dict:
        pass


    def create_user(
        self,
        UserName: str,
        Path: Optional[str] = None,
        PermissionsBoundary: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_virtual_mfa_device(
        self,
        VirtualMFADeviceName: str,
        Path: Optional[str] = None,
    ) -> Dict:
        pass


    def deactivate_mfa_device(
        self,
        UserName: str,
        SerialNumber: str,
    ):
        pass


    def delete_access_key(
        self,
        AccessKeyId: str,
        UserName: Optional[str] = None,
    ):
        pass


    def delete_account_alias(
        self,
        AccountAlias: str,
    ):
        pass


    def delete_account_password_policy(
        self,
    ):
        pass


    def delete_group(
        self,
        GroupName: str,
    ):
        pass


    def delete_group_policy(
        self,
        GroupName: str,
        PolicyName: str,
    ):
        pass


    def delete_instance_profile(
        self,
        InstanceProfileName: str,
    ):
        pass


    def delete_login_profile(
        self,
        UserName: str,
    ):
        pass


    def delete_open_id_connect_provider(
        self,
        OpenIDConnectProviderArn: str,
    ):
        pass


    def delete_policy(
        self,
        PolicyArn: str,
    ):
        pass


    def delete_policy_version(
        self,
        PolicyArn: str,
        VersionId: str,
    ):
        pass


    def delete_role(
        self,
        RoleName: str,
    ):
        pass


    def delete_role_permissions_boundary(
        self,
        RoleName: str,
    ):
        pass


    def delete_role_policy(
        self,
        RoleName: str,
        PolicyName: str,
    ):
        pass


    def delete_saml_provider(
        self,
        SAMLProviderArn: str,
    ):
        pass


    def delete_server_certificate(
        self,
        ServerCertificateName: str,
    ):
        pass


    def delete_service_linked_role(
        self,
        RoleName: str,
    ) -> Dict:
        pass


    def delete_service_specific_credential(
        self,
        ServiceSpecificCredentialId: str,
        UserName: Optional[str] = None,
    ):
        pass


    def delete_signing_certificate(
        self,
        CertificateId: str,
        UserName: Optional[str] = None,
    ):
        pass


    def delete_ssh_public_key(
        self,
        UserName: str,
        SSHPublicKeyId: str,
    ):
        pass


    def delete_user(
        self,
        UserName: str,
    ):
        pass


    def delete_user_permissions_boundary(
        self,
        UserName: str,
    ):
        pass


    def delete_user_policy(
        self,
        UserName: str,
        PolicyName: str,
    ):
        pass


    def delete_virtual_mfa_device(
        self,
        SerialNumber: str,
    ):
        pass


    def detach_group_policy(
        self,
        GroupName: str,
        PolicyArn: str,
    ):
        pass


    def detach_role_policy(
        self,
        RoleName: str,
        PolicyArn: str,
    ):
        pass


    def detach_user_policy(
        self,
        UserName: str,
        PolicyArn: str,
    ):
        pass


    def enable_mfa_device(
        self,
        UserName: str,
        SerialNumber: str,
        AuthenticationCode1: str,
        AuthenticationCode2: str,
    ):
        pass


    def generate_credential_report(
        self,
    ) -> Dict:
        pass


    def generate_organizations_access_report(
        self,
        EntityPath: str,
        OrganizationsPolicyId: Optional[str] = None,
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


    def generate_service_last_accessed_details(
        self,
        Arn: str,
    ) -> Dict:
        pass


    def get_access_key_last_used(
        self,
        AccessKeyId: str,
    ) -> Dict:
        pass


    def get_account_authorization_details(
        self,
        Filter: Optional[List] = None,
        MaxItems: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def get_account_password_policy(
        self,
    ) -> Dict:
        pass


    def get_account_summary(
        self,
    ) -> Dict:
        pass


    def get_context_keys_for_custom_policy(
        self,
        PolicyInputList: List,
    ) -> Dict:
        pass


    def get_context_keys_for_principal_policy(
        self,
        PolicySourceArn: str,
        PolicyInputList: Optional[List] = None,
    ) -> Dict:
        pass


    def get_credential_report(
        self,
    ) -> Dict:
        pass


    def get_group(
        self,
        GroupName: str,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def get_group_policy(
        self,
        GroupName: str,
        PolicyName: str,
    ) -> Dict:
        pass


    def get_instance_profile(
        self,
        InstanceProfileName: str,
    ) -> Dict:
        pass


    def get_login_profile(
        self,
        UserName: str,
    ) -> Dict:
        pass


    def get_open_id_connect_provider(
        self,
        OpenIDConnectProviderArn: str,
    ) -> Dict:
        pass


    def get_organizations_access_report(
        self,
        JobId: str,
        MaxItems: Optional[int] = None,
        Marker: Optional[str] = None,
        SortKey: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_policy(
        self,
        PolicyArn: str,
    ) -> Dict:
        pass


    def get_policy_version(
        self,
        PolicyArn: str,
        VersionId: str,
    ) -> Dict:
        pass


    def get_role(
        self,
        RoleName: str,
    ) -> Dict:
        pass


    def get_role_policy(
        self,
        RoleName: str,
        PolicyName: str,
    ) -> Dict:
        pass


    def get_saml_provider(
        self,
        SAMLProviderArn: str,
    ) -> Dict:
        pass


    def get_server_certificate(
        self,
        ServerCertificateName: str,
    ) -> Dict:
        pass


    def get_service_last_accessed_details(
        self,
        JobId: str,
        MaxItems: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def get_service_last_accessed_details_with_entities(
        self,
        JobId: str,
        ServiceNamespace: str,
        MaxItems: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def get_service_linked_role_deletion_status(
        self,
        DeletionTaskId: str,
    ) -> Dict:
        pass


    def get_ssh_public_key(
        self,
        UserName: str,
        SSHPublicKeyId: str,
        Encoding: str,
    ) -> Dict:
        pass


    def get_user(
        self,
        UserName: Optional[str] = None,
    ) -> Dict:
        pass


    def get_user_policy(
        self,
        UserName: str,
        PolicyName: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_access_keys(
        self,
        UserName: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_account_aliases(
        self,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_attached_group_policies(
        self,
        GroupName: str,
        PathPrefix: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_attached_role_policies(
        self,
        RoleName: str,
        PathPrefix: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_attached_user_policies(
        self,
        UserName: str,
        PathPrefix: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_entities_for_policy(
        self,
        PolicyArn: str,
        EntityFilter: Optional[str] = None,
        PathPrefix: Optional[str] = None,
        PolicyUsageFilter: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_group_policies(
        self,
        GroupName: str,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_groups(
        self,
        PathPrefix: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_groups_for_user(
        self,
        UserName: str,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_instance_profiles(
        self,
        PathPrefix: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_instance_profiles_for_role(
        self,
        RoleName: str,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_mfa_devices(
        self,
        UserName: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_open_id_connect_providers(
        self,
    ) -> Dict:
        pass


    def list_policies(
        self,
        Scope: Optional[str] = None,
        OnlyAttached: Optional[bool] = None,
        PathPrefix: Optional[str] = None,
        PolicyUsageFilter: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_policies_granting_service_access(
        self,
        Arn: str,
        ServiceNamespaces: List,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_policy_versions(
        self,
        PolicyArn: str,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_role_policies(
        self,
        RoleName: str,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_role_tags(
        self,
        RoleName: str,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_roles(
        self,
        PathPrefix: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_saml_providers(
        self,
    ) -> Dict:
        pass


    def list_server_certificates(
        self,
        PathPrefix: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_service_specific_credentials(
        self,
        UserName: Optional[str] = None,
        ServiceName: Optional[str] = None,
    ) -> Dict:
        pass


    def list_signing_certificates(
        self,
        UserName: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_ssh_public_keys(
        self,
        UserName: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_user_policies(
        self,
        UserName: str,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_user_tags(
        self,
        UserName: str,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_users(
        self,
        PathPrefix: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_virtual_mfa_devices(
        self,
        AssignmentStatus: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def put_group_policy(
        self,
        GroupName: str,
        PolicyName: str,
        PolicyDocument: str,
    ):
        pass


    def put_role_permissions_boundary(
        self,
        RoleName: str,
        PermissionsBoundary: str,
    ):
        pass


    def put_role_policy(
        self,
        RoleName: str,
        PolicyName: str,
        PolicyDocument: str,
    ):
        pass


    def put_user_permissions_boundary(
        self,
        UserName: str,
        PermissionsBoundary: str,
    ):
        pass


    def put_user_policy(
        self,
        UserName: str,
        PolicyName: str,
        PolicyDocument: str,
    ):
        pass


    def remove_client_id_from_open_id_connect_provider(
        self,
        OpenIDConnectProviderArn: str,
        ClientID: str,
    ):
        pass


    def remove_role_from_instance_profile(
        self,
        InstanceProfileName: str,
        RoleName: str,
    ):
        pass


    def remove_user_from_group(
        self,
        GroupName: str,
        UserName: str,
    ):
        pass


    def reset_service_specific_credential(
        self,
        ServiceSpecificCredentialId: str,
        UserName: Optional[str] = None,
    ) -> Dict:
        pass


    def resync_mfa_device(
        self,
        UserName: str,
        SerialNumber: str,
        AuthenticationCode1: str,
        AuthenticationCode2: str,
    ):
        pass


    def set_default_policy_version(
        self,
        PolicyArn: str,
        VersionId: str,
    ):
        pass


    def set_security_token_service_preferences(
        self,
        GlobalEndpointTokenVersion: str,
    ):
        pass


    def simulate_custom_policy(
        self,
        PolicyInputList: List,
        ActionNames: List,
        ResourceArns: Optional[List] = None,
        ResourcePolicy: Optional[str] = None,
        ResourceOwner: Optional[str] = None,
        CallerArn: Optional[str] = None,
        ContextEntries: Optional[List] = None,
        ResourceHandlingOption: Optional[str] = None,
        MaxItems: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def simulate_principal_policy(
        self,
        PolicySourceArn: str,
        ActionNames: List,
        PolicyInputList: Optional[List] = None,
        ResourceArns: Optional[List] = None,
        ResourcePolicy: Optional[str] = None,
        ResourceOwner: Optional[str] = None,
        CallerArn: Optional[str] = None,
        ContextEntries: Optional[List] = None,
        ResourceHandlingOption: Optional[str] = None,
        MaxItems: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def tag_role(
        self,
        RoleName: str,
        Tags: List,
    ):
        pass


    def tag_user(
        self,
        UserName: str,
        Tags: List,
    ):
        pass


    def untag_role(
        self,
        RoleName: str,
        TagKeys: List,
    ):
        pass


    def untag_user(
        self,
        UserName: str,
        TagKeys: List,
    ):
        pass


    def update_access_key(
        self,
        AccessKeyId: str,
        Status: str,
        UserName: Optional[str] = None,
    ):
        pass


    def update_account_password_policy(
        self,
        MinimumPasswordLength: Optional[int] = None,
        RequireSymbols: Optional[bool] = None,
        RequireNumbers: Optional[bool] = None,
        RequireUppercaseCharacters: Optional[bool] = None,
        RequireLowercaseCharacters: Optional[bool] = None,
        AllowUsersToChangePassword: Optional[bool] = None,
        MaxPasswordAge: Optional[int] = None,
        PasswordReusePrevention: Optional[int] = None,
        HardExpiry: Optional[bool] = None,
    ):
        pass


    def update_assume_role_policy(
        self,
        RoleName: str,
        PolicyDocument: str,
    ):
        pass


    def update_group(
        self,
        GroupName: str,
        NewPath: Optional[str] = None,
        NewGroupName: Optional[str] = None,
    ):
        pass


    def update_login_profile(
        self,
        UserName: str,
        Password: Optional[str] = None,
        PasswordResetRequired: Optional[bool] = None,
    ):
        pass


    def update_open_id_connect_provider_thumbprint(
        self,
        OpenIDConnectProviderArn: str,
        ThumbprintList: List,
    ):
        pass


    def update_role(
        self,
        RoleName: str,
        Description: Optional[str] = None,
        MaxSessionDuration: Optional[int] = None,
    ) -> Dict:
        pass


    def update_role_description(
        self,
        RoleName: str,
        Description: str,
    ) -> Dict:
        pass


    def update_saml_provider(
        self,
        SAMLMetadataDocument: str,
        SAMLProviderArn: str,
    ) -> Dict:
        pass


    def update_server_certificate(
        self,
        ServerCertificateName: str,
        NewPath: Optional[str] = None,
        NewServerCertificateName: Optional[str] = None,
    ):
        pass


    def update_service_specific_credential(
        self,
        ServiceSpecificCredentialId: str,
        Status: str,
        UserName: Optional[str] = None,
    ):
        pass


    def update_signing_certificate(
        self,
        CertificateId: str,
        Status: str,
        UserName: Optional[str] = None,
    ):
        pass


    def update_ssh_public_key(
        self,
        UserName: str,
        SSHPublicKeyId: str,
        Status: str,
    ):
        pass


    def update_user(
        self,
        UserName: str,
        NewPath: Optional[str] = None,
        NewUserName: Optional[str] = None,
    ):
        pass


    def upload_server_certificate(
        self,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: Optional[str] = None,
        CertificateChain: Optional[str] = None,
    ) -> Dict:
        pass


    def upload_signing_certificate(
        self,
        CertificateBody: str,
        UserName: Optional[str] = None,
    ) -> Dict:
        pass


    def upload_ssh_public_key(
        self,
        UserName: str,
        SSHPublicKeyBody: str,
    ) -> Dict:
        pass

