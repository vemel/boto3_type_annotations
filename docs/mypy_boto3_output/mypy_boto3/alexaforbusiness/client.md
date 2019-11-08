# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.alexaforbusiness.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Alexaforbusiness](index.md#alexaforbusiness) / Client
    - [Client](#client)
        - [Client().approve_skill](#clientapprove_skill)
        - [Client().associate_contact_with_address_book](#clientassociate_contact_with_address_book)
        - [Client().associate_device_with_network_profile](#clientassociate_device_with_network_profile)
        - [Client().associate_device_with_room](#clientassociate_device_with_room)
        - [Client().associate_skill_group_with_room](#clientassociate_skill_group_with_room)
        - [Client().associate_skill_with_skill_group](#clientassociate_skill_with_skill_group)
        - [Client().associate_skill_with_users](#clientassociate_skill_with_users)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_address_book](#clientcreate_address_book)
        - [Client().create_business_report_schedule](#clientcreate_business_report_schedule)
        - [Client().create_conference_provider](#clientcreate_conference_provider)
        - [Client().create_contact](#clientcreate_contact)
        - [Client().create_gateway_group](#clientcreate_gateway_group)
        - [Client().create_network_profile](#clientcreate_network_profile)
        - [Client().create_profile](#clientcreate_profile)
        - [Client().create_room](#clientcreate_room)
        - [Client().create_skill_group](#clientcreate_skill_group)
        - [Client().create_user](#clientcreate_user)
        - [Client().delete_address_book](#clientdelete_address_book)
        - [Client().delete_business_report_schedule](#clientdelete_business_report_schedule)
        - [Client().delete_conference_provider](#clientdelete_conference_provider)
        - [Client().delete_contact](#clientdelete_contact)
        - [Client().delete_device](#clientdelete_device)
        - [Client().delete_device_usage_data](#clientdelete_device_usage_data)
        - [Client().delete_gateway_group](#clientdelete_gateway_group)
        - [Client().delete_network_profile](#clientdelete_network_profile)
        - [Client().delete_profile](#clientdelete_profile)
        - [Client().delete_room](#clientdelete_room)
        - [Client().delete_room_skill_parameter](#clientdelete_room_skill_parameter)
        - [Client().delete_skill_authorization](#clientdelete_skill_authorization)
        - [Client().delete_skill_group](#clientdelete_skill_group)
        - [Client().delete_user](#clientdelete_user)
        - [Client().disassociate_contact_from_address_book](#clientdisassociate_contact_from_address_book)
        - [Client().disassociate_device_from_room](#clientdisassociate_device_from_room)
        - [Client().disassociate_skill_from_skill_group](#clientdisassociate_skill_from_skill_group)
        - [Client().disassociate_skill_from_users](#clientdisassociate_skill_from_users)
        - [Client().disassociate_skill_group_from_room](#clientdisassociate_skill_group_from_room)
        - [Client().forget_smart_home_appliances](#clientforget_smart_home_appliances)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_address_book](#clientget_address_book)
        - [Client().get_conference_preference](#clientget_conference_preference)
        - [Client().get_conference_provider](#clientget_conference_provider)
        - [Client().get_contact](#clientget_contact)
        - [Client().get_device](#clientget_device)
        - [Client().get_gateway](#clientget_gateway)
        - [Client().get_gateway_group](#clientget_gateway_group)
        - [Client().get_invitation_configuration](#clientget_invitation_configuration)
        - [Client().get_network_profile](#clientget_network_profile)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_profile](#clientget_profile)
        - [Client().get_room](#clientget_room)
        - [Client().get_room_skill_parameter](#clientget_room_skill_parameter)
        - [Client().get_skill_group](#clientget_skill_group)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_business_report_schedules](#clientlist_business_report_schedules)
        - [Client().list_conference_providers](#clientlist_conference_providers)
        - [Client().list_device_events](#clientlist_device_events)
        - [Client().list_gateway_groups](#clientlist_gateway_groups)
        - [Client().list_gateways](#clientlist_gateways)
        - [Client().list_skills](#clientlist_skills)
        - [Client().list_skills_store_categories](#clientlist_skills_store_categories)
        - [Client().list_skills_store_skills_by_category](#clientlist_skills_store_skills_by_category)
        - [Client().list_smart_home_appliances](#clientlist_smart_home_appliances)
        - [Client().list_tags](#clientlist_tags)
        - [Client().put_conference_preference](#clientput_conference_preference)
        - [Client().put_invitation_configuration](#clientput_invitation_configuration)
        - [Client().put_room_skill_parameter](#clientput_room_skill_parameter)
        - [Client().put_skill_authorization](#clientput_skill_authorization)
        - [Client().register_avs_device](#clientregister_avs_device)
        - [Client().reject_skill](#clientreject_skill)
        - [Client().resolve_room](#clientresolve_room)
        - [Client().revoke_invitation](#clientrevoke_invitation)
        - [Client().search_address_books](#clientsearch_address_books)
        - [Client().search_contacts](#clientsearch_contacts)
        - [Client().search_devices](#clientsearch_devices)
        - [Client().search_network_profiles](#clientsearch_network_profiles)
        - [Client().search_profiles](#clientsearch_profiles)
        - [Client().search_rooms](#clientsearch_rooms)
        - [Client().search_skill_groups](#clientsearch_skill_groups)
        - [Client().search_users](#clientsearch_users)
        - [Client().send_announcement](#clientsend_announcement)
        - [Client().send_invitation](#clientsend_invitation)
        - [Client().start_device_sync](#clientstart_device_sync)
        - [Client().start_smart_home_appliance_discovery](#clientstart_smart_home_appliance_discovery)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_address_book](#clientupdate_address_book)
        - [Client().update_business_report_schedule](#clientupdate_business_report_schedule)
        - [Client().update_conference_provider](#clientupdate_conference_provider)
        - [Client().update_contact](#clientupdate_contact)
        - [Client().update_device](#clientupdate_device)
        - [Client().update_gateway](#clientupdate_gateway)
        - [Client().update_gateway_group](#clientupdate_gateway_group)
        - [Client().update_network_profile](#clientupdate_network_profile)
        - [Client().update_profile](#clientupdate_profile)
        - [Client().update_room](#clientupdate_room)
        - [Client().update_skill_group](#clientupdate_skill_group)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L12)

```python
class Client(BaseClient):
```

### Client().approve_skill

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L15)

```python
def approve_skill(SkillId: str) -> Dict[str, Any]:
```

### Client().associate_contact_with_address_book

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L19)

```python
def associate_contact_with_address_book(
    ContactArn: str,
    AddressBookArn: str,
) -> Dict[str, Any]:
```

### Client().associate_device_with_network_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L25)

```python
def associate_device_with_network_profile(
    DeviceArn: str,
    NetworkProfileArn: str,
) -> Dict[str, Any]:
```

### Client().associate_device_with_room

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L31)

```python
def associate_device_with_room(
    DeviceArn: str = None,
    RoomArn: str = None,
) -> Dict[str, Any]:
```

### Client().associate_skill_group_with_room

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L37)

```python
def associate_skill_group_with_room(
    SkillGroupArn: str = None,
    RoomArn: str = None,
) -> Dict[str, Any]:
```

### Client().associate_skill_with_skill_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L43)

```python
def associate_skill_with_skill_group(
    SkillId: str,
    SkillGroupArn: str = None,
) -> Dict[str, Any]:
```

### Client().associate_skill_with_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L49)

```python
def associate_skill_with_users(SkillId: str) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L53)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_address_book

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L57)

```python
def create_address_book(
    Name: str,
    Description: str = None,
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_business_report_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L63)

```python
def create_business_report_schedule(
    Format: str,
    ContentRange: Dict[str, Any],
    ScheduleName: str = None,
    S3BucketName: str = None,
    S3KeyPrefix: str = None,
    Recurrence: Dict[str, Any] = None,
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_conference_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L76)

```python
def create_conference_provider(
    ConferenceProviderName: str,
    ConferenceProviderType: str,
    MeetingSetting: Dict[str, Any],
    IPDialIn: Dict[str, Any] = None,
    PSTNDialIn: Dict[str, Any] = None,
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_contact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L88)

```python
def create_contact(
    FirstName: str,
    DisplayName: str = None,
    LastName: str = None,
    PhoneNumber: str = None,
    PhoneNumbers: List[Any] = None,
    SipAddresses: List[Any] = None,
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_gateway_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L101)

```python
def create_gateway_group(
    Name: str,
    ClientRequestToken: str,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().create_network_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L107)

```python
def create_network_profile(
    NetworkProfileName: str,
    Ssid: str,
    SecurityType: str,
    ClientRequestToken: str,
    Description: str = None,
    EapMethod: str = None,
    CurrentPassword: str = None,
    NextPassword: str = None,
    CertificateAuthorityArn: str = None,
    TrustAnchors: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L123)

```python
def create_profile(
    ProfileName: str,
    Timezone: str,
    Address: str,
    DistanceUnit: str,
    TemperatureUnit: str,
    WakeWord: str,
    Locale: str = None,
    ClientRequestToken: str = None,
    SetupModeDisabled: bool = None,
    MaxVolumeLimit: int = None,
    PSTNEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().create_room

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L140)

```python
def create_room(
    RoomName: str,
    Description: str = None,
    ProfileArn: str = None,
    ProviderCalendarId: str = None,
    ClientRequestToken: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_skill_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L152)

```python
def create_skill_group(
    SkillGroupName: str,
    Description: str = None,
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L161)

```python
def create_user(
    UserId: str,
    FirstName: str = None,
    LastName: str = None,
    Email: str = None,
    ClientRequestToken: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_address_book

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L173)

```python
def delete_address_book(AddressBookArn: str) -> Dict[str, Any]:
```

### Client().delete_business_report_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L177)

```python
def delete_business_report_schedule(ScheduleArn: str) -> Dict[str, Any]:
```

### Client().delete_conference_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L181)

```python
def delete_conference_provider(ConferenceProviderArn: str) -> Dict[str, Any]:
```

### Client().delete_contact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L185)

```python
def delete_contact(ContactArn: str) -> Dict[str, Any]:
```

### Client().delete_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L189)

```python
def delete_device(DeviceArn: str) -> Dict[str, Any]:
```

### Client().delete_device_usage_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L193)

```python
def delete_device_usage_data(
    DeviceArn: str,
    DeviceUsageType: str,
) -> Dict[str, Any]:
```

### Client().delete_gateway_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L199)

```python
def delete_gateway_group(GatewayGroupArn: str) -> Dict[str, Any]:
```

### Client().delete_network_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L203)

```python
def delete_network_profile(NetworkProfileArn: str) -> Dict[str, Any]:
```

### Client().delete_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L207)

```python
def delete_profile(ProfileArn: str = None) -> Dict[str, Any]:
```

### Client().delete_room

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L211)

```python
def delete_room(RoomArn: str = None) -> Dict[str, Any]:
```

### Client().delete_room_skill_parameter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L215)

```python
def delete_room_skill_parameter(
    SkillId: str,
    ParameterKey: str,
    RoomArn: str = None,
) -> Dict[str, Any]:
```

### Client().delete_skill_authorization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L221)

```python
def delete_skill_authorization(
    SkillId: str,
    RoomArn: str = None,
) -> Dict[str, Any]:
```

### Client().delete_skill_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L227)

```python
def delete_skill_group(SkillGroupArn: str = None) -> Dict[str, Any]:
```

### Client().delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L231)

```python
def delete_user(EnrollmentId: str, UserArn: str = None) -> Dict[str, Any]:
```

### Client().disassociate_contact_from_address_book

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L235)

```python
def disassociate_contact_from_address_book(
    ContactArn: str,
    AddressBookArn: str,
) -> Dict[str, Any]:
```

### Client().disassociate_device_from_room

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L241)

```python
def disassociate_device_from_room(DeviceArn: str = None) -> Dict[str, Any]:
```

### Client().disassociate_skill_from_skill_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L245)

```python
def disassociate_skill_from_skill_group(
    SkillId: str,
    SkillGroupArn: str = None,
) -> Dict[str, Any]:
```

### Client().disassociate_skill_from_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L251)

```python
def disassociate_skill_from_users(SkillId: str) -> Dict[str, Any]:
```

### Client().disassociate_skill_group_from_room

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L255)

```python
def disassociate_skill_group_from_room(
    SkillGroupArn: str = None,
    RoomArn: str = None,
) -> Dict[str, Any]:
```

### Client().forget_smart_home_appliances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L261)

```python
def forget_smart_home_appliances(RoomArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L265)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_address_book

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L275)

```python
def get_address_book(AddressBookArn: str) -> Dict[str, Any]:
```

### Client().get_conference_preference

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L279)

```python
def get_conference_preference() -> Dict[str, Any]:
```

### Client().get_conference_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L283)

```python
def get_conference_provider(ConferenceProviderArn: str) -> Dict[str, Any]:
```

### Client().get_contact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L287)

```python
def get_contact(ContactArn: str) -> Dict[str, Any]:
```

### Client().get_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L291)

```python
def get_device(DeviceArn: str = None) -> Dict[str, Any]:
```

### Client().get_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L295)

```python
def get_gateway(GatewayArn: str) -> Dict[str, Any]:
```

### Client().get_gateway_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L299)

```python
def get_gateway_group(GatewayGroupArn: str) -> Dict[str, Any]:
```

### Client().get_invitation_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L303)

```python
def get_invitation_configuration() -> Dict[str, Any]:
```

### Client().get_network_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L307)

```python
def get_network_profile(NetworkProfileArn: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L311)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L315)

```python
def get_profile(ProfileArn: str = None) -> Dict[str, Any]:
```

### Client().get_room

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L319)

```python
def get_room(RoomArn: str = None) -> Dict[str, Any]:
```

### Client().get_room_skill_parameter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L323)

```python
def get_room_skill_parameter(
    SkillId: str,
    ParameterKey: str,
    RoomArn: str = None,
) -> Dict[str, Any]:
```

### Client().get_skill_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L329)

```python
def get_skill_group(SkillGroupArn: str = None) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L333)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_business_report_schedules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L337)

```python
def list_business_report_schedules(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_conference_providers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L343)

```python
def list_conference_providers(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_device_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L349)

```python
def list_device_events(
    DeviceArn: str,
    EventType: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_gateway_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L359)

```python
def list_gateway_groups(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L365)

```python
def list_gateways(
    GatewayGroupArn: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_skills

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L371)

```python
def list_skills(
    SkillGroupArn: str = None,
    EnablementType: str = None,
    SkillType: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_skills_store_categories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L382)

```python
def list_skills_store_categories(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_skills_store_skills_by_category

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L388)

```python
def list_skills_store_skills_by_category(
    CategoryId: int,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_smart_home_appliances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L394)

```python
def list_smart_home_appliances(
    RoomArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L400)

```python
def list_tags(
    Arn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().put_conference_preference

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L406)

```python
def put_conference_preference(
    ConferencePreference: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_invitation_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L412)

```python
def put_invitation_configuration(
    OrganizationName: str,
    ContactEmail: str = None,
    PrivateSkillIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().put_room_skill_parameter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L421)

```python
def put_room_skill_parameter(
    SkillId: str,
    RoomSkillParameter: Dict[str, Any],
    RoomArn: str = None,
) -> Dict[str, Any]:
```

### Client().put_skill_authorization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L427)

```python
def put_skill_authorization(
    AuthorizationResult: Dict[str, Any],
    SkillId: str,
    RoomArn: str = None,
) -> Dict[str, Any]:
```

### Client().register_avs_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L433)

```python
def register_avs_device(
    ClientId: str,
    UserCode: str,
    ProductId: str,
    DeviceSerialNumber: str,
    AmazonId: str,
) -> Dict[str, Any]:
```

### Client().reject_skill

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L444)

```python
def reject_skill(SkillId: str) -> Dict[str, Any]:
```

### Client().resolve_room

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L448)

```python
def resolve_room(UserId: str, SkillId: str) -> Dict[str, Any]:
```

### Client().revoke_invitation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L452)

```python
def revoke_invitation(
    UserArn: str = None,
    EnrollmentId: str = None,
) -> Dict[str, Any]:
```

### Client().search_address_books

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L458)

```python
def search_address_books(
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().search_contacts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L468)

```python
def search_contacts(
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().search_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L478)

```python
def search_devices(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().search_network_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L488)

```python
def search_network_profiles(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().search_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L498)

```python
def search_profiles(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().search_rooms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L508)

```python
def search_rooms(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().search_skill_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L518)

```python
def search_skill_groups(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().search_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L528)

```python
def search_users(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().send_announcement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L538)

```python
def send_announcement(
    RoomFilters: List[Any],
    Content: Dict[str, Any],
    ClientRequestToken: str,
    TimeToLiveInSeconds: int = None,
) -> Dict[str, Any]:
```

### Client().send_invitation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L548)

```python
def send_invitation(UserArn: str = None) -> Dict[str, Any]:
```

### Client().start_device_sync

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L552)

```python
def start_device_sync(
    Features: List[Any],
    RoomArn: str = None,
    DeviceArn: str = None,
) -> Dict[str, Any]:
```

### Client().start_smart_home_appliance_discovery

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L558)

```python
def start_smart_home_appliance_discovery(RoomArn: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L562)

```python
def tag_resource(Arn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L566)

```python
def untag_resource(Arn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_address_book

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L570)

```python
def update_address_book(
    AddressBookArn: str,
    Name: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().update_business_report_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L576)

```python
def update_business_report_schedule(
    ScheduleArn: str,
    S3BucketName: str = None,
    S3KeyPrefix: str = None,
    Format: str = None,
    ScheduleName: str = None,
    Recurrence: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_conference_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L588)

```python
def update_conference_provider(
    ConferenceProviderArn: str,
    ConferenceProviderType: str,
    MeetingSetting: Dict[str, Any],
    IPDialIn: Dict[str, Any] = None,
    PSTNDialIn: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_contact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L599)

```python
def update_contact(
    ContactArn: str,
    DisplayName: str = None,
    FirstName: str = None,
    LastName: str = None,
    PhoneNumber: str = None,
    PhoneNumbers: List[Any] = None,
    SipAddresses: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L612)

```python
def update_device(
    DeviceArn: str = None,
    DeviceName: str = None,
) -> Dict[str, Any]:
```

### Client().update_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L618)

```python
def update_gateway(
    GatewayArn: str,
    Name: str = None,
    Description: str = None,
    SoftwareVersion: str = None,
) -> Dict[str, Any]:
```

### Client().update_gateway_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L628)

```python
def update_gateway_group(
    GatewayGroupArn: str,
    Name: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().update_network_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L634)

```python
def update_network_profile(
    NetworkProfileArn: str,
    NetworkProfileName: str = None,
    Description: str = None,
    CurrentPassword: str = None,
    NextPassword: str = None,
    CertificateAuthorityArn: str = None,
    TrustAnchors: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L647)

```python
def update_profile(
    ProfileArn: str = None,
    ProfileName: str = None,
    IsDefault: bool = None,
    Timezone: str = None,
    Address: str = None,
    DistanceUnit: str = None,
    TemperatureUnit: str = None,
    WakeWord: str = None,
    Locale: str = None,
    SetupModeDisabled: bool = None,
    MaxVolumeLimit: int = None,
    PSTNEnabled: bool = None,
) -> Dict[str, Any]:
```

### Client().update_room

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L665)

```python
def update_room(
    RoomArn: str = None,
    RoomName: str = None,
    Description: str = None,
    ProviderCalendarId: str = None,
    ProfileArn: str = None,
) -> Dict[str, Any]:
```

### Client().update_skill_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/client.py#L676)

```python
def update_skill_group(
    SkillGroupArn: str = None,
    SkillGroupName: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```
