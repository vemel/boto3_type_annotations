from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_instance_fleet(
        self,
        ClusterId: str,
        InstanceFleet: Dict,
    ) -> Dict:
        pass


    def add_instance_groups(
        self,
        InstanceGroups: List,
        JobFlowId: str,
    ) -> Dict:
        pass


    def add_job_flow_steps(
        self,
        JobFlowId: str,
        Steps: List,
    ) -> Dict:
        pass


    def add_tags(
        self,
        ResourceId: str,
        Tags: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_steps(
        self,
        ClusterId: Optional[str] = None,
        StepIds: Optional[List] = None,
    ) -> Dict:
        pass


    def create_security_configuration(
        self,
        Name: str,
        SecurityConfiguration: str,
    ) -> Dict:
        pass


    def delete_security_configuration(
        self,
        Name: str,
    ) -> Dict:
        pass


    def describe_cluster(
        self,
        ClusterId: str,
    ) -> Dict:
        pass


    def describe_job_flows(
        self,
        CreatedAfter: Optional[datetime] = None,
        CreatedBefore: Optional[datetime] = None,
        JobFlowIds: Optional[List] = None,
        JobFlowStates: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_security_configuration(
        self,
        Name: str,
    ) -> Dict:
        pass


    def describe_step(
        self,
        ClusterId: str,
        StepId: str,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_block_public_access_configuration(
        self,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_bootstrap_actions(
        self,
        ClusterId: str,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_clusters(
        self,
        CreatedAfter: Optional[datetime] = None,
        CreatedBefore: Optional[datetime] = None,
        ClusterStates: Optional[List] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_instance_fleets(
        self,
        ClusterId: str,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_instance_groups(
        self,
        ClusterId: str,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_instances(
        self,
        ClusterId: str,
        InstanceGroupId: Optional[str] = None,
        InstanceGroupTypes: Optional[List] = None,
        InstanceFleetId: Optional[str] = None,
        InstanceFleetType: Optional[str] = None,
        InstanceStates: Optional[List] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_security_configurations(
        self,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_steps(
        self,
        ClusterId: str,
        StepStates: Optional[List] = None,
        StepIds: Optional[List] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_instance_fleet(
        self,
        ClusterId: str,
        InstanceFleet: Dict,
    ):
        pass


    def modify_instance_groups(
        self,
        ClusterId: Optional[str] = None,
        InstanceGroups: Optional[List] = None,
    ):
        pass


    def put_auto_scaling_policy(
        self,
        ClusterId: str,
        InstanceGroupId: str,
        AutoScalingPolicy: Dict,
    ) -> Dict:
        pass


    def put_block_public_access_configuration(
        self,
        BlockPublicAccessConfiguration: Dict,
    ) -> Dict:
        pass


    def remove_auto_scaling_policy(
        self,
        ClusterId: str,
        InstanceGroupId: str,
    ) -> Dict:
        pass


    def remove_tags(
        self,
        ResourceId: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def run_job_flow(
        self,
        Name: str,
        Instances: Dict,
        LogUri: Optional[str] = None,
        AdditionalInfo: Optional[str] = None,
        AmiVersion: Optional[str] = None,
        ReleaseLabel: Optional[str] = None,
        Steps: Optional[List] = None,
        BootstrapActions: Optional[List] = None,
        SupportedProducts: Optional[List] = None,
        NewSupportedProducts: Optional[List] = None,
        Applications: Optional[List] = None,
        Configurations: Optional[List] = None,
        VisibleToAllUsers: Optional[bool] = None,
        JobFlowRole: Optional[str] = None,
        ServiceRole: Optional[str] = None,
        Tags: Optional[List] = None,
        SecurityConfiguration: Optional[str] = None,
        AutoScalingRole: Optional[str] = None,
        ScaleDownBehavior: Optional[str] = None,
        CustomAmiId: Optional[str] = None,
        EbsRootVolumeSize: Optional[int] = None,
        RepoUpgradeOnBoot: Optional[str] = None,
        KerberosAttributes: Optional[Dict] = None,
    ) -> Dict:
        pass


    def set_termination_protection(
        self,
        JobFlowIds: List,
        TerminationProtected: bool,
    ):
        pass


    def set_visible_to_all_users(
        self,
        JobFlowIds: List,
        VisibleToAllUsers: bool,
    ):
        pass


    def terminate_job_flows(
        self,
        JobFlowIds: List,
    ):
        pass

