# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ec2.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ec2](index.md#ec2) / Waiter
    - [BundleTaskComplete](#bundletaskcomplete)
        - [BundleTaskComplete().wait](#bundletaskcompletewait)
    - [ConversionTaskCancelled](#conversiontaskcancelled)
        - [ConversionTaskCancelled().wait](#conversiontaskcancelledwait)
    - [ConversionTaskCompleted](#conversiontaskcompleted)
        - [ConversionTaskCompleted().wait](#conversiontaskcompletedwait)
    - [ConversionTaskDeleted](#conversiontaskdeleted)
        - [ConversionTaskDeleted().wait](#conversiontaskdeletedwait)
    - [CustomerGatewayAvailable](#customergatewayavailable)
        - [CustomerGatewayAvailable().wait](#customergatewayavailablewait)
    - [ExportTaskCancelled](#exporttaskcancelled)
        - [ExportTaskCancelled().wait](#exporttaskcancelledwait)
    - [ExportTaskCompleted](#exporttaskcompleted)
        - [ExportTaskCompleted().wait](#exporttaskcompletedwait)
    - [ImageAvailable](#imageavailable)
        - [ImageAvailable().wait](#imageavailablewait)
    - [ImageExists](#imageexists)
        - [ImageExists().wait](#imageexistswait)
    - [InstanceExists](#instanceexists)
        - [InstanceExists().wait](#instanceexistswait)
    - [InstanceRunning](#instancerunning)
        - [InstanceRunning().wait](#instancerunningwait)
    - [InstanceStatusOk](#instancestatusok)
        - [InstanceStatusOk().wait](#instancestatusokwait)
    - [InstanceStopped](#instancestopped)
        - [InstanceStopped().wait](#instancestoppedwait)
    - [InstanceTerminated](#instanceterminated)
        - [InstanceTerminated().wait](#instanceterminatedwait)
    - [KeyPairExists](#keypairexists)
        - [KeyPairExists().wait](#keypairexistswait)
    - [NatGatewayAvailable](#natgatewayavailable)
        - [NatGatewayAvailable().wait](#natgatewayavailablewait)
    - [NetworkInterfaceAvailable](#networkinterfaceavailable)
        - [NetworkInterfaceAvailable().wait](#networkinterfaceavailablewait)
    - [PasswordDataAvailable](#passworddataavailable)
        - [PasswordDataAvailable().wait](#passworddataavailablewait)
    - [SnapshotCompleted](#snapshotcompleted)
        - [SnapshotCompleted().wait](#snapshotcompletedwait)
    - [SpotInstanceRequestFulfilled](#spotinstancerequestfulfilled)
        - [SpotInstanceRequestFulfilled().wait](#spotinstancerequestfulfilledwait)
    - [SubnetAvailable](#subnetavailable)
        - [SubnetAvailable().wait](#subnetavailablewait)
    - [SystemStatusOk](#systemstatusok)
        - [SystemStatusOk().wait](#systemstatusokwait)
    - [VolumeAvailable](#volumeavailable)
        - [VolumeAvailable().wait](#volumeavailablewait)
    - [VolumeDeleted](#volumedeleted)
        - [VolumeDeleted().wait](#volumedeletedwait)
    - [VolumeInUse](#volumeinuse)
        - [VolumeInUse().wait](#volumeinusewait)
    - [VpcAvailable](#vpcavailable)
        - [VpcAvailable().wait](#vpcavailablewait)
    - [VpcExists](#vpcexists)
        - [VpcExists().wait](#vpcexistswait)
    - [VpcPeeringConnectionDeleted](#vpcpeeringconnectiondeleted)
        - [VpcPeeringConnectionDeleted().wait](#vpcpeeringconnectiondeletedwait)
    - [VpcPeeringConnectionExists](#vpcpeeringconnectionexists)
        - [VpcPeeringConnectionExists().wait](#vpcpeeringconnectionexistswait)
    - [VpnConnectionAvailable](#vpnconnectionavailable)
        - [VpnConnectionAvailable().wait](#vpnconnectionavailablewait)
    - [VpnConnectionDeleted](#vpnconnectiondeleted)
        - [VpnConnectionDeleted().wait](#vpnconnectiondeletedwait)

## BundleTaskComplete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L10)

```python
class BundleTaskComplete(Waiter):
```

### BundleTaskComplete().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L13)

```python
def wait(
    BundleIds: List[Any] = None,
    Filters: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ConversionTaskCancelled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L23)

```python
class ConversionTaskCancelled(Waiter):
```

### ConversionTaskCancelled().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L26)

```python
def wait(
    ConversionTaskIds: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ConversionTaskCompleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L35)

```python
class ConversionTaskCompleted(Waiter):
```

### ConversionTaskCompleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L38)

```python
def wait(
    ConversionTaskIds: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ConversionTaskDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L47)

```python
class ConversionTaskDeleted(Waiter):
```

### ConversionTaskDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L50)

```python
def wait(
    ConversionTaskIds: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## CustomerGatewayAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L59)

```python
class CustomerGatewayAvailable(Waiter):
```

### CustomerGatewayAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L62)

```python
def wait(
    CustomerGatewayIds: List[Any] = None,
    Filters: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ExportTaskCancelled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L72)

```python
class ExportTaskCancelled(Waiter):
```

### ExportTaskCancelled().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L75)

```python
def wait(
    ExportTaskIds: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ExportTaskCompleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L81)

```python
class ExportTaskCompleted(Waiter):
```

### ExportTaskCompleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L84)

```python
def wait(
    ExportTaskIds: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ImageAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L90)

```python
class ImageAvailable(Waiter):
```

### ImageAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L93)

```python
def wait(
    ExecutableUsers: List[Any] = None,
    Filters: List[Any] = None,
    ImageIds: List[Any] = None,
    Owners: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ImageExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L105)

```python
class ImageExists(Waiter):
```

### ImageExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L108)

```python
def wait(
    ExecutableUsers: List[Any] = None,
    Filters: List[Any] = None,
    ImageIds: List[Any] = None,
    Owners: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L120)

```python
class InstanceExists(Waiter):
```

### InstanceExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L123)

```python
def wait(
    Filters: List[Any] = None,
    InstanceIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceRunning

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L135)

```python
class InstanceRunning(Waiter):
```

### InstanceRunning().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L138)

```python
def wait(
    Filters: List[Any] = None,
    InstanceIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceStatusOk

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L150)

```python
class InstanceStatusOk(Waiter):
```

### InstanceStatusOk().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L153)

```python
def wait(
    Filters: List[Any] = None,
    InstanceIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
    IncludeAllInstances: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceStopped

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L166)

```python
class InstanceStopped(Waiter):
```

### InstanceStopped().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L169)

```python
def wait(
    Filters: List[Any] = None,
    InstanceIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceTerminated

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L181)

```python
class InstanceTerminated(Waiter):
```

### InstanceTerminated().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L184)

```python
def wait(
    Filters: List[Any] = None,
    InstanceIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## KeyPairExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L196)

```python
class KeyPairExists(Waiter):
```

### KeyPairExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L199)

```python
def wait(
    Filters: List[Any] = None,
    KeyNames: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## NatGatewayAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L209)

```python
class NatGatewayAvailable(Waiter):
```

### NatGatewayAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L212)

```python
def wait(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NatGatewayIds: List[Any] = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## NetworkInterfaceAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L223)

```python
class NetworkInterfaceAvailable(Waiter):
```

### NetworkInterfaceAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L226)

```python
def wait(
    Filters: List[Any] = None,
    DryRun: bool = None,
    NetworkInterfaceIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## PasswordDataAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L238)

```python
class PasswordDataAvailable(Waiter):
```

### PasswordDataAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L241)

```python
def wait(
    InstanceId: str,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## SnapshotCompleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L247)

```python
class SnapshotCompleted(Waiter):
```

### SnapshotCompleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L250)

```python
def wait(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    OwnerIds: List[Any] = None,
    RestorableByUserIds: List[Any] = None,
    SnapshotIds: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## SpotInstanceRequestFulfilled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L264)

```python
class SpotInstanceRequestFulfilled(Waiter):
```

### SpotInstanceRequestFulfilled().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L267)

```python
def wait(
    Filters: List[Any] = None,
    DryRun: bool = None,
    SpotInstanceRequestIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## SubnetAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L279)

```python
class SubnetAvailable(Waiter):
```

### SubnetAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L282)

```python
def wait(
    Filters: List[Any] = None,
    SubnetIds: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## SystemStatusOk

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L294)

```python
class SystemStatusOk(Waiter):
```

### SystemStatusOk().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L297)

```python
def wait(
    Filters: List[Any] = None,
    InstanceIds: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
    IncludeAllInstances: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## VolumeAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L310)

```python
class VolumeAvailable(Waiter):
```

### VolumeAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L313)

```python
def wait(
    Filters: List[Any] = None,
    VolumeIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## VolumeDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L325)

```python
class VolumeDeleted(Waiter):
```

### VolumeDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L328)

```python
def wait(
    Filters: List[Any] = None,
    VolumeIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## VolumeInUse

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L340)

```python
class VolumeInUse(Waiter):
```

### VolumeInUse().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L343)

```python
def wait(
    Filters: List[Any] = None,
    VolumeIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## VpcAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L355)

```python
class VpcAvailable(Waiter):
```

### VpcAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L358)

```python
def wait(
    Filters: List[Any] = None,
    VpcIds: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## VpcExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L370)

```python
class VpcExists(Waiter):
```

### VpcExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L373)

```python
def wait(
    Filters: List[Any] = None,
    VpcIds: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## VpcPeeringConnectionDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L385)

```python
class VpcPeeringConnectionDeleted(Waiter):
```

### VpcPeeringConnectionDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L388)

```python
def wait(
    Filters: List[Any] = None,
    DryRun: bool = None,
    VpcPeeringConnectionIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## VpcPeeringConnectionExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L400)

```python
class VpcPeeringConnectionExists(Waiter):
```

### VpcPeeringConnectionExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L403)

```python
def wait(
    Filters: List[Any] = None,
    DryRun: bool = None,
    VpcPeeringConnectionIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## VpnConnectionAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L415)

```python
class VpnConnectionAvailable(Waiter):
```

### VpnConnectionAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L418)

```python
def wait(
    Filters: List[Any] = None,
    VpnConnectionIds: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## VpnConnectionDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L428)

```python
class VpnConnectionDeleted(Waiter):
```

### VpnConnectionDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/waiter.py#L431)

```python
def wait(
    Filters: List[Any] = None,
    VpnConnectionIds: List[Any] = None,
    DryRun: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
