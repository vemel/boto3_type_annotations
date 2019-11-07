from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeActivations(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeAssociationExecutionTargets(Paginator):
    def paginate(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeAssociationExecutions(Paginator):
    def paginate(
        self,
        AssociationId: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeAutomationExecutions(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeAutomationStepExecutions(Paginator):
    def paginate(
        self,
        AutomationExecutionId: str,
        Filters: Optional[List] = None,
        ReverseOrder: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeAvailablePatches(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEffectiveInstanceAssociations(Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEffectivePatchesForPatchBaseline(Paginator):
    def paginate(
        self,
        BaselineId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInstanceAssociationsStatus(Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInstanceInformation(Paginator):
    def paginate(
        self,
        InstanceInformationFilterList: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInstancePatchStates(Paginator):
    def paginate(
        self,
        InstanceIds: List,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInstancePatchStatesForPatchGroup(Paginator):
    def paginate(
        self,
        PatchGroup: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInstancePatches(Paginator):
    def paginate(
        self,
        InstanceId: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInventoryDeletions(Paginator):
    def paginate(
        self,
        DeletionId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMaintenanceWindowExecutionTaskInvocations(Paginator):
    def paginate(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMaintenanceWindowExecutionTasks(Paginator):
    def paginate(
        self,
        WindowExecutionId: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMaintenanceWindowExecutions(Paginator):
    def paginate(
        self,
        WindowId: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMaintenanceWindowSchedule(Paginator):
    def paginate(
        self,
        WindowId: Optional[str] = None,
        Targets: Optional[List] = None,
        ResourceType: Optional[str] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMaintenanceWindowTargets(Paginator):
    def paginate(
        self,
        WindowId: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMaintenanceWindowTasks(Paginator):
    def paginate(
        self,
        WindowId: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMaintenanceWindows(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMaintenanceWindowsForTarget(Paginator):
    def paginate(
        self,
        Targets: List,
        ResourceType: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeParameters(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        ParameterFilters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribePatchBaselines(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribePatchGroups(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSessions(Paginator):
    def paginate(
        self,
        State: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetInventory(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        Aggregators: Optional[List] = None,
        ResultAttributes: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetInventorySchema(Paginator):
    def paginate(
        self,
        TypeName: Optional[str] = None,
        Aggregator: Optional[bool] = None,
        SubType: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetParameterHistory(Paginator):
    def paginate(
        self,
        Name: str,
        WithDecryption: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetParametersByPath(Paginator):
    def paginate(
        self,
        Path: str,
        Recursive: Optional[bool] = None,
        ParameterFilters: Optional[List] = None,
        WithDecryption: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAssociationVersions(Paginator):
    def paginate(
        self,
        AssociationId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAssociations(Paginator):
    def paginate(
        self,
        AssociationFilterList: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListCommandInvocations(Paginator):
    def paginate(
        self,
        CommandId: Optional[str] = None,
        InstanceId: Optional[str] = None,
        Filters: Optional[List] = None,
        Details: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListCommands(Paginator):
    def paginate(
        self,
        CommandId: Optional[str] = None,
        InstanceId: Optional[str] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListComplianceItems(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        ResourceIds: Optional[List] = None,
        ResourceTypes: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListComplianceSummaries(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDocumentVersions(Paginator):
    def paginate(
        self,
        Name: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDocuments(Paginator):
    def paginate(
        self,
        DocumentFilterList: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListResourceComplianceSummaries(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListResourceDataSync(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

