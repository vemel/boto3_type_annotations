# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.medialive.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Medialive](index.md#medialive) / Paginator
    - [DescribeSchedule](#describeschedule)
        - [DescribeSchedule().paginate](#describeschedulepaginate)
    - [ListChannels](#listchannels)
        - [ListChannels().paginate](#listchannelspaginate)
    - [ListInputSecurityGroups](#listinputsecuritygroups)
        - [ListInputSecurityGroups().paginate](#listinputsecuritygroupspaginate)
    - [ListInputs](#listinputs)
        - [ListInputs().paginate](#listinputspaginate)
    - [ListOfferings](#listofferings)
        - [ListOfferings().paginate](#listofferingspaginate)
    - [ListReservations](#listreservations)
        - [ListReservations().paginate](#listreservationspaginate)

## DescribeSchedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L9)

```python
class DescribeSchedule(Paginator):
```

### DescribeSchedule().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L12)

```python
def paginate(
    ChannelId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListChannels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L18)

```python
class ListChannels(Paginator):
```

### ListChannels().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L21)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListInputSecurityGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L25)

```python
class ListInputSecurityGroups(Paginator):
```

### ListInputSecurityGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L28)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListInputs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L32)

```python
class ListInputs(Paginator):
```

### ListInputs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L35)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListOfferings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L39)

```python
class ListOfferings(Paginator):
```

### ListOfferings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L42)

```python
def paginate(
    ChannelClass: str = None,
    ChannelConfiguration: str = None,
    Codec: str = None,
    MaximumBitrate: str = None,
    MaximumFramerate: str = None,
    Resolution: str = None,
    ResourceType: str = None,
    SpecialFeature: str = None,
    VideoQuality: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListReservations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L58)

```python
class ListReservations(Paginator):
```

### ListReservations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/paginator.py#L61)

```python
def paginate(
    ChannelClass: str = None,
    Codec: str = None,
    MaximumBitrate: str = None,
    MaximumFramerate: str = None,
    Resolution: str = None,
    ResourceType: str = None,
    SpecialFeature: str = None,
    VideoQuality: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
