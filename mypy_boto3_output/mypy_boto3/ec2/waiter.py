from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.waiter import Waiter


class BundleTaskComplete(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        BundleIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ConversionTaskCancelled(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ConversionTaskIds: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ConversionTaskCompleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ConversionTaskIds: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ConversionTaskDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ConversionTaskIds: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class CustomerGatewayAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        CustomerGatewayIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ExportTaskCancelled(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, ExportTaskIds: List[Any] = None, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass


class ExportTaskCompleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, ExportTaskIds: List[Any] = None, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass


class ImageAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ExecutableUsers: List[Any] = None,
        Filters: List[Any] = None,
        ImageIds: List[Any] = None,
        Owners: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class ImageExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ExecutableUsers: List[Any] = None,
        Filters: List[Any] = None,
        ImageIds: List[Any] = None,
        Owners: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        InstanceIds: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceRunning(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        InstanceIds: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceStatusOk(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        InstanceIds: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceStopped(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        InstanceIds: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class InstanceTerminated(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        InstanceIds: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class KeyPairExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        KeyNames: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class NatGatewayAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NatGatewayIds: List[Any] = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class NetworkInterfaceAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class PasswordDataAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, InstanceId: str, DryRun: bool = None, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass


class SnapshotCompleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[Any] = None,
        RestorableByUserIds: List[Any] = None,
        SnapshotIds: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class SpotInstanceRequestFulfilled(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class SubnetAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        SubnetIds: List[Any] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class SystemStatusOk(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        InstanceIds: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class VolumeAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        VolumeIds: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class VolumeDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        VolumeIds: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class VolumeInUse(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        VolumeIds: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class VpcAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        VpcIds: List[Any] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class VpcExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        VpcIds: List[Any] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class VpcPeeringConnectionDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class VpcPeeringConnectionExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class VpnConnectionAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        VpnConnectionIds: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class VpnConnectionDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        Filters: List[Any] = None,
        VpnConnectionIds: List[Any] = None,
        DryRun: bool = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
