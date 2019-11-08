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
    def create_app(self, CreateApplicationRequest: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_campaign(
        self, ApplicationId: str, WriteCampaignRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_email_template(
        self, EmailTemplateRequest: Dict[str, Any], TemplateName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_export_job(
        self, ApplicationId: str, ExportJobRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_import_job(
        self, ApplicationId: str, ImportJobRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_journey(
        self, ApplicationId: str, WriteJourneyRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_push_template(
        self, PushNotificationTemplateRequest: Dict[str, Any], TemplateName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_segment(
        self, ApplicationId: str, WriteSegmentRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_sms_template(
        self, SMSTemplateRequest: Dict[str, Any], TemplateName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_adm_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_apns_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_apns_sandbox_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_apns_voip_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_apns_voip_sandbox_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_app(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_baidu_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_campaign(self, ApplicationId: str, CampaignId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_email_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_email_template(self, TemplateName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_endpoint(self, ApplicationId: str, EndpointId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_event_stream(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_gcm_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_journey(self, ApplicationId: str, JourneyId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_push_template(self, TemplateName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_segment(self, ApplicationId: str, SegmentId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_sms_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_sms_template(self, TemplateName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_user_endpoints(self, ApplicationId: str, UserId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_voice_channel(self, ApplicationId: str) -> Dict[str, Any]:
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
    def get_adm_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_apns_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_apns_sandbox_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_apns_voip_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_apns_voip_sandbox_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_app(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_application_date_range_kpi(
        self,
        ApplicationId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_application_settings(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_apps(self, PageSize: str = None, Token: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_baidu_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_campaign(self, ApplicationId: str, CampaignId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_campaign_activities(
        self,
        ApplicationId: str,
        CampaignId: str,
        PageSize: str = None,
        Token: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_campaign_date_range_kpi(
        self,
        ApplicationId: str,
        CampaignId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_campaign_version(
        self, ApplicationId: str, CampaignId: str, Version: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_campaign_versions(
        self,
        ApplicationId: str,
        CampaignId: str,
        PageSize: str = None,
        Token: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_campaigns(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_channels(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_email_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_email_template(self, TemplateName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_endpoint(self, ApplicationId: str, EndpointId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_event_stream(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_export_job(self, ApplicationId: str, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_export_jobs(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_gcm_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_import_job(self, ApplicationId: str, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_import_jobs(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_journey(self, ApplicationId: str, JourneyId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_journey_date_range_kpi(
        self,
        ApplicationId: str,
        JourneyId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_journey_execution_activity_metrics(
        self,
        ApplicationId: str,
        JourneyActivityId: str,
        JourneyId: str,
        NextToken: str = None,
        PageSize: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_journey_execution_metrics(
        self,
        ApplicationId: str,
        JourneyId: str,
        NextToken: str = None,
        PageSize: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_push_template(self, TemplateName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_segment(self, ApplicationId: str, SegmentId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_segment_export_jobs(
        self,
        ApplicationId: str,
        SegmentId: str,
        PageSize: str = None,
        Token: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_segment_import_jobs(
        self,
        ApplicationId: str,
        SegmentId: str,
        PageSize: str = None,
        Token: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_segment_version(
        self, ApplicationId: str, SegmentId: str, Version: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_segment_versions(
        self,
        ApplicationId: str,
        SegmentId: str,
        PageSize: str = None,
        Token: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_segments(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_sms_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_sms_template(self, TemplateName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_user_endpoints(self, ApplicationId: str, UserId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_voice_channel(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_journeys(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_templates(
        self,
        NextToken: str = None,
        PageSize: str = None,
        Prefix: str = None,
        TemplateType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def phone_number_validate(
        self, NumberValidateRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_event_stream(
        self, ApplicationId: str, WriteEventStream: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_events(
        self, ApplicationId: str, EventsRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_attributes(
        self,
        ApplicationId: str,
        AttributeType: str,
        UpdateAttributesRequest: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_messages(
        self, ApplicationId: str, MessageRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_users_messages(
        self, ApplicationId: str, SendUsersMessageRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, TagsModel: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_adm_channel(
        self, ADMChannelRequest: Dict[str, Any], ApplicationId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_apns_channel(
        self, APNSChannelRequest: Dict[str, Any], ApplicationId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_apns_sandbox_channel(
        self, APNSSandboxChannelRequest: Dict[str, Any], ApplicationId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_apns_voip_channel(
        self, APNSVoipChannelRequest: Dict[str, Any], ApplicationId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_apns_voip_sandbox_channel(
        self, APNSVoipSandboxChannelRequest: Dict[str, Any], ApplicationId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_application_settings(
        self, ApplicationId: str, WriteApplicationSettingsRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_baidu_channel(
        self, ApplicationId: str, BaiduChannelRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_campaign(
        self, ApplicationId: str, CampaignId: str, WriteCampaignRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_email_channel(
        self, ApplicationId: str, EmailChannelRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_email_template(
        self, EmailTemplateRequest: Dict[str, Any], TemplateName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_endpoint(
        self, ApplicationId: str, EndpointId: str, EndpointRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_endpoints_batch(
        self, ApplicationId: str, EndpointBatchRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_gcm_channel(
        self, ApplicationId: str, GCMChannelRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_journey(
        self, ApplicationId: str, JourneyId: str, WriteJourneyRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_journey_state(
        self, ApplicationId: str, JourneyId: str, JourneyStateRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_push_template(
        self, PushNotificationTemplateRequest: Dict[str, Any], TemplateName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_segment(
        self, ApplicationId: str, SegmentId: str, WriteSegmentRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_sms_channel(
        self, ApplicationId: str, SMSChannelRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_sms_template(
        self, SMSTemplateRequest: Dict[str, Any], TemplateName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_voice_channel(
        self, ApplicationId: str, VoiceChannelRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass
