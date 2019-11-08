# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.pinpoint_email.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Pinpoint Email](index.md#pinpoint-email) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_configuration_set](#clientcreate_configuration_set)
        - [Client().create_configuration_set_event_destination](#clientcreate_configuration_set_event_destination)
        - [Client().create_dedicated_ip_pool](#clientcreate_dedicated_ip_pool)
        - [Client().create_deliverability_test_report](#clientcreate_deliverability_test_report)
        - [Client().create_email_identity](#clientcreate_email_identity)
        - [Client().delete_configuration_set](#clientdelete_configuration_set)
        - [Client().delete_configuration_set_event_destination](#clientdelete_configuration_set_event_destination)
        - [Client().delete_dedicated_ip_pool](#clientdelete_dedicated_ip_pool)
        - [Client().delete_email_identity](#clientdelete_email_identity)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_account](#clientget_account)
        - [Client().get_blacklist_reports](#clientget_blacklist_reports)
        - [Client().get_configuration_set](#clientget_configuration_set)
        - [Client().get_configuration_set_event_destinations](#clientget_configuration_set_event_destinations)
        - [Client().get_dedicated_ip](#clientget_dedicated_ip)
        - [Client().get_dedicated_ips](#clientget_dedicated_ips)
        - [Client().get_deliverability_dashboard_options](#clientget_deliverability_dashboard_options)
        - [Client().get_deliverability_test_report](#clientget_deliverability_test_report)
        - [Client().get_domain_deliverability_campaign](#clientget_domain_deliverability_campaign)
        - [Client().get_domain_statistics_report](#clientget_domain_statistics_report)
        - [Client().get_email_identity](#clientget_email_identity)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_configuration_sets](#clientlist_configuration_sets)
        - [Client().list_dedicated_ip_pools](#clientlist_dedicated_ip_pools)
        - [Client().list_deliverability_test_reports](#clientlist_deliverability_test_reports)
        - [Client().list_domain_deliverability_campaigns](#clientlist_domain_deliverability_campaigns)
        - [Client().list_email_identities](#clientlist_email_identities)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_account_dedicated_ip_warmup_attributes](#clientput_account_dedicated_ip_warmup_attributes)
        - [Client().put_account_sending_attributes](#clientput_account_sending_attributes)
        - [Client().put_configuration_set_delivery_options](#clientput_configuration_set_delivery_options)
        - [Client().put_configuration_set_reputation_options](#clientput_configuration_set_reputation_options)
        - [Client().put_configuration_set_sending_options](#clientput_configuration_set_sending_options)
        - [Client().put_configuration_set_tracking_options](#clientput_configuration_set_tracking_options)
        - [Client().put_dedicated_ip_in_pool](#clientput_dedicated_ip_in_pool)
        - [Client().put_dedicated_ip_warmup_attributes](#clientput_dedicated_ip_warmup_attributes)
        - [Client().put_deliverability_dashboard_option](#clientput_deliverability_dashboard_option)
        - [Client().put_email_identity_dkim_attributes](#clientput_email_identity_dkim_attributes)
        - [Client().put_email_identity_feedback_attributes](#clientput_email_identity_feedback_attributes)
        - [Client().put_email_identity_mail_from_attributes](#clientput_email_identity_mail_from_attributes)
        - [Client().send_email](#clientsend_email)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_configuration_set_event_destination](#clientupdate_configuration_set_event_destination)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_configuration_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L20)

```python
def create_configuration_set(
    ConfigurationSetName: str,
    TrackingOptions: Dict[str, Any] = None,
    DeliveryOptions: Dict[str, Any] = None,
    ReputationOptions: Dict[str, Any] = None,
    SendingOptions: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_configuration_set_event_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L32)

```python
def create_configuration_set_event_destination(
    ConfigurationSetName: str,
    EventDestinationName: str,
    EventDestination: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_dedicated_ip_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L41)

```python
def create_dedicated_ip_pool(
    PoolName: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_deliverability_test_report

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L47)

```python
def create_deliverability_test_report(
    FromEmailAddress: str,
    Content: Dict[str, Any],
    ReportName: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_email_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L57)

```python
def create_email_identity(
    EmailIdentity: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_configuration_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L63)

```python
def delete_configuration_set(ConfigurationSetName: str) -> Dict[str, Any]:
```

### Client().delete_configuration_set_event_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L67)

```python
def delete_configuration_set_event_destination(
    ConfigurationSetName: str,
    EventDestinationName: str,
) -> Dict[str, Any]:
```

### Client().delete_dedicated_ip_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L73)

```python
def delete_dedicated_ip_pool(PoolName: str) -> Dict[str, Any]:
```

### Client().delete_email_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L77)

```python
def delete_email_identity(EmailIdentity: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L81)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L91)

```python
def get_account() -> Dict[str, Any]:
```

### Client().get_blacklist_reports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L95)

```python
def get_blacklist_reports(BlacklistItemNames: List[Any]) -> Dict[str, Any]:
```

### Client().get_configuration_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L99)

```python
def get_configuration_set(ConfigurationSetName: str) -> Dict[str, Any]:
```

### Client().get_configuration_set_event_destinations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L103)

```python
def get_configuration_set_event_destinations(
    ConfigurationSetName: str,
) -> Dict[str, Any]:
```

### Client().get_dedicated_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L109)

```python
def get_dedicated_ip(Ip: str) -> Dict[str, Any]:
```

### Client().get_dedicated_ips

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L113)

```python
def get_dedicated_ips(
    PoolName: str = None,
    NextToken: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().get_deliverability_dashboard_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L119)

```python
def get_deliverability_dashboard_options() -> Dict[str, Any]:
```

### Client().get_deliverability_test_report

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L123)

```python
def get_deliverability_test_report(ReportId: str) -> Dict[str, Any]:
```

### Client().get_domain_deliverability_campaign

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L127)

```python
def get_domain_deliverability_campaign(CampaignId: str) -> Dict[str, Any]:
```

### Client().get_domain_statistics_report

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L131)

```python
def get_domain_statistics_report(
    Domain: str,
    StartDate: datetime,
    EndDate: datetime,
) -> Dict[str, Any]:
```

### Client().get_email_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L137)

```python
def get_email_identity(EmailIdentity: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L141)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L145)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_configuration_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L149)

```python
def list_configuration_sets(
    NextToken: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().list_dedicated_ip_pools

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L155)

```python
def list_dedicated_ip_pools(
    NextToken: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().list_deliverability_test_reports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L161)

```python
def list_deliverability_test_reports(
    NextToken: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().list_domain_deliverability_campaigns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L167)

```python
def list_domain_deliverability_campaigns(
    StartDate: datetime,
    EndDate: datetime,
    SubscribedDomain: str,
    NextToken: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().list_email_identities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L178)

```python
def list_email_identities(
    NextToken: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L184)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().put_account_dedicated_ip_warmup_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L188)

```python
def put_account_dedicated_ip_warmup_attributes(
    AutoWarmupEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().put_account_sending_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L194)

```python
def put_account_sending_attributes(
    SendingEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().put_configuration_set_delivery_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L200)

```python
def put_configuration_set_delivery_options(
    ConfigurationSetName: str,
    TlsPolicy: str = None,
    SendingPoolName: str = None,
) -> Dict[str, Any]:
```

### Client().put_configuration_set_reputation_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L209)

```python
def put_configuration_set_reputation_options(
    ConfigurationSetName: str,
    ReputationMetricsEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().put_configuration_set_sending_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L215)

```python
def put_configuration_set_sending_options(
    ConfigurationSetName: str,
    SendingEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().put_configuration_set_tracking_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L221)

```python
def put_configuration_set_tracking_options(
    ConfigurationSetName: str,
    CustomRedirectDomain: str = None,
) -> Dict[str, Any]:
```

### Client().put_dedicated_ip_in_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L227)

```python
def put_dedicated_ip_in_pool(
    Ip: str,
    DestinationPoolName: str,
) -> Dict[str, Any]:
```

### Client().put_dedicated_ip_warmup_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L233)

```python
def put_dedicated_ip_warmup_attributes(
    Ip: str,
    WarmupPercentage: int,
) -> Dict[str, Any]:
```

### Client().put_deliverability_dashboard_option

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L239)

```python
def put_deliverability_dashboard_option(
    DashboardEnabled: bool,
    SubscribedDomains: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().put_email_identity_dkim_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L245)

```python
def put_email_identity_dkim_attributes(
    EmailIdentity: str,
    SigningEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().put_email_identity_feedback_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L251)

```python
def put_email_identity_feedback_attributes(
    EmailIdentity: str,
    EmailForwardingEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().put_email_identity_mail_from_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L257)

```python
def put_email_identity_mail_from_attributes(
    EmailIdentity: str,
    MailFromDomain: str = None,
    BehaviorOnMxFailure: str = None,
) -> Dict[str, Any]:
```

### Client().send_email

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L266)

```python
def send_email(
    Destination: Dict[str, Any],
    Content: Dict[str, Any],
    FromEmailAddress: str = None,
    ReplyToAddresses: List[Any] = None,
    FeedbackForwardingEmailAddress: str = None,
    EmailTags: List[Any] = None,
    ConfigurationSetName: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L279)

```python
def tag_resource(ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L283)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_configuration_set_event_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint_email/client.py#L287)

```python
def update_configuration_set_event_destination(
    ConfigurationSetName: str,
    EventDestinationName: str,
    EventDestination: Dict[str, Any],
) -> Dict[str, Any]:
```
