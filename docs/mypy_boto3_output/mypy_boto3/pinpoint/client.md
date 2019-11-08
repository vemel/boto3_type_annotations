# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.pinpoint.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Pinpoint](index.md#pinpoint) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_app](#clientcreate_app)
        - [Client().create_campaign](#clientcreate_campaign)
        - [Client().create_email_template](#clientcreate_email_template)
        - [Client().create_export_job](#clientcreate_export_job)
        - [Client().create_import_job](#clientcreate_import_job)
        - [Client().create_journey](#clientcreate_journey)
        - [Client().create_push_template](#clientcreate_push_template)
        - [Client().create_segment](#clientcreate_segment)
        - [Client().create_sms_template](#clientcreate_sms_template)
        - [Client().delete_adm_channel](#clientdelete_adm_channel)
        - [Client().delete_apns_channel](#clientdelete_apns_channel)
        - [Client().delete_apns_sandbox_channel](#clientdelete_apns_sandbox_channel)
        - [Client().delete_apns_voip_channel](#clientdelete_apns_voip_channel)
        - [Client().delete_apns_voip_sandbox_channel](#clientdelete_apns_voip_sandbox_channel)
        - [Client().delete_app](#clientdelete_app)
        - [Client().delete_baidu_channel](#clientdelete_baidu_channel)
        - [Client().delete_campaign](#clientdelete_campaign)
        - [Client().delete_email_channel](#clientdelete_email_channel)
        - [Client().delete_email_template](#clientdelete_email_template)
        - [Client().delete_endpoint](#clientdelete_endpoint)
        - [Client().delete_event_stream](#clientdelete_event_stream)
        - [Client().delete_gcm_channel](#clientdelete_gcm_channel)
        - [Client().delete_journey](#clientdelete_journey)
        - [Client().delete_push_template](#clientdelete_push_template)
        - [Client().delete_segment](#clientdelete_segment)
        - [Client().delete_sms_channel](#clientdelete_sms_channel)
        - [Client().delete_sms_template](#clientdelete_sms_template)
        - [Client().delete_user_endpoints](#clientdelete_user_endpoints)
        - [Client().delete_voice_channel](#clientdelete_voice_channel)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_adm_channel](#clientget_adm_channel)
        - [Client().get_apns_channel](#clientget_apns_channel)
        - [Client().get_apns_sandbox_channel](#clientget_apns_sandbox_channel)
        - [Client().get_apns_voip_channel](#clientget_apns_voip_channel)
        - [Client().get_apns_voip_sandbox_channel](#clientget_apns_voip_sandbox_channel)
        - [Client().get_app](#clientget_app)
        - [Client().get_application_date_range_kpi](#clientget_application_date_range_kpi)
        - [Client().get_application_settings](#clientget_application_settings)
        - [Client().get_apps](#clientget_apps)
        - [Client().get_baidu_channel](#clientget_baidu_channel)
        - [Client().get_campaign](#clientget_campaign)
        - [Client().get_campaign_activities](#clientget_campaign_activities)
        - [Client().get_campaign_date_range_kpi](#clientget_campaign_date_range_kpi)
        - [Client().get_campaign_version](#clientget_campaign_version)
        - [Client().get_campaign_versions](#clientget_campaign_versions)
        - [Client().get_campaigns](#clientget_campaigns)
        - [Client().get_channels](#clientget_channels)
        - [Client().get_email_channel](#clientget_email_channel)
        - [Client().get_email_template](#clientget_email_template)
        - [Client().get_endpoint](#clientget_endpoint)
        - [Client().get_event_stream](#clientget_event_stream)
        - [Client().get_export_job](#clientget_export_job)
        - [Client().get_export_jobs](#clientget_export_jobs)
        - [Client().get_gcm_channel](#clientget_gcm_channel)
        - [Client().get_import_job](#clientget_import_job)
        - [Client().get_import_jobs](#clientget_import_jobs)
        - [Client().get_journey](#clientget_journey)
        - [Client().get_journey_date_range_kpi](#clientget_journey_date_range_kpi)
        - [Client().get_journey_execution_activity_metrics](#clientget_journey_execution_activity_metrics)
        - [Client().get_journey_execution_metrics](#clientget_journey_execution_metrics)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_push_template](#clientget_push_template)
        - [Client().get_segment](#clientget_segment)
        - [Client().get_segment_export_jobs](#clientget_segment_export_jobs)
        - [Client().get_segment_import_jobs](#clientget_segment_import_jobs)
        - [Client().get_segment_version](#clientget_segment_version)
        - [Client().get_segment_versions](#clientget_segment_versions)
        - [Client().get_segments](#clientget_segments)
        - [Client().get_sms_channel](#clientget_sms_channel)
        - [Client().get_sms_template](#clientget_sms_template)
        - [Client().get_user_endpoints](#clientget_user_endpoints)
        - [Client().get_voice_channel](#clientget_voice_channel)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_journeys](#clientlist_journeys)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_templates](#clientlist_templates)
        - [Client().phone_number_validate](#clientphone_number_validate)
        - [Client().put_event_stream](#clientput_event_stream)
        - [Client().put_events](#clientput_events)
        - [Client().remove_attributes](#clientremove_attributes)
        - [Client().send_messages](#clientsend_messages)
        - [Client().send_users_messages](#clientsend_users_messages)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_adm_channel](#clientupdate_adm_channel)
        - [Client().update_apns_channel](#clientupdate_apns_channel)
        - [Client().update_apns_sandbox_channel](#clientupdate_apns_sandbox_channel)
        - [Client().update_apns_voip_channel](#clientupdate_apns_voip_channel)
        - [Client().update_apns_voip_sandbox_channel](#clientupdate_apns_voip_sandbox_channel)
        - [Client().update_application_settings](#clientupdate_application_settings)
        - [Client().update_baidu_channel](#clientupdate_baidu_channel)
        - [Client().update_campaign](#clientupdate_campaign)
        - [Client().update_email_channel](#clientupdate_email_channel)
        - [Client().update_email_template](#clientupdate_email_template)
        - [Client().update_endpoint](#clientupdate_endpoint)
        - [Client().update_endpoints_batch](#clientupdate_endpoints_batch)
        - [Client().update_gcm_channel](#clientupdate_gcm_channel)
        - [Client().update_journey](#clientupdate_journey)
        - [Client().update_journey_state](#clientupdate_journey_state)
        - [Client().update_push_template](#clientupdate_push_template)
        - [Client().update_segment](#clientupdate_segment)
        - [Client().update_sms_channel](#clientupdate_sms_channel)
        - [Client().update_sms_template](#clientupdate_sms_template)
        - [Client().update_voice_channel](#clientupdate_voice_channel)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L20)

```python
def create_app(CreateApplicationRequest: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().create_campaign

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L24)

```python
def create_campaign(
    ApplicationId: str,
    WriteCampaignRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_email_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L30)

```python
def create_email_template(
    EmailTemplateRequest: Dict[str, Any],
    TemplateName: str,
) -> Dict[str, Any]:
```

### Client().create_export_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L36)

```python
def create_export_job(
    ApplicationId: str,
    ExportJobRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L42)

```python
def create_import_job(
    ApplicationId: str,
    ImportJobRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_journey

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L48)

```python
def create_journey(
    ApplicationId: str,
    WriteJourneyRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_push_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L54)

```python
def create_push_template(
    PushNotificationTemplateRequest: Dict[str, Any],
    TemplateName: str,
) -> Dict[str, Any]:
```

### Client().create_segment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L60)

```python
def create_segment(
    ApplicationId: str,
    WriteSegmentRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_sms_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L66)

```python
def create_sms_template(
    SMSTemplateRequest: Dict[str, Any],
    TemplateName: str,
) -> Dict[str, Any]:
```

### Client().delete_adm_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L72)

```python
def delete_adm_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_apns_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L76)

```python
def delete_apns_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_apns_sandbox_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L80)

```python
def delete_apns_sandbox_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_apns_voip_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L84)

```python
def delete_apns_voip_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_apns_voip_sandbox_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L88)

```python
def delete_apns_voip_sandbox_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L92)

```python
def delete_app(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_baidu_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L96)

```python
def delete_baidu_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_campaign

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L100)

```python
def delete_campaign(ApplicationId: str, CampaignId: str) -> Dict[str, Any]:
```

### Client().delete_email_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L104)

```python
def delete_email_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_email_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L108)

```python
def delete_email_template(TemplateName: str) -> Dict[str, Any]:
```

### Client().delete_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L112)

```python
def delete_endpoint(ApplicationId: str, EndpointId: str) -> Dict[str, Any]:
```

### Client().delete_event_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L116)

```python
def delete_event_stream(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_gcm_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L120)

```python
def delete_gcm_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_journey

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L124)

```python
def delete_journey(ApplicationId: str, JourneyId: str) -> Dict[str, Any]:
```

### Client().delete_push_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L128)

```python
def delete_push_template(TemplateName: str) -> Dict[str, Any]:
```

### Client().delete_segment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L132)

```python
def delete_segment(ApplicationId: str, SegmentId: str) -> Dict[str, Any]:
```

### Client().delete_sms_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L136)

```python
def delete_sms_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().delete_sms_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L140)

```python
def delete_sms_template(TemplateName: str) -> Dict[str, Any]:
```

### Client().delete_user_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L144)

```python
def delete_user_endpoints(ApplicationId: str, UserId: str) -> Dict[str, Any]:
```

### Client().delete_voice_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L148)

```python
def delete_voice_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L152)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_adm_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L162)

```python
def get_adm_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_apns_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L166)

```python
def get_apns_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_apns_sandbox_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L170)

```python
def get_apns_sandbox_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_apns_voip_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L174)

```python
def get_apns_voip_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_apns_voip_sandbox_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L178)

```python
def get_apns_voip_sandbox_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L182)

```python
def get_app(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_application_date_range_kpi

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L186)

```python
def get_application_date_range_kpi(
    ApplicationId: str,
    KpiName: str,
    EndTime: datetime = None,
    NextToken: str = None,
    PageSize: str = None,
    StartTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().get_application_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L198)

```python
def get_application_settings(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_apps

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L202)

```python
def get_apps(PageSize: str = None, Token: str = None) -> Dict[str, Any]:
```

### Client().get_baidu_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L206)

```python
def get_baidu_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_campaign

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L210)

```python
def get_campaign(ApplicationId: str, CampaignId: str) -> Dict[str, Any]:
```

### Client().get_campaign_activities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L214)

```python
def get_campaign_activities(
    ApplicationId: str,
    CampaignId: str,
    PageSize: str = None,
    Token: str = None,
) -> Dict[str, Any]:
```

### Client().get_campaign_date_range_kpi

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L224)

```python
def get_campaign_date_range_kpi(
    ApplicationId: str,
    CampaignId: str,
    KpiName: str,
    EndTime: datetime = None,
    NextToken: str = None,
    PageSize: str = None,
    StartTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().get_campaign_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L237)

```python
def get_campaign_version(
    ApplicationId: str,
    CampaignId: str,
    Version: str,
) -> Dict[str, Any]:
```

### Client().get_campaign_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L243)

```python
def get_campaign_versions(
    ApplicationId: str,
    CampaignId: str,
    PageSize: str = None,
    Token: str = None,
) -> Dict[str, Any]:
```

### Client().get_campaigns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L253)

```python
def get_campaigns(
    ApplicationId: str,
    PageSize: str = None,
    Token: str = None,
) -> Dict[str, Any]:
```

### Client().get_channels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L259)

```python
def get_channels(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_email_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L263)

```python
def get_email_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_email_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L267)

```python
def get_email_template(TemplateName: str) -> Dict[str, Any]:
```

### Client().get_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L271)

```python
def get_endpoint(ApplicationId: str, EndpointId: str) -> Dict[str, Any]:
```

### Client().get_event_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L275)

```python
def get_event_stream(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_export_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L279)

```python
def get_export_job(ApplicationId: str, JobId: str) -> Dict[str, Any]:
```

### Client().get_export_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L283)

```python
def get_export_jobs(
    ApplicationId: str,
    PageSize: str = None,
    Token: str = None,
) -> Dict[str, Any]:
```

### Client().get_gcm_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L289)

```python
def get_gcm_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L293)

```python
def get_import_job(ApplicationId: str, JobId: str) -> Dict[str, Any]:
```

### Client().get_import_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L297)

```python
def get_import_jobs(
    ApplicationId: str,
    PageSize: str = None,
    Token: str = None,
) -> Dict[str, Any]:
```

### Client().get_journey

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L303)

```python
def get_journey(ApplicationId: str, JourneyId: str) -> Dict[str, Any]:
```

### Client().get_journey_date_range_kpi

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L307)

```python
def get_journey_date_range_kpi(
    ApplicationId: str,
    JourneyId: str,
    KpiName: str,
    EndTime: datetime = None,
    NextToken: str = None,
    PageSize: str = None,
    StartTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().get_journey_execution_activity_metrics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L320)

```python
def get_journey_execution_activity_metrics(
    ApplicationId: str,
    JourneyActivityId: str,
    JourneyId: str,
    NextToken: str = None,
    PageSize: str = None,
) -> Dict[str, Any]:
```

### Client().get_journey_execution_metrics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L331)

```python
def get_journey_execution_metrics(
    ApplicationId: str,
    JourneyId: str,
    NextToken: str = None,
    PageSize: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L341)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_push_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L345)

```python
def get_push_template(TemplateName: str) -> Dict[str, Any]:
```

### Client().get_segment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L349)

```python
def get_segment(ApplicationId: str, SegmentId: str) -> Dict[str, Any]:
```

### Client().get_segment_export_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L353)

```python
def get_segment_export_jobs(
    ApplicationId: str,
    SegmentId: str,
    PageSize: str = None,
    Token: str = None,
) -> Dict[str, Any]:
```

### Client().get_segment_import_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L363)

```python
def get_segment_import_jobs(
    ApplicationId: str,
    SegmentId: str,
    PageSize: str = None,
    Token: str = None,
) -> Dict[str, Any]:
```

### Client().get_segment_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L373)

```python
def get_segment_version(
    ApplicationId: str,
    SegmentId: str,
    Version: str,
) -> Dict[str, Any]:
```

### Client().get_segment_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L379)

```python
def get_segment_versions(
    ApplicationId: str,
    SegmentId: str,
    PageSize: str = None,
    Token: str = None,
) -> Dict[str, Any]:
```

### Client().get_segments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L389)

```python
def get_segments(
    ApplicationId: str,
    PageSize: str = None,
    Token: str = None,
) -> Dict[str, Any]:
```

### Client().get_sms_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L395)

```python
def get_sms_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_sms_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L399)

```python
def get_sms_template(TemplateName: str) -> Dict[str, Any]:
```

### Client().get_user_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L403)

```python
def get_user_endpoints(ApplicationId: str, UserId: str) -> Dict[str, Any]:
```

### Client().get_voice_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L407)

```python
def get_voice_channel(ApplicationId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L411)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_journeys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L415)

```python
def list_journeys(
    ApplicationId: str,
    PageSize: str = None,
    Token: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L421)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().list_templates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L425)

```python
def list_templates(
    NextToken: str = None,
    PageSize: str = None,
    Prefix: str = None,
    TemplateType: str = None,
) -> Dict[str, Any]:
```

### Client().phone_number_validate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L435)

```python
def phone_number_validate(
    NumberValidateRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_event_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L441)

```python
def put_event_stream(
    ApplicationId: str,
    WriteEventStream: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L447)

```python
def put_events(
    ApplicationId: str,
    EventsRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().remove_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L453)

```python
def remove_attributes(
    ApplicationId: str,
    AttributeType: str,
    UpdateAttributesRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().send_messages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L462)

```python
def send_messages(
    ApplicationId: str,
    MessageRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().send_users_messages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L468)

```python
def send_users_messages(
    ApplicationId: str,
    SendUsersMessageRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L474)

```python
def tag_resource(ResourceArn: str, TagsModel: Dict[str, Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L478)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().update_adm_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L482)

```python
def update_adm_channel(
    ADMChannelRequest: Dict[str, Any],
    ApplicationId: str,
) -> Dict[str, Any]:
```

### Client().update_apns_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L488)

```python
def update_apns_channel(
    APNSChannelRequest: Dict[str, Any],
    ApplicationId: str,
) -> Dict[str, Any]:
```

### Client().update_apns_sandbox_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L494)

```python
def update_apns_sandbox_channel(
    APNSSandboxChannelRequest: Dict[str, Any],
    ApplicationId: str,
) -> Dict[str, Any]:
```

### Client().update_apns_voip_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L500)

```python
def update_apns_voip_channel(
    APNSVoipChannelRequest: Dict[str, Any],
    ApplicationId: str,
) -> Dict[str, Any]:
```

### Client().update_apns_voip_sandbox_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L506)

```python
def update_apns_voip_sandbox_channel(
    APNSVoipSandboxChannelRequest: Dict[str, Any],
    ApplicationId: str,
) -> Dict[str, Any]:
```

### Client().update_application_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L512)

```python
def update_application_settings(
    ApplicationId: str,
    WriteApplicationSettingsRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_baidu_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L518)

```python
def update_baidu_channel(
    ApplicationId: str,
    BaiduChannelRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_campaign

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L524)

```python
def update_campaign(
    ApplicationId: str,
    CampaignId: str,
    WriteCampaignRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_email_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L530)

```python
def update_email_channel(
    ApplicationId: str,
    EmailChannelRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_email_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L536)

```python
def update_email_template(
    EmailTemplateRequest: Dict[str, Any],
    TemplateName: str,
) -> Dict[str, Any]:
```

### Client().update_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L542)

```python
def update_endpoint(
    ApplicationId: str,
    EndpointId: str,
    EndpointRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_endpoints_batch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L548)

```python
def update_endpoints_batch(
    ApplicationId: str,
    EndpointBatchRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_gcm_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L554)

```python
def update_gcm_channel(
    ApplicationId: str,
    GCMChannelRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_journey

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L560)

```python
def update_journey(
    ApplicationId: str,
    JourneyId: str,
    WriteJourneyRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_journey_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L566)

```python
def update_journey_state(
    ApplicationId: str,
    JourneyId: str,
    JourneyStateRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_push_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L572)

```python
def update_push_template(
    PushNotificationTemplateRequest: Dict[str, Any],
    TemplateName: str,
) -> Dict[str, Any]:
```

### Client().update_segment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L578)

```python
def update_segment(
    ApplicationId: str,
    SegmentId: str,
    WriteSegmentRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_sms_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L584)

```python
def update_sms_channel(
    ApplicationId: str,
    SMSChannelRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_sms_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L590)

```python
def update_sms_template(
    SMSTemplateRequest: Dict[str, Any],
    TemplateName: str,
) -> Dict[str, Any]:
```

### Client().update_voice_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pinpoint/client.py#L596)

```python
def update_voice_channel(
    ApplicationId: str,
    VoiceChannelRequest: Dict[str, Any],
) -> Dict[str, Any]:
```
