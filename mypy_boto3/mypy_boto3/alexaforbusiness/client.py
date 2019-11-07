from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def approve_skill(
        self,
        SkillId: str,
    ) -> Dict:
        pass


    def associate_contact_with_address_book(
        self,
        ContactArn: str,
        AddressBookArn: str,
    ) -> Dict:
        pass


    def associate_device_with_network_profile(
        self,
        DeviceArn: str,
        NetworkProfileArn: str,
    ) -> Dict:
        pass


    def associate_device_with_room(
        self,
        DeviceArn: Optional[str] = None,
        RoomArn: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_skill_group_with_room(
        self,
        SkillGroupArn: Optional[str] = None,
        RoomArn: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_skill_with_skill_group(
        self,
        SkillId: str,
        SkillGroupArn: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_skill_with_users(
        self,
        SkillId: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_address_book(
        self,
        Name: str,
        Description: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_business_report_schedule(
        self,
        Format: str,
        ContentRange: Dict,
        ScheduleName: Optional[str] = None,
        S3BucketName: Optional[str] = None,
        S3KeyPrefix: Optional[str] = None,
        Recurrence: Optional[Dict] = None,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_conference_provider(
        self,
        ConferenceProviderName: str,
        ConferenceProviderType: str,
        MeetingSetting: Dict,
        IPDialIn: Optional[Dict] = None,
        PSTNDialIn: Optional[Dict] = None,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_contact(
        self,
        FirstName: str,
        DisplayName: Optional[str] = None,
        LastName: Optional[str] = None,
        PhoneNumber: Optional[str] = None,
        PhoneNumbers: Optional[List] = None,
        SipAddresses: Optional[List] = None,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_gateway_group(
        self,
        Name: str,
        ClientRequestToken: str,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_network_profile(
        self,
        NetworkProfileName: str,
        Ssid: str,
        SecurityType: str,
        ClientRequestToken: str,
        Description: Optional[str] = None,
        EapMethod: Optional[str] = None,
        CurrentPassword: Optional[str] = None,
        NextPassword: Optional[str] = None,
        CertificateAuthorityArn: Optional[str] = None,
        TrustAnchors: Optional[List] = None,
    ) -> Dict:
        pass


    def create_profile(
        self,
        ProfileName: str,
        Timezone: str,
        Address: str,
        DistanceUnit: str,
        TemperatureUnit: str,
        WakeWord: str,
        Locale: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        SetupModeDisabled: Optional[bool] = None,
        MaxVolumeLimit: Optional[int] = None,
        PSTNEnabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_room(
        self,
        RoomName: str,
        Description: Optional[str] = None,
        ProfileArn: Optional[str] = None,
        ProviderCalendarId: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_skill_group(
        self,
        SkillGroupName: str,
        Description: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_user(
        self,
        UserId: str,
        FirstName: Optional[str] = None,
        LastName: Optional[str] = None,
        Email: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_address_book(
        self,
        AddressBookArn: str,
    ) -> Dict:
        pass


    def delete_business_report_schedule(
        self,
        ScheduleArn: str,
    ) -> Dict:
        pass


    def delete_conference_provider(
        self,
        ConferenceProviderArn: str,
    ) -> Dict:
        pass


    def delete_contact(
        self,
        ContactArn: str,
    ) -> Dict:
        pass


    def delete_device(
        self,
        DeviceArn: str,
    ) -> Dict:
        pass


    def delete_device_usage_data(
        self,
        DeviceArn: str,
        DeviceUsageType: str,
    ) -> Dict:
        pass


    def delete_gateway_group(
        self,
        GatewayGroupArn: str,
    ) -> Dict:
        pass


    def delete_network_profile(
        self,
        NetworkProfileArn: str,
    ) -> Dict:
        pass


    def delete_profile(
        self,
        ProfileArn: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_room(
        self,
        RoomArn: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_room_skill_parameter(
        self,
        SkillId: str,
        ParameterKey: str,
        RoomArn: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_skill_authorization(
        self,
        SkillId: str,
        RoomArn: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_skill_group(
        self,
        SkillGroupArn: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_user(
        self,
        EnrollmentId: str,
        UserArn: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_contact_from_address_book(
        self,
        ContactArn: str,
        AddressBookArn: str,
    ) -> Dict:
        pass


    def disassociate_device_from_room(
        self,
        DeviceArn: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_skill_from_skill_group(
        self,
        SkillId: str,
        SkillGroupArn: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_skill_from_users(
        self,
        SkillId: str,
    ) -> Dict:
        pass


    def disassociate_skill_group_from_room(
        self,
        SkillGroupArn: Optional[str] = None,
        RoomArn: Optional[str] = None,
    ) -> Dict:
        pass


    def forget_smart_home_appliances(
        self,
        RoomArn: str,
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


    def get_address_book(
        self,
        AddressBookArn: str,
    ) -> Dict:
        pass


    def get_conference_preference(
        self,
    ) -> Dict:
        pass


    def get_conference_provider(
        self,
        ConferenceProviderArn: str,
    ) -> Dict:
        pass


    def get_contact(
        self,
        ContactArn: str,
    ) -> Dict:
        pass


    def get_device(
        self,
        DeviceArn: Optional[str] = None,
    ) -> Dict:
        pass


    def get_gateway(
        self,
        GatewayArn: str,
    ) -> Dict:
        pass


    def get_gateway_group(
        self,
        GatewayGroupArn: str,
    ) -> Dict:
        pass


    def get_invitation_configuration(
        self,
    ) -> Dict:
        pass


    def get_network_profile(
        self,
        NetworkProfileArn: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_profile(
        self,
        ProfileArn: Optional[str] = None,
    ) -> Dict:
        pass


    def get_room(
        self,
        RoomArn: Optional[str] = None,
    ) -> Dict:
        pass


    def get_room_skill_parameter(
        self,
        SkillId: str,
        ParameterKey: str,
        RoomArn: Optional[str] = None,
    ) -> Dict:
        pass


    def get_skill_group(
        self,
        SkillGroupArn: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_business_report_schedules(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_conference_providers(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_device_events(
        self,
        DeviceArn: str,
        EventType: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_gateway_groups(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_gateways(
        self,
        GatewayGroupArn: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_skills(
        self,
        SkillGroupArn: Optional[str] = None,
        EnablementType: Optional[str] = None,
        SkillType: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_skills_store_categories(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_skills_store_skills_by_category(
        self,
        CategoryId: int,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_smart_home_appliances(
        self,
        RoomArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags(
        self,
        Arn: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def put_conference_preference(
        self,
        ConferencePreference: Dict,
    ) -> Dict:
        pass


    def put_invitation_configuration(
        self,
        OrganizationName: str,
        ContactEmail: Optional[str] = None,
        PrivateSkillIds: Optional[List] = None,
    ) -> Dict:
        pass


    def put_room_skill_parameter(
        self,
        SkillId: str,
        RoomSkillParameter: Dict,
        RoomArn: Optional[str] = None,
    ) -> Dict:
        pass


    def put_skill_authorization(
        self,
        AuthorizationResult: Dict,
        SkillId: str,
        RoomArn: Optional[str] = None,
    ) -> Dict:
        pass


    def register_avs_device(
        self,
        ClientId: str,
        UserCode: str,
        ProductId: str,
        DeviceSerialNumber: str,
        AmazonId: str,
    ) -> Dict:
        pass


    def reject_skill(
        self,
        SkillId: str,
    ) -> Dict:
        pass


    def resolve_room(
        self,
        UserId: str,
        SkillId: str,
    ) -> Dict:
        pass


    def revoke_invitation(
        self,
        UserArn: Optional[str] = None,
        EnrollmentId: Optional[str] = None,
    ) -> Dict:
        pass


    def search_address_books(
        self,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def search_contacts(
        self,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def search_devices(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
    ) -> Dict:
        pass


    def search_network_profiles(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
    ) -> Dict:
        pass


    def search_profiles(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
    ) -> Dict:
        pass


    def search_rooms(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
    ) -> Dict:
        pass


    def search_skill_groups(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
    ) -> Dict:
        pass


    def search_users(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
    ) -> Dict:
        pass


    def send_announcement(
        self,
        RoomFilters: List,
        Content: Dict,
        ClientRequestToken: str,
        TimeToLiveInSeconds: Optional[int] = None,
    ) -> Dict:
        pass


    def send_invitation(
        self,
        UserArn: Optional[str] = None,
    ) -> Dict:
        pass


    def start_device_sync(
        self,
        Features: List,
        RoomArn: Optional[str] = None,
        DeviceArn: Optional[str] = None,
    ) -> Dict:
        pass


    def start_smart_home_appliance_discovery(
        self,
        RoomArn: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        Arn: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        Arn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_address_book(
        self,
        AddressBookArn: str,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_business_report_schedule(
        self,
        ScheduleArn: str,
        S3BucketName: Optional[str] = None,
        S3KeyPrefix: Optional[str] = None,
        Format: Optional[str] = None,
        ScheduleName: Optional[str] = None,
        Recurrence: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_conference_provider(
        self,
        ConferenceProviderArn: str,
        ConferenceProviderType: str,
        MeetingSetting: Dict,
        IPDialIn: Optional[Dict] = None,
        PSTNDialIn: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_contact(
        self,
        ContactArn: str,
        DisplayName: Optional[str] = None,
        FirstName: Optional[str] = None,
        LastName: Optional[str] = None,
        PhoneNumber: Optional[str] = None,
        PhoneNumbers: Optional[List] = None,
        SipAddresses: Optional[List] = None,
    ) -> Dict:
        pass


    def update_device(
        self,
        DeviceArn: Optional[str] = None,
        DeviceName: Optional[str] = None,
    ) -> Dict:
        pass


    def update_gateway(
        self,
        GatewayArn: str,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        SoftwareVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def update_gateway_group(
        self,
        GatewayGroupArn: str,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_network_profile(
        self,
        NetworkProfileArn: str,
        NetworkProfileName: Optional[str] = None,
        Description: Optional[str] = None,
        CurrentPassword: Optional[str] = None,
        NextPassword: Optional[str] = None,
        CertificateAuthorityArn: Optional[str] = None,
        TrustAnchors: Optional[List] = None,
    ) -> Dict:
        pass


    def update_profile(
        self,
        ProfileArn: Optional[str] = None,
        ProfileName: Optional[str] = None,
        IsDefault: Optional[bool] = None,
        Timezone: Optional[str] = None,
        Address: Optional[str] = None,
        DistanceUnit: Optional[str] = None,
        TemperatureUnit: Optional[str] = None,
        WakeWord: Optional[str] = None,
        Locale: Optional[str] = None,
        SetupModeDisabled: Optional[bool] = None,
        MaxVolumeLimit: Optional[int] = None,
        PSTNEnabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_room(
        self,
        RoomArn: Optional[str] = None,
        RoomName: Optional[str] = None,
        Description: Optional[str] = None,
        ProviderCalendarId: Optional[str] = None,
        ProfileArn: Optional[str] = None,
    ) -> Dict:
        pass


    def update_skill_group(
        self,
        SkillGroupArn: Optional[str] = None,
        SkillGroupName: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass

