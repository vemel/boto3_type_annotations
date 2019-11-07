from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_phone_number_with_user(
        self,
        AccountId: str,
        UserId: str,
        E164PhoneNumber: str,
    ) -> Dict:
        pass


    def associate_phone_numbers_with_voice_connector(
        self,
        VoiceConnectorId: str,
        E164PhoneNumbers: Optional[List] = None,
        ForceAssociate: Optional[bool] = None,
    ) -> Dict:
        pass


    def associate_phone_numbers_with_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        E164PhoneNumbers: Optional[List] = None,
        ForceAssociate: Optional[bool] = None,
    ) -> Dict:
        pass


    def batch_delete_phone_number(
        self,
        PhoneNumberIds: List,
    ) -> Dict:
        pass


    def batch_suspend_user(
        self,
        AccountId: str,
        UserIdList: List,
    ) -> Dict:
        pass


    def batch_unsuspend_user(
        self,
        AccountId: str,
        UserIdList: List,
    ) -> Dict:
        pass


    def batch_update_phone_number(
        self,
        UpdatePhoneNumberRequestItems: List,
    ) -> Dict:
        pass


    def batch_update_user(
        self,
        AccountId: str,
        UpdateUserRequestItems: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_account(
        self,
        Name: str,
    ) -> Dict:
        pass


    def create_bot(
        self,
        AccountId: str,
        DisplayName: str,
        Domain: Optional[str] = None,
    ) -> Dict:
        pass


    def create_phone_number_order(
        self,
        ProductType: str,
        E164PhoneNumbers: List,
    ) -> Dict:
        pass


    def create_voice_connector(
        self,
        Name: str,
        RequireEncryption: bool,
        AwsRegion: Optional[str] = None,
    ) -> Dict:
        pass


    def create_voice_connector_group(
        self,
        Name: str,
        VoiceConnectorItems: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_account(
        self,
        AccountId: str,
    ) -> Dict:
        pass


    def delete_events_configuration(
        self,
        AccountId: str,
        BotId: str,
    ):
        pass


    def delete_phone_number(
        self,
        PhoneNumberId: str,
    ):
        pass


    def delete_voice_connector(
        self,
        VoiceConnectorId: str,
    ):
        pass


    def delete_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
    ):
        pass


    def delete_voice_connector_origination(
        self,
        VoiceConnectorId: str,
    ):
        pass


    def delete_voice_connector_streaming_configuration(
        self,
        VoiceConnectorId: str,
    ):
        pass


    def delete_voice_connector_termination(
        self,
        VoiceConnectorId: str,
    ):
        pass


    def delete_voice_connector_termination_credentials(
        self,
        VoiceConnectorId: str,
        Usernames: Optional[List] = None,
    ):
        pass


    def disassociate_phone_number_from_user(
        self,
        AccountId: str,
        UserId: str,
    ) -> Dict:
        pass


    def disassociate_phone_numbers_from_voice_connector(
        self,
        VoiceConnectorId: str,
        E164PhoneNumbers: Optional[List] = None,
    ) -> Dict:
        pass


    def disassociate_phone_numbers_from_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        E164PhoneNumbers: Optional[List] = None,
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


    def get_account(
        self,
        AccountId: str,
    ) -> Dict:
        pass


    def get_account_settings(
        self,
        AccountId: str,
    ) -> Dict:
        pass


    def get_bot(
        self,
        AccountId: str,
        BotId: str,
    ) -> Dict:
        pass


    def get_events_configuration(
        self,
        AccountId: str,
        BotId: str,
    ) -> Dict:
        pass


    def get_global_settings(
        self,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_phone_number(
        self,
        PhoneNumberId: str,
    ) -> Dict:
        pass


    def get_phone_number_order(
        self,
        PhoneNumberOrderId: str,
    ) -> Dict:
        pass


    def get_phone_number_settings(
        self,
    ) -> Dict:
        pass


    def get_user(
        self,
        AccountId: str,
        UserId: str,
    ) -> Dict:
        pass


    def get_user_settings(
        self,
        AccountId: str,
        UserId: str,
    ) -> Dict:
        pass


    def get_voice_connector(
        self,
        VoiceConnectorId: str,
    ) -> Dict:
        pass


    def get_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
    ) -> Dict:
        pass


    def get_voice_connector_logging_configuration(
        self,
        VoiceConnectorId: str,
    ) -> Dict:
        pass


    def get_voice_connector_origination(
        self,
        VoiceConnectorId: str,
    ) -> Dict:
        pass


    def get_voice_connector_streaming_configuration(
        self,
        VoiceConnectorId: str,
    ) -> Dict:
        pass


    def get_voice_connector_termination(
        self,
        VoiceConnectorId: str,
    ) -> Dict:
        pass


    def get_voice_connector_termination_health(
        self,
        VoiceConnectorId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def invite_users(
        self,
        AccountId: str,
        UserEmailList: List,
    ) -> Dict:
        pass


    def list_accounts(
        self,
        Name: Optional[str] = None,
        UserEmail: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_bots(
        self,
        AccountId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_phone_number_orders(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_phone_numbers(
        self,
        Status: Optional[str] = None,
        ProductType: Optional[str] = None,
        FilterName: Optional[str] = None,
        FilterValue: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_users(
        self,
        AccountId: str,
        UserEmail: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_voice_connector_groups(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_voice_connector_termination_credentials(
        self,
        VoiceConnectorId: str,
    ) -> Dict:
        pass


    def list_voice_connectors(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def logout_user(
        self,
        AccountId: str,
        UserId: str,
    ) -> Dict:
        pass


    def put_events_configuration(
        self,
        AccountId: str,
        BotId: str,
        OutboundEventsHTTPSEndpoint: Optional[str] = None,
        LambdaFunctionArn: Optional[str] = None,
    ) -> Dict:
        pass


    def put_voice_connector_logging_configuration(
        self,
        VoiceConnectorId: str,
        LoggingConfiguration: Dict,
    ) -> Dict:
        pass


    def put_voice_connector_origination(
        self,
        VoiceConnectorId: str,
        Origination: Dict,
    ) -> Dict:
        pass


    def put_voice_connector_streaming_configuration(
        self,
        VoiceConnectorId: str,
        StreamingConfiguration: Dict,
    ) -> Dict:
        pass


    def put_voice_connector_termination(
        self,
        VoiceConnectorId: str,
        Termination: Dict,
    ) -> Dict:
        pass


    def put_voice_connector_termination_credentials(
        self,
        VoiceConnectorId: str,
        Credentials: Optional[List] = None,
    ):
        pass


    def regenerate_security_token(
        self,
        AccountId: str,
        BotId: str,
    ) -> Dict:
        pass


    def reset_personal_pin(
        self,
        AccountId: str,
        UserId: str,
    ) -> Dict:
        pass


    def restore_phone_number(
        self,
        PhoneNumberId: str,
    ) -> Dict:
        pass


    def search_available_phone_numbers(
        self,
        AreaCode: Optional[str] = None,
        City: Optional[str] = None,
        Country: Optional[str] = None,
        State: Optional[str] = None,
        TollFreePrefix: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def update_account(
        self,
        AccountId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def update_account_settings(
        self,
        AccountId: str,
        AccountSettings: Dict,
    ) -> Dict:
        pass


    def update_bot(
        self,
        AccountId: str,
        BotId: str,
        Disabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_global_settings(
        self,
        BusinessCalling: Dict,
        VoiceConnector: Dict,
    ):
        pass


    def update_phone_number(
        self,
        PhoneNumberId: str,
        ProductType: Optional[str] = None,
        CallingName: Optional[str] = None,
    ) -> Dict:
        pass


    def update_phone_number_settings(
        self,
        CallingName: str,
    ):
        pass


    def update_user(
        self,
        AccountId: str,
        UserId: str,
        LicenseType: Optional[str] = None,
    ) -> Dict:
        pass


    def update_user_settings(
        self,
        AccountId: str,
        UserId: str,
        UserSettings: Dict,
    ):
        pass


    def update_voice_connector(
        self,
        VoiceConnectorId: str,
        Name: str,
        RequireEncryption: bool,
    ) -> Dict:
        pass


    def update_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        Name: str,
        VoiceConnectorItems: List,
    ) -> Dict:
        pass

