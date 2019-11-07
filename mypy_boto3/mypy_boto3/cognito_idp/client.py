from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_custom_attributes(
        self,
        UserPoolId: str,
        CustomAttributes: List,
    ) -> Dict:
        pass


    def admin_add_user_to_group(
        self,
        UserPoolId: str,
        Username: str,
        GroupName: str,
    ):
        pass


    def admin_confirm_sign_up(
        self,
        UserPoolId: str,
        Username: str,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def admin_create_user(
        self,
        UserPoolId: str,
        Username: str,
        UserAttributes: Optional[List] = None,
        ValidationData: Optional[List] = None,
        TemporaryPassword: Optional[str] = None,
        ForceAliasCreation: Optional[bool] = None,
        MessageAction: Optional[str] = None,
        DesiredDeliveryMediums: Optional[List] = None,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def admin_delete_user(
        self,
        UserPoolId: str,
        Username: str,
    ):
        pass


    def admin_delete_user_attributes(
        self,
        UserPoolId: str,
        Username: str,
        UserAttributeNames: List,
    ) -> Dict:
        pass


    def admin_disable_provider_for_user(
        self,
        UserPoolId: str,
        User: Dict,
    ) -> Dict:
        pass


    def admin_disable_user(
        self,
        UserPoolId: str,
        Username: str,
    ) -> Dict:
        pass


    def admin_enable_user(
        self,
        UserPoolId: str,
        Username: str,
    ) -> Dict:
        pass


    def admin_forget_device(
        self,
        UserPoolId: str,
        Username: str,
        DeviceKey: str,
    ):
        pass


    def admin_get_device(
        self,
        DeviceKey: str,
        UserPoolId: str,
        Username: str,
    ) -> Dict:
        pass


    def admin_get_user(
        self,
        UserPoolId: str,
        Username: str,
    ) -> Dict:
        pass


    def admin_initiate_auth(
        self,
        UserPoolId: str,
        ClientId: str,
        AuthFlow: str,
        AuthParameters: Optional[Dict] = None,
        ClientMetadata: Optional[Dict] = None,
        AnalyticsMetadata: Optional[Dict] = None,
        ContextData: Optional[Dict] = None,
    ) -> Dict:
        pass


    def admin_link_provider_for_user(
        self,
        UserPoolId: str,
        DestinationUser: Dict,
        SourceUser: Dict,
    ) -> Dict:
        pass


    def admin_list_devices(
        self,
        UserPoolId: str,
        Username: str,
        Limit: Optional[int] = None,
        PaginationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def admin_list_groups_for_user(
        self,
        Username: str,
        UserPoolId: str,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def admin_list_user_auth_events(
        self,
        UserPoolId: str,
        Username: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def admin_remove_user_from_group(
        self,
        UserPoolId: str,
        Username: str,
        GroupName: str,
    ):
        pass


    def admin_reset_user_password(
        self,
        UserPoolId: str,
        Username: str,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def admin_respond_to_auth_challenge(
        self,
        UserPoolId: str,
        ClientId: str,
        ChallengeName: str,
        ChallengeResponses: Optional[Dict] = None,
        Session: Optional[str] = None,
        AnalyticsMetadata: Optional[Dict] = None,
        ContextData: Optional[Dict] = None,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def admin_set_user_mfa_preference(
        self,
        Username: str,
        UserPoolId: str,
        SMSMfaSettings: Optional[Dict] = None,
        SoftwareTokenMfaSettings: Optional[Dict] = None,
    ) -> Dict:
        pass


    def admin_set_user_password(
        self,
        UserPoolId: str,
        Username: str,
        Password: str,
        Permanent: Optional[bool] = None,
    ) -> Dict:
        pass


    def admin_set_user_settings(
        self,
        UserPoolId: str,
        Username: str,
        MFAOptions: List,
    ) -> Dict:
        pass


    def admin_update_auth_event_feedback(
        self,
        UserPoolId: str,
        Username: str,
        EventId: str,
        FeedbackValue: str,
    ) -> Dict:
        pass


    def admin_update_device_status(
        self,
        UserPoolId: str,
        Username: str,
        DeviceKey: str,
        DeviceRememberedStatus: Optional[str] = None,
    ) -> Dict:
        pass


    def admin_update_user_attributes(
        self,
        UserPoolId: str,
        Username: str,
        UserAttributes: List,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def admin_user_global_sign_out(
        self,
        UserPoolId: str,
        Username: str,
    ) -> Dict:
        pass


    def associate_software_token(
        self,
        AccessToken: Optional[str] = None,
        Session: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def change_password(
        self,
        PreviousPassword: str,
        ProposedPassword: str,
        AccessToken: str,
    ) -> Dict:
        pass


    def confirm_device(
        self,
        AccessToken: str,
        DeviceKey: str,
        DeviceSecretVerifierConfig: Optional[Dict] = None,
        DeviceName: Optional[str] = None,
    ) -> Dict:
        pass


    def confirm_forgot_password(
        self,
        ClientId: str,
        Username: str,
        ConfirmationCode: str,
        Password: str,
        SecretHash: Optional[str] = None,
        AnalyticsMetadata: Optional[Dict] = None,
        UserContextData: Optional[Dict] = None,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def confirm_sign_up(
        self,
        ClientId: str,
        Username: str,
        ConfirmationCode: str,
        SecretHash: Optional[str] = None,
        ForceAliasCreation: Optional[bool] = None,
        AnalyticsMetadata: Optional[Dict] = None,
        UserContextData: Optional[Dict] = None,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_group(
        self,
        GroupName: str,
        UserPoolId: str,
        Description: Optional[str] = None,
        RoleArn: Optional[str] = None,
        Precedence: Optional[int] = None,
    ) -> Dict:
        pass


    def create_identity_provider(
        self,
        UserPoolId: str,
        ProviderName: str,
        ProviderType: str,
        ProviderDetails: Dict,
        AttributeMapping: Optional[Dict] = None,
        IdpIdentifiers: Optional[List] = None,
    ) -> Dict:
        pass


    def create_resource_server(
        self,
        UserPoolId: str,
        Identifier: str,
        Name: str,
        Scopes: Optional[List] = None,
    ) -> Dict:
        pass


    def create_user_import_job(
        self,
        JobName: str,
        UserPoolId: str,
        CloudWatchLogsRoleArn: str,
    ) -> Dict:
        pass


    def create_user_pool(
        self,
        PoolName: str,
        Policies: Optional[Dict] = None,
        LambdaConfig: Optional[Dict] = None,
        AutoVerifiedAttributes: Optional[List] = None,
        AliasAttributes: Optional[List] = None,
        UsernameAttributes: Optional[List] = None,
        SmsVerificationMessage: Optional[str] = None,
        EmailVerificationMessage: Optional[str] = None,
        EmailVerificationSubject: Optional[str] = None,
        VerificationMessageTemplate: Optional[Dict] = None,
        SmsAuthenticationMessage: Optional[str] = None,
        MfaConfiguration: Optional[str] = None,
        DeviceConfiguration: Optional[Dict] = None,
        EmailConfiguration: Optional[Dict] = None,
        SmsConfiguration: Optional[Dict] = None,
        UserPoolTags: Optional[Dict] = None,
        AdminCreateUserConfig: Optional[Dict] = None,
        Schema: Optional[List] = None,
        UserPoolAddOns: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_user_pool_client(
        self,
        UserPoolId: str,
        ClientName: str,
        GenerateSecret: Optional[bool] = None,
        RefreshTokenValidity: Optional[int] = None,
        ReadAttributes: Optional[List] = None,
        WriteAttributes: Optional[List] = None,
        ExplicitAuthFlows: Optional[List] = None,
        SupportedIdentityProviders: Optional[List] = None,
        CallbackURLs: Optional[List] = None,
        LogoutURLs: Optional[List] = None,
        DefaultRedirectURI: Optional[str] = None,
        AllowedOAuthFlows: Optional[List] = None,
        AllowedOAuthScopes: Optional[List] = None,
        AllowedOAuthFlowsUserPoolClient: Optional[bool] = None,
        AnalyticsConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_user_pool_domain(
        self,
        Domain: str,
        UserPoolId: str,
        CustomDomainConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_group(
        self,
        GroupName: str,
        UserPoolId: str,
    ):
        pass


    def delete_identity_provider(
        self,
        UserPoolId: str,
        ProviderName: str,
    ):
        pass


    def delete_resource_server(
        self,
        UserPoolId: str,
        Identifier: str,
    ):
        pass


    def delete_user(
        self,
        AccessToken: str,
    ):
        pass


    def delete_user_attributes(
        self,
        UserAttributeNames: List,
        AccessToken: str,
    ) -> Dict:
        pass


    def delete_user_pool(
        self,
        UserPoolId: str,
    ):
        pass


    def delete_user_pool_client(
        self,
        UserPoolId: str,
        ClientId: str,
    ):
        pass


    def delete_user_pool_domain(
        self,
        Domain: str,
        UserPoolId: str,
    ) -> Dict:
        pass


    def describe_identity_provider(
        self,
        UserPoolId: str,
        ProviderName: str,
    ) -> Dict:
        pass


    def describe_resource_server(
        self,
        UserPoolId: str,
        Identifier: str,
    ) -> Dict:
        pass


    def describe_risk_configuration(
        self,
        UserPoolId: str,
        ClientId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_user_import_job(
        self,
        UserPoolId: str,
        JobId: str,
    ) -> Dict:
        pass


    def describe_user_pool(
        self,
        UserPoolId: str,
    ) -> Dict:
        pass


    def describe_user_pool_client(
        self,
        UserPoolId: str,
        ClientId: str,
    ) -> Dict:
        pass


    def describe_user_pool_domain(
        self,
        Domain: str,
    ) -> Dict:
        pass


    def forget_device(
        self,
        DeviceKey: str,
        AccessToken: Optional[str] = None,
    ):
        pass


    def forgot_password(
        self,
        ClientId: str,
        Username: str,
        SecretHash: Optional[str] = None,
        UserContextData: Optional[Dict] = None,
        AnalyticsMetadata: Optional[Dict] = None,
        ClientMetadata: Optional[Dict] = None,
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


    def get_csv_header(
        self,
        UserPoolId: str,
    ) -> Dict:
        pass


    def get_device(
        self,
        DeviceKey: str,
        AccessToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_group(
        self,
        GroupName: str,
        UserPoolId: str,
    ) -> Dict:
        pass


    def get_identity_provider_by_identifier(
        self,
        UserPoolId: str,
        IdpIdentifier: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_signing_certificate(
        self,
        UserPoolId: str,
    ) -> Dict:
        pass


    def get_ui_customization(
        self,
        UserPoolId: str,
        ClientId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_user(
        self,
        AccessToken: str,
    ) -> Dict:
        pass


    def get_user_attribute_verification_code(
        self,
        AccessToken: str,
        AttributeName: str,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_user_pool_mfa_config(
        self,
        UserPoolId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def global_sign_out(
        self,
        AccessToken: str,
    ) -> Dict:
        pass


    def initiate_auth(
        self,
        AuthFlow: str,
        ClientId: str,
        AuthParameters: Optional[Dict] = None,
        ClientMetadata: Optional[Dict] = None,
        AnalyticsMetadata: Optional[Dict] = None,
        UserContextData: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_devices(
        self,
        AccessToken: str,
        Limit: Optional[int] = None,
        PaginationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_groups(
        self,
        UserPoolId: str,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_identity_providers(
        self,
        UserPoolId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_resource_servers(
        self,
        UserPoolId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def list_user_import_jobs(
        self,
        UserPoolId: str,
        MaxResults: int,
        PaginationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_user_pool_clients(
        self,
        UserPoolId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_user_pools(
        self,
        MaxResults: int,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_users(
        self,
        UserPoolId: str,
        AttributesToGet: Optional[List] = None,
        Limit: Optional[int] = None,
        PaginationToken: Optional[str] = None,
        Filter: Optional[str] = None,
    ) -> Dict:
        pass


    def list_users_in_group(
        self,
        UserPoolId: str,
        GroupName: str,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def resend_confirmation_code(
        self,
        ClientId: str,
        Username: str,
        SecretHash: Optional[str] = None,
        UserContextData: Optional[Dict] = None,
        AnalyticsMetadata: Optional[Dict] = None,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def respond_to_auth_challenge(
        self,
        ClientId: str,
        ChallengeName: str,
        Session: Optional[str] = None,
        ChallengeResponses: Optional[Dict] = None,
        AnalyticsMetadata: Optional[Dict] = None,
        UserContextData: Optional[Dict] = None,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def set_risk_configuration(
        self,
        UserPoolId: str,
        ClientId: Optional[str] = None,
        CompromisedCredentialsRiskConfiguration: Optional[Dict] = None,
        AccountTakeoverRiskConfiguration: Optional[Dict] = None,
        RiskExceptionConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def set_ui_customization(
        self,
        UserPoolId: str,
        ClientId: Optional[str] = None,
        CSS: Optional[str] = None,
        ImageFile: Optional[bytes] = None,
    ) -> Dict:
        pass


    def set_user_mfa_preference(
        self,
        AccessToken: str,
        SMSMfaSettings: Optional[Dict] = None,
        SoftwareTokenMfaSettings: Optional[Dict] = None,
    ) -> Dict:
        pass


    def set_user_pool_mfa_config(
        self,
        UserPoolId: str,
        SmsMfaConfiguration: Optional[Dict] = None,
        SoftwareTokenMfaConfiguration: Optional[Dict] = None,
        MfaConfiguration: Optional[str] = None,
    ) -> Dict:
        pass


    def set_user_settings(
        self,
        AccessToken: str,
        MFAOptions: List,
    ) -> Dict:
        pass


    def sign_up(
        self,
        ClientId: str,
        Username: str,
        Password: str,
        SecretHash: Optional[str] = None,
        UserAttributes: Optional[List] = None,
        ValidationData: Optional[List] = None,
        AnalyticsMetadata: Optional[Dict] = None,
        UserContextData: Optional[Dict] = None,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_user_import_job(
        self,
        UserPoolId: str,
        JobId: str,
    ) -> Dict:
        pass


    def stop_user_import_job(
        self,
        UserPoolId: str,
        JobId: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_auth_event_feedback(
        self,
        UserPoolId: str,
        Username: str,
        EventId: str,
        FeedbackToken: str,
        FeedbackValue: str,
    ) -> Dict:
        pass


    def update_device_status(
        self,
        AccessToken: str,
        DeviceKey: str,
        DeviceRememberedStatus: Optional[str] = None,
    ) -> Dict:
        pass


    def update_group(
        self,
        GroupName: str,
        UserPoolId: str,
        Description: Optional[str] = None,
        RoleArn: Optional[str] = None,
        Precedence: Optional[int] = None,
    ) -> Dict:
        pass


    def update_identity_provider(
        self,
        UserPoolId: str,
        ProviderName: str,
        ProviderDetails: Optional[Dict] = None,
        AttributeMapping: Optional[Dict] = None,
        IdpIdentifiers: Optional[List] = None,
    ) -> Dict:
        pass


    def update_resource_server(
        self,
        UserPoolId: str,
        Identifier: str,
        Name: str,
        Scopes: Optional[List] = None,
    ) -> Dict:
        pass


    def update_user_attributes(
        self,
        UserAttributes: List,
        AccessToken: str,
        ClientMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_user_pool(
        self,
        UserPoolId: str,
        Policies: Optional[Dict] = None,
        LambdaConfig: Optional[Dict] = None,
        AutoVerifiedAttributes: Optional[List] = None,
        SmsVerificationMessage: Optional[str] = None,
        EmailVerificationMessage: Optional[str] = None,
        EmailVerificationSubject: Optional[str] = None,
        VerificationMessageTemplate: Optional[Dict] = None,
        SmsAuthenticationMessage: Optional[str] = None,
        MfaConfiguration: Optional[str] = None,
        DeviceConfiguration: Optional[Dict] = None,
        EmailConfiguration: Optional[Dict] = None,
        SmsConfiguration: Optional[Dict] = None,
        UserPoolTags: Optional[Dict] = None,
        AdminCreateUserConfig: Optional[Dict] = None,
        UserPoolAddOns: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_user_pool_client(
        self,
        UserPoolId: str,
        ClientId: str,
        ClientName: Optional[str] = None,
        RefreshTokenValidity: Optional[int] = None,
        ReadAttributes: Optional[List] = None,
        WriteAttributes: Optional[List] = None,
        ExplicitAuthFlows: Optional[List] = None,
        SupportedIdentityProviders: Optional[List] = None,
        CallbackURLs: Optional[List] = None,
        LogoutURLs: Optional[List] = None,
        DefaultRedirectURI: Optional[str] = None,
        AllowedOAuthFlows: Optional[List] = None,
        AllowedOAuthScopes: Optional[List] = None,
        AllowedOAuthFlowsUserPoolClient: Optional[bool] = None,
        AnalyticsConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_user_pool_domain(
        self,
        Domain: str,
        UserPoolId: str,
        CustomDomainConfig: Dict,
    ) -> Dict:
        pass


    def verify_software_token(
        self,
        UserCode: str,
        AccessToken: Optional[str] = None,
        Session: Optional[str] = None,
        FriendlyDeviceName: Optional[str] = None,
    ) -> Dict:
        pass


    def verify_user_attribute(
        self,
        AccessToken: str,
        AttributeName: str,
        Code: str,
    ) -> Dict:
        pass

