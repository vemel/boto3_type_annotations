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


    def create_app(
        self,
        CreateApplicationRequest: Dict,
    ) -> Dict:
        pass


    def create_campaign(
        self,
        ApplicationId: str,
        WriteCampaignRequest: Dict,
    ) -> Dict:
        pass


    def create_email_template(
        self,
        EmailTemplateRequest: Dict,
        TemplateName: str,
    ) -> Dict:
        pass


    def create_export_job(
        self,
        ApplicationId: str,
        ExportJobRequest: Dict,
    ) -> Dict:
        pass


    def create_import_job(
        self,
        ApplicationId: str,
        ImportJobRequest: Dict,
    ) -> Dict:
        pass


    def create_journey(
        self,
        ApplicationId: str,
        WriteJourneyRequest: Dict,
    ) -> Dict:
        pass


    def create_push_template(
        self,
        PushNotificationTemplateRequest: Dict,
        TemplateName: str,
    ) -> Dict:
        pass


    def create_segment(
        self,
        ApplicationId: str,
        WriteSegmentRequest: Dict,
    ) -> Dict:
        pass


    def create_sms_template(
        self,
        SMSTemplateRequest: Dict,
        TemplateName: str,
    ) -> Dict:
        pass


    def delete_adm_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_apns_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_apns_sandbox_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_apns_voip_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_apns_voip_sandbox_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_app(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_baidu_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_campaign(
        self,
        ApplicationId: str,
        CampaignId: str,
    ) -> Dict:
        pass


    def delete_email_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_email_template(
        self,
        TemplateName: str,
    ) -> Dict:
        pass


    def delete_endpoint(
        self,
        ApplicationId: str,
        EndpointId: str,
    ) -> Dict:
        pass


    def delete_event_stream(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_gcm_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_journey(
        self,
        ApplicationId: str,
        JourneyId: str,
    ) -> Dict:
        pass


    def delete_push_template(
        self,
        TemplateName: str,
    ) -> Dict:
        pass


    def delete_segment(
        self,
        ApplicationId: str,
        SegmentId: str,
    ) -> Dict:
        pass


    def delete_sms_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def delete_sms_template(
        self,
        TemplateName: str,
    ) -> Dict:
        pass


    def delete_user_endpoints(
        self,
        ApplicationId: str,
        UserId: str,
    ) -> Dict:
        pass


    def delete_voice_channel(
        self,
        ApplicationId: str,
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


    def get_adm_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_apns_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_apns_sandbox_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_apns_voip_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_apns_voip_sandbox_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_app(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_application_date_range_kpi(
        self,
        ApplicationId: str,
        KpiName: str,
        EndTime: Optional[datetime] = None,
        NextToken: Optional[str] = None,
        PageSize: Optional[str] = None,
        StartTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def get_application_settings(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_apps(
        self,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def get_baidu_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_campaign(
        self,
        ApplicationId: str,
        CampaignId: str,
    ) -> Dict:
        pass


    def get_campaign_activities(
        self,
        ApplicationId: str,
        CampaignId: str,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def get_campaign_date_range_kpi(
        self,
        ApplicationId: str,
        CampaignId: str,
        KpiName: str,
        EndTime: Optional[datetime] = None,
        NextToken: Optional[str] = None,
        PageSize: Optional[str] = None,
        StartTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def get_campaign_version(
        self,
        ApplicationId: str,
        CampaignId: str,
        Version: str,
    ) -> Dict:
        pass


    def get_campaign_versions(
        self,
        ApplicationId: str,
        CampaignId: str,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def get_campaigns(
        self,
        ApplicationId: str,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def get_channels(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_email_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_email_template(
        self,
        TemplateName: str,
    ) -> Dict:
        pass


    def get_endpoint(
        self,
        ApplicationId: str,
        EndpointId: str,
    ) -> Dict:
        pass


    def get_event_stream(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_export_job(
        self,
        ApplicationId: str,
        JobId: str,
    ) -> Dict:
        pass


    def get_export_jobs(
        self,
        ApplicationId: str,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def get_gcm_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_import_job(
        self,
        ApplicationId: str,
        JobId: str,
    ) -> Dict:
        pass


    def get_import_jobs(
        self,
        ApplicationId: str,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def get_journey(
        self,
        ApplicationId: str,
        JourneyId: str,
    ) -> Dict:
        pass


    def get_journey_date_range_kpi(
        self,
        ApplicationId: str,
        JourneyId: str,
        KpiName: str,
        EndTime: Optional[datetime] = None,
        NextToken: Optional[str] = None,
        PageSize: Optional[str] = None,
        StartTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def get_journey_execution_activity_metrics(
        self,
        ApplicationId: str,
        JourneyActivityId: str,
        JourneyId: str,
        NextToken: Optional[str] = None,
        PageSize: Optional[str] = None,
    ) -> Dict:
        pass


    def get_journey_execution_metrics(
        self,
        ApplicationId: str,
        JourneyId: str,
        NextToken: Optional[str] = None,
        PageSize: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_push_template(
        self,
        TemplateName: str,
    ) -> Dict:
        pass


    def get_segment(
        self,
        ApplicationId: str,
        SegmentId: str,
    ) -> Dict:
        pass


    def get_segment_export_jobs(
        self,
        ApplicationId: str,
        SegmentId: str,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def get_segment_import_jobs(
        self,
        ApplicationId: str,
        SegmentId: str,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def get_segment_version(
        self,
        ApplicationId: str,
        SegmentId: str,
        Version: str,
    ) -> Dict:
        pass


    def get_segment_versions(
        self,
        ApplicationId: str,
        SegmentId: str,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def get_segments(
        self,
        ApplicationId: str,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def get_sms_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_sms_template(
        self,
        TemplateName: str,
    ) -> Dict:
        pass


    def get_user_endpoints(
        self,
        ApplicationId: str,
        UserId: str,
    ) -> Dict:
        pass


    def get_voice_channel(
        self,
        ApplicationId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_journeys(
        self,
        ApplicationId: str,
        PageSize: Optional[str] = None,
        Token: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def list_templates(
        self,
        NextToken: Optional[str] = None,
        PageSize: Optional[str] = None,
        Prefix: Optional[str] = None,
        TemplateType: Optional[str] = None,
    ) -> Dict:
        pass


    def phone_number_validate(
        self,
        NumberValidateRequest: Dict,
    ) -> Dict:
        pass


    def put_event_stream(
        self,
        ApplicationId: str,
        WriteEventStream: Dict,
    ) -> Dict:
        pass


    def put_events(
        self,
        ApplicationId: str,
        EventsRequest: Dict,
    ) -> Dict:
        pass


    def remove_attributes(
        self,
        ApplicationId: str,
        AttributeType: str,
        UpdateAttributesRequest: Dict,
    ) -> Dict:
        pass


    def send_messages(
        self,
        ApplicationId: str,
        MessageRequest: Dict,
    ) -> Dict:
        pass


    def send_users_messages(
        self,
        ApplicationId: str,
        SendUsersMessageRequest: Dict,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        TagsModel: Dict,
    ):
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass


    def update_adm_channel(
        self,
        ADMChannelRequest: Dict,
        ApplicationId: str,
    ) -> Dict:
        pass


    def update_apns_channel(
        self,
        APNSChannelRequest: Dict,
        ApplicationId: str,
    ) -> Dict:
        pass


    def update_apns_sandbox_channel(
        self,
        APNSSandboxChannelRequest: Dict,
        ApplicationId: str,
    ) -> Dict:
        pass


    def update_apns_voip_channel(
        self,
        APNSVoipChannelRequest: Dict,
        ApplicationId: str,
    ) -> Dict:
        pass


    def update_apns_voip_sandbox_channel(
        self,
        APNSVoipSandboxChannelRequest: Dict,
        ApplicationId: str,
    ) -> Dict:
        pass


    def update_application_settings(
        self,
        ApplicationId: str,
        WriteApplicationSettingsRequest: Dict,
    ) -> Dict:
        pass


    def update_baidu_channel(
        self,
        ApplicationId: str,
        BaiduChannelRequest: Dict,
    ) -> Dict:
        pass


    def update_campaign(
        self,
        ApplicationId: str,
        CampaignId: str,
        WriteCampaignRequest: Dict,
    ) -> Dict:
        pass


    def update_email_channel(
        self,
        ApplicationId: str,
        EmailChannelRequest: Dict,
    ) -> Dict:
        pass


    def update_email_template(
        self,
        EmailTemplateRequest: Dict,
        TemplateName: str,
    ) -> Dict:
        pass


    def update_endpoint(
        self,
        ApplicationId: str,
        EndpointId: str,
        EndpointRequest: Dict,
    ) -> Dict:
        pass


    def update_endpoints_batch(
        self,
        ApplicationId: str,
        EndpointBatchRequest: Dict,
    ) -> Dict:
        pass


    def update_gcm_channel(
        self,
        ApplicationId: str,
        GCMChannelRequest: Dict,
    ) -> Dict:
        pass


    def update_journey(
        self,
        ApplicationId: str,
        JourneyId: str,
        WriteJourneyRequest: Dict,
    ) -> Dict:
        pass


    def update_journey_state(
        self,
        ApplicationId: str,
        JourneyId: str,
        JourneyStateRequest: Dict,
    ) -> Dict:
        pass


    def update_push_template(
        self,
        PushNotificationTemplateRequest: Dict,
        TemplateName: str,
    ) -> Dict:
        pass


    def update_segment(
        self,
        ApplicationId: str,
        SegmentId: str,
        WriteSegmentRequest: Dict,
    ) -> Dict:
        pass


    def update_sms_channel(
        self,
        ApplicationId: str,
        SMSChannelRequest: Dict,
    ) -> Dict:
        pass


    def update_sms_template(
        self,
        SMSTemplateRequest: Dict,
        TemplateName: str,
    ) -> Dict:
        pass


    def update_voice_channel(
        self,
        ApplicationId: str,
        VoiceChannelRequest: Dict,
    ) -> Dict:
        pass

