# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ses.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ses](index.md#ses) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().clone_receipt_rule_set](#clientclone_receipt_rule_set)
        - [Client().create_configuration_set](#clientcreate_configuration_set)
        - [Client().create_configuration_set_event_destination](#clientcreate_configuration_set_event_destination)
        - [Client().create_configuration_set_tracking_options](#clientcreate_configuration_set_tracking_options)
        - [Client().create_custom_verification_email_template](#clientcreate_custom_verification_email_template)
        - [Client().create_receipt_filter](#clientcreate_receipt_filter)
        - [Client().create_receipt_rule](#clientcreate_receipt_rule)
        - [Client().create_receipt_rule_set](#clientcreate_receipt_rule_set)
        - [Client().create_template](#clientcreate_template)
        - [Client().delete_configuration_set](#clientdelete_configuration_set)
        - [Client().delete_configuration_set_event_destination](#clientdelete_configuration_set_event_destination)
        - [Client().delete_configuration_set_tracking_options](#clientdelete_configuration_set_tracking_options)
        - [Client().delete_custom_verification_email_template](#clientdelete_custom_verification_email_template)
        - [Client().delete_identity](#clientdelete_identity)
        - [Client().delete_identity_policy](#clientdelete_identity_policy)
        - [Client().delete_receipt_filter](#clientdelete_receipt_filter)
        - [Client().delete_receipt_rule](#clientdelete_receipt_rule)
        - [Client().delete_receipt_rule_set](#clientdelete_receipt_rule_set)
        - [Client().delete_template](#clientdelete_template)
        - [Client().delete_verified_email_address](#clientdelete_verified_email_address)
        - [Client().describe_active_receipt_rule_set](#clientdescribe_active_receipt_rule_set)
        - [Client().describe_configuration_set](#clientdescribe_configuration_set)
        - [Client().describe_receipt_rule](#clientdescribe_receipt_rule)
        - [Client().describe_receipt_rule_set](#clientdescribe_receipt_rule_set)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_account_sending_enabled](#clientget_account_sending_enabled)
        - [Client().get_custom_verification_email_template](#clientget_custom_verification_email_template)
        - [Client().get_identity_dkim_attributes](#clientget_identity_dkim_attributes)
        - [Client().get_identity_mail_from_domain_attributes](#clientget_identity_mail_from_domain_attributes)
        - [Client().get_identity_notification_attributes](#clientget_identity_notification_attributes)
        - [Client().get_identity_policies](#clientget_identity_policies)
        - [Client().get_identity_verification_attributes](#clientget_identity_verification_attributes)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_send_quota](#clientget_send_quota)
        - [Client().get_send_statistics](#clientget_send_statistics)
        - [Client().get_template](#clientget_template)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_configuration_sets](#clientlist_configuration_sets)
        - [Client().list_custom_verification_email_templates](#clientlist_custom_verification_email_templates)
        - [Client().list_identities](#clientlist_identities)
        - [Client().list_identity_policies](#clientlist_identity_policies)
        - [Client().list_receipt_filters](#clientlist_receipt_filters)
        - [Client().list_receipt_rule_sets](#clientlist_receipt_rule_sets)
        - [Client().list_templates](#clientlist_templates)
        - [Client().list_verified_email_addresses](#clientlist_verified_email_addresses)
        - [Client().put_configuration_set_delivery_options](#clientput_configuration_set_delivery_options)
        - [Client().put_identity_policy](#clientput_identity_policy)
        - [Client().reorder_receipt_rule_set](#clientreorder_receipt_rule_set)
        - [Client().send_bounce](#clientsend_bounce)
        - [Client().send_bulk_templated_email](#clientsend_bulk_templated_email)
        - [Client().send_custom_verification_email](#clientsend_custom_verification_email)
        - [Client().send_email](#clientsend_email)
        - [Client().send_raw_email](#clientsend_raw_email)
        - [Client().send_templated_email](#clientsend_templated_email)
        - [Client().set_active_receipt_rule_set](#clientset_active_receipt_rule_set)
        - [Client().set_identity_dkim_enabled](#clientset_identity_dkim_enabled)
        - [Client().set_identity_feedback_forwarding_enabled](#clientset_identity_feedback_forwarding_enabled)
        - [Client().set_identity_headers_in_notifications_enabled](#clientset_identity_headers_in_notifications_enabled)
        - [Client().set_identity_mail_from_domain](#clientset_identity_mail_from_domain)
        - [Client().set_identity_notification_topic](#clientset_identity_notification_topic)
        - [Client().set_receipt_rule_position](#clientset_receipt_rule_position)
        - [Client().test_render_template](#clienttest_render_template)
        - [Client().update_account_sending_enabled](#clientupdate_account_sending_enabled)
        - [Client().update_configuration_set_event_destination](#clientupdate_configuration_set_event_destination)
        - [Client().update_configuration_set_reputation_metrics_enabled](#clientupdate_configuration_set_reputation_metrics_enabled)
        - [Client().update_configuration_set_sending_enabled](#clientupdate_configuration_set_sending_enabled)
        - [Client().update_configuration_set_tracking_options](#clientupdate_configuration_set_tracking_options)
        - [Client().update_custom_verification_email_template](#clientupdate_custom_verification_email_template)
        - [Client().update_receipt_rule](#clientupdate_receipt_rule)
        - [Client().update_template](#clientupdate_template)
        - [Client().verify_domain_dkim](#clientverify_domain_dkim)
        - [Client().verify_domain_identity](#clientverify_domain_identity)
        - [Client().verify_email_address](#clientverify_email_address)
        - [Client().verify_email_identity](#clientverify_email_identity)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().clone_receipt_rule_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L19)

```python
def clone_receipt_rule_set(
    RuleSetName: str,
    OriginalRuleSetName: str,
) -> Dict[str, Any]:
```

### Client().create_configuration_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L25)

```python
def create_configuration_set(
    ConfigurationSet: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_configuration_set_event_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L31)

```python
def create_configuration_set_event_destination(
    ConfigurationSetName: str,
    EventDestination: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_configuration_set_tracking_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L37)

```python
def create_configuration_set_tracking_options(
    ConfigurationSetName: str,
    TrackingOptions: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_custom_verification_email_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L43)

```python
def create_custom_verification_email_template(
    TemplateName: str,
    FromEmailAddress: str,
    TemplateSubject: str,
    TemplateContent: str,
    SuccessRedirectionURL: str,
    FailureRedirectionURL: str,
) -> None:
```

### Client().create_receipt_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L55)

```python
def create_receipt_filter(Filter: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().create_receipt_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L59)

```python
def create_receipt_rule(
    RuleSetName: str,
    Rule: Dict[str, Any],
    After: str = None,
) -> Dict[str, Any]:
```

### Client().create_receipt_rule_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L65)

```python
def create_receipt_rule_set(RuleSetName: str) -> Dict[str, Any]:
```

### Client().create_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L69)

```python
def create_template(Template: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().delete_configuration_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L73)

```python
def delete_configuration_set(ConfigurationSetName: str) -> Dict[str, Any]:
```

### Client().delete_configuration_set_event_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L77)

```python
def delete_configuration_set_event_destination(
    ConfigurationSetName: str,
    EventDestinationName: str,
) -> Dict[str, Any]:
```

### Client().delete_configuration_set_tracking_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L83)

```python
def delete_configuration_set_tracking_options(
    ConfigurationSetName: str,
) -> Dict[str, Any]:
```

### Client().delete_custom_verification_email_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L89)

```python
def delete_custom_verification_email_template(TemplateName: str) -> None:
```

### Client().delete_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L93)

```python
def delete_identity(Identity: str) -> Dict[str, Any]:
```

### Client().delete_identity_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L97)

```python
def delete_identity_policy(Identity: str, PolicyName: str) -> Dict[str, Any]:
```

### Client().delete_receipt_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L101)

```python
def delete_receipt_filter(FilterName: str) -> Dict[str, Any]:
```

### Client().delete_receipt_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L105)

```python
def delete_receipt_rule(RuleSetName: str, RuleName: str) -> Dict[str, Any]:
```

### Client().delete_receipt_rule_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L109)

```python
def delete_receipt_rule_set(RuleSetName: str) -> Dict[str, Any]:
```

### Client().delete_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L113)

```python
def delete_template(TemplateName: str) -> Dict[str, Any]:
```

### Client().delete_verified_email_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L117)

```python
def delete_verified_email_address(EmailAddress: str) -> None:
```

### Client().describe_active_receipt_rule_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L121)

```python
def describe_active_receipt_rule_set() -> Dict[str, Any]:
```

### Client().describe_configuration_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L125)

```python
def describe_configuration_set(
    ConfigurationSetName: str,
    ConfigurationSetAttributeNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_receipt_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L133)

```python
def describe_receipt_rule(RuleSetName: str, RuleName: str) -> Dict[str, Any]:
```

### Client().describe_receipt_rule_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L137)

```python
def describe_receipt_rule_set(RuleSetName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L141)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_account_sending_enabled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L151)

```python
def get_account_sending_enabled() -> Dict[str, Any]:
```

### Client().get_custom_verification_email_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L155)

```python
def get_custom_verification_email_template(
    TemplateName: str,
) -> Dict[str, Any]:
```

### Client().get_identity_dkim_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L161)

```python
def get_identity_dkim_attributes(Identities: List[Any]) -> Dict[str, Any]:
```

### Client().get_identity_mail_from_domain_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L165)

```python
def get_identity_mail_from_domain_attributes(
    Identities: List[Any],
) -> Dict[str, Any]:
```

### Client().get_identity_notification_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L171)

```python
def get_identity_notification_attributes(
    Identities: List[Any],
) -> Dict[str, Any]:
```

### Client().get_identity_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L177)

```python
def get_identity_policies(
    Identity: str,
    PolicyNames: List[Any],
) -> Dict[str, Any]:
```

### Client().get_identity_verification_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L183)

```python
def get_identity_verification_attributes(
    Identities: List[Any],
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L189)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_send_quota

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L193)

```python
def get_send_quota() -> Dict[str, Any]:
```

### Client().get_send_statistics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L197)

```python
def get_send_statistics() -> Dict[str, Any]:
```

### Client().get_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L201)

```python
def get_template(TemplateName: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L205)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_configuration_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L209)

```python
def list_configuration_sets(
    NextToken: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_custom_verification_email_templates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L215)

```python
def list_custom_verification_email_templates(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_identities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L221)

```python
def list_identities(
    IdentityType: str = None,
    NextToken: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_identity_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L227)

```python
def list_identity_policies(Identity: str) -> Dict[str, Any]:
```

### Client().list_receipt_filters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L231)

```python
def list_receipt_filters() -> Dict[str, Any]:
```

### Client().list_receipt_rule_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L235)

```python
def list_receipt_rule_sets(NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_templates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L239)

```python
def list_templates(
    NextToken: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_verified_email_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L245)

```python
def list_verified_email_addresses() -> Dict[str, Any]:
```

### Client().put_configuration_set_delivery_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L249)

```python
def put_configuration_set_delivery_options(
    ConfigurationSetName: str,
    DeliveryOptions: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().put_identity_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L255)

```python
def put_identity_policy(
    Identity: str,
    PolicyName: str,
    Policy: str,
) -> Dict[str, Any]:
```

### Client().reorder_receipt_rule_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L261)

```python
def reorder_receipt_rule_set(
    RuleSetName: str,
    RuleNames: List[Any],
) -> Dict[str, Any]:
```

### Client().send_bounce

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L267)

```python
def send_bounce(
    OriginalMessageId: str,
    BounceSender: str,
    BouncedRecipientInfoList: List[Any],
    Explanation: str = None,
    MessageDsn: Dict[str, Any] = None,
    BounceSenderArn: str = None,
) -> Dict[str, Any]:
```

### Client().send_bulk_templated_email

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L279)

```python
def send_bulk_templated_email(
    Source: str,
    Template: str,
    Destinations: List[Any],
    SourceArn: str = None,
    ReplyToAddresses: List[Any] = None,
    ReturnPath: str = None,
    ReturnPathArn: str = None,
    ConfigurationSetName: str = None,
    DefaultTags: List[Any] = None,
    TemplateArn: str = None,
    DefaultTemplateData: str = None,
) -> Dict[str, Any]:
```

### Client().send_custom_verification_email

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L296)

```python
def send_custom_verification_email(
    EmailAddress: str,
    TemplateName: str,
    ConfigurationSetName: str = None,
) -> Dict[str, Any]:
```

### Client().send_email

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L302)

```python
def send_email(
    Source: str,
    Destination: Dict[str, Any],
    Message: Dict[str, Any],
    ReplyToAddresses: List[Any] = None,
    ReturnPath: str = None,
    SourceArn: str = None,
    ReturnPathArn: str = None,
    Tags: List[Any] = None,
    ConfigurationSetName: str = None,
) -> Dict[str, Any]:
```

### Client().send_raw_email

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L317)

```python
def send_raw_email(
    RawMessage: Dict[str, Any],
    Source: str = None,
    Destinations: List[Any] = None,
    FromArn: str = None,
    SourceArn: str = None,
    ReturnPathArn: str = None,
    Tags: List[Any] = None,
    ConfigurationSetName: str = None,
) -> Dict[str, Any]:
```

### Client().send_templated_email

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L331)

```python
def send_templated_email(
    Source: str,
    Destination: Dict[str, Any],
    Template: str,
    TemplateData: str,
    ReplyToAddresses: List[Any] = None,
    ReturnPath: str = None,
    SourceArn: str = None,
    ReturnPathArn: str = None,
    Tags: List[Any] = None,
    ConfigurationSetName: str = None,
    TemplateArn: str = None,
) -> Dict[str, Any]:
```

### Client().set_active_receipt_rule_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L348)

```python
def set_active_receipt_rule_set(RuleSetName: str = None) -> Dict[str, Any]:
```

### Client().set_identity_dkim_enabled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L352)

```python
def set_identity_dkim_enabled(
    Identity: str,
    DkimEnabled: bool,
) -> Dict[str, Any]:
```

### Client().set_identity_feedback_forwarding_enabled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L358)

```python
def set_identity_feedback_forwarding_enabled(
    Identity: str,
    ForwardingEnabled: bool,
) -> Dict[str, Any]:
```

### Client().set_identity_headers_in_notifications_enabled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L364)

```python
def set_identity_headers_in_notifications_enabled(
    Identity: str,
    NotificationType: str,
    Enabled: bool,
) -> Dict[str, Any]:
```

### Client().set_identity_mail_from_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L370)

```python
def set_identity_mail_from_domain(
    Identity: str,
    MailFromDomain: str = None,
    BehaviorOnMXFailure: str = None,
) -> Dict[str, Any]:
```

### Client().set_identity_notification_topic

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L376)

```python
def set_identity_notification_topic(
    Identity: str,
    NotificationType: str,
    SnsTopic: str = None,
) -> Dict[str, Any]:
```

### Client().set_receipt_rule_position

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L382)

```python
def set_receipt_rule_position(
    RuleSetName: str,
    RuleName: str,
    After: str = None,
) -> Dict[str, Any]:
```

### Client().test_render_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L388)

```python
def test_render_template(
    TemplateName: str,
    TemplateData: str,
) -> Dict[str, Any]:
```

### Client().update_account_sending_enabled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L394)

```python
def update_account_sending_enabled(Enabled: bool = None) -> None:
```

### Client().update_configuration_set_event_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L398)

```python
def update_configuration_set_event_destination(
    ConfigurationSetName: str,
    EventDestination: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_configuration_set_reputation_metrics_enabled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L404)

```python
def update_configuration_set_reputation_metrics_enabled(
    ConfigurationSetName: str,
    Enabled: bool,
) -> None:
```

### Client().update_configuration_set_sending_enabled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L410)

```python
def update_configuration_set_sending_enabled(
    ConfigurationSetName: str,
    Enabled: bool,
) -> None:
```

### Client().update_configuration_set_tracking_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L416)

```python
def update_configuration_set_tracking_options(
    ConfigurationSetName: str,
    TrackingOptions: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_custom_verification_email_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L422)

```python
def update_custom_verification_email_template(
    TemplateName: str,
    FromEmailAddress: str = None,
    TemplateSubject: str = None,
    TemplateContent: str = None,
    SuccessRedirectionURL: str = None,
    FailureRedirectionURL: str = None,
) -> None:
```

### Client().update_receipt_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L434)

```python
def update_receipt_rule(
    RuleSetName: str,
    Rule: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L440)

```python
def update_template(Template: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().verify_domain_dkim

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L444)

```python
def verify_domain_dkim(Domain: str) -> Dict[str, Any]:
```

### Client().verify_domain_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L448)

```python
def verify_domain_identity(Domain: str) -> Dict[str, Any]:
```

### Client().verify_email_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L452)

```python
def verify_email_address(EmailAddress: str) -> None:
```

### Client().verify_email_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ses/client.py#L456)

```python
def verify_email_identity(EmailAddress: str) -> Dict[str, Any]:
```
