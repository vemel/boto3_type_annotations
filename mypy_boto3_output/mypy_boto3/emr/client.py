from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_instance_fleet(
        self, ClusterId: str, InstanceFleet: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_instance_groups(
        self, InstanceGroups: List[Any], JobFlowId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_job_flow_steps(self, JobFlowId: str, Steps: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_tags(self, ResourceId: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_steps(
        self, ClusterId: str = None, StepIds: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_security_configuration(
        self, Name: str, SecurityConfiguration: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_security_configuration(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cluster(self, ClusterId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_job_flows(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        JobFlowIds: List[Any] = None,
        JobFlowStates: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_security_configuration(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_step(self, ClusterId: str, StepId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_block_public_access_configuration(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_bootstrap_actions(
        self, ClusterId: str, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_clusters(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        ClusterStates: List[Any] = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_instance_fleets(
        self, ClusterId: str, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_instance_groups(
        self, ClusterId: str, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_instances(
        self,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[Any] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: str = None,
        InstanceStates: List[Any] = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_security_configurations(self, Marker: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_steps(
        self,
        ClusterId: str,
        StepStates: List[Any] = None,
        StepIds: List[Any] = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_instance_fleet(
        self, ClusterId: str, InstanceFleet: Dict[str, Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def modify_instance_groups(
        self, ClusterId: str = None, InstanceGroups: List[Any] = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def put_auto_scaling_policy(
        self, ClusterId: str, InstanceGroupId: str, AutoScalingPolicy: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_block_public_access_configuration(
        self, BlockPublicAccessConfiguration: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_auto_scaling_policy(
        self, ClusterId: str, InstanceGroupId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags(self, ResourceId: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def run_job_flow(
        self,
        Name: str,
        Instances: Dict[str, Any],
        LogUri: str = None,
        AdditionalInfo: str = None,
        AmiVersion: str = None,
        ReleaseLabel: str = None,
        Steps: List[Any] = None,
        BootstrapActions: List[Any] = None,
        SupportedProducts: List[Any] = None,
        NewSupportedProducts: List[Any] = None,
        Applications: List[Any] = None,
        Configurations: List[Any] = None,
        VisibleToAllUsers: bool = None,
        JobFlowRole: str = None,
        ServiceRole: str = None,
        Tags: List[Any] = None,
        SecurityConfiguration: str = None,
        AutoScalingRole: str = None,
        ScaleDownBehavior: str = None,
        CustomAmiId: str = None,
        EbsRootVolumeSize: int = None,
        RepoUpgradeOnBoot: str = None,
        KerberosAttributes: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_termination_protection(
        self, JobFlowIds: List[Any], TerminationProtected: bool
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_visible_to_all_users(
        self, JobFlowIds: List[Any], VisibleToAllUsers: bool
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def terminate_job_flows(self, JobFlowIds: List[Any]) -> None:
        pass
