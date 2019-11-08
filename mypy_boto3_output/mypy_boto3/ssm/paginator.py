from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeActivations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeAssociationExecutionTargets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeAssociationExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AssociationId: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeAutomationExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeAutomationStepExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AutomationExecutionId: str,
        Filters: List[Any] = None,
        ReverseOrder: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeAvailablePatches(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeEffectiveInstanceAssociations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, InstanceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeEffectivePatchesForPatchBaseline(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, BaselineId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeInstanceAssociationsStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, InstanceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeInstanceInformation(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        InstanceInformationFilterList: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeInstancePatchStates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, InstanceIds: List[Any], PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeInstancePatchStatesForPatchGroup(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        PatchGroup: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeInstancePatches(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        InstanceId: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeInventoryDeletions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DeletionId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeMaintenanceWindowExecutionTaskInvocations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMaintenanceWindowExecutionTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        WindowExecutionId: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMaintenanceWindowExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        WindowId: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMaintenanceWindowSchedule(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        WindowId: str = None,
        Targets: List[Any] = None,
        ResourceType: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMaintenanceWindowTargets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        WindowId: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMaintenanceWindowTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        WindowId: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMaintenanceWindows(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeMaintenanceWindowsForTarget(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Targets: List[Any],
        ResourceType: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        ParameterFilters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribePatchBaselines(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribePatchGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeSessions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        State: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetInventory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        Aggregators: List[Any] = None,
        ResultAttributes: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetInventorySchema(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TypeName: str = None,
        Aggregator: bool = None,
        SubType: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetParameterHistory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Name: str,
        WithDecryption: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetParametersByPath(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List[Any] = None,
        WithDecryption: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAssociationVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AssociationId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListAssociations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AssociationFilterList: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListCommandInvocations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List[Any] = None,
        Details: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListCommands(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListComplianceItems(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        ResourceIds: List[Any] = None,
        ResourceTypes: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListComplianceSummaries(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDocumentVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Name: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDocuments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DocumentFilterList: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListResourceComplianceSummaries(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListResourceDataSync(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
