from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class BundleTaskComplete(Waiter):
    def wait(
        self,
        BundleIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ConversionTaskCancelled(Waiter):
    def wait(
        self,
        ConversionTaskIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ConversionTaskCompleted(Waiter):
    def wait(
        self,
        ConversionTaskIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ConversionTaskDeleted(Waiter):
    def wait(
        self,
        ConversionTaskIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class CustomerGatewayAvailable(Waiter):
    def wait(
        self,
        CustomerGatewayIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ExportTaskCancelled(Waiter):
    def wait(
        self,
        ExportTaskIds: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ExportTaskCompleted(Waiter):
    def wait(
        self,
        ExportTaskIds: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ImageAvailable(Waiter):
    def wait(
        self,
        ExecutableUsers: Optional[List] = None,
        Filters: Optional[List] = None,
        ImageIds: Optional[List] = None,
        Owners: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ImageExists(Waiter):
    def wait(
        self,
        ExecutableUsers: Optional[List] = None,
        Filters: Optional[List] = None,
        ImageIds: Optional[List] = None,
        Owners: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class InstanceExists(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class InstanceRunning(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class InstanceStatusOk(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
        IncludeAllInstances: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class InstanceStopped(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class InstanceTerminated(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class KeyPairExists(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        KeyNames: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class NatGatewayAvailable(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NatGatewayIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class NetworkInterfaceAvailable(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NetworkInterfaceIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class PasswordDataAvailable(Waiter):
    def wait(
        self,
        InstanceId: str,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class SnapshotCompleted(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        OwnerIds: Optional[List] = None,
        RestorableByUserIds: Optional[List] = None,
        SnapshotIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class SpotInstanceRequestFulfilled(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        SpotInstanceRequestIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class SubnetAvailable(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        SubnetIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class SystemStatusOk(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
        IncludeAllInstances: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class VolumeAvailable(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        VolumeIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class VolumeDeleted(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        VolumeIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class VolumeInUse(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        VolumeIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class VpcAvailable(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        VpcIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class VpcExists(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        VpcIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class VpcPeeringConnectionDeleted(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        VpcPeeringConnectionIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class VpcPeeringConnectionExists(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        VpcPeeringConnectionIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class VpnConnectionAvailable(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        VpnConnectionIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class VpnConnectionDeleted(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        VpnConnectionIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

