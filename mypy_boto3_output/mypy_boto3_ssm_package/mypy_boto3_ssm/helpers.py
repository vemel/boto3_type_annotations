"Helper functions for ssm service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_ssm.client import Client
from mypy_boto3_ssm.paginator import (
    DescribeActivationsPaginator,
    DescribeAssociationExecutionTargetsPaginator,
    DescribeAssociationExecutionsPaginator,
    DescribeAutomationExecutionsPaginator,
    DescribeAutomationStepExecutionsPaginator,
    DescribeAvailablePatchesPaginator,
    DescribeEffectiveInstanceAssociationsPaginator,
    DescribeEffectivePatchesForPatchBaselinePaginator,
    DescribeInstanceAssociationsStatusPaginator,
    DescribeInstanceInformationPaginator,
    DescribeInstancePatchStatesForPatchGroupPaginator,
    DescribeInstancePatchStatesPaginator,
    DescribeInstancePatchesPaginator,
    DescribeInventoryDeletionsPaginator,
    DescribeMaintenanceWindowExecutionTaskInvocationsPaginator,
    DescribeMaintenanceWindowExecutionTasksPaginator,
    DescribeMaintenanceWindowExecutionsPaginator,
    DescribeMaintenanceWindowSchedulePaginator,
    DescribeMaintenanceWindowTargetsPaginator,
    DescribeMaintenanceWindowTasksPaginator,
    DescribeMaintenanceWindowsForTargetPaginator,
    DescribeMaintenanceWindowsPaginator,
    DescribeParametersPaginator,
    DescribePatchBaselinesPaginator,
    DescribePatchGroupsPaginator,
    DescribeSessionsPaginator,
    GetInventoryPaginator,
    GetInventorySchemaPaginator,
    GetParameterHistoryPaginator,
    GetParametersByPathPaginator,
    ListAssociationVersionsPaginator,
    ListAssociationsPaginator,
    ListCommandInvocationsPaginator,
    ListCommandsPaginator,
    ListComplianceItemsPaginator,
    ListComplianceSummariesPaginator,
    ListDocumentVersionsPaginator,
    ListDocumentsPaginator,
    ListResourceComplianceSummariesPaginator,
    ListResourceDataSyncPaginator,
)

# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_client(
    session: Session = None,
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Client:
    """
    Equivalent of `boto3.client('ssm')`, returns a correct type.
    """
    kwargs: Dict[str, Any] = {}
    if region_name is not None:
        kwargs["region_name"] = region_name
    if api_version is not None:
        kwargs["api_version"] = api_version
    if use_ssl is not None:
        kwargs["use_ssl"] = use_ssl
    if verify is not None:
        kwargs["verify"] = verify
    if endpoint_url is not None:
        kwargs["endpoint_url"] = endpoint_url
    if aws_access_key_id is not None:
        kwargs["aws_access_key_id"] = aws_access_key_id
    if aws_secret_access_key is not None:
        kwargs["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token is not None:
        kwargs["aws_session_token"] = aws_session_token
    if config is not None:
        kwargs["config"] = config
    if session is not None:
        return session.client("ssm", **kwargs)
    return boto3.client("ssm", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_activations_paginator(client: Client) -> DescribeActivationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_activations')`, returns a correct type.
    """
    return client.get_paginator("describe_activations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_association_execution_targets_paginator(
    client: Client,
) -> DescribeAssociationExecutionTargetsPaginator:
    """
    Equivalent of `client.get_paginator('describe_association_execution_targets')`, returns a correct type.
    """
    return client.get_paginator("describe_association_execution_targets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_association_executions_paginator(
    client: Client,
) -> DescribeAssociationExecutionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_association_executions')`, returns a correct type.
    """
    return client.get_paginator("describe_association_executions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_automation_executions_paginator(
    client: Client,
) -> DescribeAutomationExecutionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_automation_executions')`, returns a correct type.
    """
    return client.get_paginator("describe_automation_executions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_automation_step_executions_paginator(
    client: Client,
) -> DescribeAutomationStepExecutionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_automation_step_executions')`, returns a correct type.
    """
    return client.get_paginator("describe_automation_step_executions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_available_patches_paginator(
    client: Client,
) -> DescribeAvailablePatchesPaginator:
    """
    Equivalent of `client.get_paginator('describe_available_patches')`, returns a correct type.
    """
    return client.get_paginator("describe_available_patches")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_effective_instance_associations_paginator(
    client: Client,
) -> DescribeEffectiveInstanceAssociationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_effective_instance_associations')`, returns a correct type.
    """
    return client.get_paginator("describe_effective_instance_associations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_effective_patches_for_patch_baseline_paginator(
    client: Client,
) -> DescribeEffectivePatchesForPatchBaselinePaginator:
    """
    Equivalent of `client.get_paginator('describe_effective_patches_for_patch_baseline')`, returns a correct type.
    """
    return client.get_paginator("describe_effective_patches_for_patch_baseline")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_instance_associations_status_paginator(
    client: Client,
) -> DescribeInstanceAssociationsStatusPaginator:
    """
    Equivalent of `client.get_paginator('describe_instance_associations_status')`, returns a correct type.
    """
    return client.get_paginator("describe_instance_associations_status")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_instance_information_paginator(
    client: Client,
) -> DescribeInstanceInformationPaginator:
    """
    Equivalent of `client.get_paginator('describe_instance_information')`, returns a correct type.
    """
    return client.get_paginator("describe_instance_information")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_instance_patch_states_paginator(
    client: Client,
) -> DescribeInstancePatchStatesPaginator:
    """
    Equivalent of `client.get_paginator('describe_instance_patch_states')`, returns a correct type.
    """
    return client.get_paginator("describe_instance_patch_states")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_instance_patch_states_for_patch_group_paginator(
    client: Client,
) -> DescribeInstancePatchStatesForPatchGroupPaginator:
    """
    Equivalent of `client.get_paginator('describe_instance_patch_states_for_patch_group')`, returns a correct type.
    """
    return client.get_paginator("describe_instance_patch_states_for_patch_group")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_instance_patches_paginator(
    client: Client,
) -> DescribeInstancePatchesPaginator:
    """
    Equivalent of `client.get_paginator('describe_instance_patches')`, returns a correct type.
    """
    return client.get_paginator("describe_instance_patches")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_inventory_deletions_paginator(
    client: Client,
) -> DescribeInventoryDeletionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_inventory_deletions')`, returns a correct type.
    """
    return client.get_paginator("describe_inventory_deletions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_maintenance_window_execution_task_invocations_paginator(
    client: Client,
) -> DescribeMaintenanceWindowExecutionTaskInvocationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_maintenance_window_execution_task_invocations')`, returns a correct type.
    """
    return client.get_paginator(
        "describe_maintenance_window_execution_task_invocations"
    )


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_maintenance_window_execution_tasks_paginator(
    client: Client,
) -> DescribeMaintenanceWindowExecutionTasksPaginator:
    """
    Equivalent of `client.get_paginator('describe_maintenance_window_execution_tasks')`, returns a correct type.
    """
    return client.get_paginator("describe_maintenance_window_execution_tasks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_maintenance_window_executions_paginator(
    client: Client,
) -> DescribeMaintenanceWindowExecutionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_maintenance_window_executions')`, returns a correct type.
    """
    return client.get_paginator("describe_maintenance_window_executions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_maintenance_window_schedule_paginator(
    client: Client,
) -> DescribeMaintenanceWindowSchedulePaginator:
    """
    Equivalent of `client.get_paginator('describe_maintenance_window_schedule')`, returns a correct type.
    """
    return client.get_paginator("describe_maintenance_window_schedule")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_maintenance_window_targets_paginator(
    client: Client,
) -> DescribeMaintenanceWindowTargetsPaginator:
    """
    Equivalent of `client.get_paginator('describe_maintenance_window_targets')`, returns a correct type.
    """
    return client.get_paginator("describe_maintenance_window_targets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_maintenance_window_tasks_paginator(
    client: Client,
) -> DescribeMaintenanceWindowTasksPaginator:
    """
    Equivalent of `client.get_paginator('describe_maintenance_window_tasks')`, returns a correct type.
    """
    return client.get_paginator("describe_maintenance_window_tasks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_maintenance_windows_paginator(
    client: Client,
) -> DescribeMaintenanceWindowsPaginator:
    """
    Equivalent of `client.get_paginator('describe_maintenance_windows')`, returns a correct type.
    """
    return client.get_paginator("describe_maintenance_windows")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_maintenance_windows_for_target_paginator(
    client: Client,
) -> DescribeMaintenanceWindowsForTargetPaginator:
    """
    Equivalent of `client.get_paginator('describe_maintenance_windows_for_target')`, returns a correct type.
    """
    return client.get_paginator("describe_maintenance_windows_for_target")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_parameters_paginator(client: Client) -> DescribeParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_patch_baselines_paginator(
    client: Client,
) -> DescribePatchBaselinesPaginator:
    """
    Equivalent of `client.get_paginator('describe_patch_baselines')`, returns a correct type.
    """
    return client.get_paginator("describe_patch_baselines")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_patch_groups_paginator(client: Client) -> DescribePatchGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_patch_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_patch_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_sessions_paginator(client: Client) -> DescribeSessionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_sessions')`, returns a correct type.
    """
    return client.get_paginator("describe_sessions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_inventory_paginator(client: Client) -> GetInventoryPaginator:
    """
    Equivalent of `client.get_paginator('get_inventory')`, returns a correct type.
    """
    return client.get_paginator("get_inventory")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_inventory_schema_paginator(client: Client) -> GetInventorySchemaPaginator:
    """
    Equivalent of `client.get_paginator('get_inventory_schema')`, returns a correct type.
    """
    return client.get_paginator("get_inventory_schema")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_parameter_history_paginator(client: Client) -> GetParameterHistoryPaginator:
    """
    Equivalent of `client.get_paginator('get_parameter_history')`, returns a correct type.
    """
    return client.get_paginator("get_parameter_history")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_parameters_by_path_paginator(
    client: Client,
) -> GetParametersByPathPaginator:
    """
    Equivalent of `client.get_paginator('get_parameters_by_path')`, returns a correct type.
    """
    return client.get_paginator("get_parameters_by_path")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_association_versions_paginator(
    client: Client,
) -> ListAssociationVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_association_versions')`, returns a correct type.
    """
    return client.get_paginator("list_association_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_associations_paginator(client: Client) -> ListAssociationsPaginator:
    """
    Equivalent of `client.get_paginator('list_associations')`, returns a correct type.
    """
    return client.get_paginator("list_associations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_command_invocations_paginator(
    client: Client,
) -> ListCommandInvocationsPaginator:
    """
    Equivalent of `client.get_paginator('list_command_invocations')`, returns a correct type.
    """
    return client.get_paginator("list_command_invocations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_commands_paginator(client: Client) -> ListCommandsPaginator:
    """
    Equivalent of `client.get_paginator('list_commands')`, returns a correct type.
    """
    return client.get_paginator("list_commands")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_compliance_items_paginator(client: Client) -> ListComplianceItemsPaginator:
    """
    Equivalent of `client.get_paginator('list_compliance_items')`, returns a correct type.
    """
    return client.get_paginator("list_compliance_items")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_compliance_summaries_paginator(
    client: Client,
) -> ListComplianceSummariesPaginator:
    """
    Equivalent of `client.get_paginator('list_compliance_summaries')`, returns a correct type.
    """
    return client.get_paginator("list_compliance_summaries")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_document_versions_paginator(
    client: Client,
) -> ListDocumentVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_document_versions')`, returns a correct type.
    """
    return client.get_paginator("list_document_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_documents_paginator(client: Client) -> ListDocumentsPaginator:
    """
    Equivalent of `client.get_paginator('list_documents')`, returns a correct type.
    """
    return client.get_paginator("list_documents")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resource_compliance_summaries_paginator(
    client: Client,
) -> ListResourceComplianceSummariesPaginator:
    """
    Equivalent of `client.get_paginator('list_resource_compliance_summaries')`, returns a correct type.
    """
    return client.get_paginator("list_resource_compliance_summaries")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resource_data_sync_paginator(
    client: Client,
) -> ListResourceDataSyncPaginator:
    """
    Equivalent of `client.get_paginator('list_resource_data_sync')`, returns a correct type.
    """
    return client.get_paginator("list_resource_data_sync")
