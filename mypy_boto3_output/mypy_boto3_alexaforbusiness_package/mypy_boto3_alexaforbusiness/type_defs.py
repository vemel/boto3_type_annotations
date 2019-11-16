"Main interface for alexaforbusiness type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAddressBookResponseTypeDef",
    "ClientCreateBusinessReportScheduleContentRangeTypeDef",
    "ClientCreateBusinessReportScheduleRecurrenceTypeDef",
    "ClientCreateBusinessReportScheduleResponseTypeDef",
    "ClientCreateConferenceProviderIPDialInTypeDef",
    "ClientCreateConferenceProviderMeetingSettingTypeDef",
    "ClientCreateConferenceProviderPSTNDialInTypeDef",
    "ClientCreateConferenceProviderResponseTypeDef",
    "ClientCreateContactPhoneNumbersTypeDef",
    "ClientCreateContactResponseTypeDef",
    "ClientCreateContactSipAddressesTypeDef",
    "ClientCreateGatewayGroupResponseTypeDef",
    "ClientCreateNetworkProfileResponseTypeDef",
    "ClientCreateProfileResponseTypeDef",
    "ClientCreateRoomResponseTypeDef",
    "ClientCreateRoomTagsTypeDef",
    "ClientCreateSkillGroupResponseTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserTagsTypeDef",
    "ClientGetAddressBookResponseAddressBookTypeDef",
    "ClientGetAddressBookResponseTypeDef",
    "ClientGetConferencePreferenceResponsePreferenceTypeDef",
    "ClientGetConferencePreferenceResponseTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderTypeDef",
    "ClientGetConferenceProviderResponseTypeDef",
    "ClientGetContactResponseContactPhoneNumbersTypeDef",
    "ClientGetContactResponseContactSipAddressesTypeDef",
    "ClientGetContactResponseContactTypeDef",
    "ClientGetContactResponseTypeDef",
    "ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef",
    "ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef",
    "ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef",
    "ClientGetDeviceResponseDeviceTypeDef",
    "ClientGetDeviceResponseTypeDef",
    "ClientGetGatewayGroupResponseGatewayGroupTypeDef",
    "ClientGetGatewayGroupResponseTypeDef",
    "ClientGetGatewayResponseGatewayTypeDef",
    "ClientGetGatewayResponseTypeDef",
    "ClientGetInvitationConfigurationResponseTypeDef",
    "ClientGetNetworkProfileResponseNetworkProfileTypeDef",
    "ClientGetNetworkProfileResponseTypeDef",
    "ClientGetProfileResponseProfileTypeDef",
    "ClientGetProfileResponseTypeDef",
    "ClientGetRoomResponseRoomTypeDef",
    "ClientGetRoomResponseTypeDef",
    "ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef",
    "ClientGetRoomSkillParameterResponseTypeDef",
    "ClientGetSkillGroupResponseSkillGroupTypeDef",
    "ClientGetSkillGroupResponseTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef",
    "ClientListBusinessReportSchedulesResponseTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersTypeDef",
    "ClientListConferenceProvidersResponseTypeDef",
    "ClientListDeviceEventsResponseDeviceEventsTypeDef",
    "ClientListDeviceEventsResponseTypeDef",
    "ClientListGatewayGroupsResponseGatewayGroupsTypeDef",
    "ClientListGatewayGroupsResponseTypeDef",
    "ClientListGatewaysResponseGatewaysTypeDef",
    "ClientListGatewaysResponseTypeDef",
    "ClientListSkillsResponseSkillSummariesTypeDef",
    "ClientListSkillsResponseTypeDef",
    "ClientListSkillsStoreCategoriesResponseCategoryListTypeDef",
    "ClientListSkillsStoreCategoriesResponseTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseTypeDef",
    "ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef",
    "ClientListSmartHomeAppliancesResponseTypeDef",
    "ClientListTagsResponseTagsTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientPutConferencePreferenceConferencePreferenceTypeDef",
    "ClientPutRoomSkillParameterRoomSkillParameterTypeDef",
    "ClientRegisterAvsDeviceResponseTypeDef",
    "ClientResolveRoomResponseRoomSkillParametersTypeDef",
    "ClientResolveRoomResponseTypeDef",
    "ClientSearchAddressBooksFiltersTypeDef",
    "ClientSearchAddressBooksResponseAddressBooksTypeDef",
    "ClientSearchAddressBooksResponseTypeDef",
    "ClientSearchAddressBooksSortCriteriaTypeDef",
    "ClientSearchContactsFiltersTypeDef",
    "ClientSearchContactsResponseContactsPhoneNumbersTypeDef",
    "ClientSearchContactsResponseContactsSipAddressesTypeDef",
    "ClientSearchContactsResponseContactsTypeDef",
    "ClientSearchContactsResponseTypeDef",
    "ClientSearchContactsSortCriteriaTypeDef",
    "ClientSearchDevicesFiltersTypeDef",
    "ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef",
    "ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef",
    "ClientSearchDevicesResponseDevicesTypeDef",
    "ClientSearchDevicesResponseTypeDef",
    "ClientSearchDevicesSortCriteriaTypeDef",
    "ClientSearchNetworkProfilesFiltersTypeDef",
    "ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef",
    "ClientSearchNetworkProfilesResponseTypeDef",
    "ClientSearchNetworkProfilesSortCriteriaTypeDef",
    "ClientSearchProfilesFiltersTypeDef",
    "ClientSearchProfilesResponseProfilesTypeDef",
    "ClientSearchProfilesResponseTypeDef",
    "ClientSearchProfilesSortCriteriaTypeDef",
    "ClientSearchRoomsFiltersTypeDef",
    "ClientSearchRoomsResponseRoomsTypeDef",
    "ClientSearchRoomsResponseTypeDef",
    "ClientSearchRoomsSortCriteriaTypeDef",
    "ClientSearchSkillGroupsFiltersTypeDef",
    "ClientSearchSkillGroupsResponseSkillGroupsTypeDef",
    "ClientSearchSkillGroupsResponseTypeDef",
    "ClientSearchSkillGroupsSortCriteriaTypeDef",
    "ClientSearchUsersFiltersTypeDef",
    "ClientSearchUsersResponseUsersTypeDef",
    "ClientSearchUsersResponseTypeDef",
    "ClientSearchUsersSortCriteriaTypeDef",
    "ClientSendAnnouncementContentAudioListTypeDef",
    "ClientSendAnnouncementContentSsmlListTypeDef",
    "ClientSendAnnouncementContentTextListTypeDef",
    "ClientSendAnnouncementContentTypeDef",
    "ClientSendAnnouncementResponseTypeDef",
    "ClientSendAnnouncementRoomFiltersTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateBusinessReportScheduleRecurrenceTypeDef",
    "ClientUpdateConferenceProviderIPDialInTypeDef",
    "ClientUpdateConferenceProviderMeetingSettingTypeDef",
    "ClientUpdateConferenceProviderPSTNDialInTypeDef",
    "ClientUpdateContactPhoneNumbersTypeDef",
    "ClientUpdateContactSipAddressesTypeDef",
    "ListBusinessReportSchedulesPaginatePaginationConfigTypeDef",
    "ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef",
    "ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef",
    "ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef",
    "ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef",
    "ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef",
    "ListBusinessReportSchedulesPaginateResponseTypeDef",
    "ListConferenceProvidersPaginatePaginationConfigTypeDef",
    "ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef",
    "ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef",
    "ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef",
    "ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef",
    "ListConferenceProvidersPaginateResponseTypeDef",
    "ListDeviceEventsPaginatePaginationConfigTypeDef",
    "ListDeviceEventsPaginateResponseDeviceEventsTypeDef",
    "ListDeviceEventsPaginateResponseTypeDef",
    "ListSkillsPaginatePaginationConfigTypeDef",
    "ListSkillsPaginateResponseSkillSummariesTypeDef",
    "ListSkillsPaginateResponseTypeDef",
    "ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef",
    "ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef",
    "ListSkillsStoreCategoriesPaginateResponseTypeDef",
    "ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef",
    "ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef",
    "ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef",
    "ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef",
    "ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef",
    "ListSmartHomeAppliancesPaginatePaginationConfigTypeDef",
    "ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef",
    "ListSmartHomeAppliancesPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseTagsTypeDef",
    "ListTagsPaginateResponseTypeDef",
    "SearchDevicesPaginateFiltersTypeDef",
    "SearchDevicesPaginatePaginationConfigTypeDef",
    "SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef",
    "SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef",
    "SearchDevicesPaginateResponseDevicesTypeDef",
    "SearchDevicesPaginateResponseTypeDef",
    "SearchDevicesPaginateSortCriteriaTypeDef",
    "SearchProfilesPaginateFiltersTypeDef",
    "SearchProfilesPaginatePaginationConfigTypeDef",
    "SearchProfilesPaginateResponseProfilesTypeDef",
    "SearchProfilesPaginateResponseTypeDef",
    "SearchProfilesPaginateSortCriteriaTypeDef",
    "SearchRoomsPaginateFiltersTypeDef",
    "SearchRoomsPaginatePaginationConfigTypeDef",
    "SearchRoomsPaginateResponseRoomsTypeDef",
    "SearchRoomsPaginateResponseTypeDef",
    "SearchRoomsPaginateSortCriteriaTypeDef",
    "SearchSkillGroupsPaginateFiltersTypeDef",
    "SearchSkillGroupsPaginatePaginationConfigTypeDef",
    "SearchSkillGroupsPaginateResponseSkillGroupsTypeDef",
    "SearchSkillGroupsPaginateResponseTypeDef",
    "SearchSkillGroupsPaginateSortCriteriaTypeDef",
    "SearchUsersPaginateFiltersTypeDef",
    "SearchUsersPaginatePaginationConfigTypeDef",
    "SearchUsersPaginateResponseUsersTypeDef",
    "SearchUsersPaginateResponseTypeDef",
    "SearchUsersPaginateSortCriteriaTypeDef",
)


_ClientCreateAddressBookResponseTypeDef = TypedDict(
    "_ClientCreateAddressBookResponseTypeDef", {"AddressBookArn": str}, total=False
)


class ClientCreateAddressBookResponseTypeDef(_ClientCreateAddressBookResponseTypeDef):
    """
    Type definition for `ClientCreateAddressBook` `Response`

    - **AddressBookArn** *(string) --*

      The ARN of the newly created address book.
    """


_ClientCreateBusinessReportScheduleContentRangeTypeDef = TypedDict(
    "_ClientCreateBusinessReportScheduleContentRangeTypeDef",
    {"Interval": str},
    total=False,
)


class ClientCreateBusinessReportScheduleContentRangeTypeDef(
    _ClientCreateBusinessReportScheduleContentRangeTypeDef
):
    """
    Type definition for `ClientCreateBusinessReportSchedule` `ContentRange`

    The content range of the reports.

    - **Interval** *(string) --*

      The interval of the content range.
    """


_ClientCreateBusinessReportScheduleRecurrenceTypeDef = TypedDict(
    "_ClientCreateBusinessReportScheduleRecurrenceTypeDef",
    {"StartDate": str},
    total=False,
)


class ClientCreateBusinessReportScheduleRecurrenceTypeDef(
    _ClientCreateBusinessReportScheduleRecurrenceTypeDef
):
    """
    Type definition for `ClientCreateBusinessReportSchedule` `Recurrence`

    The recurrence of the reports. If this isn't specified, the report will only be delivered one
    time when the API is called.

    - **StartDate** *(string) --*

      The start date.
    """


_ClientCreateBusinessReportScheduleResponseTypeDef = TypedDict(
    "_ClientCreateBusinessReportScheduleResponseTypeDef",
    {"ScheduleArn": str},
    total=False,
)


class ClientCreateBusinessReportScheduleResponseTypeDef(
    _ClientCreateBusinessReportScheduleResponseTypeDef
):
    """
    Type definition for `ClientCreateBusinessReportSchedule` `Response`

    - **ScheduleArn** *(string) --*

      The ARN of the business report schedule.
    """


_ClientCreateConferenceProviderIPDialInTypeDef = TypedDict(
    "_ClientCreateConferenceProviderIPDialInTypeDef",
    {"Endpoint": str, "CommsProtocol": str},
)


class ClientCreateConferenceProviderIPDialInTypeDef(
    _ClientCreateConferenceProviderIPDialInTypeDef
):
    """
    Type definition for `ClientCreateConferenceProvider` `IPDialIn`

    The IP endpoint and protocol for calling.

    - **Endpoint** *(string) --* **[REQUIRED]**

      The IP address.

    - **CommsProtocol** *(string) --* **[REQUIRED]**

      The protocol, including SIP, SIPS, and H323.
    """


_ClientCreateConferenceProviderMeetingSettingTypeDef = TypedDict(
    "_ClientCreateConferenceProviderMeetingSettingTypeDef", {"RequirePin": str}
)


class ClientCreateConferenceProviderMeetingSettingTypeDef(
    _ClientCreateConferenceProviderMeetingSettingTypeDef
):
    """
    Type definition for `ClientCreateConferenceProvider` `MeetingSetting`

    The meeting settings for the conference provider.

    - **RequirePin** *(string) --* **[REQUIRED]**

      The values that indicate whether the pin is always required.
    """


_ClientCreateConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_ClientCreateConferenceProviderPSTNDialInTypeDef",
    {
        "CountryCode": str,
        "PhoneNumber": str,
        "OneClickIdDelay": str,
        "OneClickPinDelay": str,
    },
)


class ClientCreateConferenceProviderPSTNDialInTypeDef(
    _ClientCreateConferenceProviderPSTNDialInTypeDef
):
    """
    Type definition for `ClientCreateConferenceProvider` `PSTNDialIn`

    The information for PSTN conferencing.

    - **CountryCode** *(string) --* **[REQUIRED]**

      The zip code.

    - **PhoneNumber** *(string) --* **[REQUIRED]**

      The phone number to call to join the conference.

    - **OneClickIdDelay** *(string) --* **[REQUIRED]**

      The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF).
      Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the
      telephone network.

    - **OneClickPinDelay** *(string) --* **[REQUIRED]**

      The delay duration before Alexa enters the conference pin with dual-tone multi-frequency
      (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over
      the telephone network.
    """


_ClientCreateConferenceProviderResponseTypeDef = TypedDict(
    "_ClientCreateConferenceProviderResponseTypeDef",
    {"ConferenceProviderArn": str},
    total=False,
)


class ClientCreateConferenceProviderResponseTypeDef(
    _ClientCreateConferenceProviderResponseTypeDef
):
    """
    Type definition for `ClientCreateConferenceProvider` `Response`

    - **ConferenceProviderArn** *(string) --*

      The ARN of the newly-created conference provider.
    """


_ClientCreateContactPhoneNumbersTypeDef = TypedDict(
    "_ClientCreateContactPhoneNumbersTypeDef", {"Number": str, "Type": str}
)


class ClientCreateContactPhoneNumbersTypeDef(_ClientCreateContactPhoneNumbersTypeDef):
    """
    Type definition for `ClientCreateContact` `PhoneNumbers`

    The phone number for the contact containing the raw number and phone number type.

    - **Number** *(string) --* **[REQUIRED]**

      The raw value of the phone number.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the phone number.
    """


_ClientCreateContactResponseTypeDef = TypedDict(
    "_ClientCreateContactResponseTypeDef", {"ContactArn": str}, total=False
)


class ClientCreateContactResponseTypeDef(_ClientCreateContactResponseTypeDef):
    """
    Type definition for `ClientCreateContact` `Response`

    - **ContactArn** *(string) --*

      The ARN of the newly created address book.
    """


_ClientCreateContactSipAddressesTypeDef = TypedDict(
    "_ClientCreateContactSipAddressesTypeDef", {"Uri": str, "Type": str}
)


class ClientCreateContactSipAddressesTypeDef(_ClientCreateContactSipAddressesTypeDef):
    """
    Type definition for `ClientCreateContact` `SipAddresses`

    The SIP address for the contact containing the URI and SIP address type.

    - **Uri** *(string) --* **[REQUIRED]**

      The URI for the SIP address.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the SIP address.
    """


_ClientCreateGatewayGroupResponseTypeDef = TypedDict(
    "_ClientCreateGatewayGroupResponseTypeDef", {"GatewayGroupArn": str}, total=False
)


class ClientCreateGatewayGroupResponseTypeDef(_ClientCreateGatewayGroupResponseTypeDef):
    """
    Type definition for `ClientCreateGatewayGroup` `Response`

    - **GatewayGroupArn** *(string) --*

      The ARN of the created gateway group.
    """


_ClientCreateNetworkProfileResponseTypeDef = TypedDict(
    "_ClientCreateNetworkProfileResponseTypeDef",
    {"NetworkProfileArn": str},
    total=False,
)


class ClientCreateNetworkProfileResponseTypeDef(
    _ClientCreateNetworkProfileResponseTypeDef
):
    """
    Type definition for `ClientCreateNetworkProfile` `Response`

    - **NetworkProfileArn** *(string) --*

      The ARN of the network profile associated with a device.
    """


_ClientCreateProfileResponseTypeDef = TypedDict(
    "_ClientCreateProfileResponseTypeDef", {"ProfileArn": str}, total=False
)


class ClientCreateProfileResponseTypeDef(_ClientCreateProfileResponseTypeDef):
    """
    Type definition for `ClientCreateProfile` `Response`

    - **ProfileArn** *(string) --*

      The ARN of the newly created room profile in the response.
    """


_ClientCreateRoomResponseTypeDef = TypedDict(
    "_ClientCreateRoomResponseTypeDef", {"RoomArn": str}, total=False
)


class ClientCreateRoomResponseTypeDef(_ClientCreateRoomResponseTypeDef):
    """
    Type definition for `ClientCreateRoom` `Response`

    - **RoomArn** *(string) --*

      The ARN of the newly created room in the response.
    """


_ClientCreateRoomTagsTypeDef = TypedDict(
    "_ClientCreateRoomTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateRoomTagsTypeDef(_ClientCreateRoomTagsTypeDef):
    """
    Type definition for `ClientCreateRoom` `Tags`

    A key-value pair that can be associated with a resource.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a tag. Tag keys are case-sensitive.

    - **Value** *(string) --* **[REQUIRED]**

      The value of a tag. Tag values are case-sensitive and can be null.
    """


_ClientCreateSkillGroupResponseTypeDef = TypedDict(
    "_ClientCreateSkillGroupResponseTypeDef", {"SkillGroupArn": str}, total=False
)


class ClientCreateSkillGroupResponseTypeDef(_ClientCreateSkillGroupResponseTypeDef):
    """
    Type definition for `ClientCreateSkillGroup` `Response`

    - **SkillGroupArn** *(string) --*

      The ARN of the newly created skill group in the response.
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef", {"UserArn": str}, total=False
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    Type definition for `ClientCreateUser` `Response`

    - **UserArn** *(string) --*

      The ARN of the newly created user in the response.
    """


_ClientCreateUserTagsTypeDef = TypedDict(
    "_ClientCreateUserTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateUserTagsTypeDef(_ClientCreateUserTagsTypeDef):
    """
    Type definition for `ClientCreateUser` `Tags`

    A key-value pair that can be associated with a resource.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a tag. Tag keys are case-sensitive.

    - **Value** *(string) --* **[REQUIRED]**

      The value of a tag. Tag values are case-sensitive and can be null.
    """


_ClientGetAddressBookResponseAddressBookTypeDef = TypedDict(
    "_ClientGetAddressBookResponseAddressBookTypeDef",
    {"AddressBookArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientGetAddressBookResponseAddressBookTypeDef(
    _ClientGetAddressBookResponseAddressBookTypeDef
):
    """
    Type definition for `ClientGetAddressBookResponse` `AddressBook`

    The details of the requested address book.

    - **AddressBookArn** *(string) --*

      The ARN of the address book.

    - **Name** *(string) --*

      The name of the address book.

    - **Description** *(string) --*

      The description of the address book.
    """


_ClientGetAddressBookResponseTypeDef = TypedDict(
    "_ClientGetAddressBookResponseTypeDef",
    {"AddressBook": ClientGetAddressBookResponseAddressBookTypeDef},
    total=False,
)


class ClientGetAddressBookResponseTypeDef(_ClientGetAddressBookResponseTypeDef):
    """
    Type definition for `ClientGetAddressBook` `Response`

    - **AddressBook** *(dict) --*

      The details of the requested address book.

      - **AddressBookArn** *(string) --*

        The ARN of the address book.

      - **Name** *(string) --*

        The name of the address book.

      - **Description** *(string) --*

        The description of the address book.
    """


_ClientGetConferencePreferenceResponsePreferenceTypeDef = TypedDict(
    "_ClientGetConferencePreferenceResponsePreferenceTypeDef",
    {"DefaultConferenceProviderArn": str},
    total=False,
)


class ClientGetConferencePreferenceResponsePreferenceTypeDef(
    _ClientGetConferencePreferenceResponsePreferenceTypeDef
):
    """
    Type definition for `ClientGetConferencePreferenceResponse` `Preference`

    The conference preference.

    - **DefaultConferenceProviderArn** *(string) --*

      The ARN of the default conference provider.
    """


_ClientGetConferencePreferenceResponseTypeDef = TypedDict(
    "_ClientGetConferencePreferenceResponseTypeDef",
    {"Preference": ClientGetConferencePreferenceResponsePreferenceTypeDef},
    total=False,
)


class ClientGetConferencePreferenceResponseTypeDef(
    _ClientGetConferencePreferenceResponseTypeDef
):
    """
    Type definition for `ClientGetConferencePreference` `Response`

    - **Preference** *(dict) --*

      The conference preference.

      - **DefaultConferenceProviderArn** *(string) --*

        The ARN of the default conference provider.
    """


_ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef = TypedDict(
    "_ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef",
    {"Endpoint": str, "CommsProtocol": str},
    total=False,
)


class ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef(
    _ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef
):
    """
    Type definition for `ClientGetConferenceProviderResponseConferenceProvider` `IPDialIn`

    The IP endpoint and protocol for calling.

    - **Endpoint** *(string) --*

      The IP address.

    - **CommsProtocol** *(string) --*

      The protocol, including SIP, SIPS, and H323.
    """


_ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef = TypedDict(
    "_ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef",
    {"RequirePin": str},
    total=False,
)


class ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef(
    _ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef
):
    """
    Type definition for `ClientGetConferenceProviderResponseConferenceProvider` `MeetingSetting`

    The meeting settings for the conference provider.

    - **RequirePin** *(string) --*

      The values that indicate whether the pin is always required.
    """


_ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef",
    {
        "CountryCode": str,
        "PhoneNumber": str,
        "OneClickIdDelay": str,
        "OneClickPinDelay": str,
    },
    total=False,
)


class ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef(
    _ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef
):
    """
    Type definition for `ClientGetConferenceProviderResponseConferenceProvider` `PSTNDialIn`

    The information for PSTN conferencing.

    - **CountryCode** *(string) --*

      The zip code.

    - **PhoneNumber** *(string) --*

      The phone number to call to join the conference.

    - **OneClickIdDelay** *(string) --*

      The delay duration before Alexa enters the conference ID with dual-tone multi-frequency
      (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data
      over the telephone network.

    - **OneClickPinDelay** *(string) --*

      The delay duration before Alexa enters the conference pin with dual-tone multi-frequency
      (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data
      over the telephone network.
    """


_ClientGetConferenceProviderResponseConferenceProviderTypeDef = TypedDict(
    "_ClientGetConferenceProviderResponseConferenceProviderTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": str,
        "IPDialIn": ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef,
        "PSTNDialIn": ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef,
        "MeetingSetting": ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef,
    },
    total=False,
)


class ClientGetConferenceProviderResponseConferenceProviderTypeDef(
    _ClientGetConferenceProviderResponseConferenceProviderTypeDef
):
    """
    Type definition for `ClientGetConferenceProviderResponse` `ConferenceProvider`

    The conference provider.

    - **Arn** *(string) --*

      The ARN of the newly created conference provider.

    - **Name** *(string) --*

      The name of the conference provider.

    - **Type** *(string) --*

      The type of conference providers.

    - **IPDialIn** *(dict) --*

      The IP endpoint and protocol for calling.

      - **Endpoint** *(string) --*

        The IP address.

      - **CommsProtocol** *(string) --*

        The protocol, including SIP, SIPS, and H323.

    - **PSTNDialIn** *(dict) --*

      The information for PSTN conferencing.

      - **CountryCode** *(string) --*

        The zip code.

      - **PhoneNumber** *(string) --*

        The phone number to call to join the conference.

      - **OneClickIdDelay** *(string) --*

        The delay duration before Alexa enters the conference ID with dual-tone multi-frequency
        (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data
        over the telephone network.

      - **OneClickPinDelay** *(string) --*

        The delay duration before Alexa enters the conference pin with dual-tone multi-frequency
        (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data
        over the telephone network.

    - **MeetingSetting** *(dict) --*

      The meeting settings for the conference provider.

      - **RequirePin** *(string) --*

        The values that indicate whether the pin is always required.
    """


_ClientGetConferenceProviderResponseTypeDef = TypedDict(
    "_ClientGetConferenceProviderResponseTypeDef",
    {
        "ConferenceProvider": ClientGetConferenceProviderResponseConferenceProviderTypeDef
    },
    total=False,
)


class ClientGetConferenceProviderResponseTypeDef(
    _ClientGetConferenceProviderResponseTypeDef
):
    """
    Type definition for `ClientGetConferenceProvider` `Response`

    - **ConferenceProvider** *(dict) --*

      The conference provider.

      - **Arn** *(string) --*

        The ARN of the newly created conference provider.

      - **Name** *(string) --*

        The name of the conference provider.

      - **Type** *(string) --*

        The type of conference providers.

      - **IPDialIn** *(dict) --*

        The IP endpoint and protocol for calling.

        - **Endpoint** *(string) --*

          The IP address.

        - **CommsProtocol** *(string) --*

          The protocol, including SIP, SIPS, and H323.

      - **PSTNDialIn** *(dict) --*

        The information for PSTN conferencing.

        - **CountryCode** *(string) --*

          The zip code.

        - **PhoneNumber** *(string) --*

          The phone number to call to join the conference.

        - **OneClickIdDelay** *(string) --*

          The delay duration before Alexa enters the conference ID with dual-tone multi-frequency
          (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data
          over the telephone network.

        - **OneClickPinDelay** *(string) --*

          The delay duration before Alexa enters the conference pin with dual-tone multi-frequency
          (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data
          over the telephone network.

      - **MeetingSetting** *(dict) --*

        The meeting settings for the conference provider.

        - **RequirePin** *(string) --*

          The values that indicate whether the pin is always required.
    """


_ClientGetContactResponseContactPhoneNumbersTypeDef = TypedDict(
    "_ClientGetContactResponseContactPhoneNumbersTypeDef",
    {"Number": str, "Type": str},
    total=False,
)


class ClientGetContactResponseContactPhoneNumbersTypeDef(
    _ClientGetContactResponseContactPhoneNumbersTypeDef
):
    """
    Type definition for `ClientGetContactResponseContact` `PhoneNumbers`

    The phone number for the contact containing the raw number and phone number type.

    - **Number** *(string) --*

      The raw value of the phone number.

    - **Type** *(string) --*

      The type of the phone number.
    """


_ClientGetContactResponseContactSipAddressesTypeDef = TypedDict(
    "_ClientGetContactResponseContactSipAddressesTypeDef",
    {"Uri": str, "Type": str},
    total=False,
)


class ClientGetContactResponseContactSipAddressesTypeDef(
    _ClientGetContactResponseContactSipAddressesTypeDef
):
    """
    Type definition for `ClientGetContactResponseContact` `SipAddresses`

    The SIP address for the contact containing the URI and SIP address type.

    - **Uri** *(string) --*

      The URI for the SIP address.

    - **Type** *(string) --*

      The type of the SIP address.
    """


_ClientGetContactResponseContactTypeDef = TypedDict(
    "_ClientGetContactResponseContactTypeDef",
    {
        "ContactArn": str,
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List[ClientGetContactResponseContactPhoneNumbersTypeDef],
        "SipAddresses": List[ClientGetContactResponseContactSipAddressesTypeDef],
    },
    total=False,
)


class ClientGetContactResponseContactTypeDef(_ClientGetContactResponseContactTypeDef):
    """
    Type definition for `ClientGetContactResponse` `Contact`

    The details of the requested contact.

    - **ContactArn** *(string) --*

      The ARN of the contact.

    - **DisplayName** *(string) --*

      The name of the contact to display on the console.

    - **FirstName** *(string) --*

      The first name of the contact, used to call the contact on the device.

    - **LastName** *(string) --*

      The last name of the contact, used to call the contact on the device.

    - **PhoneNumber** *(string) --*

      The phone number of the contact. The phone number type defaults to WORK. You can either
      specify PhoneNumber or PhoneNumbers. We recommend that you use PhoneNumbers, which lets you
      specify the phone number type and multiple numbers.

    - **PhoneNumbers** *(list) --*

      The list of phone numbers for the contact.

      - *(dict) --*

        The phone number for the contact containing the raw number and phone number type.

        - **Number** *(string) --*

          The raw value of the phone number.

        - **Type** *(string) --*

          The type of the phone number.

    - **SipAddresses** *(list) --*

      The list of SIP addresses for the contact.

      - *(dict) --*

        The SIP address for the contact containing the URI and SIP address type.

        - **Uri** *(string) --*

          The URI for the SIP address.

        - **Type** *(string) --*

          The type of the SIP address.
    """


_ClientGetContactResponseTypeDef = TypedDict(
    "_ClientGetContactResponseTypeDef",
    {"Contact": ClientGetContactResponseContactTypeDef},
    total=False,
)


class ClientGetContactResponseTypeDef(_ClientGetContactResponseTypeDef):
    """
    Type definition for `ClientGetContact` `Response`

    - **Contact** *(dict) --*

      The details of the requested contact.

      - **ContactArn** *(string) --*

        The ARN of the contact.

      - **DisplayName** *(string) --*

        The name of the contact to display on the console.

      - **FirstName** *(string) --*

        The first name of the contact, used to call the contact on the device.

      - **LastName** *(string) --*

        The last name of the contact, used to call the contact on the device.

      - **PhoneNumber** *(string) --*

        The phone number of the contact. The phone number type defaults to WORK. You can either
        specify PhoneNumber or PhoneNumbers. We recommend that you use PhoneNumbers, which lets you
        specify the phone number type and multiple numbers.

      - **PhoneNumbers** *(list) --*

        The list of phone numbers for the contact.

        - *(dict) --*

          The phone number for the contact containing the raw number and phone number type.

          - **Number** *(string) --*

            The raw value of the phone number.

          - **Type** *(string) --*

            The type of the phone number.

      - **SipAddresses** *(list) --*

        The list of SIP addresses for the contact.

        - *(dict) --*

          The SIP address for the contact containing the URI and SIP address type.

          - **Uri** *(string) --*

            The URI for the SIP address.

          - **Type** *(string) --*

            The type of the SIP address.
    """


_ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef",
    {"Feature": str, "Code": str},
    total=False,
)


class ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef(
    _ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef
):
    """
    Type definition for `ClientGetDeviceResponseDeviceDeviceStatusInfo` `DeviceStatusDetails`

    Details of a device’s status.

    - **Feature** *(string) --*

      The list of available features on the device.

    - **Code** *(string) --*

      The device status detail code.
    """


_ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List[
            ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef
        ],
        "ConnectionStatus": str,
    },
    total=False,
)


class ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef(
    _ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef
):
    """
    Type definition for `ClientGetDeviceResponseDevice` `DeviceStatusInfo`

    Detailed information about a device's status.

    - **DeviceStatusDetails** *(list) --*

      One or more device status detail descriptions.

      - *(dict) --*

        Details of a device’s status.

        - **Feature** *(string) --*

          The list of available features on the device.

        - **Code** *(string) --*

          The device status detail code.

    - **ConnectionStatus** *(string) --*

      The latest available information about the connection status of a device.
    """


_ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef",
    {
        "NetworkProfileArn": str,
        "CertificateArn": str,
        "CertificateExpirationTime": datetime,
    },
    total=False,
)


class ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef(
    _ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef
):
    """
    Type definition for `ClientGetDeviceResponseDevice` `NetworkProfileInfo`

    Detailed information about a device's network profile.

    - **NetworkProfileArn** *(string) --*

      The ARN of the network profile associated with a device.

    - **CertificateArn** *(string) --*

      The ARN of the certificate associated with a device.

    - **CertificateExpirationTime** *(datetime) --*

      The time (in epoch) when the certificate expires.
    """


_ClientGetDeviceResponseDeviceTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "RoomArn": str,
        "DeviceStatus": str,
        "DeviceStatusInfo": ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef,
        "NetworkProfileInfo": ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef,
    },
    total=False,
)


class ClientGetDeviceResponseDeviceTypeDef(_ClientGetDeviceResponseDeviceTypeDef):
    """
    Type definition for `ClientGetDeviceResponse` `Device`

    The details of the device requested. Required.

    - **DeviceArn** *(string) --*

      The ARN of a device.

    - **DeviceSerialNumber** *(string) --*

      The serial number of a device.

    - **DeviceType** *(string) --*

      The type of a device.

    - **DeviceName** *(string) --*

      The name of a device.

    - **SoftwareVersion** *(string) --*

      The software version of a device.

    - **MacAddress** *(string) --*

      The MAC address of a device.

    - **RoomArn** *(string) --*

      The room ARN of a device.

    - **DeviceStatus** *(string) --*

      The status of a device. If the status is not READY, check the DeviceStatusInfo value for
      details.

    - **DeviceStatusInfo** *(dict) --*

      Detailed information about a device's status.

      - **DeviceStatusDetails** *(list) --*

        One or more device status detail descriptions.

        - *(dict) --*

          Details of a device’s status.

          - **Feature** *(string) --*

            The list of available features on the device.

          - **Code** *(string) --*

            The device status detail code.

      - **ConnectionStatus** *(string) --*

        The latest available information about the connection status of a device.

    - **NetworkProfileInfo** *(dict) --*

      Detailed information about a device's network profile.

      - **NetworkProfileArn** *(string) --*

        The ARN of the network profile associated with a device.

      - **CertificateArn** *(string) --*

        The ARN of the certificate associated with a device.

      - **CertificateExpirationTime** *(datetime) --*

        The time (in epoch) when the certificate expires.
    """


_ClientGetDeviceResponseTypeDef = TypedDict(
    "_ClientGetDeviceResponseTypeDef",
    {"Device": ClientGetDeviceResponseDeviceTypeDef},
    total=False,
)


class ClientGetDeviceResponseTypeDef(_ClientGetDeviceResponseTypeDef):
    """
    Type definition for `ClientGetDevice` `Response`

    - **Device** *(dict) --*

      The details of the device requested. Required.

      - **DeviceArn** *(string) --*

        The ARN of a device.

      - **DeviceSerialNumber** *(string) --*

        The serial number of a device.

      - **DeviceType** *(string) --*

        The type of a device.

      - **DeviceName** *(string) --*

        The name of a device.

      - **SoftwareVersion** *(string) --*

        The software version of a device.

      - **MacAddress** *(string) --*

        The MAC address of a device.

      - **RoomArn** *(string) --*

        The room ARN of a device.

      - **DeviceStatus** *(string) --*

        The status of a device. If the status is not READY, check the DeviceStatusInfo value for
        details.

      - **DeviceStatusInfo** *(dict) --*

        Detailed information about a device's status.

        - **DeviceStatusDetails** *(list) --*

          One or more device status detail descriptions.

          - *(dict) --*

            Details of a device’s status.

            - **Feature** *(string) --*

              The list of available features on the device.

            - **Code** *(string) --*

              The device status detail code.

        - **ConnectionStatus** *(string) --*

          The latest available information about the connection status of a device.

      - **NetworkProfileInfo** *(dict) --*

        Detailed information about a device's network profile.

        - **NetworkProfileArn** *(string) --*

          The ARN of the network profile associated with a device.

        - **CertificateArn** *(string) --*

          The ARN of the certificate associated with a device.

        - **CertificateExpirationTime** *(datetime) --*

          The time (in epoch) when the certificate expires.
    """


_ClientGetGatewayGroupResponseGatewayGroupTypeDef = TypedDict(
    "_ClientGetGatewayGroupResponseGatewayGroupTypeDef",
    {"Arn": str, "Name": str, "Description": str},
    total=False,
)


class ClientGetGatewayGroupResponseGatewayGroupTypeDef(
    _ClientGetGatewayGroupResponseGatewayGroupTypeDef
):
    """
    Type definition for `ClientGetGatewayGroupResponse` `GatewayGroup`

    The details of the gateway group.

    - **Arn** *(string) --*

      The ARN of the gateway group.

    - **Name** *(string) --*

      The name of the gateway group.

    - **Description** *(string) --*

      The description of the gateway group.
    """


_ClientGetGatewayGroupResponseTypeDef = TypedDict(
    "_ClientGetGatewayGroupResponseTypeDef",
    {"GatewayGroup": ClientGetGatewayGroupResponseGatewayGroupTypeDef},
    total=False,
)


class ClientGetGatewayGroupResponseTypeDef(_ClientGetGatewayGroupResponseTypeDef):
    """
    Type definition for `ClientGetGatewayGroup` `Response`

    - **GatewayGroup** *(dict) --*

      The details of the gateway group.

      - **Arn** *(string) --*

        The ARN of the gateway group.

      - **Name** *(string) --*

        The name of the gateway group.

      - **Description** *(string) --*

        The description of the gateway group.
    """


_ClientGetGatewayResponseGatewayTypeDef = TypedDict(
    "_ClientGetGatewayResponseGatewayTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "GatewayGroupArn": str,
        "SoftwareVersion": str,
    },
    total=False,
)


class ClientGetGatewayResponseGatewayTypeDef(_ClientGetGatewayResponseGatewayTypeDef):
    """
    Type definition for `ClientGetGatewayResponse` `Gateway`

    The details of the gateway.

    - **Arn** *(string) --*

      The ARN of the gateway.

    - **Name** *(string) --*

      The name of the gateway.

    - **Description** *(string) --*

      The description of the gateway.

    - **GatewayGroupArn** *(string) --*

      The ARN of the gateway group that the gateway is associated to.

    - **SoftwareVersion** *(string) --*

      The software version of the gateway. The gateway automatically updates its software version
      during normal operation.
    """


_ClientGetGatewayResponseTypeDef = TypedDict(
    "_ClientGetGatewayResponseTypeDef",
    {"Gateway": ClientGetGatewayResponseGatewayTypeDef},
    total=False,
)


class ClientGetGatewayResponseTypeDef(_ClientGetGatewayResponseTypeDef):
    """
    Type definition for `ClientGetGateway` `Response`

    - **Gateway** *(dict) --*

      The details of the gateway.

      - **Arn** *(string) --*

        The ARN of the gateway.

      - **Name** *(string) --*

        The name of the gateway.

      - **Description** *(string) --*

        The description of the gateway.

      - **GatewayGroupArn** *(string) --*

        The ARN of the gateway group that the gateway is associated to.

      - **SoftwareVersion** *(string) --*

        The software version of the gateway. The gateway automatically updates its software version
        during normal operation.
    """


_ClientGetInvitationConfigurationResponseTypeDef = TypedDict(
    "_ClientGetInvitationConfigurationResponseTypeDef",
    {"OrganizationName": str, "ContactEmail": str, "PrivateSkillIds": List[str]},
    total=False,
)


class ClientGetInvitationConfigurationResponseTypeDef(
    _ClientGetInvitationConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetInvitationConfiguration` `Response`

    - **OrganizationName** *(string) --*

      The name of the organization sending the enrollment invite to a user.

    - **ContactEmail** *(string) --*

      The email ID of the organization or individual contact that the enrolled user can use.

    - **PrivateSkillIds** *(list) --*

      The list of private skill IDs that you want to recommend to the user to enable in the
      invitation.

      - *(string) --*
    """


_ClientGetNetworkProfileResponseNetworkProfileTypeDef = TypedDict(
    "_ClientGetNetworkProfileResponseNetworkProfileTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "Description": str,
        "Ssid": str,
        "SecurityType": str,
        "EapMethod": str,
        "CurrentPassword": str,
        "NextPassword": str,
        "CertificateAuthorityArn": str,
        "TrustAnchors": List[str],
    },
    total=False,
)


class ClientGetNetworkProfileResponseNetworkProfileTypeDef(
    _ClientGetNetworkProfileResponseNetworkProfileTypeDef
):
    """
    Type definition for `ClientGetNetworkProfileResponse` `NetworkProfile`

    The network profile associated with a device.

    - **NetworkProfileArn** *(string) --*

      The ARN of the network profile associated with a device.

    - **NetworkProfileName** *(string) --*

      The name of the network profile associated with a device.

    - **Description** *(string) --*

      Detailed information about a device's network profile.

    - **Ssid** *(string) --*

      The SSID of the Wi-Fi network.

    - **SecurityType** *(string) --*

      The security type of the Wi-Fi network. This can be WPA2_ENTERPRISE, WPA2_PSK, WPA_PSK,
      WEP, or OPEN.

    - **EapMethod** *(string) --*

      The authentication standard that is used in the EAP framework. Currently, EAP_TLS is
      supported.

    - **CurrentPassword** *(string) --*

      The current password of the Wi-Fi network.

    - **NextPassword** *(string) --*

      The next, or subsequent, password of the Wi-Fi network. This password is asynchronously
      transmitted to the device and is used when the password of the network changes to
      NextPassword.

    - **CertificateAuthorityArn** *(string) --*

      The ARN of the Private Certificate Authority (PCA) created in AWS Certificate Manager
      (ACM). This is used to issue certificates to the devices.

    - **TrustAnchors** *(list) --*

      The root certificates of your authentication server, which is installed on your devices and
      used to trust your authentication server during EAP negotiation.

      - *(string) --*
    """


_ClientGetNetworkProfileResponseTypeDef = TypedDict(
    "_ClientGetNetworkProfileResponseTypeDef",
    {"NetworkProfile": ClientGetNetworkProfileResponseNetworkProfileTypeDef},
    total=False,
)


class ClientGetNetworkProfileResponseTypeDef(_ClientGetNetworkProfileResponseTypeDef):
    """
    Type definition for `ClientGetNetworkProfile` `Response`

    - **NetworkProfile** *(dict) --*

      The network profile associated with a device.

      - **NetworkProfileArn** *(string) --*

        The ARN of the network profile associated with a device.

      - **NetworkProfileName** *(string) --*

        The name of the network profile associated with a device.

      - **Description** *(string) --*

        Detailed information about a device's network profile.

      - **Ssid** *(string) --*

        The SSID of the Wi-Fi network.

      - **SecurityType** *(string) --*

        The security type of the Wi-Fi network. This can be WPA2_ENTERPRISE, WPA2_PSK, WPA_PSK,
        WEP, or OPEN.

      - **EapMethod** *(string) --*

        The authentication standard that is used in the EAP framework. Currently, EAP_TLS is
        supported.

      - **CurrentPassword** *(string) --*

        The current password of the Wi-Fi network.

      - **NextPassword** *(string) --*

        The next, or subsequent, password of the Wi-Fi network. This password is asynchronously
        transmitted to the device and is used when the password of the network changes to
        NextPassword.

      - **CertificateAuthorityArn** *(string) --*

        The ARN of the Private Certificate Authority (PCA) created in AWS Certificate Manager
        (ACM). This is used to issue certificates to the devices.

      - **TrustAnchors** *(list) --*

        The root certificates of your authentication server, which is installed on your devices and
        used to trust your authentication server during EAP negotiation.

        - *(string) --*
    """


_ClientGetProfileResponseProfileTypeDef = TypedDict(
    "_ClientGetProfileResponseProfileTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": str,
        "TemperatureUnit": str,
        "WakeWord": str,
        "Locale": str,
        "SetupModeDisabled": bool,
        "MaxVolumeLimit": int,
        "PSTNEnabled": bool,
        "AddressBookArn": str,
    },
    total=False,
)


class ClientGetProfileResponseProfileTypeDef(_ClientGetProfileResponseProfileTypeDef):
    """
    Type definition for `ClientGetProfileResponse` `Profile`

    The details of the room profile requested. Required.

    - **ProfileArn** *(string) --*

      The ARN of a room profile.

    - **ProfileName** *(string) --*

      The name of a room profile.

    - **IsDefault** *(boolean) --*

      Retrieves if the profile is default or not.

    - **Address** *(string) --*

      The address of a room profile.

    - **Timezone** *(string) --*

      The time zone of a room profile.

    - **DistanceUnit** *(string) --*

      The distance unit of a room profile.

    - **TemperatureUnit** *(string) --*

      The temperature unit of a room profile.

    - **WakeWord** *(string) --*

      The wake word of a room profile.

    - **Locale** *(string) --*

      The locale of a room profile.

    - **SetupModeDisabled** *(boolean) --*

      The setup mode of a room profile.

    - **MaxVolumeLimit** *(integer) --*

      The max volume limit of a room profile.

    - **PSTNEnabled** *(boolean) --*

      The PSTN setting of a room profile.

    - **AddressBookArn** *(string) --*

      The ARN of the address book.
    """


_ClientGetProfileResponseTypeDef = TypedDict(
    "_ClientGetProfileResponseTypeDef",
    {"Profile": ClientGetProfileResponseProfileTypeDef},
    total=False,
)


class ClientGetProfileResponseTypeDef(_ClientGetProfileResponseTypeDef):
    """
    Type definition for `ClientGetProfile` `Response`

    - **Profile** *(dict) --*

      The details of the room profile requested. Required.

      - **ProfileArn** *(string) --*

        The ARN of a room profile.

      - **ProfileName** *(string) --*

        The name of a room profile.

      - **IsDefault** *(boolean) --*

        Retrieves if the profile is default or not.

      - **Address** *(string) --*

        The address of a room profile.

      - **Timezone** *(string) --*

        The time zone of a room profile.

      - **DistanceUnit** *(string) --*

        The distance unit of a room profile.

      - **TemperatureUnit** *(string) --*

        The temperature unit of a room profile.

      - **WakeWord** *(string) --*

        The wake word of a room profile.

      - **Locale** *(string) --*

        The locale of a room profile.

      - **SetupModeDisabled** *(boolean) --*

        The setup mode of a room profile.

      - **MaxVolumeLimit** *(integer) --*

        The max volume limit of a room profile.

      - **PSTNEnabled** *(boolean) --*

        The PSTN setting of a room profile.

      - **AddressBookArn** *(string) --*

        The ARN of the address book.
    """


_ClientGetRoomResponseRoomTypeDef = TypedDict(
    "_ClientGetRoomResponseRoomTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
    },
    total=False,
)


class ClientGetRoomResponseRoomTypeDef(_ClientGetRoomResponseRoomTypeDef):
    """
    Type definition for `ClientGetRoomResponse` `Room`

    The details of the room requested.

    - **RoomArn** *(string) --*

      The ARN of a room.

    - **RoomName** *(string) --*

      The name of a room.

    - **Description** *(string) --*

      The description of a room.

    - **ProviderCalendarId** *(string) --*

      The provider calendar ARN of a room.

    - **ProfileArn** *(string) --*

      The profile ARN of a room.
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

      The details of the room requested.

      - **RoomArn** *(string) --*

        The ARN of a room.

      - **RoomName** *(string) --*

        The name of a room.

      - **Description** *(string) --*

        The description of a room.

      - **ProviderCalendarId** *(string) --*

        The provider calendar ARN of a room.

      - **ProfileArn** *(string) --*

        The profile ARN of a room.
    """


_ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef = TypedDict(
    "_ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef",
    {"ParameterKey": str, "ParameterValue": str},
    total=False,
)


class ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef(
    _ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef
):
    """
    Type definition for `ClientGetRoomSkillParameterResponse` `RoomSkillParameter`

    The details of the room skill parameter requested. Required.

    - **ParameterKey** *(string) --*

      The parameter key of a room skill parameter. ParameterKey is an enumerated type that only
      takes “DEFAULT” or “SCOPE” as valid values.

    - **ParameterValue** *(string) --*

      The parameter value of a room skill parameter.
    """


_ClientGetRoomSkillParameterResponseTypeDef = TypedDict(
    "_ClientGetRoomSkillParameterResponseTypeDef",
    {
        "RoomSkillParameter": ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef
    },
    total=False,
)


class ClientGetRoomSkillParameterResponseTypeDef(
    _ClientGetRoomSkillParameterResponseTypeDef
):
    """
    Type definition for `ClientGetRoomSkillParameter` `Response`

    - **RoomSkillParameter** *(dict) --*

      The details of the room skill parameter requested. Required.

      - **ParameterKey** *(string) --*

        The parameter key of a room skill parameter. ParameterKey is an enumerated type that only
        takes “DEFAULT” or “SCOPE” as valid values.

      - **ParameterValue** *(string) --*

        The parameter value of a room skill parameter.
    """


_ClientGetSkillGroupResponseSkillGroupTypeDef = TypedDict(
    "_ClientGetSkillGroupResponseSkillGroupTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)


class ClientGetSkillGroupResponseSkillGroupTypeDef(
    _ClientGetSkillGroupResponseSkillGroupTypeDef
):
    """
    Type definition for `ClientGetSkillGroupResponse` `SkillGroup`

    The details of the skill group requested. Required.

    - **SkillGroupArn** *(string) --*

      The ARN of a skill group.

    - **SkillGroupName** *(string) --*

      The name of a skill group.

    - **Description** *(string) --*

      The description of a skill group.
    """


_ClientGetSkillGroupResponseTypeDef = TypedDict(
    "_ClientGetSkillGroupResponseTypeDef",
    {"SkillGroup": ClientGetSkillGroupResponseSkillGroupTypeDef},
    total=False,
)


class ClientGetSkillGroupResponseTypeDef(_ClientGetSkillGroupResponseTypeDef):
    """
    Type definition for `ClientGetSkillGroup` `Response`

    - **SkillGroup** *(dict) --*

      The details of the skill group requested. Required.

      - **SkillGroupArn** *(string) --*

        The ARN of a skill group.

      - **SkillGroupName** *(string) --*

        The name of a skill group.

      - **Description** *(string) --*

        The description of a skill group.
    """


_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef",
    {"Interval": str},
    total=False,
)


class ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef(
    _ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef
):
    """
    Type definition for `ClientListBusinessReportSchedulesResponseBusinessReportSchedules` `ContentRange`

    The content range of the reports.

    - **Interval** *(string) --*

      The interval of the content range.
    """


_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef",
    {"Path": str, "BucketName": str},
    total=False,
)


class ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef(
    _ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef
):
    """
    Type definition for `ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReport` `S3Location`

    The S3 location of the output reports.

    - **Path** *(string) --*

      The path of the business report.

    - **BucketName** *(string) --*

      The S3 bucket name of the output reports.
    """


_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef",
    {
        "Status": str,
        "FailureCode": str,
        "S3Location": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef,
        "DeliveryTime": datetime,
        "DownloadUrl": str,
    },
    total=False,
)


class ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef(
    _ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef
):
    """
    Type definition for `ClientListBusinessReportSchedulesResponseBusinessReportSchedules` `LastBusinessReport`

    The details of the last business report delivery for a specified time interval.

    - **Status** *(string) --*

      The status of the report generation execution (RUNNING, SUCCEEDED, or FAILED).

    - **FailureCode** *(string) --*

      The failure code.

    - **S3Location** *(dict) --*

      The S3 location of the output reports.

      - **Path** *(string) --*

        The path of the business report.

      - **BucketName** *(string) --*

        The S3 bucket name of the output reports.

    - **DeliveryTime** *(datetime) --*

      The time of report delivery.

    - **DownloadUrl** *(string) --*

      The download link where a user can download the report.
    """


_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef",
    {"StartDate": str},
    total=False,
)


class ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef(
    _ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef
):
    """
    Type definition for `ClientListBusinessReportSchedulesResponseBusinessReportSchedules` `Recurrence`

    The recurrence of the reports.

    - **StartDate** *(string) --*

      The start date.
    """


_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef",
    {
        "ScheduleArn": str,
        "ScheduleName": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "Format": str,
        "ContentRange": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef,
        "Recurrence": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef,
        "LastBusinessReport": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef,
    },
    total=False,
)


class ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef(
    _ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef
):
    """
    Type definition for `ClientListBusinessReportSchedulesResponse` `BusinessReportSchedules`

    The schedule of the usage report.

    - **ScheduleArn** *(string) --*

      The ARN of the business report schedule.

    - **ScheduleName** *(string) --*

      The name identifier of the schedule.

    - **S3BucketName** *(string) --*

      The S3 bucket name of the output reports.

    - **S3KeyPrefix** *(string) --*

      The S3 key where the report is delivered.

    - **Format** *(string) --*

      The format of the generated report (individual CSV files or zipped files of individual
      files).

    - **ContentRange** *(dict) --*

      The content range of the reports.

      - **Interval** *(string) --*

        The interval of the content range.

    - **Recurrence** *(dict) --*

      The recurrence of the reports.

      - **StartDate** *(string) --*

        The start date.

    - **LastBusinessReport** *(dict) --*

      The details of the last business report delivery for a specified time interval.

      - **Status** *(string) --*

        The status of the report generation execution (RUNNING, SUCCEEDED, or FAILED).

      - **FailureCode** *(string) --*

        The failure code.

      - **S3Location** *(dict) --*

        The S3 location of the output reports.

        - **Path** *(string) --*

          The path of the business report.

        - **BucketName** *(string) --*

          The S3 bucket name of the output reports.

      - **DeliveryTime** *(datetime) --*

        The time of report delivery.

      - **DownloadUrl** *(string) --*

        The download link where a user can download the report.
    """


_ClientListBusinessReportSchedulesResponseTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseTypeDef",
    {
        "BusinessReportSchedules": List[
            ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListBusinessReportSchedulesResponseTypeDef(
    _ClientListBusinessReportSchedulesResponseTypeDef
):
    """
    Type definition for `ClientListBusinessReportSchedules` `Response`

    - **BusinessReportSchedules** *(list) --*

      The schedule of the reports.

      - *(dict) --*

        The schedule of the usage report.

        - **ScheduleArn** *(string) --*

          The ARN of the business report schedule.

        - **ScheduleName** *(string) --*

          The name identifier of the schedule.

        - **S3BucketName** *(string) --*

          The S3 bucket name of the output reports.

        - **S3KeyPrefix** *(string) --*

          The S3 key where the report is delivered.

        - **Format** *(string) --*

          The format of the generated report (individual CSV files or zipped files of individual
          files).

        - **ContentRange** *(dict) --*

          The content range of the reports.

          - **Interval** *(string) --*

            The interval of the content range.

        - **Recurrence** *(dict) --*

          The recurrence of the reports.

          - **StartDate** *(string) --*

            The start date.

        - **LastBusinessReport** *(dict) --*

          The details of the last business report delivery for a specified time interval.

          - **Status** *(string) --*

            The status of the report generation execution (RUNNING, SUCCEEDED, or FAILED).

          - **FailureCode** *(string) --*

            The failure code.

          - **S3Location** *(dict) --*

            The S3 location of the output reports.

            - **Path** *(string) --*

              The path of the business report.

            - **BucketName** *(string) --*

              The S3 bucket name of the output reports.

          - **DeliveryTime** *(datetime) --*

            The time of report delivery.

          - **DownloadUrl** *(string) --*

            The download link where a user can download the report.

    - **NextToken** *(string) --*

      The token used to list the remaining schedules from the previous API call.
    """


_ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef = TypedDict(
    "_ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef",
    {"Endpoint": str, "CommsProtocol": str},
    total=False,
)


class ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef(
    _ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef
):
    """
    Type definition for `ClientListConferenceProvidersResponseConferenceProviders` `IPDialIn`

    The IP endpoint and protocol for calling.

    - **Endpoint** *(string) --*

      The IP address.

    - **CommsProtocol** *(string) --*

      The protocol, including SIP, SIPS, and H323.
    """


_ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef = TypedDict(
    "_ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef",
    {"RequirePin": str},
    total=False,
)


class ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef(
    _ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef
):
    """
    Type definition for `ClientListConferenceProvidersResponseConferenceProviders` `MeetingSetting`

    The meeting settings for the conference provider.

    - **RequirePin** *(string) --*

      The values that indicate whether the pin is always required.
    """


_ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef = TypedDict(
    "_ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef",
    {
        "CountryCode": str,
        "PhoneNumber": str,
        "OneClickIdDelay": str,
        "OneClickPinDelay": str,
    },
    total=False,
)


class ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef(
    _ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef
):
    """
    Type definition for `ClientListConferenceProvidersResponseConferenceProviders` `PSTNDialIn`

    The information for PSTN conferencing.

    - **CountryCode** *(string) --*

      The zip code.

    - **PhoneNumber** *(string) --*

      The phone number to call to join the conference.

    - **OneClickIdDelay** *(string) --*

      The delay duration before Alexa enters the conference ID with dual-tone multi-frequency
      (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send
      data over the telephone network.

    - **OneClickPinDelay** *(string) --*

      The delay duration before Alexa enters the conference pin with dual-tone
      multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which
      is how we send data over the telephone network.
    """


_ClientListConferenceProvidersResponseConferenceProvidersTypeDef = TypedDict(
    "_ClientListConferenceProvidersResponseConferenceProvidersTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": str,
        "IPDialIn": ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef,
        "PSTNDialIn": ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef,
        "MeetingSetting": ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef,
    },
    total=False,
)


class ClientListConferenceProvidersResponseConferenceProvidersTypeDef(
    _ClientListConferenceProvidersResponseConferenceProvidersTypeDef
):
    """
    Type definition for `ClientListConferenceProvidersResponse` `ConferenceProviders`

    An entity that provides a conferencing solution. Alexa for Business acts as the voice
    interface and mediator that connects users to their preferred conference provider. Examples
    of conference providers include Amazon Chime, Zoom, Cisco, and Polycom.

    - **Arn** *(string) --*

      The ARN of the newly created conference provider.

    - **Name** *(string) --*

      The name of the conference provider.

    - **Type** *(string) --*

      The type of conference providers.

    - **IPDialIn** *(dict) --*

      The IP endpoint and protocol for calling.

      - **Endpoint** *(string) --*

        The IP address.

      - **CommsProtocol** *(string) --*

        The protocol, including SIP, SIPS, and H323.

    - **PSTNDialIn** *(dict) --*

      The information for PSTN conferencing.

      - **CountryCode** *(string) --*

        The zip code.

      - **PhoneNumber** *(string) --*

        The phone number to call to join the conference.

      - **OneClickIdDelay** *(string) --*

        The delay duration before Alexa enters the conference ID with dual-tone multi-frequency
        (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send
        data over the telephone network.

      - **OneClickPinDelay** *(string) --*

        The delay duration before Alexa enters the conference pin with dual-tone
        multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which
        is how we send data over the telephone network.

    - **MeetingSetting** *(dict) --*

      The meeting settings for the conference provider.

      - **RequirePin** *(string) --*

        The values that indicate whether the pin is always required.
    """


_ClientListConferenceProvidersResponseTypeDef = TypedDict(
    "_ClientListConferenceProvidersResponseTypeDef",
    {
        "ConferenceProviders": List[
            ClientListConferenceProvidersResponseConferenceProvidersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListConferenceProvidersResponseTypeDef(
    _ClientListConferenceProvidersResponseTypeDef
):
    """
    Type definition for `ClientListConferenceProviders` `Response`

    - **ConferenceProviders** *(list) --*

      The conference providers.

      - *(dict) --*

        An entity that provides a conferencing solution. Alexa for Business acts as the voice
        interface and mediator that connects users to their preferred conference provider. Examples
        of conference providers include Amazon Chime, Zoom, Cisco, and Polycom.

        - **Arn** *(string) --*

          The ARN of the newly created conference provider.

        - **Name** *(string) --*

          The name of the conference provider.

        - **Type** *(string) --*

          The type of conference providers.

        - **IPDialIn** *(dict) --*

          The IP endpoint and protocol for calling.

          - **Endpoint** *(string) --*

            The IP address.

          - **CommsProtocol** *(string) --*

            The protocol, including SIP, SIPS, and H323.

        - **PSTNDialIn** *(dict) --*

          The information for PSTN conferencing.

          - **CountryCode** *(string) --*

            The zip code.

          - **PhoneNumber** *(string) --*

            The phone number to call to join the conference.

          - **OneClickIdDelay** *(string) --*

            The delay duration before Alexa enters the conference ID with dual-tone multi-frequency
            (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send
            data over the telephone network.

          - **OneClickPinDelay** *(string) --*

            The delay duration before Alexa enters the conference pin with dual-tone
            multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which
            is how we send data over the telephone network.

        - **MeetingSetting** *(dict) --*

          The meeting settings for the conference provider.

          - **RequirePin** *(string) --*

            The values that indicate whether the pin is always required.

    - **NextToken** *(string) --*

      The tokens used for pagination.
    """


_ClientListDeviceEventsResponseDeviceEventsTypeDef = TypedDict(
    "_ClientListDeviceEventsResponseDeviceEventsTypeDef",
    {"Type": str, "Value": str, "Timestamp": datetime},
    total=False,
)


class ClientListDeviceEventsResponseDeviceEventsTypeDef(
    _ClientListDeviceEventsResponseDeviceEventsTypeDef
):
    """
    Type definition for `ClientListDeviceEventsResponse` `DeviceEvents`

    The list of device events.

    - **Type** *(string) --*

      The type of device event.

    - **Value** *(string) --*

      The value of the event.

    - **Timestamp** *(datetime) --*

      The time (in epoch) when the event occurred.
    """


_ClientListDeviceEventsResponseTypeDef = TypedDict(
    "_ClientListDeviceEventsResponseTypeDef",
    {
        "DeviceEvents": List[ClientListDeviceEventsResponseDeviceEventsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListDeviceEventsResponseTypeDef(_ClientListDeviceEventsResponseTypeDef):
    """
    Type definition for `ClientListDeviceEvents` `Response`

    - **DeviceEvents** *(list) --*

      The device events requested for the device ARN.

      - *(dict) --*

        The list of device events.

        - **Type** *(string) --*

          The type of device event.

        - **Value** *(string) --*

          The value of the event.

        - **Timestamp** *(datetime) --*

          The time (in epoch) when the event occurred.

    - **NextToken** *(string) --*

      The token returned to indicate that there is more data available.
    """


_ClientListGatewayGroupsResponseGatewayGroupsTypeDef = TypedDict(
    "_ClientListGatewayGroupsResponseGatewayGroupsTypeDef",
    {"Arn": str, "Name": str, "Description": str},
    total=False,
)


class ClientListGatewayGroupsResponseGatewayGroupsTypeDef(
    _ClientListGatewayGroupsResponseGatewayGroupsTypeDef
):
    """
    Type definition for `ClientListGatewayGroupsResponse` `GatewayGroups`

    The summary of a gateway group.

    - **Arn** *(string) --*

      The ARN of the gateway group.

    - **Name** *(string) --*

      The name of the gateway group.

    - **Description** *(string) --*

      The description of the gateway group.
    """


_ClientListGatewayGroupsResponseTypeDef = TypedDict(
    "_ClientListGatewayGroupsResponseTypeDef",
    {
        "GatewayGroups": List[ClientListGatewayGroupsResponseGatewayGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListGatewayGroupsResponseTypeDef(_ClientListGatewayGroupsResponseTypeDef):
    """
    Type definition for `ClientListGatewayGroups` `Response`

    - **GatewayGroups** *(list) --*

      The gateway groups in the list.

      - *(dict) --*

        The summary of a gateway group.

        - **Arn** *(string) --*

          The ARN of the gateway group.

        - **Name** *(string) --*

          The name of the gateway group.

        - **Description** *(string) --*

          The description of the gateway group.

    - **NextToken** *(string) --*

      The token used to paginate though multiple pages of gateway group summaries.
    """


_ClientListGatewaysResponseGatewaysTypeDef = TypedDict(
    "_ClientListGatewaysResponseGatewaysTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "GatewayGroupArn": str,
        "SoftwareVersion": str,
    },
    total=False,
)


class ClientListGatewaysResponseGatewaysTypeDef(
    _ClientListGatewaysResponseGatewaysTypeDef
):
    """
    Type definition for `ClientListGatewaysResponse` `Gateways`

    The summary of a gateway.

    - **Arn** *(string) --*

      The ARN of the gateway.

    - **Name** *(string) --*

      The name of the gateway.

    - **Description** *(string) --*

      The description of the gateway.

    - **GatewayGroupArn** *(string) --*

      The ARN of the gateway group that the gateway is associated to.

    - **SoftwareVersion** *(string) --*

      The software version of the gateway. The gateway automatically updates its software
      version during normal operation.
    """


_ClientListGatewaysResponseTypeDef = TypedDict(
    "_ClientListGatewaysResponseTypeDef",
    {"Gateways": List[ClientListGatewaysResponseGatewaysTypeDef], "NextToken": str},
    total=False,
)


class ClientListGatewaysResponseTypeDef(_ClientListGatewaysResponseTypeDef):
    """
    Type definition for `ClientListGateways` `Response`

    - **Gateways** *(list) --*

      The gateways in the list.

      - *(dict) --*

        The summary of a gateway.

        - **Arn** *(string) --*

          The ARN of the gateway.

        - **Name** *(string) --*

          The name of the gateway.

        - **Description** *(string) --*

          The description of the gateway.

        - **GatewayGroupArn** *(string) --*

          The ARN of the gateway group that the gateway is associated to.

        - **SoftwareVersion** *(string) --*

          The software version of the gateway. The gateway automatically updates its software
          version during normal operation.

    - **NextToken** *(string) --*

      The token used to paginate though multiple pages of gateway summaries.
    """


_ClientListSkillsResponseSkillSummariesTypeDef = TypedDict(
    "_ClientListSkillsResponseSkillSummariesTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "SupportsLinking": bool,
        "EnablementType": str,
        "SkillType": str,
    },
    total=False,
)


class ClientListSkillsResponseSkillSummariesTypeDef(
    _ClientListSkillsResponseSkillSummariesTypeDef
):
    """
    Type definition for `ClientListSkillsResponse` `SkillSummaries`

    The summary of skills.

    - **SkillId** *(string) --*

      The ARN of the skill summary.

    - **SkillName** *(string) --*

      The name of the skill.

    - **SupportsLinking** *(boolean) --*

      Linking support for a skill.

    - **EnablementType** *(string) --*

      Whether the skill is enabled under the user's account, or if it requires linking to be
      used.

    - **SkillType** *(string) --*

      Whether the skill is publicly available or is a private skill.
    """


_ClientListSkillsResponseTypeDef = TypedDict(
    "_ClientListSkillsResponseTypeDef",
    {
        "SkillSummaries": List[ClientListSkillsResponseSkillSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListSkillsResponseTypeDef(_ClientListSkillsResponseTypeDef):
    """
    Type definition for `ClientListSkills` `Response`

    - **SkillSummaries** *(list) --*

      The list of enabled skills requested. Required.

      - *(dict) --*

        The summary of skills.

        - **SkillId** *(string) --*

          The ARN of the skill summary.

        - **SkillName** *(string) --*

          The name of the skill.

        - **SupportsLinking** *(boolean) --*

          Linking support for a skill.

        - **EnablementType** *(string) --*

          Whether the skill is enabled under the user's account, or if it requires linking to be
          used.

        - **SkillType** *(string) --*

          Whether the skill is publicly available or is a private skill.

    - **NextToken** *(string) --*

      The token returned to indicate that there is more data available.
    """


_ClientListSkillsStoreCategoriesResponseCategoryListTypeDef = TypedDict(
    "_ClientListSkillsStoreCategoriesResponseCategoryListTypeDef",
    {"CategoryId": int, "CategoryName": str},
    total=False,
)


class ClientListSkillsStoreCategoriesResponseCategoryListTypeDef(
    _ClientListSkillsStoreCategoriesResponseCategoryListTypeDef
):
    """
    Type definition for `ClientListSkillsStoreCategoriesResponse` `CategoryList`

    The skill store category that is shown. Alexa skills are assigned a specific skill category
    during creation, such as News, Social, and Sports.

    - **CategoryId** *(integer) --*

      The ID of the skill store category.

    - **CategoryName** *(string) --*

      The name of the skill store category.
    """


_ClientListSkillsStoreCategoriesResponseTypeDef = TypedDict(
    "_ClientListSkillsStoreCategoriesResponseTypeDef",
    {
        "CategoryList": List[
            ClientListSkillsStoreCategoriesResponseCategoryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSkillsStoreCategoriesResponseTypeDef(
    _ClientListSkillsStoreCategoriesResponseTypeDef
):
    """
    Type definition for `ClientListSkillsStoreCategories` `Response`

    - **CategoryList** *(list) --*

      The list of categories.

      - *(dict) --*

        The skill store category that is shown. Alexa skills are assigned a specific skill category
        during creation, such as News, Social, and Sports.

        - **CategoryId** *(integer) --*

          The ID of the skill store category.

        - **CategoryName** *(string) --*

          The name of the skill store category.

    - **NextToken** *(string) --*

      The tokens used for pagination.
    """


_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef = TypedDict(
    "_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef",
    {"DeveloperName": str, "PrivacyPolicy": str, "Email": str, "Url": str},
    total=False,
)


class ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef(
    _ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef
):
    """
    Type definition for `ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetails` `DeveloperInfo`

    The details about the developer that published the skill.

    - **DeveloperName** *(string) --*

      The name of the developer.

    - **PrivacyPolicy** *(string) --*

      The URL of the privacy policy.

    - **Email** *(string) --*

      The email of the developer.

    - **Url** *(string) --*

      The website of the developer.
    """


_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef = TypedDict(
    "_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef",
    {
        "ProductDescription": str,
        "InvocationPhrase": str,
        "ReleaseDate": str,
        "EndUserLicenseAgreement": str,
        "GenericKeywords": List[str],
        "BulletPoints": List[str],
        "NewInThisVersionBulletPoints": List[str],
        "SkillTypes": List[str],
        "Reviews": Dict[str, str],
        "DeveloperInfo": ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef,
    },
    total=False,
)


class ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef(
    _ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef
):
    """
    Type definition for `ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkills` `SkillDetails`

    Information about the skill.

    - **ProductDescription** *(string) --*

      The description of the product.

    - **InvocationPhrase** *(string) --*

      The phrase used to trigger the skill.

    - **ReleaseDate** *(string) --*

      The date when the skill was released.

    - **EndUserLicenseAgreement** *(string) --*

      The URL of the end user license agreement.

    - **GenericKeywords** *(list) --*

      The generic keywords associated with the skill that can be used to find a skill.

      - *(string) --*

    - **BulletPoints** *(list) --*

      The details about what the skill supports organized as bullet points.

      - *(string) --*

    - **NewInThisVersionBulletPoints** *(list) --*

      The updates added in bullet points.

      - *(string) --*

    - **SkillTypes** *(list) --*

      The types of skills.

      - *(string) --*

    - **Reviews** *(dict) --*

      The list of reviews for the skill, including Key and Value pair.

      - *(string) --*

        - *(string) --*

    - **DeveloperInfo** *(dict) --*

      The details about the developer that published the skill.

      - **DeveloperName** *(string) --*

        The name of the developer.

      - **PrivacyPolicy** *(string) --*

        The URL of the privacy policy.

      - **Email** *(string) --*

        The email of the developer.

      - **Url** *(string) --*

        The website of the developer.
    """


_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef = TypedDict(
    "_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "ShortDescription": str,
        "IconUrl": str,
        "SampleUtterances": List[str],
        "SkillDetails": ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef,
        "SupportsLinking": bool,
    },
    total=False,
)


class ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef(
    _ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef
):
    """
    Type definition for `ClientListSkillsStoreSkillsByCategoryResponse` `SkillsStoreSkills`

    The detailed information about an Alexa skill.

    - **SkillId** *(string) --*

      The ARN of the skill.

    - **SkillName** *(string) --*

      The name of the skill.

    - **ShortDescription** *(string) --*

      Short description about the skill.

    - **IconUrl** *(string) --*

      The URL where the skill icon resides.

    - **SampleUtterances** *(list) --*

      Sample utterances that interact with the skill.

      - *(string) --*

    - **SkillDetails** *(dict) --*

      Information about the skill.

      - **ProductDescription** *(string) --*

        The description of the product.

      - **InvocationPhrase** *(string) --*

        The phrase used to trigger the skill.

      - **ReleaseDate** *(string) --*

        The date when the skill was released.

      - **EndUserLicenseAgreement** *(string) --*

        The URL of the end user license agreement.

      - **GenericKeywords** *(list) --*

        The generic keywords associated with the skill that can be used to find a skill.

        - *(string) --*

      - **BulletPoints** *(list) --*

        The details about what the skill supports organized as bullet points.

        - *(string) --*

      - **NewInThisVersionBulletPoints** *(list) --*

        The updates added in bullet points.

        - *(string) --*

      - **SkillTypes** *(list) --*

        The types of skills.

        - *(string) --*

      - **Reviews** *(dict) --*

        The list of reviews for the skill, including Key and Value pair.

        - *(string) --*

          - *(string) --*

      - **DeveloperInfo** *(dict) --*

        The details about the developer that published the skill.

        - **DeveloperName** *(string) --*

          The name of the developer.

        - **PrivacyPolicy** *(string) --*

          The URL of the privacy policy.

        - **Email** *(string) --*

          The email of the developer.

        - **Url** *(string) --*

          The website of the developer.

    - **SupportsLinking** *(boolean) --*

      Linking support for a skill.
    """


_ClientListSkillsStoreSkillsByCategoryResponseTypeDef = TypedDict(
    "_ClientListSkillsStoreSkillsByCategoryResponseTypeDef",
    {
        "SkillsStoreSkills": List[
            ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSkillsStoreSkillsByCategoryResponseTypeDef(
    _ClientListSkillsStoreSkillsByCategoryResponseTypeDef
):
    """
    Type definition for `ClientListSkillsStoreSkillsByCategory` `Response`

    - **SkillsStoreSkills** *(list) --*

      The skill store skills.

      - *(dict) --*

        The detailed information about an Alexa skill.

        - **SkillId** *(string) --*

          The ARN of the skill.

        - **SkillName** *(string) --*

          The name of the skill.

        - **ShortDescription** *(string) --*

          Short description about the skill.

        - **IconUrl** *(string) --*

          The URL where the skill icon resides.

        - **SampleUtterances** *(list) --*

          Sample utterances that interact with the skill.

          - *(string) --*

        - **SkillDetails** *(dict) --*

          Information about the skill.

          - **ProductDescription** *(string) --*

            The description of the product.

          - **InvocationPhrase** *(string) --*

            The phrase used to trigger the skill.

          - **ReleaseDate** *(string) --*

            The date when the skill was released.

          - **EndUserLicenseAgreement** *(string) --*

            The URL of the end user license agreement.

          - **GenericKeywords** *(list) --*

            The generic keywords associated with the skill that can be used to find a skill.

            - *(string) --*

          - **BulletPoints** *(list) --*

            The details about what the skill supports organized as bullet points.

            - *(string) --*

          - **NewInThisVersionBulletPoints** *(list) --*

            The updates added in bullet points.

            - *(string) --*

          - **SkillTypes** *(list) --*

            The types of skills.

            - *(string) --*

          - **Reviews** *(dict) --*

            The list of reviews for the skill, including Key and Value pair.

            - *(string) --*

              - *(string) --*

          - **DeveloperInfo** *(dict) --*

            The details about the developer that published the skill.

            - **DeveloperName** *(string) --*

              The name of the developer.

            - **PrivacyPolicy** *(string) --*

              The URL of the privacy policy.

            - **Email** *(string) --*

              The email of the developer.

            - **Url** *(string) --*

              The website of the developer.

        - **SupportsLinking** *(boolean) --*

          Linking support for a skill.

    - **NextToken** *(string) --*

      The tokens used for pagination.
    """


_ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef = TypedDict(
    "_ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef",
    {"FriendlyName": str, "Description": str, "ManufacturerName": str},
    total=False,
)


class ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef(
    _ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef
):
    """
    Type definition for `ClientListSmartHomeAppliancesResponse` `SmartHomeAppliances`

    A smart home appliance that can connect to a central system. Any domestic device can be a
    smart appliance.

    - **FriendlyName** *(string) --*

      The friendly name of the smart home appliance.

    - **Description** *(string) --*

      The description of the smart home appliance.

    - **ManufacturerName** *(string) --*

      The name of the manufacturer of the smart home appliance.
    """


_ClientListSmartHomeAppliancesResponseTypeDef = TypedDict(
    "_ClientListSmartHomeAppliancesResponseTypeDef",
    {
        "SmartHomeAppliances": List[
            ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSmartHomeAppliancesResponseTypeDef(
    _ClientListSmartHomeAppliancesResponseTypeDef
):
    """
    Type definition for `ClientListSmartHomeAppliances` `Response`

    - **SmartHomeAppliances** *(list) --*

      The smart home appliances.

      - *(dict) --*

        A smart home appliance that can connect to a central system. Any domestic device can be a
        smart appliance.

        - **FriendlyName** *(string) --*

          The friendly name of the smart home appliance.

        - **Description** *(string) --*

          The description of the smart home appliance.

        - **ManufacturerName** *(string) --*

          The name of the manufacturer of the smart home appliance.

    - **NextToken** *(string) --*

      The tokens used for pagination.
    """


_ClientListTagsResponseTagsTypeDef = TypedDict(
    "_ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagsTypeDef(_ClientListTagsResponseTagsTypeDef):
    """
    Type definition for `ClientListTagsResponse` `Tags`

    A key-value pair that can be associated with a resource.

    - **Key** *(string) --*

      The key of a tag. Tag keys are case-sensitive.

    - **Value** *(string) --*

      The value of a tag. Tag values are case-sensitive and can be null.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    Type definition for `ClientListTags` `Response`

    - **Tags** *(list) --*

      The tags requested for the specified resource.

      - *(dict) --*

        A key-value pair that can be associated with a resource.

        - **Key** *(string) --*

          The key of a tag. Tag keys are case-sensitive.

        - **Value** *(string) --*

          The value of a tag. Tag values are case-sensitive and can be null.

    - **NextToken** *(string) --*

      The token returned to indicate that there is more data available.
    """


_ClientPutConferencePreferenceConferencePreferenceTypeDef = TypedDict(
    "_ClientPutConferencePreferenceConferencePreferenceTypeDef",
    {"DefaultConferenceProviderArn": str},
    total=False,
)


class ClientPutConferencePreferenceConferencePreferenceTypeDef(
    _ClientPutConferencePreferenceConferencePreferenceTypeDef
):
    """
    Type definition for `ClientPutConferencePreference` `ConferencePreference`

    The conference preference of a specific conference provider.

    - **DefaultConferenceProviderArn** *(string) --*

      The ARN of the default conference provider.
    """


_ClientPutRoomSkillParameterRoomSkillParameterTypeDef = TypedDict(
    "_ClientPutRoomSkillParameterRoomSkillParameterTypeDef",
    {"ParameterKey": str, "ParameterValue": str},
)


class ClientPutRoomSkillParameterRoomSkillParameterTypeDef(
    _ClientPutRoomSkillParameterRoomSkillParameterTypeDef
):
    """
    Type definition for `ClientPutRoomSkillParameter` `RoomSkillParameter`

    The updated room skill parameter. Required.

    - **ParameterKey** *(string) --* **[REQUIRED]**

      The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes
      “DEFAULT” or “SCOPE” as valid values.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      The parameter value of a room skill parameter.
    """


_ClientRegisterAvsDeviceResponseTypeDef = TypedDict(
    "_ClientRegisterAvsDeviceResponseTypeDef", {"DeviceArn": str}, total=False
)


class ClientRegisterAvsDeviceResponseTypeDef(_ClientRegisterAvsDeviceResponseTypeDef):
    """
    Type definition for `ClientRegisterAvsDevice` `Response`

    - **DeviceArn** *(string) --*

      The ARN of the device.
    """


_ClientResolveRoomResponseRoomSkillParametersTypeDef = TypedDict(
    "_ClientResolveRoomResponseRoomSkillParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str},
    total=False,
)


class ClientResolveRoomResponseRoomSkillParametersTypeDef(
    _ClientResolveRoomResponseRoomSkillParametersTypeDef
):
    """
    Type definition for `ClientResolveRoomResponse` `RoomSkillParameters`

    A skill parameter associated with a room.

    - **ParameterKey** *(string) --*

      The parameter key of a room skill parameter. ParameterKey is an enumerated type that only
      takes “DEFAULT” or “SCOPE” as valid values.

    - **ParameterValue** *(string) --*

      The parameter value of a room skill parameter.
    """


_ClientResolveRoomResponseTypeDef = TypedDict(
    "_ClientResolveRoomResponseTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "RoomSkillParameters": List[
            ClientResolveRoomResponseRoomSkillParametersTypeDef
        ],
    },
    total=False,
)


class ClientResolveRoomResponseTypeDef(_ClientResolveRoomResponseTypeDef):
    """
    Type definition for `ClientResolveRoom` `Response`

    - **RoomArn** *(string) --*

      The ARN of the room from which the skill request was invoked.

    - **RoomName** *(string) --*

      The name of the room from which the skill request was invoked.

    - **RoomSkillParameters** *(list) --*

      Response to get the room profile request. Required.

      - *(dict) --*

        A skill parameter associated with a room.

        - **ParameterKey** *(string) --*

          The parameter key of a room skill parameter. ParameterKey is an enumerated type that only
          takes “DEFAULT” or “SCOPE” as valid values.

        - **ParameterValue** *(string) --*

          The parameter value of a room skill parameter.
    """


_ClientSearchAddressBooksFiltersTypeDef = TypedDict(
    "_ClientSearchAddressBooksFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class ClientSearchAddressBooksFiltersTypeDef(_ClientSearchAddressBooksFiltersTypeDef):
    """
    Type definition for `ClientSearchAddressBooks` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_ClientSearchAddressBooksResponseAddressBooksTypeDef = TypedDict(
    "_ClientSearchAddressBooksResponseAddressBooksTypeDef",
    {"AddressBookArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientSearchAddressBooksResponseAddressBooksTypeDef(
    _ClientSearchAddressBooksResponseAddressBooksTypeDef
):
    """
    Type definition for `ClientSearchAddressBooksResponse` `AddressBooks`

    Information related to an address book.

    - **AddressBookArn** *(string) --*

      The ARN of the address book.

    - **Name** *(string) --*

      The name of the address book.

    - **Description** *(string) --*

      The description of the address book.
    """


_ClientSearchAddressBooksResponseTypeDef = TypedDict(
    "_ClientSearchAddressBooksResponseTypeDef",
    {
        "AddressBooks": List[ClientSearchAddressBooksResponseAddressBooksTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchAddressBooksResponseTypeDef(_ClientSearchAddressBooksResponseTypeDef):
    """
    Type definition for `ClientSearchAddressBooks` `Response`

    - **AddressBooks** *(list) --*

      The address books that meet the specified set of filter criteria, in sort order.

      - *(dict) --*

        Information related to an address book.

        - **AddressBookArn** *(string) --*

          The ARN of the address book.

        - **Name** *(string) --*

          The name of the address book.

        - **Description** *(string) --*

          The description of the address book.

    - **NextToken** *(string) --*

      The token returned to indicate that there is more data available.

    - **TotalCount** *(integer) --*

      The total number of address books returned.
    """


_ClientSearchAddressBooksSortCriteriaTypeDef = TypedDict(
    "_ClientSearchAddressBooksSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class ClientSearchAddressBooksSortCriteriaTypeDef(
    _ClientSearchAddressBooksSortCriteriaTypeDef
):
    """
    Type definition for `ClientSearchAddressBooks` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_ClientSearchContactsFiltersTypeDef = TypedDict(
    "_ClientSearchContactsFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class ClientSearchContactsFiltersTypeDef(_ClientSearchContactsFiltersTypeDef):
    """
    Type definition for `ClientSearchContacts` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_ClientSearchContactsResponseContactsPhoneNumbersTypeDef = TypedDict(
    "_ClientSearchContactsResponseContactsPhoneNumbersTypeDef",
    {"Number": str, "Type": str},
    total=False,
)


class ClientSearchContactsResponseContactsPhoneNumbersTypeDef(
    _ClientSearchContactsResponseContactsPhoneNumbersTypeDef
):
    """
    Type definition for `ClientSearchContactsResponseContacts` `PhoneNumbers`

    The phone number for the contact containing the raw number and phone number type.

    - **Number** *(string) --*

      The raw value of the phone number.

    - **Type** *(string) --*

      The type of the phone number.
    """


_ClientSearchContactsResponseContactsSipAddressesTypeDef = TypedDict(
    "_ClientSearchContactsResponseContactsSipAddressesTypeDef",
    {"Uri": str, "Type": str},
    total=False,
)


class ClientSearchContactsResponseContactsSipAddressesTypeDef(
    _ClientSearchContactsResponseContactsSipAddressesTypeDef
):
    """
    Type definition for `ClientSearchContactsResponseContacts` `SipAddresses`

    The SIP address for the contact containing the URI and SIP address type.

    - **Uri** *(string) --*

      The URI for the SIP address.

    - **Type** *(string) --*

      The type of the SIP address.
    """


_ClientSearchContactsResponseContactsTypeDef = TypedDict(
    "_ClientSearchContactsResponseContactsTypeDef",
    {
        "ContactArn": str,
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List[ClientSearchContactsResponseContactsPhoneNumbersTypeDef],
        "SipAddresses": List[ClientSearchContactsResponseContactsSipAddressesTypeDef],
    },
    total=False,
)


class ClientSearchContactsResponseContactsTypeDef(
    _ClientSearchContactsResponseContactsTypeDef
):
    """
    Type definition for `ClientSearchContactsResponse` `Contacts`

    Information related to a contact.

    - **ContactArn** *(string) --*

      The ARN of the contact.

    - **DisplayName** *(string) --*

      The name of the contact to display on the console.

    - **FirstName** *(string) --*

      The first name of the contact, used to call the contact on the device.

    - **LastName** *(string) --*

      The last name of the contact, used to call the contact on the device.

    - **PhoneNumber** *(string) --*

      The phone number of the contact. The phone number type defaults to WORK. You can specify
      PhoneNumber or PhoneNumbers. We recommend that you use PhoneNumbers, which lets you
      specify the phone number type and multiple numbers.

    - **PhoneNumbers** *(list) --*

      The list of phone numbers for the contact.

      - *(dict) --*

        The phone number for the contact containing the raw number and phone number type.

        - **Number** *(string) --*

          The raw value of the phone number.

        - **Type** *(string) --*

          The type of the phone number.

    - **SipAddresses** *(list) --*

      The list of SIP addresses for the contact.

      - *(dict) --*

        The SIP address for the contact containing the URI and SIP address type.

        - **Uri** *(string) --*

          The URI for the SIP address.

        - **Type** *(string) --*

          The type of the SIP address.
    """


_ClientSearchContactsResponseTypeDef = TypedDict(
    "_ClientSearchContactsResponseTypeDef",
    {
        "Contacts": List[ClientSearchContactsResponseContactsTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchContactsResponseTypeDef(_ClientSearchContactsResponseTypeDef):
    """
    Type definition for `ClientSearchContacts` `Response`

    - **Contacts** *(list) --*

      The contacts that meet the specified set of filter criteria, in sort order.

      - *(dict) --*

        Information related to a contact.

        - **ContactArn** *(string) --*

          The ARN of the contact.

        - **DisplayName** *(string) --*

          The name of the contact to display on the console.

        - **FirstName** *(string) --*

          The first name of the contact, used to call the contact on the device.

        - **LastName** *(string) --*

          The last name of the contact, used to call the contact on the device.

        - **PhoneNumber** *(string) --*

          The phone number of the contact. The phone number type defaults to WORK. You can specify
          PhoneNumber or PhoneNumbers. We recommend that you use PhoneNumbers, which lets you
          specify the phone number type and multiple numbers.

        - **PhoneNumbers** *(list) --*

          The list of phone numbers for the contact.

          - *(dict) --*

            The phone number for the contact containing the raw number and phone number type.

            - **Number** *(string) --*

              The raw value of the phone number.

            - **Type** *(string) --*

              The type of the phone number.

        - **SipAddresses** *(list) --*

          The list of SIP addresses for the contact.

          - *(dict) --*

            The SIP address for the contact containing the URI and SIP address type.

            - **Uri** *(string) --*

              The URI for the SIP address.

            - **Type** *(string) --*

              The type of the SIP address.

    - **NextToken** *(string) --*

      The token returned to indicate that there is more data available.

    - **TotalCount** *(integer) --*

      The total number of contacts returned.
    """


_ClientSearchContactsSortCriteriaTypeDef = TypedDict(
    "_ClientSearchContactsSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class ClientSearchContactsSortCriteriaTypeDef(_ClientSearchContactsSortCriteriaTypeDef):
    """
    Type definition for `ClientSearchContacts` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_ClientSearchDevicesFiltersTypeDef = TypedDict(
    "_ClientSearchDevicesFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class ClientSearchDevicesFiltersTypeDef(_ClientSearchDevicesFiltersTypeDef):
    """
    Type definition for `ClientSearchDevices` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef = TypedDict(
    "_ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef",
    {"Feature": str, "Code": str},
    total=False,
)


class ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef(
    _ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef
):
    """
    Type definition for `ClientSearchDevicesResponseDevicesDeviceStatusInfo` `DeviceStatusDetails`

    Details of a device’s status.

    - **Feature** *(string) --*

      The list of available features on the device.

    - **Code** *(string) --*

      The device status detail code.
    """


_ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef = TypedDict(
    "_ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List[
            ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef
        ],
        "ConnectionStatus": str,
    },
    total=False,
)


class ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef(
    _ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef
):
    """
    Type definition for `ClientSearchDevicesResponseDevices` `DeviceStatusInfo`

    Detailed information about a device's status.

    - **DeviceStatusDetails** *(list) --*

      One or more device status detail descriptions.

      - *(dict) --*

        Details of a device’s status.

        - **Feature** *(string) --*

          The list of available features on the device.

        - **Code** *(string) --*

          The device status detail code.

    - **ConnectionStatus** *(string) --*

      The latest available information about the connection status of a device.
    """


_ClientSearchDevicesResponseDevicesTypeDef = TypedDict(
    "_ClientSearchDevicesResponseDevicesTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "DeviceStatus": str,
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "RoomArn": str,
        "RoomName": str,
        "DeviceStatusInfo": ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef,
    },
    total=False,
)


class ClientSearchDevicesResponseDevicesTypeDef(
    _ClientSearchDevicesResponseDevicesTypeDef
):
    """
    Type definition for `ClientSearchDevicesResponse` `Devices`

    Device attributes.

    - **DeviceArn** *(string) --*

      The ARN of a device.

    - **DeviceSerialNumber** *(string) --*

      The serial number of a device.

    - **DeviceType** *(string) --*

      The type of a device.

    - **DeviceName** *(string) --*

      The name of a device.

    - **SoftwareVersion** *(string) --*

      The software version of a device.

    - **MacAddress** *(string) --*

      The MAC address of a device.

    - **DeviceStatus** *(string) --*

      The status of a device.

    - **NetworkProfileArn** *(string) --*

      The ARN of the network profile associated with a device.

    - **NetworkProfileName** *(string) --*

      The name of the network profile associated with a device.

    - **RoomArn** *(string) --*

      The room ARN associated with a device.

    - **RoomName** *(string) --*

      The name of the room associated with a device.

    - **DeviceStatusInfo** *(dict) --*

      Detailed information about a device's status.

      - **DeviceStatusDetails** *(list) --*

        One or more device status detail descriptions.

        - *(dict) --*

          Details of a device’s status.

          - **Feature** *(string) --*

            The list of available features on the device.

          - **Code** *(string) --*

            The device status detail code.

      - **ConnectionStatus** *(string) --*

        The latest available information about the connection status of a device.
    """


_ClientSearchDevicesResponseTypeDef = TypedDict(
    "_ClientSearchDevicesResponseTypeDef",
    {
        "Devices": List[ClientSearchDevicesResponseDevicesTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchDevicesResponseTypeDef(_ClientSearchDevicesResponseTypeDef):
    """
    Type definition for `ClientSearchDevices` `Response`

    - **Devices** *(list) --*

      The devices that meet the specified set of filter criteria, in sort order.

      - *(dict) --*

        Device attributes.

        - **DeviceArn** *(string) --*

          The ARN of a device.

        - **DeviceSerialNumber** *(string) --*

          The serial number of a device.

        - **DeviceType** *(string) --*

          The type of a device.

        - **DeviceName** *(string) --*

          The name of a device.

        - **SoftwareVersion** *(string) --*

          The software version of a device.

        - **MacAddress** *(string) --*

          The MAC address of a device.

        - **DeviceStatus** *(string) --*

          The status of a device.

        - **NetworkProfileArn** *(string) --*

          The ARN of the network profile associated with a device.

        - **NetworkProfileName** *(string) --*

          The name of the network profile associated with a device.

        - **RoomArn** *(string) --*

          The room ARN associated with a device.

        - **RoomName** *(string) --*

          The name of the room associated with a device.

        - **DeviceStatusInfo** *(dict) --*

          Detailed information about a device's status.

          - **DeviceStatusDetails** *(list) --*

            One or more device status detail descriptions.

            - *(dict) --*

              Details of a device’s status.

              - **Feature** *(string) --*

                The list of available features on the device.

              - **Code** *(string) --*

                The device status detail code.

          - **ConnectionStatus** *(string) --*

            The latest available information about the connection status of a device.

    - **NextToken** *(string) --*

      The token returned to indicate that there is more data available.

    - **TotalCount** *(integer) --*

      The total number of devices returned.
    """


_ClientSearchDevicesSortCriteriaTypeDef = TypedDict(
    "_ClientSearchDevicesSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class ClientSearchDevicesSortCriteriaTypeDef(_ClientSearchDevicesSortCriteriaTypeDef):
    """
    Type definition for `ClientSearchDevices` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_ClientSearchNetworkProfilesFiltersTypeDef = TypedDict(
    "_ClientSearchNetworkProfilesFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class ClientSearchNetworkProfilesFiltersTypeDef(
    _ClientSearchNetworkProfilesFiltersTypeDef
):
    """
    Type definition for `ClientSearchNetworkProfiles` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef = TypedDict(
    "_ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "Description": str,
        "Ssid": str,
        "SecurityType": str,
        "EapMethod": str,
        "CertificateAuthorityArn": str,
    },
    total=False,
)


class ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef(
    _ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef
):
    """
    Type definition for `ClientSearchNetworkProfilesResponse` `NetworkProfiles`

    The data associated with a network profile.

    - **NetworkProfileArn** *(string) --*

      The ARN of the network profile associated with a device.

    - **NetworkProfileName** *(string) --*

      The name of the network profile associated with a device.

    - **Description** *(string) --*

      Detailed information about a device's network profile.

    - **Ssid** *(string) --*

      The SSID of the Wi-Fi network.

    - **SecurityType** *(string) --*

      The security type of the Wi-Fi network. This can be WPA2_ENTERPRISE, WPA2_PSK, WPA_PSK,
      WEP, or OPEN.

    - **EapMethod** *(string) --*

      The authentication standard that is used in the EAP framework. Currently, EAP_TLS is
      supported.

    - **CertificateAuthorityArn** *(string) --*

      The ARN of the Private Certificate Authority (PCA) created in AWS Certificate Manager
      (ACM). This is used to issue certificates to the devices.
    """


_ClientSearchNetworkProfilesResponseTypeDef = TypedDict(
    "_ClientSearchNetworkProfilesResponseTypeDef",
    {
        "NetworkProfiles": List[
            ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef
        ],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchNetworkProfilesResponseTypeDef(
    _ClientSearchNetworkProfilesResponseTypeDef
):
    """
    Type definition for `ClientSearchNetworkProfiles` `Response`

    - **NetworkProfiles** *(list) --*

      The network profiles that meet the specified set of filter criteria, in sort order. It is a
      list of NetworkProfileData objects.

      - *(dict) --*

        The data associated with a network profile.

        - **NetworkProfileArn** *(string) --*

          The ARN of the network profile associated with a device.

        - **NetworkProfileName** *(string) --*

          The name of the network profile associated with a device.

        - **Description** *(string) --*

          Detailed information about a device's network profile.

        - **Ssid** *(string) --*

          The SSID of the Wi-Fi network.

        - **SecurityType** *(string) --*

          The security type of the Wi-Fi network. This can be WPA2_ENTERPRISE, WPA2_PSK, WPA_PSK,
          WEP, or OPEN.

        - **EapMethod** *(string) --*

          The authentication standard that is used in the EAP framework. Currently, EAP_TLS is
          supported.

        - **CertificateAuthorityArn** *(string) --*

          The ARN of the Private Certificate Authority (PCA) created in AWS Certificate Manager
          (ACM). This is used to issue certificates to the devices.

    - **NextToken** *(string) --*

      An optional token returned from a prior request. Use this token for pagination of results
      from this action. If this parameter is specified, the response includes only results beyond
      the token, up to the value specified by MaxResults.

    - **TotalCount** *(integer) --*

      The total number of network profiles returned.
    """


_ClientSearchNetworkProfilesSortCriteriaTypeDef = TypedDict(
    "_ClientSearchNetworkProfilesSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class ClientSearchNetworkProfilesSortCriteriaTypeDef(
    _ClientSearchNetworkProfilesSortCriteriaTypeDef
):
    """
    Type definition for `ClientSearchNetworkProfiles` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_ClientSearchProfilesFiltersTypeDef = TypedDict(
    "_ClientSearchProfilesFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class ClientSearchProfilesFiltersTypeDef(_ClientSearchProfilesFiltersTypeDef):
    """
    Type definition for `ClientSearchProfiles` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_ClientSearchProfilesResponseProfilesTypeDef = TypedDict(
    "_ClientSearchProfilesResponseProfilesTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": str,
        "TemperatureUnit": str,
        "WakeWord": str,
        "Locale": str,
    },
    total=False,
)


class ClientSearchProfilesResponseProfilesTypeDef(
    _ClientSearchProfilesResponseProfilesTypeDef
):
    """
    Type definition for `ClientSearchProfilesResponse` `Profiles`

    The data of a room profile.

    - **ProfileArn** *(string) --*

      The ARN of a room profile.

    - **ProfileName** *(string) --*

      The name of a room profile.

    - **IsDefault** *(boolean) --*

      Retrieves if the profile data is default or not.

    - **Address** *(string) --*

      The address of a room profile.

    - **Timezone** *(string) --*

      The timezone of a room profile.

    - **DistanceUnit** *(string) --*

      The distance unit of a room profile.

    - **TemperatureUnit** *(string) --*

      The temperature unit of a room profile.

    - **WakeWord** *(string) --*

      The wake word of a room profile.

    - **Locale** *(string) --*

      The locale of a room profile.
    """


_ClientSearchProfilesResponseTypeDef = TypedDict(
    "_ClientSearchProfilesResponseTypeDef",
    {
        "Profiles": List[ClientSearchProfilesResponseProfilesTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchProfilesResponseTypeDef(_ClientSearchProfilesResponseTypeDef):
    """
    Type definition for `ClientSearchProfiles` `Response`

    - **Profiles** *(list) --*

      The profiles that meet the specified set of filter criteria, in sort order.

      - *(dict) --*

        The data of a room profile.

        - **ProfileArn** *(string) --*

          The ARN of a room profile.

        - **ProfileName** *(string) --*

          The name of a room profile.

        - **IsDefault** *(boolean) --*

          Retrieves if the profile data is default or not.

        - **Address** *(string) --*

          The address of a room profile.

        - **Timezone** *(string) --*

          The timezone of a room profile.

        - **DistanceUnit** *(string) --*

          The distance unit of a room profile.

        - **TemperatureUnit** *(string) --*

          The temperature unit of a room profile.

        - **WakeWord** *(string) --*

          The wake word of a room profile.

        - **Locale** *(string) --*

          The locale of a room profile.

    - **NextToken** *(string) --*

      The token returned to indicate that there is more data available.

    - **TotalCount** *(integer) --*

      The total number of room profiles returned.
    """


_ClientSearchProfilesSortCriteriaTypeDef = TypedDict(
    "_ClientSearchProfilesSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class ClientSearchProfilesSortCriteriaTypeDef(_ClientSearchProfilesSortCriteriaTypeDef):
    """
    Type definition for `ClientSearchProfiles` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_ClientSearchRoomsFiltersTypeDef = TypedDict(
    "_ClientSearchRoomsFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class ClientSearchRoomsFiltersTypeDef(_ClientSearchRoomsFiltersTypeDef):
    """
    Type definition for `ClientSearchRooms` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_ClientSearchRoomsResponseRoomsTypeDef = TypedDict(
    "_ClientSearchRoomsResponseRoomsTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
        "ProfileName": str,
    },
    total=False,
)


class ClientSearchRoomsResponseRoomsTypeDef(_ClientSearchRoomsResponseRoomsTypeDef):
    """
    Type definition for `ClientSearchRoomsResponse` `Rooms`

    The data of a room.

    - **RoomArn** *(string) --*

      The ARN of a room.

    - **RoomName** *(string) --*

      The name of a room.

    - **Description** *(string) --*

      The description of a room.

    - **ProviderCalendarId** *(string) --*

      The provider calendar ARN of a room.

    - **ProfileArn** *(string) --*

      The profile ARN of a room.

    - **ProfileName** *(string) --*

      The profile name of a room.
    """


_ClientSearchRoomsResponseTypeDef = TypedDict(
    "_ClientSearchRoomsResponseTypeDef",
    {
        "Rooms": List[ClientSearchRoomsResponseRoomsTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchRoomsResponseTypeDef(_ClientSearchRoomsResponseTypeDef):
    """
    Type definition for `ClientSearchRooms` `Response`

    - **Rooms** *(list) --*

      The rooms that meet the specified set of filter criteria, in sort order.

      - *(dict) --*

        The data of a room.

        - **RoomArn** *(string) --*

          The ARN of a room.

        - **RoomName** *(string) --*

          The name of a room.

        - **Description** *(string) --*

          The description of a room.

        - **ProviderCalendarId** *(string) --*

          The provider calendar ARN of a room.

        - **ProfileArn** *(string) --*

          The profile ARN of a room.

        - **ProfileName** *(string) --*

          The profile name of a room.

    - **NextToken** *(string) --*

      The token returned to indicate that there is more data available.

    - **TotalCount** *(integer) --*

      The total number of rooms returned.
    """


_ClientSearchRoomsSortCriteriaTypeDef = TypedDict(
    "_ClientSearchRoomsSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class ClientSearchRoomsSortCriteriaTypeDef(_ClientSearchRoomsSortCriteriaTypeDef):
    """
    Type definition for `ClientSearchRooms` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_ClientSearchSkillGroupsFiltersTypeDef = TypedDict(
    "_ClientSearchSkillGroupsFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class ClientSearchSkillGroupsFiltersTypeDef(_ClientSearchSkillGroupsFiltersTypeDef):
    """
    Type definition for `ClientSearchSkillGroups` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_ClientSearchSkillGroupsResponseSkillGroupsTypeDef = TypedDict(
    "_ClientSearchSkillGroupsResponseSkillGroupsTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)


class ClientSearchSkillGroupsResponseSkillGroupsTypeDef(
    _ClientSearchSkillGroupsResponseSkillGroupsTypeDef
):
    """
    Type definition for `ClientSearchSkillGroupsResponse` `SkillGroups`

    The attributes of a skill group.

    - **SkillGroupArn** *(string) --*

      The skill group ARN of a skill group.

    - **SkillGroupName** *(string) --*

      The skill group name of a skill group.

    - **Description** *(string) --*

      The description of a skill group.
    """


_ClientSearchSkillGroupsResponseTypeDef = TypedDict(
    "_ClientSearchSkillGroupsResponseTypeDef",
    {
        "SkillGroups": List[ClientSearchSkillGroupsResponseSkillGroupsTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchSkillGroupsResponseTypeDef(_ClientSearchSkillGroupsResponseTypeDef):
    """
    Type definition for `ClientSearchSkillGroups` `Response`

    - **SkillGroups** *(list) --*

      The skill groups that meet the filter criteria, in sort order.

      - *(dict) --*

        The attributes of a skill group.

        - **SkillGroupArn** *(string) --*

          The skill group ARN of a skill group.

        - **SkillGroupName** *(string) --*

          The skill group name of a skill group.

        - **Description** *(string) --*

          The description of a skill group.

    - **NextToken** *(string) --*

      The token returned to indicate that there is more data available.

    - **TotalCount** *(integer) --*

      The total number of skill groups returned.
    """


_ClientSearchSkillGroupsSortCriteriaTypeDef = TypedDict(
    "_ClientSearchSkillGroupsSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class ClientSearchSkillGroupsSortCriteriaTypeDef(
    _ClientSearchSkillGroupsSortCriteriaTypeDef
):
    """
    Type definition for `ClientSearchSkillGroups` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_ClientSearchUsersFiltersTypeDef = TypedDict(
    "_ClientSearchUsersFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class ClientSearchUsersFiltersTypeDef(_ClientSearchUsersFiltersTypeDef):
    """
    Type definition for `ClientSearchUsers` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_ClientSearchUsersResponseUsersTypeDef = TypedDict(
    "_ClientSearchUsersResponseUsersTypeDef",
    {
        "UserArn": str,
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "EnrollmentStatus": str,
        "EnrollmentId": str,
    },
    total=False,
)


class ClientSearchUsersResponseUsersTypeDef(_ClientSearchUsersResponseUsersTypeDef):
    """
    Type definition for `ClientSearchUsersResponse` `Users`

    Information related to a user.

    - **UserArn** *(string) --*

      The ARN of a user.

    - **FirstName** *(string) --*

      The first name of a user.

    - **LastName** *(string) --*

      The last name of a user.

    - **Email** *(string) --*

      The email of a user.

    - **EnrollmentStatus** *(string) --*

      The enrollment status of a user.

    - **EnrollmentId** *(string) --*

      The enrollment ARN of a user.
    """


_ClientSearchUsersResponseTypeDef = TypedDict(
    "_ClientSearchUsersResponseTypeDef",
    {
        "Users": List[ClientSearchUsersResponseUsersTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchUsersResponseTypeDef(_ClientSearchUsersResponseTypeDef):
    """
    Type definition for `ClientSearchUsers` `Response`

    - **Users** *(list) --*

      The users that meet the specified set of filter criteria, in sort order.

      - *(dict) --*

        Information related to a user.

        - **UserArn** *(string) --*

          The ARN of a user.

        - **FirstName** *(string) --*

          The first name of a user.

        - **LastName** *(string) --*

          The last name of a user.

        - **Email** *(string) --*

          The email of a user.

        - **EnrollmentStatus** *(string) --*

          The enrollment status of a user.

        - **EnrollmentId** *(string) --*

          The enrollment ARN of a user.

    - **NextToken** *(string) --*

      The token returned to indicate that there is more data available.

    - **TotalCount** *(integer) --*

      The total number of users returned.
    """


_ClientSearchUsersSortCriteriaTypeDef = TypedDict(
    "_ClientSearchUsersSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class ClientSearchUsersSortCriteriaTypeDef(_ClientSearchUsersSortCriteriaTypeDef):
    """
    Type definition for `ClientSearchUsers` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_ClientSendAnnouncementContentAudioListTypeDef = TypedDict(
    "_ClientSendAnnouncementContentAudioListTypeDef", {"Locale": str, "Location": str}
)


class ClientSendAnnouncementContentAudioListTypeDef(
    _ClientSendAnnouncementContentAudioListTypeDef
):
    """
    Type definition for `ClientSendAnnouncementContent` `AudioList`

    The audio message. There is a 1 MB limit on the audio file input and the only supported
    format is MP3. To convert your MP3 audio files to an Alexa-friendly,

    required codec version (MPEG version 2) and bit rate (48 kbps), you might use converter
    software. One option for this is a command-line tool, FFmpeg. For more information, see
    `FFmpeg <https://www.ffmpeg.org/>`__ . The following command converts the provided
    <input-file> to an MP3 file that is played in the announcement:

     ``ffmpeg -i <input-file> -ac 2 -codec:a libmp3lame -b:a 48k -ar 16000 <output-file.mp3>``

    - **Locale** *(string) --* **[REQUIRED]**

      The locale of the audio message. Currently, en-US is supported.

    - **Location** *(string) --* **[REQUIRED]**

      The location of the audio file. Currently, S3 URLs are supported. Only S3 locations
      comprised of safe characters are valid. For more information, see `Safe Characters
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#Safe%20Characters>`__ .
    """


_ClientSendAnnouncementContentSsmlListTypeDef = TypedDict(
    "_ClientSendAnnouncementContentSsmlListTypeDef", {"Locale": str, "Value": str}
)


class ClientSendAnnouncementContentSsmlListTypeDef(
    _ClientSendAnnouncementContentSsmlListTypeDef
):
    """
    Type definition for `ClientSendAnnouncementContent` `SsmlList`

    The SSML message. For more information, see `SSML Reference
    <https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html>`__
    .

    - **Locale** *(string) --* **[REQUIRED]**

      The locale of the SSML message. Currently, en-US is supported.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the SSML message in the correct SSML format. The audio tag is not supported.
    """


_ClientSendAnnouncementContentTextListTypeDef = TypedDict(
    "_ClientSendAnnouncementContentTextListTypeDef", {"Locale": str, "Value": str}
)


class ClientSendAnnouncementContentTextListTypeDef(
    _ClientSendAnnouncementContentTextListTypeDef
):
    """
    Type definition for `ClientSendAnnouncementContent` `TextList`

    The text message.

    - **Locale** *(string) --* **[REQUIRED]**

      The locale of the text message. Currently, en-US is supported.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the text message.
    """


_ClientSendAnnouncementContentTypeDef = TypedDict(
    "_ClientSendAnnouncementContentTypeDef",
    {
        "TextList": List[ClientSendAnnouncementContentTextListTypeDef],
        "SsmlList": List[ClientSendAnnouncementContentSsmlListTypeDef],
        "AudioList": List[ClientSendAnnouncementContentAudioListTypeDef],
    },
    total=False,
)


class ClientSendAnnouncementContentTypeDef(_ClientSendAnnouncementContentTypeDef):
    """
    Type definition for `ClientSendAnnouncement` `Content`

    The announcement content. This can contain only one of the three possible announcement types
    (text, SSML or audio).

    - **TextList** *(list) --*

      The list of text messages.

      - *(dict) --*

        The text message.

        - **Locale** *(string) --* **[REQUIRED]**

          The locale of the text message. Currently, en-US is supported.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the text message.

    - **SsmlList** *(list) --*

      The list of SSML messages.

      - *(dict) --*

        The SSML message. For more information, see `SSML Reference
        <https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html>`__
        .

        - **Locale** *(string) --* **[REQUIRED]**

          The locale of the SSML message. Currently, en-US is supported.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the SSML message in the correct SSML format. The audio tag is not supported.

    - **AudioList** *(list) --*

      The list of audio messages.

      - *(dict) --*

        The audio message. There is a 1 MB limit on the audio file input and the only supported
        format is MP3. To convert your MP3 audio files to an Alexa-friendly,

        required codec version (MPEG version 2) and bit rate (48 kbps), you might use converter
        software. One option for this is a command-line tool, FFmpeg. For more information, see
        `FFmpeg <https://www.ffmpeg.org/>`__ . The following command converts the provided
        <input-file> to an MP3 file that is played in the announcement:

         ``ffmpeg -i <input-file> -ac 2 -codec:a libmp3lame -b:a 48k -ar 16000 <output-file.mp3>``

        - **Locale** *(string) --* **[REQUIRED]**

          The locale of the audio message. Currently, en-US is supported.

        - **Location** *(string) --* **[REQUIRED]**

          The location of the audio file. Currently, S3 URLs are supported. Only S3 locations
          comprised of safe characters are valid. For more information, see `Safe Characters
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#Safe%20Characters>`__ .
    """


_ClientSendAnnouncementResponseTypeDef = TypedDict(
    "_ClientSendAnnouncementResponseTypeDef", {"AnnouncementArn": str}, total=False
)


class ClientSendAnnouncementResponseTypeDef(_ClientSendAnnouncementResponseTypeDef):
    """
    Type definition for `ClientSendAnnouncement` `Response`

    - **AnnouncementArn** *(string) --*

      The identifier of the announcement.
    """


_ClientSendAnnouncementRoomFiltersTypeDef = TypedDict(
    "_ClientSendAnnouncementRoomFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class ClientSendAnnouncementRoomFiltersTypeDef(
    _ClientSendAnnouncementRoomFiltersTypeDef
):
    """
    Type definition for `ClientSendAnnouncement` `RoomFilters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    A key-value pair that can be associated with a resource.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a tag. Tag keys are case-sensitive.

    - **Value** *(string) --* **[REQUIRED]**

      The value of a tag. Tag values are case-sensitive and can be null.
    """


_ClientUpdateBusinessReportScheduleRecurrenceTypeDef = TypedDict(
    "_ClientUpdateBusinessReportScheduleRecurrenceTypeDef",
    {"StartDate": str},
    total=False,
)


class ClientUpdateBusinessReportScheduleRecurrenceTypeDef(
    _ClientUpdateBusinessReportScheduleRecurrenceTypeDef
):
    """
    Type definition for `ClientUpdateBusinessReportSchedule` `Recurrence`

    The recurrence of the reports.

    - **StartDate** *(string) --*

      The start date.
    """


_ClientUpdateConferenceProviderIPDialInTypeDef = TypedDict(
    "_ClientUpdateConferenceProviderIPDialInTypeDef",
    {"Endpoint": str, "CommsProtocol": str},
)


class ClientUpdateConferenceProviderIPDialInTypeDef(
    _ClientUpdateConferenceProviderIPDialInTypeDef
):
    """
    Type definition for `ClientUpdateConferenceProvider` `IPDialIn`

    The IP endpoint and protocol for calling.

    - **Endpoint** *(string) --* **[REQUIRED]**

      The IP address.

    - **CommsProtocol** *(string) --* **[REQUIRED]**

      The protocol, including SIP, SIPS, and H323.
    """


_ClientUpdateConferenceProviderMeetingSettingTypeDef = TypedDict(
    "_ClientUpdateConferenceProviderMeetingSettingTypeDef", {"RequirePin": str}
)


class ClientUpdateConferenceProviderMeetingSettingTypeDef(
    _ClientUpdateConferenceProviderMeetingSettingTypeDef
):
    """
    Type definition for `ClientUpdateConferenceProvider` `MeetingSetting`

    The meeting settings for the conference provider.

    - **RequirePin** *(string) --* **[REQUIRED]**

      The values that indicate whether the pin is always required.
    """


_ClientUpdateConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_ClientUpdateConferenceProviderPSTNDialInTypeDef",
    {
        "CountryCode": str,
        "PhoneNumber": str,
        "OneClickIdDelay": str,
        "OneClickPinDelay": str,
    },
)


class ClientUpdateConferenceProviderPSTNDialInTypeDef(
    _ClientUpdateConferenceProviderPSTNDialInTypeDef
):
    """
    Type definition for `ClientUpdateConferenceProvider` `PSTNDialIn`

    The information for PSTN conferencing.

    - **CountryCode** *(string) --* **[REQUIRED]**

      The zip code.

    - **PhoneNumber** *(string) --* **[REQUIRED]**

      The phone number to call to join the conference.

    - **OneClickIdDelay** *(string) --* **[REQUIRED]**

      The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF).
      Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the
      telephone network.

    - **OneClickPinDelay** *(string) --* **[REQUIRED]**

      The delay duration before Alexa enters the conference pin with dual-tone multi-frequency
      (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over
      the telephone network.
    """


_ClientUpdateContactPhoneNumbersTypeDef = TypedDict(
    "_ClientUpdateContactPhoneNumbersTypeDef", {"Number": str, "Type": str}
)


class ClientUpdateContactPhoneNumbersTypeDef(_ClientUpdateContactPhoneNumbersTypeDef):
    """
    Type definition for `ClientUpdateContact` `PhoneNumbers`

    The phone number for the contact containing the raw number and phone number type.

    - **Number** *(string) --* **[REQUIRED]**

      The raw value of the phone number.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the phone number.
    """


_ClientUpdateContactSipAddressesTypeDef = TypedDict(
    "_ClientUpdateContactSipAddressesTypeDef", {"Uri": str, "Type": str}
)


class ClientUpdateContactSipAddressesTypeDef(_ClientUpdateContactSipAddressesTypeDef):
    """
    Type definition for `ClientUpdateContact` `SipAddresses`

    The SIP address for the contact containing the URI and SIP address type.

    - **Uri** *(string) --* **[REQUIRED]**

      The URI for the SIP address.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the SIP address.
    """


_ListBusinessReportSchedulesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBusinessReportSchedulesPaginatePaginationConfigTypeDef(
    _ListBusinessReportSchedulesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBusinessReportSchedulesPaginate` `PaginationConfig`

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


_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef",
    {"Interval": str},
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef(
    _ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef
):
    """
    Type definition for `ListBusinessReportSchedulesPaginateResponseBusinessReportSchedules` `ContentRange`

    The content range of the reports.

    - **Interval** *(string) --*

      The interval of the content range.
    """


_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef",
    {"Path": str, "BucketName": str},
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef(
    _ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef
):
    """
    Type definition for `ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReport` `S3Location`

    The S3 location of the output reports.

    - **Path** *(string) --*

      The path of the business report.

    - **BucketName** *(string) --*

      The S3 bucket name of the output reports.
    """


_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef",
    {
        "Status": str,
        "FailureCode": str,
        "S3Location": ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef,
        "DeliveryTime": datetime,
        "DownloadUrl": str,
    },
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef(
    _ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef
):
    """
    Type definition for `ListBusinessReportSchedulesPaginateResponseBusinessReportSchedules` `LastBusinessReport`

    The details of the last business report delivery for a specified time interval.

    - **Status** *(string) --*

      The status of the report generation execution (RUNNING, SUCCEEDED, or FAILED).

    - **FailureCode** *(string) --*

      The failure code.

    - **S3Location** *(dict) --*

      The S3 location of the output reports.

      - **Path** *(string) --*

        The path of the business report.

      - **BucketName** *(string) --*

        The S3 bucket name of the output reports.

    - **DeliveryTime** *(datetime) --*

      The time of report delivery.

    - **DownloadUrl** *(string) --*

      The download link where a user can download the report.
    """


_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef",
    {"StartDate": str},
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef(
    _ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef
):
    """
    Type definition for `ListBusinessReportSchedulesPaginateResponseBusinessReportSchedules` `Recurrence`

    The recurrence of the reports.

    - **StartDate** *(string) --*

      The start date.
    """


_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef",
    {
        "ScheduleArn": str,
        "ScheduleName": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "Format": str,
        "ContentRange": ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef,
        "Recurrence": ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef,
        "LastBusinessReport": ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef,
    },
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef(
    _ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef
):
    """
    Type definition for `ListBusinessReportSchedulesPaginateResponse` `BusinessReportSchedules`

    The schedule of the usage report.

    - **ScheduleArn** *(string) --*

      The ARN of the business report schedule.

    - **ScheduleName** *(string) --*

      The name identifier of the schedule.

    - **S3BucketName** *(string) --*

      The S3 bucket name of the output reports.

    - **S3KeyPrefix** *(string) --*

      The S3 key where the report is delivered.

    - **Format** *(string) --*

      The format of the generated report (individual CSV files or zipped files of individual
      files).

    - **ContentRange** *(dict) --*

      The content range of the reports.

      - **Interval** *(string) --*

        The interval of the content range.

    - **Recurrence** *(dict) --*

      The recurrence of the reports.

      - **StartDate** *(string) --*

        The start date.

    - **LastBusinessReport** *(dict) --*

      The details of the last business report delivery for a specified time interval.

      - **Status** *(string) --*

        The status of the report generation execution (RUNNING, SUCCEEDED, or FAILED).

      - **FailureCode** *(string) --*

        The failure code.

      - **S3Location** *(dict) --*

        The S3 location of the output reports.

        - **Path** *(string) --*

          The path of the business report.

        - **BucketName** *(string) --*

          The S3 bucket name of the output reports.

      - **DeliveryTime** *(datetime) --*

        The time of report delivery.

      - **DownloadUrl** *(string) --*

        The download link where a user can download the report.
    """


_ListBusinessReportSchedulesPaginateResponseTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseTypeDef",
    {
        "BusinessReportSchedules": List[
            ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef
        ]
    },
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseTypeDef(
    _ListBusinessReportSchedulesPaginateResponseTypeDef
):
    """
    Type definition for `ListBusinessReportSchedulesPaginate` `Response`

    - **BusinessReportSchedules** *(list) --*

      The schedule of the reports.

      - *(dict) --*

        The schedule of the usage report.

        - **ScheduleArn** *(string) --*

          The ARN of the business report schedule.

        - **ScheduleName** *(string) --*

          The name identifier of the schedule.

        - **S3BucketName** *(string) --*

          The S3 bucket name of the output reports.

        - **S3KeyPrefix** *(string) --*

          The S3 key where the report is delivered.

        - **Format** *(string) --*

          The format of the generated report (individual CSV files or zipped files of individual
          files).

        - **ContentRange** *(dict) --*

          The content range of the reports.

          - **Interval** *(string) --*

            The interval of the content range.

        - **Recurrence** *(dict) --*

          The recurrence of the reports.

          - **StartDate** *(string) --*

            The start date.

        - **LastBusinessReport** *(dict) --*

          The details of the last business report delivery for a specified time interval.

          - **Status** *(string) --*

            The status of the report generation execution (RUNNING, SUCCEEDED, or FAILED).

          - **FailureCode** *(string) --*

            The failure code.

          - **S3Location** *(dict) --*

            The S3 location of the output reports.

            - **Path** *(string) --*

              The path of the business report.

            - **BucketName** *(string) --*

              The S3 bucket name of the output reports.

          - **DeliveryTime** *(datetime) --*

            The time of report delivery.

          - **DownloadUrl** *(string) --*

            The download link where a user can download the report.
    """


_ListConferenceProvidersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConferenceProvidersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConferenceProvidersPaginatePaginationConfigTypeDef(
    _ListConferenceProvidersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListConferenceProvidersPaginate` `PaginationConfig`

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


_ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef = TypedDict(
    "_ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef",
    {"Endpoint": str, "CommsProtocol": str},
    total=False,
)


class ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef(
    _ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef
):
    """
    Type definition for `ListConferenceProvidersPaginateResponseConferenceProviders` `IPDialIn`

    The IP endpoint and protocol for calling.

    - **Endpoint** *(string) --*

      The IP address.

    - **CommsProtocol** *(string) --*

      The protocol, including SIP, SIPS, and H323.
    """


_ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef = TypedDict(
    "_ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef",
    {"RequirePin": str},
    total=False,
)


class ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef(
    _ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef
):
    """
    Type definition for `ListConferenceProvidersPaginateResponseConferenceProviders` `MeetingSetting`

    The meeting settings for the conference provider.

    - **RequirePin** *(string) --*

      The values that indicate whether the pin is always required.
    """


_ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef = TypedDict(
    "_ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef",
    {
        "CountryCode": str,
        "PhoneNumber": str,
        "OneClickIdDelay": str,
        "OneClickPinDelay": str,
    },
    total=False,
)


class ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef(
    _ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef
):
    """
    Type definition for `ListConferenceProvidersPaginateResponseConferenceProviders` `PSTNDialIn`

    The information for PSTN conferencing.

    - **CountryCode** *(string) --*

      The zip code.

    - **PhoneNumber** *(string) --*

      The phone number to call to join the conference.

    - **OneClickIdDelay** *(string) --*

      The delay duration before Alexa enters the conference ID with dual-tone multi-frequency
      (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send
      data over the telephone network.

    - **OneClickPinDelay** *(string) --*

      The delay duration before Alexa enters the conference pin with dual-tone
      multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which
      is how we send data over the telephone network.
    """


_ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef = TypedDict(
    "_ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": str,
        "IPDialIn": ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef,
        "PSTNDialIn": ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef,
        "MeetingSetting": ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef,
    },
    total=False,
)


class ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef(
    _ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef
):
    """
    Type definition for `ListConferenceProvidersPaginateResponse` `ConferenceProviders`

    An entity that provides a conferencing solution. Alexa for Business acts as the voice
    interface and mediator that connects users to their preferred conference provider. Examples
    of conference providers include Amazon Chime, Zoom, Cisco, and Polycom.

    - **Arn** *(string) --*

      The ARN of the newly created conference provider.

    - **Name** *(string) --*

      The name of the conference provider.

    - **Type** *(string) --*

      The type of conference providers.

    - **IPDialIn** *(dict) --*

      The IP endpoint and protocol for calling.

      - **Endpoint** *(string) --*

        The IP address.

      - **CommsProtocol** *(string) --*

        The protocol, including SIP, SIPS, and H323.

    - **PSTNDialIn** *(dict) --*

      The information for PSTN conferencing.

      - **CountryCode** *(string) --*

        The zip code.

      - **PhoneNumber** *(string) --*

        The phone number to call to join the conference.

      - **OneClickIdDelay** *(string) --*

        The delay duration before Alexa enters the conference ID with dual-tone multi-frequency
        (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send
        data over the telephone network.

      - **OneClickPinDelay** *(string) --*

        The delay duration before Alexa enters the conference pin with dual-tone
        multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which
        is how we send data over the telephone network.

    - **MeetingSetting** *(dict) --*

      The meeting settings for the conference provider.

      - **RequirePin** *(string) --*

        The values that indicate whether the pin is always required.
    """


_ListConferenceProvidersPaginateResponseTypeDef = TypedDict(
    "_ListConferenceProvidersPaginateResponseTypeDef",
    {
        "ConferenceProviders": List[
            ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef
        ]
    },
    total=False,
)


class ListConferenceProvidersPaginateResponseTypeDef(
    _ListConferenceProvidersPaginateResponseTypeDef
):
    """
    Type definition for `ListConferenceProvidersPaginate` `Response`

    - **ConferenceProviders** *(list) --*

      The conference providers.

      - *(dict) --*

        An entity that provides a conferencing solution. Alexa for Business acts as the voice
        interface and mediator that connects users to their preferred conference provider. Examples
        of conference providers include Amazon Chime, Zoom, Cisco, and Polycom.

        - **Arn** *(string) --*

          The ARN of the newly created conference provider.

        - **Name** *(string) --*

          The name of the conference provider.

        - **Type** *(string) --*

          The type of conference providers.

        - **IPDialIn** *(dict) --*

          The IP endpoint and protocol for calling.

          - **Endpoint** *(string) --*

            The IP address.

          - **CommsProtocol** *(string) --*

            The protocol, including SIP, SIPS, and H323.

        - **PSTNDialIn** *(dict) --*

          The information for PSTN conferencing.

          - **CountryCode** *(string) --*

            The zip code.

          - **PhoneNumber** *(string) --*

            The phone number to call to join the conference.

          - **OneClickIdDelay** *(string) --*

            The delay duration before Alexa enters the conference ID with dual-tone multi-frequency
            (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send
            data over the telephone network.

          - **OneClickPinDelay** *(string) --*

            The delay duration before Alexa enters the conference pin with dual-tone
            multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which
            is how we send data over the telephone network.

        - **MeetingSetting** *(dict) --*

          The meeting settings for the conference provider.

          - **RequirePin** *(string) --*

            The values that indicate whether the pin is always required.
    """


_ListDeviceEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeviceEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeviceEventsPaginatePaginationConfigTypeDef(
    _ListDeviceEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeviceEventsPaginate` `PaginationConfig`

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


_ListDeviceEventsPaginateResponseDeviceEventsTypeDef = TypedDict(
    "_ListDeviceEventsPaginateResponseDeviceEventsTypeDef",
    {"Type": str, "Value": str, "Timestamp": datetime},
    total=False,
)


class ListDeviceEventsPaginateResponseDeviceEventsTypeDef(
    _ListDeviceEventsPaginateResponseDeviceEventsTypeDef
):
    """
    Type definition for `ListDeviceEventsPaginateResponse` `DeviceEvents`

    The list of device events.

    - **Type** *(string) --*

      The type of device event.

    - **Value** *(string) --*

      The value of the event.

    - **Timestamp** *(datetime) --*

      The time (in epoch) when the event occurred.
    """


_ListDeviceEventsPaginateResponseTypeDef = TypedDict(
    "_ListDeviceEventsPaginateResponseTypeDef",
    {"DeviceEvents": List[ListDeviceEventsPaginateResponseDeviceEventsTypeDef]},
    total=False,
)


class ListDeviceEventsPaginateResponseTypeDef(_ListDeviceEventsPaginateResponseTypeDef):
    """
    Type definition for `ListDeviceEventsPaginate` `Response`

    - **DeviceEvents** *(list) --*

      The device events requested for the device ARN.

      - *(dict) --*

        The list of device events.

        - **Type** *(string) --*

          The type of device event.

        - **Value** *(string) --*

          The value of the event.

        - **Timestamp** *(datetime) --*

          The time (in epoch) when the event occurred.
    """


_ListSkillsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSkillsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSkillsPaginatePaginationConfigTypeDef(
    _ListSkillsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSkillsPaginate` `PaginationConfig`

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


_ListSkillsPaginateResponseSkillSummariesTypeDef = TypedDict(
    "_ListSkillsPaginateResponseSkillSummariesTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "SupportsLinking": bool,
        "EnablementType": str,
        "SkillType": str,
    },
    total=False,
)


class ListSkillsPaginateResponseSkillSummariesTypeDef(
    _ListSkillsPaginateResponseSkillSummariesTypeDef
):
    """
    Type definition for `ListSkillsPaginateResponse` `SkillSummaries`

    The summary of skills.

    - **SkillId** *(string) --*

      The ARN of the skill summary.

    - **SkillName** *(string) --*

      The name of the skill.

    - **SupportsLinking** *(boolean) --*

      Linking support for a skill.

    - **EnablementType** *(string) --*

      Whether the skill is enabled under the user's account, or if it requires linking to be
      used.

    - **SkillType** *(string) --*

      Whether the skill is publicly available or is a private skill.
    """


_ListSkillsPaginateResponseTypeDef = TypedDict(
    "_ListSkillsPaginateResponseTypeDef",
    {"SkillSummaries": List[ListSkillsPaginateResponseSkillSummariesTypeDef]},
    total=False,
)


class ListSkillsPaginateResponseTypeDef(_ListSkillsPaginateResponseTypeDef):
    """
    Type definition for `ListSkillsPaginate` `Response`

    - **SkillSummaries** *(list) --*

      The list of enabled skills requested. Required.

      - *(dict) --*

        The summary of skills.

        - **SkillId** *(string) --*

          The ARN of the skill summary.

        - **SkillName** *(string) --*

          The name of the skill.

        - **SupportsLinking** *(boolean) --*

          Linking support for a skill.

        - **EnablementType** *(string) --*

          Whether the skill is enabled under the user's account, or if it requires linking to be
          used.

        - **SkillType** *(string) --*

          Whether the skill is publicly available or is a private skill.
    """


_ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef(
    _ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSkillsStoreCategoriesPaginate` `PaginationConfig`

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


_ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef = TypedDict(
    "_ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef",
    {"CategoryId": int, "CategoryName": str},
    total=False,
)


class ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef(
    _ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef
):
    """
    Type definition for `ListSkillsStoreCategoriesPaginateResponse` `CategoryList`

    The skill store category that is shown. Alexa skills are assigned a specific skill category
    during creation, such as News, Social, and Sports.

    - **CategoryId** *(integer) --*

      The ID of the skill store category.

    - **CategoryName** *(string) --*

      The name of the skill store category.
    """


_ListSkillsStoreCategoriesPaginateResponseTypeDef = TypedDict(
    "_ListSkillsStoreCategoriesPaginateResponseTypeDef",
    {
        "CategoryList": List[
            ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef
        ]
    },
    total=False,
)


class ListSkillsStoreCategoriesPaginateResponseTypeDef(
    _ListSkillsStoreCategoriesPaginateResponseTypeDef
):
    """
    Type definition for `ListSkillsStoreCategoriesPaginate` `Response`

    - **CategoryList** *(list) --*

      The list of categories.

      - *(dict) --*

        The skill store category that is shown. Alexa skills are assigned a specific skill category
        during creation, such as News, Social, and Sports.

        - **CategoryId** *(integer) --*

          The ID of the skill store category.

        - **CategoryName** *(string) --*

          The name of the skill store category.
    """


_ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef(
    _ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSkillsStoreSkillsByCategoryPaginate` `PaginationConfig`

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


_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef = TypedDict(
    "_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef",
    {"DeveloperName": str, "PrivacyPolicy": str, "Email": str, "Url": str},
    total=False,
)


class ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef(
    _ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef
):
    """
    Type definition for `ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetails` `DeveloperInfo`

    The details about the developer that published the skill.

    - **DeveloperName** *(string) --*

      The name of the developer.

    - **PrivacyPolicy** *(string) --*

      The URL of the privacy policy.

    - **Email** *(string) --*

      The email of the developer.

    - **Url** *(string) --*

      The website of the developer.
    """


_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef = TypedDict(
    "_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef",
    {
        "ProductDescription": str,
        "InvocationPhrase": str,
        "ReleaseDate": str,
        "EndUserLicenseAgreement": str,
        "GenericKeywords": List[str],
        "BulletPoints": List[str],
        "NewInThisVersionBulletPoints": List[str],
        "SkillTypes": List[str],
        "Reviews": Dict[str, str],
        "DeveloperInfo": ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef,
    },
    total=False,
)


class ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef(
    _ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef
):
    """
    Type definition for `ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkills` `SkillDetails`

    Information about the skill.

    - **ProductDescription** *(string) --*

      The description of the product.

    - **InvocationPhrase** *(string) --*

      The phrase used to trigger the skill.

    - **ReleaseDate** *(string) --*

      The date when the skill was released.

    - **EndUserLicenseAgreement** *(string) --*

      The URL of the end user license agreement.

    - **GenericKeywords** *(list) --*

      The generic keywords associated with the skill that can be used to find a skill.

      - *(string) --*

    - **BulletPoints** *(list) --*

      The details about what the skill supports organized as bullet points.

      - *(string) --*

    - **NewInThisVersionBulletPoints** *(list) --*

      The updates added in bullet points.

      - *(string) --*

    - **SkillTypes** *(list) --*

      The types of skills.

      - *(string) --*

    - **Reviews** *(dict) --*

      The list of reviews for the skill, including Key and Value pair.

      - *(string) --*

        - *(string) --*

    - **DeveloperInfo** *(dict) --*

      The details about the developer that published the skill.

      - **DeveloperName** *(string) --*

        The name of the developer.

      - **PrivacyPolicy** *(string) --*

        The URL of the privacy policy.

      - **Email** *(string) --*

        The email of the developer.

      - **Url** *(string) --*

        The website of the developer.
    """


_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef = TypedDict(
    "_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "ShortDescription": str,
        "IconUrl": str,
        "SampleUtterances": List[str],
        "SkillDetails": ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef,
        "SupportsLinking": bool,
    },
    total=False,
)


class ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef(
    _ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef
):
    """
    Type definition for `ListSkillsStoreSkillsByCategoryPaginateResponse` `SkillsStoreSkills`

    The detailed information about an Alexa skill.

    - **SkillId** *(string) --*

      The ARN of the skill.

    - **SkillName** *(string) --*

      The name of the skill.

    - **ShortDescription** *(string) --*

      Short description about the skill.

    - **IconUrl** *(string) --*

      The URL where the skill icon resides.

    - **SampleUtterances** *(list) --*

      Sample utterances that interact with the skill.

      - *(string) --*

    - **SkillDetails** *(dict) --*

      Information about the skill.

      - **ProductDescription** *(string) --*

        The description of the product.

      - **InvocationPhrase** *(string) --*

        The phrase used to trigger the skill.

      - **ReleaseDate** *(string) --*

        The date when the skill was released.

      - **EndUserLicenseAgreement** *(string) --*

        The URL of the end user license agreement.

      - **GenericKeywords** *(list) --*

        The generic keywords associated with the skill that can be used to find a skill.

        - *(string) --*

      - **BulletPoints** *(list) --*

        The details about what the skill supports organized as bullet points.

        - *(string) --*

      - **NewInThisVersionBulletPoints** *(list) --*

        The updates added in bullet points.

        - *(string) --*

      - **SkillTypes** *(list) --*

        The types of skills.

        - *(string) --*

      - **Reviews** *(dict) --*

        The list of reviews for the skill, including Key and Value pair.

        - *(string) --*

          - *(string) --*

      - **DeveloperInfo** *(dict) --*

        The details about the developer that published the skill.

        - **DeveloperName** *(string) --*

          The name of the developer.

        - **PrivacyPolicy** *(string) --*

          The URL of the privacy policy.

        - **Email** *(string) --*

          The email of the developer.

        - **Url** *(string) --*

          The website of the developer.

    - **SupportsLinking** *(boolean) --*

      Linking support for a skill.
    """


_ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef = TypedDict(
    "_ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef",
    {
        "SkillsStoreSkills": List[
            ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef
        ]
    },
    total=False,
)


class ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef(
    _ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef
):
    """
    Type definition for `ListSkillsStoreSkillsByCategoryPaginate` `Response`

    - **SkillsStoreSkills** *(list) --*

      The skill store skills.

      - *(dict) --*

        The detailed information about an Alexa skill.

        - **SkillId** *(string) --*

          The ARN of the skill.

        - **SkillName** *(string) --*

          The name of the skill.

        - **ShortDescription** *(string) --*

          Short description about the skill.

        - **IconUrl** *(string) --*

          The URL where the skill icon resides.

        - **SampleUtterances** *(list) --*

          Sample utterances that interact with the skill.

          - *(string) --*

        - **SkillDetails** *(dict) --*

          Information about the skill.

          - **ProductDescription** *(string) --*

            The description of the product.

          - **InvocationPhrase** *(string) --*

            The phrase used to trigger the skill.

          - **ReleaseDate** *(string) --*

            The date when the skill was released.

          - **EndUserLicenseAgreement** *(string) --*

            The URL of the end user license agreement.

          - **GenericKeywords** *(list) --*

            The generic keywords associated with the skill that can be used to find a skill.

            - *(string) --*

          - **BulletPoints** *(list) --*

            The details about what the skill supports organized as bullet points.

            - *(string) --*

          - **NewInThisVersionBulletPoints** *(list) --*

            The updates added in bullet points.

            - *(string) --*

          - **SkillTypes** *(list) --*

            The types of skills.

            - *(string) --*

          - **Reviews** *(dict) --*

            The list of reviews for the skill, including Key and Value pair.

            - *(string) --*

              - *(string) --*

          - **DeveloperInfo** *(dict) --*

            The details about the developer that published the skill.

            - **DeveloperName** *(string) --*

              The name of the developer.

            - **PrivacyPolicy** *(string) --*

              The URL of the privacy policy.

            - **Email** *(string) --*

              The email of the developer.

            - **Url** *(string) --*

              The website of the developer.

        - **SupportsLinking** *(boolean) --*

          Linking support for a skill.
    """


_ListSmartHomeAppliancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSmartHomeAppliancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSmartHomeAppliancesPaginatePaginationConfigTypeDef(
    _ListSmartHomeAppliancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSmartHomeAppliancesPaginate` `PaginationConfig`

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


_ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef = TypedDict(
    "_ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef",
    {"FriendlyName": str, "Description": str, "ManufacturerName": str},
    total=False,
)


class ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef(
    _ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef
):
    """
    Type definition for `ListSmartHomeAppliancesPaginateResponse` `SmartHomeAppliances`

    A smart home appliance that can connect to a central system. Any domestic device can be a
    smart appliance.

    - **FriendlyName** *(string) --*

      The friendly name of the smart home appliance.

    - **Description** *(string) --*

      The description of the smart home appliance.

    - **ManufacturerName** *(string) --*

      The name of the manufacturer of the smart home appliance.
    """


_ListSmartHomeAppliancesPaginateResponseTypeDef = TypedDict(
    "_ListSmartHomeAppliancesPaginateResponseTypeDef",
    {
        "SmartHomeAppliances": List[
            ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef
        ]
    },
    total=False,
)


class ListSmartHomeAppliancesPaginateResponseTypeDef(
    _ListSmartHomeAppliancesPaginateResponseTypeDef
):
    """
    Type definition for `ListSmartHomeAppliancesPaginate` `Response`

    - **SmartHomeAppliances** *(list) --*

      The smart home appliances.

      - *(dict) --*

        A smart home appliance that can connect to a central system. Any domestic device can be a
        smart appliance.

        - **FriendlyName** *(string) --*

          The friendly name of the smart home appliance.

        - **Description** *(string) --*

          The description of the smart home appliance.

        - **ManufacturerName** *(string) --*

          The name of the manufacturer of the smart home appliance.
    """


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsPaginatePaginationConfigTypeDef(_ListTagsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListTagsPaginate` `PaginationConfig`

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


_ListTagsPaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsPaginateResponseTagsTypeDef(_ListTagsPaginateResponseTagsTypeDef):
    """
    Type definition for `ListTagsPaginateResponse` `Tags`

    A key-value pair that can be associated with a resource.

    - **Key** *(string) --*

      The key of a tag. Tag keys are case-sensitive.

    - **Value** *(string) --*

      The value of a tag. Tag values are case-sensitive and can be null.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"Tags": List[ListTagsPaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    Type definition for `ListTagsPaginate` `Response`

    - **Tags** *(list) --*

      The tags requested for the specified resource.

      - *(dict) --*

        A key-value pair that can be associated with a resource.

        - **Key** *(string) --*

          The key of a tag. Tag keys are case-sensitive.

        - **Value** *(string) --*

          The value of a tag. Tag values are case-sensitive and can be null.
    """


_SearchDevicesPaginateFiltersTypeDef = TypedDict(
    "_SearchDevicesPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class SearchDevicesPaginateFiltersTypeDef(_SearchDevicesPaginateFiltersTypeDef):
    """
    Type definition for `SearchDevicesPaginate` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_SearchDevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchDevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchDevicesPaginatePaginationConfigTypeDef(
    _SearchDevicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchDevicesPaginate` `PaginationConfig`

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


_SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef = TypedDict(
    "_SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef",
    {"Feature": str, "Code": str},
    total=False,
)


class SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef(
    _SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef
):
    """
    Type definition for `SearchDevicesPaginateResponseDevicesDeviceStatusInfo` `DeviceStatusDetails`

    Details of a device’s status.

    - **Feature** *(string) --*

      The list of available features on the device.

    - **Code** *(string) --*

      The device status detail code.
    """


_SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef = TypedDict(
    "_SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List[
            SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef
        ],
        "ConnectionStatus": str,
    },
    total=False,
)


class SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef(
    _SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef
):
    """
    Type definition for `SearchDevicesPaginateResponseDevices` `DeviceStatusInfo`

    Detailed information about a device's status.

    - **DeviceStatusDetails** *(list) --*

      One or more device status detail descriptions.

      - *(dict) --*

        Details of a device’s status.

        - **Feature** *(string) --*

          The list of available features on the device.

        - **Code** *(string) --*

          The device status detail code.

    - **ConnectionStatus** *(string) --*

      The latest available information about the connection status of a device.
    """


_SearchDevicesPaginateResponseDevicesTypeDef = TypedDict(
    "_SearchDevicesPaginateResponseDevicesTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "DeviceStatus": str,
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "RoomArn": str,
        "RoomName": str,
        "DeviceStatusInfo": SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef,
    },
    total=False,
)


class SearchDevicesPaginateResponseDevicesTypeDef(
    _SearchDevicesPaginateResponseDevicesTypeDef
):
    """
    Type definition for `SearchDevicesPaginateResponse` `Devices`

    Device attributes.

    - **DeviceArn** *(string) --*

      The ARN of a device.

    - **DeviceSerialNumber** *(string) --*

      The serial number of a device.

    - **DeviceType** *(string) --*

      The type of a device.

    - **DeviceName** *(string) --*

      The name of a device.

    - **SoftwareVersion** *(string) --*

      The software version of a device.

    - **MacAddress** *(string) --*

      The MAC address of a device.

    - **DeviceStatus** *(string) --*

      The status of a device.

    - **NetworkProfileArn** *(string) --*

      The ARN of the network profile associated with a device.

    - **NetworkProfileName** *(string) --*

      The name of the network profile associated with a device.

    - **RoomArn** *(string) --*

      The room ARN associated with a device.

    - **RoomName** *(string) --*

      The name of the room associated with a device.

    - **DeviceStatusInfo** *(dict) --*

      Detailed information about a device's status.

      - **DeviceStatusDetails** *(list) --*

        One or more device status detail descriptions.

        - *(dict) --*

          Details of a device’s status.

          - **Feature** *(string) --*

            The list of available features on the device.

          - **Code** *(string) --*

            The device status detail code.

      - **ConnectionStatus** *(string) --*

        The latest available information about the connection status of a device.
    """


_SearchDevicesPaginateResponseTypeDef = TypedDict(
    "_SearchDevicesPaginateResponseTypeDef",
    {"Devices": List[SearchDevicesPaginateResponseDevicesTypeDef], "TotalCount": int},
    total=False,
)


class SearchDevicesPaginateResponseTypeDef(_SearchDevicesPaginateResponseTypeDef):
    """
    Type definition for `SearchDevicesPaginate` `Response`

    - **Devices** *(list) --*

      The devices that meet the specified set of filter criteria, in sort order.

      - *(dict) --*

        Device attributes.

        - **DeviceArn** *(string) --*

          The ARN of a device.

        - **DeviceSerialNumber** *(string) --*

          The serial number of a device.

        - **DeviceType** *(string) --*

          The type of a device.

        - **DeviceName** *(string) --*

          The name of a device.

        - **SoftwareVersion** *(string) --*

          The software version of a device.

        - **MacAddress** *(string) --*

          The MAC address of a device.

        - **DeviceStatus** *(string) --*

          The status of a device.

        - **NetworkProfileArn** *(string) --*

          The ARN of the network profile associated with a device.

        - **NetworkProfileName** *(string) --*

          The name of the network profile associated with a device.

        - **RoomArn** *(string) --*

          The room ARN associated with a device.

        - **RoomName** *(string) --*

          The name of the room associated with a device.

        - **DeviceStatusInfo** *(dict) --*

          Detailed information about a device's status.

          - **DeviceStatusDetails** *(list) --*

            One or more device status detail descriptions.

            - *(dict) --*

              Details of a device’s status.

              - **Feature** *(string) --*

                The list of available features on the device.

              - **Code** *(string) --*

                The device status detail code.

          - **ConnectionStatus** *(string) --*

            The latest available information about the connection status of a device.

    - **TotalCount** *(integer) --*

      The total number of devices returned.
    """


_SearchDevicesPaginateSortCriteriaTypeDef = TypedDict(
    "_SearchDevicesPaginateSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class SearchDevicesPaginateSortCriteriaTypeDef(
    _SearchDevicesPaginateSortCriteriaTypeDef
):
    """
    Type definition for `SearchDevicesPaginate` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_SearchProfilesPaginateFiltersTypeDef = TypedDict(
    "_SearchProfilesPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class SearchProfilesPaginateFiltersTypeDef(_SearchProfilesPaginateFiltersTypeDef):
    """
    Type definition for `SearchProfilesPaginate` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_SearchProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchProfilesPaginatePaginationConfigTypeDef(
    _SearchProfilesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchProfilesPaginate` `PaginationConfig`

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


_SearchProfilesPaginateResponseProfilesTypeDef = TypedDict(
    "_SearchProfilesPaginateResponseProfilesTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": str,
        "TemperatureUnit": str,
        "WakeWord": str,
        "Locale": str,
    },
    total=False,
)


class SearchProfilesPaginateResponseProfilesTypeDef(
    _SearchProfilesPaginateResponseProfilesTypeDef
):
    """
    Type definition for `SearchProfilesPaginateResponse` `Profiles`

    The data of a room profile.

    - **ProfileArn** *(string) --*

      The ARN of a room profile.

    - **ProfileName** *(string) --*

      The name of a room profile.

    - **IsDefault** *(boolean) --*

      Retrieves if the profile data is default or not.

    - **Address** *(string) --*

      The address of a room profile.

    - **Timezone** *(string) --*

      The timezone of a room profile.

    - **DistanceUnit** *(string) --*

      The distance unit of a room profile.

    - **TemperatureUnit** *(string) --*

      The temperature unit of a room profile.

    - **WakeWord** *(string) --*

      The wake word of a room profile.

    - **Locale** *(string) --*

      The locale of a room profile.
    """


_SearchProfilesPaginateResponseTypeDef = TypedDict(
    "_SearchProfilesPaginateResponseTypeDef",
    {
        "Profiles": List[SearchProfilesPaginateResponseProfilesTypeDef],
        "TotalCount": int,
    },
    total=False,
)


class SearchProfilesPaginateResponseTypeDef(_SearchProfilesPaginateResponseTypeDef):
    """
    Type definition for `SearchProfilesPaginate` `Response`

    - **Profiles** *(list) --*

      The profiles that meet the specified set of filter criteria, in sort order.

      - *(dict) --*

        The data of a room profile.

        - **ProfileArn** *(string) --*

          The ARN of a room profile.

        - **ProfileName** *(string) --*

          The name of a room profile.

        - **IsDefault** *(boolean) --*

          Retrieves if the profile data is default or not.

        - **Address** *(string) --*

          The address of a room profile.

        - **Timezone** *(string) --*

          The timezone of a room profile.

        - **DistanceUnit** *(string) --*

          The distance unit of a room profile.

        - **TemperatureUnit** *(string) --*

          The temperature unit of a room profile.

        - **WakeWord** *(string) --*

          The wake word of a room profile.

        - **Locale** *(string) --*

          The locale of a room profile.

    - **TotalCount** *(integer) --*

      The total number of room profiles returned.
    """


_SearchProfilesPaginateSortCriteriaTypeDef = TypedDict(
    "_SearchProfilesPaginateSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class SearchProfilesPaginateSortCriteriaTypeDef(
    _SearchProfilesPaginateSortCriteriaTypeDef
):
    """
    Type definition for `SearchProfilesPaginate` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_SearchRoomsPaginateFiltersTypeDef = TypedDict(
    "_SearchRoomsPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class SearchRoomsPaginateFiltersTypeDef(_SearchRoomsPaginateFiltersTypeDef):
    """
    Type definition for `SearchRoomsPaginate` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_SearchRoomsPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchRoomsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchRoomsPaginatePaginationConfigTypeDef(
    _SearchRoomsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchRoomsPaginate` `PaginationConfig`

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


_SearchRoomsPaginateResponseRoomsTypeDef = TypedDict(
    "_SearchRoomsPaginateResponseRoomsTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
        "ProfileName": str,
    },
    total=False,
)


class SearchRoomsPaginateResponseRoomsTypeDef(_SearchRoomsPaginateResponseRoomsTypeDef):
    """
    Type definition for `SearchRoomsPaginateResponse` `Rooms`

    The data of a room.

    - **RoomArn** *(string) --*

      The ARN of a room.

    - **RoomName** *(string) --*

      The name of a room.

    - **Description** *(string) --*

      The description of a room.

    - **ProviderCalendarId** *(string) --*

      The provider calendar ARN of a room.

    - **ProfileArn** *(string) --*

      The profile ARN of a room.

    - **ProfileName** *(string) --*

      The profile name of a room.
    """


_SearchRoomsPaginateResponseTypeDef = TypedDict(
    "_SearchRoomsPaginateResponseTypeDef",
    {"Rooms": List[SearchRoomsPaginateResponseRoomsTypeDef], "TotalCount": int},
    total=False,
)


class SearchRoomsPaginateResponseTypeDef(_SearchRoomsPaginateResponseTypeDef):
    """
    Type definition for `SearchRoomsPaginate` `Response`

    - **Rooms** *(list) --*

      The rooms that meet the specified set of filter criteria, in sort order.

      - *(dict) --*

        The data of a room.

        - **RoomArn** *(string) --*

          The ARN of a room.

        - **RoomName** *(string) --*

          The name of a room.

        - **Description** *(string) --*

          The description of a room.

        - **ProviderCalendarId** *(string) --*

          The provider calendar ARN of a room.

        - **ProfileArn** *(string) --*

          The profile ARN of a room.

        - **ProfileName** *(string) --*

          The profile name of a room.

    - **TotalCount** *(integer) --*

      The total number of rooms returned.
    """


_SearchRoomsPaginateSortCriteriaTypeDef = TypedDict(
    "_SearchRoomsPaginateSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class SearchRoomsPaginateSortCriteriaTypeDef(_SearchRoomsPaginateSortCriteriaTypeDef):
    """
    Type definition for `SearchRoomsPaginate` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_SearchSkillGroupsPaginateFiltersTypeDef = TypedDict(
    "_SearchSkillGroupsPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class SearchSkillGroupsPaginateFiltersTypeDef(_SearchSkillGroupsPaginateFiltersTypeDef):
    """
    Type definition for `SearchSkillGroupsPaginate` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_SearchSkillGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchSkillGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchSkillGroupsPaginatePaginationConfigTypeDef(
    _SearchSkillGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchSkillGroupsPaginate` `PaginationConfig`

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


_SearchSkillGroupsPaginateResponseSkillGroupsTypeDef = TypedDict(
    "_SearchSkillGroupsPaginateResponseSkillGroupsTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)


class SearchSkillGroupsPaginateResponseSkillGroupsTypeDef(
    _SearchSkillGroupsPaginateResponseSkillGroupsTypeDef
):
    """
    Type definition for `SearchSkillGroupsPaginateResponse` `SkillGroups`

    The attributes of a skill group.

    - **SkillGroupArn** *(string) --*

      The skill group ARN of a skill group.

    - **SkillGroupName** *(string) --*

      The skill group name of a skill group.

    - **Description** *(string) --*

      The description of a skill group.
    """


_SearchSkillGroupsPaginateResponseTypeDef = TypedDict(
    "_SearchSkillGroupsPaginateResponseTypeDef",
    {
        "SkillGroups": List[SearchSkillGroupsPaginateResponseSkillGroupsTypeDef],
        "TotalCount": int,
    },
    total=False,
)


class SearchSkillGroupsPaginateResponseTypeDef(
    _SearchSkillGroupsPaginateResponseTypeDef
):
    """
    Type definition for `SearchSkillGroupsPaginate` `Response`

    - **SkillGroups** *(list) --*

      The skill groups that meet the filter criteria, in sort order.

      - *(dict) --*

        The attributes of a skill group.

        - **SkillGroupArn** *(string) --*

          The skill group ARN of a skill group.

        - **SkillGroupName** *(string) --*

          The skill group name of a skill group.

        - **Description** *(string) --*

          The description of a skill group.

    - **TotalCount** *(integer) --*

      The total number of skill groups returned.
    """


_SearchSkillGroupsPaginateSortCriteriaTypeDef = TypedDict(
    "_SearchSkillGroupsPaginateSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class SearchSkillGroupsPaginateSortCriteriaTypeDef(
    _SearchSkillGroupsPaginateSortCriteriaTypeDef
):
    """
    Type definition for `SearchSkillGroupsPaginate` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """


_SearchUsersPaginateFiltersTypeDef = TypedDict(
    "_SearchUsersPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}
)


class SearchUsersPaginateFiltersTypeDef(_SearchUsersPaginateFiltersTypeDef):
    """
    Type definition for `SearchUsersPaginate` `Filters`

    A filter name and value pair that is used to return a more specific list of results. Filters
    can be used to match a set of resources by various criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The key of a filter.

    - **Values** *(list) --* **[REQUIRED]**

      The values of a filter.

      - *(string) --*
    """


_SearchUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchUsersPaginatePaginationConfigTypeDef(
    _SearchUsersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchUsersPaginate` `PaginationConfig`

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


_SearchUsersPaginateResponseUsersTypeDef = TypedDict(
    "_SearchUsersPaginateResponseUsersTypeDef",
    {
        "UserArn": str,
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "EnrollmentStatus": str,
        "EnrollmentId": str,
    },
    total=False,
)


class SearchUsersPaginateResponseUsersTypeDef(_SearchUsersPaginateResponseUsersTypeDef):
    """
    Type definition for `SearchUsersPaginateResponse` `Users`

    Information related to a user.

    - **UserArn** *(string) --*

      The ARN of a user.

    - **FirstName** *(string) --*

      The first name of a user.

    - **LastName** *(string) --*

      The last name of a user.

    - **Email** *(string) --*

      The email of a user.

    - **EnrollmentStatus** *(string) --*

      The enrollment status of a user.

    - **EnrollmentId** *(string) --*

      The enrollment ARN of a user.
    """


_SearchUsersPaginateResponseTypeDef = TypedDict(
    "_SearchUsersPaginateResponseTypeDef",
    {"Users": List[SearchUsersPaginateResponseUsersTypeDef], "TotalCount": int},
    total=False,
)


class SearchUsersPaginateResponseTypeDef(_SearchUsersPaginateResponseTypeDef):
    """
    Type definition for `SearchUsersPaginate` `Response`

    - **Users** *(list) --*

      The users that meet the specified set of filter criteria, in sort order.

      - *(dict) --*

        Information related to a user.

        - **UserArn** *(string) --*

          The ARN of a user.

        - **FirstName** *(string) --*

          The first name of a user.

        - **LastName** *(string) --*

          The last name of a user.

        - **Email** *(string) --*

          The email of a user.

        - **EnrollmentStatus** *(string) --*

          The enrollment status of a user.

        - **EnrollmentId** *(string) --*

          The enrollment ARN of a user.

    - **TotalCount** *(integer) --*

      The total number of users returned.
    """


_SearchUsersPaginateSortCriteriaTypeDef = TypedDict(
    "_SearchUsersPaginateSortCriteriaTypeDef", {"Key": str, "Value": str}
)


class SearchUsersPaginateSortCriteriaTypeDef(_SearchUsersPaginateSortCriteriaTypeDef):
    """
    Type definition for `SearchUsersPaginate` `SortCriteria`

    An object representing a sort criteria.

    - **Key** *(string) --* **[REQUIRED]**

      The sort key of a sort object.

    - **Value** *(string) --* **[REQUIRED]**

      The sort value of a sort object.
    """
