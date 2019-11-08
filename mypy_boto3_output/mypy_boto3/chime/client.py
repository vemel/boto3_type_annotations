from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_phone_number_with_user(
        self, AccountId: str, UserId: str, E164PhoneNumber: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_phone_numbers_with_voice_connector(
        self,
        VoiceConnectorId: str,
        E164PhoneNumbers: List[Any] = None,
        ForceAssociate: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_phone_numbers_with_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        E164PhoneNumbers: List[Any] = None,
        ForceAssociate: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_delete_phone_number(self, PhoneNumberIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_suspend_user(
        self, AccountId: str, UserIdList: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_unsuspend_user(
        self, AccountId: str, UserIdList: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_update_phone_number(
        self, UpdatePhoneNumberRequestItems: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_update_user(
        self, AccountId: str, UpdateUserRequestItems: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_account(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_bot(
        self, AccountId: str, DisplayName: str, Domain: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_phone_number_order(
        self, ProductType: str, E164PhoneNumbers: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_voice_connector(
        self, Name: str, RequireEncryption: bool, AwsRegion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_voice_connector_group(
        self, Name: str, VoiceConnectorItems: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_account(self, AccountId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_events_configuration(self, AccountId: str, BotId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_phone_number(self, PhoneNumberId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_voice_connector(self, VoiceConnectorId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_voice_connector_group(self, VoiceConnectorGroupId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_voice_connector_origination(self, VoiceConnectorId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_voice_connector_streaming_configuration(
        self, VoiceConnectorId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_voice_connector_termination(self, VoiceConnectorId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_voice_connector_termination_credentials(
        self, VoiceConnectorId: str, Usernames: List[Any] = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def disassociate_phone_number_from_user(
        self, AccountId: str, UserId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_phone_numbers_from_voice_connector(
        self, VoiceConnectorId: str, E164PhoneNumbers: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_phone_numbers_from_voice_connector_group(
        self, VoiceConnectorGroupId: str, E164PhoneNumbers: List[Any] = None
    ) -> Dict[str, Any]:
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
    def get_account(self, AccountId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_account_settings(self, AccountId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_bot(self, AccountId: str, BotId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_events_configuration(self, AccountId: str, BotId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_global_settings(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_phone_number(self, PhoneNumberId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_phone_number_order(self, PhoneNumberOrderId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_phone_number_settings(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_user(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_user_settings(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_voice_connector(self, VoiceConnectorId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_voice_connector_group(self, VoiceConnectorGroupId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_voice_connector_logging_configuration(
        self, VoiceConnectorId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_voice_connector_origination(self, VoiceConnectorId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_voice_connector_streaming_configuration(
        self, VoiceConnectorId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_voice_connector_termination(self, VoiceConnectorId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_voice_connector_termination_health(
        self, VoiceConnectorId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def invite_users(self, AccountId: str, UserEmailList: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_accounts(
        self,
        Name: str = None,
        UserEmail: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_bots(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_phone_number_orders(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_phone_numbers(
        self,
        Status: str = None,
        ProductType: str = None,
        FilterName: str = None,
        FilterValue: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_users(
        self,
        AccountId: str,
        UserEmail: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_voice_connector_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_voice_connector_termination_credentials(
        self, VoiceConnectorId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_voice_connectors(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def logout_user(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_events_configuration(
        self,
        AccountId: str,
        BotId: str,
        OutboundEventsHTTPSEndpoint: str = None,
        LambdaFunctionArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_voice_connector_logging_configuration(
        self, VoiceConnectorId: str, LoggingConfiguration: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_voice_connector_origination(
        self, VoiceConnectorId: str, Origination: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_voice_connector_streaming_configuration(
        self, VoiceConnectorId: str, StreamingConfiguration: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_voice_connector_termination(
        self, VoiceConnectorId: str, Termination: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_voice_connector_termination_credentials(
        self, VoiceConnectorId: str, Credentials: List[Any] = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def regenerate_security_token(self, AccountId: str, BotId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reset_personal_pin(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_phone_number(self, PhoneNumberId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def search_available_phone_numbers(
        self,
        AreaCode: str = None,
        City: str = None,
        Country: str = None,
        State: str = None,
        TollFreePrefix: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_account(self, AccountId: str, Name: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_account_settings(
        self, AccountId: str, AccountSettings: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_bot(
        self, AccountId: str, BotId: str, Disabled: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_global_settings(
        self, BusinessCalling: Dict[str, Any], VoiceConnector: Dict[str, Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_phone_number(
        self, PhoneNumberId: str, ProductType: str = None, CallingName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_phone_number_settings(self, CallingName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_user(
        self, AccountId: str, UserId: str, LicenseType: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_user_settings(
        self, AccountId: str, UserId: str, UserSettings: Dict[str, Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_voice_connector(
        self, VoiceConnectorId: str, Name: str, RequireEncryption: bool
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_voice_connector_group(
        self, VoiceConnectorGroupId: str, Name: str, VoiceConnectorItems: List[Any]
    ) -> Dict[str, Any]:
        pass
