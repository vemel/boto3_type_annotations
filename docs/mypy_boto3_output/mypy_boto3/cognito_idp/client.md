# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cognito_idp.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cognito Idp](index.md#cognito-idp) / Client
    - [Client](#client)
        - [Client().add_custom_attributes](#clientadd_custom_attributes)
        - [Client().admin_add_user_to_group](#clientadmin_add_user_to_group)
        - [Client().admin_confirm_sign_up](#clientadmin_confirm_sign_up)
        - [Client().admin_create_user](#clientadmin_create_user)
        - [Client().admin_delete_user](#clientadmin_delete_user)
        - [Client().admin_delete_user_attributes](#clientadmin_delete_user_attributes)
        - [Client().admin_disable_provider_for_user](#clientadmin_disable_provider_for_user)
        - [Client().admin_disable_user](#clientadmin_disable_user)
        - [Client().admin_enable_user](#clientadmin_enable_user)
        - [Client().admin_forget_device](#clientadmin_forget_device)
        - [Client().admin_get_device](#clientadmin_get_device)
        - [Client().admin_get_user](#clientadmin_get_user)
        - [Client().admin_initiate_auth](#clientadmin_initiate_auth)
        - [Client().admin_link_provider_for_user](#clientadmin_link_provider_for_user)
        - [Client().admin_list_devices](#clientadmin_list_devices)
        - [Client().admin_list_groups_for_user](#clientadmin_list_groups_for_user)
        - [Client().admin_list_user_auth_events](#clientadmin_list_user_auth_events)
        - [Client().admin_remove_user_from_group](#clientadmin_remove_user_from_group)
        - [Client().admin_reset_user_password](#clientadmin_reset_user_password)
        - [Client().admin_respond_to_auth_challenge](#clientadmin_respond_to_auth_challenge)
        - [Client().admin_set_user_mfa_preference](#clientadmin_set_user_mfa_preference)
        - [Client().admin_set_user_password](#clientadmin_set_user_password)
        - [Client().admin_set_user_settings](#clientadmin_set_user_settings)
        - [Client().admin_update_auth_event_feedback](#clientadmin_update_auth_event_feedback)
        - [Client().admin_update_device_status](#clientadmin_update_device_status)
        - [Client().admin_update_user_attributes](#clientadmin_update_user_attributes)
        - [Client().admin_user_global_sign_out](#clientadmin_user_global_sign_out)
        - [Client().associate_software_token](#clientassociate_software_token)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().change_password](#clientchange_password)
        - [Client().confirm_device](#clientconfirm_device)
        - [Client().confirm_forgot_password](#clientconfirm_forgot_password)
        - [Client().confirm_sign_up](#clientconfirm_sign_up)
        - [Client().create_group](#clientcreate_group)
        - [Client().create_identity_provider](#clientcreate_identity_provider)
        - [Client().create_resource_server](#clientcreate_resource_server)
        - [Client().create_user_import_job](#clientcreate_user_import_job)
        - [Client().create_user_pool](#clientcreate_user_pool)
        - [Client().create_user_pool_client](#clientcreate_user_pool_client)
        - [Client().create_user_pool_domain](#clientcreate_user_pool_domain)
        - [Client().delete_group](#clientdelete_group)
        - [Client().delete_identity_provider](#clientdelete_identity_provider)
        - [Client().delete_resource_server](#clientdelete_resource_server)
        - [Client().delete_user](#clientdelete_user)
        - [Client().delete_user_attributes](#clientdelete_user_attributes)
        - [Client().delete_user_pool](#clientdelete_user_pool)
        - [Client().delete_user_pool_client](#clientdelete_user_pool_client)
        - [Client().delete_user_pool_domain](#clientdelete_user_pool_domain)
        - [Client().describe_identity_provider](#clientdescribe_identity_provider)
        - [Client().describe_resource_server](#clientdescribe_resource_server)
        - [Client().describe_risk_configuration](#clientdescribe_risk_configuration)
        - [Client().describe_user_import_job](#clientdescribe_user_import_job)
        - [Client().describe_user_pool](#clientdescribe_user_pool)
        - [Client().describe_user_pool_client](#clientdescribe_user_pool_client)
        - [Client().describe_user_pool_domain](#clientdescribe_user_pool_domain)
        - [Client().forget_device](#clientforget_device)
        - [Client().forgot_password](#clientforgot_password)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_csv_header](#clientget_csv_header)
        - [Client().get_device](#clientget_device)
        - [Client().get_group](#clientget_group)
        - [Client().get_identity_provider_by_identifier](#clientget_identity_provider_by_identifier)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_signing_certificate](#clientget_signing_certificate)
        - [Client().get_ui_customization](#clientget_ui_customization)
        - [Client().get_user](#clientget_user)
        - [Client().get_user_attribute_verification_code](#clientget_user_attribute_verification_code)
        - [Client().get_user_pool_mfa_config](#clientget_user_pool_mfa_config)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().global_sign_out](#clientglobal_sign_out)
        - [Client().initiate_auth](#clientinitiate_auth)
        - [Client().list_devices](#clientlist_devices)
        - [Client().list_groups](#clientlist_groups)
        - [Client().list_identity_providers](#clientlist_identity_providers)
        - [Client().list_resource_servers](#clientlist_resource_servers)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_user_import_jobs](#clientlist_user_import_jobs)
        - [Client().list_user_pool_clients](#clientlist_user_pool_clients)
        - [Client().list_user_pools](#clientlist_user_pools)
        - [Client().list_users](#clientlist_users)
        - [Client().list_users_in_group](#clientlist_users_in_group)
        - [Client().resend_confirmation_code](#clientresend_confirmation_code)
        - [Client().respond_to_auth_challenge](#clientrespond_to_auth_challenge)
        - [Client().set_risk_configuration](#clientset_risk_configuration)
        - [Client().set_ui_customization](#clientset_ui_customization)
        - [Client().set_user_mfa_preference](#clientset_user_mfa_preference)
        - [Client().set_user_pool_mfa_config](#clientset_user_pool_mfa_config)
        - [Client().set_user_settings](#clientset_user_settings)
        - [Client().sign_up](#clientsign_up)
        - [Client().start_user_import_job](#clientstart_user_import_job)
        - [Client().stop_user_import_job](#clientstop_user_import_job)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_auth_event_feedback](#clientupdate_auth_event_feedback)
        - [Client().update_device_status](#clientupdate_device_status)
        - [Client().update_group](#clientupdate_group)
        - [Client().update_identity_provider](#clientupdate_identity_provider)
        - [Client().update_resource_server](#clientupdate_resource_server)
        - [Client().update_user_attributes](#clientupdate_user_attributes)
        - [Client().update_user_pool](#clientupdate_user_pool)
        - [Client().update_user_pool_client](#clientupdate_user_pool_client)
        - [Client().update_user_pool_domain](#clientupdate_user_pool_domain)
        - [Client().verify_software_token](#clientverify_software_token)
        - [Client().verify_user_attribute](#clientverify_user_attribute)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_custom_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L15)

```python
def add_custom_attributes(
    UserPoolId: str,
    CustomAttributes: List[Any],
) -> Dict[str, Any]:
```

### Client().admin_add_user_to_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L21)

```python
def admin_add_user_to_group(
    UserPoolId: str,
    Username: str,
    GroupName: str,
) -> None:
```

### Client().admin_confirm_sign_up

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L27)

```python
def admin_confirm_sign_up(
    UserPoolId: str,
    Username: str,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().admin_create_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L33)

```python
def admin_create_user(
    UserPoolId: str,
    Username: str,
    UserAttributes: List[Any] = None,
    ValidationData: List[Any] = None,
    TemporaryPassword: str = None,
    ForceAliasCreation: bool = None,
    MessageAction: str = None,
    DesiredDeliveryMediums: List[Any] = None,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().admin_delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L48)

```python
def admin_delete_user(UserPoolId: str, Username: str) -> None:
```

### Client().admin_delete_user_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L52)

```python
def admin_delete_user_attributes(
    UserPoolId: str,
    Username: str,
    UserAttributeNames: List[Any],
) -> Dict[str, Any]:
```

### Client().admin_disable_provider_for_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L58)

```python
def admin_disable_provider_for_user(
    UserPoolId: str,
    User: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().admin_disable_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L64)

```python
def admin_disable_user(UserPoolId: str, Username: str) -> Dict[str, Any]:
```

### Client().admin_enable_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L68)

```python
def admin_enable_user(UserPoolId: str, Username: str) -> Dict[str, Any]:
```

### Client().admin_forget_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L72)

```python
def admin_forget_device(
    UserPoolId: str,
    Username: str,
    DeviceKey: str,
) -> None:
```

### Client().admin_get_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L78)

```python
def admin_get_device(
    DeviceKey: str,
    UserPoolId: str,
    Username: str,
) -> Dict[str, Any]:
```

### Client().admin_get_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L84)

```python
def admin_get_user(UserPoolId: str, Username: str) -> Dict[str, Any]:
```

### Client().admin_initiate_auth

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L88)

```python
def admin_initiate_auth(
    UserPoolId: str,
    ClientId: str,
    AuthFlow: str,
    AuthParameters: Dict[str, Any] = None,
    ClientMetadata: Dict[str, Any] = None,
    AnalyticsMetadata: Dict[str, Any] = None,
    ContextData: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().admin_link_provider_for_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L101)

```python
def admin_link_provider_for_user(
    UserPoolId: str,
    DestinationUser: Dict[str, Any],
    SourceUser: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().admin_list_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L110)

```python
def admin_list_devices(
    UserPoolId: str,
    Username: str,
    Limit: int = None,
    PaginationToken: str = None,
) -> Dict[str, Any]:
```

### Client().admin_list_groups_for_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L120)

```python
def admin_list_groups_for_user(
    Username: str,
    UserPoolId: str,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().admin_list_user_auth_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L126)

```python
def admin_list_user_auth_events(
    UserPoolId: str,
    Username: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().admin_remove_user_from_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L136)

```python
def admin_remove_user_from_group(
    UserPoolId: str,
    Username: str,
    GroupName: str,
) -> None:
```

### Client().admin_reset_user_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L142)

```python
def admin_reset_user_password(
    UserPoolId: str,
    Username: str,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().admin_respond_to_auth_challenge

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L148)

```python
def admin_respond_to_auth_challenge(
    UserPoolId: str,
    ClientId: str,
    ChallengeName: str,
    ChallengeResponses: Dict[str, Any] = None,
    Session: str = None,
    AnalyticsMetadata: Dict[str, Any] = None,
    ContextData: Dict[str, Any] = None,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().admin_set_user_mfa_preference

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L162)

```python
def admin_set_user_mfa_preference(
    Username: str,
    UserPoolId: str,
    SMSMfaSettings: Dict[str, Any] = None,
    SoftwareTokenMfaSettings: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().admin_set_user_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L172)

```python
def admin_set_user_password(
    UserPoolId: str,
    Username: str,
    Password: str,
    Permanent: bool = None,
) -> Dict[str, Any]:
```

### Client().admin_set_user_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L178)

```python
def admin_set_user_settings(
    UserPoolId: str,
    Username: str,
    MFAOptions: List[Any],
) -> Dict[str, Any]:
```

### Client().admin_update_auth_event_feedback

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L184)

```python
def admin_update_auth_event_feedback(
    UserPoolId: str,
    Username: str,
    EventId: str,
    FeedbackValue: str,
) -> Dict[str, Any]:
```

### Client().admin_update_device_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L190)

```python
def admin_update_device_status(
    UserPoolId: str,
    Username: str,
    DeviceKey: str,
    DeviceRememberedStatus: str = None,
) -> Dict[str, Any]:
```

### Client().admin_update_user_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L200)

```python
def admin_update_user_attributes(
    UserPoolId: str,
    Username: str,
    UserAttributes: List[Any],
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().admin_user_global_sign_out

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L210)

```python
def admin_user_global_sign_out(
    UserPoolId: str,
    Username: str,
) -> Dict[str, Any]:
```

### Client().associate_software_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L216)

```python
def associate_software_token(
    AccessToken: str = None,
    Session: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L222)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().change_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L226)

```python
def change_password(
    PreviousPassword: str,
    ProposedPassword: str,
    AccessToken: str,
) -> Dict[str, Any]:
```

### Client().confirm_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L232)

```python
def confirm_device(
    AccessToken: str,
    DeviceKey: str,
    DeviceSecretVerifierConfig: Dict[str, Any] = None,
    DeviceName: str = None,
) -> Dict[str, Any]:
```

### Client().confirm_forgot_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L242)

```python
def confirm_forgot_password(
    ClientId: str,
    Username: str,
    ConfirmationCode: str,
    Password: str,
    SecretHash: str = None,
    AnalyticsMetadata: Dict[str, Any] = None,
    UserContextData: Dict[str, Any] = None,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().confirm_sign_up

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L256)

```python
def confirm_sign_up(
    ClientId: str,
    Username: str,
    ConfirmationCode: str,
    SecretHash: str = None,
    ForceAliasCreation: bool = None,
    AnalyticsMetadata: Dict[str, Any] = None,
    UserContextData: Dict[str, Any] = None,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L270)

```python
def create_group(
    GroupName: str,
    UserPoolId: str,
    Description: str = None,
    RoleArn: str = None,
    Precedence: int = None,
) -> Dict[str, Any]:
```

### Client().create_identity_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L281)

```python
def create_identity_provider(
    UserPoolId: str,
    ProviderName: str,
    ProviderType: str,
    ProviderDetails: Dict[str, Any],
    AttributeMapping: Dict[str, Any] = None,
    IdpIdentifiers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_resource_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L293)

```python
def create_resource_server(
    UserPoolId: str,
    Identifier: str,
    Name: str,
    Scopes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_user_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L299)

```python
def create_user_import_job(
    JobName: str,
    UserPoolId: str,
    CloudWatchLogsRoleArn: str,
) -> Dict[str, Any]:
```

### Client().create_user_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L305)

```python
def create_user_pool(
    PoolName: str,
    Policies: Dict[str, Any] = None,
    LambdaConfig: Dict[str, Any] = None,
    AutoVerifiedAttributes: List[Any] = None,
    AliasAttributes: List[Any] = None,
    UsernameAttributes: List[Any] = None,
    SmsVerificationMessage: str = None,
    EmailVerificationMessage: str = None,
    EmailVerificationSubject: str = None,
    VerificationMessageTemplate: Dict[str, Any] = None,
    SmsAuthenticationMessage: str = None,
    MfaConfiguration: str = None,
    DeviceConfiguration: Dict[str, Any] = None,
    EmailConfiguration: Dict[str, Any] = None,
    SmsConfiguration: Dict[str, Any] = None,
    UserPoolTags: Dict[str, Any] = None,
    AdminCreateUserConfig: Dict[str, Any] = None,
    Schema: List[Any] = None,
    UserPoolAddOns: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_user_pool_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L330)

```python
def create_user_pool_client(
    UserPoolId: str,
    ClientName: str,
    GenerateSecret: bool = None,
    RefreshTokenValidity: int = None,
    ReadAttributes: List[Any] = None,
    WriteAttributes: List[Any] = None,
    ExplicitAuthFlows: List[Any] = None,
    SupportedIdentityProviders: List[Any] = None,
    CallbackURLs: List[Any] = None,
    LogoutURLs: List[Any] = None,
    DefaultRedirectURI: str = None,
    AllowedOAuthFlows: List[Any] = None,
    AllowedOAuthScopes: List[Any] = None,
    AllowedOAuthFlowsUserPoolClient: bool = None,
    AnalyticsConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_user_pool_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L351)

```python
def create_user_pool_domain(
    Domain: str,
    UserPoolId: str,
    CustomDomainConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L357)

```python
def delete_group(GroupName: str, UserPoolId: str) -> None:
```

### Client().delete_identity_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L361)

```python
def delete_identity_provider(UserPoolId: str, ProviderName: str) -> None:
```

### Client().delete_resource_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L365)

```python
def delete_resource_server(UserPoolId: str, Identifier: str) -> None:
```

### Client().delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L369)

```python
def delete_user(AccessToken: str) -> None:
```

### Client().delete_user_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L373)

```python
def delete_user_attributes(
    UserAttributeNames: List[Any],
    AccessToken: str,
) -> Dict[str, Any]:
```

### Client().delete_user_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L379)

```python
def delete_user_pool(UserPoolId: str) -> None:
```

### Client().delete_user_pool_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L383)

```python
def delete_user_pool_client(UserPoolId: str, ClientId: str) -> None:
```

### Client().delete_user_pool_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L387)

```python
def delete_user_pool_domain(Domain: str, UserPoolId: str) -> Dict[str, Any]:
```

### Client().describe_identity_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L391)

```python
def describe_identity_provider(
    UserPoolId: str,
    ProviderName: str,
) -> Dict[str, Any]:
```

### Client().describe_resource_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L397)

```python
def describe_resource_server(
    UserPoolId: str,
    Identifier: str,
) -> Dict[str, Any]:
```

### Client().describe_risk_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L403)

```python
def describe_risk_configuration(
    UserPoolId: str,
    ClientId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_user_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L409)

```python
def describe_user_import_job(UserPoolId: str, JobId: str) -> Dict[str, Any]:
```

### Client().describe_user_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L413)

```python
def describe_user_pool(UserPoolId: str) -> Dict[str, Any]:
```

### Client().describe_user_pool_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L417)

```python
def describe_user_pool_client(
    UserPoolId: str,
    ClientId: str,
) -> Dict[str, Any]:
```

### Client().describe_user_pool_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L423)

```python
def describe_user_pool_domain(Domain: str) -> Dict[str, Any]:
```

### Client().forget_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L427)

```python
def forget_device(DeviceKey: str, AccessToken: str = None) -> None:
```

### Client().forgot_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L431)

```python
def forgot_password(
    ClientId: str,
    Username: str,
    SecretHash: str = None,
    UserContextData: Dict[str, Any] = None,
    AnalyticsMetadata: Dict[str, Any] = None,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L443)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_csv_header

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L453)

```python
def get_csv_header(UserPoolId: str) -> Dict[str, Any]:
```

### Client().get_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L457)

```python
def get_device(DeviceKey: str, AccessToken: str = None) -> Dict[str, Any]:
```

### Client().get_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L461)

```python
def get_group(GroupName: str, UserPoolId: str) -> Dict[str, Any]:
```

### Client().get_identity_provider_by_identifier

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L465)

```python
def get_identity_provider_by_identifier(
    UserPoolId: str,
    IdpIdentifier: str,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L471)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_signing_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L475)

```python
def get_signing_certificate(UserPoolId: str) -> Dict[str, Any]:
```

### Client().get_ui_customization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L479)

```python
def get_ui_customization(
    UserPoolId: str,
    ClientId: str = None,
) -> Dict[str, Any]:
```

### Client().get_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L485)

```python
def get_user(AccessToken: str) -> Dict[str, Any]:
```

### Client().get_user_attribute_verification_code

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L489)

```python
def get_user_attribute_verification_code(
    AccessToken: str,
    AttributeName: str,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_user_pool_mfa_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L498)

```python
def get_user_pool_mfa_config(UserPoolId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L502)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().global_sign_out

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L506)

```python
def global_sign_out(AccessToken: str) -> Dict[str, Any]:
```

### Client().initiate_auth

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L510)

```python
def initiate_auth(
    AuthFlow: str,
    ClientId: str,
    AuthParameters: Dict[str, Any] = None,
    ClientMetadata: Dict[str, Any] = None,
    AnalyticsMetadata: Dict[str, Any] = None,
    UserContextData: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L522)

```python
def list_devices(
    AccessToken: str,
    Limit: int = None,
    PaginationToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L528)

```python
def list_groups(
    UserPoolId: str,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_identity_providers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L534)

```python
def list_identity_providers(
    UserPoolId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_resource_servers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L540)

```python
def list_resource_servers(
    UserPoolId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L546)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().list_user_import_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L550)

```python
def list_user_import_jobs(
    UserPoolId: str,
    MaxResults: int,
    PaginationToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_user_pool_clients

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L556)

```python
def list_user_pool_clients(
    UserPoolId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_user_pools

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L562)

```python
def list_user_pools(MaxResults: int, NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L566)

```python
def list_users(
    UserPoolId: str,
    AttributesToGet: List[Any] = None,
    Limit: int = None,
    PaginationToken: str = None,
    Filter: str = None,
) -> Dict[str, Any]:
```

### Client().list_users_in_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L577)

```python
def list_users_in_group(
    UserPoolId: str,
    GroupName: str,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().resend_confirmation_code

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L583)

```python
def resend_confirmation_code(
    ClientId: str,
    Username: str,
    SecretHash: str = None,
    UserContextData: Dict[str, Any] = None,
    AnalyticsMetadata: Dict[str, Any] = None,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().respond_to_auth_challenge

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L595)

```python
def respond_to_auth_challenge(
    ClientId: str,
    ChallengeName: str,
    Session: str = None,
    ChallengeResponses: Dict[str, Any] = None,
    AnalyticsMetadata: Dict[str, Any] = None,
    UserContextData: Dict[str, Any] = None,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().set_risk_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L608)

```python
def set_risk_configuration(
    UserPoolId: str,
    ClientId: str = None,
    CompromisedCredentialsRiskConfiguration: Dict[str, Any] = None,
    AccountTakeoverRiskConfiguration: Dict[str, Any] = None,
    RiskExceptionConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().set_ui_customization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L619)

```python
def set_ui_customization(
    UserPoolId: str,
    ClientId: str = None,
    CSS: str = None,
    ImageFile: bytes = None,
) -> Dict[str, Any]:
```

### Client().set_user_mfa_preference

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L629)

```python
def set_user_mfa_preference(
    AccessToken: str,
    SMSMfaSettings: Dict[str, Any] = None,
    SoftwareTokenMfaSettings: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().set_user_pool_mfa_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L638)

```python
def set_user_pool_mfa_config(
    UserPoolId: str,
    SmsMfaConfiguration: Dict[str, Any] = None,
    SoftwareTokenMfaConfiguration: Dict[str, Any] = None,
    MfaConfiguration: str = None,
) -> Dict[str, Any]:
```

### Client().set_user_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L648)

```python
def set_user_settings(
    AccessToken: str,
    MFAOptions: List[Any],
) -> Dict[str, Any]:
```

### Client().sign_up

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L654)

```python
def sign_up(
    ClientId: str,
    Username: str,
    Password: str,
    SecretHash: str = None,
    UserAttributes: List[Any] = None,
    ValidationData: List[Any] = None,
    AnalyticsMetadata: Dict[str, Any] = None,
    UserContextData: Dict[str, Any] = None,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().start_user_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L669)

```python
def start_user_import_job(UserPoolId: str, JobId: str) -> Dict[str, Any]:
```

### Client().stop_user_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L673)

```python
def stop_user_import_job(UserPoolId: str, JobId: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L677)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L681)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_auth_event_feedback

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L685)

```python
def update_auth_event_feedback(
    UserPoolId: str,
    Username: str,
    EventId: str,
    FeedbackToken: str,
    FeedbackValue: str,
) -> Dict[str, Any]:
```

### Client().update_device_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L696)

```python
def update_device_status(
    AccessToken: str,
    DeviceKey: str,
    DeviceRememberedStatus: str = None,
) -> Dict[str, Any]:
```

### Client().update_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L702)

```python
def update_group(
    GroupName: str,
    UserPoolId: str,
    Description: str = None,
    RoleArn: str = None,
    Precedence: int = None,
) -> Dict[str, Any]:
```

### Client().update_identity_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L713)

```python
def update_identity_provider(
    UserPoolId: str,
    ProviderName: str,
    ProviderDetails: Dict[str, Any] = None,
    AttributeMapping: Dict[str, Any] = None,
    IdpIdentifiers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_resource_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L724)

```python
def update_resource_server(
    UserPoolId: str,
    Identifier: str,
    Name: str,
    Scopes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_user_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L730)

```python
def update_user_attributes(
    UserAttributes: List[Any],
    AccessToken: str,
    ClientMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_user_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L739)

```python
def update_user_pool(
    UserPoolId: str,
    Policies: Dict[str, Any] = None,
    LambdaConfig: Dict[str, Any] = None,
    AutoVerifiedAttributes: List[Any] = None,
    SmsVerificationMessage: str = None,
    EmailVerificationMessage: str = None,
    EmailVerificationSubject: str = None,
    VerificationMessageTemplate: Dict[str, Any] = None,
    SmsAuthenticationMessage: str = None,
    MfaConfiguration: str = None,
    DeviceConfiguration: Dict[str, Any] = None,
    EmailConfiguration: Dict[str, Any] = None,
    SmsConfiguration: Dict[str, Any] = None,
    UserPoolTags: Dict[str, Any] = None,
    AdminCreateUserConfig: Dict[str, Any] = None,
    UserPoolAddOns: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_user_pool_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L761)

```python
def update_user_pool_client(
    UserPoolId: str,
    ClientId: str,
    ClientName: str = None,
    RefreshTokenValidity: int = None,
    ReadAttributes: List[Any] = None,
    WriteAttributes: List[Any] = None,
    ExplicitAuthFlows: List[Any] = None,
    SupportedIdentityProviders: List[Any] = None,
    CallbackURLs: List[Any] = None,
    LogoutURLs: List[Any] = None,
    DefaultRedirectURI: str = None,
    AllowedOAuthFlows: List[Any] = None,
    AllowedOAuthScopes: List[Any] = None,
    AllowedOAuthFlowsUserPoolClient: bool = None,
    AnalyticsConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_user_pool_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L782)

```python
def update_user_pool_domain(
    Domain: str,
    UserPoolId: str,
    CustomDomainConfig: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().verify_software_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L788)

```python
def verify_software_token(
    UserCode: str,
    AccessToken: str = None,
    Session: str = None,
    FriendlyDeviceName: str = None,
) -> Dict[str, Any]:
```

### Client().verify_user_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/client.py#L798)

```python
def verify_user_attribute(
    AccessToken: str,
    AttributeName: str,
    Code: str,
) -> Dict[str, Any]:
```
