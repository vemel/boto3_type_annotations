# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.chime.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Chime](index.md#chime) / Client
    - [Client](#client)
        - [Client().associate_phone_number_with_user](#clientassociate_phone_number_with_user)
        - [Client().associate_phone_numbers_with_voice_connector](#clientassociate_phone_numbers_with_voice_connector)
        - [Client().associate_phone_numbers_with_voice_connector_group](#clientassociate_phone_numbers_with_voice_connector_group)
        - [Client().batch_delete_phone_number](#clientbatch_delete_phone_number)
        - [Client().batch_suspend_user](#clientbatch_suspend_user)
        - [Client().batch_unsuspend_user](#clientbatch_unsuspend_user)
        - [Client().batch_update_phone_number](#clientbatch_update_phone_number)
        - [Client().batch_update_user](#clientbatch_update_user)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_account](#clientcreate_account)
        - [Client().create_bot](#clientcreate_bot)
        - [Client().create_phone_number_order](#clientcreate_phone_number_order)
        - [Client().create_voice_connector](#clientcreate_voice_connector)
        - [Client().create_voice_connector_group](#clientcreate_voice_connector_group)
        - [Client().delete_account](#clientdelete_account)
        - [Client().delete_events_configuration](#clientdelete_events_configuration)
        - [Client().delete_phone_number](#clientdelete_phone_number)
        - [Client().delete_voice_connector](#clientdelete_voice_connector)
        - [Client().delete_voice_connector_group](#clientdelete_voice_connector_group)
        - [Client().delete_voice_connector_origination](#clientdelete_voice_connector_origination)
        - [Client().delete_voice_connector_streaming_configuration](#clientdelete_voice_connector_streaming_configuration)
        - [Client().delete_voice_connector_termination](#clientdelete_voice_connector_termination)
        - [Client().delete_voice_connector_termination_credentials](#clientdelete_voice_connector_termination_credentials)
        - [Client().disassociate_phone_number_from_user](#clientdisassociate_phone_number_from_user)
        - [Client().disassociate_phone_numbers_from_voice_connector](#clientdisassociate_phone_numbers_from_voice_connector)
        - [Client().disassociate_phone_numbers_from_voice_connector_group](#clientdisassociate_phone_numbers_from_voice_connector_group)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_account](#clientget_account)
        - [Client().get_account_settings](#clientget_account_settings)
        - [Client().get_bot](#clientget_bot)
        - [Client().get_events_configuration](#clientget_events_configuration)
        - [Client().get_global_settings](#clientget_global_settings)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_phone_number](#clientget_phone_number)
        - [Client().get_phone_number_order](#clientget_phone_number_order)
        - [Client().get_phone_number_settings](#clientget_phone_number_settings)
        - [Client().get_user](#clientget_user)
        - [Client().get_user_settings](#clientget_user_settings)
        - [Client().get_voice_connector](#clientget_voice_connector)
        - [Client().get_voice_connector_group](#clientget_voice_connector_group)
        - [Client().get_voice_connector_logging_configuration](#clientget_voice_connector_logging_configuration)
        - [Client().get_voice_connector_origination](#clientget_voice_connector_origination)
        - [Client().get_voice_connector_streaming_configuration](#clientget_voice_connector_streaming_configuration)
        - [Client().get_voice_connector_termination](#clientget_voice_connector_termination)
        - [Client().get_voice_connector_termination_health](#clientget_voice_connector_termination_health)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().invite_users](#clientinvite_users)
        - [Client().list_accounts](#clientlist_accounts)
        - [Client().list_bots](#clientlist_bots)
        - [Client().list_phone_number_orders](#clientlist_phone_number_orders)
        - [Client().list_phone_numbers](#clientlist_phone_numbers)
        - [Client().list_users](#clientlist_users)
        - [Client().list_voice_connector_groups](#clientlist_voice_connector_groups)
        - [Client().list_voice_connector_termination_credentials](#clientlist_voice_connector_termination_credentials)
        - [Client().list_voice_connectors](#clientlist_voice_connectors)
        - [Client().logout_user](#clientlogout_user)
        - [Client().put_events_configuration](#clientput_events_configuration)
        - [Client().put_voice_connector_logging_configuration](#clientput_voice_connector_logging_configuration)
        - [Client().put_voice_connector_origination](#clientput_voice_connector_origination)
        - [Client().put_voice_connector_streaming_configuration](#clientput_voice_connector_streaming_configuration)
        - [Client().put_voice_connector_termination](#clientput_voice_connector_termination)
        - [Client().put_voice_connector_termination_credentials](#clientput_voice_connector_termination_credentials)
        - [Client().regenerate_security_token](#clientregenerate_security_token)
        - [Client().reset_personal_pin](#clientreset_personal_pin)
        - [Client().restore_phone_number](#clientrestore_phone_number)
        - [Client().search_available_phone_numbers](#clientsearch_available_phone_numbers)
        - [Client().update_account](#clientupdate_account)
        - [Client().update_account_settings](#clientupdate_account_settings)
        - [Client().update_bot](#clientupdate_bot)
        - [Client().update_global_settings](#clientupdate_global_settings)
        - [Client().update_phone_number](#clientupdate_phone_number)
        - [Client().update_phone_number_settings](#clientupdate_phone_number_settings)
        - [Client().update_user](#clientupdate_user)
        - [Client().update_user_settings](#clientupdate_user_settings)
        - [Client().update_voice_connector](#clientupdate_voice_connector)
        - [Client().update_voice_connector_group](#clientupdate_voice_connector_group)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_phone_number_with_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L15)

```python
def associate_phone_number_with_user(
    AccountId: str,
    UserId: str,
    E164PhoneNumber: str,
) -> Dict[str, Any]:
```

### Client().associate_phone_numbers_with_voice_connector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L21)

```python
def associate_phone_numbers_with_voice_connector(
    VoiceConnectorId: str,
    E164PhoneNumbers: List[Any] = None,
    ForceAssociate: bool = None,
) -> Dict[str, Any]:
```

### Client().associate_phone_numbers_with_voice_connector_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L30)

```python
def associate_phone_numbers_with_voice_connector_group(
    VoiceConnectorGroupId: str,
    E164PhoneNumbers: List[Any] = None,
    ForceAssociate: bool = None,
) -> Dict[str, Any]:
```

### Client().batch_delete_phone_number

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L39)

```python
def batch_delete_phone_number(PhoneNumberIds: List[Any]) -> Dict[str, Any]:
```

### Client().batch_suspend_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L43)

```python
def batch_suspend_user(
    AccountId: str,
    UserIdList: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_unsuspend_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L49)

```python
def batch_unsuspend_user(
    AccountId: str,
    UserIdList: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_update_phone_number

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L55)

```python
def batch_update_phone_number(
    UpdatePhoneNumberRequestItems: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_update_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L61)

```python
def batch_update_user(
    AccountId: str,
    UpdateUserRequestItems: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L67)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L71)

```python
def create_account(Name: str) -> Dict[str, Any]:
```

### Client().create_bot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L75)

```python
def create_bot(
    AccountId: str,
    DisplayName: str,
    Domain: str = None,
) -> Dict[str, Any]:
```

### Client().create_phone_number_order

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L81)

```python
def create_phone_number_order(
    ProductType: str,
    E164PhoneNumbers: List[Any],
) -> Dict[str, Any]:
```

### Client().create_voice_connector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L87)

```python
def create_voice_connector(
    Name: str,
    RequireEncryption: bool,
    AwsRegion: str = None,
) -> Dict[str, Any]:
```

### Client().create_voice_connector_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L93)

```python
def create_voice_connector_group(
    Name: str,
    VoiceConnectorItems: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L99)

```python
def delete_account(AccountId: str) -> Dict[str, Any]:
```

### Client().delete_events_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L103)

```python
def delete_events_configuration(AccountId: str, BotId: str) -> None:
```

### Client().delete_phone_number

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L107)

```python
def delete_phone_number(PhoneNumberId: str) -> None:
```

### Client().delete_voice_connector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L111)

```python
def delete_voice_connector(VoiceConnectorId: str) -> None:
```

### Client().delete_voice_connector_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L115)

```python
def delete_voice_connector_group(VoiceConnectorGroupId: str) -> None:
```

### Client().delete_voice_connector_origination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L119)

```python
def delete_voice_connector_origination(VoiceConnectorId: str) -> None:
```

### Client().delete_voice_connector_streaming_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L123)

```python
def delete_voice_connector_streaming_configuration(
    VoiceConnectorId: str,
) -> None:
```

### Client().delete_voice_connector_termination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L129)

```python
def delete_voice_connector_termination(VoiceConnectorId: str) -> None:
```

### Client().delete_voice_connector_termination_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L133)

```python
def delete_voice_connector_termination_credentials(
    VoiceConnectorId: str,
    Usernames: List[Any] = None,
) -> None:
```

### Client().disassociate_phone_number_from_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L139)

```python
def disassociate_phone_number_from_user(
    AccountId: str,
    UserId: str,
) -> Dict[str, Any]:
```

### Client().disassociate_phone_numbers_from_voice_connector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L145)

```python
def disassociate_phone_numbers_from_voice_connector(
    VoiceConnectorId: str,
    E164PhoneNumbers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().disassociate_phone_numbers_from_voice_connector_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L151)

```python
def disassociate_phone_numbers_from_voice_connector_group(
    VoiceConnectorGroupId: str,
    E164PhoneNumbers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L157)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L167)

```python
def get_account(AccountId: str) -> Dict[str, Any]:
```

### Client().get_account_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L171)

```python
def get_account_settings(AccountId: str) -> Dict[str, Any]:
```

### Client().get_bot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L175)

```python
def get_bot(AccountId: str, BotId: str) -> Dict[str, Any]:
```

### Client().get_events_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L179)

```python
def get_events_configuration(AccountId: str, BotId: str) -> Dict[str, Any]:
```

### Client().get_global_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L183)

```python
def get_global_settings() -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L187)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_phone_number

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L191)

```python
def get_phone_number(PhoneNumberId: str) -> Dict[str, Any]:
```

### Client().get_phone_number_order

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L195)

```python
def get_phone_number_order(PhoneNumberOrderId: str) -> Dict[str, Any]:
```

### Client().get_phone_number_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L199)

```python
def get_phone_number_settings() -> Dict[str, Any]:
```

### Client().get_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L203)

```python
def get_user(AccountId: str, UserId: str) -> Dict[str, Any]:
```

### Client().get_user_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L207)

```python
def get_user_settings(AccountId: str, UserId: str) -> Dict[str, Any]:
```

### Client().get_voice_connector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L211)

```python
def get_voice_connector(VoiceConnectorId: str) -> Dict[str, Any]:
```

### Client().get_voice_connector_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L215)

```python
def get_voice_connector_group(VoiceConnectorGroupId: str) -> Dict[str, Any]:
```

### Client().get_voice_connector_logging_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L219)

```python
def get_voice_connector_logging_configuration(
    VoiceConnectorId: str,
) -> Dict[str, Any]:
```

### Client().get_voice_connector_origination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L225)

```python
def get_voice_connector_origination(VoiceConnectorId: str) -> Dict[str, Any]:
```

### Client().get_voice_connector_streaming_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L229)

```python
def get_voice_connector_streaming_configuration(
    VoiceConnectorId: str,
) -> Dict[str, Any]:
```

### Client().get_voice_connector_termination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L235)

```python
def get_voice_connector_termination(VoiceConnectorId: str) -> Dict[str, Any]:
```

### Client().get_voice_connector_termination_health

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L239)

```python
def get_voice_connector_termination_health(
    VoiceConnectorId: str,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L245)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().invite_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L249)

```python
def invite_users(AccountId: str, UserEmailList: List[Any]) -> Dict[str, Any]:
```

### Client().list_accounts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L253)

```python
def list_accounts(
    Name: str = None,
    UserEmail: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_bots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L263)

```python
def list_bots(
    AccountId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_phone_number_orders

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L269)

```python
def list_phone_number_orders(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_phone_numbers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L275)

```python
def list_phone_numbers(
    Status: str = None,
    ProductType: str = None,
    FilterName: str = None,
    FilterValue: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L287)

```python
def list_users(
    AccountId: str,
    UserEmail: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_voice_connector_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L297)

```python
def list_voice_connector_groups(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_voice_connector_termination_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L303)

```python
def list_voice_connector_termination_credentials(
    VoiceConnectorId: str,
) -> Dict[str, Any]:
```

### Client().list_voice_connectors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L309)

```python
def list_voice_connectors(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().logout_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L315)

```python
def logout_user(AccountId: str, UserId: str) -> Dict[str, Any]:
```

### Client().put_events_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L319)

```python
def put_events_configuration(
    AccountId: str,
    BotId: str,
    OutboundEventsHTTPSEndpoint: str = None,
    LambdaFunctionArn: str = None,
) -> Dict[str, Any]:
```

### Client().put_voice_connector_logging_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L329)

```python
def put_voice_connector_logging_configuration(
    VoiceConnectorId: str,
    LoggingConfiguration: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_voice_connector_origination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L335)

```python
def put_voice_connector_origination(
    VoiceConnectorId: str,
    Origination: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_voice_connector_streaming_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L341)

```python
def put_voice_connector_streaming_configuration(
    VoiceConnectorId: str,
    StreamingConfiguration: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_voice_connector_termination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L347)

```python
def put_voice_connector_termination(
    VoiceConnectorId: str,
    Termination: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_voice_connector_termination_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L353)

```python
def put_voice_connector_termination_credentials(
    VoiceConnectorId: str,
    Credentials: List[Any] = None,
) -> None:
```

### Client().regenerate_security_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L359)

```python
def regenerate_security_token(AccountId: str, BotId: str) -> Dict[str, Any]:
```

### Client().reset_personal_pin

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L363)

```python
def reset_personal_pin(AccountId: str, UserId: str) -> Dict[str, Any]:
```

### Client().restore_phone_number

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L367)

```python
def restore_phone_number(PhoneNumberId: str) -> Dict[str, Any]:
```

### Client().search_available_phone_numbers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L371)

```python
def search_available_phone_numbers(
    AreaCode: str = None,
    City: str = None,
    Country: str = None,
    State: str = None,
    TollFreePrefix: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().update_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L384)

```python
def update_account(AccountId: str, Name: str = None) -> Dict[str, Any]:
```

### Client().update_account_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L388)

```python
def update_account_settings(
    AccountId: str,
    AccountSettings: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_bot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L394)

```python
def update_bot(
    AccountId: str,
    BotId: str,
    Disabled: bool = None,
) -> Dict[str, Any]:
```

### Client().update_global_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L400)

```python
def update_global_settings(
    BusinessCalling: Dict[str, Any],
    VoiceConnector: Dict[str, Any],
) -> None:
```

### Client().update_phone_number

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L406)

```python
def update_phone_number(
    PhoneNumberId: str,
    ProductType: str = None,
    CallingName: str = None,
) -> Dict[str, Any]:
```

### Client().update_phone_number_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L412)

```python
def update_phone_number_settings(CallingName: str) -> None:
```

### Client().update_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L416)

```python
def update_user(
    AccountId: str,
    UserId: str,
    LicenseType: str = None,
) -> Dict[str, Any]:
```

### Client().update_user_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L422)

```python
def update_user_settings(
    AccountId: str,
    UserId: str,
    UserSettings: Dict[str, Any],
) -> None:
```

### Client().update_voice_connector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L428)

```python
def update_voice_connector(
    VoiceConnectorId: str,
    Name: str,
    RequireEncryption: bool,
) -> Dict[str, Any]:
```

### Client().update_voice_connector_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/client.py#L434)

```python
def update_voice_connector_group(
    VoiceConnectorGroupId: str,
    Name: str,
    VoiceConnectorItems: List[Any],
) -> Dict[str, Any]:
```
