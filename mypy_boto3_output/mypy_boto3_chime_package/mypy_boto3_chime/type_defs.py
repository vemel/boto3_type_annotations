"Main interface for chime type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    "ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    "ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "ClientBatchCreateRoomMembershipMembershipItemListTypeDef",
    "ClientBatchCreateRoomMembershipResponseErrorsTypeDef",
    "ClientBatchCreateRoomMembershipResponseTypeDef",
    "ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef",
    "ClientBatchDeletePhoneNumberResponseTypeDef",
    "ClientBatchSuspendUserResponseUserErrorsTypeDef",
    "ClientBatchSuspendUserResponseTypeDef",
    "ClientBatchUnsuspendUserResponseUserErrorsTypeDef",
    "ClientBatchUnsuspendUserResponseTypeDef",
    "ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef",
    "ClientBatchUpdatePhoneNumberResponseTypeDef",
    "ClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef",
    "ClientBatchUpdateUserResponseUserErrorsTypeDef",
    "ClientBatchUpdateUserResponseTypeDef",
    "ClientBatchUpdateUserUpdateUserRequestItemsTypeDef",
    "ClientCreateAccountResponseAccountTypeDef",
    "ClientCreateAccountResponseTypeDef",
    "ClientCreateBotResponseBotTypeDef",
    "ClientCreateBotResponseTypeDef",
    "ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    "ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    "ClientCreatePhoneNumberOrderResponseTypeDef",
    "ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef",
    "ClientCreateRoomMembershipResponseRoomMembershipTypeDef",
    "ClientCreateRoomMembershipResponseTypeDef",
    "ClientCreateRoomResponseRoomTypeDef",
    "ClientCreateRoomResponseTypeDef",
    "ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    "ClientCreateVoiceConnectorGroupResponseTypeDef",
    "ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef",
    "ClientCreateVoiceConnectorResponseTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "ClientGetAccountResponseAccountTypeDef",
    "ClientGetAccountResponseTypeDef",
    "ClientGetAccountSettingsResponseAccountSettingsTypeDef",
    "ClientGetAccountSettingsResponseTypeDef",
    "ClientGetBotResponseBotTypeDef",
    "ClientGetBotResponseTypeDef",
    "ClientGetEventsConfigurationResponseEventsConfigurationTypeDef",
    "ClientGetEventsConfigurationResponseTypeDef",
    "ClientGetGlobalSettingsResponseBusinessCallingTypeDef",
    "ClientGetGlobalSettingsResponseVoiceConnectorTypeDef",
    "ClientGetGlobalSettingsResponseTypeDef",
    "ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    "ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    "ClientGetPhoneNumberOrderResponseTypeDef",
    "ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef",
    "ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    "ClientGetPhoneNumberResponsePhoneNumberTypeDef",
    "ClientGetPhoneNumberResponseTypeDef",
    "ClientGetPhoneNumberSettingsResponseTypeDef",
    "ClientGetRoomResponseRoomTypeDef",
    "ClientGetRoomResponseTypeDef",
    "ClientGetUserResponseUserTypeDef",
    "ClientGetUserResponseTypeDef",
    "ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef",
    "ClientGetUserSettingsResponseUserSettingsTypeDef",
    "ClientGetUserSettingsResponseTypeDef",
    "ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    "ClientGetVoiceConnectorGroupResponseTypeDef",
    "ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    "ClientGetVoiceConnectorOriginationResponseOriginationTypeDef",
    "ClientGetVoiceConnectorOriginationResponseTypeDef",
    "ClientGetVoiceConnectorResponseVoiceConnectorTypeDef",
    "ClientGetVoiceConnectorResponseTypeDef",
    "ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    "ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef",
    "ClientGetVoiceConnectorTerminationHealthResponseTypeDef",
    "ClientGetVoiceConnectorTerminationResponseTerminationTypeDef",
    "ClientGetVoiceConnectorTerminationResponseTypeDef",
    "ClientInviteUsersResponseInvitesTypeDef",
    "ClientInviteUsersResponseTypeDef",
    "ClientListAccountsResponseAccountsTypeDef",
    "ClientListAccountsResponseTypeDef",
    "ClientListBotsResponseBotsTypeDef",
    "ClientListBotsResponseTypeDef",
    "ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef",
    "ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef",
    "ClientListPhoneNumberOrdersResponseTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumbersTypeDef",
    "ClientListPhoneNumbersResponseTypeDef",
    "ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef",
    "ClientListRoomMembershipsResponseRoomMembershipsTypeDef",
    "ClientListRoomMembershipsResponseTypeDef",
    "ClientListRoomsResponseRoomsTypeDef",
    "ClientListRoomsResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef",
    "ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef",
    "ClientListVoiceConnectorGroupsResponseTypeDef",
    "ClientListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef",
    "ClientListVoiceConnectorsResponseTypeDef",
    "ClientPutEventsConfigurationResponseEventsConfigurationTypeDef",
    "ClientPutEventsConfigurationResponseTypeDef",
    "ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef",
    "ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef",
    "ClientPutVoiceConnectorOriginationOriginationTypeDef",
    "ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    "ClientPutVoiceConnectorOriginationResponseOriginationTypeDef",
    "ClientPutVoiceConnectorOriginationResponseTypeDef",
    "ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    "ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "ClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef",
    "ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef",
    "ClientPutVoiceConnectorTerminationResponseTerminationTypeDef",
    "ClientPutVoiceConnectorTerminationResponseTypeDef",
    "ClientPutVoiceConnectorTerminationTerminationTypeDef",
    "ClientRegenerateSecurityTokenResponseBotTypeDef",
    "ClientRegenerateSecurityTokenResponseTypeDef",
    "ClientResetPersonalPinResponseUserTypeDef",
    "ClientResetPersonalPinResponseTypeDef",
    "ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    "ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    "ClientRestorePhoneNumberResponsePhoneNumberTypeDef",
    "ClientRestorePhoneNumberResponseTypeDef",
    "ClientSearchAvailablePhoneNumbersResponseTypeDef",
    "ClientUpdateAccountResponseAccountTypeDef",
    "ClientUpdateAccountResponseTypeDef",
    "ClientUpdateAccountSettingsAccountSettingsTypeDef",
    "ClientUpdateBotResponseBotTypeDef",
    "ClientUpdateBotResponseTypeDef",
    "ClientUpdateGlobalSettingsBusinessCallingTypeDef",
    "ClientUpdateGlobalSettingsVoiceConnectorTypeDef",
    "ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    "ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    "ClientUpdatePhoneNumberResponsePhoneNumberTypeDef",
    "ClientUpdatePhoneNumberResponseTypeDef",
    "ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef",
    "ClientUpdateRoomMembershipResponseRoomMembershipTypeDef",
    "ClientUpdateRoomMembershipResponseTypeDef",
    "ClientUpdateRoomResponseRoomTypeDef",
    "ClientUpdateRoomResponseTypeDef",
    "ClientUpdateUserResponseUserTypeDef",
    "ClientUpdateUserResponseTypeDef",
    "ClientUpdateUserSettingsUserSettingsTelephonyTypeDef",
    "ClientUpdateUserSettingsUserSettingsTypeDef",
    "ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    "ClientUpdateVoiceConnectorGroupResponseTypeDef",
    "ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef",
    "ClientUpdateVoiceConnectorResponseTypeDef",
    "ListAccountsPaginatePaginationConfigTypeDef",
    "ListAccountsPaginateResponseAccountsTypeDef",
    "ListAccountsPaginateResponseTypeDef",
    "ListUsersPaginatePaginationConfigTypeDef",
    "ListUsersPaginateResponseUsersTypeDef",
    "ListUsersPaginateResponseTypeDef",
)


_ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    {"PhoneNumberId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef(
    _ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef
):
    """
    Type definition for `ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponse` `PhoneNumberErrors`

    If the phone number action fails for one or more of the phone numbers in the request, a
    list of the phone numbers is returned, along with error codes and error messages.

    - **PhoneNumberId** *(string) --*

      The phone number ID for which the action failed.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef = TypedDict(
    "_ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)


class ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef(
    _ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef
):
    """
    Type definition for `ClientAssociatePhoneNumbersWithVoiceConnectorGroup` `Response`

    - **PhoneNumberErrors** *(list) --*

      If the action fails for one or more of the phone numbers in the request, a list of the phone
      numbers is returned, along with error codes and error messages.

      - *(dict) --*

        If the phone number action fails for one or more of the phone numbers in the request, a
        list of the phone numbers is returned, along with error codes and error messages.

        - **PhoneNumberId** *(string) --*

          The phone number ID for which the action failed.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.
    """


_ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    {"PhoneNumberId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef(
    _ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef
):
    """
    Type definition for `ClientAssociatePhoneNumbersWithVoiceConnectorResponse` `PhoneNumberErrors`

    If the phone number action fails for one or more of the phone numbers in the request, a
    list of the phone numbers is returned, along with error codes and error messages.

    - **PhoneNumberId** *(string) --*

      The phone number ID for which the action failed.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef = TypedDict(
    "_ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)


class ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef(
    _ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef
):
    """
    Type definition for `ClientAssociatePhoneNumbersWithVoiceConnector` `Response`

    - **PhoneNumberErrors** *(list) --*

      If the action fails for one or more of the phone numbers in the request, a list of the phone
      numbers is returned, along with error codes and error messages.

      - *(dict) --*

        If the phone number action fails for one or more of the phone numbers in the request, a
        list of the phone numbers is returned, along with error codes and error messages.

        - **PhoneNumberId** *(string) --*

          The phone number ID for which the action failed.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.
    """


_ClientBatchCreateRoomMembershipMembershipItemListTypeDef = TypedDict(
    "_ClientBatchCreateRoomMembershipMembershipItemListTypeDef",
    {"MemberId": str, "Role": str},
    total=False,
)


class ClientBatchCreateRoomMembershipMembershipItemListTypeDef(
    _ClientBatchCreateRoomMembershipMembershipItemListTypeDef
):
    """
    Type definition for `ClientBatchCreateRoomMembership` `MembershipItemList`

    Membership details, such as member ID and member role.

    - **MemberId** *(string) --*

      The member ID.

    - **Role** *(string) --*

      The member role.
    """


_ClientBatchCreateRoomMembershipResponseErrorsTypeDef = TypedDict(
    "_ClientBatchCreateRoomMembershipResponseErrorsTypeDef",
    {"MemberId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchCreateRoomMembershipResponseErrorsTypeDef(
    _ClientBatchCreateRoomMembershipResponseErrorsTypeDef
):
    """
    Type definition for `ClientBatchCreateRoomMembershipResponse` `Errors`

    The list of errors returned when a member action results in an error.

    - **MemberId** *(string) --*

      The member ID.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientBatchCreateRoomMembershipResponseTypeDef = TypedDict(
    "_ClientBatchCreateRoomMembershipResponseTypeDef",
    {"Errors": List[ClientBatchCreateRoomMembershipResponseErrorsTypeDef]},
    total=False,
)


class ClientBatchCreateRoomMembershipResponseTypeDef(
    _ClientBatchCreateRoomMembershipResponseTypeDef
):
    """
    Type definition for `ClientBatchCreateRoomMembership` `Response`

    - **Errors** *(list) --*

      If the action fails for one or more of the member IDs in the request, a list of the member
      IDs is returned, along with error codes and error messages.

      - *(dict) --*

        The list of errors returned when a member action results in an error.

        - **MemberId** *(string) --*

          The member ID.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.
    """


_ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef",
    {"PhoneNumberId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef(
    _ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef
):
    """
    Type definition for `ClientBatchDeletePhoneNumberResponse` `PhoneNumberErrors`

    If the phone number action fails for one or more of the phone numbers in the request, a
    list of the phone numbers is returned, along with error codes and error messages.

    - **PhoneNumberId** *(string) --*

      The phone number ID for which the action failed.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientBatchDeletePhoneNumberResponseTypeDef = TypedDict(
    "_ClientBatchDeletePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)


class ClientBatchDeletePhoneNumberResponseTypeDef(
    _ClientBatchDeletePhoneNumberResponseTypeDef
):
    """
    Type definition for `ClientBatchDeletePhoneNumber` `Response`

    - **PhoneNumberErrors** *(list) --*

      If the action fails for one or more of the phone numbers in the request, a list of the phone
      numbers is returned, along with error codes and error messages.

      - *(dict) --*

        If the phone number action fails for one or more of the phone numbers in the request, a
        list of the phone numbers is returned, along with error codes and error messages.

        - **PhoneNumberId** *(string) --*

          The phone number ID for which the action failed.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.
    """


_ClientBatchSuspendUserResponseUserErrorsTypeDef = TypedDict(
    "_ClientBatchSuspendUserResponseUserErrorsTypeDef",
    {"UserId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchSuspendUserResponseUserErrorsTypeDef(
    _ClientBatchSuspendUserResponseUserErrorsTypeDef
):
    """
    Type definition for `ClientBatchSuspendUserResponse` `UserErrors`

    The list of errors returned when errors are encountered during the  BatchSuspendUser ,
    BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
    error messages.

    - **UserId** *(string) --*

      The user ID for which the action failed.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientBatchSuspendUserResponseTypeDef = TypedDict(
    "_ClientBatchSuspendUserResponseTypeDef",
    {"UserErrors": List[ClientBatchSuspendUserResponseUserErrorsTypeDef]},
    total=False,
)


class ClientBatchSuspendUserResponseTypeDef(_ClientBatchSuspendUserResponseTypeDef):
    """
    Type definition for `ClientBatchSuspendUser` `Response`

    - **UserErrors** *(list) --*

      If the  BatchSuspendUser action fails for one or more of the user IDs in the request, a list
      of the user IDs is returned, along with error codes and error messages.

      - *(dict) --*

        The list of errors returned when errors are encountered during the  BatchSuspendUser ,
        BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
        error messages.

        - **UserId** *(string) --*

          The user ID for which the action failed.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.
    """


_ClientBatchUnsuspendUserResponseUserErrorsTypeDef = TypedDict(
    "_ClientBatchUnsuspendUserResponseUserErrorsTypeDef",
    {"UserId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchUnsuspendUserResponseUserErrorsTypeDef(
    _ClientBatchUnsuspendUserResponseUserErrorsTypeDef
):
    """
    Type definition for `ClientBatchUnsuspendUserResponse` `UserErrors`

    The list of errors returned when errors are encountered during the  BatchSuspendUser ,
    BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
    error messages.

    - **UserId** *(string) --*

      The user ID for which the action failed.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientBatchUnsuspendUserResponseTypeDef = TypedDict(
    "_ClientBatchUnsuspendUserResponseTypeDef",
    {"UserErrors": List[ClientBatchUnsuspendUserResponseUserErrorsTypeDef]},
    total=False,
)


class ClientBatchUnsuspendUserResponseTypeDef(_ClientBatchUnsuspendUserResponseTypeDef):
    """
    Type definition for `ClientBatchUnsuspendUser` `Response`

    - **UserErrors** *(list) --*

      If the  BatchUnsuspendUser action fails for one or more of the user IDs in the request, a
      list of the user IDs is returned, along with error codes and error messages.

      - *(dict) --*

        The list of errors returned when errors are encountered during the  BatchSuspendUser ,
        BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
        error messages.

        - **UserId** *(string) --*

          The user ID for which the action failed.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.
    """


_ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef",
    {"PhoneNumberId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef(
    _ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef
):
    """
    Type definition for `ClientBatchUpdatePhoneNumberResponse` `PhoneNumberErrors`

    If the phone number action fails for one or more of the phone numbers in the request, a
    list of the phone numbers is returned, along with error codes and error messages.

    - **PhoneNumberId** *(string) --*

      The phone number ID for which the action failed.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientBatchUpdatePhoneNumberResponseTypeDef = TypedDict(
    "_ClientBatchUpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)


class ClientBatchUpdatePhoneNumberResponseTypeDef(
    _ClientBatchUpdatePhoneNumberResponseTypeDef
):
    """
    Type definition for `ClientBatchUpdatePhoneNumber` `Response`

    - **PhoneNumberErrors** *(list) --*

      If the action fails for one or more of the phone numbers in the request, a list of the phone
      numbers is returned, along with error codes and error messages.

      - *(dict) --*

        If the phone number action fails for one or more of the phone numbers in the request, a
        list of the phone numbers is returned, along with error codes and error messages.

        - **PhoneNumberId** *(string) --*

          The phone number ID for which the action failed.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.
    """


_RequiredClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef = TypedDict(
    "_RequiredClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef",
    {"PhoneNumberId": str},
)
_OptionalClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef = TypedDict(
    "_OptionalClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef",
    {"ProductType": str, "CallingName": str},
    total=False,
)


class ClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef(
    _RequiredClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef,
    _OptionalClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef,
):
    """
    Type definition for `ClientBatchUpdatePhoneNumber` `UpdatePhoneNumberRequestItems`

    The phone number ID, product type, or calling name fields to update, used with the
    BatchUpdatePhoneNumber and  UpdatePhoneNumber actions.

    - **PhoneNumberId** *(string) --* **[REQUIRED]**

      The phone number ID to update.

    - **ProductType** *(string) --*

      The product type to update.

    - **CallingName** *(string) --*

      The outbound calling name to update.
    """


_ClientBatchUpdateUserResponseUserErrorsTypeDef = TypedDict(
    "_ClientBatchUpdateUserResponseUserErrorsTypeDef",
    {"UserId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchUpdateUserResponseUserErrorsTypeDef(
    _ClientBatchUpdateUserResponseUserErrorsTypeDef
):
    """
    Type definition for `ClientBatchUpdateUserResponse` `UserErrors`

    The list of errors returned when errors are encountered during the  BatchSuspendUser ,
    BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
    error messages.

    - **UserId** *(string) --*

      The user ID for which the action failed.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientBatchUpdateUserResponseTypeDef = TypedDict(
    "_ClientBatchUpdateUserResponseTypeDef",
    {"UserErrors": List[ClientBatchUpdateUserResponseUserErrorsTypeDef]},
    total=False,
)


class ClientBatchUpdateUserResponseTypeDef(_ClientBatchUpdateUserResponseTypeDef):
    """
    Type definition for `ClientBatchUpdateUser` `Response`

    - **UserErrors** *(list) --*

      If the  BatchUpdateUser action fails for one or more of the user IDs in the request, a list
      of the user IDs is returned, along with error codes and error messages.

      - *(dict) --*

        The list of errors returned when errors are encountered during the  BatchSuspendUser ,
        BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
        error messages.

        - **UserId** *(string) --*

          The user ID for which the action failed.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.
    """


_RequiredClientBatchUpdateUserUpdateUserRequestItemsTypeDef = TypedDict(
    "_RequiredClientBatchUpdateUserUpdateUserRequestItemsTypeDef", {"UserId": str}
)
_OptionalClientBatchUpdateUserUpdateUserRequestItemsTypeDef = TypedDict(
    "_OptionalClientBatchUpdateUserUpdateUserRequestItemsTypeDef",
    {"LicenseType": str},
    total=False,
)


class ClientBatchUpdateUserUpdateUserRequestItemsTypeDef(
    _RequiredClientBatchUpdateUserUpdateUserRequestItemsTypeDef,
    _OptionalClientBatchUpdateUserUpdateUserRequestItemsTypeDef,
):
    """
    Type definition for `ClientBatchUpdateUser` `UpdateUserRequestItems`

    The user ID and user fields to update, used with the  BatchUpdateUser action.

    - **UserId** *(string) --* **[REQUIRED]**

      The user ID.

    - **LicenseType** *(string) --*

      The user license type.
    """


_ClientCreateAccountResponseAccountTypeDef = TypedDict(
    "_ClientCreateAccountResponseAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": str,
        "CreatedTimestamp": datetime,
        "DefaultLicense": str,
        "SupportedLicenses": List[str],
    },
    total=False,
)


class ClientCreateAccountResponseAccountTypeDef(
    _ClientCreateAccountResponseAccountTypeDef
):
    """
    Type definition for `ClientCreateAccountResponse` `Account`

    The Amazon Chime account details.

    - **AwsAccountId** *(string) --*

      The AWS account ID.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **Name** *(string) --*

      The Amazon Chime account name.

    - **AccountType** *(string) --*

      The Amazon Chime account type. For more information about different account types, see
      `Managing Your Amazon Chime Accounts
      <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
      Chime Administration Guide* .

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime account creation timestamp, in ISO 8601 format.

    - **DefaultLicense** *(string) --*

      The default license for the Amazon Chime account.

    - **SupportedLicenses** *(list) --*

      Supported licenses for the Amazon Chime account.

      - *(string) --*
    """


_ClientCreateAccountResponseTypeDef = TypedDict(
    "_ClientCreateAccountResponseTypeDef",
    {"Account": ClientCreateAccountResponseAccountTypeDef},
    total=False,
)


class ClientCreateAccountResponseTypeDef(_ClientCreateAccountResponseTypeDef):
    """
    Type definition for `ClientCreateAccount` `Response`

    - **Account** *(dict) --*

      The Amazon Chime account details.

      - **AwsAccountId** *(string) --*

        The AWS account ID.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

      - **Name** *(string) --*

        The Amazon Chime account name.

      - **AccountType** *(string) --*

        The Amazon Chime account type. For more information about different account types, see
        `Managing Your Amazon Chime Accounts
        <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
        Chime Administration Guide* .

      - **CreatedTimestamp** *(datetime) --*

        The Amazon Chime account creation timestamp, in ISO 8601 format.

      - **DefaultLicense** *(string) --*

        The default license for the Amazon Chime account.

      - **SupportedLicenses** *(list) --*

        Supported licenses for the Amazon Chime account.

        - *(string) --*
    """


_ClientCreateBotResponseBotTypeDef = TypedDict(
    "_ClientCreateBotResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)


class ClientCreateBotResponseBotTypeDef(_ClientCreateBotResponseBotTypeDef):
    """
    Type definition for `ClientCreateBotResponse` `Bot`

    The bot details.

    - **BotId** *(string) --*

      The bot ID.

    - **UserId** *(string) --*

      The unique ID for the bot user.

    - **DisplayName** *(string) --*

      The bot display name.

    - **BotType** *(string) --*

      The bot type.

    - **Disabled** *(boolean) --*

      When true, the bot is stopped from running in your account.

    - **CreatedTimestamp** *(datetime) --*

      The bot creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated bot timestamp, in ISO 8601 format.

    - **BotEmail** *(string) --*

      The bot email address.

    - **SecurityToken** *(string) --*

      The security token used to authenticate Amazon Chime with the outgoing event endpoint.
    """


_ClientCreateBotResponseTypeDef = TypedDict(
    "_ClientCreateBotResponseTypeDef",
    {"Bot": ClientCreateBotResponseBotTypeDef},
    total=False,
)


class ClientCreateBotResponseTypeDef(_ClientCreateBotResponseTypeDef):
    """
    Type definition for `ClientCreateBot` `Response`

    - **Bot** *(dict) --*

      The bot details.

      - **BotId** *(string) --*

        The bot ID.

      - **UserId** *(string) --*

        The unique ID for the bot user.

      - **DisplayName** *(string) --*

        The bot display name.

      - **BotType** *(string) --*

        The bot type.

      - **Disabled** *(boolean) --*

        When true, the bot is stopped from running in your account.

      - **CreatedTimestamp** *(datetime) --*

        The bot creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated bot timestamp, in ISO 8601 format.

      - **BotEmail** *(string) --*

        The bot email address.

      - **SecurityToken** *(string) --*

        The security token used to authenticate Amazon Chime with the outgoing event endpoint.
    """


_ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef = TypedDict(
    "_ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    {"E164PhoneNumber": str, "Status": str},
    total=False,
)


class ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef(
    _ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef
):
    """
    Type definition for `ClientCreatePhoneNumberOrderResponsePhoneNumberOrder` `OrderedPhoneNumbers`

    A phone number for which an order has been placed.

    - **E164PhoneNumber** *(string) --*

      The phone number, in E.164 format.

    - **Status** *(string) --*

      The phone number status.
    """


_ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef = TypedDict(
    "_ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": str,
        "Status": str,
        "OrderedPhoneNumbers": List[
            ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef(
    _ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef
):
    """
    Type definition for `ClientCreatePhoneNumberOrderResponse` `PhoneNumberOrder`

    The phone number order details.

    - **PhoneNumberOrderId** *(string) --*

      The phone number order ID.

    - **ProductType** *(string) --*

      The phone number order product type.

    - **Status** *(string) --*

      The status of the phone number order.

    - **OrderedPhoneNumbers** *(list) --*

      The ordered phone number details, such as the phone number in E.164 format and the phone
      number status.

      - *(dict) --*

        A phone number for which an order has been placed.

        - **E164PhoneNumber** *(string) --*

          The phone number, in E.164 format.

        - **Status** *(string) --*

          The phone number status.

    - **CreatedTimestamp** *(datetime) --*

      The phone number order creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated phone number order timestamp, in ISO 8601 format.
    """


_ClientCreatePhoneNumberOrderResponseTypeDef = TypedDict(
    "_ClientCreatePhoneNumberOrderResponseTypeDef",
    {"PhoneNumberOrder": ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef},
    total=False,
)


class ClientCreatePhoneNumberOrderResponseTypeDef(
    _ClientCreatePhoneNumberOrderResponseTypeDef
):
    """
    Type definition for `ClientCreatePhoneNumberOrder` `Response`

    - **PhoneNumberOrder** *(dict) --*

      The phone number order details.

      - **PhoneNumberOrderId** *(string) --*

        The phone number order ID.

      - **ProductType** *(string) --*

        The phone number order product type.

      - **Status** *(string) --*

        The status of the phone number order.

      - **OrderedPhoneNumbers** *(list) --*

        The ordered phone number details, such as the phone number in E.164 format and the phone
        number status.

        - *(dict) --*

          A phone number for which an order has been placed.

          - **E164PhoneNumber** *(string) --*

            The phone number, in E.164 format.

          - **Status** *(string) --*

            The phone number status.

      - **CreatedTimestamp** *(datetime) --*

        The phone number order creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated phone number order timestamp, in ISO 8601 format.
    """


_ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef = TypedDict(
    "_ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": str,
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)


class ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef(
    _ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef
):
    """
    Type definition for `ClientCreateRoomMembershipResponseRoomMembership` `Member`

    The member details, such as email address, name, member ID, and member type.

    - **MemberId** *(string) --*

      The member ID (user ID or bot ID).

    - **MemberType** *(string) --*

      The member type.

    - **Email** *(string) --*

      The member email address.

    - **FullName** *(string) --*

      The member name.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.
    """


_ClientCreateRoomMembershipResponseRoomMembershipTypeDef = TypedDict(
    "_ClientCreateRoomMembershipResponseRoomMembershipTypeDef",
    {
        "RoomId": str,
        "Member": ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef,
        "Role": str,
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientCreateRoomMembershipResponseRoomMembershipTypeDef(
    _ClientCreateRoomMembershipResponseRoomMembershipTypeDef
):
    """
    Type definition for `ClientCreateRoomMembershipResponse` `RoomMembership`

    The room membership details.

    - **RoomId** *(string) --*

      The room ID.

    - **Member** *(dict) --*

      The member details, such as email address, name, member ID, and member type.

      - **MemberId** *(string) --*

        The member ID (user ID or bot ID).

      - **MemberType** *(string) --*

        The member type.

      - **Email** *(string) --*

        The member email address.

      - **FullName** *(string) --*

        The member name.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

    - **Role** *(string) --*

      The membership role.

    - **InvitedBy** *(string) --*

      The identifier of the user that invited the room member.

    - **UpdatedTimestamp** *(datetime) --*

      The room membership update timestamp, in ISO 8601 format.
    """


_ClientCreateRoomMembershipResponseTypeDef = TypedDict(
    "_ClientCreateRoomMembershipResponseTypeDef",
    {"RoomMembership": ClientCreateRoomMembershipResponseRoomMembershipTypeDef},
    total=False,
)


class ClientCreateRoomMembershipResponseTypeDef(
    _ClientCreateRoomMembershipResponseTypeDef
):
    """
    Type definition for `ClientCreateRoomMembership` `Response`

    - **RoomMembership** *(dict) --*

      The room membership details.

      - **RoomId** *(string) --*

        The room ID.

      - **Member** *(dict) --*

        The member details, such as email address, name, member ID, and member type.

        - **MemberId** *(string) --*

          The member ID (user ID or bot ID).

        - **MemberType** *(string) --*

          The member type.

        - **Email** *(string) --*

          The member email address.

        - **FullName** *(string) --*

          The member name.

        - **AccountId** *(string) --*

          The Amazon Chime account ID.

      - **Role** *(string) --*

        The membership role.

      - **InvitedBy** *(string) --*

        The identifier of the user that invited the room member.

      - **UpdatedTimestamp** *(datetime) --*

        The room membership update timestamp, in ISO 8601 format.
    """


_ClientCreateRoomResponseRoomTypeDef = TypedDict(
    "_ClientCreateRoomResponseRoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientCreateRoomResponseRoomTypeDef(_ClientCreateRoomResponseRoomTypeDef):
    """
    Type definition for `ClientCreateRoomResponse` `Room`

    The room details.

    - **RoomId** *(string) --*

      The room ID.

    - **Name** *(string) --*

      The room name.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **CreatedBy** *(string) --*

      The identifier of the room creator.

    - **CreatedTimestamp** *(datetime) --*

      The room creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The room update timestamp, in ISO 8601 format.
    """


_ClientCreateRoomResponseTypeDef = TypedDict(
    "_ClientCreateRoomResponseTypeDef",
    {"Room": ClientCreateRoomResponseRoomTypeDef},
    total=False,
)


class ClientCreateRoomResponseTypeDef(_ClientCreateRoomResponseTypeDef):
    """
    Type definition for `ClientCreateRoom` `Response`

    - **Room** *(dict) --*

      The room details.

      - **RoomId** *(string) --*

        The room ID.

      - **Name** *(string) --*

        The room name.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

      - **CreatedBy** *(string) --*

        The identifier of the room creator.

      - **CreatedTimestamp** *(datetime) --*

        The room creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The room update timestamp, in ISO 8601 format.
    """


_ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)


class ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
):
    """
    Type definition for `ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroup` `VoiceConnectorItems`

    For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
    route inbound calls. Includes priority configuration settings. Limit: 3
    ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

    - **VoiceConnectorId** *(string) --*

      The Amazon Chime Voice Connector ID.

    - **Priority** *(integer) --*

      The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
      priority. Higher priority Amazon Chime Voice Connectors are attempted first.
    """


_ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef(
    _ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef
):
    """
    Type definition for `ClientCreateVoiceConnectorGroupResponse` `VoiceConnectorGroup`

    The Amazon Chime Voice Connector group details.

    - **VoiceConnectorGroupId** *(string) --*

      The Amazon Chime Voice Connector group ID.

    - **Name** *(string) --*

      The name of the Amazon Chime Voice Connector group.

    - **VoiceConnectorItems** *(list) --*

      The Amazon Chime Voice Connectors to which to route inbound calls.

      - *(dict) --*

        For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
        route inbound calls. Includes priority configuration settings. Limit: 3
        ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

        - **VoiceConnectorId** *(string) --*

          The Amazon Chime Voice Connector ID.

        - **Priority** *(integer) --*

          The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
          priority. Higher priority Amazon Chime Voice Connectors are attempted first.

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.
    """


_ClientCreateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef
    },
    total=False,
)


class ClientCreateVoiceConnectorGroupResponseTypeDef(
    _ClientCreateVoiceConnectorGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateVoiceConnectorGroup` `Response`

    - **VoiceConnectorGroup** *(dict) --*

      The Amazon Chime Voice Connector group details.

      - **VoiceConnectorGroupId** *(string) --*

        The Amazon Chime Voice Connector group ID.

      - **Name** *(string) --*

        The name of the Amazon Chime Voice Connector group.

      - **VoiceConnectorItems** *(list) --*

        The Amazon Chime Voice Connectors to which to route inbound calls.

        - *(dict) --*

          For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
          route inbound calls. Includes priority configuration settings. Limit: 3
          ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

          - **VoiceConnectorId** *(string) --*

            The Amazon Chime Voice Connector ID.

          - **Priority** *(integer) --*

            The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
            priority. Higher priority Amazon Chime Voice Connectors are attempted first.

      - **CreatedTimestamp** *(datetime) --*

        The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.
    """


_ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
)


class ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef
):
    """
    Type definition for `ClientCreateVoiceConnectorGroup` `VoiceConnectorItems`

    For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route
    inbound calls. Includes priority configuration settings. Limit: 3 ``VoiceConnectorItems`` per
    Amazon Chime Voice Connector group.

    - **VoiceConnectorId** *(string) --* **[REQUIRED]**

      The Amazon Chime Voice Connector ID.

    - **Priority** *(integer) --* **[REQUIRED]**

      The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
      priority. Higher priority Amazon Chime Voice Connectors are attempted first.
    """


_ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": str,
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef(
    _ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef
):
    """
    Type definition for `ClientCreateVoiceConnectorResponse` `VoiceConnector`

    The Amazon Chime Voice Connector details.

    - **VoiceConnectorId** *(string) --*

      The Amazon Chime Voice Connector ID.

    - **AwsRegion** *(string) --*

      The AWS Region in which the Amazon Chime Voice Connector is created. Default: ``us-east-1``
      .

    - **Name** *(string) --*

      The name of the Amazon Chime Voice Connector.

    - **OutboundHostName** *(string) --*

      The outbound host name for the Amazon Chime Voice Connector.

    - **RequireEncryption** *(boolean) --*

      Designates whether encryption is required for the Amazon Chime Voice Connector.

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
    """


_ClientCreateVoiceConnectorResponseTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorResponseTypeDef",
    {"VoiceConnector": ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef},
    total=False,
)


class ClientCreateVoiceConnectorResponseTypeDef(
    _ClientCreateVoiceConnectorResponseTypeDef
):
    """
    Type definition for `ClientCreateVoiceConnector` `Response`

    - **VoiceConnector** *(dict) --*

      The Amazon Chime Voice Connector details.

      - **VoiceConnectorId** *(string) --*

        The Amazon Chime Voice Connector ID.

      - **AwsRegion** *(string) --*

        The AWS Region in which the Amazon Chime Voice Connector is created. Default: ``us-east-1``
        .

      - **Name** *(string) --*

        The name of the Amazon Chime Voice Connector.

      - **OutboundHostName** *(string) --*

        The outbound host name for the Amazon Chime Voice Connector.

      - **RequireEncryption** *(boolean) --*

        Designates whether encryption is required for the Amazon Chime Voice Connector.

      - **CreatedTimestamp** *(datetime) --*

        The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
    """


_ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    {"PhoneNumberId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef(
    _ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef
):
    """
    Type definition for `ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponse` `PhoneNumberErrors`

    If the phone number action fails for one or more of the phone numbers in the request, a
    list of the phone numbers is returned, along with error codes and error messages.

    - **PhoneNumberId** *(string) --*

      The phone number ID for which the action failed.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef = TypedDict(
    "_ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)


class ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef(
    _ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef
):
    """
    Type definition for `ClientDisassociatePhoneNumbersFromVoiceConnectorGroup` `Response`

    - **PhoneNumberErrors** *(list) --*

      If the action fails for one or more of the phone numbers in the request, a list of the phone
      numbers is returned, along with error codes and error messages.

      - *(dict) --*

        If the phone number action fails for one or more of the phone numbers in the request, a
        list of the phone numbers is returned, along with error codes and error messages.

        - **PhoneNumberId** *(string) --*

          The phone number ID for which the action failed.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.
    """


_ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    {"PhoneNumberId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef(
    _ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef
):
    """
    Type definition for `ClientDisassociatePhoneNumbersFromVoiceConnectorResponse` `PhoneNumberErrors`

    If the phone number action fails for one or more of the phone numbers in the request, a
    list of the phone numbers is returned, along with error codes and error messages.

    - **PhoneNumberId** *(string) --*

      The phone number ID for which the action failed.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message.
    """


_ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef = TypedDict(
    "_ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)


class ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef(
    _ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef
):
    """
    Type definition for `ClientDisassociatePhoneNumbersFromVoiceConnector` `Response`

    - **PhoneNumberErrors** *(list) --*

      If the action fails for one or more of the phone numbers in the request, a list of the phone
      numbers is returned, along with error codes and error messages.

      - *(dict) --*

        If the phone number action fails for one or more of the phone numbers in the request, a
        list of the phone numbers is returned, along with error codes and error messages.

        - **PhoneNumberId** *(string) --*

          The phone number ID for which the action failed.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message.
    """


_ClientGetAccountResponseAccountTypeDef = TypedDict(
    "_ClientGetAccountResponseAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": str,
        "CreatedTimestamp": datetime,
        "DefaultLicense": str,
        "SupportedLicenses": List[str],
    },
    total=False,
)


class ClientGetAccountResponseAccountTypeDef(_ClientGetAccountResponseAccountTypeDef):
    """
    Type definition for `ClientGetAccountResponse` `Account`

    The Amazon Chime account details.

    - **AwsAccountId** *(string) --*

      The AWS account ID.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **Name** *(string) --*

      The Amazon Chime account name.

    - **AccountType** *(string) --*

      The Amazon Chime account type. For more information about different account types, see
      `Managing Your Amazon Chime Accounts
      <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
      Chime Administration Guide* .

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime account creation timestamp, in ISO 8601 format.

    - **DefaultLicense** *(string) --*

      The default license for the Amazon Chime account.

    - **SupportedLicenses** *(list) --*

      Supported licenses for the Amazon Chime account.

      - *(string) --*
    """


_ClientGetAccountResponseTypeDef = TypedDict(
    "_ClientGetAccountResponseTypeDef",
    {"Account": ClientGetAccountResponseAccountTypeDef},
    total=False,
)


class ClientGetAccountResponseTypeDef(_ClientGetAccountResponseTypeDef):
    """
    Type definition for `ClientGetAccount` `Response`

    - **Account** *(dict) --*

      The Amazon Chime account details.

      - **AwsAccountId** *(string) --*

        The AWS account ID.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

      - **Name** *(string) --*

        The Amazon Chime account name.

      - **AccountType** *(string) --*

        The Amazon Chime account type. For more information about different account types, see
        `Managing Your Amazon Chime Accounts
        <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
        Chime Administration Guide* .

      - **CreatedTimestamp** *(datetime) --*

        The Amazon Chime account creation timestamp, in ISO 8601 format.

      - **DefaultLicense** *(string) --*

        The default license for the Amazon Chime account.

      - **SupportedLicenses** *(list) --*

        Supported licenses for the Amazon Chime account.

        - *(string) --*
    """


_ClientGetAccountSettingsResponseAccountSettingsTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseAccountSettingsTypeDef",
    {"DisableRemoteControl": bool, "EnableDialOut": bool},
    total=False,
)


class ClientGetAccountSettingsResponseAccountSettingsTypeDef(
    _ClientGetAccountSettingsResponseAccountSettingsTypeDef
):
    """
    Type definition for `ClientGetAccountSettingsResponse` `AccountSettings`

    The Amazon Chime account settings.

    - **DisableRemoteControl** *(boolean) --*

      Setting that stops or starts remote control of shared screens during meetings.

    - **EnableDialOut** *(boolean) --*

      Setting that allows meeting participants to choose the **Call me at a phone number**
      option. For more information, see `Join a Meeting without the Amazon Chime App
      <https://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html>`__ .
    """


_ClientGetAccountSettingsResponseTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseTypeDef",
    {"AccountSettings": ClientGetAccountSettingsResponseAccountSettingsTypeDef},
    total=False,
)


class ClientGetAccountSettingsResponseTypeDef(_ClientGetAccountSettingsResponseTypeDef):
    """
    Type definition for `ClientGetAccountSettings` `Response`

    - **AccountSettings** *(dict) --*

      The Amazon Chime account settings.

      - **DisableRemoteControl** *(boolean) --*

        Setting that stops or starts remote control of shared screens during meetings.

      - **EnableDialOut** *(boolean) --*

        Setting that allows meeting participants to choose the **Call me at a phone number**
        option. For more information, see `Join a Meeting without the Amazon Chime App
        <https://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html>`__ .
    """


_ClientGetBotResponseBotTypeDef = TypedDict(
    "_ClientGetBotResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)


class ClientGetBotResponseBotTypeDef(_ClientGetBotResponseBotTypeDef):
    """
    Type definition for `ClientGetBotResponse` `Bot`

    The chat bot details.

    - **BotId** *(string) --*

      The bot ID.

    - **UserId** *(string) --*

      The unique ID for the bot user.

    - **DisplayName** *(string) --*

      The bot display name.

    - **BotType** *(string) --*

      The bot type.

    - **Disabled** *(boolean) --*

      When true, the bot is stopped from running in your account.

    - **CreatedTimestamp** *(datetime) --*

      The bot creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated bot timestamp, in ISO 8601 format.

    - **BotEmail** *(string) --*

      The bot email address.

    - **SecurityToken** *(string) --*

      The security token used to authenticate Amazon Chime with the outgoing event endpoint.
    """


_ClientGetBotResponseTypeDef = TypedDict(
    "_ClientGetBotResponseTypeDef", {"Bot": ClientGetBotResponseBotTypeDef}, total=False
)


class ClientGetBotResponseTypeDef(_ClientGetBotResponseTypeDef):
    """
    Type definition for `ClientGetBot` `Response`

    - **Bot** *(dict) --*

      The chat bot details.

      - **BotId** *(string) --*

        The bot ID.

      - **UserId** *(string) --*

        The unique ID for the bot user.

      - **DisplayName** *(string) --*

        The bot display name.

      - **BotType** *(string) --*

        The bot type.

      - **Disabled** *(boolean) --*

        When true, the bot is stopped from running in your account.

      - **CreatedTimestamp** *(datetime) --*

        The bot creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated bot timestamp, in ISO 8601 format.

      - **BotEmail** *(string) --*

        The bot email address.

      - **SecurityToken** *(string) --*

        The security token used to authenticate Amazon Chime with the outgoing event endpoint.
    """


_ClientGetEventsConfigurationResponseEventsConfigurationTypeDef = TypedDict(
    "_ClientGetEventsConfigurationResponseEventsConfigurationTypeDef",
    {"BotId": str, "OutboundEventsHTTPSEndpoint": str, "LambdaFunctionArn": str},
    total=False,
)


class ClientGetEventsConfigurationResponseEventsConfigurationTypeDef(
    _ClientGetEventsConfigurationResponseEventsConfigurationTypeDef
):
    """
    Type definition for `ClientGetEventsConfigurationResponse` `EventsConfiguration`

    The events configuration details.

    - **BotId** *(string) --*

      The bot ID.

    - **OutboundEventsHTTPSEndpoint** *(string) --*

      HTTPS endpoint that allows a bot to receive outgoing events.

    - **LambdaFunctionArn** *(string) --*

      Lambda function ARN that allows a bot to receive outgoing events.
    """


_ClientGetEventsConfigurationResponseTypeDef = TypedDict(
    "_ClientGetEventsConfigurationResponseTypeDef",
    {
        "EventsConfiguration": ClientGetEventsConfigurationResponseEventsConfigurationTypeDef
    },
    total=False,
)


class ClientGetEventsConfigurationResponseTypeDef(
    _ClientGetEventsConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetEventsConfiguration` `Response`

    - **EventsConfiguration** *(dict) --*

      The events configuration details.

      - **BotId** *(string) --*

        The bot ID.

      - **OutboundEventsHTTPSEndpoint** *(string) --*

        HTTPS endpoint that allows a bot to receive outgoing events.

      - **LambdaFunctionArn** *(string) --*

        Lambda function ARN that allows a bot to receive outgoing events.
    """


_ClientGetGlobalSettingsResponseBusinessCallingTypeDef = TypedDict(
    "_ClientGetGlobalSettingsResponseBusinessCallingTypeDef",
    {"CdrBucket": str},
    total=False,
)


class ClientGetGlobalSettingsResponseBusinessCallingTypeDef(
    _ClientGetGlobalSettingsResponseBusinessCallingTypeDef
):
    """
    Type definition for `ClientGetGlobalSettingsResponse` `BusinessCalling`

    The Amazon Chime Business Calling settings.

    - **CdrBucket** *(string) --*

      The Amazon S3 bucket designated for call detail record storage.
    """


_ClientGetGlobalSettingsResponseVoiceConnectorTypeDef = TypedDict(
    "_ClientGetGlobalSettingsResponseVoiceConnectorTypeDef",
    {"CdrBucket": str},
    total=False,
)


class ClientGetGlobalSettingsResponseVoiceConnectorTypeDef(
    _ClientGetGlobalSettingsResponseVoiceConnectorTypeDef
):
    """
    Type definition for `ClientGetGlobalSettingsResponse` `VoiceConnector`

    The Amazon Chime Voice Connector settings.

    - **CdrBucket** *(string) --*

      The Amazon S3 bucket designated for call detail record storage.
    """


_ClientGetGlobalSettingsResponseTypeDef = TypedDict(
    "_ClientGetGlobalSettingsResponseTypeDef",
    {
        "BusinessCalling": ClientGetGlobalSettingsResponseBusinessCallingTypeDef,
        "VoiceConnector": ClientGetGlobalSettingsResponseVoiceConnectorTypeDef,
    },
    total=False,
)


class ClientGetGlobalSettingsResponseTypeDef(_ClientGetGlobalSettingsResponseTypeDef):
    """
    Type definition for `ClientGetGlobalSettings` `Response`

    - **BusinessCalling** *(dict) --*

      The Amazon Chime Business Calling settings.

      - **CdrBucket** *(string) --*

        The Amazon S3 bucket designated for call detail record storage.

    - **VoiceConnector** *(dict) --*

      The Amazon Chime Voice Connector settings.

      - **CdrBucket** *(string) --*

        The Amazon S3 bucket designated for call detail record storage.
    """


_ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef = TypedDict(
    "_ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    {"E164PhoneNumber": str, "Status": str},
    total=False,
)


class ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef(
    _ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef
):
    """
    Type definition for `ClientGetPhoneNumberOrderResponsePhoneNumberOrder` `OrderedPhoneNumbers`

    A phone number for which an order has been placed.

    - **E164PhoneNumber** *(string) --*

      The phone number, in E.164 format.

    - **Status** *(string) --*

      The phone number status.
    """


_ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef = TypedDict(
    "_ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": str,
        "Status": str,
        "OrderedPhoneNumbers": List[
            ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef(
    _ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef
):
    """
    Type definition for `ClientGetPhoneNumberOrderResponse` `PhoneNumberOrder`

    The phone number order details.

    - **PhoneNumberOrderId** *(string) --*

      The phone number order ID.

    - **ProductType** *(string) --*

      The phone number order product type.

    - **Status** *(string) --*

      The status of the phone number order.

    - **OrderedPhoneNumbers** *(list) --*

      The ordered phone number details, such as the phone number in E.164 format and the phone
      number status.

      - *(dict) --*

        A phone number for which an order has been placed.

        - **E164PhoneNumber** *(string) --*

          The phone number, in E.164 format.

        - **Status** *(string) --*

          The phone number status.

    - **CreatedTimestamp** *(datetime) --*

      The phone number order creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated phone number order timestamp, in ISO 8601 format.
    """


_ClientGetPhoneNumberOrderResponseTypeDef = TypedDict(
    "_ClientGetPhoneNumberOrderResponseTypeDef",
    {"PhoneNumberOrder": ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef},
    total=False,
)


class ClientGetPhoneNumberOrderResponseTypeDef(
    _ClientGetPhoneNumberOrderResponseTypeDef
):
    """
    Type definition for `ClientGetPhoneNumberOrder` `Response`

    - **PhoneNumberOrder** *(dict) --*

      The phone number order details.

      - **PhoneNumberOrderId** *(string) --*

        The phone number order ID.

      - **ProductType** *(string) --*

        The phone number order product type.

      - **Status** *(string) --*

        The status of the phone number order.

      - **OrderedPhoneNumbers** *(list) --*

        The ordered phone number details, such as the phone number in E.164 format and the phone
        number status.

        - *(dict) --*

          A phone number for which an order has been placed.

          - **E164PhoneNumber** *(string) --*

            The phone number, in E.164 format.

          - **Status** *(string) --*

            The phone number status.

      - **CreatedTimestamp** *(datetime) --*

        The phone number order creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated phone number order timestamp, in ISO 8601 format.
    """


_ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef = TypedDict(
    "_ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef",
    {"Value": str, "Name": str, "AssociatedTimestamp": datetime},
    total=False,
)


class ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef(
    _ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef
):
    """
    Type definition for `ClientGetPhoneNumberResponsePhoneNumber` `Associations`

    The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
    Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

    - **Value** *(string) --*

      Contains the ID for the entity specified in Name.

    - **Name** *(string) --*

      Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
      Connector ID, or Amazon Chime Voice Connector group ID.

    - **AssociatedTimestamp** *(datetime) --*

      The timestamp of the phone number association, in ISO 8601 format.
    """


_ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef = TypedDict(
    "_ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)


class ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef(
    _ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef
):
    """
    Type definition for `ClientGetPhoneNumberResponsePhoneNumber` `Capabilities`

    The phone number capabilities.

    - **InboundCall** *(boolean) --*

      Allows or denies inbound calling for the specified phone number.

    - **OutboundCall** *(boolean) --*

      Allows or denies outbound calling for the specified phone number.

    - **InboundSMS** *(boolean) --*

      Allows or denies inbound SMS messaging for the specified phone number.

    - **OutboundSMS** *(boolean) --*

      Allows or denies outbound SMS messaging for the specified phone number.

    - **InboundMMS** *(boolean) --*

      Allows or denies inbound MMS messaging for the specified phone number.

    - **OutboundMMS** *(boolean) --*

      Allows or denies outbound MMS messaging for the specified phone number.
    """


_ClientGetPhoneNumberResponsePhoneNumberTypeDef = TypedDict(
    "_ClientGetPhoneNumberResponsePhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": str,
        "ProductType": str,
        "Status": str,
        "Capabilities": ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef,
        "Associations": List[
            ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef
        ],
        "CallingName": str,
        "CallingNameStatus": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)


class ClientGetPhoneNumberResponsePhoneNumberTypeDef(
    _ClientGetPhoneNumberResponsePhoneNumberTypeDef
):
    """
    Type definition for `ClientGetPhoneNumberResponse` `PhoneNumber`

    The phone number details.

    - **PhoneNumberId** *(string) --*

      The phone number ID.

    - **E164PhoneNumber** *(string) --*

      The phone number, in E.164 format.

    - **Type** *(string) --*

      The phone number type.

    - **ProductType** *(string) --*

      The phone number product type.

    - **Status** *(string) --*

      The phone number status.

    - **Capabilities** *(dict) --*

      The phone number capabilities.

      - **InboundCall** *(boolean) --*

        Allows or denies inbound calling for the specified phone number.

      - **OutboundCall** *(boolean) --*

        Allows or denies outbound calling for the specified phone number.

      - **InboundSMS** *(boolean) --*

        Allows or denies inbound SMS messaging for the specified phone number.

      - **OutboundSMS** *(boolean) --*

        Allows or denies outbound SMS messaging for the specified phone number.

      - **InboundMMS** *(boolean) --*

        Allows or denies inbound MMS messaging for the specified phone number.

      - **OutboundMMS** *(boolean) --*

        Allows or denies outbound MMS messaging for the specified phone number.

    - **Associations** *(list) --*

      The phone number associations.

      - *(dict) --*

        The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
        Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

        - **Value** *(string) --*

          Contains the ID for the entity specified in Name.

        - **Name** *(string) --*

          Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
          Connector ID, or Amazon Chime Voice Connector group ID.

        - **AssociatedTimestamp** *(datetime) --*

          The timestamp of the phone number association, in ISO 8601 format.

    - **CallingName** *(string) --*

      The outbound calling name associated with the phone number.

    - **CallingNameStatus** *(string) --*

      The outbound calling name status.

    - **CreatedTimestamp** *(datetime) --*

      The phone number creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated phone number timestamp, in ISO 8601 format.

    - **DeletionTimestamp** *(datetime) --*

      The deleted phone number timestamp, in ISO 8601 format.
    """


_ClientGetPhoneNumberResponseTypeDef = TypedDict(
    "_ClientGetPhoneNumberResponseTypeDef",
    {"PhoneNumber": ClientGetPhoneNumberResponsePhoneNumberTypeDef},
    total=False,
)


class ClientGetPhoneNumberResponseTypeDef(_ClientGetPhoneNumberResponseTypeDef):
    """
    Type definition for `ClientGetPhoneNumber` `Response`

    - **PhoneNumber** *(dict) --*

      The phone number details.

      - **PhoneNumberId** *(string) --*

        The phone number ID.

      - **E164PhoneNumber** *(string) --*

        The phone number, in E.164 format.

      - **Type** *(string) --*

        The phone number type.

      - **ProductType** *(string) --*

        The phone number product type.

      - **Status** *(string) --*

        The phone number status.

      - **Capabilities** *(dict) --*

        The phone number capabilities.

        - **InboundCall** *(boolean) --*

          Allows or denies inbound calling for the specified phone number.

        - **OutboundCall** *(boolean) --*

          Allows or denies outbound calling for the specified phone number.

        - **InboundSMS** *(boolean) --*

          Allows or denies inbound SMS messaging for the specified phone number.

        - **OutboundSMS** *(boolean) --*

          Allows or denies outbound SMS messaging for the specified phone number.

        - **InboundMMS** *(boolean) --*

          Allows or denies inbound MMS messaging for the specified phone number.

        - **OutboundMMS** *(boolean) --*

          Allows or denies outbound MMS messaging for the specified phone number.

      - **Associations** *(list) --*

        The phone number associations.

        - *(dict) --*

          The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
          Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

          - **Value** *(string) --*

            Contains the ID for the entity specified in Name.

          - **Name** *(string) --*

            Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
            Connector ID, or Amazon Chime Voice Connector group ID.

          - **AssociatedTimestamp** *(datetime) --*

            The timestamp of the phone number association, in ISO 8601 format.

      - **CallingName** *(string) --*

        The outbound calling name associated with the phone number.

      - **CallingNameStatus** *(string) --*

        The outbound calling name status.

      - **CreatedTimestamp** *(datetime) --*

        The phone number creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated phone number timestamp, in ISO 8601 format.

      - **DeletionTimestamp** *(datetime) --*

        The deleted phone number timestamp, in ISO 8601 format.
    """


_ClientGetPhoneNumberSettingsResponseTypeDef = TypedDict(
    "_ClientGetPhoneNumberSettingsResponseTypeDef",
    {"CallingName": str, "CallingNameUpdatedTimestamp": datetime},
    total=False,
)


class ClientGetPhoneNumberSettingsResponseTypeDef(
    _ClientGetPhoneNumberSettingsResponseTypeDef
):
    """
    Type definition for `ClientGetPhoneNumberSettings` `Response`

    - **CallingName** *(string) --*

      The default outbound calling name for the account.

    - **CallingNameUpdatedTimestamp** *(datetime) --*

      The updated outbound calling name timestamp, in ISO 8601 format.
    """


_ClientGetRoomResponseRoomTypeDef = TypedDict(
    "_ClientGetRoomResponseRoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientGetRoomResponseRoomTypeDef(_ClientGetRoomResponseRoomTypeDef):
    """
    Type definition for `ClientGetRoomResponse` `Room`

    The room details.

    - **RoomId** *(string) --*

      The room ID.

    - **Name** *(string) --*

      The room name.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **CreatedBy** *(string) --*

      The identifier of the room creator.

    - **CreatedTimestamp** *(datetime) --*

      The room creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The room update timestamp, in ISO 8601 format.
    """


_ClientGetRoomResponseTypeDef = TypedDict(
    "_ClientGetRoomResponseTypeDef",
    {"Room": ClientGetRoomResponseRoomTypeDef},
    total=False,
)


class ClientGetRoomResponseTypeDef(_ClientGetRoomResponseTypeDef):
    """
    Type definition for `ClientGetRoom` `Response`

    - **Room** *(dict) --*

      The room details.

      - **RoomId** *(string) --*

        The room ID.

      - **Name** *(string) --*

        The room name.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

      - **CreatedBy** *(string) --*

        The identifier of the room creator.

      - **CreatedTimestamp** *(datetime) --*

        The room creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The room update timestamp, in ISO 8601 format.
    """


_ClientGetUserResponseUserTypeDef = TypedDict(
    "_ClientGetUserResponseUserTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": str,
        "UserRegistrationStatus": str,
        "UserInvitationStatus": str,
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "PersonalPIN": str,
    },
    total=False,
)


class ClientGetUserResponseUserTypeDef(_ClientGetUserResponseUserTypeDef):
    """
    Type definition for `ClientGetUserResponse` `User`

    The user details.

    - **UserId** *(string) --*

      The user ID.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **PrimaryEmail** *(string) --*

      The primary email address of the user.

    - **PrimaryProvisionedNumber** *(string) --*

      The primary phone number associated with the user.

    - **DisplayName** *(string) --*

      The display name of the user.

    - **LicenseType** *(string) --*

      The license type for the user.

    - **UserRegistrationStatus** *(string) --*

      The user registration status.

    - **UserInvitationStatus** *(string) --*

      The user invite status.

    - **RegisteredOn** *(datetime) --*

      Date and time when the user is registered, in ISO 8601 format.

    - **InvitedOn** *(datetime) --*

      Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

    - **PersonalPIN** *(string) --*

      The user's personal meeting PIN.
    """


_ClientGetUserResponseTypeDef = TypedDict(
    "_ClientGetUserResponseTypeDef",
    {"User": ClientGetUserResponseUserTypeDef},
    total=False,
)


class ClientGetUserResponseTypeDef(_ClientGetUserResponseTypeDef):
    """
    Type definition for `ClientGetUser` `Response`

    - **User** *(dict) --*

      The user details.

      - **UserId** *(string) --*

        The user ID.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

      - **PrimaryEmail** *(string) --*

        The primary email address of the user.

      - **PrimaryProvisionedNumber** *(string) --*

        The primary phone number associated with the user.

      - **DisplayName** *(string) --*

        The display name of the user.

      - **LicenseType** *(string) --*

        The license type for the user.

      - **UserRegistrationStatus** *(string) --*

        The user registration status.

      - **UserInvitationStatus** *(string) --*

        The user invite status.

      - **RegisteredOn** *(datetime) --*

        Date and time when the user is registered, in ISO 8601 format.

      - **InvitedOn** *(datetime) --*

        Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

      - **PersonalPIN** *(string) --*

        The user's personal meeting PIN.
    """


_ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef = TypedDict(
    "_ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef",
    {"InboundCalling": bool, "OutboundCalling": bool, "SMS": bool},
    total=False,
)


class ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef(
    _ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef
):
    """
    Type definition for `ClientGetUserSettingsResponseUserSettings` `Telephony`

    The telephony settings associated with the user.

    - **InboundCalling** *(boolean) --*

      Allows or denies inbound calling.

    - **OutboundCalling** *(boolean) --*

      Allows or denies outbound calling.

    - **SMS** *(boolean) --*

      Allows or denies SMS messaging.
    """


_ClientGetUserSettingsResponseUserSettingsTypeDef = TypedDict(
    "_ClientGetUserSettingsResponseUserSettingsTypeDef",
    {"Telephony": ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef},
    total=False,
)


class ClientGetUserSettingsResponseUserSettingsTypeDef(
    _ClientGetUserSettingsResponseUserSettingsTypeDef
):
    """
    Type definition for `ClientGetUserSettingsResponse` `UserSettings`

    The user settings.

    - **Telephony** *(dict) --*

      The telephony settings associated with the user.

      - **InboundCalling** *(boolean) --*

        Allows or denies inbound calling.

      - **OutboundCalling** *(boolean) --*

        Allows or denies outbound calling.

      - **SMS** *(boolean) --*

        Allows or denies SMS messaging.
    """


_ClientGetUserSettingsResponseTypeDef = TypedDict(
    "_ClientGetUserSettingsResponseTypeDef",
    {"UserSettings": ClientGetUserSettingsResponseUserSettingsTypeDef},
    total=False,
)


class ClientGetUserSettingsResponseTypeDef(_ClientGetUserSettingsResponseTypeDef):
    """
    Type definition for `ClientGetUserSettings` `Response`

    - **UserSettings** *(dict) --*

      The user settings.

      - **Telephony** *(dict) --*

        The telephony settings associated with the user.

        - **InboundCalling** *(boolean) --*

          Allows or denies inbound calling.

        - **OutboundCalling** *(boolean) --*

          Allows or denies outbound calling.

        - **SMS** *(boolean) --*

          Allows or denies SMS messaging.
    """


_ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)


class ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorGroupResponseVoiceConnectorGroup` `VoiceConnectorItems`

    For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
    route inbound calls. Includes priority configuration settings. Limit: 3
    ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

    - **VoiceConnectorId** *(string) --*

      The Amazon Chime Voice Connector ID.

    - **Priority** *(integer) --*

      The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
      priority. Higher priority Amazon Chime Voice Connectors are attempted first.
    """


_ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef = TypedDict(
    "_ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef(
    _ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorGroupResponse` `VoiceConnectorGroup`

    The Amazon Chime Voice Connector group details.

    - **VoiceConnectorGroupId** *(string) --*

      The Amazon Chime Voice Connector group ID.

    - **Name** *(string) --*

      The name of the Amazon Chime Voice Connector group.

    - **VoiceConnectorItems** *(list) --*

      The Amazon Chime Voice Connectors to which to route inbound calls.

      - *(dict) --*

        For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
        route inbound calls. Includes priority configuration settings. Limit: 3
        ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

        - **VoiceConnectorId** *(string) --*

          The Amazon Chime Voice Connector ID.

        - **Priority** *(integer) --*

          The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
          priority. Higher priority Amazon Chime Voice Connectors are attempted first.

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.
    """


_ClientGetVoiceConnectorGroupResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef
    },
    total=False,
)


class ClientGetVoiceConnectorGroupResponseTypeDef(
    _ClientGetVoiceConnectorGroupResponseTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorGroup` `Response`

    - **VoiceConnectorGroup** *(dict) --*

      The Amazon Chime Voice Connector group details.

      - **VoiceConnectorGroupId** *(string) --*

        The Amazon Chime Voice Connector group ID.

      - **Name** *(string) --*

        The name of the Amazon Chime Voice Connector group.

      - **VoiceConnectorItems** *(list) --*

        The Amazon Chime Voice Connectors to which to route inbound calls.

        - *(dict) --*

          For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
          route inbound calls. Includes priority configuration settings. Limit: 3
          ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

          - **VoiceConnectorId** *(string) --*

            The Amazon Chime Voice Connector ID.

          - **Priority** *(integer) --*

            The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
            priority. Higher priority Amazon Chime Voice Connectors are attempted first.

      - **CreatedTimestamp** *(datetime) --*

        The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.
    """


_ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "_ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {"EnableSIPLogs": bool},
    total=False,
)


class ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef(
    _ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorLoggingConfigurationResponse` `LoggingConfiguration`

    The logging configuration details.

    - **EnableSIPLogs** *(boolean) --*

      When true, enables SIP message logs for sending to Amazon CloudWatch Logs.
    """


_ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef
    },
    total=False,
)


class ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef(
    _ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorLoggingConfiguration` `Response`

    - **LoggingConfiguration** *(dict) --*

      The logging configuration details.

      - **EnableSIPLogs** *(boolean) --*

        When true, enables SIP message logs for sending to Amazon CloudWatch Logs.
    """


_ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef = TypedDict(
    "_ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    {"Host": str, "Port": int, "Protocol": str, "Priority": int, "Weight": int},
    total=False,
)


class ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef(
    _ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorOriginationResponseOrigination` `Routes`

    Origination routes define call distribution properties for your SIP hosts to receive
    inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
    each Amazon Chime Voice Connector.

    - **Host** *(string) --*

      The FQDN or IP address to contact for origination traffic.

    - **Port** *(integer) --*

      The designated origination route port. Defaults to 5060.

    - **Protocol** *(string) --*

      The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
      Connectors use TCP protocol by default.

    - **Priority** *(integer) --*

      The priority associated with the host, with 1 being the highest priority. Higher
      priority hosts are attempted first.

    - **Weight** *(integer) --*

      The weight associated with the host. If hosts are equal in priority, calls are
      distributed among them based on their relative weight.
    """


_ClientGetVoiceConnectorOriginationResponseOriginationTypeDef = TypedDict(
    "_ClientGetVoiceConnectorOriginationResponseOriginationTypeDef",
    {
        "Routes": List[
            ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef
        ],
        "Disabled": bool,
    },
    total=False,
)


class ClientGetVoiceConnectorOriginationResponseOriginationTypeDef(
    _ClientGetVoiceConnectorOriginationResponseOriginationTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorOriginationResponse` `Origination`

    The origination setting details.

    - **Routes** *(list) --*

      The call distribution properties defined for your SIP hosts. Valid range: Minimum value of
      1. Maximum value of 20.

      - *(dict) --*

        Origination routes define call distribution properties for your SIP hosts to receive
        inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
        each Amazon Chime Voice Connector.

        - **Host** *(string) --*

          The FQDN or IP address to contact for origination traffic.

        - **Port** *(integer) --*

          The designated origination route port. Defaults to 5060.

        - **Protocol** *(string) --*

          The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
          Connectors use TCP protocol by default.

        - **Priority** *(integer) --*

          The priority associated with the host, with 1 being the highest priority. Higher
          priority hosts are attempted first.

        - **Weight** *(integer) --*

          The weight associated with the host. If hosts are equal in priority, calls are
          distributed among them based on their relative weight.

    - **Disabled** *(boolean) --*

      When origination settings are disabled, inbound calls are not enabled for your Amazon Chime
      Voice Connector.
    """


_ClientGetVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorOriginationResponseTypeDef",
    {"Origination": ClientGetVoiceConnectorOriginationResponseOriginationTypeDef},
    total=False,
)


class ClientGetVoiceConnectorOriginationResponseTypeDef(
    _ClientGetVoiceConnectorOriginationResponseTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorOrigination` `Response`

    - **Origination** *(dict) --*

      The origination setting details.

      - **Routes** *(list) --*

        The call distribution properties defined for your SIP hosts. Valid range: Minimum value of
        1. Maximum value of 20.

        - *(dict) --*

          Origination routes define call distribution properties for your SIP hosts to receive
          inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
          each Amazon Chime Voice Connector.

          - **Host** *(string) --*

            The FQDN or IP address to contact for origination traffic.

          - **Port** *(integer) --*

            The designated origination route port. Defaults to 5060.

          - **Protocol** *(string) --*

            The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
            Connectors use TCP protocol by default.

          - **Priority** *(integer) --*

            The priority associated with the host, with 1 being the highest priority. Higher
            priority hosts are attempted first.

          - **Weight** *(integer) --*

            The weight associated with the host. If hosts are equal in priority, calls are
            distributed among them based on their relative weight.

      - **Disabled** *(boolean) --*

        When origination settings are disabled, inbound calls are not enabled for your Amazon Chime
        Voice Connector.
    """


_ClientGetVoiceConnectorResponseVoiceConnectorTypeDef = TypedDict(
    "_ClientGetVoiceConnectorResponseVoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": str,
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientGetVoiceConnectorResponseVoiceConnectorTypeDef(
    _ClientGetVoiceConnectorResponseVoiceConnectorTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorResponse` `VoiceConnector`

    The Amazon Chime Voice Connector details.

    - **VoiceConnectorId** *(string) --*

      The Amazon Chime Voice Connector ID.

    - **AwsRegion** *(string) --*

      The AWS Region in which the Amazon Chime Voice Connector is created. Default: ``us-east-1``
      .

    - **Name** *(string) --*

      The name of the Amazon Chime Voice Connector.

    - **OutboundHostName** *(string) --*

      The outbound host name for the Amazon Chime Voice Connector.

    - **RequireEncryption** *(boolean) --*

      Designates whether encryption is required for the Amazon Chime Voice Connector.

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
    """


_ClientGetVoiceConnectorResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorResponseTypeDef",
    {"VoiceConnector": ClientGetVoiceConnectorResponseVoiceConnectorTypeDef},
    total=False,
)


class ClientGetVoiceConnectorResponseTypeDef(_ClientGetVoiceConnectorResponseTypeDef):
    """
    Type definition for `ClientGetVoiceConnector` `Response`

    - **VoiceConnector** *(dict) --*

      The Amazon Chime Voice Connector details.

      - **VoiceConnectorId** *(string) --*

        The Amazon Chime Voice Connector ID.

      - **AwsRegion** *(string) --*

        The AWS Region in which the Amazon Chime Voice Connector is created. Default: ``us-east-1``
        .

      - **Name** *(string) --*

        The name of the Amazon Chime Voice Connector.

      - **OutboundHostName** *(string) --*

        The outbound host name for the Amazon Chime Voice Connector.

      - **RequireEncryption** *(boolean) --*

        Designates whether encryption is required for the Amazon Chime Voice Connector.

      - **CreatedTimestamp** *(datetime) --*

        The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
    """


_ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef = TypedDict(
    "_ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    {"DataRetentionInHours": int, "Disabled": bool},
    total=False,
)


class ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef(
    _ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorStreamingConfigurationResponse` `StreamingConfiguration`

    The streaming configuration details.

    - **DataRetentionInHours** *(integer) --*

      The retention period, in hours, for the Amazon Kinesis data.

    - **Disabled** *(boolean) --*

      When true, media streaming to Amazon Kinesis is turned off.
    """


_ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef
    },
    total=False,
)


class ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef(
    _ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorStreamingConfiguration` `Response`

    - **StreamingConfiguration** *(dict) --*

      The streaming configuration details.

      - **DataRetentionInHours** *(integer) --*

        The retention period, in hours, for the Amazon Kinesis data.

      - **Disabled** *(boolean) --*

        When true, media streaming to Amazon Kinesis is turned off.
    """


_ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef = TypedDict(
    "_ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef",
    {"Timestamp": datetime, "Source": str},
    total=False,
)


class ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef(
    _ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorTerminationHealthResponse` `TerminationHealth`

    The termination health details.

    - **Timestamp** *(datetime) --*

      The timestamp, in ISO 8601 format.

    - **Source** *(string) --*

      The source IP address.
    """


_ClientGetVoiceConnectorTerminationHealthResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorTerminationHealthResponseTypeDef",
    {
        "TerminationHealth": ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef
    },
    total=False,
)


class ClientGetVoiceConnectorTerminationHealthResponseTypeDef(
    _ClientGetVoiceConnectorTerminationHealthResponseTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorTerminationHealth` `Response`

    - **TerminationHealth** *(dict) --*

      The termination health details.

      - **Timestamp** *(datetime) --*

        The timestamp, in ISO 8601 format.

      - **Source** *(string) --*

        The source IP address.
    """


_ClientGetVoiceConnectorTerminationResponseTerminationTypeDef = TypedDict(
    "_ClientGetVoiceConnectorTerminationResponseTerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)


class ClientGetVoiceConnectorTerminationResponseTerminationTypeDef(
    _ClientGetVoiceConnectorTerminationResponseTerminationTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorTerminationResponse` `Termination`

    The termination setting details.

    - **CpsLimit** *(integer) --*

      The limit on calls per second. Max value based on account service limit. Default value of 1.

    - **DefaultPhoneNumber** *(string) --*

      The default caller ID phone number.

    - **CallingRegions** *(list) --*

      The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.

      - *(string) --*

    - **CidrAllowedList** *(list) --*

      The IP addresses allowed to make calls, in CIDR format. Required.

      - *(string) --*

    - **Disabled** *(boolean) --*

      When termination settings are disabled, outbound calls can not be made.
    """


_ClientGetVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorTerminationResponseTypeDef",
    {"Termination": ClientGetVoiceConnectorTerminationResponseTerminationTypeDef},
    total=False,
)


class ClientGetVoiceConnectorTerminationResponseTypeDef(
    _ClientGetVoiceConnectorTerminationResponseTypeDef
):
    """
    Type definition for `ClientGetVoiceConnectorTermination` `Response`

    - **Termination** *(dict) --*

      The termination setting details.

      - **CpsLimit** *(integer) --*

        The limit on calls per second. Max value based on account service limit. Default value of 1.

      - **DefaultPhoneNumber** *(string) --*

        The default caller ID phone number.

      - **CallingRegions** *(list) --*

        The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.

        - *(string) --*

      - **CidrAllowedList** *(list) --*

        The IP addresses allowed to make calls, in CIDR format. Required.

        - *(string) --*

      - **Disabled** *(boolean) --*

        When termination settings are disabled, outbound calls can not be made.
    """


_ClientInviteUsersResponseInvitesTypeDef = TypedDict(
    "_ClientInviteUsersResponseInvitesTypeDef",
    {"InviteId": str, "Status": str, "EmailAddress": str, "EmailStatus": str},
    total=False,
)


class ClientInviteUsersResponseInvitesTypeDef(_ClientInviteUsersResponseInvitesTypeDef):
    """
    Type definition for `ClientInviteUsersResponse` `Invites`

    Invitation object returned after emailing users to invite them to join the Amazon Chime
    ``Team`` account.

    - **InviteId** *(string) --*

      The invite ID.

    - **Status** *(string) --*

      The status of the invite.

    - **EmailAddress** *(string) --*

      The email address to which the invite is sent.

    - **EmailStatus** *(string) --*

      The status of the invite email.
    """


_ClientInviteUsersResponseTypeDef = TypedDict(
    "_ClientInviteUsersResponseTypeDef",
    {"Invites": List[ClientInviteUsersResponseInvitesTypeDef]},
    total=False,
)


class ClientInviteUsersResponseTypeDef(_ClientInviteUsersResponseTypeDef):
    """
    Type definition for `ClientInviteUsers` `Response`

    - **Invites** *(list) --*

      The email invitation details.

      - *(dict) --*

        Invitation object returned after emailing users to invite them to join the Amazon Chime
        ``Team`` account.

        - **InviteId** *(string) --*

          The invite ID.

        - **Status** *(string) --*

          The status of the invite.

        - **EmailAddress** *(string) --*

          The email address to which the invite is sent.

        - **EmailStatus** *(string) --*

          The status of the invite email.
    """


_ClientListAccountsResponseAccountsTypeDef = TypedDict(
    "_ClientListAccountsResponseAccountsTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": str,
        "CreatedTimestamp": datetime,
        "DefaultLicense": str,
        "SupportedLicenses": List[str],
    },
    total=False,
)


class ClientListAccountsResponseAccountsTypeDef(
    _ClientListAccountsResponseAccountsTypeDef
):
    """
    Type definition for `ClientListAccountsResponse` `Accounts`

    The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.

    - **AwsAccountId** *(string) --*

      The AWS account ID.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **Name** *(string) --*

      The Amazon Chime account name.

    - **AccountType** *(string) --*

      The Amazon Chime account type. For more information about different account types, see
      `Managing Your Amazon Chime Accounts
      <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
      Chime Administration Guide* .

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime account creation timestamp, in ISO 8601 format.

    - **DefaultLicense** *(string) --*

      The default license for the Amazon Chime account.

    - **SupportedLicenses** *(list) --*

      Supported licenses for the Amazon Chime account.

      - *(string) --*
    """


_ClientListAccountsResponseTypeDef = TypedDict(
    "_ClientListAccountsResponseTypeDef",
    {"Accounts": List[ClientListAccountsResponseAccountsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAccountsResponseTypeDef(_ClientListAccountsResponseTypeDef):
    """
    Type definition for `ClientListAccounts` `Response`

    - **Accounts** *(list) --*

      List of Amazon Chime accounts and account details.

      - *(dict) --*

        The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.

        - **AwsAccountId** *(string) --*

          The AWS account ID.

        - **AccountId** *(string) --*

          The Amazon Chime account ID.

        - **Name** *(string) --*

          The Amazon Chime account name.

        - **AccountType** *(string) --*

          The Amazon Chime account type. For more information about different account types, see
          `Managing Your Amazon Chime Accounts
          <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
          Chime Administration Guide* .

        - **CreatedTimestamp** *(datetime) --*

          The Amazon Chime account creation timestamp, in ISO 8601 format.

        - **DefaultLicense** *(string) --*

          The default license for the Amazon Chime account.

        - **SupportedLicenses** *(list) --*

          Supported licenses for the Amazon Chime account.

          - *(string) --*

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results.
    """


_ClientListBotsResponseBotsTypeDef = TypedDict(
    "_ClientListBotsResponseBotsTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)


class ClientListBotsResponseBotsTypeDef(_ClientListBotsResponseBotsTypeDef):
    """
    Type definition for `ClientListBotsResponse` `Bots`

    A resource that allows Enterprise account administrators to configure an interface to
    receive events from Amazon Chime.

    - **BotId** *(string) --*

      The bot ID.

    - **UserId** *(string) --*

      The unique ID for the bot user.

    - **DisplayName** *(string) --*

      The bot display name.

    - **BotType** *(string) --*

      The bot type.

    - **Disabled** *(boolean) --*

      When true, the bot is stopped from running in your account.

    - **CreatedTimestamp** *(datetime) --*

      The bot creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated bot timestamp, in ISO 8601 format.

    - **BotEmail** *(string) --*

      The bot email address.

    - **SecurityToken** *(string) --*

      The security token used to authenticate Amazon Chime with the outgoing event endpoint.
    """


_ClientListBotsResponseTypeDef = TypedDict(
    "_ClientListBotsResponseTypeDef",
    {"Bots": List[ClientListBotsResponseBotsTypeDef], "NextToken": str},
    total=False,
)


class ClientListBotsResponseTypeDef(_ClientListBotsResponseTypeDef):
    """
    Type definition for `ClientListBots` `Response`

    - **Bots** *(list) --*

      List of bots and bot details.

      - *(dict) --*

        A resource that allows Enterprise account administrators to configure an interface to
        receive events from Amazon Chime.

        - **BotId** *(string) --*

          The bot ID.

        - **UserId** *(string) --*

          The unique ID for the bot user.

        - **DisplayName** *(string) --*

          The bot display name.

        - **BotType** *(string) --*

          The bot type.

        - **Disabled** *(boolean) --*

          When true, the bot is stopped from running in your account.

        - **CreatedTimestamp** *(datetime) --*

          The bot creation timestamp, in ISO 8601 format.

        - **UpdatedTimestamp** *(datetime) --*

          The updated bot timestamp, in ISO 8601 format.

        - **BotEmail** *(string) --*

          The bot email address.

        - **SecurityToken** *(string) --*

          The security token used to authenticate Amazon Chime with the outgoing event endpoint.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results.
    """


_ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef = TypedDict(
    "_ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef",
    {"E164PhoneNumber": str, "Status": str},
    total=False,
)


class ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef(
    _ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef
):
    """
    Type definition for `ClientListPhoneNumberOrdersResponsePhoneNumberOrders` `OrderedPhoneNumbers`

    A phone number for which an order has been placed.

    - **E164PhoneNumber** *(string) --*

      The phone number, in E.164 format.

    - **Status** *(string) --*

      The phone number status.
    """


_ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef = TypedDict(
    "_ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": str,
        "Status": str,
        "OrderedPhoneNumbers": List[
            ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef(
    _ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef
):
    """
    Type definition for `ClientListPhoneNumberOrdersResponse` `PhoneNumberOrders`

    The details of a phone number order created for Amazon Chime.

    - **PhoneNumberOrderId** *(string) --*

      The phone number order ID.

    - **ProductType** *(string) --*

      The phone number order product type.

    - **Status** *(string) --*

      The status of the phone number order.

    - **OrderedPhoneNumbers** *(list) --*

      The ordered phone number details, such as the phone number in E.164 format and the phone
      number status.

      - *(dict) --*

        A phone number for which an order has been placed.

        - **E164PhoneNumber** *(string) --*

          The phone number, in E.164 format.

        - **Status** *(string) --*

          The phone number status.

    - **CreatedTimestamp** *(datetime) --*

      The phone number order creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated phone number order timestamp, in ISO 8601 format.
    """


_ClientListPhoneNumberOrdersResponseTypeDef = TypedDict(
    "_ClientListPhoneNumberOrdersResponseTypeDef",
    {
        "PhoneNumberOrders": List[
            ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPhoneNumberOrdersResponseTypeDef(
    _ClientListPhoneNumberOrdersResponseTypeDef
):
    """
    Type definition for `ClientListPhoneNumberOrders` `Response`

    - **PhoneNumberOrders** *(list) --*

      The phone number order details.

      - *(dict) --*

        The details of a phone number order created for Amazon Chime.

        - **PhoneNumberOrderId** *(string) --*

          The phone number order ID.

        - **ProductType** *(string) --*

          The phone number order product type.

        - **Status** *(string) --*

          The status of the phone number order.

        - **OrderedPhoneNumbers** *(list) --*

          The ordered phone number details, such as the phone number in E.164 format and the phone
          number status.

          - *(dict) --*

            A phone number for which an order has been placed.

            - **E164PhoneNumber** *(string) --*

              The phone number, in E.164 format.

            - **Status** *(string) --*

              The phone number status.

        - **CreatedTimestamp** *(datetime) --*

          The phone number order creation timestamp, in ISO 8601 format.

        - **UpdatedTimestamp** *(datetime) --*

          The updated phone number order timestamp, in ISO 8601 format.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results.
    """


_ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef",
    {"Value": str, "Name": str, "AssociatedTimestamp": datetime},
    total=False,
)


class ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef(
    _ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef
):
    """
    Type definition for `ClientListPhoneNumbersResponsePhoneNumbers` `Associations`

    The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
    Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

    - **Value** *(string) --*

      Contains the ID for the entity specified in Name.

    - **Name** *(string) --*

      Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
      Connector ID, or Amazon Chime Voice Connector group ID.

    - **AssociatedTimestamp** *(datetime) --*

      The timestamp of the phone number association, in ISO 8601 format.
    """


_ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)


class ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef(
    _ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef
):
    """
    Type definition for `ClientListPhoneNumbersResponsePhoneNumbers` `Capabilities`

    The phone number capabilities.

    - **InboundCall** *(boolean) --*

      Allows or denies inbound calling for the specified phone number.

    - **OutboundCall** *(boolean) --*

      Allows or denies outbound calling for the specified phone number.

    - **InboundSMS** *(boolean) --*

      Allows or denies inbound SMS messaging for the specified phone number.

    - **OutboundSMS** *(boolean) --*

      Allows or denies outbound SMS messaging for the specified phone number.

    - **InboundMMS** *(boolean) --*

      Allows or denies inbound MMS messaging for the specified phone number.

    - **OutboundMMS** *(boolean) --*

      Allows or denies outbound MMS messaging for the specified phone number.
    """


_ClientListPhoneNumbersResponsePhoneNumbersTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponsePhoneNumbersTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": str,
        "ProductType": str,
        "Status": str,
        "Capabilities": ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef,
        "Associations": List[
            ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef
        ],
        "CallingName": str,
        "CallingNameStatus": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)


class ClientListPhoneNumbersResponsePhoneNumbersTypeDef(
    _ClientListPhoneNumbersResponsePhoneNumbersTypeDef
):
    """
    Type definition for `ClientListPhoneNumbersResponse` `PhoneNumbers`

    A phone number used for Amazon Chime Business Calling or an Amazon Chime Voice Connector.

    - **PhoneNumberId** *(string) --*

      The phone number ID.

    - **E164PhoneNumber** *(string) --*

      The phone number, in E.164 format.

    - **Type** *(string) --*

      The phone number type.

    - **ProductType** *(string) --*

      The phone number product type.

    - **Status** *(string) --*

      The phone number status.

    - **Capabilities** *(dict) --*

      The phone number capabilities.

      - **InboundCall** *(boolean) --*

        Allows or denies inbound calling for the specified phone number.

      - **OutboundCall** *(boolean) --*

        Allows or denies outbound calling for the specified phone number.

      - **InboundSMS** *(boolean) --*

        Allows or denies inbound SMS messaging for the specified phone number.

      - **OutboundSMS** *(boolean) --*

        Allows or denies outbound SMS messaging for the specified phone number.

      - **InboundMMS** *(boolean) --*

        Allows or denies inbound MMS messaging for the specified phone number.

      - **OutboundMMS** *(boolean) --*

        Allows or denies outbound MMS messaging for the specified phone number.

    - **Associations** *(list) --*

      The phone number associations.

      - *(dict) --*

        The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
        Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

        - **Value** *(string) --*

          Contains the ID for the entity specified in Name.

        - **Name** *(string) --*

          Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
          Connector ID, or Amazon Chime Voice Connector group ID.

        - **AssociatedTimestamp** *(datetime) --*

          The timestamp of the phone number association, in ISO 8601 format.

    - **CallingName** *(string) --*

      The outbound calling name associated with the phone number.

    - **CallingNameStatus** *(string) --*

      The outbound calling name status.

    - **CreatedTimestamp** *(datetime) --*

      The phone number creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated phone number timestamp, in ISO 8601 format.

    - **DeletionTimestamp** *(datetime) --*

      The deleted phone number timestamp, in ISO 8601 format.
    """


_ClientListPhoneNumbersResponseTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumbers": List[ClientListPhoneNumbersResponsePhoneNumbersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListPhoneNumbersResponseTypeDef(_ClientListPhoneNumbersResponseTypeDef):
    """
    Type definition for `ClientListPhoneNumbers` `Response`

    - **PhoneNumbers** *(list) --*

      The phone number details.

      - *(dict) --*

        A phone number used for Amazon Chime Business Calling or an Amazon Chime Voice Connector.

        - **PhoneNumberId** *(string) --*

          The phone number ID.

        - **E164PhoneNumber** *(string) --*

          The phone number, in E.164 format.

        - **Type** *(string) --*

          The phone number type.

        - **ProductType** *(string) --*

          The phone number product type.

        - **Status** *(string) --*

          The phone number status.

        - **Capabilities** *(dict) --*

          The phone number capabilities.

          - **InboundCall** *(boolean) --*

            Allows or denies inbound calling for the specified phone number.

          - **OutboundCall** *(boolean) --*

            Allows or denies outbound calling for the specified phone number.

          - **InboundSMS** *(boolean) --*

            Allows or denies inbound SMS messaging for the specified phone number.

          - **OutboundSMS** *(boolean) --*

            Allows or denies outbound SMS messaging for the specified phone number.

          - **InboundMMS** *(boolean) --*

            Allows or denies inbound MMS messaging for the specified phone number.

          - **OutboundMMS** *(boolean) --*

            Allows or denies outbound MMS messaging for the specified phone number.

        - **Associations** *(list) --*

          The phone number associations.

          - *(dict) --*

            The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
            Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

            - **Value** *(string) --*

              Contains the ID for the entity specified in Name.

            - **Name** *(string) --*

              Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
              Connector ID, or Amazon Chime Voice Connector group ID.

            - **AssociatedTimestamp** *(datetime) --*

              The timestamp of the phone number association, in ISO 8601 format.

        - **CallingName** *(string) --*

          The outbound calling name associated with the phone number.

        - **CallingNameStatus** *(string) --*

          The outbound calling name status.

        - **CreatedTimestamp** *(datetime) --*

          The phone number creation timestamp, in ISO 8601 format.

        - **UpdatedTimestamp** *(datetime) --*

          The updated phone number timestamp, in ISO 8601 format.

        - **DeletionTimestamp** *(datetime) --*

          The deleted phone number timestamp, in ISO 8601 format.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results.
    """


_ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef = TypedDict(
    "_ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": str,
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)


class ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef(
    _ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef
):
    """
    Type definition for `ClientListRoomMembershipsResponseRoomMemberships` `Member`

    The member details, such as email address, name, member ID, and member type.

    - **MemberId** *(string) --*

      The member ID (user ID or bot ID).

    - **MemberType** *(string) --*

      The member type.

    - **Email** *(string) --*

      The member email address.

    - **FullName** *(string) --*

      The member name.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.
    """


_ClientListRoomMembershipsResponseRoomMembershipsTypeDef = TypedDict(
    "_ClientListRoomMembershipsResponseRoomMembershipsTypeDef",
    {
        "RoomId": str,
        "Member": ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef,
        "Role": str,
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientListRoomMembershipsResponseRoomMembershipsTypeDef(
    _ClientListRoomMembershipsResponseRoomMembershipsTypeDef
):
    """
    Type definition for `ClientListRoomMembershipsResponse` `RoomMemberships`

    The room membership details.

    - **RoomId** *(string) --*

      The room ID.

    - **Member** *(dict) --*

      The member details, such as email address, name, member ID, and member type.

      - **MemberId** *(string) --*

        The member ID (user ID or bot ID).

      - **MemberType** *(string) --*

        The member type.

      - **Email** *(string) --*

        The member email address.

      - **FullName** *(string) --*

        The member name.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

    - **Role** *(string) --*

      The membership role.

    - **InvitedBy** *(string) --*

      The identifier of the user that invited the room member.

    - **UpdatedTimestamp** *(datetime) --*

      The room membership update timestamp, in ISO 8601 format.
    """


_ClientListRoomMembershipsResponseTypeDef = TypedDict(
    "_ClientListRoomMembershipsResponseTypeDef",
    {
        "RoomMemberships": List[
            ClientListRoomMembershipsResponseRoomMembershipsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListRoomMembershipsResponseTypeDef(
    _ClientListRoomMembershipsResponseTypeDef
):
    """
    Type definition for `ClientListRoomMemberships` `Response`

    - **RoomMemberships** *(list) --*

      The room membership details.

      - *(dict) --*

        The room membership details.

        - **RoomId** *(string) --*

          The room ID.

        - **Member** *(dict) --*

          The member details, such as email address, name, member ID, and member type.

          - **MemberId** *(string) --*

            The member ID (user ID or bot ID).

          - **MemberType** *(string) --*

            The member type.

          - **Email** *(string) --*

            The member email address.

          - **FullName** *(string) --*

            The member name.

          - **AccountId** *(string) --*

            The Amazon Chime account ID.

        - **Role** *(string) --*

          The membership role.

        - **InvitedBy** *(string) --*

          The identifier of the user that invited the room member.

        - **UpdatedTimestamp** *(datetime) --*

          The room membership update timestamp, in ISO 8601 format.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results.
    """


_ClientListRoomsResponseRoomsTypeDef = TypedDict(
    "_ClientListRoomsResponseRoomsTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientListRoomsResponseRoomsTypeDef(_ClientListRoomsResponseRoomsTypeDef):
    """
    Type definition for `ClientListRoomsResponse` `Rooms`

    The Amazon Chime chat room details.

    - **RoomId** *(string) --*

      The room ID.

    - **Name** *(string) --*

      The room name.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **CreatedBy** *(string) --*

      The identifier of the room creator.

    - **CreatedTimestamp** *(datetime) --*

      The room creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The room update timestamp, in ISO 8601 format.
    """


_ClientListRoomsResponseTypeDef = TypedDict(
    "_ClientListRoomsResponseTypeDef",
    {"Rooms": List[ClientListRoomsResponseRoomsTypeDef], "NextToken": str},
    total=False,
)


class ClientListRoomsResponseTypeDef(_ClientListRoomsResponseTypeDef):
    """
    Type definition for `ClientListRooms` `Response`

    - **Rooms** *(list) --*

      The room details.

      - *(dict) --*

        The Amazon Chime chat room details.

        - **RoomId** *(string) --*

          The room ID.

        - **Name** *(string) --*

          The room name.

        - **AccountId** *(string) --*

          The Amazon Chime account ID.

        - **CreatedBy** *(string) --*

          The identifier of the room creator.

        - **CreatedTimestamp** *(datetime) --*

          The room creation timestamp, in ISO 8601 format.

        - **UpdatedTimestamp** *(datetime) --*

          The room update timestamp, in ISO 8601 format.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results.
    """


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": str,
        "UserRegistrationStatus": str,
        "UserInvitationStatus": str,
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "PersonalPIN": str,
    },
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    Type definition for `ClientListUsersResponse` `Users`

    The user on the Amazon Chime account.

    - **UserId** *(string) --*

      The user ID.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **PrimaryEmail** *(string) --*

      The primary email address of the user.

    - **PrimaryProvisionedNumber** *(string) --*

      The primary phone number associated with the user.

    - **DisplayName** *(string) --*

      The display name of the user.

    - **LicenseType** *(string) --*

      The license type for the user.

    - **UserRegistrationStatus** *(string) --*

      The user registration status.

    - **UserInvitationStatus** *(string) --*

      The user invite status.

    - **RegisteredOn** *(datetime) --*

      Date and time when the user is registered, in ISO 8601 format.

    - **InvitedOn** *(datetime) --*

      Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

    - **PersonalPIN** *(string) --*

      The user's personal meeting PIN.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "NextToken": str},
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    Type definition for `ClientListUsers` `Response`

    - **Users** *(list) --*

      List of users and user details.

      - *(dict) --*

        The user on the Amazon Chime account.

        - **UserId** *(string) --*

          The user ID.

        - **AccountId** *(string) --*

          The Amazon Chime account ID.

        - **PrimaryEmail** *(string) --*

          The primary email address of the user.

        - **PrimaryProvisionedNumber** *(string) --*

          The primary phone number associated with the user.

        - **DisplayName** *(string) --*

          The display name of the user.

        - **LicenseType** *(string) --*

          The license type for the user.

        - **UserRegistrationStatus** *(string) --*

          The user registration status.

        - **UserInvitationStatus** *(string) --*

          The user invite status.

        - **RegisteredOn** *(datetime) --*

          Date and time when the user is registered, in ISO 8601 format.

        - **InvitedOn** *(datetime) --*

          Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

        - **PersonalPIN** *(string) --*

          The user's personal meeting PIN.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results.
    """


_ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef = TypedDict(
    "_ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)


class ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef(
    _ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef
):
    """
    Type definition for `ClientListVoiceConnectorGroupsResponseVoiceConnectorGroups` `VoiceConnectorItems`

    For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
    route inbound calls. Includes priority configuration settings. Limit: 3
    ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

    - **VoiceConnectorId** *(string) --*

      The Amazon Chime Voice Connector ID.

    - **Priority** *(integer) --*

      The priority associated with the Amazon Chime Voice Connector, with 1 being the
      highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.
    """


_ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef = TypedDict(
    "_ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef(
    _ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef
):
    """
    Type definition for `ClientListVoiceConnectorGroupsResponse` `VoiceConnectorGroups`

    The Amazon Chime Voice Connector group configuration, including associated Amazon Chime
    Voice Connectors. You can include Amazon Chime Voice Connectors from different AWS Regions
    in your group. This creates a fault tolerant mechanism for fallback in case of availability
    events.

    - **VoiceConnectorGroupId** *(string) --*

      The Amazon Chime Voice Connector group ID.

    - **Name** *(string) --*

      The name of the Amazon Chime Voice Connector group.

    - **VoiceConnectorItems** *(list) --*

      The Amazon Chime Voice Connectors to which to route inbound calls.

      - *(dict) --*

        For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
        route inbound calls. Includes priority configuration settings. Limit: 3
        ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

        - **VoiceConnectorId** *(string) --*

          The Amazon Chime Voice Connector ID.

        - **Priority** *(integer) --*

          The priority associated with the Amazon Chime Voice Connector, with 1 being the
          highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.
    """


_ClientListVoiceConnectorGroupsResponseTypeDef = TypedDict(
    "_ClientListVoiceConnectorGroupsResponseTypeDef",
    {
        "VoiceConnectorGroups": List[
            ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListVoiceConnectorGroupsResponseTypeDef(
    _ClientListVoiceConnectorGroupsResponseTypeDef
):
    """
    Type definition for `ClientListVoiceConnectorGroups` `Response`

    - **VoiceConnectorGroups** *(list) --*

      The details of the Amazon Chime Voice Connector groups.

      - *(dict) --*

        The Amazon Chime Voice Connector group configuration, including associated Amazon Chime
        Voice Connectors. You can include Amazon Chime Voice Connectors from different AWS Regions
        in your group. This creates a fault tolerant mechanism for fallback in case of availability
        events.

        - **VoiceConnectorGroupId** *(string) --*

          The Amazon Chime Voice Connector group ID.

        - **Name** *(string) --*

          The name of the Amazon Chime Voice Connector group.

        - **VoiceConnectorItems** *(list) --*

          The Amazon Chime Voice Connectors to which to route inbound calls.

          - *(dict) --*

            For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
            route inbound calls. Includes priority configuration settings. Limit: 3
            ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

            - **VoiceConnectorId** *(string) --*

              The Amazon Chime Voice Connector ID.

            - **Priority** *(integer) --*

              The priority associated with the Amazon Chime Voice Connector, with 1 being the
              highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.

        - **CreatedTimestamp** *(datetime) --*

          The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

        - **UpdatedTimestamp** *(datetime) --*

          The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results.
    """


_ClientListVoiceConnectorTerminationCredentialsResponseTypeDef = TypedDict(
    "_ClientListVoiceConnectorTerminationCredentialsResponseTypeDef",
    {"Usernames": List[str]},
    total=False,
)


class ClientListVoiceConnectorTerminationCredentialsResponseTypeDef(
    _ClientListVoiceConnectorTerminationCredentialsResponseTypeDef
):
    """
    Type definition for `ClientListVoiceConnectorTerminationCredentials` `Response`

    - **Usernames** *(list) --*

      A list of user names.

      - *(string) --*
    """


_ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef = TypedDict(
    "_ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": str,
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef(
    _ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef
):
    """
    Type definition for `ClientListVoiceConnectorsResponse` `VoiceConnectors`

    The Amazon Chime Voice Connector configuration, including outbound host name and encryption
    settings.

    - **VoiceConnectorId** *(string) --*

      The Amazon Chime Voice Connector ID.

    - **AwsRegion** *(string) --*

      The AWS Region in which the Amazon Chime Voice Connector is created. Default:
      ``us-east-1`` .

    - **Name** *(string) --*

      The name of the Amazon Chime Voice Connector.

    - **OutboundHostName** *(string) --*

      The outbound host name for the Amazon Chime Voice Connector.

    - **RequireEncryption** *(boolean) --*

      Designates whether encryption is required for the Amazon Chime Voice Connector.

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
    """


_ClientListVoiceConnectorsResponseTypeDef = TypedDict(
    "_ClientListVoiceConnectorsResponseTypeDef",
    {
        "VoiceConnectors": List[
            ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListVoiceConnectorsResponseTypeDef(
    _ClientListVoiceConnectorsResponseTypeDef
):
    """
    Type definition for `ClientListVoiceConnectors` `Response`

    - **VoiceConnectors** *(list) --*

      The details of the Amazon Chime Voice Connectors.

      - *(dict) --*

        The Amazon Chime Voice Connector configuration, including outbound host name and encryption
        settings.

        - **VoiceConnectorId** *(string) --*

          The Amazon Chime Voice Connector ID.

        - **AwsRegion** *(string) --*

          The AWS Region in which the Amazon Chime Voice Connector is created. Default:
          ``us-east-1`` .

        - **Name** *(string) --*

          The name of the Amazon Chime Voice Connector.

        - **OutboundHostName** *(string) --*

          The outbound host name for the Amazon Chime Voice Connector.

        - **RequireEncryption** *(boolean) --*

          Designates whether encryption is required for the Amazon Chime Voice Connector.

        - **CreatedTimestamp** *(datetime) --*

          The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

        - **UpdatedTimestamp** *(datetime) --*

          The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results.
    """


_ClientPutEventsConfigurationResponseEventsConfigurationTypeDef = TypedDict(
    "_ClientPutEventsConfigurationResponseEventsConfigurationTypeDef",
    {"BotId": str, "OutboundEventsHTTPSEndpoint": str, "LambdaFunctionArn": str},
    total=False,
)


class ClientPutEventsConfigurationResponseEventsConfigurationTypeDef(
    _ClientPutEventsConfigurationResponseEventsConfigurationTypeDef
):
    """
    Type definition for `ClientPutEventsConfigurationResponse` `EventsConfiguration`

    The configuration that allows a bot to receive outgoing events. Can be either an HTTPS
    endpoint or a Lambda function ARN.

    - **BotId** *(string) --*

      The bot ID.

    - **OutboundEventsHTTPSEndpoint** *(string) --*

      HTTPS endpoint that allows a bot to receive outgoing events.

    - **LambdaFunctionArn** *(string) --*

      Lambda function ARN that allows a bot to receive outgoing events.
    """


_ClientPutEventsConfigurationResponseTypeDef = TypedDict(
    "_ClientPutEventsConfigurationResponseTypeDef",
    {
        "EventsConfiguration": ClientPutEventsConfigurationResponseEventsConfigurationTypeDef
    },
    total=False,
)


class ClientPutEventsConfigurationResponseTypeDef(
    _ClientPutEventsConfigurationResponseTypeDef
):
    """
    Type definition for `ClientPutEventsConfiguration` `Response`

    - **EventsConfiguration** *(dict) --*

      The configuration that allows a bot to receive outgoing events. Can be either an HTTPS
      endpoint or a Lambda function ARN.

      - **BotId** *(string) --*

        The bot ID.

      - **OutboundEventsHTTPSEndpoint** *(string) --*

        HTTPS endpoint that allows a bot to receive outgoing events.

      - **LambdaFunctionArn** *(string) --*

        Lambda function ARN that allows a bot to receive outgoing events.
    """


_ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef",
    {"EnableSIPLogs": bool},
    total=False,
)


class ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef(
    _ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorLoggingConfiguration` `LoggingConfiguration`

    The logging configuration details to add.

    - **EnableSIPLogs** *(boolean) --*

      When true, enables SIP message logs for sending to Amazon CloudWatch Logs.
    """


_ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {"EnableSIPLogs": bool},
    total=False,
)


class ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef(
    _ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorLoggingConfigurationResponse` `LoggingConfiguration`

    The updated logging configuration details.

    - **EnableSIPLogs** *(boolean) --*

      When true, enables SIP message logs for sending to Amazon CloudWatch Logs.
    """


_ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "_ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef
    },
    total=False,
)


class ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef(
    _ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorLoggingConfiguration` `Response`

    - **LoggingConfiguration** *(dict) --*

      The updated logging configuration details.

      - **EnableSIPLogs** *(boolean) --*

        When true, enables SIP message logs for sending to Amazon CloudWatch Logs.
    """


_ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef = TypedDict(
    "_ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef",
    {"Host": str, "Port": int, "Protocol": str, "Priority": int, "Weight": int},
    total=False,
)


class ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef(
    _ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorOriginationOrigination` `Routes`

    Origination routes define call distribution properties for your SIP hosts to receive inbound
    calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon
    Chime Voice Connector.

    - **Host** *(string) --*

      The FQDN or IP address to contact for origination traffic.

    - **Port** *(integer) --*

      The designated origination route port. Defaults to 5060.

    - **Protocol** *(string) --*

      The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
      Connectors use TCP protocol by default.

    - **Priority** *(integer) --*

      The priority associated with the host, with 1 being the highest priority. Higher priority
      hosts are attempted first.

    - **Weight** *(integer) --*

      The weight associated with the host. If hosts are equal in priority, calls are distributed
      among them based on their relative weight.
    """


_ClientPutVoiceConnectorOriginationOriginationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorOriginationOriginationTypeDef",
    {
        "Routes": List[ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef],
        "Disabled": bool,
    },
    total=False,
)


class ClientPutVoiceConnectorOriginationOriginationTypeDef(
    _ClientPutVoiceConnectorOriginationOriginationTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorOrigination` `Origination`

    The origination setting details to add.

    - **Routes** *(list) --*

      The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1.
      Maximum value of 20.

      - *(dict) --*

        Origination routes define call distribution properties for your SIP hosts to receive inbound
        calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon
        Chime Voice Connector.

        - **Host** *(string) --*

          The FQDN or IP address to contact for origination traffic.

        - **Port** *(integer) --*

          The designated origination route port. Defaults to 5060.

        - **Protocol** *(string) --*

          The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
          Connectors use TCP protocol by default.

        - **Priority** *(integer) --*

          The priority associated with the host, with 1 being the highest priority. Higher priority
          hosts are attempted first.

        - **Weight** *(integer) --*

          The weight associated with the host. If hosts are equal in priority, calls are distributed
          among them based on their relative weight.

    - **Disabled** *(boolean) --*

      When origination settings are disabled, inbound calls are not enabled for your Amazon Chime
      Voice Connector.
    """


_ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef = TypedDict(
    "_ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    {"Host": str, "Port": int, "Protocol": str, "Priority": int, "Weight": int},
    total=False,
)


class ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef(
    _ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorOriginationResponseOrigination` `Routes`

    Origination routes define call distribution properties for your SIP hosts to receive
    inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
    each Amazon Chime Voice Connector.

    - **Host** *(string) --*

      The FQDN or IP address to contact for origination traffic.

    - **Port** *(integer) --*

      The designated origination route port. Defaults to 5060.

    - **Protocol** *(string) --*

      The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
      Connectors use TCP protocol by default.

    - **Priority** *(integer) --*

      The priority associated with the host, with 1 being the highest priority. Higher
      priority hosts are attempted first.

    - **Weight** *(integer) --*

      The weight associated with the host. If hosts are equal in priority, calls are
      distributed among them based on their relative weight.
    """


_ClientPutVoiceConnectorOriginationResponseOriginationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorOriginationResponseOriginationTypeDef",
    {
        "Routes": List[
            ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef
        ],
        "Disabled": bool,
    },
    total=False,
)


class ClientPutVoiceConnectorOriginationResponseOriginationTypeDef(
    _ClientPutVoiceConnectorOriginationResponseOriginationTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorOriginationResponse` `Origination`

    The updated origination setting details.

    - **Routes** *(list) --*

      The call distribution properties defined for your SIP hosts. Valid range: Minimum value of
      1. Maximum value of 20.

      - *(dict) --*

        Origination routes define call distribution properties for your SIP hosts to receive
        inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
        each Amazon Chime Voice Connector.

        - **Host** *(string) --*

          The FQDN or IP address to contact for origination traffic.

        - **Port** *(integer) --*

          The designated origination route port. Defaults to 5060.

        - **Protocol** *(string) --*

          The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
          Connectors use TCP protocol by default.

        - **Priority** *(integer) --*

          The priority associated with the host, with 1 being the highest priority. Higher
          priority hosts are attempted first.

        - **Weight** *(integer) --*

          The weight associated with the host. If hosts are equal in priority, calls are
          distributed among them based on their relative weight.

    - **Disabled** *(boolean) --*

      When origination settings are disabled, inbound calls are not enabled for your Amazon Chime
      Voice Connector.
    """


_ClientPutVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "_ClientPutVoiceConnectorOriginationResponseTypeDef",
    {"Origination": ClientPutVoiceConnectorOriginationResponseOriginationTypeDef},
    total=False,
)


class ClientPutVoiceConnectorOriginationResponseTypeDef(
    _ClientPutVoiceConnectorOriginationResponseTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorOrigination` `Response`

    - **Origination** *(dict) --*

      The updated origination setting details.

      - **Routes** *(list) --*

        The call distribution properties defined for your SIP hosts. Valid range: Minimum value of
        1. Maximum value of 20.

        - *(dict) --*

          Origination routes define call distribution properties for your SIP hosts to receive
          inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
          each Amazon Chime Voice Connector.

          - **Host** *(string) --*

            The FQDN or IP address to contact for origination traffic.

          - **Port** *(integer) --*

            The designated origination route port. Defaults to 5060.

          - **Protocol** *(string) --*

            The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice
            Connectors use TCP protocol by default.

          - **Priority** *(integer) --*

            The priority associated with the host, with 1 being the highest priority. Higher
            priority hosts are attempted first.

          - **Weight** *(integer) --*

            The weight associated with the host. If hosts are equal in priority, calls are
            distributed among them based on their relative weight.

      - **Disabled** *(boolean) --*

        When origination settings are disabled, inbound calls are not enabled for your Amazon Chime
        Voice Connector.
    """


_ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    {"DataRetentionInHours": int, "Disabled": bool},
    total=False,
)


class ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef(
    _ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorStreamingConfigurationResponse` `StreamingConfiguration`

    The updated streaming configuration details.

    - **DataRetentionInHours** *(integer) --*

      The retention period, in hours, for the Amazon Kinesis data.

    - **Disabled** *(boolean) --*

      When true, media streaming to Amazon Kinesis is turned off.
    """


_ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "_ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef
    },
    total=False,
)


class ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef(
    _ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorStreamingConfiguration` `Response`

    - **StreamingConfiguration** *(dict) --*

      The updated streaming configuration details.

      - **DataRetentionInHours** *(integer) --*

        The retention period, in hours, for the Amazon Kinesis data.

      - **Disabled** *(boolean) --*

        When true, media streaming to Amazon Kinesis is turned off.
    """


_RequiredClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef = TypedDict(
    "_RequiredClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef",
    {"DataRetentionInHours": int},
)
_OptionalClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef = TypedDict(
    "_OptionalClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef",
    {"Disabled": bool},
    total=False,
)


class ClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef(
    _RequiredClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef,
    _OptionalClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef,
):
    """
    Type definition for `ClientPutVoiceConnectorStreamingConfiguration` `StreamingConfiguration`

    The streaming configuration details to add.

    - **DataRetentionInHours** *(integer) --* **[REQUIRED]**

      The retention period, in hours, for the Amazon Kinesis data.

    - **Disabled** *(boolean) --*

      When true, media streaming to Amazon Kinesis is turned off.
    """


_ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef = TypedDict(
    "_ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef",
    {"Username": str, "Password": str},
    total=False,
)


class ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef(
    _ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorTerminationCredentials` `Credentials`

    The SIP credentials used to authenticate requests to your Amazon Chime Voice Connector.

    - **Username** *(string) --*

      The RFC2617 compliant user name associated with the SIP credentials, in US-ASCII format.

    - **Password** *(string) --*

      The RFC2617 compliant password associated with the SIP credentials, in US-ASCII format.
    """


_ClientPutVoiceConnectorTerminationResponseTerminationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorTerminationResponseTerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)


class ClientPutVoiceConnectorTerminationResponseTerminationTypeDef(
    _ClientPutVoiceConnectorTerminationResponseTerminationTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorTerminationResponse` `Termination`

    The updated termination setting details.

    - **CpsLimit** *(integer) --*

      The limit on calls per second. Max value based on account service limit. Default value of 1.

    - **DefaultPhoneNumber** *(string) --*

      The default caller ID phone number.

    - **CallingRegions** *(list) --*

      The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.

      - *(string) --*

    - **CidrAllowedList** *(list) --*

      The IP addresses allowed to make calls, in CIDR format. Required.

      - *(string) --*

    - **Disabled** *(boolean) --*

      When termination settings are disabled, outbound calls can not be made.
    """


_ClientPutVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "_ClientPutVoiceConnectorTerminationResponseTypeDef",
    {"Termination": ClientPutVoiceConnectorTerminationResponseTerminationTypeDef},
    total=False,
)


class ClientPutVoiceConnectorTerminationResponseTypeDef(
    _ClientPutVoiceConnectorTerminationResponseTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorTermination` `Response`

    - **Termination** *(dict) --*

      The updated termination setting details.

      - **CpsLimit** *(integer) --*

        The limit on calls per second. Max value based on account service limit. Default value of 1.

      - **DefaultPhoneNumber** *(string) --*

        The default caller ID phone number.

      - **CallingRegions** *(list) --*

        The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.

        - *(string) --*

      - **CidrAllowedList** *(list) --*

        The IP addresses allowed to make calls, in CIDR format. Required.

        - *(string) --*

      - **Disabled** *(boolean) --*

        When termination settings are disabled, outbound calls can not be made.
    """


_ClientPutVoiceConnectorTerminationTerminationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorTerminationTerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)


class ClientPutVoiceConnectorTerminationTerminationTypeDef(
    _ClientPutVoiceConnectorTerminationTerminationTypeDef
):
    """
    Type definition for `ClientPutVoiceConnectorTermination` `Termination`

    The termination setting details to add.

    - **CpsLimit** *(integer) --*

      The limit on calls per second. Max value based on account service limit. Default value of 1.

    - **DefaultPhoneNumber** *(string) --*

      The default caller ID phone number.

    - **CallingRegions** *(list) --*

      The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.

      - *(string) --*

    - **CidrAllowedList** *(list) --*

      The IP addresses allowed to make calls, in CIDR format. Required.

      - *(string) --*

    - **Disabled** *(boolean) --*

      When termination settings are disabled, outbound calls can not be made.
    """


_ClientRegenerateSecurityTokenResponseBotTypeDef = TypedDict(
    "_ClientRegenerateSecurityTokenResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)


class ClientRegenerateSecurityTokenResponseBotTypeDef(
    _ClientRegenerateSecurityTokenResponseBotTypeDef
):
    """
    Type definition for `ClientRegenerateSecurityTokenResponse` `Bot`

    A resource that allows Enterprise account administrators to configure an interface to receive
    events from Amazon Chime.

    - **BotId** *(string) --*

      The bot ID.

    - **UserId** *(string) --*

      The unique ID for the bot user.

    - **DisplayName** *(string) --*

      The bot display name.

    - **BotType** *(string) --*

      The bot type.

    - **Disabled** *(boolean) --*

      When true, the bot is stopped from running in your account.

    - **CreatedTimestamp** *(datetime) --*

      The bot creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated bot timestamp, in ISO 8601 format.

    - **BotEmail** *(string) --*

      The bot email address.

    - **SecurityToken** *(string) --*

      The security token used to authenticate Amazon Chime with the outgoing event endpoint.
    """


_ClientRegenerateSecurityTokenResponseTypeDef = TypedDict(
    "_ClientRegenerateSecurityTokenResponseTypeDef",
    {"Bot": ClientRegenerateSecurityTokenResponseBotTypeDef},
    total=False,
)


class ClientRegenerateSecurityTokenResponseTypeDef(
    _ClientRegenerateSecurityTokenResponseTypeDef
):
    """
    Type definition for `ClientRegenerateSecurityToken` `Response`

    - **Bot** *(dict) --*

      A resource that allows Enterprise account administrators to configure an interface to receive
      events from Amazon Chime.

      - **BotId** *(string) --*

        The bot ID.

      - **UserId** *(string) --*

        The unique ID for the bot user.

      - **DisplayName** *(string) --*

        The bot display name.

      - **BotType** *(string) --*

        The bot type.

      - **Disabled** *(boolean) --*

        When true, the bot is stopped from running in your account.

      - **CreatedTimestamp** *(datetime) --*

        The bot creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated bot timestamp, in ISO 8601 format.

      - **BotEmail** *(string) --*

        The bot email address.

      - **SecurityToken** *(string) --*

        The security token used to authenticate Amazon Chime with the outgoing event endpoint.
    """


_ClientResetPersonalPinResponseUserTypeDef = TypedDict(
    "_ClientResetPersonalPinResponseUserTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": str,
        "UserRegistrationStatus": str,
        "UserInvitationStatus": str,
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "PersonalPIN": str,
    },
    total=False,
)


class ClientResetPersonalPinResponseUserTypeDef(
    _ClientResetPersonalPinResponseUserTypeDef
):
    """
    Type definition for `ClientResetPersonalPinResponse` `User`

    The user details and new personal meeting PIN.

    - **UserId** *(string) --*

      The user ID.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **PrimaryEmail** *(string) --*

      The primary email address of the user.

    - **PrimaryProvisionedNumber** *(string) --*

      The primary phone number associated with the user.

    - **DisplayName** *(string) --*

      The display name of the user.

    - **LicenseType** *(string) --*

      The license type for the user.

    - **UserRegistrationStatus** *(string) --*

      The user registration status.

    - **UserInvitationStatus** *(string) --*

      The user invite status.

    - **RegisteredOn** *(datetime) --*

      Date and time when the user is registered, in ISO 8601 format.

    - **InvitedOn** *(datetime) --*

      Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

    - **PersonalPIN** *(string) --*

      The user's personal meeting PIN.
    """


_ClientResetPersonalPinResponseTypeDef = TypedDict(
    "_ClientResetPersonalPinResponseTypeDef",
    {"User": ClientResetPersonalPinResponseUserTypeDef},
    total=False,
)


class ClientResetPersonalPinResponseTypeDef(_ClientResetPersonalPinResponseTypeDef):
    """
    Type definition for `ClientResetPersonalPin` `Response`

    - **User** *(dict) --*

      The user details and new personal meeting PIN.

      - **UserId** *(string) --*

        The user ID.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

      - **PrimaryEmail** *(string) --*

        The primary email address of the user.

      - **PrimaryProvisionedNumber** *(string) --*

        The primary phone number associated with the user.

      - **DisplayName** *(string) --*

        The display name of the user.

      - **LicenseType** *(string) --*

        The license type for the user.

      - **UserRegistrationStatus** *(string) --*

        The user registration status.

      - **UserInvitationStatus** *(string) --*

        The user invite status.

      - **RegisteredOn** *(datetime) --*

        Date and time when the user is registered, in ISO 8601 format.

      - **InvitedOn** *(datetime) --*

        Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

      - **PersonalPIN** *(string) --*

        The user's personal meeting PIN.
    """


_ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef = TypedDict(
    "_ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    {"Value": str, "Name": str, "AssociatedTimestamp": datetime},
    total=False,
)


class ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef(
    _ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef
):
    """
    Type definition for `ClientRestorePhoneNumberResponsePhoneNumber` `Associations`

    The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
    Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

    - **Value** *(string) --*

      Contains the ID for the entity specified in Name.

    - **Name** *(string) --*

      Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
      Connector ID, or Amazon Chime Voice Connector group ID.

    - **AssociatedTimestamp** *(datetime) --*

      The timestamp of the phone number association, in ISO 8601 format.
    """


_ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef = TypedDict(
    "_ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)


class ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef(
    _ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef
):
    """
    Type definition for `ClientRestorePhoneNumberResponsePhoneNumber` `Capabilities`

    The phone number capabilities.

    - **InboundCall** *(boolean) --*

      Allows or denies inbound calling for the specified phone number.

    - **OutboundCall** *(boolean) --*

      Allows or denies outbound calling for the specified phone number.

    - **InboundSMS** *(boolean) --*

      Allows or denies inbound SMS messaging for the specified phone number.

    - **OutboundSMS** *(boolean) --*

      Allows or denies outbound SMS messaging for the specified phone number.

    - **InboundMMS** *(boolean) --*

      Allows or denies inbound MMS messaging for the specified phone number.

    - **OutboundMMS** *(boolean) --*

      Allows or denies outbound MMS messaging for the specified phone number.
    """


_ClientRestorePhoneNumberResponsePhoneNumberTypeDef = TypedDict(
    "_ClientRestorePhoneNumberResponsePhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": str,
        "ProductType": str,
        "Status": str,
        "Capabilities": ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef,
        "Associations": List[
            ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef
        ],
        "CallingName": str,
        "CallingNameStatus": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)


class ClientRestorePhoneNumberResponsePhoneNumberTypeDef(
    _ClientRestorePhoneNumberResponsePhoneNumberTypeDef
):
    """
    Type definition for `ClientRestorePhoneNumberResponse` `PhoneNumber`

    The phone number details.

    - **PhoneNumberId** *(string) --*

      The phone number ID.

    - **E164PhoneNumber** *(string) --*

      The phone number, in E.164 format.

    - **Type** *(string) --*

      The phone number type.

    - **ProductType** *(string) --*

      The phone number product type.

    - **Status** *(string) --*

      The phone number status.

    - **Capabilities** *(dict) --*

      The phone number capabilities.

      - **InboundCall** *(boolean) --*

        Allows or denies inbound calling for the specified phone number.

      - **OutboundCall** *(boolean) --*

        Allows or denies outbound calling for the specified phone number.

      - **InboundSMS** *(boolean) --*

        Allows or denies inbound SMS messaging for the specified phone number.

      - **OutboundSMS** *(boolean) --*

        Allows or denies outbound SMS messaging for the specified phone number.

      - **InboundMMS** *(boolean) --*

        Allows or denies inbound MMS messaging for the specified phone number.

      - **OutboundMMS** *(boolean) --*

        Allows or denies outbound MMS messaging for the specified phone number.

    - **Associations** *(list) --*

      The phone number associations.

      - *(dict) --*

        The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
        Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

        - **Value** *(string) --*

          Contains the ID for the entity specified in Name.

        - **Name** *(string) --*

          Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
          Connector ID, or Amazon Chime Voice Connector group ID.

        - **AssociatedTimestamp** *(datetime) --*

          The timestamp of the phone number association, in ISO 8601 format.

    - **CallingName** *(string) --*

      The outbound calling name associated with the phone number.

    - **CallingNameStatus** *(string) --*

      The outbound calling name status.

    - **CreatedTimestamp** *(datetime) --*

      The phone number creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated phone number timestamp, in ISO 8601 format.

    - **DeletionTimestamp** *(datetime) --*

      The deleted phone number timestamp, in ISO 8601 format.
    """


_ClientRestorePhoneNumberResponseTypeDef = TypedDict(
    "_ClientRestorePhoneNumberResponseTypeDef",
    {"PhoneNumber": ClientRestorePhoneNumberResponsePhoneNumberTypeDef},
    total=False,
)


class ClientRestorePhoneNumberResponseTypeDef(_ClientRestorePhoneNumberResponseTypeDef):
    """
    Type definition for `ClientRestorePhoneNumber` `Response`

    - **PhoneNumber** *(dict) --*

      The phone number details.

      - **PhoneNumberId** *(string) --*

        The phone number ID.

      - **E164PhoneNumber** *(string) --*

        The phone number, in E.164 format.

      - **Type** *(string) --*

        The phone number type.

      - **ProductType** *(string) --*

        The phone number product type.

      - **Status** *(string) --*

        The phone number status.

      - **Capabilities** *(dict) --*

        The phone number capabilities.

        - **InboundCall** *(boolean) --*

          Allows or denies inbound calling for the specified phone number.

        - **OutboundCall** *(boolean) --*

          Allows or denies outbound calling for the specified phone number.

        - **InboundSMS** *(boolean) --*

          Allows or denies inbound SMS messaging for the specified phone number.

        - **OutboundSMS** *(boolean) --*

          Allows or denies outbound SMS messaging for the specified phone number.

        - **InboundMMS** *(boolean) --*

          Allows or denies inbound MMS messaging for the specified phone number.

        - **OutboundMMS** *(boolean) --*

          Allows or denies outbound MMS messaging for the specified phone number.

      - **Associations** *(list) --*

        The phone number associations.

        - *(dict) --*

          The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
          Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

          - **Value** *(string) --*

            Contains the ID for the entity specified in Name.

          - **Name** *(string) --*

            Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
            Connector ID, or Amazon Chime Voice Connector group ID.

          - **AssociatedTimestamp** *(datetime) --*

            The timestamp of the phone number association, in ISO 8601 format.

      - **CallingName** *(string) --*

        The outbound calling name associated with the phone number.

      - **CallingNameStatus** *(string) --*

        The outbound calling name status.

      - **CreatedTimestamp** *(datetime) --*

        The phone number creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated phone number timestamp, in ISO 8601 format.

      - **DeletionTimestamp** *(datetime) --*

        The deleted phone number timestamp, in ISO 8601 format.
    """


_ClientSearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "_ClientSearchAvailablePhoneNumbersResponseTypeDef",
    {"E164PhoneNumbers": List[str]},
    total=False,
)


class ClientSearchAvailablePhoneNumbersResponseTypeDef(
    _ClientSearchAvailablePhoneNumbersResponseTypeDef
):
    """
    Type definition for `ClientSearchAvailablePhoneNumbers` `Response`

    - **E164PhoneNumbers** *(list) --*

      List of phone numbers, in E.164 format.

      - *(string) --*
    """


_ClientUpdateAccountResponseAccountTypeDef = TypedDict(
    "_ClientUpdateAccountResponseAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": str,
        "CreatedTimestamp": datetime,
        "DefaultLicense": str,
        "SupportedLicenses": List[str],
    },
    total=False,
)


class ClientUpdateAccountResponseAccountTypeDef(
    _ClientUpdateAccountResponseAccountTypeDef
):
    """
    Type definition for `ClientUpdateAccountResponse` `Account`

    The updated Amazon Chime account details.

    - **AwsAccountId** *(string) --*

      The AWS account ID.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **Name** *(string) --*

      The Amazon Chime account name.

    - **AccountType** *(string) --*

      The Amazon Chime account type. For more information about different account types, see
      `Managing Your Amazon Chime Accounts
      <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
      Chime Administration Guide* .

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime account creation timestamp, in ISO 8601 format.

    - **DefaultLicense** *(string) --*

      The default license for the Amazon Chime account.

    - **SupportedLicenses** *(list) --*

      Supported licenses for the Amazon Chime account.

      - *(string) --*
    """


_ClientUpdateAccountResponseTypeDef = TypedDict(
    "_ClientUpdateAccountResponseTypeDef",
    {"Account": ClientUpdateAccountResponseAccountTypeDef},
    total=False,
)


class ClientUpdateAccountResponseTypeDef(_ClientUpdateAccountResponseTypeDef):
    """
    Type definition for `ClientUpdateAccount` `Response`

    - **Account** *(dict) --*

      The updated Amazon Chime account details.

      - **AwsAccountId** *(string) --*

        The AWS account ID.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

      - **Name** *(string) --*

        The Amazon Chime account name.

      - **AccountType** *(string) --*

        The Amazon Chime account type. For more information about different account types, see
        `Managing Your Amazon Chime Accounts
        <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
        Chime Administration Guide* .

      - **CreatedTimestamp** *(datetime) --*

        The Amazon Chime account creation timestamp, in ISO 8601 format.

      - **DefaultLicense** *(string) --*

        The default license for the Amazon Chime account.

      - **SupportedLicenses** *(list) --*

        Supported licenses for the Amazon Chime account.

        - *(string) --*
    """


_ClientUpdateAccountSettingsAccountSettingsTypeDef = TypedDict(
    "_ClientUpdateAccountSettingsAccountSettingsTypeDef",
    {"DisableRemoteControl": bool, "EnableDialOut": bool},
    total=False,
)


class ClientUpdateAccountSettingsAccountSettingsTypeDef(
    _ClientUpdateAccountSettingsAccountSettingsTypeDef
):
    """
    Type definition for `ClientUpdateAccountSettings` `AccountSettings`

    The Amazon Chime account settings to update.

    - **DisableRemoteControl** *(boolean) --*

      Setting that stops or starts remote control of shared screens during meetings.

    - **EnableDialOut** *(boolean) --*

      Setting that allows meeting participants to choose the **Call me at a phone number** option.
      For more information, see `Join a Meeting without the Amazon Chime App
      <https://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html>`__ .
    """


_ClientUpdateBotResponseBotTypeDef = TypedDict(
    "_ClientUpdateBotResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)


class ClientUpdateBotResponseBotTypeDef(_ClientUpdateBotResponseBotTypeDef):
    """
    Type definition for `ClientUpdateBotResponse` `Bot`

    The updated bot details.

    - **BotId** *(string) --*

      The bot ID.

    - **UserId** *(string) --*

      The unique ID for the bot user.

    - **DisplayName** *(string) --*

      The bot display name.

    - **BotType** *(string) --*

      The bot type.

    - **Disabled** *(boolean) --*

      When true, the bot is stopped from running in your account.

    - **CreatedTimestamp** *(datetime) --*

      The bot creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated bot timestamp, in ISO 8601 format.

    - **BotEmail** *(string) --*

      The bot email address.

    - **SecurityToken** *(string) --*

      The security token used to authenticate Amazon Chime with the outgoing event endpoint.
    """


_ClientUpdateBotResponseTypeDef = TypedDict(
    "_ClientUpdateBotResponseTypeDef",
    {"Bot": ClientUpdateBotResponseBotTypeDef},
    total=False,
)


class ClientUpdateBotResponseTypeDef(_ClientUpdateBotResponseTypeDef):
    """
    Type definition for `ClientUpdateBot` `Response`

    - **Bot** *(dict) --*

      The updated bot details.

      - **BotId** *(string) --*

        The bot ID.

      - **UserId** *(string) --*

        The unique ID for the bot user.

      - **DisplayName** *(string) --*

        The bot display name.

      - **BotType** *(string) --*

        The bot type.

      - **Disabled** *(boolean) --*

        When true, the bot is stopped from running in your account.

      - **CreatedTimestamp** *(datetime) --*

        The bot creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated bot timestamp, in ISO 8601 format.

      - **BotEmail** *(string) --*

        The bot email address.

      - **SecurityToken** *(string) --*

        The security token used to authenticate Amazon Chime with the outgoing event endpoint.
    """


_ClientUpdateGlobalSettingsBusinessCallingTypeDef = TypedDict(
    "_ClientUpdateGlobalSettingsBusinessCallingTypeDef", {"CdrBucket": str}, total=False
)


class ClientUpdateGlobalSettingsBusinessCallingTypeDef(
    _ClientUpdateGlobalSettingsBusinessCallingTypeDef
):
    """
    Type definition for `ClientUpdateGlobalSettings` `BusinessCalling`

    The Amazon Chime Business Calling settings.

    - **CdrBucket** *(string) --*

      The Amazon S3 bucket designated for call detail record storage.
    """


_ClientUpdateGlobalSettingsVoiceConnectorTypeDef = TypedDict(
    "_ClientUpdateGlobalSettingsVoiceConnectorTypeDef", {"CdrBucket": str}, total=False
)


class ClientUpdateGlobalSettingsVoiceConnectorTypeDef(
    _ClientUpdateGlobalSettingsVoiceConnectorTypeDef
):
    """
    Type definition for `ClientUpdateGlobalSettings` `VoiceConnector`

    The Amazon Chime Voice Connector settings.

    - **CdrBucket** *(string) --*

      The Amazon S3 bucket designated for call detail record storage.
    """


_ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef = TypedDict(
    "_ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    {"Value": str, "Name": str, "AssociatedTimestamp": datetime},
    total=False,
)


class ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef(
    _ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef
):
    """
    Type definition for `ClientUpdatePhoneNumberResponsePhoneNumber` `Associations`

    The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
    Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

    - **Value** *(string) --*

      Contains the ID for the entity specified in Name.

    - **Name** *(string) --*

      Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
      Connector ID, or Amazon Chime Voice Connector group ID.

    - **AssociatedTimestamp** *(datetime) --*

      The timestamp of the phone number association, in ISO 8601 format.
    """


_ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef = TypedDict(
    "_ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)


class ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef(
    _ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef
):
    """
    Type definition for `ClientUpdatePhoneNumberResponsePhoneNumber` `Capabilities`

    The phone number capabilities.

    - **InboundCall** *(boolean) --*

      Allows or denies inbound calling for the specified phone number.

    - **OutboundCall** *(boolean) --*

      Allows or denies outbound calling for the specified phone number.

    - **InboundSMS** *(boolean) --*

      Allows or denies inbound SMS messaging for the specified phone number.

    - **OutboundSMS** *(boolean) --*

      Allows or denies outbound SMS messaging for the specified phone number.

    - **InboundMMS** *(boolean) --*

      Allows or denies inbound MMS messaging for the specified phone number.

    - **OutboundMMS** *(boolean) --*

      Allows or denies outbound MMS messaging for the specified phone number.
    """


_ClientUpdatePhoneNumberResponsePhoneNumberTypeDef = TypedDict(
    "_ClientUpdatePhoneNumberResponsePhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": str,
        "ProductType": str,
        "Status": str,
        "Capabilities": ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef,
        "Associations": List[
            ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef
        ],
        "CallingName": str,
        "CallingNameStatus": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)


class ClientUpdatePhoneNumberResponsePhoneNumberTypeDef(
    _ClientUpdatePhoneNumberResponsePhoneNumberTypeDef
):
    """
    Type definition for `ClientUpdatePhoneNumberResponse` `PhoneNumber`

    The updated phone number details.

    - **PhoneNumberId** *(string) --*

      The phone number ID.

    - **E164PhoneNumber** *(string) --*

      The phone number, in E.164 format.

    - **Type** *(string) --*

      The phone number type.

    - **ProductType** *(string) --*

      The phone number product type.

    - **Status** *(string) --*

      The phone number status.

    - **Capabilities** *(dict) --*

      The phone number capabilities.

      - **InboundCall** *(boolean) --*

        Allows or denies inbound calling for the specified phone number.

      - **OutboundCall** *(boolean) --*

        Allows or denies outbound calling for the specified phone number.

      - **InboundSMS** *(boolean) --*

        Allows or denies inbound SMS messaging for the specified phone number.

      - **OutboundSMS** *(boolean) --*

        Allows or denies outbound SMS messaging for the specified phone number.

      - **InboundMMS** *(boolean) --*

        Allows or denies inbound MMS messaging for the specified phone number.

      - **OutboundMMS** *(boolean) --*

        Allows or denies outbound MMS messaging for the specified phone number.

    - **Associations** *(list) --*

      The phone number associations.

      - *(dict) --*

        The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
        Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

        - **Value** *(string) --*

          Contains the ID for the entity specified in Name.

        - **Name** *(string) --*

          Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
          Connector ID, or Amazon Chime Voice Connector group ID.

        - **AssociatedTimestamp** *(datetime) --*

          The timestamp of the phone number association, in ISO 8601 format.

    - **CallingName** *(string) --*

      The outbound calling name associated with the phone number.

    - **CallingNameStatus** *(string) --*

      The outbound calling name status.

    - **CreatedTimestamp** *(datetime) --*

      The phone number creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated phone number timestamp, in ISO 8601 format.

    - **DeletionTimestamp** *(datetime) --*

      The deleted phone number timestamp, in ISO 8601 format.
    """


_ClientUpdatePhoneNumberResponseTypeDef = TypedDict(
    "_ClientUpdatePhoneNumberResponseTypeDef",
    {"PhoneNumber": ClientUpdatePhoneNumberResponsePhoneNumberTypeDef},
    total=False,
)


class ClientUpdatePhoneNumberResponseTypeDef(_ClientUpdatePhoneNumberResponseTypeDef):
    """
    Type definition for `ClientUpdatePhoneNumber` `Response`

    - **PhoneNumber** *(dict) --*

      The updated phone number details.

      - **PhoneNumberId** *(string) --*

        The phone number ID.

      - **E164PhoneNumber** *(string) --*

        The phone number, in E.164 format.

      - **Type** *(string) --*

        The phone number type.

      - **ProductType** *(string) --*

        The phone number product type.

      - **Status** *(string) --*

        The phone number status.

      - **Capabilities** *(dict) --*

        The phone number capabilities.

        - **InboundCall** *(boolean) --*

          Allows or denies inbound calling for the specified phone number.

        - **OutboundCall** *(boolean) --*

          Allows or denies outbound calling for the specified phone number.

        - **InboundSMS** *(boolean) --*

          Allows or denies inbound SMS messaging for the specified phone number.

        - **OutboundSMS** *(boolean) --*

          Allows or denies outbound SMS messaging for the specified phone number.

        - **InboundMMS** *(boolean) --*

          Allows or denies inbound MMS messaging for the specified phone number.

        - **OutboundMMS** *(boolean) --*

          Allows or denies outbound MMS messaging for the specified phone number.

      - **Associations** *(list) --*

        The phone number associations.

        - *(dict) --*

          The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID,
          Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

          - **Value** *(string) --*

            Contains the ID for the entity specified in Name.

          - **Name** *(string) --*

            Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice
            Connector ID, or Amazon Chime Voice Connector group ID.

          - **AssociatedTimestamp** *(datetime) --*

            The timestamp of the phone number association, in ISO 8601 format.

      - **CallingName** *(string) --*

        The outbound calling name associated with the phone number.

      - **CallingNameStatus** *(string) --*

        The outbound calling name status.

      - **CreatedTimestamp** *(datetime) --*

        The phone number creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated phone number timestamp, in ISO 8601 format.

      - **DeletionTimestamp** *(datetime) --*

        The deleted phone number timestamp, in ISO 8601 format.
    """


_ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef = TypedDict(
    "_ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": str,
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)


class ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef(
    _ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef
):
    """
    Type definition for `ClientUpdateRoomMembershipResponseRoomMembership` `Member`

    The member details, such as email address, name, member ID, and member type.

    - **MemberId** *(string) --*

      The member ID (user ID or bot ID).

    - **MemberType** *(string) --*

      The member type.

    - **Email** *(string) --*

      The member email address.

    - **FullName** *(string) --*

      The member name.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.
    """


_ClientUpdateRoomMembershipResponseRoomMembershipTypeDef = TypedDict(
    "_ClientUpdateRoomMembershipResponseRoomMembershipTypeDef",
    {
        "RoomId": str,
        "Member": ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef,
        "Role": str,
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientUpdateRoomMembershipResponseRoomMembershipTypeDef(
    _ClientUpdateRoomMembershipResponseRoomMembershipTypeDef
):
    """
    Type definition for `ClientUpdateRoomMembershipResponse` `RoomMembership`

    The room membership details.

    - **RoomId** *(string) --*

      The room ID.

    - **Member** *(dict) --*

      The member details, such as email address, name, member ID, and member type.

      - **MemberId** *(string) --*

        The member ID (user ID or bot ID).

      - **MemberType** *(string) --*

        The member type.

      - **Email** *(string) --*

        The member email address.

      - **FullName** *(string) --*

        The member name.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

    - **Role** *(string) --*

      The membership role.

    - **InvitedBy** *(string) --*

      The identifier of the user that invited the room member.

    - **UpdatedTimestamp** *(datetime) --*

      The room membership update timestamp, in ISO 8601 format.
    """


_ClientUpdateRoomMembershipResponseTypeDef = TypedDict(
    "_ClientUpdateRoomMembershipResponseTypeDef",
    {"RoomMembership": ClientUpdateRoomMembershipResponseRoomMembershipTypeDef},
    total=False,
)


class ClientUpdateRoomMembershipResponseTypeDef(
    _ClientUpdateRoomMembershipResponseTypeDef
):
    """
    Type definition for `ClientUpdateRoomMembership` `Response`

    - **RoomMembership** *(dict) --*

      The room membership details.

      - **RoomId** *(string) --*

        The room ID.

      - **Member** *(dict) --*

        The member details, such as email address, name, member ID, and member type.

        - **MemberId** *(string) --*

          The member ID (user ID or bot ID).

        - **MemberType** *(string) --*

          The member type.

        - **Email** *(string) --*

          The member email address.

        - **FullName** *(string) --*

          The member name.

        - **AccountId** *(string) --*

          The Amazon Chime account ID.

      - **Role** *(string) --*

        The membership role.

      - **InvitedBy** *(string) --*

        The identifier of the user that invited the room member.

      - **UpdatedTimestamp** *(datetime) --*

        The room membership update timestamp, in ISO 8601 format.
    """


_ClientUpdateRoomResponseRoomTypeDef = TypedDict(
    "_ClientUpdateRoomResponseRoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientUpdateRoomResponseRoomTypeDef(_ClientUpdateRoomResponseRoomTypeDef):
    """
    Type definition for `ClientUpdateRoomResponse` `Room`

    The room details.

    - **RoomId** *(string) --*

      The room ID.

    - **Name** *(string) --*

      The room name.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **CreatedBy** *(string) --*

      The identifier of the room creator.

    - **CreatedTimestamp** *(datetime) --*

      The room creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The room update timestamp, in ISO 8601 format.
    """


_ClientUpdateRoomResponseTypeDef = TypedDict(
    "_ClientUpdateRoomResponseTypeDef",
    {"Room": ClientUpdateRoomResponseRoomTypeDef},
    total=False,
)


class ClientUpdateRoomResponseTypeDef(_ClientUpdateRoomResponseTypeDef):
    """
    Type definition for `ClientUpdateRoom` `Response`

    - **Room** *(dict) --*

      The room details.

      - **RoomId** *(string) --*

        The room ID.

      - **Name** *(string) --*

        The room name.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

      - **CreatedBy** *(string) --*

        The identifier of the room creator.

      - **CreatedTimestamp** *(datetime) --*

        The room creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The room update timestamp, in ISO 8601 format.
    """


_ClientUpdateUserResponseUserTypeDef = TypedDict(
    "_ClientUpdateUserResponseUserTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": str,
        "UserRegistrationStatus": str,
        "UserInvitationStatus": str,
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "PersonalPIN": str,
    },
    total=False,
)


class ClientUpdateUserResponseUserTypeDef(_ClientUpdateUserResponseUserTypeDef):
    """
    Type definition for `ClientUpdateUserResponse` `User`

    The updated user details.

    - **UserId** *(string) --*

      The user ID.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **PrimaryEmail** *(string) --*

      The primary email address of the user.

    - **PrimaryProvisionedNumber** *(string) --*

      The primary phone number associated with the user.

    - **DisplayName** *(string) --*

      The display name of the user.

    - **LicenseType** *(string) --*

      The license type for the user.

    - **UserRegistrationStatus** *(string) --*

      The user registration status.

    - **UserInvitationStatus** *(string) --*

      The user invite status.

    - **RegisteredOn** *(datetime) --*

      Date and time when the user is registered, in ISO 8601 format.

    - **InvitedOn** *(datetime) --*

      Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

    - **PersonalPIN** *(string) --*

      The user's personal meeting PIN.
    """


_ClientUpdateUserResponseTypeDef = TypedDict(
    "_ClientUpdateUserResponseTypeDef",
    {"User": ClientUpdateUserResponseUserTypeDef},
    total=False,
)


class ClientUpdateUserResponseTypeDef(_ClientUpdateUserResponseTypeDef):
    """
    Type definition for `ClientUpdateUser` `Response`

    - **User** *(dict) --*

      The updated user details.

      - **UserId** *(string) --*

        The user ID.

      - **AccountId** *(string) --*

        The Amazon Chime account ID.

      - **PrimaryEmail** *(string) --*

        The primary email address of the user.

      - **PrimaryProvisionedNumber** *(string) --*

        The primary phone number associated with the user.

      - **DisplayName** *(string) --*

        The display name of the user.

      - **LicenseType** *(string) --*

        The license type for the user.

      - **UserRegistrationStatus** *(string) --*

        The user registration status.

      - **UserInvitationStatus** *(string) --*

        The user invite status.

      - **RegisteredOn** *(datetime) --*

        Date and time when the user is registered, in ISO 8601 format.

      - **InvitedOn** *(datetime) --*

        Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

      - **PersonalPIN** *(string) --*

        The user's personal meeting PIN.
    """


_ClientUpdateUserSettingsUserSettingsTelephonyTypeDef = TypedDict(
    "_ClientUpdateUserSettingsUserSettingsTelephonyTypeDef",
    {"InboundCalling": bool, "OutboundCalling": bool, "SMS": bool},
)


class ClientUpdateUserSettingsUserSettingsTelephonyTypeDef(
    _ClientUpdateUserSettingsUserSettingsTelephonyTypeDef
):
    """
    Type definition for `ClientUpdateUserSettingsUserSettings` `Telephony`

    The telephony settings associated with the user.

    - **InboundCalling** *(boolean) --* **[REQUIRED]**

      Allows or denies inbound calling.

    - **OutboundCalling** *(boolean) --* **[REQUIRED]**

      Allows or denies outbound calling.

    - **SMS** *(boolean) --* **[REQUIRED]**

      Allows or denies SMS messaging.
    """


_ClientUpdateUserSettingsUserSettingsTypeDef = TypedDict(
    "_ClientUpdateUserSettingsUserSettingsTypeDef",
    {"Telephony": ClientUpdateUserSettingsUserSettingsTelephonyTypeDef},
)


class ClientUpdateUserSettingsUserSettingsTypeDef(
    _ClientUpdateUserSettingsUserSettingsTypeDef
):
    """
    Type definition for `ClientUpdateUserSettings` `UserSettings`

    The user settings to update.

    - **Telephony** *(dict) --* **[REQUIRED]**

      The telephony settings associated with the user.

      - **InboundCalling** *(boolean) --* **[REQUIRED]**

        Allows or denies inbound calling.

      - **OutboundCalling** *(boolean) --* **[REQUIRED]**

        Allows or denies outbound calling.

      - **SMS** *(boolean) --* **[REQUIRED]**

        Allows or denies SMS messaging.
    """


_ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)


class ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
):
    """
    Type definition for `ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroup` `VoiceConnectorItems`

    For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
    route inbound calls. Includes priority configuration settings. Limit: 3
    ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

    - **VoiceConnectorId** *(string) --*

      The Amazon Chime Voice Connector ID.

    - **Priority** *(integer) --*

      The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
      priority. Higher priority Amazon Chime Voice Connectors are attempted first.
    """


_ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef(
    _ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef
):
    """
    Type definition for `ClientUpdateVoiceConnectorGroupResponse` `VoiceConnectorGroup`

    The updated Amazon Chime Voice Connector group details.

    - **VoiceConnectorGroupId** *(string) --*

      The Amazon Chime Voice Connector group ID.

    - **Name** *(string) --*

      The name of the Amazon Chime Voice Connector group.

    - **VoiceConnectorItems** *(list) --*

      The Amazon Chime Voice Connectors to which to route inbound calls.

      - *(dict) --*

        For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
        route inbound calls. Includes priority configuration settings. Limit: 3
        ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

        - **VoiceConnectorId** *(string) --*

          The Amazon Chime Voice Connector ID.

        - **Priority** *(integer) --*

          The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
          priority. Higher priority Amazon Chime Voice Connectors are attempted first.

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.
    """


_ClientUpdateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef
    },
    total=False,
)


class ClientUpdateVoiceConnectorGroupResponseTypeDef(
    _ClientUpdateVoiceConnectorGroupResponseTypeDef
):
    """
    Type definition for `ClientUpdateVoiceConnectorGroup` `Response`

    - **VoiceConnectorGroup** *(dict) --*

      The updated Amazon Chime Voice Connector group details.

      - **VoiceConnectorGroupId** *(string) --*

        The Amazon Chime Voice Connector group ID.

      - **Name** *(string) --*

        The name of the Amazon Chime Voice Connector group.

      - **VoiceConnectorItems** *(list) --*

        The Amazon Chime Voice Connectors to which to route inbound calls.

        - *(dict) --*

          For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to
          route inbound calls. Includes priority configuration settings. Limit: 3
          ``VoiceConnectorItems`` per Amazon Chime Voice Connector group.

          - **VoiceConnectorId** *(string) --*

            The Amazon Chime Voice Connector ID.

          - **Priority** *(integer) --*

            The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
            priority. Higher priority Amazon Chime Voice Connectors are attempted first.

      - **CreatedTimestamp** *(datetime) --*

        The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.
    """


_ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
)


class ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef
):
    """
    Type definition for `ClientUpdateVoiceConnectorGroup` `VoiceConnectorItems`

    For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route
    inbound calls. Includes priority configuration settings. Limit: 3 ``VoiceConnectorItems`` per
    Amazon Chime Voice Connector group.

    - **VoiceConnectorId** *(string) --* **[REQUIRED]**

      The Amazon Chime Voice Connector ID.

    - **Priority** *(integer) --* **[REQUIRED]**

      The priority associated with the Amazon Chime Voice Connector, with 1 being the highest
      priority. Higher priority Amazon Chime Voice Connectors are attempted first.
    """


_ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": str,
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef(
    _ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef
):
    """
    Type definition for `ClientUpdateVoiceConnectorResponse` `VoiceConnector`

    The updated Amazon Chime Voice Connector details.

    - **VoiceConnectorId** *(string) --*

      The Amazon Chime Voice Connector ID.

    - **AwsRegion** *(string) --*

      The AWS Region in which the Amazon Chime Voice Connector is created. Default: ``us-east-1``
      .

    - **Name** *(string) --*

      The name of the Amazon Chime Voice Connector.

    - **OutboundHostName** *(string) --*

      The outbound host name for the Amazon Chime Voice Connector.

    - **RequireEncryption** *(boolean) --*

      Designates whether encryption is required for the Amazon Chime Voice Connector.

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

    - **UpdatedTimestamp** *(datetime) --*

      The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
    """


_ClientUpdateVoiceConnectorResponseTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorResponseTypeDef",
    {"VoiceConnector": ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef},
    total=False,
)


class ClientUpdateVoiceConnectorResponseTypeDef(
    _ClientUpdateVoiceConnectorResponseTypeDef
):
    """
    Type definition for `ClientUpdateVoiceConnector` `Response`

    - **VoiceConnector** *(dict) --*

      The updated Amazon Chime Voice Connector details.

      - **VoiceConnectorId** *(string) --*

        The Amazon Chime Voice Connector ID.

      - **AwsRegion** *(string) --*

        The AWS Region in which the Amazon Chime Voice Connector is created. Default: ``us-east-1``
        .

      - **Name** *(string) --*

        The name of the Amazon Chime Voice Connector.

      - **OutboundHostName** *(string) --*

        The outbound host name for the Amazon Chime Voice Connector.

      - **RequireEncryption** *(boolean) --*

        Designates whether encryption is required for the Amazon Chime Voice Connector.

      - **CreatedTimestamp** *(datetime) --*

        The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

      - **UpdatedTimestamp** *(datetime) --*

        The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
    """


_ListAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccountsPaginatePaginationConfigTypeDef(
    _ListAccountsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAccountsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListAccountsPaginateResponseAccountsTypeDef = TypedDict(
    "_ListAccountsPaginateResponseAccountsTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": str,
        "CreatedTimestamp": datetime,
        "DefaultLicense": str,
        "SupportedLicenses": List[str],
    },
    total=False,
)


class ListAccountsPaginateResponseAccountsTypeDef(
    _ListAccountsPaginateResponseAccountsTypeDef
):
    """
    Type definition for `ListAccountsPaginateResponse` `Accounts`

    The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.

    - **AwsAccountId** *(string) --*

      The AWS account ID.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **Name** *(string) --*

      The Amazon Chime account name.

    - **AccountType** *(string) --*

      The Amazon Chime account type. For more information about different account types, see
      `Managing Your Amazon Chime Accounts
      <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
      Chime Administration Guide* .

    - **CreatedTimestamp** *(datetime) --*

      The Amazon Chime account creation timestamp, in ISO 8601 format.

    - **DefaultLicense** *(string) --*

      The default license for the Amazon Chime account.

    - **SupportedLicenses** *(list) --*

      Supported licenses for the Amazon Chime account.

      - *(string) --*
    """


_ListAccountsPaginateResponseTypeDef = TypedDict(
    "_ListAccountsPaginateResponseTypeDef",
    {"Accounts": List[ListAccountsPaginateResponseAccountsTypeDef]},
    total=False,
)


class ListAccountsPaginateResponseTypeDef(_ListAccountsPaginateResponseTypeDef):
    """
    Type definition for `ListAccountsPaginate` `Response`

    - **Accounts** *(list) --*

      List of Amazon Chime accounts and account details.

      - *(dict) --*

        The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.

        - **AwsAccountId** *(string) --*

          The AWS account ID.

        - **AccountId** *(string) --*

          The Amazon Chime account ID.

        - **Name** *(string) --*

          The Amazon Chime account name.

        - **AccountType** *(string) --*

          The Amazon Chime account type. For more information about different account types, see
          `Managing Your Amazon Chime Accounts
          <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon
          Chime Administration Guide* .

        - **CreatedTimestamp** *(datetime) --*

          The Amazon Chime account creation timestamp, in ISO 8601 format.

        - **DefaultLicense** *(string) --*

          The default license for the Amazon Chime account.

        - **SupportedLicenses** *(list) --*

          Supported licenses for the Amazon Chime account.

          - *(string) --*
    """


_ListUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsersPaginatePaginationConfigTypeDef(
    _ListUsersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUsersPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListUsersPaginateResponseUsersTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": str,
        "UserRegistrationStatus": str,
        "UserInvitationStatus": str,
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "PersonalPIN": str,
    },
    total=False,
)


class ListUsersPaginateResponseUsersTypeDef(_ListUsersPaginateResponseUsersTypeDef):
    """
    Type definition for `ListUsersPaginateResponse` `Users`

    The user on the Amazon Chime account.

    - **UserId** *(string) --*

      The user ID.

    - **AccountId** *(string) --*

      The Amazon Chime account ID.

    - **PrimaryEmail** *(string) --*

      The primary email address of the user.

    - **PrimaryProvisionedNumber** *(string) --*

      The primary phone number associated with the user.

    - **DisplayName** *(string) --*

      The display name of the user.

    - **LicenseType** *(string) --*

      The license type for the user.

    - **UserRegistrationStatus** *(string) --*

      The user registration status.

    - **UserInvitationStatus** *(string) --*

      The user invite status.

    - **RegisteredOn** *(datetime) --*

      Date and time when the user is registered, in ISO 8601 format.

    - **InvitedOn** *(datetime) --*

      Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

    - **PersonalPIN** *(string) --*

      The user's personal meeting PIN.
    """


_ListUsersPaginateResponseTypeDef = TypedDict(
    "_ListUsersPaginateResponseTypeDef",
    {"Users": List[ListUsersPaginateResponseUsersTypeDef]},
    total=False,
)


class ListUsersPaginateResponseTypeDef(_ListUsersPaginateResponseTypeDef):
    """
    Type definition for `ListUsersPaginate` `Response`

    - **Users** *(list) --*

      List of users and user details.

      - *(dict) --*

        The user on the Amazon Chime account.

        - **UserId** *(string) --*

          The user ID.

        - **AccountId** *(string) --*

          The Amazon Chime account ID.

        - **PrimaryEmail** *(string) --*

          The primary email address of the user.

        - **PrimaryProvisionedNumber** *(string) --*

          The primary phone number associated with the user.

        - **DisplayName** *(string) --*

          The display name of the user.

        - **LicenseType** *(string) --*

          The license type for the user.

        - **UserRegistrationStatus** *(string) --*

          The user registration status.

        - **UserInvitationStatus** *(string) --*

          The user invite status.

        - **RegisteredOn** *(datetime) --*

          Date and time when the user is registered, in ISO 8601 format.

        - **InvitedOn** *(datetime) --*

          Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

        - **PersonalPIN** *(string) --*

          The user's personal meeting PIN.
    """
