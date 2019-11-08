# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.alexaforbusiness.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Alexaforbusiness](index.md#alexaforbusiness) / Paginator
    - [ListBusinessReportSchedules](#listbusinessreportschedules)
        - [ListBusinessReportSchedules().paginate](#listbusinessreportschedulespaginate)
    - [ListConferenceProviders](#listconferenceproviders)
        - [ListConferenceProviders().paginate](#listconferenceproviderspaginate)
    - [ListDeviceEvents](#listdeviceevents)
        - [ListDeviceEvents().paginate](#listdeviceeventspaginate)
    - [ListSkills](#listskills)
        - [ListSkills().paginate](#listskillspaginate)
    - [ListSkillsStoreCategories](#listskillsstorecategories)
        - [ListSkillsStoreCategories().paginate](#listskillsstorecategoriespaginate)
    - [ListSkillsStoreSkillsByCategory](#listskillsstoreskillsbycategory)
        - [ListSkillsStoreSkillsByCategory().paginate](#listskillsstoreskillsbycategorypaginate)
    - [ListSmartHomeAppliances](#listsmarthomeappliances)
        - [ListSmartHomeAppliances().paginate](#listsmarthomeappliancespaginate)
    - [ListTags](#listtags)
        - [ListTags().paginate](#listtagspaginate)
    - [SearchDevices](#searchdevices)
        - [SearchDevices().paginate](#searchdevicespaginate)
    - [SearchProfiles](#searchprofiles)
        - [SearchProfiles().paginate](#searchprofilespaginate)
    - [SearchRooms](#searchrooms)
        - [SearchRooms().paginate](#searchroomspaginate)
    - [SearchSkillGroups](#searchskillgroups)
        - [SearchSkillGroups().paginate](#searchskillgroupspaginate)
    - [SearchUsers](#searchusers)
        - [SearchUsers().paginate](#searchuserspaginate)

## ListBusinessReportSchedules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L10)

```python
class ListBusinessReportSchedules(Paginator):
```

### ListBusinessReportSchedules().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L13)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListConferenceProviders

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L17)

```python
class ListConferenceProviders(Paginator):
```

### ListConferenceProviders().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L20)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListDeviceEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L24)

```python
class ListDeviceEvents(Paginator):
```

### ListDeviceEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L27)

```python
def paginate(
    DeviceArn: str,
    EventType: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSkills

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L36)

```python
class ListSkills(Paginator):
```

### ListSkills().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L39)

```python
def paginate(
    SkillGroupArn: str = None,
    EnablementType: str = None,
    SkillType: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSkillsStoreCategories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L49)

```python
class ListSkillsStoreCategories(Paginator):
```

### ListSkillsStoreCategories().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L52)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListSkillsStoreSkillsByCategory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L56)

```python
class ListSkillsStoreSkillsByCategory(Paginator):
```

### ListSkillsStoreSkillsByCategory().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L59)

```python
def paginate(
    CategoryId: int,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSmartHomeAppliances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L65)

```python
class ListSmartHomeAppliances(Paginator):
```

### ListSmartHomeAppliances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L68)

```python
def paginate(
    RoomArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L74)

```python
class ListTags(Paginator):
```

### ListTags().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L77)

```python
def paginate(
    Arn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## SearchDevices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L83)

```python
class SearchDevices(Paginator):
```

### SearchDevices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L86)

```python
def paginate(
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## SearchProfiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L95)

```python
class SearchProfiles(Paginator):
```

### SearchProfiles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L98)

```python
def paginate(
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## SearchRooms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L107)

```python
class SearchRooms(Paginator):
```

### SearchRooms().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L110)

```python
def paginate(
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## SearchSkillGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L119)

```python
class SearchSkillGroups(Paginator):
```

### SearchSkillGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L122)

```python
def paginate(
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## SearchUsers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L131)

```python
class SearchUsers(Paginator):
```

### SearchUsers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/alexaforbusiness/paginator.py#L134)

```python
def paginate(
    Filters: List[Any] = None,
    SortCriteria: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
